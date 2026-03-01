"""Integration tests for example scripts."""

from __future__ import annotations

from os import getenv

import pytest

from examples.channel_status import report_channel_status
from examples.dlq_inspector import inspect_dlq
from examples.health_check import check_health
from examples.provision_environment import provision, teardown
from examples.queue_depth_monitor import monitor_queue_depths
from examples.queue_status import report_connection_handles, report_queue_handles
from pymqrest.auth import BasicAuth
from pymqrest.session import MQRESTSession

INTEGRATION_ENV_FLAG = "MQ_REST_ADMIN_RUN_INTEGRATION"

pytestmark = [pytest.mark.integration]


def _require_integration() -> None:
    if getenv(INTEGRATION_ENV_FLAG) != "1":
        pytest.skip(f"Set {INTEGRATION_ENV_FLAG}=1 to enable integration tests.")


def _qm1_session() -> MQRESTSession:
    return MQRESTSession(
        rest_base_url=getenv("MQ_REST_BASE_URL", "https://localhost:9443/ibmmq/rest/v2"),
        qmgr_name=getenv("MQ_QMGR_NAME", "QM1"),
        credentials=BasicAuth(getenv("MQ_ADMIN_USER", "mqadmin"), getenv("MQ_ADMIN_PASSWORD", "mqadmin")),
        verify_tls=False,
    )


def _qm2_session() -> MQRESTSession:
    return MQRESTSession(
        rest_base_url=getenv("MQ_REST_BASE_URL_QM2", "https://localhost:9444/ibmmq/rest/v2"),
        qmgr_name="QM2",
        credentials=BasicAuth(getenv("MQ_ADMIN_USER", "mqadmin"), getenv("MQ_ADMIN_PASSWORD", "mqadmin")),
        verify_tls=False,
    )


def test_health_check_qm1() -> None:
    _require_integration()
    session = _qm1_session()
    result = check_health(session)

    assert result.reachable is True
    assert result.passed is True
    assert result.qmgr_name == "QM1"


def test_health_check_qm2() -> None:
    _require_integration()
    session = _qm2_session()
    result = check_health(session)

    assert result.reachable is True
    assert result.passed is True
    assert result.qmgr_name == "QM2"


def test_queue_depth_monitor() -> None:
    _require_integration()
    session = _qm1_session()
    results = monitor_queue_depths(session)

    assert len(results) > 0
    names = [result.name for result in results]
    assert "DEV.QLOCAL" in names


def test_channel_status_report() -> None:
    _require_integration()
    session = _qm1_session()
    results = report_channel_status(session)

    assert len(results) > 0
    names = [result.name for result in results]
    assert "DEV.SVRCONN" in names


def test_dlq_inspector() -> None:
    _require_integration()
    session = _qm1_session()
    report = inspect_dlq(session)

    assert report.configured is True
    assert report.dlq_name == "DEV.DEAD.LETTER"
    assert report.current_depth == 0


def test_queue_status_report() -> None:
    _require_integration()
    session = _qm1_session()

    queue_handles = report_queue_handles(session)
    assert isinstance(queue_handles, list)

    conn_handles = report_connection_handles(session)
    assert isinstance(conn_handles, list)


def test_provision_and_teardown() -> None:
    _require_integration()
    qm1 = _qm1_session()
    qm2 = _qm2_session()

    result = provision(qm1, qm2)

    assert len(result.objects_created) > 0
    assert result.verified is True

    failures = teardown(qm1, qm2)
    assert failures == [] or all("not found" not in msg.lower() for msg in failures)
