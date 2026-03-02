"""Tests for the internal mapping merge module."""

from __future__ import annotations

import pytest

from pymqrest._mapping_merge import (
    MappingOverrideMode,
    merge_mapping_data,
    replace_mapping_data,
    validate_mapping_overrides,
    validate_mapping_overrides_complete,
)

# -- validate_mapping_overrides --


def test_validate_accepts_empty_overrides() -> None:
    validate_mapping_overrides({})


def test_validate_accepts_minimal_overrides() -> None:
    validate_mapping_overrides({"commands": {}, "qualifiers": {}})


def test_validate_rejects_invalid_top_level_key() -> None:
    with pytest.raises(ValueError, match="Invalid top-level key"):
        validate_mapping_overrides({"bogus": {}})


def test_validate_rejects_non_mapping_commands() -> None:
    with pytest.raises(TypeError, match=r"commands.*must be a Mapping"):
        validate_mapping_overrides({"commands": "bad"})


def test_validate_rejects_non_mapping_command_entry() -> None:
    with pytest.raises(TypeError, match=r"commands.*must be a Mapping"):
        validate_mapping_overrides({"commands": {"DISPLAY QUEUE": "bad"}})


def test_validate_rejects_non_mapping_qualifiers() -> None:
    with pytest.raises(TypeError, match=r"qualifiers.*must be a Mapping"):
        validate_mapping_overrides({"qualifiers": "bad"})


def test_validate_rejects_non_mapping_qualifier_entry() -> None:
    with pytest.raises(TypeError, match=r"qualifiers.*must be a Mapping"):
        validate_mapping_overrides({"qualifiers": {"queue": "bad"}})


def test_validate_rejects_unknown_qualifier_sub_key() -> None:
    with pytest.raises(ValueError, match="Invalid sub-key"):
        validate_mapping_overrides({"qualifiers": {"queue": {"bogus_map": {}}}})


def test_validate_rejects_non_mapping_sub_value() -> None:
    with pytest.raises(TypeError, match="must be a Mapping"):
        validate_mapping_overrides({"qualifiers": {"queue": {"request_key_map": "bad"}}})


def test_validate_accepts_commands_with_valid_entries() -> None:
    validate_mapping_overrides(
        {
            "commands": {"DISPLAY QUEUE": {"qualifier": "queue"}},
        }
    )


def test_validate_accepts_all_valid_sub_keys() -> None:
    validate_mapping_overrides(
        {
            "qualifiers": {
                "queue": {
                    "request_key_map": {},
                    "request_value_map": {},
                    "request_key_value_map": {},
                    "response_key_map": {},
                    "response_value_map": {},
                },
            },
        }
    )


# -- merge_mapping_data --


def test_merge_returns_deep_copy() -> None:
    base: dict[str, object] = {
        "commands": {"DISPLAY QUEUE": {"qualifier": "queue"}},
        "qualifiers": {"queue": {"request_key_map": {"foo": "FOO"}}},
    }
    merged = merge_mapping_data(base, {})

    assert merged == base
    assert merged is not base
    assert merged["commands"] is not base["commands"]


def test_merge_does_not_mutate_base() -> None:
    base: dict[str, object] = {
        "commands": {"DISPLAY QUEUE": {"qualifier": "queue"}},
        "qualifiers": {"queue": {"request_key_map": {"foo": "FOO"}}},
    }
    original_commands = dict(base["commands"])  # type: ignore[arg-type]

    merge_mapping_data(base, {"commands": {"DISPLAY QUEUE": {"description": "override"}}})

    assert base["commands"] == original_commands


def test_merge_commands_shallow_merge() -> None:
    base: dict[str, object] = {
        "commands": {"DISPLAY QUEUE": {"qualifier": "queue", "description": "original"}},
    }
    overrides = {"commands": {"DISPLAY QUEUE": {"description": "override"}}}

    merged = merge_mapping_data(base, overrides)

    command = merged["commands"]["DISPLAY QUEUE"]  # type: ignore[index]
    assert command["qualifier"] == "queue"
    assert command["description"] == "override"


def test_merge_commands_adds_new_command() -> None:
    base: dict[str, object] = {"commands": {"DISPLAY QUEUE": {"qualifier": "queue"}}}
    overrides = {"commands": {"CUSTOM CMD": {"qualifier": "custom"}}}

    merged = merge_mapping_data(base, overrides)

    assert "CUSTOM CMD" in merged["commands"]  # type: ignore[operator]
    assert "DISPLAY QUEUE" in merged["commands"]  # type: ignore[operator]


