"""Integration test scaffolding for MQ REST validation."""

from __future__ import annotations

import contextlib
import subprocess
import time
from dataclasses import dataclass
from os import getenv
from pathlib import Path

import pytest

from pymqrest.auth import BasicAuth, LTPAAuth
from pymqrest.ensure import EnsureAction
from pymqrest.exceptions import MQRESTError
from pymqrest.session import MQRESTSession

INTEGRATION_ENV_FLAG = "PYMQREST_RUN_INTEGRATION"
REPO_ROOT = Path(__file__).resolve().parents[2]
MQ_START_SCRIPT = REPO_ROOT / "scripts/dev/mq_start.sh"
MQ_STOP_SCRIPT = REPO_ROOT / "scripts/dev/mq_stop.sh"
MQ_SEED_SCRIPT = REPO_ROOT / "scripts/dev/mq_seed.sh"
MQ_READY_TIMEOUT_SECONDS = 90.0
MQ_READY_SLEEP_SECONDS = 2.0

SEEDED_QUEUES = (
    "PYMQREST.DEAD.LETTER",
    "PYMQREST.QLOCAL",
    "PYMQREST.QREMOTE",
    "PYMQREST.QALIAS",
    "PYMQREST.QMODEL",
    "PYMQREST.XMITQ",
)
SEEDED_CHANNELS = (
    "PYMQREST.SVRCONN",
    "PYMQREST.SDR",
    "PYMQREST.RCVR",
)
SEEDED_LISTENER = "PYMQREST.LSTR"
SEEDED_TOPIC = "PYMQREST.TOPIC"
SEEDED_NAMELIST = "PYMQREST.NAMELIST"
SEEDED_PROCESS = "PYMQREST.PROC"

TEST_QLOCAL = "PYMQREST.TEST.QLOCAL"
TEST_QREMOTE = "PYMQREST.TEST.QREMOTE"
TEST_QALIAS = "PYMQREST.TEST.QALIAS"
TEST_QMODEL = "PYMQREST.TEST.QMODEL"
TEST_CHANNEL = "PYMQREST.TEST.SVRCONN"
TEST_LISTENER = "PYMQREST.TEST.LSTR"
TEST_PROCESS = "PYMQREST.TEST.PROC"
TEST_TOPIC = "PYMQREST.TEST.TOPIC"
TEST_NAMELIST = "PYMQREST.TEST.NAMELIST"
TEST_ENSURE_QLOCAL = "PYMQREST.ENSURE.QLOCAL"
TEST_ENSURE_CHANNEL = "PYMQREST.ENSURE.CHL"

pytestmark = [pytest.mark.integration, pytest.mark.usefixtures("integration_environment")]


@dataclass(frozen=True)
class IntegrationConfig:
    rest_base_url: str
    admin_user: str
    admin_password: str
    qmgr_name: str
    verify_tls: bool


@dataclass(frozen=True)
class LifecycleCase:
    name: str
    object_name: str
    define_method: str
    display_method: str
    delete_method: str
    define_parameters: dict[str, object]
    alter_method: str | None = None
    alter_parameters: dict[str, object] | None = None
    alter_description: str | None = None


def load_integration_config() -> IntegrationConfig:
    return IntegrationConfig(
        rest_base_url=getenv("MQ_REST_BASE_URL", "https://localhost:9443/ibmmq/rest/v2"),
        admin_user=getenv("MQ_ADMIN_USER", "mqadmin"),
        admin_password=getenv("MQ_ADMIN_PASSWORD", "mqadmin"),
        qmgr_name=getenv("MQ_QMGR_NAME", "QM1"),
        verify_tls=_parse_bool(getenv("MQ_REST_VERIFY_TLS", "false")),
    )


def _parse_bool(value: str | None) -> bool:
    if value is None:
        return False
    normalized = value.strip().lower()
    return normalized in {"1", "true", "yes", "on"}


