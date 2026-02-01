"""Integration test scaffolding for MQ REST validation."""

from __future__ import annotations

from dataclasses import dataclass
from os import getenv

import pytest

from pymqrest.session import MQRESTSession

INTEGRATION_ENV_FLAG = "PYMQREST_RUN_INTEGRATION"


@dataclass(frozen=True)
class IntegrationConfig:
    rest_base_url: str
    admin_user: str
    admin_password: str
    qmgr_name: str
    verify_tls: bool
    queue_name: str
    channel_name: str
    authinfo_name: str | None
    comminfo_name: str | None
    listener_name: str | None
    namelist_name: str | None
    policy_name: str | None
    process_name: str | None
    service_name: str | None
    stgclass_name: str | None
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
        authinfo_name=getenv("MQ_TEST_AUTHINFO"),
        comminfo_name=getenv("MQ_TEST_COMMINFO"),
        listener_name=getenv("MQ_TEST_LISTENER"),
        namelist_name=getenv("MQ_TEST_NAMELIST"),
        policy_name=getenv("MQ_TEST_POLICY"),
        process_name=getenv("MQ_TEST_PROCESS"),
        service_name=getenv("MQ_TEST_SERVICE"),
        stgclass_name=getenv("MQ_TEST_STGCLASS"),
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
def test_display_authinfo_returns_object_when_configured() -> None:
    _require_integration_enabled()
    config = load_integration_config()
    if config.authinfo_name is None:
        pytest.skip("Set MQ_TEST_AUTHINFO to enable authinfo integration checks.")
    session = _build_session(config)

    results = session.display_authinfo(name=config.authinfo_name)

    assert results
    assert any(_contains_string_value(result, config.authinfo_name) for result in results)


@pytest.mark.integration
def test_display_comminfo_returns_object_when_configured() -> None:
    _require_integration_enabled()
    config = load_integration_config()
    if config.comminfo_name is None:
        pytest.skip("Set MQ_TEST_COMMINFO to enable comminfo integration checks.")
    session = _build_session(config)

    results = session.display_comminfo(name=config.comminfo_name)

    assert results
    assert any(_contains_string_value(result, config.comminfo_name) for result in results)


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
def test_display_namelist_returns_object_when_configured() -> None:
    _require_integration_enabled()
    config = load_integration_config()
    if config.namelist_name is None:
        pytest.skip("Set MQ_TEST_NAMELIST to enable namelist integration checks.")
    session = _build_session(config)

    results = session.display_namelist(name=config.namelist_name)

    assert results
    assert any(_contains_string_value(result, config.namelist_name) for result in results)


@pytest.mark.integration
def test_display_policy_returns_object_when_configured() -> None:
    _require_integration_enabled()
    config = load_integration_config()
    if config.policy_name is None:
        pytest.skip("Set MQ_TEST_POLICY to enable policy integration checks.")
    session = _build_session(config)

    results = session.display_policy(name=config.policy_name)

    assert results
    assert any(_contains_string_value(result, config.policy_name) for result in results)


@pytest.mark.integration
def test_display_process_returns_object_when_configured() -> None:
    _require_integration_enabled()
    config = load_integration_config()
    if config.process_name is None:
        pytest.skip("Set MQ_TEST_PROCESS to enable process integration checks.")
    session = _build_session(config)

    results = session.display_process(name=config.process_name)

    assert results
    assert any(_contains_string_value(result, config.process_name) for result in results)


@pytest.mark.integration
def test_display_service_returns_object_when_configured() -> None:
    _require_integration_enabled()
    config = load_integration_config()
    if config.service_name is None:
        pytest.skip("Set MQ_TEST_SERVICE to enable service integration checks.")
    session = _build_session(config)

    results = session.display_service(name=config.service_name)

    assert results
    assert any(_contains_string_value(result, config.service_name) for result in results)


@pytest.mark.integration
def test_display_stgclass_returns_object_when_configured() -> None:
    _require_integration_enabled()
    config = load_integration_config()
    if config.stgclass_name is None:
        pytest.skip("Set MQ_TEST_STGCLASS to enable stgclass integration checks.")
    session = _build_session(config)

    results = session.display_stgclass(name=config.stgclass_name)

    assert results
    assert any(_contains_string_value(result, config.stgclass_name) for result in results)


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


def _require_integration_enabled() -> None:
    if getenv(INTEGRATION_ENV_FLAG) != "1":
        pytest.skip(f"Set {INTEGRATION_ENV_FLAG}=1 to enable integration tests.")


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
