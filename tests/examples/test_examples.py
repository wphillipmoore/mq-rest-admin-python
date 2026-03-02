from __future__ import annotations

from unittest.mock import MagicMock

from examples.channel_status import main as channel_status_main
from examples.channel_status import report_channel_status
from examples.dlq_inspector import _to_int as dlq_to_int
from examples.dlq_inspector import inspect_dlq
from examples.dlq_inspector import main as dlq_main
from examples.health_check import ListenerResult, check_health
from examples.health_check import main as health_check_main
from examples.provision_environment import (
    ProvisionResult,
    _define,
    _delete,
    provision,
    teardown,
)
from examples.provision_environment import main as provision_main
from examples.queue_depth_monitor import _to_int as qdm_to_int
from examples.queue_depth_monitor import main as qdm_main
from examples.queue_depth_monitor import monitor_queue_depths
from examples.queue_status import main as queue_status_main
from examples.queue_status import report_connection_handles, report_queue_handles
from pymqrest import MQRESTError

EXPECTED_PROVISION_OBJECT_COUNT = 10


# ---------------------------------------------------------------------------
# health_check
# ---------------------------------------------------------------------------


class TestHealthCheck:
    def test_success_path(self, mock_session: MagicMock) -> None:
        mock_session.display_qmgr.return_value = {"queue_manager_name": "QM1"}
        mock_session.display_qmstatus.return_value = {"ha_status": "ACTIVE"}
        mock_session.display_cmdserv.return_value = {"status": "RUNNING"}
        mock_session.display_listener.return_value = [
            {"listener_name": "LIS1", "start_mode": "MANUAL"},
        ]

        result = check_health(mock_session)

        assert result.reachable is True
        assert result.status == "ACTIVE"
        assert result.command_server == "RUNNING"
        assert result.passed is True
        assert len(result.listeners) == 1
        assert result.listeners[0] == ListenerResult(name="LIS1", status="MANUAL")

    def test_display_qmgr_error(self, mock_session: MagicMock) -> None:
        mock_session.display_qmgr.side_effect = MQRESTError("fail")

        result = check_health(mock_session)

        assert result.reachable is False
        assert result.passed is False

    def test_display_listener_error(self, mock_session: MagicMock) -> None:
        mock_session.display_qmgr.return_value = {"queue_manager_name": "QM1"}
        mock_session.display_qmstatus.return_value = {"ha_status": "ACTIVE"}
        mock_session.display_cmdserv.return_value = {"status": "RUNNING"}
        mock_session.display_listener.side_effect = MQRESTError("fail")

        result = check_health(mock_session)

        assert result.listeners == []
        assert result.passed is True

    def test_empty_qmgr_response(self, mock_session: MagicMock) -> None:
        mock_session.display_qmgr.return_value = {}
        mock_session.display_qmstatus.return_value = {}
        mock_session.display_cmdserv.return_value = {}
        mock_session.display_listener.return_value = []

        result = check_health(mock_session)

        assert result.reachable is True
        assert result.qmgr_name == "QM1"
        assert result.status == "UNKNOWN"
        assert result.passed is False

    def test_none_qmgr_response(self, mock_session: MagicMock) -> None:
        mock_session.display_qmgr.return_value = None
        mock_session.display_qmstatus.return_value = None
        mock_session.display_cmdserv.return_value = None
        mock_session.display_listener.return_value = []

        result = check_health(mock_session)

        assert result.reachable is True
        assert result.status == "UNKNOWN"

    def test_qmgr_name_non_string(self, mock_session: MagicMock) -> None:
        mock_session.display_qmgr.return_value = {"queue_manager_name": 123}
        mock_session.display_qmstatus.return_value = {"ha_status": "ACTIVE"}
        mock_session.display_cmdserv.return_value = {"status": "RUNNING"}
        mock_session.display_listener.return_value = []

        result = check_health(mock_session)

        assert result.qmgr_name == "QM1"

    def test_qmgr_name_blank(self, mock_session: MagicMock) -> None:
        mock_session.display_qmgr.return_value = {"queue_manager_name": "   "}
        mock_session.display_qmstatus.return_value = {"ha_status": "ACTIVE"}
        mock_session.display_cmdserv.return_value = {"status": "RUNNING"}
        mock_session.display_listener.return_value = []

        result = check_health(mock_session)

        assert result.qmgr_name == "QM1"

    def test_main_prints_results(self, mock_session: MagicMock) -> None:
        mock_session.display_qmgr.return_value = {"queue_manager_name": "QM1"}
        mock_session.display_qmstatus.return_value = {"ha_status": "ACTIVE"}
        mock_session.display_cmdserv.return_value = {"status": "RUNNING"}
        mock_session.display_listener.return_value = [
            {"listener_name": "LIS1", "start_mode": "MANUAL"},
        ]

        results = health_check_main([mock_session])

        assert len(results) == 1
        assert results[0].passed is True