def _lifecycle_cases() -> list[LifecycleCase]:
    config = load_integration_config()
    return [
        LifecycleCase(
            name="qlocal",
            object_name=TEST_QLOCAL,
            define_method="define_qlocal",
            display_method="display_queue",
            delete_method="delete_queue",
            define_parameters={
                "replace": "YES",
                "default_persistence": "YES",
                "description": "pymqrest test qlocal",
            },
        ),
        LifecycleCase(
            name="qremote",
            object_name=TEST_QREMOTE,
            define_method="define_qremote",
            display_method="display_queue",
            delete_method="delete_queue",
            define_parameters={
                "replace": "YES",
                "remote_queue_name": "PYMQREST.TARGET",
                "remote_queue_manager_name": config.qmgr_name,
                "xmit_q_name": "PYMQREST.XMITQ",
                "description": "pymqrest test qremote",
            },
        ),
        LifecycleCase(
            name="qalias",
            object_name=TEST_QALIAS,
            define_method="define_qalias",
            display_method="display_queue",
            delete_method="delete_queue",
            define_parameters={
                "replace": "YES",
                "target_queue_name": "PYMQREST.QLOCAL",
                "description": "pymqrest test qalias",
            },
        ),
        LifecycleCase(
            name="qmodel",
            object_name=TEST_QMODEL,
            define_method="define_qmodel",
            display_method="display_queue",
            delete_method="delete_queue",
            define_parameters={
                "replace": "YES",
                "definition_type": "TEMPDYN",
                "default_share_option": "SHARED",
                "description": "pymqrest test qmodel",
            },
        ),
        LifecycleCase(
            name="channel",
            object_name=TEST_CHANNEL,
            define_method="define_channel",
            display_method="display_channel",
            delete_method="delete_channel",
            define_parameters={
                "replace": "YES",
                "channel_type": "SVRCONN",
                "transport_type": "TCP",
                "description": "pymqrest test channel",
            },
            alter_method="alter_channel",
            alter_parameters={
                "channel_type": "SVRCONN",
                "description": "pymqrest test channel updated",
            },
            alter_description="pymqrest test channel updated",
        ),
        LifecycleCase(
            name="listener",
            object_name=TEST_LISTENER,
            define_method="define_listener",
            display_method="display_listener",
            delete_method="delete_listener",
            define_parameters={
                "replace": "YES",
                "transport_type": "TCP",
                "port": 1416,
                "control": "QMGR",
                "description": "pymqrest test listener",
            },
            alter_method="alter_listener",
            alter_parameters={
                "transport_type": "TCP",
                "description": "pymqrest test listener updated",
            },
            alter_description="pymqrest test listener updated",
        ),
        LifecycleCase(
            name="process",
            object_name=TEST_PROCESS,
            define_method="define_process",
            display_method="display_process",
            delete_method="delete_process",
            define_parameters={
                "replace": "YES",
                "application_id": "/bin/true",
                "description": "pymqrest test process",
            },
            alter_method="alter_process",
            alter_parameters={
                "description": "pymqrest test process updated",
            },
            alter_description="pymqrest test process updated",
        ),
        LifecycleCase(
            name="topic",
            object_name=TEST_TOPIC,
            define_method="define_topic",
            display_method="display_topic",
            delete_method="delete_topic",
            define_parameters={
                "replace": "YES",
                "topic_string": "pymqrest/test",
                "description": "pymqrest test topic",
            },
            alter_method="alter_topic",
            alter_parameters={
                "description": "pymqrest test topic updated",
            },
            alter_description="pymqrest test topic updated",
        ),
        LifecycleCase(
            name="namelist",
            object_name=TEST_NAMELIST,
            define_method="define_namelist",
            display_method="display_namelist",
            delete_method="delete_namelist",
            define_parameters={
                "replace": "YES",
                "names": "PYMQREST.QLOCAL",
                "description": "pymqrest test namelist",
            },
            alter_method="alter_namelist",
            alter_parameters={
                "description": "pymqrest test namelist updated",
            },
            alter_description="pymqrest test namelist updated",
        ),
    ]


LIFECYCLE_CASES = _lifecycle_cases()


@pytest.fixture(scope="session")
def integration_environment() -> None:
    _require_integration_enabled()
    _run_script(MQ_START_SCRIPT)
    config = load_integration_config()
    _wait_for_rest_ready(config)
    _run_script(MQ_SEED_SCRIPT)
    try:
        yield
    finally:
        _run_script(MQ_STOP_SCRIPT, allow_fail=True)


def test_integration_config_defaults() -> None:
    config = load_integration_config()
    assert config.rest_base_url.startswith("https://")
    assert config.admin_user
    assert config.admin_password
    assert config.qmgr_name


def test_display_qmgr_returns_object() -> None:
    config = load_integration_config()
    session = _build_session(config)

    result = session.display_qmgr()

    assert result is not None
    assert isinstance(result, dict)
    assert _contains_string_value(result, config.qmgr_name)


def test_display_qmstatus_returns_object_or_none() -> None:
    config = load_integration_config()
    session = _build_session(config)

    result = session.display_qmstatus()

    assert result is None or isinstance(result, dict)


def test_display_cmdserv_returns_object_or_none() -> None:
    config = load_integration_config()
    session = _build_session(config)

    result = session.display_cmdserv()

    assert result is None or isinstance(result, dict)


@pytest.mark.parametrize("queue_name", SEEDED_QUEUES)
def test_display_seeded_queues(queue_name: str) -> None:
    config = load_integration_config()
    session = _build_session(config)

    results = session.display_queue(name=queue_name)

    assert results
    assert any(_contains_string_value(result, queue_name) for result in results)


