"""Internal helpers for validating and merging mapping overrides."""

from __future__ import annotations

import copy
import enum
from collections.abc import Mapping
from typing import cast

_VALID_TOP_LEVEL_KEYS = frozenset({"commands", "qualifiers"})

_VALID_QUALIFIER_SUB_KEYS = frozenset(
    {
        "request_key_map",
        "request_value_map",
        "request_key_value_map",
        "response_key_map",
        "response_value_map",
    }
)


class MappingOverrideMode(enum.Enum):
    """Mode for applying mapping overrides.

    Attributes:
        MERGE: Sparse merge — override entries are layered on top of
            the built-in mapping data (default).
        REPLACE: Complete replacement — override data replaces the
            built-in mapping data entirely. A completeness check
            validates that all command and qualifier keys are present.

    """

    MERGE = "merge"
    REPLACE = "replace"


def validate_mapping_overrides(overrides: Mapping[str, object]) -> None:
    """Validate the structure of a mapping overrides dict.

    Raises ``TypeError`` for type violations and ``ValueError`` for
    invalid keys.
    """
    _validate_top_level_keys(overrides)
    _validate_commands_section(overrides.get("commands"))
    _validate_qualifiers_section(overrides.get("qualifiers"))


def _validate_top_level_keys(overrides: Mapping[str, object]) -> None:
    for key in overrides:
        if key not in _VALID_TOP_LEVEL_KEYS:
            msg = f"Invalid top-level key in mapping_overrides: {key!r} (expected subset of {sorted(_VALID_TOP_LEVEL_KEYS)})"
            raise ValueError(msg)


def _validate_commands_section(commands: object) -> None:
    if commands is None:
        return
    if not isinstance(commands, Mapping):
        msg = "mapping_overrides['commands'] must be a Mapping"
        raise TypeError(msg)
    commands_map = cast("Mapping[str, object]", commands)
    for command_key, command_entry in commands_map.items():
        if not isinstance(command_entry, Mapping):
            msg = f"mapping_overrides['commands'][{command_key!r}] must be a Mapping"
            raise TypeError(msg)


def _validate_qualifiers_section(qualifiers: object) -> None:
    if qualifiers is None:
        return
    if not isinstance(qualifiers, Mapping):
        msg = "mapping_overrides['qualifiers'] must be a Mapping"
        raise TypeError(msg)
    qualifiers_map = cast("Mapping[str, object]", qualifiers)
    for qualifier_key, qualifier_entry in qualifiers_map.items():
        if not isinstance(qualifier_entry, Mapping):
            msg = f"mapping_overrides['qualifiers'][{qualifier_key!r}] must be a Mapping"
            raise TypeError(msg)
        _validate_qualifier_entry(qualifier_key, cast("Mapping[str, object]", qualifier_entry))


def _validate_qualifier_entry(qualifier_key: str, entry: Mapping[str, object]) -> None:
    for sub_key in entry:
        if sub_key not in _VALID_QUALIFIER_SUB_KEYS:
            msg = (
                f"Invalid sub-key {sub_key!r} in mapping_overrides['qualifiers'][{qualifier_key!r}] "
                f"(expected subset of {sorted(_VALID_QUALIFIER_SUB_KEYS)})"
            )
            raise ValueError(msg)
        sub_value = entry[sub_key]
        if not isinstance(sub_value, Mapping):
            msg = f"mapping_overrides['qualifiers'][{qualifier_key!r}][{sub_key!r}] must be a Mapping"
            raise TypeError(msg)


def merge_mapping_data(
    base: dict[str, object],
    overrides: Mapping[str, object],
) -> dict[str, object]:
    """Deep-copy *base* and merge *overrides* into it.

    Commands: per-command shallow merge.
    Qualifiers: per-qualifier, per-sub-map key-level merge.
    """
    merged = copy.deepcopy(base)
    _merge_commands(merged, overrides.get("commands"))
    _merge_qualifiers(merged, overrides.get("qualifiers"))
    return merged


