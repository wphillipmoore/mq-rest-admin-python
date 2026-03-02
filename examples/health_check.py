"""Queue manager health check.

Connects to one or more queue managers and checks QMGR status,
command server availability, and listener state. Produces a
pass/fail summary for each queue manager.

Usage::

    uv run python3 examples/health_check.py

Set ``MQ_REST_BASE_URL_QM2`` to also check QM2.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from os import getenv

from pymqrest import MQRESTError, MQRESTSession
from pymqrest.auth import LTPAAuth


@dataclass
class ListenerResult:
    """Health status for a single listener."""

    name: str
    status: str


@dataclass
class QMHealthResult:
    """Health check result for a single queue manager."""

    qmgr_name: str
    reachable: bool = False
    status: str = "UNKNOWN"
    command_server: str = "UNKNOWN"
    listeners: list[ListenerResult] = field(default_factory=list)
    passed: bool = False


def check_health(session: MQRESTSession) -> QMHealthResult:
    """Run a health check against a single queue manager.

    Args:
        session: An authenticated MQRESTSession.

    Returns:
        A QMHealthResult with the check outcome.

    """
    result = QMHealthResult(qmgr_name=session.qmgr_name)

    try:
        qmgr = session.display_qmgr()
    except MQRESTError:
        return result

    result.reachable = True

    if qmgr:
        name = qmgr.get("queue_manager_name", "")
        if isinstance(name, str) and name.strip():
            result.qmgr_name = name.strip()

    qmstatus = session.display_qmstatus()
    if qmstatus:
        status = qmstatus.get("ha_status", "UNKNOWN")
        result.status = str(status).strip()

    cmdserv = session.display_cmdserv()
    if cmdserv:
        status = cmdserv.get("status", "UNKNOWN")
        result.command_server = str(status).strip()

    try:
        listeners = session.display_listener(name="*")
    except MQRESTError:
        listeners = []

    for listener in listeners:
        lname = listener.get("listener_name", "")
        lstatus = listener.get("start_mode", "")
        result.listeners.append(ListenerResult(name=str(lname).strip(), status=str(lstatus).strip()))

    result.passed = result.reachable and result.status != "UNKNOWN"
    return result


def main(sessions: list[MQRESTSession]) -> list[QMHealthResult]:
    """Run health checks against one or more queue managers.

    Args:
        sessions: List of authenticated MQRESTSession instances.

    Returns:
        List of QMHealthResult, one per session.

    """
    results = []
    for session in sessions:
        result = check_health(session)
        results.append(result)

        verdict = "PASS" if result.passed else "FAIL"
        print(f"\n=== {result.qmgr_name}: {verdict} ===")
        print(f"  Reachable:      {result.reachable}")
        print(f"  Status:         {result.status}")
        print(f"  Command server: {result.command_server}")
        print(f"  Listeners:      {len(result.listeners)}")
        for listener in result.listeners:
            print(f"    {listener.name}: {listener.status}")

    return results


if __name__ == "__main__":  # pragma: no cover
    sessions: list[MQRESTSession] = []

    sessions.append(
        MQRESTSession(
            rest_base_url=getenv("MQ_REST_BASE_URL", "https://localhost:9443/ibmmq/rest/v2"),
            qmgr_name=getenv("MQ_QMGR_NAME", "QM1"),
            credentials=LTPAAuth(getenv("MQ_ADMIN_USER", "mqadmin"), getenv("MQ_ADMIN_PASSWORD", "mqadmin")),
            verify_tls=False,
        )
    )

    qm2_url = getenv("MQ_REST_BASE_URL_QM2")
    if qm2_url:
        sessions.append(
            MQRESTSession(
                rest_base_url=qm2_url,
                qmgr_name="QM2",
                credentials=LTPAAuth(getenv("MQ_ADMIN_USER", "mqadmin"), getenv("MQ_ADMIN_PASSWORD", "mqadmin")),
                verify_tls=False,
            )
        )

    main(sessions)