def test_merge_qualifiers_key_level_merge() -> None:
    base: dict[str, object] = {
        "qualifiers": {
            "queue": {
                "request_key_map": {"foo": "FOO", "bar": "BAR"},
                "response_key_map": {"BSIZ": "buffer_size"},
            },
        },
    }
    overrides = {
        "qualifiers": {
            "queue": {
                "request_key_map": {"foo": "OVERRIDDEN_FOO"},
                "response_key_map": {"NEWATTR": "new_attribute"},
            },
        },
    }

    merged = merge_mapping_data(base, overrides)

    qualifier = merged["qualifiers"]["queue"]  # type: ignore[index]
    assert qualifier["request_key_map"]["foo"] == "OVERRIDDEN_FOO"
    assert qualifier["request_key_map"]["bar"] == "BAR"
    assert qualifier["response_key_map"]["BSIZ"] == "buffer_size"
    assert qualifier["response_key_map"]["NEWATTR"] == "new_attribute"


def test_merge_adds_new_qualifier() -> None:
    base: dict[str, object] = {"qualifiers": {"queue": {"request_key_map": {"a": "A"}}}}
    overrides = {"qualifiers": {"custom": {"request_key_map": {"x": "X"}}}}

    merged = merge_mapping_data(base, overrides)

    assert "custom" in merged["qualifiers"]  # type: ignore[operator]
    assert merged["qualifiers"]["custom"]["request_key_map"]["x"] == "X"  # type: ignore[index]
    assert "queue" in merged["qualifiers"]  # type: ignore[operator]


def test_merge_handles_missing_base_commands() -> None:
    base: dict[str, object] = {"qualifiers": {}}
    overrides = {"commands": {"NEW CMD": {"qualifier": "new"}}}

    merged = merge_mapping_data(base, overrides)

    assert merged["commands"]["NEW CMD"]["qualifier"] == "new"  # type: ignore[index]


def test_merge_handles_missing_base_qualifiers() -> None:
    base: dict[str, object] = {"commands": {}}
    overrides = {"qualifiers": {"new": {"request_key_map": {"a": "A"}}}}

    merged = merge_mapping_data(base, overrides)

    assert merged["qualifiers"]["new"]["request_key_map"]["a"] == "A"  # type: ignore[index]


def test_merge_skips_non_mapping_qualifier_entry() -> None:
    base: dict[str, object] = {"qualifiers": {"queue": {"request_key_map": {"a": "A"}}}}
    overrides: dict[str, object] = {"qualifiers": {"queue": "not_a_mapping"}}

    merged = merge_mapping_data(base, overrides)

    assert merged["qualifiers"]["queue"]["request_key_map"]["a"] == "A"  # type: ignore[index]


def test_merge_skips_non_mapping_sub_value() -> None:
    base: dict[str, object] = {"qualifiers": {"queue": {"request_key_map": {"a": "A"}}}}
    overrides: dict[str, object] = {"qualifiers": {"queue": {"request_key_map": "not_a_mapping"}}}

    merged = merge_mapping_data(base, overrides)

    assert merged["qualifiers"]["queue"]["request_key_map"]["a"] == "A"  # type: ignore[index]


def test_merge_skips_non_mapping_command_entry() -> None:
    base: dict[str, object] = {"commands": {"DISPLAY QUEUE": {"qualifier": "queue"}}}
    overrides: dict[str, object] = {"commands": {"DISPLAY QUEUE": "not_a_mapping"}}

    merged = merge_mapping_data(base, overrides)

    assert merged["commands"]["DISPLAY QUEUE"]["qualifier"] == "queue"  # type: ignore[index]


def test_merge_adds_new_sub_map_to_existing_qualifier() -> None:
    base: dict[str, object] = {"qualifiers": {"queue": {"request_key_map": {"a": "A"}}}}
    overrides = {"qualifiers": {"queue": {"response_key_map": {"B": "b_mapped"}}}}

    merged = merge_mapping_data(base, overrides)

    qualifier = merged["qualifiers"]["queue"]  # type: ignore[index]
    assert qualifier["request_key_map"]["a"] == "A"
    assert qualifier["response_key_map"]["B"] == "b_mapped"


# -- MappingOverrideMode --


def test_mapping_override_mode_values() -> None:
    assert MappingOverrideMode.MERGE.value == "merge"
    assert MappingOverrideMode.REPLACE.value == "replace"


# -- validate_mapping_overrides_complete --


def test_validate_complete_accepts_matching_keys() -> None:
    base: dict[str, object] = {
        "commands": {"DISPLAY QUEUE": {"qualifier": "queue"}},
        "qualifiers": {"queue": {"request_key_map": {"a": "A"}}},
    }
    overrides: dict[str, object] = {
        "commands": {"DISPLAY QUEUE": {"qualifier": "queue"}},
        "qualifiers": {"queue": {"request_key_map": {"x": "X"}}},
    }

    validate_mapping_overrides_complete(base, overrides)


