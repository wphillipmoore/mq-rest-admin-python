#!/usr/bin/env python3
"""Rebuild mapping_data.py from extracted MQSC/PCF attribute maps."""
from __future__ import annotations

import argparse
import importlib.util
import pprint
from dataclasses import dataclass
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
ATTR_MAP_DIR = PROJECT_ROOT / "docs" / "extraction" / "mqsc-pcf-attribute-map"
MAPPING_DATA_PATH = PROJECT_ROOT / "src" / "pymqrest" / "mapping_data.py"
OVERRIDES_PATH = PROJECT_ROOT / "docs" / "extraction" / "mqsc-pcf-attribute-overrides.yaml"

ALLOWED_STATUSES = {"matched", "input-only", "output-only", "override"}


@dataclass
class AttributeEntry:
    mqsc: str
    contexts: list[str]
    status: str
    snake: str | None


def load_mapping_data() -> dict[str, object]:
    spec = importlib.util.spec_from_file_location("mapping_data", MAPPING_DATA_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load mapping_data module")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.MAPPING_DATA


def parse_qualifier_file(path: Path) -> tuple[str, list[AttributeEntry]]:
    qualifier: str | None = None
    entries: list[AttributeEntry] = []
    current: AttributeEntry | None = None
    mode: str | None = None

    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if stripped.startswith("qualifier:"):
            qualifier = stripped.split(":", 1)[1].strip().strip('"')
            continue
        if stripped.startswith("- mqsc:"):
            if current is not None:
                entries.append(current)
            mqsc = stripped.split(":", 1)[1].strip().strip('"')
            current = AttributeEntry(mqsc=mqsc, contexts=[], status="", snake=None)
            mode = None
            continue
        if current is None:
            continue
        if stripped.startswith("contexts:"):
            mode = "contexts"
            continue
        if mode == "contexts" and stripped.startswith("-"):
            current.contexts.append(stripped[1:].strip().strip('"'))
            continue
        if stripped.startswith("status:"):
            current.status = stripped.split(":", 1)[1].strip().strip('"')
            mode = None
            continue
        if stripped.startswith("snake:"):
            current.snake = stripped.split(":", 1)[1].strip().strip('"')
            mode = None
            continue
        if stripped.startswith("pcf:") or stripped.startswith("candidates:"):
            mode = None
            continue

    if current is not None:
        entries.append(current)

    if qualifier is None:
        raise ValueError(f"Qualifier not found in {path}")
    return qualifier, entries


def read_request_prefer_map(path: Path) -> dict[str, dict[str, str]]:
    if not path.exists():
        return {}
    prefer_map: dict[str, dict[str, str]] = {}
    in_section = False
    current_qualifier: str | None = None
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if stripped.startswith("request_prefer_mqsc:"):
            in_section = True
            continue
        if not in_section:
            continue
        if line.startswith("  ") and stripped.endswith(":"):
            current_qualifier = stripped[:-1]
            prefer_map.setdefault(current_qualifier, {})
            continue
        if line.startswith("    ") and ":" in stripped and current_qualifier:
            key, value = stripped.split(":", 1)
            prefer_map[current_qualifier][key.strip()] = value.strip().strip('"')
    return prefer_map


def read_request_key_value_map(path: Path) -> dict[str, dict[str, dict[str, dict[str, str]]]]:
    if not path.exists():
        return {}
    key_value_map: dict[str, dict[str, dict[str, dict[str, str]]]] = {}
    in_section = False
    current_qualifier: str | None = None
    current_attribute: str | None = None
    current_value: str | None = None
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if stripped.startswith("request_key_value_map:"):
            in_section = True
            current_qualifier = None
            current_attribute = None
            current_value = None
            continue
        if not in_section:
            continue
        indent = len(line) - len(line.lstrip(" "))
        if indent == 0:
            in_section = False
            current_qualifier = None
            current_attribute = None
            current_value = None
            continue
        if indent == 2 and stripped.endswith(":"):
            current_qualifier = stripped[:-1]
            key_value_map.setdefault(current_qualifier, {})
            current_attribute = None
            current_value = None
            continue
        if indent == 4 and stripped.endswith(":") and current_qualifier:
            current_attribute = stripped[:-1]
            key_value_map[current_qualifier].setdefault(current_attribute, {})
            current_value = None
            continue
        if indent == 6 and stripped.endswith(":") and current_qualifier and current_attribute:
            current_value = stripped[:-1]
            key_value_map[current_qualifier][current_attribute].setdefault(current_value, {})
            continue
        if indent == 8 and ":" in stripped and current_qualifier and current_attribute and current_value:
            key, value = stripped.split(":", 1)
            key_value_map[current_qualifier][current_attribute][current_value][key.strip()] = (
                value.strip().strip('"')
            )
    return key_value_map


def read_request_value_map(path: Path) -> dict[str, dict[str, dict[str, str]]]:
    if not path.exists():
        return {}
    value_map: dict[str, dict[str, dict[str, str]]] = {}
    in_section = False
    current_qualifier: str | None = None
    current_attribute: str | None = None
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if stripped.startswith("request_value_map:"):
            in_section = True
            current_qualifier = None
            current_attribute = None
            continue
        if not in_section:
            continue
        indent = len(line) - len(line.lstrip(" "))
        if indent == 0:
            in_section = False
            current_qualifier = None
            current_attribute = None
            continue
        if indent == 2 and stripped.endswith(":"):
            current_qualifier = stripped[:-1]
            value_map.setdefault(current_qualifier, {})
            current_attribute = None
            continue
        if indent == 4 and stripped.endswith(":") and current_qualifier:
            current_attribute = stripped[:-1]
            value_map[current_qualifier].setdefault(current_attribute, {})
            continue
        if indent == 6 and ":" in stripped and current_qualifier and current_attribute:
            key, value = stripped.split(":", 1)
            value_map[current_qualifier][current_attribute][key.strip()] = value.strip().strip('"')
    return value_map


def read_skip_qualifiers(path: Path) -> set[str]:
    if not path.exists():
        return set()
    in_section = False
    qualifiers: set[str] = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if stripped.startswith("skip_qualifiers:"):
            in_section = True
            continue
        if not in_section:
            continue
        indent = len(line) - len(line.lstrip(" "))
        if indent == 0:
            in_section = False
            continue
        if indent == 2 and stripped.startswith("-"):
            qualifier = stripped[1:].strip().strip('"')
            if qualifier:
                qualifiers.add(qualifier)
    return qualifiers


def build_maps(
    entries: list[AttributeEntry],
    *,
    prefer_mqsc: dict[str, str],
) -> tuple[dict[str, str], dict[str, str], list[str]]:
    request_candidates: dict[str, set[str]] = {}
    response_key_map: dict[str, str] = {}
    response_conflicts: set[str] = set()
    collisions: list[str] = []

    for entry in entries:
        if entry.status not in ALLOWED_STATUSES:
            continue
        if entry.snake is None:
            continue
        if "input" in entry.contexts:
            request_candidates.setdefault(entry.snake, set()).add(entry.mqsc)
        if "output" in entry.contexts:
            if entry.mqsc in response_conflicts:
                continue
            existing = response_key_map.get(entry.mqsc)
            if existing and existing != entry.snake:
                collisions.append(f"response:{entry.mqsc}:{existing}:{entry.snake}")
                response_conflicts.add(entry.mqsc)
                response_key_map.pop(entry.mqsc, None)
            else:
                response_key_map[entry.mqsc] = entry.snake

    request_key_map: dict[str, str] = {}
    for snake, candidates in request_candidates.items():
        if len(candidates) == 1:
            request_key_map[snake] = next(iter(candidates))
            continue
        preferred = prefer_mqsc.get(snake)
        if preferred and preferred in candidates:
            request_key_map[snake] = preferred
            collisions.append(f"request:{snake}:{','.join(sorted(candidates))}:preferred:{preferred}")
            continue
        collisions.append(f"request:{snake}:{','.join(sorted(candidates))}")

    return request_key_map, response_key_map, collisions


def main() -> None:
    parser = argparse.ArgumentParser(description="Build src/pymqrest/mapping_data.py")
    parser.add_argument("--attr-dir", type=Path, default=ATTR_MAP_DIR)
    parser.add_argument("--output", type=Path, default=MAPPING_DATA_PATH)
    args = parser.parse_args()

    mapping_data = load_mapping_data()
    qualifiers = mapping_data.setdefault("qualifiers", {})
    if not isinstance(qualifiers, dict):
        raise RuntimeError("mapping_data.qualifiers is not a dict")

    collision_log: list[str] = []
    prefer_map = read_request_prefer_map(OVERRIDES_PATH)
    request_key_value_map = read_request_key_value_map(OVERRIDES_PATH)
    request_value_map = read_request_value_map(OVERRIDES_PATH)
    skip_qualifiers = read_skip_qualifiers(OVERRIDES_PATH)

    commands = mapping_data.get("commands")
    if isinstance(commands, dict) and skip_qualifiers:
        filtered_commands: dict[str, object] = {}
        for command_name, command_data in commands.items():
            if isinstance(command_data, dict):
                qualifier = command_data.get("qualifier")
                if isinstance(qualifier, str) and qualifier in skip_qualifiers:
                    continue
            filtered_commands[command_name] = command_data
        mapping_data["commands"] = filtered_commands
        if isinstance(qualifiers, dict):
            for qualifier in skip_qualifiers:
                qualifiers.pop(qualifier, None)
    for path in sorted(args.attr_dir.glob("*.yaml")):
        qualifier, entries = parse_qualifier_file(path)
        if qualifier in skip_qualifiers:
            continue
        request_key_map, response_key_map, collisions = build_maps(
            entries,
            prefer_mqsc=prefer_map.get(qualifier, {}),
        )
        collision_log.extend([f"{qualifier}:{entry}" for entry in collisions])

        qualifier_entry = qualifiers.get(qualifier)
        if not isinstance(qualifier_entry, dict):
            qualifier_entry = {}
        qualifier_entry["request_key_map"] = dict(sorted(request_key_map.items()))
        qualifier_entry["response_key_map"] = dict(sorted(response_key_map.items()))
        if qualifier in request_value_map:
            qualifier_entry["request_value_map"] = request_value_map[qualifier]
        else:
            qualifier_entry.setdefault("request_value_map", {})
        qualifier_entry.setdefault("response_value_map", {})
        if qualifier in request_key_value_map:
            qualifier_entry["request_key_value_map"] = request_key_value_map[qualifier]
        qualifiers[qualifier] = qualifier_entry

    mapping_data["qualifiers"] = qualifiers

    output_text = "".join(
        [
            "\"\"\"Precompiled mapping data for MQSC <-> snake_case translations.\"\"\"\n\n",
            "from __future__ import annotations\n\n",
            "MAPPING_DATA: dict[str, object] = ",
            pprint.pformat(mapping_data, width=120, sort_dicts=True),
            "\n",
        ]
    )

    args.output.write_text(output_text, encoding="utf-8")

    if collision_log:
        print("Collisions detected:")
        for item in collision_log:
            print(f"- {item}")


if __name__ == "__main__":
    main()
