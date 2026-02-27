"""Tests for synchronous start/stop/restart wrappers."""

from __future__ import annotations

import json
import time
from dataclasses import dataclass
from typing import TYPE_CHECKING

import pytest

from pymqrest.auth import BasicAuth
from pymqrest.exceptions import MQRESTError, MQRESTTimeoutError
from pymqrest.session import MQRESTSession, TransportResponse
from pymqrest.sync import SyncConfig, SyncOperation, SyncResult

if TYPE_CHECKING:
    from collections.abc import Mapping, Sequence

TEST_PASSWORD = "pass"
EXPECT_ONE_POLL = 1
EXPECT_TWO_POLLS = 2
EXPECT_THREE_POLLS = 3
EXPECT_FOUR_POLLS = 4
EXPECT_TWO_REQUESTS = 2
EXPECT_FOUR_REQUESTS = 4
ELAPSED_ONE_SECOND = 1.0
ELAPSED_HALF_SECOND = 0.5
ELAPSED_TWO_SECONDS = 2.0
ELAPSED_THREE_SECONDS = 3.0
ELAPSED_FOUR_SECONDS = 4.0
EXPECT_ELAPSED_2_5 = 2.5
CUSTOM_TIMEOUT_SECONDS = 10.0
EXPECT_ELAPSED_30_5 = 30.5
DEFAULT_TIMEOUT_SECONDS = 30.0
TIMEOUT_POLL_OVERSHOOT = 35


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
    map_attributes: bool = True,
) -> tuple[MQRESTSession, MultiResponseTransport]:
    transport = MultiResponseTransport([_make_response(resp) for resp in responses])
    session = MQRESTSession(
        rest_base_url="https://example.invalid/ibmmq/rest/v2",
        qmgr_name="QM1",
        credentials=BasicAuth("user", TEST_PASSWORD),
        transport=transport,
        map_attributes=map_attributes,
    )
    return session, transport


# ---------------------------------------------------------------------------
# SyncConfig dataclass
# ---------------------------------------------------------------------------


class TestSyncConfig:
    def test_defaults(self) -> None:
        sync_config = SyncConfig()
        assert sync_config.timeout_seconds == DEFAULT_TIMEOUT_SECONDS
        assert sync_config.poll_interval_seconds == ELAPSED_ONE_SECOND

    def test_custom_values(self) -> None:
        sync_config = SyncConfig(timeout_seconds=10.0, poll_interval_seconds=0.5)
        assert sync_config.timeout_seconds == CUSTOM_TIMEOUT_SECONDS
        assert sync_config.poll_interval_seconds == ELAPSED_HALF_SECOND

    def test_frozen(self) -> None:
        sync_config = SyncConfig()
        with pytest.raises(AttributeError):
            sync_config.timeout_seconds = 99.0  # type: ignore[misc]


# ---------------------------------------------------------------------------
# SyncOperation enum
# ---------------------------------------------------------------------------


class TestSyncOperation:
    def test_values(self) -> None:
        assert SyncOperation.STARTED.value == "started"
        assert SyncOperation.STOPPED.value == "stopped"
        assert SyncOperation.RESTARTED.value == "restarted"

    def test_members(self) -> None:
        assert set(SyncOperation) == {
            SyncOperation.STARTED,
            SyncOperation.STOPPED,
            SyncOperation.RESTARTED,
        }


# ---------------------------------------------------------------------------
# SyncResult dataclass
# ---------------------------------------------------------------------------


class TestSyncResult:
    def test_attributes(self) -> None:
        result = SyncResult(SyncOperation.STARTED, polls=3, elapsed_seconds=2.5)
        assert result.operation is SyncOperation.STARTED
        assert result.polls == EXPECT_THREE_POLLS
        assert result.elapsed_seconds == EXPECT_ELAPSED_2_5

    def test_frozen(self) -> None:
        result = SyncResult(SyncOperation.STOPPED, polls=1, elapsed_seconds=1.0)
        with pytest.raises(AttributeError):
            result.polls = 99  # type: ignore[misc]


