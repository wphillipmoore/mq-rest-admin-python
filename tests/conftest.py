"""Pytest configuration for pymqrest tests."""

from __future__ import annotations

import sys
from os import getenv
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = PROJECT_ROOT / "src"
SCRIPTS_ROOT = PROJECT_ROOT / "scripts"
INTEGRATION_ENV_VAR = "PYMQREST_RUN_INTEGRATION"

if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
if str(SCRIPTS_ROOT) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_ROOT))


def _integration_enabled() -> bool:
    env_value = getenv(INTEGRATION_ENV_VAR, "").strip().lower()
    return env_value in {"1", "true", "yes"}


def pytest_configure(config: pytest.Config) -> None:
    config.addinivalue_line(
        "markers",
        "integration: integration tests (require PYMQREST_RUN_INTEGRATION=1)",
    )


def pytest_collection_modifyitems(
    config: pytest.Config,
    items: list[pytest.Item],
) -> None:
    _ = config
    if _integration_enabled():
        return
    skip_marker = pytest.mark.skip(
        reason=f"Set {INTEGRATION_ENV_VAR}=1 to run integration tests.",
    )
    for test_item in items:
        if test_item.get_closest_marker("integration") is not None:
            test_item.add_marker(skip_marker)
