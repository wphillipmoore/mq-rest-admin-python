"""Channel status report.

Displays channel definitions alongside live channel status, identifies
channels that are defined but not running, and shows connection details.

Usage::

    uv run python3 examples/channel_status.py
"""

from __future__ import annotations

from dataclasses import dataclass
from os import getenv

from pymqrest import MQRESTError, MQRESTSession
from pymqrest.auth import LTPAAuth


@dataclass
class ChannelInfo:
    """Combined channel definition and status information."""

    name: str
    channel_type: str
    connection_name: str
    defined: bool
    status: str


def report_channel_status(session: MQRESTSession) -> list[ChannelInfo]:
    """Report channel definitions and live status.

    Args:
        session: An authenticated MQRESTSession.

    Returns:
        List of ChannelInfo combining definitions and status.

    """
    channels = session.display_channel(name="*")

    definitions: dict[str, dict[str, object]] = {}
    for channel in channels:
        cname = str(channel.get("channel_name", "")).strip()
        if cname:
            definitions[cname] = channel

    live_status: dict[str, str] = {}
    try:
        statuses = session.display_chstatus(name="*")
        for entry in statuses:
            cname = str(entry.get("channel_name", "")).strip()
            cstatus = str(entry.get("status", "")).strip()
            if cname:
                live_status[cname] = cstatus
    except MQRESTError:
        pass

    results: list[ChannelInfo] = []
    for cname, defn in sorted(definitions.items()):
        ctype = str(defn.get("channel_type", "")).strip()
        conname = str(defn.get("connection_name", "")).strip()
        status = live_status.get(cname, "INACTIVE")

        results.append(
            ChannelInfo(
                name=cname,
                channel_type=ctype,
                connection_name=conname,
                defined=True,
                status=status,
            )
        )

    for cname, cstatus in sorted(live_status.items()):
        if cname not in definitions:
            results.append(
                ChannelInfo(
                    name=cname,
                    channel_type="",
                    connection_name="",
                    defined=False,
                    status=cstatus,
                )
            )

    return results


def main(session: MQRESTSession) -> list[ChannelInfo]:
    """Run the channel status report and print results.

    Args:
        session: An authenticated MQRESTSession.

    Returns:
        List of ChannelInfo for all channels.

    """
    results = report_channel_status(session)

    print(f"\n{'Channel':<30} {'Type':<12} {'Connection':<25} {'Defined':<8} {'Status'}")
    print("-" * 90)

    for info in results:
        print(
            f"{info.name:<30} {info.channel_type:<12} {info.connection_name:<25}"
            f" {'Yes' if info.defined else 'No':<8} {info.status}"
        )

    inactive = [c for c in results if c.defined and c.status == "INACTIVE"]
    if inactive:
        print(f"\nDefined but inactive: {', '.join(c.name for c in inactive)}")

    return results


if __name__ == "__main__":
    session = MQRESTSession(
        rest_base_url=getenv("MQ_REST_BASE_URL", "https://localhost:9443/ibmmq/rest/v2"),
        qmgr_name=getenv("MQ_QMGR_NAME", "QM1"),
        credentials=LTPAAuth(getenv("MQ_ADMIN_USER", "mqadmin"), getenv("MQ_ADMIN_PASSWORD", "mqadmin")),
        verify_tls=False,
    )

    main(session)
