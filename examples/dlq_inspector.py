"""Dead letter queue inspector.

Checks the dead letter queue configuration for a queue manager,
reports its depth and capacity, and suggests actions when messages
are present.

Usage::

    uv run python3 examples/dlq_inspector.py
"""

from __future__ import annotations

from dataclasses import dataclass
from os import getenv

from pymqrest import MQRESTSession

CRITICAL_DEPTH_PCT = 90


@dataclass
class DLQReport:
    """Dead letter queue inspection result."""

    qmgr_name: str
    dlq_name: str
    configured: bool
    current_depth: int
    max_depth: int
    depth_pct: float
    open_input: int
    open_output: int
    suggestion: str


def inspect_dlq(session: MQRESTSession) -> DLQReport:
    """Inspect the dead letter queue for a queue manager.

    Args:
        session: An authenticated MQRESTSession.

    Returns:
        A DLQReport with the inspection findings.

    """
    qmgr = session.display_qmgr()

    dlq_name = ""
    if qmgr:
        dlq_name = str(qmgr.get("dead_letter_q_name", "")).strip()

    if not dlq_name:
        return DLQReport(
            qmgr_name=session.qmgr_name,
            dlq_name="",
            configured=False,
            current_depth=0,
            max_depth=0,
            depth_pct=0.0,
            open_input=0,
            open_output=0,
            suggestion="No dead letter queue configured. Define one with ALTER QMGR DEADQ.",
        )

    queues = session.display_queue(name=dlq_name)
    if not queues:
        return DLQReport(
            qmgr_name=session.qmgr_name,
            dlq_name=dlq_name,
            configured=True,
            current_depth=0,
            max_depth=0,
            depth_pct=0.0,
            open_input=0,
            open_output=0,
            suggestion=f"DLQ '{dlq_name}' is configured but the queue does not exist.",
        )

    dlq = queues[0]
    current_depth = _to_int(dlq.get("current_queue_depth", 0))
    max_depth = _to_int(dlq.get("max_queue_depth", 0))
    open_input = _to_int(dlq.get("open_input_count", 0))
    open_output = _to_int(dlq.get("open_output_count", 0))
    depth_pct = (current_depth / max_depth * 100.0) if max_depth > 0 else 0.0

    if current_depth == 0:
        suggestion = "DLQ is empty. No action needed."
    elif depth_pct >= CRITICAL_DEPTH_PCT:
        suggestion = "DLQ is near capacity. Investigate and clear undeliverable messages urgently."
    elif current_depth > 0:
        suggestion = "DLQ has messages. Investigate undeliverable messages."
    else:
        suggestion = "DLQ is healthy."

    return DLQReport(
        qmgr_name=session.qmgr_name,
        dlq_name=dlq_name,
        configured=True,
        current_depth=current_depth,
        max_depth=max_depth,
        depth_pct=depth_pct,
        open_input=open_input,
        open_output=open_output,
        suggestion=suggestion,
    )


def main(session: MQRESTSession) -> DLQReport:
    """Run the DLQ inspection and print results.

    Args:
        session: An authenticated MQRESTSession.

    Returns:
        A DLQReport with the inspection findings.

    """
    report = inspect_dlq(session)

    print(f"\n=== Dead Letter Queue: {report.qmgr_name} ===")
    print(f"  Configured: {report.configured}")
    print(f"  DLQ name:   {report.dlq_name or '(none)'}")

    if report.configured and report.dlq_name:
        print(f"  Depth:      {report.current_depth} / {report.max_depth} ({report.depth_pct:.1f}%)")
        print(f"  Input:      {report.open_input}")
        print(f"  Output:     {report.open_output}")

    print(f"  Suggestion: {report.suggestion}")

    return report


def _to_int(value: object) -> int:
    """Safely convert a value to int."""
    if isinstance(value, int):
        return value
    try:
        return int(str(value))
    except (TypeError, ValueError):
        return 0


if __name__ == "__main__":
    session = MQRESTSession(
        rest_base_url=getenv("MQ_REST_BASE_URL", "https://localhost:9443/ibmmq/rest/v2"),
        qmgr_name=getenv("MQ_QMGR_NAME", "QM1"),
        username=getenv("MQ_ADMIN_USER", "mqadmin"),
        password=getenv("MQ_ADMIN_PASSWORD", "mqadmin"),
        verify_tls=False,
    )

    main(session)