def test_validate_complete_rejects_missing_commands() -> None:
    base: dict[str, object] = {
        "commands": {"DISPLAY QUEUE": {}, "ALTER QUEUE": {}},
        "qualifiers": {"queue": {}},
    }
    overrides: dict[str, object] = {
        "commands": {"DISPLAY QUEUE": {}},
        "qualifiers": {"queue": {}},
    }

    with pytest.raises(ValueError, match="ALTER QUEUE"):
        validate_mapping_overrides_complete(base, overrides)


def test_validate_complete_rejects_missing_qualifiers() -> None:
    base: dict[str, object] = {
        "commands": {"DISPLAY QUEUE": {}},
        "qualifiers": {"queue": {}, "channel": {}},
    }
    overrides: dict[str, object] = {
        "commands": {"DISPLAY QUEUE": {}},
        "qualifiers": {"queue": {}},
    }

    with pytest.raises(ValueError, match="channel"):
        validate_mapping_overrides_complete(base, overrides)


def test_validate_complete_rejects_missing_both() -> None:
    base: dict[str, object] = {
        "commands": {"DISPLAY QUEUE": {}, "ALTER QUEUE": {}},
        "qualifiers": {"queue": {}, "channel": {}},
    }
    overrides: dict[str, object] = {
        "commands": {"DISPLAY QUEUE": {}},
        "qualifiers": {"queue": {}},
    }

    with pytest.raises(ValueError, match="incomplete for REPLACE") as error_info:
        validate_mapping_overrides_complete(base, overrides)

    message = str(error_info.value)
    assert "ALTER QUEUE" in message
    assert "channel" in message


def test_validate_complete_accepts_extra_keys() -> None:
    base: dict[str, object] = {
        "commands": {"DISPLAY QUEUE": {}},
        "qualifiers": {"queue": {}},
    }
    overrides: dict[str, object] = {
        "commands": {"DISPLAY QUEUE": {}, "CUSTOM CMD": {}},
        "qualifiers": {"queue": {}, "custom": {}},
    }

    validate_mapping_overrides_complete(base, overrides)


def test_validate_complete_skips_missing_base_commands() -> None:
    base: dict[str, object] = {"qualifiers": {"queue": {}}}
    overrides: dict[str, object] = {"qualifiers": {"queue": {}}}

    validate_mapping_overrides_complete(base, overrides)


def test_validate_complete_skips_missing_base_qualifiers() -> None:
    base: dict[str, object] = {"commands": {"DISPLAY QUEUE": {}}}
    overrides: dict[str, object] = {"commands": {"DISPLAY QUEUE": {}}}

    validate_mapping_overrides_complete(base, overrides)


def test_validate_complete_handles_missing_commands_section() -> None:
    base: dict[str, object] = {
        "commands": {"DISPLAY QUEUE": {}},
        "qualifiers": {"queue": {}},
    }
    overrides: dict[str, object] = {
        "qualifiers": {"queue": {}},
    }

    with pytest.raises(ValueError, match="DISPLAY QUEUE"):
        validate_mapping_overrides_complete(base, overrides)


def test_validate_complete_handles_missing_qualifiers_section() -> None:
    base: dict[str, object] = {
        "commands": {"DISPLAY QUEUE": {}},
        "qualifiers": {"queue": {}},
    }
    overrides: dict[str, object] = {
        "commands": {"DISPLAY QUEUE": {}},
    }

    with pytest.raises(ValueError, match="queue"):
        validate_mapping_overrides_complete(base, overrides)


# -- replace_mapping_data --


def test_replace_returns_deep_copy() -> None:
    overrides: dict[str, object] = {
        "commands": {"DISPLAY QUEUE": {"qualifier": "queue"}},
        "qualifiers": {"queue": {"request_key_map": {"a": "A"}}},
    }

    result = replace_mapping_data(overrides)

    assert result == overrides
    assert result is not overrides
    assert result["commands"] is not overrides["commands"]


def test_replace_contains_only_override_data() -> None:
    overrides: dict[str, object] = {
        "commands": {"CUSTOM CMD": {"qualifier": "custom"}},
        "qualifiers": {"custom": {"request_key_map": {"x": "X"}}},
    }

    result = replace_mapping_data(overrides)

    assert set(result["commands"]) == {"CUSTOM CMD"}  # type: ignore[arg-type]
    assert set(result["qualifiers"]) == {"custom"}  # type: ignore[arg-type]
