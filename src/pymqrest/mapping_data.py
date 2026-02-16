"""Mapping data loaded from the bundled mapping-data.json resource."""

from __future__ import annotations

import json
from pathlib import Path

_JSON_PATH = Path(__file__).parent / "mapping-data.json"

MAPPING_DATA: dict[str, object] = json.loads(_JSON_PATH.read_text(encoding="utf-8"))
