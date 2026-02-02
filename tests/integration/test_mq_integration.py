"""Integration test scaffolding for MQ REST validation."""

from __future__ import annotations

import json
from dataclasses import dataclass
from os import getenv
from pathlib import Path

import pytest

from pymqrest.session import MQRESTSession

INTEGRATION_ENV_FLAG = "PYMQREST_RUN_INTEGRATION"
MUTATING_ENV_FLAG = "PYMQREST_RUN_MUTATING_INTEGRATION"
MUTATING_COMMANDS_ENV = "PYMQREST_MUTATING_COMMANDS"
MUTATING_COMMANDS_FILE_ENV = "PYMQREST_MUTATING_COMMANDS_FILE"
CORE_DISPLAY_METHODS = {
    "display_qmgr",
    "display_qmstatus",
    "display_cmdserv",
    "display_queue",
    "display_qstatus",
    "display_channel",
    "display_listener",
    "display_topic",
    "display_sub",
}
DISPLAY_ENV_OVERRIDES: dict[str, tuple[str, ...]] = {
    "sub": ("MQ_TEST_SUBSCRIPTION", "MQ_TEST_SUB"),
}
OPTIONAL_DISPLAY_METHODS = sorted(
    name
    for name, method in MQRESTSession.__dict__.items()
    if name.startswith("display_") and callable(method) and name not in CORE_DISPLAY_METHODS
)


@dataclass(frozen=True)
class IntegrationConfig:
    rest_base_url: str
    admin_user: str
    admin_password: str
    qmgr_name: str
    verify_tls: bool
    queue_name: str
    channel_name: str
    listener_name: str | None
    topic_name: str | None
    subscription_name: str | None
    map_attributes: bool


def load_integration_config() -> IntegrationConfig:
    return IntegrationConfig(
        rest_base_url=getenv("MQ_REST_BASE_URL", "https://localhost:9443/ibmmq/rest/v2"),
        admin_user=getenv("MQ_ADMIN_USER", "mqadmin"),
        admin_password=getenv("MQ_ADMIN_PASSWORD", "mqadmin"),
        qmgr_name=getenv("MQ_QMGR_NAME", "QM1"),
        verify_tls=_parse_bool(getenv("MQ_REST_VERIFY_TLS", "false")),
        queue_name=getenv("MQ_TEST_QUEUE", "PYMQREST.QLOCAL"),
        channel_name=getenv("MQ_TEST_CHANNEL", "PYMQREST.SVRCONN"),
        listener_name=getenv("MQ_TEST_LISTENER"),
        topic_name=getenv("MQ_TEST_TOPIC"),
        subscription_name=getenv("MQ_TEST_SUBSCRIPTION"),
        map_attributes=_parse_bool(getenv("MQ_REST_MAP_ATTRIBUTES", "false")),
    )


@pytest.mark.integration
def test_integration_config_defaults() -> None:
    config = load_integration_config()
    assert config.rest_base_url.startswith("https://")
    assert config.admin_user
    assert config.admin_password
    assert config.qmgr_name
    assert config.queue_name
    assert config.channel_name


@pytest.mark.integration
def test_display_qmgr_returns_object() -> None:
    _require_integration_enabled()
    config = load_integration_config()
    session = _build_session(config)

    result = session.display_qmgr()

    assert result is not None
    assert isinstance(result, dict)
    assert _contains_string_value(result, config.qmgr_name)


@pytest.mark.integration
def test_display_qmstatus_returns_object_or_none() -> None:
    _require_integration_enabled()
    config = load_integration_config()
    session = _build_session(config)

    result = session.display_qmstatus()

    assert result is None or isinstance(result, dict)


@pytest.mark.integration
def test_display_cmdserv_returns_object_or_none() -> None:
    _require_integration_enabled()
    config = load_integration_config()
    session = _build_session(config)

    result = session.display_cmdserv()

    assert result is None or isinstance(result, dict)