# ---------------------------------------------------------------------------
# channel_status
# ---------------------------------------------------------------------------


class TestChannelStatus:
    def test_definitions_and_live_status(self, mock_session: MagicMock) -> None:
        mock_session.display_channel.return_value = [
            {"channel_name": "CHL1", "channel_type": "SDR", "connection_name": "host(1414)"},
        ]
        mock_session.display_chstatus.return_value = [
            {"channel_name": "CHL1", "status": "RUNNING"},
        ]

        results = report_channel_status(mock_session)

        assert len(results) == 1
        assert results[0].name == "CHL1"
        assert results[0].defined is True
        assert results[0].status == "RUNNING"

    def test_channel_in_status_not_definitions(self, mock_session: MagicMock) -> None:
        mock_session.display_channel.return_value = []
        mock_session.display_chstatus.return_value = [
            {"channel_name": "GHOST", "status": "RUNNING"},
        ]

        results = report_channel_status(mock_session)

        assert len(results) == 1
        assert results[0].name == "GHOST"
        assert results[0].defined is False

    def test_empty_channel_name_in_definitions(self, mock_session: MagicMock) -> None:
        mock_session.display_channel.return_value = [
            {"channel_name": "", "channel_type": "SDR", "connection_name": ""},
            {"channel_name": "CHL1", "channel_type": "SDR", "connection_name": "host(1414)"},
        ]
        mock_session.display_chstatus.return_value = []

        results = report_channel_status(mock_session)

        assert len(results) == 1
        assert results[0].name == "CHL1"

    def test_empty_channel_name_in_chstatus(self, mock_session: MagicMock) -> None:
        mock_session.display_channel.return_value = []
        mock_session.display_chstatus.return_value = [
            {"channel_name": "", "status": "RUNNING"},
            {"channel_name": "CHL1", "status": "RUNNING"},
        ]

        results = report_channel_status(mock_session)

        assert len(results) == 1
        assert results[0].name == "CHL1"

    def test_chstatus_error(self, mock_session: MagicMock) -> None:
        mock_session.display_channel.return_value = [
            {"channel_name": "CHL1", "channel_type": "RCVR", "connection_name": ""},
        ]
        mock_session.display_chstatus.side_effect = MQRESTError("fail")

        results = report_channel_status(mock_session)

        assert len(results) == 1
        assert results[0].status == "INACTIVE"

    def test_main_with_inactive(self, mock_session: MagicMock) -> None:
        mock_session.display_channel.return_value = [
            {"channel_name": "CHL1", "channel_type": "SDR", "connection_name": "host(1414)"},
        ]
        mock_session.display_chstatus.return_value = []

        results = channel_status_main(mock_session)

        assert len(results) == 1
        assert results[0].status == "INACTIVE"

    def test_main_without_inactive(self, mock_session: MagicMock) -> None:
        mock_session.display_channel.return_value = [
            {"channel_name": "CHL1", "channel_type": "SDR", "connection_name": "host(1414)"},
        ]
        mock_session.display_chstatus.return_value = [
            {"channel_name": "CHL1", "status": "RUNNING"},
        ]

        results = channel_status_main(mock_session)

        assert len(results) == 1
        assert results[0].status == "RUNNING"