# ---------------------------------------------------------------------------
# MQRESTTimeoutError
# ---------------------------------------------------------------------------


class TestMQRESTTimeoutError:
    def test_attributes(self) -> None:
        error = MQRESTTimeoutError(
            "timed out",
            name="MY.CHL",
            operation="start",
            elapsed=30.5,
        )
        assert str(error) == "timed out"
        assert error.name == "MY.CHL"
        assert error.operation == "start"
        assert error.elapsed == EXPECT_ELAPSED_30_5

    def test_is_mqrest_error(self) -> None:
        error = MQRESTTimeoutError("t", name="X", operation="stop", elapsed=1.0)
        assert isinstance(error, MQRESTError)


# ---------------------------------------------------------------------------
# Fake clock fixture
# ---------------------------------------------------------------------------


@pytest.fixture
def _fake_clock(monkeypatch: pytest.MonkeyPatch) -> None:
    """Patch time.sleep and time.monotonic for deterministic polling.

    Each call to time.sleep advances the fake clock by the requested
    number of seconds.
    """
    clock = [0.0]

    def fake_monotonic() -> float:
        return clock[0]

    def fake_sleep(seconds: float) -> None:
        clock[0] += seconds

    monkeypatch.setattr(time, "monotonic", fake_monotonic)
    monkeypatch.setattr(time, "sleep", fake_sleep)


# ---------------------------------------------------------------------------
# Channel start/stop/restart
# ---------------------------------------------------------------------------


@pytest.mark.usefixtures("_fake_clock")
class TestStartChannelSync:
    def test_running_on_first_poll(self) -> None:
        start_response = _success_payload()
        status_response = _success_payload([{"STATUS": "RUNNING"}])
        session, transport = _build_session([start_response, status_response])

        result = session.start_channel_sync("MY.CHL")

        assert result.operation is SyncOperation.STARTED
        assert result.polls == EXPECT_ONE_POLL
        assert result.elapsed_seconds == ELAPSED_ONE_SECOND
        assert len(transport.recorded_requests) == EXPECT_TWO_REQUESTS
        assert transport.recorded_requests[0].payload["command"] == "START"
        assert transport.recorded_requests[0].payload["qualifier"] == "CHANNEL"
        assert transport.recorded_requests[0].payload["name"] == "MY.CHL"
        assert transport.recorded_requests[1].payload["command"] == "DISPLAY"
        assert transport.recorded_requests[1].payload["qualifier"] == "CHSTATUS"

    def test_running_after_multiple_polls(self) -> None:
        start_response = _success_payload()
        initializing = _success_payload([{"STATUS": "INITIALIZING"}])
        running = _success_payload([{"STATUS": "RUNNING"}])
        session, _transport = _build_session([start_response, initializing, initializing, running])

        result = session.start_channel_sync("MY.CHL")

        assert result.operation is SyncOperation.STARTED
        assert result.polls == EXPECT_THREE_POLLS
        assert result.elapsed_seconds == ELAPSED_THREE_SECONDS

    def test_timeout_raises(self) -> None:
        start_response = _success_payload()
        initializing_responses = [_success_payload([{"STATUS": "INITIALIZING"}])] * TIMEOUT_POLL_OVERSHOOT
        session, _transport = _build_session([start_response, *initializing_responses])

        with pytest.raises(MQRESTTimeoutError) as exc_info:
            session.start_channel_sync("MY.CHL")

        assert exc_info.value.name == "MY.CHL"
        assert exc_info.value.operation == "start"
        assert exc_info.value.elapsed >= DEFAULT_TIMEOUT_SECONDS

    def test_custom_config(self) -> None:
        start_response = _success_payload()
        running = _success_payload([{"STATUS": "RUNNING"}])
        session, _transport = _build_session([start_response, running])

        sync_config = SyncConfig(timeout_seconds=5.0, poll_interval_seconds=0.5)
        result = session.start_channel_sync("MY.CHL", config=sync_config)

        assert result.operation is SyncOperation.STARTED
        assert result.elapsed_seconds == ELAPSED_HALF_SECOND

    def test_works_with_mapping_disabled(self) -> None:
        """Polling works when mapping is off (raw MQSC STATUS key)."""
        start_response = _success_payload()
        status_response = _success_payload([{"STATUS": "RUNNING"}])
        session, _transport = _build_session(
            [start_response, status_response],
            map_attributes=False,
        )

        result = session.start_channel_sync("MY.CHL")

        assert result.operation is SyncOperation.STARTED


