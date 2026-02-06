#!/usr/bin/env python3
"""Build qualifier-scoped MQSC -> PCF attribute mappings."""

from __future__ import annotations

import argparse
import importlib.util
import re
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DOCS_ROOT = PROJECT_ROOT / "docs" / "extraction"
MQSC_METADATA_DIR = DOCS_ROOT / "mqsc-command-metadata"
PCF_METADATA_DIR = DOCS_ROOT / "pcf-command-metadata"
COMMAND_MAP_PATH = DOCS_ROOT / "mqsc-pcf-command-map.yaml"
OVERRIDES_PATH = DOCS_ROOT / "mqsc-pcf-attribute-overrides.yaml"
OUTPUT_DIR = DOCS_ROOT / "mqsc-pcf-attribute-map"

COMMAND_MAP_PATTERN = re.compile(r"^\s*- mqsc: \"(?P<mqsc>.+)\"$")
PCF_LINE_PATTERN = re.compile(r"^\s*pcf: (?P<pcf>.+)$")
INDENT_LEVEL_2 = 2
INDENT_LEVEL_4 = 4
INDENT_LEVEL_6 = 6
INDENT_LEVEL_8 = 8

WORD_ABBREV = {
    "Alteration": "ALT",
    "Application": "APPL",
    "Backout": "BO",
    "Channel": "CHL",
    "Cluster": "CLUS",
    "Command": "CMD",
    "Connection": "CONN",
    "Creation": "CR",
    "Current": "CUR",
    "Default": "DEF",
    "Destination": "DEST",
    "Disposition": "DISP",
    "Expiry": "EXP",
    "Heartbeat": "HB",
    "Identifier": "ID",
    "Interval": "INT",
    "Length": "LEN",
    "Limit": "LIM",
    "Listener": "LIST",
    "Manager": "MGR",
    "Maximum": "MAX",
    "Minimum": "MIN",
    "Message": "MSG",
    "Messages": "MSGS",
    "NonPersistent": "NP",
    "Number": "NUM",
    "Persistence": "PSIST",
    "Priority": "PRTY",
    "Process": "PROC",
    "Queue": "Q",
    "Sequence": "SEQ",
    "Service": "SERVICE",
    "Statistics": "STATS",
    "Storage": "STG",
    "Structure": "STRUC",
    "Subscription": "SUB",
    "Temporary": "TMP",
    "Topic": "TOPIC",
    "Type": "TYPE",
    "User": "USER",
    "Value": "VAL",
    "Weight": "WGHT",
}

SUBSTRING_HINTS = {
    "CHL": "Channel",
    "CLUS": "Cluster",
    "CONN": "Conn",
    "LIST": "Listener",
    "QSG": "QSG",
}

DEFAULT_QUALIFIERS: dict[str, str] = {
    "QUEUE": "queue",
    "QLOCAL": "queue",
    "QREMOTE": "queue",
    "QALIAS": "queue",
    "QMODEL": "queue",
    "CHANNEL": "channel",
    "QMGR": "qmgr",
}


@dataclass(frozen=True)
class CommandMapping:
    mqsc: str
    pcf: str | None


def load_mapping_data() -> dict[str, object]:
    path = PROJECT_ROOT / "src" / "pymqrest" / "mapping_data.py"
    spec = importlib.util.spec_from_file_location("mapping_data", path)
    if spec is None or spec.loader is None:
        message = "Unable to load mapping_data module"
        raise RuntimeError(message)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.MAPPING_DATA


