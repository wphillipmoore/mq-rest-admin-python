"""Integration test scaffolding for MQ REST validation."""

from __future__ import annotations

from dataclasses import dataclass
from os import getenv

import pytest


@dataclass(frozen=True)
class IntegrationConfig:
    rest_base_url: str
    admin_user: str
    admin_password: str


def load_integration_config() -> IntegrationConfig:
    return IntegrationConfig(
        rest_base_url=getenv("MQ_REST_BASE_URL", "https://localhost:9443/ibmmq/rest/v2"),
        admin_user=getenv("MQ_ADMIN_USER", "mqadmin"),
        admin_password=getenv("MQ_ADMIN_PASSWORD", "mqadmin"),
    )


@pytest.mark.integration
def test_integration_placeholder() -> None:
    pytest.skip(
        "Integration test framework is ready; implement tests once the API is built."
    )


@pytest.mark.integration
def test_integration_config_defaults() -> None:
    config = load_integration_config()
    assert config.rest_base_url.startswith("https://")
    assert config.admin_user
    assert config.admin_password