# ---------------------------------------------------------------------------
# dlq_inspector
# ---------------------------------------------------------------------------


_QUEUE_DEFAULTS = {
    "open_input_count": 0,
    "open_output_count": 0,
}


def _queue(depth: int = 0, max_depth: int = 5000) -> dict[str, object]:
    return {"current_queue_depth": depth, "max_queue_depth": max_depth, **_QUEUE_DEFAULTS}


class TestDLQInspector:
    def test_dlq_empty(self, mock_session: MagicMock) -> None:
        mock_session.display_qmgr.return_value = {"dead_letter_queue_name": "DLQ"}
        mock_session.display_queue.return_value = [_queue()]

        report = inspect_dlq(mock_session)

        assert report.configured is True
        assert report.current_depth == 0
        assert "empty" in report.suggestion.lower()

    def test_dlq_critical(self, mock_session: MagicMock) -> None:
        mock_session.display_qmgr.return_value = {"dead_letter_queue_name": "DLQ"}
        mock_session.display_queue.return_value = [_queue(depth=950, max_depth=1000)]

        report = inspect_dlq(mock_session)

        assert report.depth_pct >= 90  # noqa: PLR2004
        assert "near capacity" in report.suggestion.lower()

    def test_dlq_has_messages(self, mock_session: MagicMock) -> None:
        mock_session.display_qmgr.return_value = {"dead_letter_queue_name": "DLQ"}
        mock_session.display_queue.return_value = [_queue(depth=10)]

        report = inspect_dlq(mock_session)

        assert report.current_depth == 10  # noqa: PLR2004
        assert "has messages" in report.suggestion.lower()

    def test_dlq_not_configured(self, mock_session: MagicMock) -> None:
        mock_session.display_qmgr.return_value = {"dead_letter_queue_name": ""}

        report = inspect_dlq(mock_session)

        assert report.configured is False
        assert "no dead letter queue configured" in report.suggestion.lower()

    def test_dlq_none_qmgr(self, mock_session: MagicMock) -> None:
        mock_session.display_qmgr.return_value = None

        report = inspect_dlq(mock_session)

        assert report.configured is False

    def test_dlq_queue_not_found(self, mock_session: MagicMock) -> None:
        mock_session.display_qmgr.return_value = {"dead_letter_queue_name": "DLQ"}
        mock_session.display_queue.return_value = []

        report = inspect_dlq(mock_session)

        assert "does not exist" in report.suggestion.lower()

    def test_dlq_zero_max_depth(self, mock_session: MagicMock) -> None:
        mock_session.display_qmgr.return_value = {"dead_letter_queue_name": "DLQ"}
        mock_session.display_queue.return_value = [_queue(max_depth=0)]

        report = inspect_dlq(mock_session)

        assert report.depth_pct == 0.0

    def test_to_int_with_int(self) -> None:
        assert dlq_to_int(42) == 42  # noqa: PLR2004

    def test_to_int_with_str(self) -> None:
        assert dlq_to_int("123") == 123  # noqa: PLR2004

    def test_to_int_with_invalid(self) -> None:
        assert dlq_to_int("abc") == 0

    def test_main_configured(self, mock_session: MagicMock) -> None:
        mock_session.display_qmgr.return_value = {"dead_letter_queue_name": "DLQ"}
        mock_session.display_queue.return_value = [_queue(depth=5)]

        report = dlq_main(mock_session)

        assert report.configured is True
        assert report.dlq_name == "DLQ"

    def test_main_unconfigured(self, mock_session: MagicMock) -> None:
        mock_session.display_qmgr.return_value = {"dead_letter_queue_name": ""}

        report = dlq_main(mock_session)

        assert report.configured is False


# ---------------------------------------------------------------------------
# queue_depth_monitor
# ---------------------------------------------------------------------------


def _local_queue(
    name: str = "Q1",
    qtype: str = "QLOCAL",
    depth: int = 0,
    max_depth: int = 100,
) -> dict[str, object]:
    return {
        "queue_name": name,
        "type": qtype,
        "current_queue_depth": depth,
        "max_queue_depth": max_depth,
        "open_input_count": 0,
        "open_output_count": 0,
    }


