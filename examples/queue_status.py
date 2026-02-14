"""Queue status and connection handle report.

Demonstrates ``DISPLAY QSTATUS TYPE(HANDLE)`` and ``DISPLAY CONN
TYPE(HANDLE)`` queries, showing how ``pymqrest`` transparently flattens
the nested ``objects`` response structure into uniform flat dicts.

Usage::

    uv run python3 examples/queue_status.py
"""

from __future__ import annotations

from dataclasses import dataclass
from os import getenv

from pymqrest import MQRESTError, MQRESTSession
from pymqrest.auth import LTPAAuth


@dataclass
class QueueHandleInfo:
    """Per-handle queue status information."""

    queue_name: str
    handle_state: str
    connection_id: str
    open_options: str


@dataclass
class ConnectionHandleInfo:
    """Per-handle connection information."""

    connection_id: str
    object_name: str
    handle_state: str
    object_type: str


def report_queue_handles(session: MQRESTSession) -> list[QueueHandleInfo]:
    """Report per-handle queue status entries.

    Calls ``DISPLAY QSTATUS * TYPE(HANDLE)`` which returns nested
    ``objects`` arrays in the raw API response.  ``pymqrest`` flattens
    these automatically so each result is a flat dict with both
    queue-level and handle-level attributes.

    Args:
        session: An authenticated MQRESTSession.

    Returns:
        List of QueueHandleInfo for each active handle.

    """
    try:
        entries = session.display_qstatus(
            name="*",
            request_parameters={"type": "HANDLE"},
        )
    except MQRESTError:
        return []

    return [
        QueueHandleInfo(
            queue_name=str(entry.get("queue_name", "")).strip(),
            handle_state=str(entry.get("handle_state", "")).strip(),
            connection_id=str(entry.get("connection_id", "")).strip(),
            open_options=str(entry.get("open_options", "")).strip(),
        )
        for entry in entries
    ]


def report_connection_handles(session: MQRESTSession) -> list[ConnectionHandleInfo]:
    """Report per-handle connection entries.

    Calls ``DISPLAY CONN * TYPE(HANDLE)`` which also returns nested
    ``objects`` arrays.  Each flat result contains both connection-scoped
    and handle-scoped attributes.

    Args:
        session: An authenticated MQRESTSession.

    Returns:
        List of ConnectionHandleInfo for each active handle.

    """
    try:
        entries = session.display_conn(
            name="*",
            request_parameters={"connection_info_type": "HANDLE"},
        )
    except MQRESTError:
        return []

    return [
        ConnectionHandleInfo(
            connection_id=str(entry.get("connection_id", "")).strip(),
            object_name=str(entry.get("object_name", "")).strip(),
            handle_state=str(entry.get("handle_state", "")).strip(),
            object_type=str(entry.get("object_type", "")).strip(),
        )
        for entry in entries
    ]


def main(session: MQRESTSession) -> None:
    """Run the queue status and connection handle report.

    Args:
        session: An authenticated MQRESTSession.

    """
    queue_handles = report_queue_handles(session)

    print(f"\n{'Queue':<30} {'Handle State':<15} {'Connection ID':<30} {'Open Options'}")
    print("-" * 90)
    for info in queue_handles:
        print(f"{info.queue_name:<30} {info.handle_state:<15} {info.connection_id:<30} {info.open_options}")

    if not queue_handles:
        print("  (no active queue handles)")

    conn_handles = report_connection_handles(session)

    print(f"\n{'Connection ID':<30} {'Object Name':<30} {'Handle State':<15} {'Object Type'}")
    print("-" * 90)
    for conn_info in conn_handles:
        print(
            f"{conn_info.connection_id:<30} {conn_info.object_name:<30} {conn_info.handle_state:<15} {conn_info.object_type}"
        )

    if not conn_handles:
        print("  (no active connection handles)")


if __name__ == "__main__":
    session = MQRESTSession(
        rest_base_url=getenv("MQ_REST_BASE_URL", "https://localhost:9443/ibmmq/rest/v2"),
        qmgr_name=getenv("MQ_QMGR_NAME", "QM1"),
        credentials=LTPAAuth(getenv("MQ_ADMIN_USER", "mqadmin"), getenv("MQ_ADMIN_PASSWORD", "mqadmin")),
        verify_tls=False,
    )

    main(session)