def read_command_map() -> list[CommandMapping]:
    mappings: list[CommandMapping] = []
    current_mqsc: str | None = None
    current_pcf: str | None = None
    for line in COMMAND_MAP_PATH.read_text(encoding="utf-8").splitlines():
        mqsc_match = COMMAND_MAP_PATTERN.match(line)
        if mqsc_match:
            if current_mqsc is not None:
                mappings.append(CommandMapping(current_mqsc, current_pcf))
            current_mqsc = mqsc_match.group("mqsc")
            current_pcf = None
            continue
        if current_mqsc is None:
            continue
        pcf_match = PCF_LINE_PATTERN.match(line)
        if pcf_match:
            value = pcf_match.group("pcf").strip()
            current_pcf = None if value == "null" else value.strip('"')
    if current_mqsc is not None:
        mappings.append(CommandMapping(current_mqsc, current_pcf))
    return mappings


def read_mqsc_metadata() -> dict[str, dict[str, set[str]]]:
    data: dict[str, dict[str, set[str]]] = {}
    for path in sorted(MQSC_METADATA_DIR.glob("*.yaml")):
        current_command: str | None = None
        mode: str | None = None
        for line in path.read_text(encoding="utf-8").splitlines():
            stripped = line.strip()
            if stripped.startswith("- name:"):
                current_command = stripped.split(":", 1)[1].strip().strip('"')
                data.setdefault(current_command, {"input": set(), "output": set()})
                mode = None
                continue
            if stripped.startswith("input_parameters:"):
                mode = "input"
                continue
            if stripped.startswith("output_parameters:"):
                mode = "output"
                continue
            if stripped.startswith(("section_sources:", "notes:")):
                mode = None
                continue
            if mode and stripped.startswith("-"):
                token = stripped[1:].strip().strip('"')
                if token and current_command:
                    data[current_command][mode].add(token)
    return data


def read_pcf_metadata() -> dict[str, dict[str, dict[str, str]]]:
    data: dict[str, dict[str, dict[str, str]]] = {}
    for path in sorted(PCF_METADATA_DIR.glob("*.yaml")):
        current_command: str | None = None
        mode: str | None = None
        for line in path.read_text(encoding="utf-8").splitlines():
            stripped = line.strip()
            if stripped.startswith("- name:"):
                current_command = stripped.split(":", 1)[1].strip().strip('"')
                data.setdefault(current_command, {"input": {}, "output": {}})
                mode = None
                continue
            if stripped.startswith("input_parameters:"):
                mode = "input"
                continue
            if stripped.startswith("output_parameters:"):
                mode = "output"
                continue
            if stripped.startswith(("section_sources:", "notes:")):
                mode = None
                continue
            if mode and stripped.startswith("-"):
                token = stripped[1:].strip().strip('"')
                if ":" in token and current_command:
                    pcf_name, snake = token.split(":", 1)
                    data[current_command][mode][pcf_name] = snake
    return data


def read_overrides() -> dict[str, dict[str, str]]:
    if not OVERRIDES_PATH.exists():
        return {}
    overrides: dict[str, dict[str, str]] = {}
    current_qualifier: str | None = None
    in_overrides = False
    for line in OVERRIDES_PATH.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if stripped.startswith("overrides:"):
            in_overrides = True
            continue
        if not in_overrides:
            continue
        if line.startswith("  ") and stripped.endswith(":"):
            current_qualifier = stripped[:-1]
            overrides.setdefault(current_qualifier, {})
            continue
        if line.startswith("    ") and ":" in stripped and current_qualifier:
            key, value = stripped.split(":", 1)
            overrides[current_qualifier][key.strip()] = value.strip().strip('"')
    return overrides


def read_request_key_value_keys(path: Path) -> dict[str, set[str]]:  # noqa: C901
    if not path.exists():
        return {}
    key_map: dict[str, set[str]] = {}
    in_section = False
    current_qualifier: str | None = None
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if stripped.startswith("request_key_value_map:"):
            in_section = True
            current_qualifier = None
            continue
        if not in_section:
            continue
        indent = len(line) - len(line.lstrip(" "))
        if indent == 0:
            in_section = False
            current_qualifier = None
            continue
        if indent == INDENT_LEVEL_2 and stripped.endswith(":"):
            current_qualifier = stripped[:-1]
            key_map.setdefault(current_qualifier, set())
            continue
        if indent == INDENT_LEVEL_4 and stripped.endswith(":"):
            continue
        if indent == INDENT_LEVEL_6 and stripped.endswith(":"):
            continue
        if indent == INDENT_LEVEL_8 and stripped.startswith("key:") and current_qualifier:
            key_value = stripped.split(":", 1)[1].strip().strip('"')
            key_map[current_qualifier].add(key_value)
    return key_map