def test_display_qstatus_returns_object() -> None:
    config = load_integration_config()
    session = _build_session(config)

    results = session.display_qstatus(name="PYMQREST.QLOCAL")

    assert results
    assert any(_contains_string_value(result, "PYMQREST.QLOCAL") for result in results)


@pytest.mark.parametrize("channel_name", SEEDED_CHANNELS)
def test_display_seeded_channels(channel_name: str) -> None:
    config = load_integration_config()
    session = _build_session(config)

    results = session.display_channel(name=channel_name)

    assert results
    assert any(_contains_string_value(result, channel_name) for result in results)


def test_display_seeded_listener() -> None:
    config = load_integration_config()
    session = _build_session(config)

    results = session.display_listener(name=SEEDED_LISTENER)

    assert results
    assert any(_contains_string_value(result, SEEDED_LISTENER) for result in results)


def test_display_seeded_topic() -> None:
    config = load_integration_config()
    session = _build_session(config)

    results = session.display_topic(name=SEEDED_TOPIC)

    assert results
    assert any(_contains_string_value(result, SEEDED_TOPIC) for result in results)


def test_display_seeded_namelist() -> None:
    config = load_integration_config()
    session = _build_session(config)

    results = session.display_namelist(name=SEEDED_NAMELIST)

    assert results
    assert any(_contains_string_value(result, SEEDED_NAMELIST) for result in results)


def test_display_seeded_process() -> None:
    config = load_integration_config()
    session = _build_session(config)

    results = session.display_process(name=SEEDED_PROCESS)

    assert results
    assert any(_contains_string_value(result, SEEDED_PROCESS) for result in results)


@pytest.mark.parametrize("case", LIFECYCLE_CASES, ids=lambda case: case.name)
def test_mutating_object_lifecycle(case: LifecycleCase) -> None:
    config = load_integration_config()
    session = _build_session(config)

    _invoke_method(
        session,
        case.define_method,
        name=case.object_name,
        request_parameters=case.define_parameters,
    )
    display_result = _invoke_method(session, case.display_method, name=case.object_name)
    _assert_display_contains_value(display_result, case.object_name, case.display_method)

    if case.alter_method and case.alter_parameters:
        _invoke_method(
            session,
            case.alter_method,
            name=case.object_name,
            request_parameters=case.alter_parameters,
        )
        updated_result = _invoke_method(session, case.display_method, name=case.object_name)
        if case.alter_description:
            matched = _find_matching_object(updated_result, case.object_name)
            assert matched is not None
            description = _get_attribute_case_insensitive(matched, "description")
            if description is None:
                description = _get_attribute_case_insensitive(matched, "DESCR")
            assert description == case.alter_description

    _invoke_method(session, case.delete_method, name=case.object_name)
    try:
        deleted_result = _invoke_method(session, case.display_method, name=case.object_name)
    except MQRESTError:
        return
    assert not _display_contains_value(deleted_result, case.object_name)


def test_ensure_qmgr_lifecycle() -> None:
    config = load_integration_config()
    session = _build_session(config)

    # Read current description so we can restore it.
    qmgr = session.display_qmgr()
    assert qmgr is not None
    original_descr = qmgr.get("description", "")

    test_descr = "pymqrest ensure_qmgr test"

    # Alter to test value.
    result = session.ensure_qmgr(request_parameters={"description": test_descr})
    assert result.action in {EnsureAction.UPDATED, EnsureAction.UNCHANGED}

    # Unchanged (same attributes).
    result = session.ensure_qmgr(request_parameters={"description": test_descr})
    assert result.action is EnsureAction.UNCHANGED

    # Restore original description.
    session.ensure_qmgr(request_parameters={"description": original_descr})


def test_ensure_qlocal_lifecycle() -> None:
    config = load_integration_config()
    session = _build_session(config, mapping_strict=False)

    # Clean up from any prior failed run.
    with contextlib.suppress(MQRESTError):
        session.delete_queue(name=TEST_ENSURE_QLOCAL)

    # Create.
    result = session.ensure_qlocal(
        TEST_ENSURE_QLOCAL,
        request_parameters={"description": "ensure test"},
    )
    assert result.action is EnsureAction.CREATED

    # Unchanged (same attributes).
    result = session.ensure_qlocal(
        TEST_ENSURE_QLOCAL,
        request_parameters={"description": "ensure test"},
    )
    assert result.action is EnsureAction.UNCHANGED

    # Updated (different attribute).
    result = session.ensure_qlocal(
        TEST_ENSURE_QLOCAL,
        request_parameters={"description": "ensure updated"},
    )
    assert result.action is EnsureAction.UPDATED

    # Cleanup.
    session.delete_queue(name=TEST_ENSURE_QLOCAL)


