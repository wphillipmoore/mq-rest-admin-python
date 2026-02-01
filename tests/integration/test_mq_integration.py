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
def test_display_queue_returns_object() -> None:
    _require_integration_enabled()
    config = load_integration_config()
    session = _build_session(config)

    results = session.display_queue(name=config.queue_name)

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