class TestQueueDepthMonitor:
    def test_type_filtering_qlocal(self, mock_session: MagicMock) -> None:
        mock_session.display_queue.return_value = [
            _local_queue(name="Q1", depth=10),
            _local_queue(name="Q2", qtype="QREMOTE", max_depth=0),
        ]

        results = monitor_queue_depths(mock_session)

        assert len(results) == 1
        assert results[0].name == "Q1"

    def test_type_filtering_local(self, mock_session: MagicMock) -> None:
        mock_session.display_queue.return_value = [
            _local_queue(qtype="LOCAL", depth=5),
        ]

        results = monitor_queue_depths(mock_session)

        assert len(results) == 1

    def test_threshold_warning(self, mock_session: MagicMock) -> None:
        mock_session.display_queue.return_value = [_local_queue(depth=90)]

        results = monitor_queue_depths(mock_session, threshold_pct=80.0)

        assert results[0].warning is True

    def test_zero_max_depth(self, mock_session: MagicMock) -> None:
        mock_session.display_queue.return_value = [_local_queue(max_depth=0)]

        results = monitor_queue_depths(mock_session)

        assert results[0].depth_pct == 0.0

    def test_to_int_with_int(self) -> None:
        assert qdm_to_int(42) == 42  # noqa: PLR2004

    def test_to_int_with_str(self) -> None:
        assert qdm_to_int("10") == 10  # noqa: PLR2004

    def test_to_int_with_invalid(self) -> None:
        assert qdm_to_int("bad") == 0

    def test_main_output(self, mock_session: MagicMock) -> None:
        mock_session.display_queue.return_value = [
            _local_queue(depth=85, max_depth=100),
        ]

        results = qdm_main(mock_session, threshold_pct=80.0)

        assert len(results) == 1
        assert results[0].warning is True


# ---------------------------------------------------------------------------
# queue_status
# ---------------------------------------------------------------------------


class TestQueueStatus:
    def test_report_queue_handles_success(self, mock_session: MagicMock) -> None:
        mock_session.display_qstatus.return_value = [
            {"queue_name": "Q1", "handle_state": "ACTIVE", "connection_id": "C1", "open_options": "INPUT"},
        ]

        results = report_queue_handles(mock_session)

        assert len(results) == 1
        assert results[0].queue_name == "Q1"

    def test_report_queue_handles_error(self, mock_session: MagicMock) -> None:
        mock_session.display_qstatus.side_effect = MQRESTError("fail")

        results = report_queue_handles(mock_session)

        assert results == []

    def test_report_connection_handles_success(self, mock_session: MagicMock) -> None:
        mock_session.display_conn.return_value = [
            {"connection_id": "C1", "object_name": "Q1", "handle_state": "ACTIVE", "object_type": "QUEUE"},
        ]

        results = report_connection_handles(mock_session)

        assert len(results) == 1
        assert results[0].connection_id == "C1"

    def test_report_connection_handles_error(self, mock_session: MagicMock) -> None:
        mock_session.display_conn.side_effect = MQRESTError("fail")

        results = report_connection_handles(mock_session)

        assert results == []

    def test_main_with_handles(self, mock_session: MagicMock) -> None:
        mock_session.display_qstatus.return_value = [
            {"queue_name": "Q1", "handle_state": "ACTIVE", "connection_id": "C1", "open_options": "INPUT"},
        ]
        mock_session.display_conn.return_value = [
            {"connection_id": "C1", "object_name": "Q1", "handle_state": "ACTIVE", "object_type": "QUEUE"},
        ]

        queue_status_main(mock_session)

    def test_main_empty(self, mock_session: MagicMock) -> None:
        mock_session.display_qstatus.return_value = []
        mock_session.display_conn.return_value = []

        queue_status_main(mock_session)


# ---------------------------------------------------------------------------
# provision_environment
# ---------------------------------------------------------------------------


def _mock_qm(name: str = "QM1") -> MagicMock:
    session = MagicMock()
    session.qmgr_name = name
    return session


