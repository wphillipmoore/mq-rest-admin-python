"""Tests for the mapping data generator helpers."""

from __future__ import annotations

from pathlib import Path

import pytest
from scripts.generate_mapping_data import (
    MappingGenerationError,
    merge_mapping_overrides,
    normalize_mapping_data,
)


def _parse_attribute_map(path: Path) -> tuple[str | None, list[dict[str, str]]]:
    qualifier: str | None = None
    entries: list[dict[str, str]] = []
    current: dict[str, str] | None = None

    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if stripped.startswith("qualifier:"):
            qualifier = stripped.split(":", 1)[1].strip().strip('"')
            continue
        if stripped.startswith("- mqsc:"):
            if current:
                entries.append(current)
            mqsc = stripped.split(":", 1)[1].strip().strip('"')
            current = {"mqsc": mqsc}
            continue
        if current is None:
            continue
        if stripped.startswith("snake:"):
            current["snake"] = stripped.split(":", 1)[1].strip().strip('"')
            continue

    if current:
        entries.append(current)

    return qualifier, entries


def test_normalize_mapping_inverts_key_and_value_maps() -> None:
    mapping_source = {
        "version": 1,
        "commands": {
            "DISPLAY QUEUE": {"qualifier": "queue", "status": "provisional"}
        },
        "qualifiers": {
            "queue": {
                "response_key_map": {
                    "CURDEPTH": "current_q_depth",
                    "DEFPSIST": "def_persistence",
                },
                "response_value_map": {
                    "DEFPSIST": {
                        "DEF": "def",
                    }
                },
            }
        },
    }

    normalized = normalize_mapping_data(mapping_source)
    qualifier_data = normalized["qualifiers"]["queue"]

    assert qualifier_data["request_key_map"] == {
        "current_q_depth": "CURDEPTH",
        "def_persistence": "DEFPSIST",
    }
    assert qualifier_data["request_value_map"] == {"def_persistence": {"def": "DEF"}}


def test_merge_mapping_overrides_removes_entries() -> None:
    base_data = {
        "version": 1,
        "commands": {
            "DISPLAY QUEUE": {"qualifier": "queue", "status": "provisional"}
        },
        "qualifiers": {
            "queue": {
                "response_key_map": {
                    "CURDEPTH": "current_q_depth",
                    "DEFPSIST": "def_persistence",
                }
            }
        },
    }
    override_data = {
        "qualifiers": {
            "queue": {
                "response_key_map": {
                    "DEFPSIST": None
                }
            }
        }
    }

    merged = merge_mapping_overrides(base_data, override_data)
    response_map = merged["qualifiers"]["queue"]["response_key_map"]

    assert response_map == {"CURDEPTH": "current_q_depth"}


def test_normalize_mapping_rejects_inconsistent_maps() -> None:
    mapping_source = {
        "version": 1,
        "commands": {
            "DISPLAY QUEUE": {"qualifier": "queue", "status": "provisional"}
        },
        "qualifiers": {
            "queue": {
                "response_key_map": {
                    "CURDEPTH": "current_q_depth",
                },
                "request_key_map": {
                    "current_q_depth": "CURDEPTH",
                    "extra": "EXTRA",
                },
            }
        },
    }

    with pytest.raises(MappingGenerationError):
        normalize_mapping_data(mapping_source)


def test_attribute_maps_have_unique_snake_per_qualifier() -> None:
    attr_dir = Path(__file__).resolve().parents[2] / "docs" / "extraction" / "mqsc-pcf-attribute-map"
    duplicates: list[str] = []

    for path in sorted(attr_dir.glob("*.yaml")):
        qualifier, entries = _parse_attribute_map(path)
        if not qualifier:
            continue
        by_snake: dict[str, list[str]] = {}
        for entry in entries:
            snake = entry.get("snake")
            if not snake:
                continue
            by_snake.setdefault(snake, []).append(entry["mqsc"])
        for snake, mqsc_tokens in sorted(by_snake.items()):
            if len(mqsc_tokens) > 1:
                dup = ", ".join(sorted(set(mqsc_tokens)))
                duplicates.append(f"{qualifier}:{snake}:{dup}")

    assert not duplicates, "Duplicate MQSC->snake mappings found:\\n" + "\\n".join(duplicates)
