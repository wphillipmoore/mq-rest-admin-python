"""Tests for the MQ REST session wrapper."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING

import pytest
from requests import RequestException

from pymqrest import session as session_module
from pymqrest.exceptions import (
    MQRESTCommandError,
    MQRESTResponseError,
    MQRESTTransportError,
)
from pymqrest.mapping import MappingError
from pymqrest.session import MQRESTSession, RequestsTransport, TransportResponse

if TYPE_CHECKING:
    from collections.abc import Mapping


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
            )
        )
        return self.response


def _build_session(response_payload: dict[str, object]) -> tuple[MQRESTSession, FakeTransport]:
    response_text = json.dumps(response_payload)
    transport = FakeTransport(
        TransportResponse(status_code=200, text=response_text, headers={}),
    )
    session = MQRESTSession(
        rest_base_url="https://example.invalid/ibmmq/rest/v2",
        qmgr_name="QM1",
        username="user",
        password="pass",
        transport=transport,
    )
    return session, transport


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

    assert result == {"q_mgr_name": "QM1"}


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
    session, _transport = _build_session(response_payload)

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
            }
        ],
        "overallCompletionCode": 0,
        "overallReasonCode": 0,
    }
    session, transport = _build_session(response_payload)

    result = session.display_queue(
        request_parameters={"def_persistence": "def"},
        response_parameters=["def_persistence", "current_q_depth"],
    )

    recorded_request = transport.recorded_requests[0]
    assert recorded_request.payload["name"] == "*"
    assert recorded_request.payload["parameters"] == {"DEFPSIST": "DEF"}
    assert recorded_request.payload["responseParameters"] == ["DEFPSIST", "CURDEPTH"]
    assert result == [{"def_persistence": "not_fixed", "current_q_depth": 5}]


def test_map_response_parameters_unknown_key_lenient() -> None:
    session, _transport = _build_session({"commandResponse": [], "overallCompletionCode": 0, "overallReasonCode": 0})

    result = session._map_response_parameters("queue", ["unknown_key"])

    assert result == ["unknown_key"]


def test_map_response_parameters_unknown_qualifier_lenient() -> None:
    session, _transport = _build_session({"commandResponse": [], "overallCompletionCode": 0, "overallReasonCode": 0})

    result = session._map_response_parameters("unknown", ["foo"])

    assert result == ["foo"]


def test_map_response_parameters_unknown_key_strict() -> None:
    session = MQRESTSession(
        rest_base_url="https://example.invalid/ibmmq/rest/v2",
        qmgr_name="QM1",
        username="user",
        password="pass",
        mapping_strict=True,
    )

    with pytest.raises(MappingError) as error_info:
        session._map_response_parameters("queue", ["unknown_key"])

    issue = error_info.value.issues[0]
    assert issue.reason == "unknown_key"
    assert issue.attribute_name == "unknown_key"


def test_map_response_parameters_unknown_qualifier_strict() -> None:
    session = MQRESTSession(
        rest_base_url="https://example.invalid/ibmmq/rest/v2",
        qmgr_name="QM1",
        username="user",
        password="pass",
        mapping_strict=True,
    )

    with pytest.raises(MappingError) as error_info:
        session._map_response_parameters("unknown", ["foo"])

    issue = error_info.value.issues[0]
    assert issue.reason == "unknown_qualifier"
    assert issue.attribute_name == "*"


def test_map_response_parameters_handles_invalid_maps(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setitem(
        session_module.MAPPING_DATA,
        "qualifiers",
        {"queue": {"request_key_map": [], "response_key_map": {1: "foo"}}},
    )
    session, _transport = _build_session({"commandResponse": [], "overallCompletionCode": 0, "overallReasonCode": 0})

    result = session._map_response_parameters("queue", ["current_q_depth"])

    assert result == ["current_q_depth"]


def test_map_response_parameters_without_response_map(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setitem(
        session_module.MAPPING_DATA,
        "qualifiers",
        {"queue": {"request_key_map": {"foo": "FOO"}, "response_key_map": []}},
    )
    session, _transport = _build_session({"commandResponse": [], "overallCompletionCode": 0, "overallReasonCode": 0})

    result = session._map_response_parameters("queue", ["foo"])

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
        username="user",
        password="pass",
        csrf_token=None,
    )

    headers = session._build_headers()

    assert headers["Accept"] == "application/json"
    assert headers["Authorization"].startswith("Basic ")
    assert "ibm-mq-rest-csrf-token" not in headers


def test_build_command_payload_omits_optional_fields() -> None:
    payload = session_module._build_command_payload(
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
    assert session_module._normalize_response_parameters(None) == ["all"]
    assert session_module._normalize_response_parameters(["ALL"]) == ["all"]


def test_parse_response_payload_invalid_json() -> None:
    with pytest.raises(MQRESTResponseError) as excinfo:
        session_module._parse_response_payload("not json")

    assert excinfo.value.response_text == "not json"


def test_parse_response_payload_non_object() -> None:
    with pytest.raises(MQRESTResponseError):
        session_module._parse_response_payload("[]")


def test_extract_command_response_empty_returns_list() -> None:
    assert session_module._extract_command_response({}) == []


def test_extract_command_response_non_list_raises() -> None:
    with pytest.raises(MQRESTResponseError):
        session_module._extract_command_response({"commandResponse": {}})


def test_extract_command_response_invalid_item_raises() -> None:
    with pytest.raises(MQRESTResponseError):
        session_module._extract_command_response({"commandResponse": [1]})


def test_raise_for_command_errors_on_overall_error() -> None:
    payload = {
        "overallCompletionCode": 2,
        "overallReasonCode": 0,
        "commandResponse": [],
    }

    with pytest.raises(MQRESTCommandError) as excinfo:
        session_module._raise_for_command_errors(payload, 500)

    assert excinfo.value.status_code == 500


def test_raise_for_command_errors_on_command_item_error() -> None:
    payload = {
        "overallCompletionCode": 0,
        "overallReasonCode": 0,
        "commandResponse": [{"completionCode": 2, "reasonCode": 2059}],
    }

    with pytest.raises(MQRESTCommandError):
        session_module._raise_for_command_errors(payload, 200)


def test_requests_transport_wraps_request_exception() -> None:
    class FailingSession:
        def post(self, *_args: object, **_kwargs: object) -> object:
            raise RequestException("boom")

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
            }
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
        username="user",
        password="pass",
        transport=transport,
        map_attributes=False,
    )

    result = session.display_queue()

    assert result == [{"foo": "bar"}]


def test_resolve_mapping_qualifier_fallbacks() -> None:
    session = MQRESTSession(
        rest_base_url="https://example.invalid/ibmmq/rest/v2",
        qmgr_name="QM1",
        username="user",
        password="pass",
    )

    assert session._resolve_mapping_qualifier("DISPLAY", "QMGR") == "qmgr"
    assert session._resolve_mapping_qualifier("BOGUS", "QUEUE") == "queue"
    assert session._resolve_mapping_qualifier("BOGUS", "UNKNOWN") == "unknown"


def test_display_channel_defaults_to_all() -> None:
    response_payload = {
        "commandResponse": [
            {
                "completionCode": 0,
                "reasonCode": 0,
                "parameters": {"CHLTYPE": "SVRCONN"},
            }
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
    assert define_channel_request.payload["parameters"] == {"TYPE": "SVRCONN"}

    assert delete_channel_request.payload["command"] == "DELETE"
    assert delete_channel_request.payload["qualifier"] == "CHANNEL"
    assert delete_channel_request.payload["name"] == "TEST.CHANNEL"


def test_command_response_with_invalid_parameters_returns_empty_dict() -> None:
    response_payload = {
        "commandResponse": [
            {"completionCode": 0, "reasonCode": 0, "parameters": "not-a-map"}
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

    session_module._raise_for_command_errors(payload, 200)


def test_raise_for_command_errors_handles_non_list_command_response() -> None:
    payload = {
        "overallCompletionCode": 0,
        "overallReasonCode": 0,
        "commandResponse": {"completionCode": 0},
    }

    session_module._raise_for_command_errors(payload, 200)


def test_extract_optional_int_handles_non_int() -> None:
    assert session_module._extract_optional_int("nope") is None


def test_get_command_map_handles_invalid_shape(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setitem(session_module.MAPPING_DATA, "commands", [])

    assert session_module._get_command_map() == {}


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
        username="user",
        password="pass",
    )

    assert session._resolve_mapping_qualifier("BOGUS", "THING") == "thing"


def test_requests_transport_success() -> None:
    class FakeResponse:
        def __init__(self) -> None:
            self.status_code = 201
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

    assert response.status_code == 201
    assert response.text == '{"ok": true}'
    assert response.headers == {"x-test": "1"}


def test_get_qualifier_entry_invalid_shape(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setitem(session_module.MAPPING_DATA, "qualifiers", "bogus")

    assert session_module._get_qualifier_entry("queue") is None


def test_get_qualifier_entry_non_mapping_entry(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setitem(session_module.MAPPING_DATA, "qualifiers", {"queue": "bogus"})

    assert session_module._get_qualifier_entry("queue") is None


def test_mqsc_command_methods_match_mapping() -> None:
    response_payload = {
        "commandResponse": [],
        "overallCompletionCode": 0,
        "overallReasonCode": 0,
    }
    session, transport = _build_session(response_payload)
    commands = _load_mqsc_commands()
    assert commands

    for command in commands:
        method_name = _method_name_from_mqsc(command)
        method = getattr(session, method_name)
        method(name="TEST.OBJECT")

    assert len(transport.recorded_requests) == len(commands)
    for recorded_request, command in zip(transport.recorded_requests, commands, strict=True):
        verb, qualifier = _split_mqsc_command(command)
        assert recorded_request.payload["command"] == verb
        assert recorded_request.payload["qualifier"] == qualifier


def _load_mqsc_commands() -> list[str]:
    mapping_path = (
        Path(__file__).resolve().parents[2] / "docs/extraction/mqsc-commands.yaml"
    )
    commands: list[str] = []
    in_commands = False
    for line in mapping_path.read_text().splitlines():
        if line.startswith("commands:"):
            in_commands = True
            continue
        if not in_commands:
            continue
        if line and not line.startswith(" "):
            break
        match = re.match(r"\s*-\s*(.+)", line)
        if match:
            commands.append(match.group(1).strip())

    unique_commands: list[str] = []
    seen: set[str] = set()
    for command in commands:
        if command not in seen:
            seen.add(command)
            unique_commands.append(command)
    return unique_commands


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
