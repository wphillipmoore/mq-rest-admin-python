"""Environment provisioner.

Defines a complete set of queues, channels, and remote queue
definitions across two queue managers, then verifies connectivity.
Includes a teardown function to remove all provisioned objects.

Usage::

    uv run python3 examples/provision_environment.py

Requires both QM1 and QM2 to be running. Set ``MQ_REST_BASE_URL_QM2``
to the QM2 REST endpoint (default: ``https://localhost:9444/ibmmq/rest/v2``).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from os import getenv

from pymqrest import MQRESTError, MQRESTSession
from pymqrest.auth import LTPAAuth

PREFIX = "PROV"


@dataclass
class ProvisionResult:
    """Result of the provisioning operation."""

    objects_created: list[str] = field(default_factory=list)
    objects_failed: list[str] = field(default_factory=list)
    verified: bool = False


def provision(qm1: MQRESTSession, qm2: MQRESTSession) -> ProvisionResult:
    """Provision cross-QM objects on both queue managers.

    Args:
        qm1: Session connected to QM1.
        qm2: Session connected to QM2.

    Returns:
        A ProvisionResult describing what was created.

    """
    result = ProvisionResult()

    _define(
        result,
        qm1,
        "define_qlocal",
        f"{PREFIX}.QM1.LOCAL",
        {
            "replace": "yes",
            "default_persistence": "yes",
            "description": "provisioned local queue on QM1",
        },
    )

    _define(
        result,
        qm2,
        "define_qlocal",
        f"{PREFIX}.QM2.LOCAL",
        {
            "replace": "yes",
            "default_persistence": "yes",
            "description": "provisioned local queue on QM2",
        },
    )

    _define(
        result,
        qm1,
        "define_qlocal",
        f"{PREFIX}.QM1.TO.QM2.XMITQ",
        {
            "replace": "yes",
            "usage": "XMITQ",
            "description": "xmit queue QM1 to QM2",
        },
    )

    _define(
        result,
        qm2,
        "define_qlocal",
        f"{PREFIX}.QM2.TO.QM1.XMITQ",
        {
            "replace": "yes",
            "usage": "XMITQ",
            "description": "xmit queue QM2 to QM1",
        },
    )

    _define(
        result,
        qm1,
        "define_qremote",
        f"{PREFIX}.REMOTE.TO.QM2",
        {
            "replace": "yes",
            "remote_queue_name": f"{PREFIX}.QM2.LOCAL",
            "remote_queue_manager_name": "QM2",
            "transmission_queue_name": f"{PREFIX}.QM1.TO.QM2.XMITQ",
            "description": "remote queue QM1 to QM2",
        },
    )

    _define(
        result,
        qm2,
        "define_qremote",
        f"{PREFIX}.REMOTE.TO.QM1",
        {
            "replace": "yes",
            "remote_queue_name": f"{PREFIX}.QM1.LOCAL",
            "remote_queue_manager_name": "QM1",
            "transmission_queue_name": f"{PREFIX}.QM2.TO.QM1.XMITQ",
            "description": "remote queue QM2 to QM1",
        },
    )

    _define(
        result,
        qm1,
        "define_channel",
        f"{PREFIX}.QM1.TO.QM2",
        {
            "replace": "yes",
            "channel_type": "SDR",
            "transport_type": "TCP",
            "connection_name": "qm2(1414)",
            "transmission_queue_name": f"{PREFIX}.QM1.TO.QM2.XMITQ",
            "description": "sender QM1 to QM2",
        },
    )

    _define(
        result,
        qm2,
        "define_channel",
        f"{PREFIX}.QM1.TO.QM2",
        {
            "replace": "yes",
            "channel_type": "RCVR",
            "transport_type": "TCP",
            "description": "receiver QM1 to QM2",
        },
    )

    _define(
        result,
        qm2,
        "define_channel",
        f"{PREFIX}.QM2.TO.QM1",
        {
            "replace": "yes",
            "channel_type": "SDR",
            "transport_type": "TCP",
            "connection_name": "qm1(1414)",
            "transmission_queue_name": f"{PREFIX}.QM2.TO.QM1.XMITQ",
            "description": "sender QM2 to QM1",
        },
    )

    _define(
        result,
        qm1,
        "define_channel",
        f"{PREFIX}.QM2.TO.QM1",
        {
            "replace": "yes",
            "channel_type": "RCVR",
            "transport_type": "TCP",
            "description": "receiver QM2 to QM1",
        },
    )

    # Verify objects exist
    try:
        qm1_queues = qm1.display_queue(name=f"{PREFIX}.*")
        qm2_queues = qm2.display_queue(name=f"{PREFIX}.*")
        result.verified = len(qm1_queues) >= 3 and len(qm2_queues) >= 3  # noqa: PLR2004
    except MQRESTError:
        result.verified = False

    return result


def teardown(qm1: MQRESTSession, qm2: MQRESTSession) -> list[str]:
    """Remove all provisioned objects from both queue managers.

    Args:
        qm1: Session connected to QM1.
        qm2: Session connected to QM2.

    Returns:
        List of objects that could not be deleted.

    """
    failures: list[str] = []

    for session, label in [(qm1, "QM1"), (qm2, "QM2")]:
        for channel in [f"{PREFIX}.QM1.TO.QM2", f"{PREFIX}.QM2.TO.QM1"]:
            _delete(failures, session, "delete_channel", channel, label)

        for queue in [
            f"{PREFIX}.REMOTE.TO.QM1",
            f"{PREFIX}.REMOTE.TO.QM2",
            f"{PREFIX}.QM1.TO.QM2.XMITQ",
            f"{PREFIX}.QM2.TO.QM1.XMITQ",
            f"{PREFIX}.QM1.LOCAL",
            f"{PREFIX}.QM2.LOCAL",
        ]:
            _delete(failures, session, "delete_queue", queue, label)

    return failures


def main(qm1: MQRESTSession, qm2: MQRESTSession) -> ProvisionResult:
    """Provision, report, and tear down the environment.

    Args:
        qm1: Session connected to QM1.
        qm2: Session connected to QM2.

    Returns:
        The ProvisionResult from the provisioning step.

    """
    print("\n=== Provisioning environment ===")
    result = provision(qm1, qm2)

    print(f"\nCreated: {len(result.objects_created)}")
    for obj in result.objects_created:
        print(f"  + {obj}")

    if result.objects_failed:
        print(f"\nFailed: {len(result.objects_failed)}")
        for obj in result.objects_failed:
            print(f"  ! {obj}")

    print(f"\nVerified: {result.verified}")

    print("\n=== Tearing down ===")
    failures = teardown(qm1, qm2)
    if failures:
        print(f"Teardown failures: {failures}")
    else:
        print("Teardown complete.")

    return result


def _define(
    result: ProvisionResult,
    session: MQRESTSession,
    method_name: str,
    name: str,
    parameters: dict[str, object],
) -> None:
    """Define an object and record the outcome."""
    label = f"{session.qmgr_name}/{name}"
    try:
        method = getattr(session, method_name)
        method(name=name, request_parameters=parameters)
        result.objects_created.append(label)
    except MQRESTError:
        result.objects_failed.append(label)


def _delete(
    failures: list[str],
    session: MQRESTSession,
    method_name: str,
    name: str,
    label: str,
) -> None:
    """Delete an object, recording failures silently."""
    try:
        method = getattr(session, method_name)
        method(name=name)
    except MQRESTError:
        failures.append(f"{label}/{name}")


if __name__ == "__main__":
    qm1_session = MQRESTSession(
        rest_base_url=getenv("MQ_REST_BASE_URL", "https://localhost:9443/ibmmq/rest/v2"),
        qmgr_name="QM1",
        credentials=LTPAAuth(getenv("MQ_ADMIN_USER", "mqadmin"), getenv("MQ_ADMIN_PASSWORD", "mqadmin")),
        verify_tls=False,
    )

    qm2_session = MQRESTSession(
        rest_base_url=getenv("MQ_REST_BASE_URL_QM2", "https://localhost:9444/ibmmq/rest/v2"),
        qmgr_name="QM2",
        credentials=LTPAAuth(getenv("MQ_ADMIN_USER", "mqadmin"), getenv("MQ_ADMIN_PASSWORD", "mqadmin")),
        verify_tls=False,
    )

    main(qm1_session, qm2_session)