@pytest.mark.usefixtures("_fake_clock")
class TestStopChannelSync:
    def test_stopped_on_first_poll(self) -> None:
        stop_response = _success_payload()
        status_response = _success_payload([{"STATUS": "STOPPED"}])
        session, transport = _build_session([stop_response, status_response])

        result = session.stop_channel_sync("MY.CHL")

        assert result.operation is SyncOperation.STOPPED
        assert result.polls == EXPECT_ONE_POLL
        assert len(transport.recorded_requests) == EXPECT_TWO_REQUESTS
        assert transport.recorded_requests[0].payload["command"] == "STOP"
        assert transport.recorded_requests[0].payload["qualifier"] == "CHANNEL"

    def test_empty_result_means_stopped_for_channel(self) -> None:
        """Channels may disappear from CHSTATUS when stopped."""
        stop_response = _success_payload()
        empty_status = _success_payload()
        session, _transport = _build_session([stop_response, empty_status])

        result = session.stop_channel_sync("MY.CHL")

        assert result.operation is SyncOperation.STOPPED
        assert result.polls == EXPECT_ONE_POLL

    def test_timeout_raises(self) -> None:
        stop_response = _success_payload()
        stopping_responses = [_success_payload([{"STATUS": "STOPPING"}])] * TIMEOUT_POLL_OVERSHOOT
        session, _transport = _build_session([stop_response, *stopping_responses])

        with pytest.raises(MQRESTTimeoutError) as exc_info:
            session.stop_channel_sync("MY.CHL")

        assert exc_info.value.name == "MY.CHL"
        assert exc_info.value.operation == "stop"


@pytest.mark.usefixtures("_fake_clock")
class TestRestartChannel:
    def test_restart_sequence(self) -> None:
        stop_response = _success_payload()
        stopped_status = _success_payload([{"STATUS": "STOPPED"}])
        start_response = _success_payload()
        running_status = _success_payload([{"STATUS": "RUNNING"}])
        session, transport = _build_session(
            [stop_response, stopped_status, start_response, running_status],
        )

        result = session.restart_channel("MY.CHL")

        assert result.operation is SyncOperation.RESTARTED
        assert result.polls == EXPECT_TWO_POLLS
        assert result.elapsed_seconds == ELAPSED_TWO_SECONDS
        assert len(transport.recorded_requests) == EXPECT_FOUR_REQUESTS
        assert transport.recorded_requests[0].payload["command"] == "STOP"
        assert transport.recorded_requests[1].payload["command"] == "DISPLAY"
        assert transport.recorded_requests[2].payload["command"] == "START"
        assert transport.recorded_requests[3].payload["command"] == "DISPLAY"

    def test_restart_combined_totals(self) -> None:
        stop_response = _success_payload()
        stopping = _success_payload([{"STATUS": "STOPPING"}])
        stopped = _success_payload([{"STATUS": "STOPPED"}])
        start_response = _success_payload()
        initializing = _success_payload([{"STATUS": "INITIALIZING"}])
        running = _success_payload([{"STATUS": "RUNNING"}])
        session, _transport = _build_session(
            [stop_response, stopping, stopped, start_response, initializing, running],
        )

        result = session.restart_channel("MY.CHL")

        assert result.operation is SyncOperation.RESTARTED
        assert result.polls == EXPECT_FOUR_POLLS
        assert result.elapsed_seconds == ELAPSED_FOUR_SECONDS


# ---------------------------------------------------------------------------
# Listener start/stop/restart
# ---------------------------------------------------------------------------


