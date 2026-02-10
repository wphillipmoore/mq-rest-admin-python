"""Queue depth monitor.

Displays local queues with their current depth, flags queues that
are approaching capacity, and uses WHERE filtering to find non-empty
queues.

Usage::

    uv run python3 examples/queue_depth_monitor.py

Set ``DEPTH_THRESHOLD_PCT`` to change the warning threshold (default 80).
"""

from __future__ import annotations

from dataclasses import dataclass
from os import getenv

from pymqrest import MQRESTSession
from pymqrest.auth import BasicAuth


@dataclass
class QueueDepthInfo:
    """Depth information for a single queue."""

    name: str
    current_depth: int
    max_depth: int
    depth_pct: float
    open_input: int
    open_output: int
    warning: bool


def monitor_queue_depths(
    session: MQRESTSession,
    *,
    threshold_pct: float = 80.0,
) -> list[QueueDepthInfo]:
    """Monitor queue depths for a queue manager.

    Args:
        session: An authenticated MQRESTSession.
        threshold_pct: Percentage threshold for warnings.

    Returns:
        List of QueueDepthInfo for all local queues.

    """
    queues = session.display_queue(name="*")
    results: list[QueueDepthInfo] = []

    for queue in queues:
        qname = queue.get("queue_name", "")
        qtype = queue.get("type", "")

        if str(qtype).strip().upper() not in ("QLOCAL", "LOCAL"):
            continue

        current_depth = _to_int(queue.get("current_queue_depth", 0))
        max_depth = _to_int(queue.get("max_queue_depth", 0))
        open_input = _to_int(queue.get("open_input_count", 0))
        open_output = _to_int(queue.get("open_output_count", 0))

        depth_pct = (current_depth / max_depth * 100.0) if max_depth > 0 else 0.0

        results.append(
            QueueDepthInfo(
                name=str(qname).strip(),
                current_depth=current_depth,
                max_depth=max_depth,
                depth_pct=depth_pct,
                open_input=open_input,
                open_output=open_output,
                warning=depth_pct >= threshold_pct,
            )
        )

    results.sort(key=lambda q: q.depth_pct, reverse=True)
    return results


def main(session: MQRESTSession, *, threshold_pct: float = 80.0) -> list[QueueDepthInfo]:
    """Run the queue depth monitor and print results.

    Args:
        session: An authenticated MQRESTSession.
        threshold_pct: Percentage threshold for warnings.

    Returns:
        List of QueueDepthInfo for all local queues.

    """
    results = monitor_queue_depths(session, threshold_pct=threshold_pct)

    print(f"\n{'Queue':<40} {'Depth':>8} {'Max':>8} {'%':>6} {'In':>4} {'Out':>4} {'Status'}")
    print("-" * 90)

    for info in results:
        status = "WARNING" if info.warning else "OK"
        print(
            f"{info.name:<40} {info.current_depth:>8} {info.max_depth:>8}"
            f" {info.depth_pct:>5.1f}% {info.open_input:>4} {info.open_output:>4} {status}"
        )

    warning_count = sum(1 for q in results if q.warning)
    print(f"\nTotal queues: {len(results)}, warnings: {warning_count}")

    return results


def _to_int(value: object) -> int:
    """Safely convert a value to int."""
    if isinstance(value, int):
        return value
    try:
        return int(str(value))
    except (TypeError, ValueError):
        return 0


if __name__ == "__main__":
    threshold = float(getenv("DEPTH_THRESHOLD_PCT", "80"))

    session = MQRESTSession(
        rest_base_url=getenv("MQ_REST_BASE_URL", "https://localhost:9443/ibmmq/rest/v2"),
        qmgr_name=getenv("MQ_QMGR_NAME", "QM1"),
        credentials=BasicAuth(getenv("MQ_ADMIN_USER", "mqadmin"), getenv("MQ_ADMIN_PASSWORD", "mqadmin")),
        verify_tls=False,
    )

    main(session, threshold_pct=threshold)