def read_skip_tokens(path: Path) -> dict[str, set[str]]:
    if not path.exists():
        return {}
    skip_map: dict[str, set[str]] = {}
    in_section = False
    current_qualifier: str | None = None
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if stripped.startswith("skip_tokens:"):
            in_section = True
            current_qualifier = None
            continue
        if not in_section:
            continue
        indent = len(line) - len(line.lstrip(" "))
        if indent == 0:
            in_section = False
            current_qualifier = None
            continue
        if indent == INDENT_LEVEL_2 and stripped.endswith(":"):
            current_qualifier = stripped[:-1]
            skip_map.setdefault(current_qualifier, set())
            continue
        if indent == INDENT_LEVEL_4 and stripped.startswith("-") and current_qualifier:
            token = stripped[1:].strip().strip('"')
            if token:
                skip_map[current_qualifier].add(token)
    return skip_map


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
        if indent == INDENT_LEVEL_2 and stripped.startswith("-"):
            qualifier = stripped[1:].strip().strip('"')
            if qualifier:
                qualifiers.add(qualifier)
    return qualifiers


def split_pascal(name: str) -> list[str]:
    return re.findall(r"[A-Z]+(?=[A-Z][a-z]|\d|$)|[A-Z]?[a-z]+|\d+", name)


def pcf_abbrev(name: str) -> str:
    parts: list[str] = []
    for word in split_pascal(name):
        if word.isupper():
            parts.append(word)
            continue
        mapped = WORD_ABBREV.get(word)
        if mapped:
            parts.append(mapped)
        else:
            parts.append(word[:3].upper())
    return "".join(parts)


def is_subsequence(needle: str, haystack: str) -> bool:
    it = iter(haystack)
    return all(char in it for char in needle)


def score_candidate(mqsc: str, pcf_name: str) -> int | None:
    mqsc_upper = mqsc.upper()
    pcf_flat = pcf_name.lower()
    abbrev = pcf_abbrev(pcf_name)
    if mqsc_upper == pcf_name.upper():
        score = 0
    elif mqsc_upper == abbrev:
        score = 1
    elif is_subsequence(mqsc_upper.lower(), pcf_flat):
        score = 10 + (len(pcf_flat) - len(mqsc_upper))
    elif is_subsequence(mqsc_upper.lower(), abbrev.lower()):
        score = 20 + (len(abbrev) - len(mqsc_upper))
    else:
        return None

    if mqsc_upper.startswith("QM") and "QMgr" not in pcf_name:
        score += 5
    for token, hint in SUBSTRING_HINTS.items():
        if token in mqsc_upper and hint.lower() not in pcf_name.lower():
            score += 3
    return score


def choose_candidate(mqsc: str, candidates: list[str]) -> tuple[str | None, list[str]]:
    best_score: int | None = None
    best: list[str] = []
    for pcf_name in candidates:
        score = score_candidate(mqsc, pcf_name)
        if score is None:
            continue
        if best_score is None or score < best_score:
            best_score = score
            best = [pcf_name]
        elif score == best_score:
            best.append(pcf_name)
    if best_score is None:
        return None, []
    return (best[0] if len(best) == 1 else None), sorted(best)