@pytest.mark.usefixtures("_fake_clock")
class TestStartListenerSync:
    def test_running_on_first_poll(self) -> None:
        start_response = _success_payload()
        status_response = _success_payload([{"STATUS": "RUNNING"}])
        session, transport = _build_session([start_response, status_response])

        result = session.start_listener_sync("MY.LIS")

        assert result.operation is SyncOperation.STARTED
        assert result.polls == EXPECT_ONE_POLL
        assert len(transport.recorded_requests) == EXPECT_TWO_REQUESTS
        assert transport.recorded_requests[0].payload["command"] == "START"
        assert transport.recorded_requests[0].payload["qualifier"] == "LISTENER"
        assert transport.recorded_requests[1].payload["qualifier"] == "LSSTATUS"


@pytest.mark.usefixtures("_fake_clock")
class TestStopListenerSync:
    def test_stopped_on_first_poll(self) -> None:
        stop_response = _success_payload()
        status_response = _success_payload([{"STATUS": "STOPPED"}])
        session, transport = _build_session([stop_response, status_response])

        result = session.stop_listener_sync("MY.LIS")

        assert result.operation is SyncOperation.STOPPED
        assert result.polls == EXPECT_ONE_POLL
        assert transport.recorded_requests[0].payload["qualifier"] == "LISTENER"

    def test_empty_result_does_not_mean_stopped_for_listener(self) -> None:
        """Unlike channels, listeners should NOT treat empty as stopped."""
        stop_response = _success_payload()
        empty_status = _success_payload()
        more_empty = [_success_payload()] * TIMEOUT_POLL_OVERSHOOT
        session, _transport = _build_session([stop_response, empty_status, *more_empty])

        with pytest.raises(MQRESTTimeoutError):
            session.stop_listener_sync("MY.LIS")


@pytest.mark.usefixtures("_fake_clock")
class TestRestartListener:
    def test_restart_sequence(self) -> None:
        stop_response = _success_payload()
        stopped_status = _success_payload([{"STATUS": "STOPPED"}])
        start_response = _success_payload()
        running_status = _success_payload([{"STATUS": "RUNNING"}])
        session, transport = _build_session(
            [stop_response, stopped_status, start_response, running_status],
        )

        result = session.restart_listener("MY.LIS")

        assert result.operation is SyncOperation.RESTARTED
        assert result.polls == EXPECT_TWO_POLLS
        assert len(transport.recorded_requests) == EXPECT_FOUR_REQUESTS


# ---------------------------------------------------------------------------
# Service start/stop/restart
# ---------------------------------------------------------------------------


@pytest.mark.usefixtures("_fake_clock")
class TestStartServiceSync:
    def test_running_on_first_poll(self) -> None:
        start_response = _success_payload()
        status_response = _success_payload([{"STATUS": "RUNNING"}])
        session, transport = _build_session([start_response, status_response])

        result = session.start_service_sync("MY.SVC")

        assert result.operation is SyncOperation.STARTED
        assert result.polls == EXPECT_ONE_POLL
        assert len(transport.recorded_requests) == EXPECT_TWO_REQUESTS
        assert transport.recorded_requests[0].payload["command"] == "START"
        assert transport.recorded_requests[0].payload["qualifier"] == "SERVICE"
        assert transport.recorded_requests[1].payload["qualifier"] == "SVSTATUS"


@pytest.mark.usefixtures("_fake_clock")
class TestStopServiceSync:
    def test_stopped_on_first_poll(self) -> None:
        stop_response = _success_payload()
        status_response = _success_payload([{"STATUS": "STOPPED"}])
        session, transport = _build_session([stop_response, status_response])

        result = session.stop_service_sync("MY.SVC")

        assert result.operation is SyncOperation.STOPPED
        assert result.polls == EXPECT_ONE_POLL
        assert transport.recorded_requests[0].payload["qualifier"] == "SERVICE"

    def test_empty_result_does_not_mean_stopped_for_service(self) -> None:
        """Unlike channels, services should NOT treat empty as stopped."""
        stop_response = _success_payload()
        empty_responses = [_success_payload()] * (TIMEOUT_POLL_OVERSHOOT + 1)
        session, _transport = _build_session([stop_response, *empty_responses])

        with pytest.raises(MQRESTTimeoutError):
            session.stop_service_sync("MY.SVC")


