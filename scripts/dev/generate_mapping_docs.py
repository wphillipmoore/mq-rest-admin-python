#!/usr/bin/env python3
"""Generate qualifier mapping documentation pages from MAPPING_DATA."""

from __future__ import annotations

import importlib.util
from collections.abc import Mapping
from pathlib import Path
from typing import cast

PROJECT_ROOT = Path(__file__).resolve().parents[2]
MAPPING_DATA_PATH = PROJECT_ROOT / "src" / "pymqrest" / "mapping_data.py"
OUTPUT_DIR = PROJECT_ROOT / "docs" / "sphinx" / "mappings"


def load_mapping_data() -> dict[str, object]:
    spec = importlib.util.spec_from_file_location("mapping_data", MAPPING_DATA_PATH)
    if spec is None or spec.loader is None:
        message = "Unable to load mapping_data module"
        raise RuntimeError(message)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.MAPPING_DATA


def get_related_commands(
    commands: Mapping[str, object],
    qualifier: str,
) -> list[str]:
    related = []
    for command_key, command_entry in commands.items():
        if isinstance(command_entry, Mapping):
            entry_map = cast("Mapping[str, object]", command_entry)
            if entry_map.get("qualifier") == qualifier:
                related.append(command_key)
    return sorted(related)


def render_key_map_table(
    key_map: Mapping[str, object],
    left_header: str,
    right_header: str,
) -> list[str]:
    rows = []
    for left, right in sorted(key_map.items()):
        if isinstance(right, str):
            rows.append(f"| `{left}` | `{right}` |")
    if not rows:
        return []
    return [
        f"| {left_header} | {right_header} |",
        "| --- | --- |",
        *rows,
    ]


def render_value_map_section(
    value_map: Mapping[str, object],
    heading: str,
    left_header: str,
    right_header: str,
) -> list[str]:
    lines = []
    for attr_name in sorted(value_map.keys()):
        attr_values = value_map[attr_name]
        if not isinstance(attr_values, Mapping):
            continue
        attr_map = cast("Mapping[str, str]", attr_values)
        rows = []
        for left, right in sorted(attr_map.items()):
            if isinstance(right, str):
                rows.append(f"| `{left}` | `{right}` |")
        if rows:
            if not lines:
                lines.append(f"## {heading}")
                lines.append("")
            lines.append(f"### {attr_name}")
            lines.append("")
            lines.append(f"| {left_header} | {right_header} |")
            lines.append("| --- | --- |")
            lines.extend(rows)
            lines.append("")
    return lines


def render_key_value_map_section(
    key_value_map: Mapping[str, object],
) -> list[str]:
    lines = []
    for attr_name in sorted(key_value_map.keys()):
        attr_values = key_value_map[attr_name]
        if not isinstance(attr_values, Mapping):
            continue
        value_entries = cast("Mapping[str, object]", attr_values)
        rows = []
        for python_value, mapping in sorted(value_entries.items()):
            if isinstance(mapping, Mapping):
                mapping_dict = cast("Mapping[str, str]", mapping)
                mqsc_key = mapping_dict.get("key", "")
                mqsc_value = mapping_dict.get("value", "")
                rows.append(f"| `{python_value}` | `{mqsc_key}` | `{mqsc_value}` |")
        if rows:
            if not lines:
                lines.append("## Request key-value map")
                lines.append("")
            lines.append(f"### {attr_name}")
            lines.append("")
            lines.append("| Python value | MQSC key | MQSC value |")
            lines.append("| --- | --- | --- |")
            lines.extend(rows)
            lines.append("")
    return lines


