"""Generate precompiled mapping data from curated inputs."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from pprint import pformat
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from collections.abc import Mapping


class MappingGenerationError(ValueError):
    pass


def load_mapping_source(source_path: Path) -> dict[str, Any]:
    if not source_path.exists():
        raise MappingGenerationError(f"Mapping source not found: {source_path}")
    if source_path.suffix.lower() in {".json"}:
        return _load_json(source_path)
    if source_path.suffix.lower() in {".yaml", ".yml"}:
        return _load_yaml(source_path)
    raise MappingGenerationError(
        f"Unsupported mapping source format: {source_path.suffix}"
    )


def load_mapping_overrides(overrides_path: Path | None) -> dict[str, Any]:
    if overrides_path is None:
        return {}
    if not overrides_path.exists():
        raise MappingGenerationError(f"Mapping overrides not found: {overrides_path}")
    if overrides_path.suffix.lower() in {".json"}:
        return _load_json(overrides_path)
    if overrides_path.suffix.lower() in {".yaml", ".yml"}:
        return _load_yaml(overrides_path)
    raise MappingGenerationError(
        f"Unsupported mapping overrides format: {overrides_path.suffix}"
    )


def _load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        payload = json.load(handle)
    if not isinstance(payload, dict):
        raise MappingGenerationError(f"Expected JSON object at {path}")
    return payload


def _load_yaml(path: Path) -> dict[str, Any]:
    try:
        import yaml  # type: ignore
    except ImportError as error:
        raise MappingGenerationError(
            "PyYAML is required to read YAML mapping sources. "
            "Install PyYAML or provide JSON input."
        ) from error
    with path.open("r", encoding="utf-8") as handle:
        payload = yaml.safe_load(handle)
    if not isinstance(payload, dict):
        raise MappingGenerationError(f"Expected YAML mapping object at {path}")
    return payload


def merge_mapping_overrides(
    base_data: dict[str, Any],
    override_data: dict[str, Any],
) -> dict[str, Any]:
    if not override_data:
        return base_data
    return _deep_merge(base_data, override_data)


def _deep_merge(base_data: dict[str, Any], override_data: dict[str, Any]) -> dict[str, Any]:
    merged_data: dict[str, Any] = {}
    for key, value in base_data.items():
        merged_data[key] = value
    for key, override_value in override_data.items():
        if override_value is None:
            merged_data.pop(key, None)
            continue
        base_value = merged_data.get(key)
        if isinstance(base_value, dict) and isinstance(override_value, dict):
            merged_data[key] = _deep_merge(base_value, override_value)
            continue
        merged_data[key] = override_value
    return merged_data


def normalize_mapping_data(mapping_data: dict[str, Any]) -> dict[str, Any]:
    normalized_data = dict(mapping_data)
    qualifiers = normalized_data.get("qualifiers")
    if not isinstance(qualifiers, dict):
        raise MappingGenerationError("Mapping data missing qualifiers")
    normalized_qualifiers: dict[str, Any] = {}
    for qualifier_name, qualifier_data in qualifiers.items():
        if not isinstance(qualifier_data, dict):
            raise MappingGenerationError(
                f"Qualifier data must be a dict: {qualifier_name}"
            )
        normalized_qualifiers[qualifier_name] = _normalize_qualifier(
            qualifier_name, qualifier_data
        )
    normalized_data["qualifiers"] = normalized_qualifiers
    _validate_commands(normalized_data)
    return normalized_data


def _normalize_qualifier(
    qualifier_name: str,
    qualifier_data: dict[str, Any],
) -> dict[str, Any]:
    normalized_data = dict(qualifier_data)
    response_key_map = qualifier_data.get("response_key_map")
    request_key_map = qualifier_data.get("request_key_map")
    normalized_data["response_key_map"], normalized_data["request_key_map"] = (
        _normalize_key_maps(
            qualifier_name=qualifier_name,
            response_key_map=response_key_map,
            request_key_map=request_key_map,
        )
    )

    response_value_map = qualifier_data.get("response_value_map")
    request_value_map = qualifier_data.get("request_value_map")
    normalized_data["response_value_map"], normalized_data["request_value_map"] = (
        _normalize_value_maps(
            qualifier_name=qualifier_name,
            response_value_map=response_value_map,
            request_value_map=request_value_map,
            response_key_map=normalized_data["response_key_map"],
            request_key_map=normalized_data["request_key_map"],
        )
    )
    return normalized_data


def _normalize_key_maps(
    *,
    qualifier_name: str,
    response_key_map: Any,
    request_key_map: Any,
) -> tuple[dict[str, str], dict[str, str]]:
    response_map = _as_str_map(response_key_map, "response_key_map", qualifier_name)
    request_map = _as_str_map(request_key_map, "request_key_map", qualifier_name)

    if response_map and request_map:
        inverted_response = _invert_map(response_map, "response_key_map", qualifier_name)
        if inverted_response != request_map:
            raise MappingGenerationError(
                f"Key map mismatch for qualifier {qualifier_name}"
            )
        return response_map, request_map
    if response_map:
        return response_map, _invert_map(response_map, "response_key_map", qualifier_name)
    if request_map:
        inverted_request = _invert_map(request_map, "request_key_map", qualifier_name)
        return inverted_request, request_map
    return {}, {}


def _normalize_value_maps(
    *,
    qualifier_name: str,
    response_value_map: Any,
    request_value_map: Any,
    response_key_map: Mapping[str, str],
    request_key_map: Mapping[str, str],
) -> tuple[dict[str, dict[str, str]], dict[str, dict[str, str]]]:
    response_map = _as_nested_str_map(
        response_value_map, "response_value_map", qualifier_name
    )
    request_map = _as_nested_str_map(
        request_value_map, "request_value_map", qualifier_name
    )

    if response_map and request_map:
        inverted_response = _invert_response_value_map(
            response_map,
            response_key_map=response_key_map,
            map_name="response_value_map",
            qualifier_name=qualifier_name,
        )
        if inverted_response != request_map:
            raise MappingGenerationError(
                f"Value map mismatch for qualifier {qualifier_name}"
            )
        return response_map, request_map
    if response_map:
        return response_map, _invert_response_value_map(
            response_map,
            response_key_map=response_key_map,
            map_name="response_value_map",
            qualifier_name=qualifier_name,
        )
    if request_map:
        inverted_request = _invert_request_value_map(
            request_map,
            request_key_map=request_key_map,
            map_name="request_value_map",
            qualifier_name=qualifier_name,
        )
        return inverted_request, request_map
    return {}, {}


def _as_str_map(value: Any, map_name: str, qualifier_name: str) -> dict[str, str]:
    if value is None:
        return {}
    if not isinstance(value, dict):
        raise MappingGenerationError(
            f"{map_name} must be a dict for qualifier {qualifier_name}"
        )
    string_map: dict[str, str] = {}
    for key, mapped_value in value.items():
        if not isinstance(key, str) or not isinstance(mapped_value, str):
            raise MappingGenerationError(
                f"{map_name} entries must be strings for qualifier {qualifier_name}"
            )
        string_map[key] = mapped_value
    _ensure_unique_values(string_map, map_name, qualifier_name)
    return string_map


def _as_nested_str_map(
    value: Any, map_name: str, qualifier_name: str
) -> dict[str, dict[str, str]]:
    if value is None:
        return {}
    if not isinstance(value, dict):
        raise MappingGenerationError(
            f"{map_name} must be a dict for qualifier {qualifier_name}"
        )
    nested_map: dict[str, dict[str, str]] = {}
    for attribute_name, attribute_map in value.items():
        if not isinstance(attribute_name, str) or not isinstance(attribute_map, dict):
            raise MappingGenerationError(
                f"{map_name} entries must be dicts for qualifier {qualifier_name}"
            )
        nested_map[attribute_name] = _as_str_map(
            attribute_map, map_name, qualifier_name
        )
    return nested_map


def _invert_map(
    map_data: Mapping[str, str],
    map_name: str,
    qualifier_name: str,
) -> dict[str, str]:
    inverted_map: dict[str, str] = {}
    for key, mapped_value in map_data.items():
        if mapped_value in inverted_map:
            raise MappingGenerationError(
                f"{map_name} values must be unique for qualifier {qualifier_name}"
            )
        inverted_map[mapped_value] = key
    return inverted_map


def _invert_response_value_map(
    map_data: Mapping[str, Mapping[str, str]],
    *,
    response_key_map: Mapping[str, str],
    map_name: str,
    qualifier_name: str,
) -> dict[str, dict[str, str]]:
    inverted_map: dict[str, dict[str, str]] = {}
    for attribute_name, attribute_map in map_data.items():
        mapped_attribute_name = response_key_map.get(attribute_name)
        if mapped_attribute_name is None:
            raise MappingGenerationError(
                f"{map_name} references unknown attribute {attribute_name} in {qualifier_name}"
            )
        inverted_map[mapped_attribute_name] = _invert_map(
            attribute_map, map_name, qualifier_name
        )
    return inverted_map


def _invert_request_value_map(
    map_data: Mapping[str, Mapping[str, str]],
    *,
    request_key_map: Mapping[str, str],
    map_name: str,
    qualifier_name: str,
) -> dict[str, dict[str, str]]:
    inverted_map: dict[str, dict[str, str]] = {}
    for attribute_name, attribute_map in map_data.items():
        mapped_attribute_name = request_key_map.get(attribute_name)
        if mapped_attribute_name is None:
            raise MappingGenerationError(
                f"{map_name} references unknown attribute {attribute_name} in {qualifier_name}"
            )
        inverted_map[mapped_attribute_name] = _invert_map(
            attribute_map, map_name, qualifier_name
        )
    return inverted_map


def _ensure_unique_values(
    map_data: Mapping[str, str],
    map_name: str,
    qualifier_name: str,
) -> None:
    values = list(map_data.values())
    if len(values) != len(set(values)):
        raise MappingGenerationError(
            f"{map_name} values must be unique for qualifier {qualifier_name}"
        )


def _validate_commands(mapping_data: dict[str, Any]) -> None:
    commands = mapping_data.get("commands", {})
    if not isinstance(commands, dict):
        raise MappingGenerationError("commands must be a dict")
    for command_name, command_data in commands.items():
        if not isinstance(command_data, dict):
            raise MappingGenerationError(f"Command data must be dict: {command_name}")
        qualifier = command_data.get("qualifier")
        if not isinstance(qualifier, str):
            raise MappingGenerationError(f"Command qualifier missing: {command_name}")
        status = command_data.get("status")
        if not isinstance(status, str):
            raise MappingGenerationError(f"Command status missing: {command_name}")


def write_mapping_module(output_path: Path, mapping_data: dict[str, Any]) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    module_contents = _build_module_contents(mapping_data)
    output_path.write_text(module_contents, encoding="utf-8")


def _build_module_contents(mapping_data: dict[str, Any]) -> str:
    formatted_data = pformat(mapping_data, width=100, sort_dicts=True)
    return (
        '"""Precompiled mapping data for MQSC <-> snake_case translations."""\n\n'
        "from __future__ import annotations\n\n"
        "MAPPING_DATA = "
        f"{formatted_data}\n"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--source",
        type=Path,
        default=Path("docs/mapping-source.json"),
        help="Path to the base mapping source (JSON or YAML).",
    )
    parser.add_argument(
        "--overrides",
        type=Path,
        default=Path("docs/mapping-overrides.json"),
        help="Path to mapping overrides (JSON or YAML).",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("src/pymqrest/mapping_data.py"),
        help="Output path for the compiled mapping module.",
    )
    args = parser.parse_args()

    base_data = load_mapping_source(args.source)
    overrides_data = load_mapping_overrides(args.overrides)
    merged_data = merge_mapping_overrides(base_data, overrides_data)
    normalized_data = normalize_mapping_data(merged_data)
    write_mapping_module(args.output, normalized_data)


if __name__ == "__main__":
    main()