def test_ensure_channel_lifecycle() -> None:
    config = load_integration_config()
    session = _build_session(config, mapping_strict=False)

    # Clean up from any prior failed run.
    with contextlib.suppress(MQRESTError):
        session.delete_channel(name=TEST_ENSURE_CHANNEL)

    # Create.
    result = session.ensure_channel(
        TEST_ENSURE_CHANNEL,
        request_parameters={"channel_type": "SVRCONN", "description": "ensure test"},
    )
    assert result.action is EnsureAction.CREATED

    # Unchanged.
    result = session.ensure_channel(
        TEST_ENSURE_CHANNEL,
        request_parameters={"channel_type": "SVRCONN", "description": "ensure test"},
    )
    assert result.action is EnsureAction.UNCHANGED

    # Updated.
    result = session.ensure_channel(
        TEST_ENSURE_CHANNEL,
        request_parameters={"channel_type": "SVRCONN", "description": "ensure updated"},
    )
    assert result.action is EnsureAction.UPDATED

    # Cleanup.
    session.delete_channel(name=TEST_ENSURE_CHANNEL)


def test_ltpa_auth_display_qmgr() -> None:
    config = load_integration_config()
    session = MQRESTSession(
        rest_base_url=config.rest_base_url,
        qmgr_name=config.qmgr_name,
        credentials=LTPAAuth(config.admin_user, config.admin_password),
        verify_tls=config.verify_tls,
    )

    result = session.display_qmgr()

    assert result is not None
    assert isinstance(result, dict)
    assert _contains_string_value(result, config.qmgr_name)


def _require_integration_enabled() -> None:
    if getenv(INTEGRATION_ENV_FLAG) != "1":
        pytest.skip(f"Set {INTEGRATION_ENV_FLAG}=1 to enable integration tests.")


def _build_session(
    config: IntegrationConfig,
    *,
    map_attributes: bool = True,
    mapping_strict: bool = True,
) -> MQRESTSession:
    return MQRESTSession(
        rest_base_url=config.rest_base_url,
        qmgr_name=config.qmgr_name,
        credentials=BasicAuth(config.admin_user, config.admin_password),
        verify_tls=config.verify_tls,
        map_attributes=map_attributes,
        mapping_strict=mapping_strict,
    )


def _run_script(path: Path, *, allow_fail: bool = False) -> None:
    if not path.exists():
        pytest.fail(f"MQ script not found: {path}")
    try:
        subprocess.run(["bash", str(path)], check=True, cwd=REPO_ROOT)  # noqa: S603,S607
    except subprocess.CalledProcessError as error:
        if allow_fail:
            return
        pytest.fail(f"MQ script failed ({path}): {error}")


def _wait_for_rest_ready(config: IntegrationConfig) -> None:
    session = _build_session(config, map_attributes=False)
    deadline = time.monotonic() + MQ_READY_TIMEOUT_SECONDS
    last_error: Exception | None = None
    while time.monotonic() < deadline:
        try:
            session.display_qmgr()
        except MQRESTError as error:
            last_error = error
            time.sleep(MQ_READY_SLEEP_SECONDS)
        else:
            return
    pytest.fail(f"MQ REST endpoint not ready after {MQ_READY_TIMEOUT_SECONDS}s: {last_error}")


def _contains_string_value(response_object: dict[str, object], expected_value: str) -> bool:
    expected_normalized = expected_value.strip().upper()
    for attribute_value in response_object.values():
        if isinstance(attribute_value, str) and attribute_value.strip().upper() == expected_normalized:
            return True
    return False


def _display_contains_value(result: object, expected_value: str) -> bool:
    matched = _find_matching_object(result, expected_value)
    return matched is not None


def _find_matching_object(result: object, expected_value: str) -> dict[str, object] | None:
    if isinstance(result, dict):
        return result if _contains_string_value(result, expected_value) else None
    if isinstance(result, list):
        for item in result:
            if isinstance(item, dict) and _contains_string_value(item, expected_value):
                return item
    return None


def _assert_display_contains_value(result: object, expected_value: str, method_name: str) -> None:
    if not _display_contains_value(result, expected_value):
        pytest.fail(f"{method_name} did not return expected value {expected_value}.")


def _get_attribute_case_insensitive(attributes: dict[str, object], name: str) -> object | None:
    name_upper = name.upper()
    for key, value in attributes.items():
        if key.upper() == name_upper:
            return value
    return None


def _invoke_method(
    session: MQRESTSession,
    method_name: str,
    *,
    name: str | None = None,
    request_parameters: dict[str, object] | None = None,
    response_parameters: list[str] | None = None,
) -> object:
    method = getattr(session, method_name)
    kwargs: dict[str, object] = {}
    if name is not None:
        kwargs["name"] = name
    if request_parameters is not None:
        kwargs["request_parameters"] = request_parameters
    if response_parameters is not None:
        kwargs["response_parameters"] = response_parameters
    return method(**kwargs)