def generate_qualifier_page(
    qualifier: str,
    qualifier_entry: Mapping[str, object],
    related_commands: list[str],
) -> str:
    lines = [f"# {qualifier}", ""]
    lines.append(f"Attribute mapping reference for the `{qualifier}` qualifier.")
    lines.append("")

    if related_commands:
        formatted = ", ".join(f"`{cmd}`" for cmd in related_commands)
        lines.append(f"Related MQSC commands: {formatted}")
        lines.append("")

    request_key_map = qualifier_entry.get("request_key_map", {})
    response_key_map = qualifier_entry.get("response_key_map", {})
    request_value_map = qualifier_entry.get("request_value_map", {})
    response_value_map = qualifier_entry.get("response_value_map", {})
    request_key_value_map = qualifier_entry.get("request_key_value_map", {})

    if isinstance(request_key_map, Mapping) and request_key_map:
        table = render_key_map_table(request_key_map, "Python name", "MQSC parameter")
        if table:
            lines.append("## Request key map")
            lines.append("")
            lines.extend(table)
            lines.append("")

    if isinstance(response_key_map, Mapping) and response_key_map:
        table = render_key_map_table(response_key_map, "MQSC parameter", "Python name")
        if table:
            lines.append("## Response key map")
            lines.append("")
            lines.extend(table)
            lines.append("")

    if isinstance(request_value_map, Mapping) and request_value_map:
        section = render_value_map_section(
            request_value_map,
            "Request value map",
            "Python value",
            "MQSC value",
        )
        lines.extend(section)

    if isinstance(response_value_map, Mapping) and response_value_map:
        section = render_value_map_section(
            response_value_map,
            "Response value map",
            "MQSC value",
            "Python value",
        )
        lines.extend(section)

    if isinstance(request_key_value_map, Mapping) and request_key_value_map:
        section = render_key_value_map_section(request_key_value_map)
        lines.extend(section)

    lines.append("---")
    lines.append("")
    lines.append("*Auto-generated by `scripts/dev/generate_mapping_docs.py`.*")
    lines.append("")

    return "\n".join(lines)


def qualifier_has_mappings(qualifier_entry: Mapping[str, object]) -> bool:
    mapping_keys = (
        "request_key_map",
        "response_key_map",
        "request_value_map",
        "response_value_map",
        "request_key_value_map",
    )
    return any(isinstance(qualifier_entry.get(k), Mapping) and qualifier_entry.get(k) for k in mapping_keys)


def generate_index_page(
    mapped: list[str],
    unmapped: list[str],
) -> str:
    lines = [
        "# Qualifier Mapping Reference",
        "",
        "Each page below documents the attribute mappings for one MQSC qualifier.",
        "These mappings translate between Python-friendly `snake_case` names and",
        "MQSC parameter names used by the IBM MQ REST API.",
        "",
        "```{toctree}",
        ":maxdepth: 1",
        "",
    ]
    lines.extend(sorted(mapped))
    lines.append("```")
    lines.append("")

    if unmapped:
        lines.append("## Qualifiers without attribute mappings")
        lines.append("")
        formatted = ", ".join(f"`{q}`" for q in sorted(unmapped))
        lines.append(
            f"The following qualifiers are supported by pymqrest but do not"
            f" have attribute name translations: {formatted}.",
        )
        lines.append("")
        lines.append("```{toctree}")
        lines.append(":hidden:")
        lines.append("")
        lines.extend(sorted(unmapped))
        lines.append("```")
        lines.append("")

    return "\n".join(lines)


def main() -> None:
    mapping_data = load_mapping_data()

    qualifiers = mapping_data.get("qualifiers")
    if not isinstance(qualifiers, Mapping):
        print("No qualifiers found in MAPPING_DATA")
        return

    commands = mapping_data.get("commands")
    if not isinstance(commands, Mapping):
        commands = {}
    commands_map = cast("Mapping[str, object]", commands)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    mapped_qualifiers: list[str] = []
    unmapped_qualifiers: list[str] = []
    for qualifier_name in sorted(qualifiers.keys()):
        qualifier_entry = qualifiers[qualifier_name]
        if not isinstance(qualifier_entry, Mapping):
            continue
        entry_map = cast("Mapping[str, object]", qualifier_entry)
        related = get_related_commands(commands_map, qualifier_name)
        page_content = generate_qualifier_page(qualifier_name, entry_map, related)
        output_path = OUTPUT_DIR / f"{qualifier_name}.md"
        output_path.write_text(page_content, encoding="utf-8")
        if qualifier_has_mappings(entry_map):
            mapped_qualifiers.append(qualifier_name)
        else:
            unmapped_qualifiers.append(qualifier_name)
        print(f"  {output_path.relative_to(PROJECT_ROOT)}")

    index_content = generate_index_page(mapped_qualifiers, unmapped_qualifiers)
    index_path = OUTPUT_DIR / "index.md"
    index_path.write_text(index_content, encoding="utf-8")
    print(f"  {index_path.relative_to(PROJECT_ROOT)}")
    total = len(mapped_qualifiers) + len(unmapped_qualifiers)
    print(
        f"Generated {total} qualifier pages + index"
        f" ({len(mapped_qualifiers)} mapped, {len(unmapped_qualifiers)} unmapped)",
    )


if __name__ == "__main__":
    main()
