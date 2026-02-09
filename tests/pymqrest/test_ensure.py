"""Tests for idempotent ensure methods."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import TYPE_CHECKING

import pytest

from pymqrest.ensure import EnsureResult, _values_match
from pymqrest.session import MQRESTSession, TransportResponse

if TYPE_CHECKING:
    from collections.abc import Mapping, Sequence

TEST_PASSWORD = "pass"
EXPECT_ONE_REQUEST = 1
EXPECT_TWO_REQUESTS = 2


@dataclass(frozen=True)
class RecordedRequest:
    """Captured request for assertion."""

    url: str
    payload: dict[str, object]
    headers: dict[str, str]
    timeout_seconds: float | None
    verify_tls: bool


class MultiResponseTransport:
    """Transport that returns a sequence of canned responses."""

    def __init__(self, responses: Sequence[TransportResponse]) -> None:
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


def _make_response(payload: dict[str, object]) -> TransportResponse:
    return TransportResponse(status_code=200, text=json.dumps(payload), headers={})


def _success_payload(
    parameters: list[dict[str, object]] | None = None,
) -> dict[str, object]:
    if parameters is None:
        return {
            "overallCompletionCode": 0,
            "overallReasonCode": 0,
        }
    return {
        "commandResponse": [{"completionCode": 0, "reasonCode": 0, "parameters": params} for params in parameters],
        "overallCompletionCode": 0,
        "overallReasonCode": 0,
    }


def _build_session(
    responses: Sequence[dict[str, object]],
    *,
    mapping_strict: bool | None = None,
) -> tuple[MQRESTSession, MultiResponseTransport]:
    transport = MultiResponseTransport([_make_response(resp) for resp in responses])
    kwargs: dict[str, object] = {
        "rest_base_url": "https://example.invalid/ibmmq/rest/v2",
        "qmgr_name": "QM1",
        "username": "user",
        "password": TEST_PASSWORD,
        "transport": transport,
    }
    if mapping_strict is not None:
        kwargs["mapping_strict"] = mapping_strict
    session = MQRESTSession(**kwargs)  # type: ignore[arg-type]
    return session, transport


# ---------------------------------------------------------------------------
# EnsureResult enum
# ---------------------------------------------------------------------------


class TestEnsureResult:
    def test_values(self) -> None:
        assert EnsureResult.CREATED.value == "created"
        assert EnsureResult.UPDATED.value == "updated"
        assert EnsureResult.UNCHANGED.value == "unchanged"

    def test_members(self) -> None:
        assert set(EnsureResult) == {
            EnsureResult.CREATED,
            EnsureResult.UPDATED,
            EnsureResult.UNCHANGED,
        }


# ---------------------------------------------------------------------------
# _values_match helper
# ---------------------------------------------------------------------------


class TestValuesMatch:
    def test_string_match(self) -> None:
        assert _values_match("ENABLED", "ENABLED") is True

    def test_case_insensitive(self) -> None:
        assert _values_match("ENABLED", "enabled") is True
        assert _values_match("enabled", "ENABLED") is True

    def test_int_string_match(self) -> None:
        assert _values_match(5, "5") is True
        assert _values_match("5", 5) is True

    def test_whitespace_stripped(self) -> None:
        assert _values_match("YES", " YES ") is True

    def test_mismatch(self) -> None:
        assert _values_match("YES", "NO") is False

    def test_current_none(self) -> None:
        assert _values_match("YES", None) is False


# ---------------------------------------------------------------------------
# ensure_qmgr (singleton — no name, no DEFINE, never CREATED)
# ---------------------------------------------------------------------------


class TestEnsureQmgr:
    def test_unchanged_when_attributes_match(self) -> None:
        display_response = _success_payload([{"DESCR": "existing qmgr"}])
        session, transport = _build_session([display_response])

        result = session.ensure_qmgr(request_parameters={"description": "existing qmgr"})

        assert result is EnsureResult.UNCHANGED
        assert len(transport.recorded_requests) == EXPECT_ONE_REQUEST
        display_payload = transport.recorded_requests[0].payload
        assert display_payload["command"] == "DISPLAY"
        assert display_payload["qualifier"] == "QMGR"
        assert "name" not in display_payload

    def test_updated_when_attributes_differ(self) -> None:
        display_response = _success_payload([{"DESCR": "old descr"}])
        alter_response = _success_payload()
        session, transport = _build_session([display_response, alter_response])

        result = session.ensure_qmgr(request_parameters={"description": "new descr"})

        assert result is EnsureResult.UPDATED
        assert len(transport.recorded_requests) == EXPECT_TWO_REQUESTS
        alter_payload = transport.recorded_requests[1].payload
        assert alter_payload["command"] == "ALTER"
        assert alter_payload["qualifier"] == "QMGR"
        assert "name" not in alter_payload

    def test_only_changed_attributes_sent(self) -> None:
        display_response = _success_payload([{"DESCR": "keep", "ACCTINT": "1800"}])
        alter_response = _success_payload()
        session, transport = _build_session([display_response, alter_response])

        result = session.ensure_qmgr(
            request_parameters={"description": "keep", "accounting_interval": 900},
        )

        assert result is EnsureResult.UPDATED
        alter_payload = transport.recorded_requests[1].payload
        assert alter_payload["parameters"] == {"ACCTINT": 900}

    def test_unchanged_no_params(self) -> None:
        session, transport = _build_session([])

        result = session.ensure_qmgr()

        assert result is EnsureResult.UNCHANGED
        assert len(transport.recorded_requests) == 0

    def test_unchanged_empty_params(self) -> None:
        session, transport = _build_session([])

        result = session.ensure_qmgr(request_parameters={})

        assert result is EnsureResult.UNCHANGED
        assert len(transport.recorded_requests) == 0

    def test_updated_when_display_returns_empty(self) -> None:
        # Edge case: DISPLAY QMGR returns empty (shouldn't happen, but defensive).
        display_response = _success_payload()
        alter_response = _success_payload()
        session, transport = _build_session([display_response, alter_response])

        result = session.ensure_qmgr(request_parameters={"description": "new"})

        assert result is EnsureResult.UPDATED
        assert len(transport.recorded_requests) == EXPECT_TWO_REQUESTS


# ---------------------------------------------------------------------------
# Object does not exist -> CREATED
# ---------------------------------------------------------------------------


class TestEnsureCreated:
    def test_display_error_treated_as_not_found(self) -> None:
        # MQ returns error (reason 2085) for DISPLAY of non-existent object.
        # The ensure method should catch this and proceed to DEFINE.
        display_error_response: dict[str, object] = {
            "commandResponse": [
                {"completionCode": 2, "reasonCode": 2085, "message": ["AMQ8147E: object not found."]},
            ],
            "overallCompletionCode": 2,
            "overallReasonCode": 3008,
        }
        define_response = _success_payload()
        session, transport = _build_session([display_error_response, define_response])

        result = session.ensure_qlocal("TEST.Q", request_parameters={"description": "test"})

        assert result is EnsureResult.CREATED
        assert len(transport.recorded_requests) == EXPECT_TWO_REQUESTS
        define_payload = transport.recorded_requests[1].payload
        assert define_payload["command"] == "DEFINE"

    def test_object_not_found_creates(self) -> None:
        display_response = _success_payload()  # empty commandResponse
        define_response = _success_payload()
        session, transport = _build_session([display_response, define_response])

        result = session.ensure_qlocal("TEST.Q", request_parameters={"description": "test"})

        assert result is EnsureResult.CREATED
        assert len(transport.recorded_requests) == EXPECT_TWO_REQUESTS
        define_payload = transport.recorded_requests[1].payload
        assert define_payload["command"] == "DEFINE"
        assert define_payload["qualifier"] == "QLOCAL"
        assert define_payload["name"] == "TEST.Q"

    def test_object_not_found_no_params_creates(self) -> None:
        display_response = _success_payload()
        define_response = _success_payload()
        session, transport = _build_session([display_response, define_response])

        result = session.ensure_qlocal("TEST.Q")

        assert result is EnsureResult.CREATED
        assert len(transport.recorded_requests) == EXPECT_TWO_REQUESTS
        define_payload = transport.recorded_requests[1].payload
        assert define_payload["command"] == "DEFINE"
        assert "parameters" not in define_payload


# ---------------------------------------------------------------------------
# Object exists, attributes match -> UNCHANGED
# ---------------------------------------------------------------------------


class TestEnsureUnchanged:
    def test_attributes_match_exact(self) -> None:
        # Raw MQSC response uses DESCR; mapping converts to description.
        display_response = _success_payload([{"DESCR": "test"}])
        session, transport = _build_session([display_response])

        result = session.ensure_qlocal("TEST.Q", request_parameters={"description": "test"})

        assert result is EnsureResult.UNCHANGED
        assert len(transport.recorded_requests) == EXPECT_ONE_REQUEST

    def test_case_insensitive_match(self) -> None:
        display_response = _success_payload([{"DESCR": "TEST"}])
        session, transport = _build_session([display_response])

        result = session.ensure_qlocal("TEST.Q", request_parameters={"description": "test"})

        assert result is EnsureResult.UNCHANGED
        assert len(transport.recorded_requests) == EXPECT_ONE_REQUEST

    def test_int_string_match(self) -> None:
        display_response = _success_payload([{"MAXDEPTH": "5000"}])
        session, transport = _build_session([display_response])

        result = session.ensure_qlocal("TEST.Q", request_parameters={"max_queue_depth": 5000})

        assert result is EnsureResult.UNCHANGED
        assert len(transport.recorded_requests) == EXPECT_ONE_REQUEST

    def test_no_request_parameters(self) -> None:
        display_response = _success_payload([{"DESCR": "existing"}])
        session, transport = _build_session([display_response])

        result = session.ensure_qlocal("TEST.Q")

        assert result is EnsureResult.UNCHANGED
        assert len(transport.recorded_requests) == EXPECT_ONE_REQUEST

    def test_empty_request_parameters(self) -> None:
        display_response = _success_payload([{"DESCR": "existing"}])
        session, transport = _build_session([display_response])

        result = session.ensure_qlocal("TEST.Q", request_parameters={})

        assert result is EnsureResult.UNCHANGED
        assert len(transport.recorded_requests) == EXPECT_ONE_REQUEST


# ---------------------------------------------------------------------------
# Object exists, attributes differ -> UPDATED
# ---------------------------------------------------------------------------


class TestEnsureUpdated:
    def test_attributes_differ_alters(self) -> None:
        display_response = _success_payload([{"DESCR": "old"}])
        alter_response = _success_payload()
        session, transport = _build_session([display_response, alter_response])

        result = session.ensure_qlocal("TEST.Q", request_parameters={"description": "new"})

        assert result is EnsureResult.UPDATED
        assert len(transport.recorded_requests) == EXPECT_TWO_REQUESTS
        alter_payload = transport.recorded_requests[1].payload
        assert alter_payload["command"] == "ALTER"
        assert alter_payload["qualifier"] == "QLOCAL"
        assert alter_payload["name"] == "TEST.Q"

    def test_only_changed_attributes_sent(self) -> None:
        display_response = _success_payload([{"DESCR": "old", "MAXDEPTH": "5000"}])
        alter_response = _success_payload()
        session, transport = _build_session([display_response, alter_response])

        result = session.ensure_qlocal(
            "TEST.Q",
            request_parameters={"description": "new", "max_queue_depth": 5000},
        )

        assert result is EnsureResult.UPDATED
        alter_payload = transport.recorded_requests[1].payload
        # max_queue_depth matches (5000 == "5000"), so only description should be sent.
        assert alter_payload["parameters"] == {"DESCR": "new"}

    def test_missing_attribute_treated_as_changed(self) -> None:
        display_response = _success_payload([{"DESCR": "test"}])
        alter_response = _success_payload()
        session, _transport = _build_session([display_response, alter_response])

        result = session.ensure_qlocal(
            "TEST.Q",
            request_parameters={"description": "test", "max_queue_depth": 5000},
        )

        assert result is EnsureResult.UPDATED


# ---------------------------------------------------------------------------
# Display command verification
# ---------------------------------------------------------------------------


class TestDisplayCommand:
    def test_display_uses_correct_qualifier(self) -> None:
        display_response = _success_payload()
        define_response = _success_payload()
        session, transport = _build_session([display_response, define_response])

        session.ensure_qlocal("TEST.Q")

        display_payload = transport.recorded_requests[0].payload
        assert display_payload["command"] == "DISPLAY"
        assert display_payload["qualifier"] == "QUEUE"
        assert display_payload["responseParameters"] == ["all"]

    def test_display_requests_all_attributes(self) -> None:
        display_response = _success_payload()
        define_response = _success_payload()
        session, transport = _build_session([display_response, define_response])

        session.ensure_channel("TEST.CHL")

        display_payload = transport.recorded_requests[0].payload
        assert display_payload["responseParameters"] == ["all"]


# ---------------------------------------------------------------------------
# Each ensure method uses correct qualifier triple
# ---------------------------------------------------------------------------


_QUALIFIER_TRIPLES = [
    ("ensure_qlocal", "QUEUE", "QLOCAL", "QLOCAL"),
    ("ensure_qremote", "QUEUE", "QREMOTE", "QREMOTE"),
    ("ensure_qalias", "QUEUE", "QALIAS", "QALIAS"),
    ("ensure_qmodel", "QUEUE", "QMODEL", "QMODEL"),
    ("ensure_channel", "CHANNEL", "CHANNEL", "CHANNEL"),
    ("ensure_authinfo", "AUTHINFO", "AUTHINFO", "AUTHINFO"),
    ("ensure_listener", "LISTENER", "LISTENER", "LISTENER"),
    ("ensure_namelist", "NAMELIST", "NAMELIST", "NAMELIST"),
    ("ensure_process", "PROCESS", "PROCESS", "PROCESS"),
    ("ensure_service", "SERVICE", "SERVICE", "SERVICE"),
    ("ensure_topic", "TOPIC", "TOPIC", "TOPIC"),
    ("ensure_sub", "SUB", "SUB", "SUB"),
    ("ensure_stgclass", "STGCLASS", "STGCLASS", "STGCLASS"),
    ("ensure_comminfo", "COMMINFO", "COMMINFO", "COMMINFO"),
    ("ensure_cfstruct", "CFSTRUCT", "CFSTRUCT", "CFSTRUCT"),
]


class TestQualifierTriples:
    @pytest.mark.parametrize(
        ("method_name", "display_q", "define_q", "alter_q"),
        _QUALIFIER_TRIPLES,
        ids=[triple[0] for triple in _QUALIFIER_TRIPLES],
    )
    def test_create_uses_correct_qualifiers(
        self,
        method_name: str,
        display_q: str,
        define_q: str,
        alter_q: str,  # noqa: ARG002
    ) -> None:
        display_response = _success_payload()
        define_response = _success_payload()
        session, transport = _build_session([display_response, define_response])

        method = getattr(session, method_name)
        result = method("TEST.OBJ")

        assert result is EnsureResult.CREATED
        display_payload = transport.recorded_requests[0].payload
        assert display_payload["qualifier"] == display_q
        define_payload = transport.recorded_requests[1].payload
        assert define_payload["qualifier"] == define_q

    @pytest.mark.parametrize(
        ("method_name", "display_q", "define_q", "alter_q"),
        _QUALIFIER_TRIPLES,
        ids=[triple[0] for triple in _QUALIFIER_TRIPLES],
    )
    def test_update_uses_correct_qualifiers(
        self,
        method_name: str,
        display_q: str,
        define_q: str,  # noqa: ARG002
        alter_q: str,
    ) -> None:
        # Use DESCR (valid MQSC attr) and lenient mapping so qualifiers
        # without full mapping entries don't raise.
        display_response = _success_payload([{"DESCR": "old"}])
        alter_response = _success_payload()
        session, transport = _build_session(
            [display_response, alter_response],
            mapping_strict=False,
        )

        method = getattr(session, method_name)
        result = method("TEST.OBJ", request_parameters={"description": "new"})

        assert result is EnsureResult.UPDATED
        display_payload = transport.recorded_requests[0].payload
        assert display_payload["qualifier"] == display_q
        alter_payload = transport.recorded_requests[1].payload
        assert alter_payload["qualifier"] == alter_q