@pytest.mark.usefixtures("_fake_clock")
class TestRestartService:
    def test_restart_sequence(self) -> None:
        stop_response = _success_payload()
        stopped_status = _success_payload([{"STATUS": "STOPPED"}])
        start_response = _success_payload()
        running_status = _success_payload([{"STATUS": "RUNNING"}])
        session, transport = _build_session(
            [stop_response, stopped_status, start_response, running_status],
        )

        result = session.restart_service("MY.SVC")

        assert result.operation is SyncOperation.RESTARTED
        assert result.polls == EXPECT_TWO_POLLS
        assert len(transport.recorded_requests) == EXPECT_FOUR_REQUESTS


# ---------------------------------------------------------------------------
# Parametrized: correct qualifiers for all object types
# ---------------------------------------------------------------------------

_OBJECT_TYPE_PARAMS = [
    ("start_channel_sync", "START", "CHANNEL", "CHSTATUS"),
    ("start_listener_sync", "START", "LISTENER", "LSSTATUS"),
    ("start_service_sync", "START", "SERVICE", "SVSTATUS"),
    ("stop_channel_sync", "STOP", "CHANNEL", "CHSTATUS"),
    ("stop_listener_sync", "STOP", "LISTENER", "LSSTATUS"),
    ("stop_service_sync", "STOP", "SERVICE", "SVSTATUS"),
]


@pytest.mark.usefixtures("_fake_clock")
class TestObjectTypeQualifiers:
    @pytest.mark.parametrize(
        ("method_name", "expected_command", "expected_qualifier", "expected_status_qualifier"),
        _OBJECT_TYPE_PARAMS,
        ids=[p[0] for p in _OBJECT_TYPE_PARAMS],
    )
    def test_correct_qualifiers_sent(
        self,
        method_name: str,
        expected_command: str,
        expected_qualifier: str,
        expected_status_qualifier: str,
    ) -> None:
        command_response = _success_payload()
        target_status = "RUNNING" if expected_command == "START" else "STOPPED"
        status_response = _success_payload([{"STATUS": target_status}])
        session, transport = _build_session([command_response, status_response])

        method = getattr(session, method_name)
        method("TEST.OBJ")

        assert transport.recorded_requests[0].payload["command"] == expected_command
        assert transport.recorded_requests[0].payload["qualifier"] == expected_qualifier
        assert transport.recorded_requests[1].payload["command"] == "DISPLAY"
        assert transport.recorded_requests[1].payload["qualifier"] == expected_status_qualifier


# ---------------------------------------------------------------------------
# Polling with mapping disabled (raw MQSC status keys)
# ---------------------------------------------------------------------------


@pytest.mark.usefixtures("_fake_clock")
class TestMappingDisabledStatusKeys:
    """Verify polling works with mapping disabled (raw MQSC keys)."""

    def test_listener_raw_status_key(self) -> None:
        start_response = _success_payload()
        status_response = _success_payload([{"STATUS": "RUNNING"}])
        session, _transport = _build_session(
            [start_response, status_response],
            map_attributes=False,
        )

        result = session.start_listener_sync("MY.LIS")

        assert result.operation is SyncOperation.STARTED

    def test_service_raw_status_key(self) -> None:
        start_response = _success_payload()
        status_response = _success_payload([{"STATUS": "RUNNING"}])
        session, _transport = _build_session(
            [start_response, status_response],
            map_attributes=False,
        )

        result = session.start_service_sync("MY.SVC")

        assert result.operation is SyncOperation.STARTED

    def test_channel_raw_status_key(self) -> None:
        stop_response = _success_payload()
        status_response = _success_payload([{"STATUS": "STOPPED"}])
        session, _transport = _build_session(
            [stop_response, status_response],
            map_attributes=False,
        )

        result = session.stop_channel_sync("MY.CHL")

        assert result.operation is SyncOperation.STOPPED