def _merge_commands(merged: dict[str, object], override_commands: object) -> None:
    if not isinstance(override_commands, Mapping):
        return
    base_commands_raw = merged.get("commands")
    if not isinstance(base_commands_raw, dict):
        base_commands_raw = {}
        merged["commands"] = base_commands_raw
    base_commands = cast("dict[str, object]", base_commands_raw)
    commands_map = cast("Mapping[str, object]", override_commands)
    for command_key, command_entry in commands_map.items():
        if not isinstance(command_entry, Mapping):
            continue
        existing = base_commands.get(command_key)
        if isinstance(existing, dict):
            cast("dict[str, object]", existing).update(
                cast("Mapping[str, object]", command_entry),
            )
        else:
            base_commands[command_key] = dict(command_entry)


def _merge_qualifiers(merged: dict[str, object], override_qualifiers: object) -> None:
    if not isinstance(override_qualifiers, Mapping):
        return
    base_qualifiers_raw = merged.get("qualifiers")
    if not isinstance(base_qualifiers_raw, dict):
        base_qualifiers_raw = {}
        merged["qualifiers"] = base_qualifiers_raw
    base_qualifiers = cast("dict[str, object]", base_qualifiers_raw)
    qualifiers_map = cast("Mapping[str, object]", override_qualifiers)
    for qualifier_key, qualifier_entry in qualifiers_map.items():
        if not isinstance(qualifier_entry, Mapping):
            continue
        _merge_single_qualifier(
            base_qualifiers,
            qualifier_key,
            cast("Mapping[str, object]", qualifier_entry),
        )


def _merge_single_qualifier(
    base_qualifiers: dict[str, object],
    qualifier_key: str,
    qualifier_entry: Mapping[str, object],
) -> None:
    existing_raw = base_qualifiers.get(qualifier_key)
    if not isinstance(existing_raw, dict):
        base_qualifiers[qualifier_key] = dict(qualifier_entry)
        return
    existing_qualifier = cast("dict[str, object]", existing_raw)
    for sub_key, sub_value in qualifier_entry.items():
        if isinstance(sub_value, Mapping):
            existing_sub = existing_qualifier.get(sub_key)
            if isinstance(existing_sub, dict):
                cast("dict[str, object]", existing_sub).update(
                    cast("Mapping[str, object]", sub_value),
                )
            else:
                existing_qualifier[sub_key] = dict(sub_value)


def validate_mapping_overrides_complete(
    base: Mapping[str, object],
    overrides: Mapping[str, object],
) -> None:
    """Validate that *overrides* covers all command and qualifier keys in *base*.

    Raises ``ValueError`` listing every missing entry when the override
    data is incomplete.
    """
    missing_parts: list[str] = []

    base_commands = base.get("commands")
    override_commands = overrides.get("commands")
    if isinstance(base_commands, Mapping):
        base_commands_map = cast("Mapping[str, object]", base_commands)
        override_commands_map = (
            cast("Mapping[str, object]", override_commands) if isinstance(override_commands, Mapping) else {}
        )
        missing_commands = sorted(set(base_commands_map.keys()) - set(override_commands_map.keys()))
        missing_parts.extend(f"commands: {key}" for key in missing_commands)

    base_qualifiers = base.get("qualifiers")
    override_qualifiers = overrides.get("qualifiers")
    if isinstance(base_qualifiers, Mapping):
        base_qualifiers_map = cast("Mapping[str, object]", base_qualifiers)
        override_qualifiers_map = (
            cast("Mapping[str, object]", override_qualifiers) if isinstance(override_qualifiers, Mapping) else {}
        )
        missing_qualifiers = sorted(set(base_qualifiers_map.keys()) - set(override_qualifiers_map.keys()))
        missing_parts.extend(f"qualifiers: {key}" for key in missing_qualifiers)

    if missing_parts:
        detail = "\n".join(f"  {entry}" for entry in missing_parts)
        msg = f"mapping_overrides is incomplete for REPLACE mode. Missing entries:\n{detail}"
        raise ValueError(msg)


def replace_mapping_data(overrides: Mapping[str, object]) -> dict[str, object]:
    """Return a deep copy of *overrides* as the complete mapping data."""
    return copy.deepcopy(dict(overrides))