class TestProvisionEnvironment:
    def test_define_success(self) -> None:
        result = ProvisionResult()
        session = _mock_qm()

        _define(result, session, "define_qlocal", "TEST.Q", {"replace": "yes"})

        assert "QM1/TEST.Q" in result.objects_created
        assert result.objects_failed == []

    def test_define_error(self) -> None:
        result = ProvisionResult()
        session = _mock_qm()
        session.define_qlocal.side_effect = MQRESTError("fail")

        _define(result, session, "define_qlocal", "TEST.Q", {"replace": "yes"})

        assert result.objects_created == []
        assert "QM1/TEST.Q" in result.objects_failed

    def test_delete_success(self) -> None:
        failures: list[str] = []
        session = _mock_qm()

        _delete(failures, session, "delete_queue", "TEST.Q", "QM1")

        assert failures == []

    def test_delete_error(self) -> None:
        failures: list[str] = []
        session = _mock_qm()
        session.delete_queue.side_effect = MQRESTError("fail")

        _delete(failures, session, "delete_queue", "TEST.Q", "QM1")

        assert "QM1/TEST.Q" in failures

    def test_provision_verified(self) -> None:
        qm1, qm2 = _mock_qm("QM1"), _mock_qm("QM2")
        qm1.display_queue.return_value = [{"q": 1}, {"q": 2}, {"q": 3}]
        qm2.display_queue.return_value = [{"q": 1}, {"q": 2}, {"q": 3}]

        result = provision(qm1, qm2)

        assert result.verified is True
        assert len(result.objects_created) == EXPECTED_PROVISION_OBJECT_COUNT

    def test_provision_verification_fail(self) -> None:
        qm1, qm2 = _mock_qm("QM1"), _mock_qm("QM2")
        qm1.display_queue.return_value = [{"q": 1}]
        qm2.display_queue.return_value = [{"q": 1}]

        result = provision(qm1, qm2)

        assert result.verified is False

    def test_provision_verification_error(self) -> None:
        qm1, qm2 = _mock_qm("QM1"), _mock_qm("QM2")
        qm1.display_queue.side_effect = MQRESTError("fail")

        result = provision(qm1, qm2)

        assert result.verified is False

    def test_teardown(self) -> None:
        qm1, qm2 = _mock_qm("QM1"), _mock_qm("QM2")

        failures = teardown(qm1, qm2)

        assert failures == []

    def test_teardown_with_failures(self) -> None:
        qm1, qm2 = _mock_qm("QM1"), _mock_qm("QM2")
        qm1.delete_channel.side_effect = MQRESTError("fail")
        qm1.delete_queue.side_effect = MQRESTError("fail")

        failures = teardown(qm1, qm2)

        assert len(failures) > 0

    def test_main_with_failures(self) -> None:
        qm1, qm2 = _mock_qm("QM1"), _mock_qm("QM2")
        qm1.define_qlocal.side_effect = MQRESTError("fail")
        qm1.display_queue.return_value = [{"q": 1}, {"q": 2}, {"q": 3}]
        qm2.display_queue.return_value = [{"q": 1}, {"q": 2}, {"q": 3}]

        result = provision_main(qm1, qm2)

        assert len(result.objects_failed) > 0

    def test_main_clean(self) -> None:
        qm1, qm2 = _mock_qm("QM1"), _mock_qm("QM2")
        qm1.display_queue.return_value = [{"q": 1}, {"q": 2}, {"q": 3}]
        qm2.display_queue.return_value = [{"q": 1}, {"q": 2}, {"q": 3}]

        result = provision_main(qm1, qm2)

        assert result.verified is True

    def test_main_teardown_failures(self) -> None:
        qm1, qm2 = _mock_qm("QM1"), _mock_qm("QM2")
        qm1.display_queue.return_value = [{"q": 1}, {"q": 2}, {"q": 3}]
        qm2.display_queue.return_value = [{"q": 1}, {"q": 2}, {"q": 3}]
        qm1.delete_channel.side_effect = MQRESTError("fail")

        result = provision_main(qm1, qm2)

        assert result is not None
