"""Tests for the MQ REST session wrapper."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import TYPE_CHECKING

import pytest
from requests import RequestException

from pymqrest import session as session_module
from pymqrest.auth import BasicAuth, CertificateAuth, LTPAAuth
from pymqrest.exceptions import (
    MQRESTAuthError,
    MQRESTCommandError,
    MQRESTResponseError,
    MQRESTTransportError,
)
from pymqrest.mapping import MappingError
from pymqrest.mapping_data import MAPPING_DATA
from pymqrest.session import MQRESTSession, RequestsTransport, TransportResponse

if TYPE_CHECKING:
    from collections.abc import Mapping

REQUEST_EXCEPTION_MESSAGE = "boom"
STATUS_INTERNAL_SERVER_ERROR = 500
STATUS_CREATED = 201
TEST_PASSWORD = "pass"
TEST_DEPTH = 5


@dataclass(frozen=True)
class RecordedRequest:
    url: str
    payload: dict[str, object]
    headers: dict[str, str]
    timeout_seconds: float | None
    verify_tls: bool


class FakeTransport:
    def __init__(self, response: TransportResponse) -> None:
        self.response = response
        self.recorded_requests: list[RecordedRequest] = []

    def post_json(
        self,
        url: str,
        payload: Mapping[str, object],
        *,
        headers: Mapping[str, str],
        timeout_seconds: float | None,
        verify_tls: bool,
    ) -> TransportResponse:
        self.recorded_requests.append(
            RecordedRequest(
                url=url,
                payload=dict(payload),
                headers=dict(headers),
                timeout_seconds=timeout_seconds,
                verify_tls=verify_tls,
            ),
        )
        return self.response


def _build_session(
    response_payload: dict[str, object],
    *,
    mapping_strict: bool | None = None,
    mapping_overrides: dict[str, object] | None = None,
) -> tuple[MQRESTSession, FakeTransport]:
    response_text = json.dumps(response_payload)
    transport = FakeTransport(
        TransportResponse(status_code=200, text=response_text, headers={}),
    )
    kwargs: dict[str, object] = {
        "rest_base_url": "https://example.invalid/ibmmq/rest/v2",
        "qmgr_name": "QM1",
        "credentials": BasicAuth("user", TEST_PASSWORD),
        "transport": transport,
    }
    if mapping_strict is not None:
        kwargs["mapping_strict"] = mapping_strict
    if mapping_overrides is not None:
        kwargs["mapping_overrides"] = mapping_overrides
    session = MQRESTSession(**kwargs)  # type: ignore[arg-type]
    return session, transport


def test_qmgr_name_property_returns_configured_name() -> None:
    session, _ = _build_session({"overallCompletionCode": 0, "overallReasonCode": 0})
    assert session.qmgr_name == "QM1"


def test_display_qmgr_returns_first_object() -> None:
    response_payload = {
        "commandResponse": [
            {"completionCode": 0, "reasonCode": 0, "parameters": {"QMNAME": "QM1"}},
        ],
        "overallCompletionCode": 0,
        "overallReasonCode": 0,
    }
    session, _transport = _build_session(response_payload)

    result = session.display_qmgr()

    assert result == {"queue_manager_name": "QM1"}


def test_display_qmstatus_returns_first_object() -> None:
    response_payload = {
        "commandResponse": [
            {"completionCode": 0, "reasonCode": 0, "parameters": {"STATUS": "RUNNING"}},
        ],
        "overallCompletionCode": 0,
        "overallReasonCode": 0,
    }
    session, _transport = _build_session(response_payload)

    result = session.display_qmstatus()

    assert result == {"ha_status": "RUNNING"}


def test_display_qmstatus_returns_none_for_empty_response() -> None:
    response_payload = {
        "commandResponse": [],
        "overallCompletionCode": 0,
        "overallReasonCode": 0,
    }
    session, _transport = _build_session(response_payload)

    result = session.display_qmstatus()

    assert result is None


def test_display_cmdserv_returns_first_object() -> None:
    response_payload = {
        "commandResponse": [
            {"completionCode": 0, "reasonCode": 0, "parameters": {"STATE": "ACTIVE"}},
        ],
        "overallCompletionCode": 0,
        "overallReasonCode": 0,
    }
    session, _transport = _build_session(response_payload, mapping_strict=False)

    result = session.display_cmdserv()

    assert result == {"STATE": "ACTIVE"}


def test_display_cmdserv_returns_none_for_empty_response() -> None:
    response_payload = {
        "commandResponse": [],
        "overallCompletionCode": 0,
        "overallReasonCode": 0,
    }
    session, _transport = _build_session(response_payload)

    result = session.display_cmdserv()

    assert result is None


def test_display_queue_maps_parameters_and_response_parameters() -> None:
    response_payload = {
        "commandResponse": [
            {
                "completionCode": 0,
                "reasonCode": 0,
                "parameters": {"DEFPSIST": "NOTFIXED", "CURDEPTH": 5},
            },
        ],
        "overallCompletionCode": 0,
        "overallReasonCode": 0,
    }
    session, transport = _build_session(response_payload)

    result = session.display_queue(
        request_parameters={"default_persistence": "def"},
        response_parameters=["default_persistence", "current_queue_depth"],
    )

    recorded_request = transport.recorded_requests[0]
    assert recorded_request.payload["name"] == "*"
    assert recorded_request.payload["parameters"] == {"DEFPSIST": "DEF"}
    assert recorded_request.payload["responseParameters"] == ["DEFPSIST", "CURDEPTH"]
    assert result == [{"default_persistence": "not_fixed", "current_queue_depth": 5}]


def test_map_response_parameters_unknown_key_lenient() -> None:
    session, _transport = _build_session(
        {"commandResponse": [], "overallCompletionCode": 0, "overallReasonCode": 0},
        mapping_strict=False,
    )

    result = session._map_response_parameters("DISPLAY", "QUEUE", "queue", ["unknown_key"])  # noqa: SLF001

    assert result == ["unknown_key"]


def test_map_response_parameters_allows_macros() -> None:
    session, _transport = _build_session({"commandResponse": [], "overallCompletionCode": 0, "overallReasonCode": 0})

    result = session._map_response_parameters("DISPLAY", "QMGR", "qmgr", ["system", "version"])  # noqa: SLF001

    assert result == ["SYSTEM", "VERSION"]


def test_get_response_parameter_macros_ignores_invalid_shape(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setitem(
        session_module.MAPPING_DATA,
        "commands",
        {"DISPLAY QMGR": {"qualifier": "qmgr", "response_parameter_macros": "SYSTEM"}},
    )

    macros = session_module._get_response_parameter_macros(  # noqa: SLF001
        "DISPLAY",
        "QMGR",
        mapping_data=session_module.MAPPING_DATA,
    )

    assert macros == []


def test_get_response_parameter_macros_filters_non_string(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setitem(
        session_module.MAPPING_DATA,
        "commands",
        {"DISPLAY QMGR": {"qualifier": "qmgr", "response_parameter_macros": ["SYSTEM", 123]}},
    )

    macros = session_module._get_response_parameter_macros(  # noqa: SLF001
        "DISPLAY",
        "QMGR",
        mapping_data=session_module.MAPPING_DATA,
    )

    assert macros == ["SYSTEM"]


def test_map_response_parameters_unknown_qualifier_lenient() -> None:
    session, _transport = _build_session(
        {"commandResponse": [], "overallCompletionCode": 0, "overallReasonCode": 0},
        mapping_strict=False,
    )

    result = session._map_response_parameters("DISPLAY", "UNKNOWN", "unknown", ["foo"])  # noqa: SLF001

    assert result == ["foo"]


def test_map_response_parameters_unknown_key_strict() -> None:
    session = MQRESTSession(
        rest_base_url="https://example.invalid/ibmmq/rest/v2",
        qmgr_name="QM1",
        credentials=BasicAuth("user", TEST_PASSWORD),
        mapping_strict=True,
    )

    with pytest.raises(MappingError) as error_info:
        session._map_response_parameters("DISPLAY", "QUEUE", "queue", ["unknown_key"])  # noqa: SLF001

    issue = error_info.value.issues[0]
    assert issue.reason == "unknown_key"
    assert issue.attribute_name == "unknown_key"


def test_map_response_parameters_unknown_qualifier_strict() -> None:
    session = MQRESTSession(
        rest_base_url="https://example.invalid/ibmmq/rest/v2",
        qmgr_name="QM1",
        credentials=BasicAuth("user", TEST_PASSWORD),
        mapping_strict=True,
    )

    with pytest.raises(MappingError) as error_info:
        session._map_response_parameters("DISPLAY", "UNKNOWN", "unknown", ["foo"])  # noqa: SLF001

    issue = error_info.value.issues[0]
    assert issue.reason == "unknown_qualifier"
    assert issue.attribute_name == "*"


def test_map_response_parameters_handles_invalid_maps(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setitem(
        session_module.MAPPING_DATA,
        "qualifiers",
        {"queue": {"request_key_map": [], "response_key_map": {1: "foo"}}},
    )
    session, _transport = _build_session(
        {"commandResponse": [], "overallCompletionCode": 0, "overallReasonCode": 0},
        mapping_strict=False,
    )

    result = session._map_response_parameters("DISPLAY", "QUEUE", "queue", ["current_queue_depth"])  # noqa: SLF001

    assert result == ["current_queue_depth"]


def test_map_response_parameters_without_response_map(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setitem(
        session_module.MAPPING_DATA,
        "qualifiers",
        {"queue": {"request_key_map": {"foo": "FOO"}, "response_key_map": []}},
    )
    session, _transport = _build_session({"commandResponse": [], "overallCompletionCode": 0, "overallReasonCode": 0})

    result = session._map_response_parameters("DISPLAY", "QUEUE", "queue", ["foo"])  # noqa: SLF001

    assert result == ["FOO"]


def test_display_qmgr_returns_none_for_empty_response() -> None:
    response_payload = {
        "commandResponse": [],
        "overallCompletionCode": 0,
        "overallReasonCode": 0,
    }
    session, _transport = _build_session(response_payload)

    result = session.display_qmgr()

    assert result is None


def test_default_response_parameters_use_all() -> None:
    response_payload = {
        "commandResponse": [],
        "overallCompletionCode": 0,
        "overallReasonCode": 0,
    }
    session, transport = _build_session(response_payload)

    session.display_queue()

    recorded_request = transport.recorded_requests[0]
    assert recorded_request.payload["responseParameters"] == ["all"]


def test_command_error_raises_on_nonzero_completion_code() -> None:
    response_payload = {
        "commandResponse": [
            {"completionCode": 2, "reasonCode": 2059, "parameters": {}},
        ],
        "overallCompletionCode": 2,
        "overallReasonCode": 2059,
    }
    session, _transport = _build_session(response_payload)

    with pytest.raises(MQRESTCommandError):
        session.display_qmgr()


def test_build_headers_excludes_csrf_token_when_none() -> None:
    session = MQRESTSession(
        rest_base_url="https://example.invalid/ibmmq/rest/v2",
        qmgr_name="QM1",
        credentials=BasicAuth("user", TEST_PASSWORD),
        csrf_token=None,
    )

    headers = session._build_headers()  # noqa: SLF001

    assert headers["Accept"] == "application/json"
    assert headers["Authorization"].startswith("Basic ")
    assert "ibm-mq-rest-csrf-token" not in headers


def test_build_command_payload_omits_optional_fields() -> None:
    payload = session_module._build_command_payload(  # noqa: SLF001
        command="DISPLAY",
        qualifier="QUEUE",
        name=None,
        request_parameters={},
        response_parameters=[],
    )

    assert payload == {
        "type": "runCommandJSON",
        "command": "DISPLAY",
        "qualifier": "QUEUE",
    }


def test_normalize_response_parameters_handles_all() -> None:
    assert session_module._normalize_response_parameters(None) == ["all"]  # noqa: SLF001
    assert session_module._normalize_response_parameters(["ALL"]) == ["all"]  # noqa: SLF001


def test_parse_response_payload_invalid_json() -> None:
    with pytest.raises(MQRESTResponseError) as excinfo:
        session_module._parse_response_payload("not json")  # noqa: SLF001

    assert excinfo.value.response_text == "not json"


def test_parse_response_payload_non_object() -> None:
    with pytest.raises(MQRESTResponseError):
        session_module._parse_response_payload("[]")  # noqa: SLF001


def test_extract_command_response_empty_returns_list() -> None:
    assert session_module._extract_command_response({}) == []  # noqa: SLF001


def test_extract_command_response_non_list_raises() -> None:
    with pytest.raises(MQRESTResponseError):
        session_module._extract_command_response({"commandResponse": {}})  # noqa: SLF001


def test_extract_command_response_invalid_item_raises() -> None:
    with pytest.raises(MQRESTResponseError):
        session_module._extract_command_response({"commandResponse": [1]})  # noqa: SLF001


def test_raise_for_command_errors_on_overall_error() -> None:
    payload = {
        "overallCompletionCode": 2,
        "overallReasonCode": 0,
        "commandResponse": [],
    }

    with pytest.raises(MQRESTCommandError) as excinfo:
        session_module._raise_for_command_errors(payload, STATUS_INTERNAL_SERVER_ERROR)  # noqa: SLF001

    assert excinfo.value.status_code == STATUS_INTERNAL_SERVER_ERROR


def test_raise_for_command_errors_on_command_item_error() -> None:
    payload = {
        "overallCompletionCode": 0,
        "overallReasonCode": 0,
        "commandResponse": [{"completionCode": 2, "reasonCode": 2059}],
    }

    with pytest.raises(MQRESTCommandError):
        session_module._raise_for_command_errors(payload, 200)  # noqa: SLF001


def test_requests_transport_wraps_request_exception() -> None:
    class FailingSession:
        def post(self, *_args: object, **_kwargs: object) -> object:
            raise RequestException(REQUEST_EXCEPTION_MESSAGE)

    transport = RequestsTransport(FailingSession())

    with pytest.raises(MQRESTTransportError) as excinfo:
        transport.post_json(
            "https://example.invalid",
            payload={},
            headers={},
            timeout_seconds=5.0,
            verify_tls=True,
        )

    assert excinfo.value.url == "https://example.invalid"


def test_map_attributes_false_returns_raw_parameters() -> None:
    response_payload = {
        "commandResponse": [
            {
                "completionCode": 0,
                "reasonCode": 0,
                "parameters": {"foo": "bar"},
            },
        ],
        "overallCompletionCode": 0,
        "overallReasonCode": 0,
    }
    response_text = json.dumps(response_payload)
    transport = FakeTransport(
        TransportResponse(status_code=200, text=response_text, headers={}),
    )
    session = MQRESTSession(
        rest_base_url="https://example.invalid/ibmmq/rest/v2",
        qmgr_name="QM1",
        credentials=BasicAuth("user", TEST_PASSWORD),
        transport=transport,
        map_attributes=False,
    )

    result = session.display_queue()

    assert result == [{"foo": "bar"}]


def test_resolve_mapping_qualifier_fallbacks() -> None:
    session = MQRESTSession(
        rest_base_url="https://example.invalid/ibmmq/rest/v2",
        qmgr_name="QM1",
        credentials=BasicAuth("user", TEST_PASSWORD),
    )

    assert session._resolve_mapping_qualifier("DISPLAY", "QMGR") == "qmgr"  # noqa: SLF001
    assert session._resolve_mapping_qualifier("BOGUS", "QUEUE") == "queue"  # noqa: SLF001
    assert session._resolve_mapping_qualifier("BOGUS", "UNKNOWN") == "unknown"  # noqa: SLF001


def test_display_channel_defaults_to_all() -> None:
    response_payload = {
        "commandResponse": [
            {
                "completionCode": 0,
                "reasonCode": 0,
                "parameters": {"CHLTYPE": "SVRCONN"},
            },
        ],
        "overallCompletionCode": 0,
        "overallReasonCode": 0,
    }
    session, transport = _build_session(response_payload)

    result = session.display_channel()

    recorded_request = transport.recorded_requests[0]
    assert recorded_request.payload["name"] == "*"
    assert result == [{"channel_type": "SVRCONN"}]


def test_define_and_delete_commands_build_payloads() -> None:
    response_payload = {
        "commandResponse": [],
        "overallCompletionCode": 0,
        "overallReasonCode": 0,
    }
    session, transport = _build_session(response_payload)

    session.define_qlocal("TEST.QLOCAL")
    session.define_qremote("TEST.QREMOTE")
    session.define_qalias("TEST.QALIAS")
    session.define_qmodel("TEST.QMODEL")
    session.delete_queue("TEST.QLOCAL")
    session.define_channel("TEST.CHANNEL", request_parameters={"channel_type": "SVRCONN"})
    session.delete_channel("TEST.CHANNEL")

    define_qlocal_request = transport.recorded_requests[0]
    define_qremote_request = transport.recorded_requests[1]
    define_qalias_request = transport.recorded_requests[2]
    define_qmodel_request = transport.recorded_requests[3]
    delete_queue_request = transport.recorded_requests[4]
    define_channel_request = transport.recorded_requests[5]
    delete_channel_request = transport.recorded_requests[6]

    assert define_qlocal_request.payload["command"] == "DEFINE"
    assert define_qlocal_request.payload["qualifier"] == "QLOCAL"
    assert define_qlocal_request.payload["name"] == "TEST.QLOCAL"

    assert define_qremote_request.payload["command"] == "DEFINE"
    assert define_qremote_request.payload["qualifier"] == "QREMOTE"
    assert define_qremote_request.payload["name"] == "TEST.QREMOTE"

    assert define_qalias_request.payload["command"] == "DEFINE"
    assert define_qalias_request.payload["qualifier"] == "QALIAS"
    assert define_qalias_request.payload["name"] == "TEST.QALIAS"

    assert define_qmodel_request.payload["command"] == "DEFINE"
    assert define_qmodel_request.payload["qualifier"] == "QMODEL"
    assert define_qmodel_request.payload["name"] == "TEST.QMODEL"

    assert delete_queue_request.payload["command"] == "DELETE"
    assert delete_queue_request.payload["qualifier"] == "QUEUE"
    assert delete_queue_request.payload["name"] == "TEST.QLOCAL"

    assert define_channel_request.payload["command"] == "DEFINE"
    assert define_channel_request.payload["qualifier"] == "CHANNEL"
    assert define_channel_request.payload["name"] == "TEST.CHANNEL"
    assert define_channel_request.payload["parameters"] == {"CHLTYPE": "SVRCONN"}

    assert delete_channel_request.payload["command"] == "DELETE"
    assert delete_channel_request.payload["qualifier"] == "CHANNEL"
    assert delete_channel_request.payload["name"] == "TEST.CHANNEL"


def test_command_response_with_invalid_parameters_returns_empty_dict() -> None:
    response_payload = {
        "commandResponse": [
            {"completionCode": 0, "reasonCode": 0, "parameters": "not-a-map"},
        ],
        "overallCompletionCode": 0,
        "overallReasonCode": 0,
    }
    session, _transport = _build_session(response_payload)

    result = session.display_queue()

    assert result == [{}]


def test_raise_for_command_errors_ignores_non_mapping_items() -> None:
    payload = {
        "overallCompletionCode": 0,
        "overallReasonCode": 0,
        "commandResponse": [1, "bad"],
    }

    session_module._raise_for_command_errors(payload, 200)  # noqa: SLF001


def test_raise_for_command_errors_handles_non_list_command_response() -> None:
    payload = {
        "overallCompletionCode": 0,
        "overallReasonCode": 0,
        "commandResponse": {"completionCode": 0},
    }

    session_module._raise_for_command_errors(payload, 200)  # noqa: SLF001


def test_extract_optional_int_handles_non_int() -> None:
    assert session_module._extract_optional_int("nope") is None  # noqa: SLF001


def test_get_command_map_handles_invalid_shape(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setitem(session_module.MAPPING_DATA, "commands", [])

    assert session_module._get_command_map(session_module.MAPPING_DATA) == {}  # noqa: SLF001


def test_resolve_mapping_qualifier_handles_invalid_command_entry(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setitem(
        session_module.MAPPING_DATA,
        "commands",
        {"BOGUS THING": {"qualifier": 123}},
    )
    session = MQRESTSession(
        rest_base_url="https://example.invalid/ibmmq/rest/v2",
        qmgr_name="QM1",
        credentials=BasicAuth("user", TEST_PASSWORD),
    )

    assert session._resolve_mapping_qualifier("BOGUS", "THING") == "thing"  # noqa: SLF001


def test_requests_transport_success() -> None:
    class FakeResponse:
        def __init__(self) -> None:
            self.status_code = STATUS_CREATED
            self.text = '{"ok": true}'
            self.headers = {"x-test": "1"}

    class RecordingSession:
        def __init__(self) -> None:
            self.calls: list[tuple[str, dict[str, object], dict[str, str]]] = []

        def post(
            self,
            url: str,
            *,
            json: dict[str, object],
            headers: dict[str, str],
            timeout: float | None,
            verify: bool,
        ) -> FakeResponse:
            _ = timeout
            _ = verify
            self.calls.append((url, json, headers))
            return FakeResponse()

    requests_session = RecordingSession()
    transport = RequestsTransport(requests_session)

    response = transport.post_json(
        "https://example.invalid",
        payload={"command": "DISPLAY"},
        headers={"Authorization": "Basic abc"},
        timeout_seconds=5.0,
        verify_tls=False,
    )

    assert response.status_code == STATUS_CREATED
    assert response.text == '{"ok": true}'
    assert response.headers == {"x-test": "1"}


def test_get_qualifier_entry_invalid_shape(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setitem(session_module.MAPPING_DATA, "qualifiers", "bogus")

    assert session_module._get_qualifier_entry("queue", mapping_data=session_module.MAPPING_DATA) is None  # noqa: SLF001


def test_get_qualifier_entry_non_mapping_entry(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setitem(session_module.MAPPING_DATA, "qualifiers", {"queue": "bogus"})

    assert session_module._get_qualifier_entry("queue", mapping_data=session_module.MAPPING_DATA) is None  # noqa: SLF001


def test_mqsc_command_methods_match_mapping() -> None:
    response_payload = {
        "commandResponse": [],
        "overallCompletionCode": 0,
        "overallReasonCode": 0,
    }
    session, transport = _build_session(response_payload, mapping_strict=False)
    commands = _load_mqsc_commands()
    assert commands

    nameless_qualifiers = {"QMGR", "QMSTATUS", "CMDSERV"}
    for command in commands:
        method_name = _method_name_from_mqsc(command)
        method = getattr(session, method_name)
        _, qualifier = _split_mqsc_command(command)
        if qualifier in nameless_qualifiers:
            method()
        else:
            method(name="TEST.OBJECT")

    assert len(transport.recorded_requests) == len(commands)
    for recorded_request, command in zip(transport.recorded_requests, commands, strict=True):
        verb, qualifier = _split_mqsc_command(command)
        assert recorded_request.payload["command"] == verb
        assert recorded_request.payload["qualifier"] == qualifier


def test_display_queue_where_maps_filter_keyword() -> None:
    response_payload = {
        "commandResponse": [],
        "overallCompletionCode": 0,
        "overallReasonCode": 0,
    }
    session, transport = _build_session(response_payload)

    session.display_queue(where="current_queue_depth GT 100")

    recorded_request = transport.recorded_requests[0]
    assert recorded_request.payload["parameters"] == {"WHERE": "CURDEPTH GT 100"}


def test_display_queue_where_passthrough_when_mapping_disabled() -> None:
    response_payload = {
        "commandResponse": [],
        "overallCompletionCode": 0,
        "overallReasonCode": 0,
    }
    response_text = json.dumps(response_payload)
    transport = FakeTransport(
        TransportResponse(status_code=200, text=response_text, headers={}),
    )
    session = MQRESTSession(
        rest_base_url="https://example.invalid/ibmmq/rest/v2",
        qmgr_name="QM1",
        credentials=BasicAuth("user", TEST_PASSWORD),
        transport=transport,
        map_attributes=False,
    )

    session.display_queue(where="CURDEPTH GT 100")

    recorded_request = transport.recorded_requests[0]
    assert recorded_request.payload["parameters"] == {"WHERE": "CURDEPTH GT 100"}


def test_display_queue_where_unknown_keyword_strict_raises() -> None:
    response_payload = {
        "commandResponse": [],
        "overallCompletionCode": 0,
        "overallReasonCode": 0,
    }
    session, _transport = _build_session(response_payload)

    with pytest.raises(MappingError) as error_info:
        session.display_queue(where="unknown_attribute GT 100")

    issue = error_info.value.issues[0]
    assert issue.reason == "unknown_key"
    assert issue.attribute_name == "unknown_attribute"


def test_display_queue_where_unknown_keyword_lenient_passes_through() -> None:
    response_payload = {
        "commandResponse": [],
        "overallCompletionCode": 0,
        "overallReasonCode": 0,
    }
    session, transport = _build_session(response_payload, mapping_strict=False)

    session.display_queue(where="unknown_attribute GT 100")

    recorded_request = transport.recorded_requests[0]
    assert recorded_request.payload["parameters"] == {"WHERE": "unknown_attribute GT 100"}


def test_display_queue_where_none_omits_where_parameter() -> None:
    response_payload = {
        "commandResponse": [],
        "overallCompletionCode": 0,
        "overallReasonCode": 0,
    }
    session, transport = _build_session(response_payload)

    session.display_queue()

    recorded_request = transport.recorded_requests[0]
    assert "WHERE" not in recorded_request.payload.get("parameters", {})


def test_display_queue_where_empty_string_is_noop() -> None:
    response_payload = {
        "commandResponse": [],
        "overallCompletionCode": 0,
        "overallReasonCode": 0,
    }
    session, transport = _build_session(response_payload)

    session.display_queue(where="")

    recorded_request = transport.recorded_requests[0]
    assert "WHERE" not in recorded_request.payload.get("parameters", {})


def test_display_queue_where_combined_with_request_parameters() -> None:
    response_payload = {
        "commandResponse": [],
        "overallCompletionCode": 0,
        "overallReasonCode": 0,
    }
    session, transport = _build_session(response_payload)

    session.display_queue(
        request_parameters={"default_persistence": "def"},
        where="current_queue_depth GT 100",
    )

    recorded_request = transport.recorded_requests[0]
    params = recorded_request.payload["parameters"]
    assert params["WHERE"] == "CURDEPTH GT 100"
    assert params["DEFPSIST"] == "DEF"


def test_display_queue_where_overrides_request_parameters_where() -> None:
    response_payload = {
        "commandResponse": [],
        "overallCompletionCode": 0,
        "overallReasonCode": 0,
    }
    response_text = json.dumps(response_payload)
    transport = FakeTransport(
        TransportResponse(status_code=200, text=response_text, headers={}),
    )
    session = MQRESTSession(
        rest_base_url="https://example.invalid/ibmmq/rest/v2",
        qmgr_name="QM1",
        credentials=BasicAuth("user", TEST_PASSWORD),
        transport=transport,
        map_attributes=False,
    )

    session.display_queue(
        request_parameters={"WHERE": "DESCR LK 'old*'"},
        where="CURDEPTH GT 100",
    )

    recorded_request = transport.recorded_requests[0]
    assert recorded_request.payload["parameters"]["WHERE"] == "CURDEPTH GT 100"


def test_display_channel_where_maps_filter_keyword() -> None:
    response_payload = {
        "commandResponse": [],
        "overallCompletionCode": 0,
        "overallReasonCode": 0,
    }
    session, transport = _build_session(response_payload)

    session.display_channel(where="channel_type EQ SVRCONN")

    recorded_request = transport.recorded_requests[0]
    assert recorded_request.payload["parameters"]["WHERE"] == "CHLTYPE EQ SVRCONN"


def test_map_where_keyword_unknown_qualifier_strict_raises() -> None:
    with pytest.raises(MappingError) as error_info:
        session_module._map_where_keyword(  # noqa: SLF001
            "some_attr GT 5",
            "nonexistent",
            strict=True,
            mapping_data=MAPPING_DATA,
        )

    issue = error_info.value.issues[0]
    assert issue.reason == "unknown_qualifier"


def test_map_where_keyword_unknown_qualifier_lenient_passes_through() -> None:
    result = session_module._map_where_keyword(  # noqa: SLF001
        "some_attr GT 5",
        "nonexistent",
        strict=False,
        mapping_data=MAPPING_DATA,
    )
    assert result == "some_attr GT 5"


def test_map_where_keyword_keyword_only() -> None:
    result = session_module._map_where_keyword(  # noqa: SLF001
        "current_queue_depth",
        "queue",
        strict=False,
        mapping_data=MAPPING_DATA,
    )
    assert result == "CURDEPTH"


def test_nested_objects_flattened_with_mapping() -> None:
    response_payload = {
        "commandResponse": [
            {
                "completionCode": 0,
                "reasonCode": 0,
                "parameters": {
                    "conn": "ABC123",
                    "extconn": "DEF456",
                    "objects": [
                        {"objname": "Q1", "hstate": "ACTIVE"},
                        {"objname": "Q2", "hstate": "INACTIVE"},
                    ],
                },
            },
        ],
        "overallCompletionCode": 0,
        "overallReasonCode": 0,
    }
    session, _transport = _build_session(response_payload, mapping_strict=False)

    result = session.display_conn()

    first, second = result
    # Shared attributes replicated onto each flattened item (unmapped keys stay uppercase)
    assert first["CONN"] == "ABC123"
    assert first["EXTCONN"] == "DEF456"
    # Handle attributes mapped to snake_case (OBJNAME -> object_name, HSTATE -> handle_state)
    assert first["object_name"] == "Q1"
    assert first["handle_state"] == "ACTIVE"
    assert second["CONN"] == "ABC123"
    assert second["EXTCONN"] == "DEF456"
    assert second["object_name"] == "Q2"
    assert second["handle_state"] == "INACTIVE"
    # objects key is not present in flattened output
    assert "objects" not in first
    assert "OBJECTS" not in first


def test_nested_objects_flattened_without_mapping() -> None:
    response_payload = {
        "commandResponse": [
            {
                "completionCode": 0,
                "reasonCode": 0,
                "parameters": {
                    "conn": "ABC123",
                    "type": "HANDLE",
                    "objects": [
                        {"objname": "Q1", "hstate": "ACTIVE"},
                    ],
                },
            },
        ],
        "overallCompletionCode": 0,
        "overallReasonCode": 0,
    }
    session = MQRESTSession(
        rest_base_url="https://example.invalid/ibmmq/rest/v2",
        qmgr_name="QM1",
        credentials=BasicAuth("user", TEST_PASSWORD),
        transport=FakeTransport(
            TransportResponse(
                status_code=200,
                text=json.dumps(response_payload),
                headers={},
            ),
        ),
        map_attributes=False,
    )

    result = session.display_conn()

    assert result == [{"conn": "ABC123", "type": "HANDLE", "objname": "Q1", "hstate": "ACTIVE"}]


def test_nested_objects_empty_list_returns_empty() -> None:
    response_payload = {
        "commandResponse": [
            {
                "completionCode": 0,
                "reasonCode": 0,
                "parameters": {
                    "conn": "ABC123",
                    "type": "HANDLE",
                    "objects": [],
                },
            },
        ],
        "overallCompletionCode": 0,
        "overallReasonCode": 0,
    }
    session = MQRESTSession(
        rest_base_url="https://example.invalid/ibmmq/rest/v2",
        qmgr_name="QM1",
        credentials=BasicAuth("user", TEST_PASSWORD),
        transport=FakeTransport(
            TransportResponse(
                status_code=200,
                text=json.dumps(response_payload),
                headers={},
            ),
        ),
        map_attributes=False,
    )

    result = session.display_conn()

    assert result == []


def test_nested_objects_mixed_with_flat_items() -> None:
    response_payload = {
        "commandResponse": [
            {
                "completionCode": 0,
                "reasonCode": 0,
                "parameters": {
                    "conn": "ABC123",
                    "type": "HANDLE",
                    "objects": [
                        {"objname": "Q1"},
                    ],
                },
            },
            {
                "completionCode": 0,
                "reasonCode": 0,
                "parameters": {
                    "conn": "DEF456",
                    "flat_attr": "value",
                },
            },
        ],
        "overallCompletionCode": 0,
        "overallReasonCode": 0,
    }
    session = MQRESTSession(
        rest_base_url="https://example.invalid/ibmmq/rest/v2",
        qmgr_name="QM1",
        credentials=BasicAuth("user", TEST_PASSWORD),
        transport=FakeTransport(
            TransportResponse(
                status_code=200,
                text=json.dumps(response_payload),
                headers={},
            ),
        ),
        map_attributes=False,
    )

    result = session.display_conn()

    first, second = result
    assert first == {"conn": "ABC123", "type": "HANDLE", "objname": "Q1"}
    assert second == {"conn": "DEF456", "flat_attr": "value"}


def test_nested_objects_single_entry() -> None:
    response_payload = {
        "commandResponse": [
            {
                "completionCode": 0,
                "reasonCode": 0,
                "parameters": {
                    "conn": "ABC123",
                    "objects": [{"objname": "Q1"}],
                },
            },
        ],
        "overallCompletionCode": 0,
        "overallReasonCode": 0,
    }
    session = MQRESTSession(
        rest_base_url="https://example.invalid/ibmmq/rest/v2",
        qmgr_name="QM1",
        credentials=BasicAuth("user", TEST_PASSWORD),
        transport=FakeTransport(
            TransportResponse(
                status_code=200,
                text=json.dumps(response_payload),
                headers={},
            ),
        ),
        map_attributes=False,
    )

    result = session.display_conn()

    assert result == [{"conn": "ABC123", "objname": "Q1"}]


def test_nested_objects_non_list_passes_through() -> None:
    response_payload = {
        "commandResponse": [
            {
                "completionCode": 0,
                "reasonCode": 0,
                "parameters": {
                    "conn": "ABC123",
                    "objects": "not_a_list",
                },
            },
        ],
        "overallCompletionCode": 0,
        "overallReasonCode": 0,
    }
    session = MQRESTSession(
        rest_base_url="https://example.invalid/ibmmq/rest/v2",
        qmgr_name="QM1",
        credentials=BasicAuth("user", TEST_PASSWORD),
        transport=FakeTransport(
            TransportResponse(
                status_code=200,
                text=json.dumps(response_payload),
                headers={},
            ),
        ),
        map_attributes=False,
    )

    result = session.display_conn()

    assert result == [{"conn": "ABC123", "objects": "not_a_list"}]


def test_nested_objects_non_dict_items_skipped() -> None:
    response_payload = {
        "commandResponse": [
            {
                "completionCode": 0,
                "reasonCode": 0,
                "parameters": {
                    "conn": "ABC123",
                    "objects": [
                        {"objname": "Q1"},
                        "not_a_dict",
                        {"objname": "Q2"},
                    ],
                },
            },
        ],
        "overallCompletionCode": 0,
        "overallReasonCode": 0,
    }
    session = MQRESTSession(
        rest_base_url="https://example.invalid/ibmmq/rest/v2",
        qmgr_name="QM1",
        credentials=BasicAuth("user", TEST_PASSWORD),
        transport=FakeTransport(
            TransportResponse(
                status_code=200,
                text=json.dumps(response_payload),
                headers={},
            ),
        ),
        map_attributes=False,
    )

    result = session.display_conn()

    first, second = result
    assert first == {"conn": "ABC123", "objname": "Q1"}
    assert second == {"conn": "ABC123", "objname": "Q2"}


# -- Mapping overrides tests --


def test_mapping_overrides_none_uses_defaults() -> None:
    response_payload = {
        "commandResponse": [
            {"completionCode": 0, "reasonCode": 0, "parameters": {"CURDEPTH": TEST_DEPTH}},
        ],
        "overallCompletionCode": 0,
        "overallReasonCode": 0,
    }
    session, _transport = _build_session(response_payload)

    result = session.display_queue()

    assert result == [{"current_queue_depth": TEST_DEPTH}]


def test_mapping_overrides_invalid_raises_at_construction() -> None:
    with pytest.raises(ValueError, match="Invalid top-level key"):
        MQRESTSession(
            rest_base_url="https://example.invalid/ibmmq/rest/v2",
            qmgr_name="QM1",
            credentials=BasicAuth("user", TEST_PASSWORD),
            mapping_overrides={"bogus": {}},
        )


def test_mapping_overrides_response_key_override() -> None:
    response_payload = {
        "commandResponse": [
            {"completionCode": 0, "reasonCode": 0, "parameters": {"CURDEPTH": TEST_DEPTH}},
        ],
        "overallCompletionCode": 0,
        "overallReasonCode": 0,
    }
    session, _transport = _build_session(
        response_payload,
        mapping_overrides={
            "qualifiers": {
                "queue": {
                    "response_key_map": {"CURDEPTH": "queue_depth"},
                },
            },
        },
    )

    result = session.display_queue()

    assert result == [{"queue_depth": TEST_DEPTH}]


def test_mapping_overrides_request_key_override() -> None:
    response_payload = {
        "commandResponse": [],
        "overallCompletionCode": 0,
        "overallReasonCode": 0,
    }
    session, transport = _build_session(
        response_payload,
        mapping_overrides={
            "qualifiers": {
                "queue": {
                    "request_key_map": {"my_depth": "CURDEPTH"},
                },
            },
        },
    )

    session.display_queue(request_parameters={"my_depth": TEST_DEPTH})

    recorded_request = transport.recorded_requests[0]
    assert recorded_request.payload["parameters"]["CURDEPTH"] == TEST_DEPTH


def test_mapping_overrides_where_keyword_uses_override() -> None:
    response_payload = {
        "commandResponse": [],
        "overallCompletionCode": 0,
        "overallReasonCode": 0,
    }
    session, transport = _build_session(
        response_payload,
        mapping_overrides={
            "qualifiers": {
                "queue": {
                    "request_key_map": {"my_depth": "CURDEPTH"},
                },
            },
        },
    )

    session.display_queue(where="my_depth GT 100")

    recorded_request = transport.recorded_requests[0]
    assert recorded_request.payload["parameters"]["WHERE"] == "CURDEPTH GT 100"


def test_mapping_overrides_does_not_affect_unmapped_keys() -> None:
    response_payload = {
        "commandResponse": [
            {
                "completionCode": 0,
                "reasonCode": 0,
                "parameters": {"CURDEPTH": TEST_DEPTH, "DEFPSIST": "NOTFIXED"},
            },
        ],
        "overallCompletionCode": 0,
        "overallReasonCode": 0,
    }
    session, _transport = _build_session(
        response_payload,
        mapping_overrides={
            "qualifiers": {
                "queue": {
                    "response_key_map": {"CURDEPTH": "queue_depth"},
                },
            },
        },
    )

    result = session.display_queue()

    assert result[0]["queue_depth"] == TEST_DEPTH
    assert result[0]["default_persistence"] == "not_fixed"


def _load_mqsc_commands() -> list[str]:
    commands = MAPPING_DATA.get("commands", {})
    assert isinstance(commands, dict)
    return sorted(commands.keys())


def _method_name_from_mqsc(command: str) -> str:
    tokens = command.split()
    verb = tokens[0].lower()
    qualifier = "_".join(token.lower() for token in tokens[1:])
    return f"{verb}_{qualifier}"


def _split_mqsc_command(command: str) -> tuple[str, str]:
    tokens = command.split()
    verb = tokens[0].upper()
    qualifier = " ".join(tokens[1:]).upper()
    return verb, qualifier


class MultiResponseTransport:
    def __init__(self, responses: list[TransportResponse]) -> None:
        self._responses = list(responses)
        self._call_index = 0
        self.recorded_requests: list[RecordedRequest] = []

    def post_json(
        self,
        url: str,
        payload: Mapping[str, object],
        *,
        headers: Mapping[str, str],
        timeout_seconds: float | None,
        verify_tls: bool,
    ) -> TransportResponse:
        self.recorded_requests.append(
            RecordedRequest(
                url=url,
                payload=dict(payload),
                headers=dict(headers),
                timeout_seconds=timeout_seconds,
                verify_tls=verify_tls,
            ),
        )
        response = self._responses[self._call_index]
        self._call_index += 1
        return response


# -- Credential dispatch tests --


def test_credentials_ltpa_auth_sends_cookie_header() -> None:
    login_response = TransportResponse(
        status_code=200,
        text="",
        headers={"Set-Cookie": "LtpaToken2=ltpa_test_token; Path=/; HttpOnly"},
    )
    command_response = TransportResponse(
        status_code=200,
        text=json.dumps(
            {
                "commandResponse": [
                    {"completionCode": 0, "reasonCode": 0, "parameters": {"QMNAME": "QM1"}},
                ],
                "overallCompletionCode": 0,
                "overallReasonCode": 0,
            }
        ),
        headers={},
    )
    transport = MultiResponseTransport([login_response, command_response])

    session = MQRESTSession(
        "https://example.invalid/ibmmq/rest/v2",
        "QM1",
        credentials=LTPAAuth("user", TEST_PASSWORD),
        transport=transport,
    )

    result = session.display_qmgr()

    assert result == {"queue_manager_name": "QM1"}
    # First request is login
    login_request = transport.recorded_requests[0]
    assert login_request.url == "https://example.invalid/ibmmq/rest/v2/login"
    assert login_request.payload == {"username": "user", "password": TEST_PASSWORD}
    # Second request is MQSC command with cookie
    command_request = transport.recorded_requests[1]
    assert "Authorization" not in command_request.headers
    assert command_request.headers["Cookie"] == "LtpaToken2=ltpa_test_token"


def test_credentials_certificate_auth_no_auth_header() -> None:
    response_payload = {
        "commandResponse": [
            {"completionCode": 0, "reasonCode": 0, "parameters": {"QMNAME": "QM1"}},
        ],
        "overallCompletionCode": 0,
        "overallReasonCode": 0,
    }
    response_text = json.dumps(response_payload)
    transport = FakeTransport(
        TransportResponse(status_code=200, text=response_text, headers={}),
    )

    session = MQRESTSession(
        "https://example.invalid/ibmmq/rest/v2",
        "QM1",
        credentials=CertificateAuth("/cert.pem", "/key.pem"),
        transport=transport,
    )

    result = session.display_qmgr()

    assert result == {"queue_manager_name": "QM1"}
    recorded = transport.recorded_requests[0]
    assert "Authorization" not in recorded.headers
    assert "Cookie" not in recorded.headers
    # CSRF token still present
    assert recorded.headers["ibm-mq-rest-csrf-token"] == "local"


def test_no_credentials_raises_type_error() -> None:
    with pytest.raises(TypeError, match="credentials"):
        MQRESTSession(
            "https://example.invalid/ibmmq/rest/v2",
            "QM1",
        )


def test_ltpa_login_failure_raises_at_construction() -> None:
    transport = FakeTransport(
        TransportResponse(
            status_code=401,
            text='{"error": "unauthorized"}',
            headers={},
        ),
    )

    with pytest.raises(MQRESTAuthError):
        MQRESTSession(
            "https://example.invalid/ibmmq/rest/v2",
            "QM1",
            credentials=LTPAAuth("user", TEST_PASSWORD),
            transport=transport,
        )


def test_requests_transport_client_cert_configured() -> None:
    class RecordingSession:
        def __init__(self) -> None:
            self.cert: tuple[str, str] | str | None = None

    requests_session = RecordingSession()
    transport = RequestsTransport(requests_session, client_cert=("/cert.pem", "/key.pem"))

    assert requests_session.cert == ("/cert.pem", "/key.pem")
    _ = transport


def test_requests_transport_client_cert_single_file() -> None:
    class RecordingSession:
        def __init__(self) -> None:
            self.cert: tuple[str, str] | str | None = None

    requests_session = RecordingSession()
    transport = RequestsTransport(requests_session, client_cert="/combined.pem")

    assert requests_session.cert == "/combined.pem"
    _ = transport


def test_certificate_auth_creates_transport_with_cert() -> None:
    session = MQRESTSession(
        "https://example.invalid/ibmmq/rest/v2",
        "QM1",
        credentials=CertificateAuth("/cert.pem", "/key.pem"),
    )

    assert isinstance(session._transport, RequestsTransport)  # noqa: SLF001


def test_certificate_auth_single_cert_file() -> None:
    session = MQRESTSession(
        "https://example.invalid/ibmmq/rest/v2",
        "QM1",
        credentials=CertificateAuth("/combined.pem"),
    )

    assert isinstance(session._transport, RequestsTransport)  # noqa: SLF001
