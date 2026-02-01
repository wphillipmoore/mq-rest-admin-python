"""Tests for the MQ REST session wrapper."""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
import json

import pytest

from pymqrest.session import (
    MQRESTCommandError,
    MQRESTSession,
    TransportResponse,
)


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

    assert result == {"qmgr_name": "QM1"}


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
