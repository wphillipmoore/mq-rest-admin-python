from __future__ import annotations

from unittest.mock import MagicMock

import pytest


@pytest.fixture
def mock_session() -> MagicMock:
    session = MagicMock()
    session.qmgr_name = "QM1"
    return session
