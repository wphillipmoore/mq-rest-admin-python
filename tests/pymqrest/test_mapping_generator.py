"""Tests for the mapping data generator helpers."""

from __future__ import annotations

import pytest

from scripts.generate_mapping_data import (
    MappingGenerationError,
    merge_mapping_overrides,
    normalize_mapping_data,
)


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

    assert qualifier_data["request_key_map"] == {"current_q_depth": "CURDEPTH"}
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