@pytest.mark.integration
def test_display_queue_returns_object() -> None:
    _require_integration_enabled()
    config = load_integration_config()
    session = _build_session(config)

    results = session.display_queue(name=config.queue_name)

    assert results
    assert any(_contains_string_value(result, config.queue_name) for result in results)


@pytest.mark.integration
def test_display_qstatus_returns_object() -> None:
    _require_integration_enabled()
    config = load_integration_config()
    session = _build_session(config)

    results = session.display_qstatus(name=config.queue_name)

    assert results
    assert any(_contains_string_value(result, config.queue_name) for result in results)


@pytest.mark.integration
def test_display_channel_returns_object() -> None:
    _require_integration_enabled()
    config = load_integration_config()
    session = _build_session(config)

    results = session.display_channel(name=config.channel_name)

    assert results
    assert any(_contains_string_value(result, config.channel_name) for result in results)


@pytest.mark.integration
def test_display_listener_returns_object_when_configured() -> None:
    _require_integration_enabled()
    config = load_integration_config()
    if config.listener_name is None:
        pytest.skip("Set MQ_TEST_LISTENER to enable listener integration checks.")
    session = _build_session(config)

    results = session.display_listener(name=config.listener_name)

    assert results
    assert any(_contains_string_value(result, config.listener_name) for result in results)


@pytest.mark.integration
def test_display_topic_returns_object_when_configured() -> None:
    _require_integration_enabled()
    config = load_integration_config()
    if config.topic_name is None:
        pytest.skip("Set MQ_TEST_TOPIC to enable topic integration checks.")
    session = _build_session(config)

    results = session.display_topic(name=config.topic_name)

    assert results
    assert any(_contains_string_value(result, config.topic_name) for result in results)


@pytest.mark.integration
def test_display_sub_returns_object_when_configured() -> None:
    _require_integration_enabled()
    config = load_integration_config()
    if config.subscription_name is None:
        pytest.skip("Set MQ_TEST_SUBSCRIPTION to enable subscription integration checks.")
    session = _build_session(config)

    results = session.display_sub(name=config.subscription_name)

    assert results
    assert any(_contains_string_value(result, config.subscription_name) for result in results)


@pytest.mark.integration
@pytest.mark.parametrize("method_name", OPTIONAL_DISPLAY_METHODS)
def test_display_optional_returns_object_when_configured(method_name: str) -> None:
    _require_integration_enabled()
    config = load_integration_config()
    env_names = _display_env_names(method_name)
    object_name = _get_first_env_value(env_names)
    if object_name is None:
        pytest.skip(f"Set one of {', '.join(env_names)} to enable {method_name} checks.")
    session = _build_session(config)

    method = getattr(session, method_name)
    result = method(name=object_name)

    _assert_display_contains_value(result, object_name, method_name)


@pytest.mark.integration
def test_mutating_commands_execute_when_configured() -> None:
    _require_integration_enabled()
    _require_mutating_enabled()
    config = load_integration_config()
    commands = _load_mutating_commands()
    if not commands:
        pytest.skip(
            f"Set {MUTATING_COMMANDS_ENV} or {MUTATING_COMMANDS_FILE_ENV} to run mutating checks."
        )
    session = _build_session(config)
    for index, command in enumerate(commands):
        _run_mutating_command(session, command, index=index)


def _require_integration_enabled() -> None:
    if getenv(INTEGRATION_ENV_FLAG) != "1":
        pytest.skip(f"Set {INTEGRATION_ENV_FLAG}=1 to enable integration tests.")


def _require_mutating_enabled() -> None:
    if getenv(MUTATING_ENV_FLAG) != "1":
        pytest.skip(f"Set {MUTATING_ENV_FLAG}=1 to enable mutating integration tests.")


def _parse_bool(value: str | None) -> bool:
    if value is None:
        return False
    normalized = value.strip().lower()
    return normalized in {"1", "true", "yes", "on"}


