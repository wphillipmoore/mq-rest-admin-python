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


def build_maps(entries: list[AttributeEntry]) -> tuple[dict[str, str], dict[str, str], list[str]]:
    request_key_map: dict[str, str] = {}
    response_key_map: dict[str, str] = {}
    request_conflicts: set[str] = set()
    response_conflicts: set[str] = set()
    collisions: list[str] = []

    for entry in entries:
        if entry.status not in ALLOWED_STATUSES:
            continue
        if entry.snake is None:
            continue
        if "input" in entry.contexts:
            if entry.snake in request_conflicts:
                continue
            existing = request_key_map.get(entry.snake)
            if existing and existing != entry.mqsc:
                collisions.append(f"request:{entry.snake}:{existing}:{entry.mqsc}")
                request_conflicts.add(entry.snake)
                request_key_map.pop(entry.snake, None)
            else:
                request_key_map[entry.snake] = entry.mqsc
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
    for path in sorted(args.attr_dir.glob("*.yaml")):
        qualifier, entries = parse_qualifier_file(path)
        request_key_map, response_key_map, collisions = build_maps(entries)
        collision_log.extend([f"{qualifier}:{entry}" for entry in collisions])

        qualifier_entry = qualifiers.get(qualifier)
        if not isinstance(qualifier_entry, dict):
            qualifier_entry = {}
        qualifier_entry["request_key_map"] = dict(sorted(request_key_map.items()))
        qualifier_entry["response_key_map"] = dict(sorted(response_key_map.items()))
        qualifier_entry.setdefault("request_value_map", {})
        qualifier_entry.setdefault("response_value_map", {})
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