def to_snake_case(token: str) -> str:
    parts: list[str] = []
    current: list[str] = []
    length = len(token)
    for index, char in enumerate(token):
        prev = token[index - 1] if index > 0 else ""
        nxt = token[index + 1] if index + 1 < length else ""
        if index > 0 and char.isupper():
            if prev.islower() or prev.isdigit():
                parts.append("".join(current))
                current = [char]
                continue
            if prev.isupper() and nxt.islower():
                parts.append("".join(current))
                current = [char]
                continue
        current.append(char)
    if current:
        parts.append("".join(current))
    return "_".join(part.lower() for part in parts if part)


def main() -> None:  # noqa: C901, PLR0912, PLR0915
    parser = argparse.ArgumentParser(description="Build MQSC -> PCF attribute map.")
    parser.add_argument("--output-dir", type=Path, default=OUTPUT_DIR)
    args = parser.parse_args()
    output_dir: Path = args.output_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    mapping_data = load_mapping_data()
    command_qualifiers: dict[str, str] = {
        name: entry["qualifier"] for name, entry in mapping_data["commands"].items() if "qualifier" in entry
    }

    def resolve_qualifier(command_name: str) -> str | None:
        qualifier = command_qualifiers.get(command_name)
        if qualifier:
            return qualifier
        if " " not in command_name:
            return None
        _, raw_qualifier = command_name.split(" ", 1)
        qualifier_upper = raw_qualifier.strip().upper()
        return DEFAULT_QUALIFIERS.get(qualifier_upper, qualifier_upper.lower())

    mqsc_metadata = read_mqsc_metadata()
    pcf_metadata = read_pcf_metadata()
    overrides = read_overrides()
    request_key_value_keys = read_request_key_value_keys(OVERRIDES_PATH)
    explicit_skip_tokens = read_skip_tokens(OVERRIDES_PATH)
    skip_qualifiers = read_skip_qualifiers(OVERRIDES_PATH)

    qualifier_index: dict[str, dict[str, object]] = {}
    qualifier_usage: dict[str, dict[str, dict[str, set[str]]]] = {}

    for mapping in read_command_map():
        if mapping.pcf is None:
            continue
        qualifier = resolve_qualifier(mapping.mqsc)
        if not qualifier:
            continue
        if qualifier in skip_qualifiers:
            continue
        mqsc_entry = mqsc_metadata.get(mapping.mqsc)
        pcf_entry = pcf_metadata.get(mapping.pcf)
        if mqsc_entry is None or pcf_entry is None:
            continue

        qualifier_data = qualifier_index.setdefault(
            qualifier,
            {
                "mqsc_input": set(),
                "mqsc_output": set(),
                "pcf_input": {},
                "pcf_output": {},
                "mqsc_commands": set(),
                "pcf_commands": set(),
            },
        )
        usage = qualifier_usage.setdefault(qualifier, {})
        qualifier_data["mqsc_commands"].add(mapping.mqsc)
        qualifier_data["pcf_commands"].add(mapping.pcf)
        qualifier_data["mqsc_input"].update(mqsc_entry["input"])
        qualifier_data["mqsc_output"].update(mqsc_entry["output"])
        qualifier_data["pcf_input"].update(pcf_entry["input"])
        qualifier_data["pcf_output"].update(pcf_entry["output"])
        for token in mqsc_entry["input"]:
            token_usage = usage.setdefault(token, {"input": set(), "output": set()})
            token_usage["input"].add(mapping.mqsc)
        for token in mqsc_entry["output"]:
            token_usage = usage.setdefault(token, {"input": set(), "output": set()})
            token_usage["output"].add(mapping.mqsc)

    generated_at = datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")

    for qualifier in sorted(qualifier_index):
        if qualifier in skip_qualifiers:
            continue
        data = qualifier_index[qualifier]
        mqsc_tokens = sorted(set(data["mqsc_input"]) | set(data["mqsc_output"]))
        pcf_input = data["pcf_input"]
        pcf_output = data["pcf_output"]
        overrides_for_qualifier = overrides.get(qualifier, {})
        usage = qualifier_usage.get(qualifier, {})
        skip_tokens = set(request_key_value_keys.get(qualifier, set()))
        skip_tokens.update(explicit_skip_tokens.get(qualifier, set()))

        lines: list[str] = []
        lines.append("version: 1")
        lines.append(f"generated_at: {generated_at}")
        lines.append("source:")
        lines.append(f'  mqsc_metadata_dir: "{MQSC_METADATA_DIR}"')
        lines.append(f'  pcf_metadata_dir: "{PCF_METADATA_DIR}"')
        lines.append(f'  command_map: "{COMMAND_MAP_PATH}"')
        lines.append(f'  overrides: "{OVERRIDES_PATH}"')
        lines.append(f'qualifier: "{qualifier}"')
        lines.append("mqsc_commands:")
        lines.extend([f'  - "{cmd}"' for cmd in sorted(data["mqsc_commands"])])
        lines.append("pcf_commands:")
        lines.extend([f'  - "{cmd}"' for cmd in sorted(data["pcf_commands"])])
        lines.append("attributes:")

        for token in mqsc_tokens:
            if token in skip_tokens:
                continue
            contexts: list[str] = []
            if token in data["mqsc_input"]:
                contexts.append("input")
            if token in data["mqsc_output"]:
                contexts.append("output")

            override = overrides_for_qualifier.get(token)
            status = "unmapped"
            pcf_name: str | None = None
            snake: str | None = None
            candidates: list[str] = []

            if override:
                pcf_name = override
                snake = pcf_input.get(pcf_name) or pcf_output.get(pcf_name) or to_snake_case(pcf_name)
                status = "override"
            else:
                input_candidate, input_matches = choose_candidate(token, list(pcf_input))
                output_candidate, output_matches = choose_candidate(token, list(pcf_output))

                if "input" in contexts and "output" in contexts:
                    if input_candidate and output_candidate and input_candidate == output_candidate:
                        pcf_name = input_candidate
                        status = "matched"
                    elif input_candidate and not output_candidate:
                        pcf_name = input_candidate
                        status = "input-only"
                    elif output_candidate and not input_candidate:
                        pcf_name = output_candidate
                        status = "output-only"
                    elif input_candidate and output_candidate and input_candidate != output_candidate:
                        status = "conflict"
                        candidates = sorted(set(input_matches + output_matches))
                    else:
                        candidates = sorted(set(input_matches + output_matches))
                        if candidates:
                            status = "ambiguous"
                elif "input" in contexts:
                    if input_candidate:
                        pcf_name = input_candidate
                        status = "matched"
                    elif input_matches:
                        candidates = input_matches
                        status = "ambiguous"
                elif "output" in contexts:
                    if output_candidate:
                        pcf_name = output_candidate
                        status = "matched"
                    elif output_matches:
                        candidates = output_matches
                        status = "ambiguous"

                if pcf_name:
                    snake = pcf_input.get(pcf_name) or pcf_output.get(pcf_name) or to_snake_case(pcf_name)

            lines.append(f'  - mqsc: "{token}"')
            lines.append("    contexts:")
            lines.extend([f'      - "{context}"' for context in contexts])
            lines.append(f'    status: "{status}"')
            if pcf_name:
                lines.append(f'    pcf: "{pcf_name}"')
            if snake:
                lines.append(f'    snake: "{snake}"')
            if candidates and not pcf_name:
                lines.append("    candidates:")
                lines.extend([f'      - "{candidate}"' for candidate in candidates])
            command_usage = usage.get(token, {"input": set(), "output": set()})
            lines.append("    mqsc_commands:")
            lines.append("      input:")
            lines.extend([f'        - "{cmd}"' for cmd in sorted(command_usage.get("input", set()))])
            lines.append("      output:")
            lines.extend([f'        - "{cmd}"' for cmd in sorted(command_usage.get("output", set()))])

        output_path = output_dir / f"{qualifier}.yaml"
        output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
