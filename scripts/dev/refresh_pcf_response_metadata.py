#!/usr/bin/env python3
"""Refresh missing PCF response metadata in MQSC->PCF extraction docs."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DOCS_ROOT = PROJECT_ROOT / "docs"
COMMAND_METADATA_PATH = DOCS_ROOT / "command-metadata-first-run.md"
QUALIFIER_ROOT = DOCS_ROOT / "mqsc-pcf-parameter-extraction"
SUMMARY_PATH = DOCS_ROOT / "mqsc-pcf-parameter-extraction-first-run.md"


@dataclass(frozen=True)
class PcfParameter:
    name: str
    pcf_type: str | None
    type_hint: str | None
    enum_values: list[str] = field(default_factory=list)


@dataclass(frozen=True)
class PcfResponseMetadata:
    response_href: str | None
    response_parameters: list[PcfParameter]


def _leading_spaces(line: str) -> int:
    return len(line) - len(line.lstrip(" "))


def load_pcf_response_metadata(path: Path) -> dict[str, PcfResponseMetadata]:  # noqa: C901, PLR0912, PLR0915
    lines = path.read_text(encoding="utf-8").splitlines()
    in_yaml = False
    in_pcf = False
    current_name: str | None = None
    current_href: str | None = None
    response_parameters: list[PcfParameter] = []
    response_map: dict[str, PcfResponseMetadata] = {}

    index = 0
    while index < len(lines):
        line = lines[index]
        if line.startswith("```yaml"):
            in_yaml = True
            index += 1
            continue
        if in_yaml and line.startswith("```"):
            break
        if not in_yaml:
            index += 1
            continue
        if line.strip() == "pcf_commands:":
            in_pcf = True
            index += 1
            continue
        if not in_pcf:
            index += 1
            continue

        if line.startswith("  - name: "):
            if current_name:
                response_map[current_name] = PcfResponseMetadata(
                    response_href=current_href,
                    response_parameters=response_parameters,
                )
            current_name = line.split(":", 1)[1].strip()
            current_href = None
            response_parameters = []
            index += 1
            continue

        if current_name and line.strip().startswith("response_href:"):
            value = line.split(":", 1)[1].strip()
            current_href = None if value == "null" else value
            index += 1
            continue

        if current_name and line.strip() == "response_parameters:":
            response_indent = _leading_spaces(line)
            index += 1
            current_param: PcfParameter | None = None
            while index < len(lines):
                inner = lines[index]
                if inner.strip() == "":
                    index += 1
                    continue
                inner_indent = _leading_spaces(inner)
                if inner_indent <= response_indent:
                    break
                if inner.strip().startswith("- name:"):
                    if current_param:
                        response_parameters.append(current_param)
                    current_param = PcfParameter(
                        name=inner.split(":", 1)[1].strip(),
                        pcf_type=None,
                        type_hint=None,
                        enum_values=[],
                    )
                    index += 1
                    continue
                if current_param is None:
                    index += 1
                    continue
                if inner.strip().startswith("pcf_type:"):
                    value = inner.split(":", 1)[1].strip()
                    current_param = PcfParameter(
                        name=current_param.name,
                        pcf_type=value,
                        type_hint=current_param.type_hint,
                        enum_values=current_param.enum_values,
                    )
                    index += 1
                    continue
                if inner.strip().startswith("type_hint:"):
                    value = inner.split(":", 1)[1].strip()
                    current_param = PcfParameter(
                        name=current_param.name,
                        pcf_type=current_param.pcf_type,
                        type_hint=value,
                        enum_values=current_param.enum_values,
                    )
                    index += 1
                    continue
                if inner.strip() == "enum_values:":
                    index += 1
                    enum_values: list[str] = []
                    while index < len(lines):
                        enum_line = lines[index]
                        if enum_line.strip() == "":
                            index += 1
                            continue
                        enum_indent = _leading_spaces(enum_line)
                        if enum_indent <= inner_indent:
                            break
                        if enum_line.strip().startswith("- "):
                            enum_values.append(enum_line.split("-", 1)[1].strip())
                        index += 1
                    current_param = PcfParameter(
                        name=current_param.name,
                        pcf_type=current_param.pcf_type,
                        type_hint=current_param.type_hint,
                        enum_values=enum_values,
                    )
                    continue
                index += 1
            if current_param:
                response_parameters.append(current_param)
            continue

        index += 1

    if current_name:
        response_map[current_name] = PcfResponseMetadata(
            response_href=current_href,
            response_parameters=response_parameters,
        )
    return response_map


def format_response_parameters(indent: str, parameters: Iterable[PcfParameter]) -> list[str]:
    lines: list[str] = []
    list_indent = f"{indent}  "
    field_indent = f"{list_indent}  "
    enum_indent = f"{field_indent}  "
    for param in parameters:
        lines.append(f"{list_indent}- name: {param.name}")
        if param.pcf_type is not None:
            lines.append(f"{field_indent}pcf_type: {param.pcf_type}")
        if param.type_hint is not None:
            lines.append(f"{field_indent}type_hint: {param.type_hint}")
        if param.enum_values:
            lines.append(f"{field_indent}enum_values:")
            lines.extend([f"{enum_indent}- {value}" for value in param.enum_values])
    return lines


def update_qualifier_file(  # noqa: C901, PLR0912, PLR0915
    path: Path,
    pcf_map: dict[str, PcfResponseMetadata],
) -> tuple[int, int]:
    lines = path.read_text(encoding="utf-8").splitlines()
    updated: list[str] = []
    in_yaml = False
    current_pcf_command: str | None = None
    updated_response = False
    in_notes = False
    notes_indent = ""
    href_updates = 0
    param_updates = 0

    for line in lines:
        if line.startswith("```yaml"):
            in_yaml = True
            updated.append(line)
            continue
        if in_yaml and line.startswith("```"):
            in_yaml = False
            current_pcf_command = None
            updated_response = False
            in_notes = False
            updated.append(line)
            continue
        if not in_yaml:
            updated.append(line)
            continue

        if line.strip().startswith("command:") and line.startswith("      command:"):
            current_pcf_command = line.split(":", 1)[1].strip()
            updated_response = False
            in_notes = False
            updated.append(line)
            continue

        if in_notes:
            if line.startswith(f"{notes_indent}  - "):
                if updated_response and "response-doc-not-found" in line:
                    continue
                updated.append(line)
                continue
            in_notes = False

        if current_pcf_command and line.strip().startswith("response_href:"):
            indent = line.split("response_href:")[0]
            current_value = line.split(":", 1)[1].strip()
            metadata = pcf_map.get(current_pcf_command)
            if metadata and current_value == "null" and metadata.response_href:
                updated.append(f"{indent}response_href: {metadata.response_href}")
                updated_response = True
                href_updates += 1
                continue
            updated.append(line)
            continue

        if current_pcf_command and line.strip().startswith("response_parameters:"):
            metadata = pcf_map.get(current_pcf_command)
            if metadata and line.strip() == "response_parameters: []" and metadata.response_parameters:
                indent = line.split("response_parameters:")[0]
                updated.append(f"{indent}response_parameters:")
                updated.extend(format_response_parameters(indent, metadata.response_parameters))
                updated_response = True
                param_updates += 1
                continue
            updated.append(line)
            continue

        if line.strip() == "notes:":
            in_notes = True
            notes_indent = line.split("notes:")[0]
            updated.append(line)
            continue

        updated.append(line)

    path.write_text("\n".join(updated) + "\n", encoding="utf-8")
    return href_updates, param_updates


def update_summary(path: Path, response_found: int, response_missing: int) -> None:
    lines = path.read_text(encoding="utf-8").splitlines()
    updated: list[str] = []
    for line in lines:
        if line.strip().startswith("- PCF response topics found:"):
            updated.append(f"- PCF response topics found: {response_found}")
            continue
        if line.strip().startswith("- PCF response pages fetched:"):
            updated.append(f"- PCF response pages fetched: {response_found}")
            continue
        if line.strip().startswith("- PCF response pages missing:"):
            updated.append(f"- PCF response pages missing: {response_missing}")
            continue
        updated.append(line)
    path.write_text("\n".join(updated) + "\n", encoding="utf-8")


def count_response_hrefs(paths: Iterable[Path]) -> tuple[int, int]:
    found = 0
    missing = 0
    for path in paths:
        lines = path.read_text(encoding="utf-8").splitlines()
        in_yaml = False
        current_command: str | None = None
        for line in lines:
            if line.startswith("```yaml"):
                in_yaml = True
                continue
            if in_yaml and line.startswith("```"):
                break
            if not in_yaml:
                continue
            if line.strip().startswith("command:") and line.startswith("      command:"):
                current_command = line.split(":", 1)[1].strip()
                continue
            if line.strip().startswith("response_href:"):
                if current_command == "null":
                    continue
                value = line.split(":", 1)[1].strip()
                if value == "null":
                    missing += 1
                else:
                    found += 1
    return found, missing


def main() -> None:
    pcf_map = load_pcf_response_metadata(COMMAND_METADATA_PATH)
    href_updates = 0
    param_updates = 0
    qualifier_paths = sorted(QUALIFIER_ROOT.glob("*.md"))
    for path in qualifier_paths:
        href_delta, param_delta = update_qualifier_file(path, pcf_map)
        href_updates += href_delta
        param_updates += param_delta

    response_found, response_missing = count_response_hrefs(qualifier_paths)
    update_summary(SUMMARY_PATH, response_found, response_missing)

    print(f"Updated response hrefs: {href_updates}")
    print(f"Updated response parameters: {param_updates}")


if __name__ == "__main__":
    main()