def _build_session(config: IntegrationConfig) -> MQRESTSession:
    return MQRESTSession(
        rest_base_url=config.rest_base_url,
        qmgr_name=config.qmgr_name,
        username=config.admin_user,
        password=config.admin_password,
        verify_tls=config.verify_tls,
        map_attributes=config.map_attributes,
    )


def _contains_string_value(response_object: dict[str, object], expected_value: str) -> bool:
    expected_normalized = expected_value.strip().upper()
    for attribute_value in response_object.values():
        if isinstance(attribute_value, str) and attribute_value.strip().upper() == expected_normalized:
            return True
    return False


def _display_env_names(method_name: str) -> tuple[str, ...]:
    suffix = method_name.removeprefix("display_")
    override = DISPLAY_ENV_OVERRIDES.get(suffix)
    if override:
        return override
    return (f"MQ_TEST_{suffix.upper()}",)


def _get_first_env_value(env_names: tuple[str, ...]) -> str | None:
    for name in env_names:
        value = getenv(name)
        if value:
            return value
    return None


def _assert_display_contains_value(
    result: object,
    expected_value: str,
    method_name: str,
) -> None:
    if isinstance(result, dict):
        assert _contains_string_value(result, expected_value)
        return
    if isinstance(result, list):
        assert result
        assert any(
            isinstance(item, dict) and _contains_string_value(item, expected_value) for item in result
        )
        return
    pytest.fail(f"{method_name} returned unexpected type {type(result)}")


def _load_mutating_commands() -> list[dict[str, object]]:
    raw = _read_mutating_commands_source()
    if raw is None:
        return []
    try:
        payload = json.loads(raw)
    except json.JSONDecodeError as error:
        pytest.fail(f"Invalid JSON for mutating commands: {error}")
    if not isinstance(payload, list):
        pytest.fail("Mutating commands payload must be a JSON list.")

    commands: list[dict[str, object]] = []
    for index, entry in enumerate(payload):
        if not isinstance(entry, dict):
            pytest.fail(f"Mutating command at index {index} must be a JSON object.")
        method = entry.get("method")
        if not isinstance(method, str):
            pytest.fail(f"Mutating command at index {index} missing 'method' string.")
        if method.startswith("display_"):
            pytest.fail(f"Mutating command at index {index} cannot call {method}.")
        commands.append(entry)
    return commands


def _read_mutating_commands_source() -> str | None:
    file_path = getenv(MUTATING_COMMANDS_FILE_ENV)
    if file_path:
        path = Path(file_path)
        if not path.exists():
            pytest.fail(f"Mutating commands file not found: {file_path}")
        return path.read_text(encoding="utf-8")
    return getenv(MUTATING_COMMANDS_ENV)


def _run_mutating_command(
    session: MQRESTSession,
    command: dict[str, object],
    *,
    index: int,
) -> None:
    method_name = command.get("method")
    if not isinstance(method_name, str):
        pytest.fail(f"Mutating command at index {index} missing 'method' string.")
    method = getattr(session, method_name, None)
    if method is None:
        pytest.fail(f"Mutating command at index {index} references unknown method {method_name}.")

    name = command.get("name")
    request_parameters = command.get("request_parameters")
    response_parameters = command.get("response_parameters")

    if request_parameters is not None and not isinstance(request_parameters, dict):
        pytest.fail(f"Mutating command at index {index} has invalid request_parameters.")
    if response_parameters is not None and not isinstance(response_parameters, list):
        pytest.fail(f"Mutating command at index {index} has invalid response_parameters.")

    kwargs: dict[str, object] = {}
    if name is not None:
        kwargs["name"] = name
    if request_parameters is not None:
        kwargs["request_parameters"] = request_parameters
    if response_parameters is not None:
        kwargs["response_parameters"] = response_parameters

    method(**kwargs)
