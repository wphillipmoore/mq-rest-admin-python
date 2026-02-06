#!/usr/bin/env python3
"""Refresh MQSC output parameter extraction for DISPLAY commands.

This script updates:
- docs/command-metadata-first-run.md (input_only/output_only + notes)
- docs/mqsc-pcf-parameter-extraction/*.md (first-run output_parameters)

It fetches IBM Docs HTML via the content API and parses the "Requested
parameters" sections for DISPLAY commands.
"""

from __future__ import annotations

import re
import ssl
import urllib.request
from dataclasses import dataclass
from datetime import UTC, datetime
from html.parser import HTMLParser
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable
PROJECT_ROOT = Path(__file__).resolve().parents[2]
DOCS_ROOT = PROJECT_ROOT / "docs"
QUALIFIER_ROOT = DOCS_ROOT / "mqsc-pcf-parameter-extraction"
COMMAND_METADATA_PATH = DOCS_ROOT / "command-metadata-first-run.md"
CACHE_ROOT = PROJECT_ROOT / "scripts" / "dev" / "mqsc-output-cache"

IBM_DOCS_BASE = "https://www.ibm.com/docs/api/v1/content/"
OUTPUT_HEADING_PREFIXES = (
    "Requested parameters",
    "Returned parameters",
    "Response parameters",
    "Parameters returned",
    "Parameters that can be returned",
    "Parameters for",
    "Returned data",
    "Response data",
)
OUTPUT_HEADING_KEYWORDS = ("parameters", "status", "attributes", "data")
OUTPUT_HEADING_EXCLUDES = (
    "parameter descriptions",
    "using mqsc commands",
    "syntax diagram",
    "usage notes",
    "related concepts",
    "related tasks",
    "related reference",
    "setting monitor values",
)
FALLBACK_IGNORE_TOKENS = {"ALL", "CMDSCOPE", "QSGDISP", "TYPE", "WHERE"}

DISPLAY_PREFIX = "DISPLAY "
EXCLUDED_TOKENS = {"IBM", "AMQ", "CSQ", "MQ", "NO", "YES"}
MANUAL_OUTPUT_PARAMETERS = {
    "DISPLAY AUTHSERV": ["ALL", "IFVER", "SERVCOMP", "UIDSUPP"],
    "DISPLAY GROUP": ["OBSMSGS"],
    "DISPLAY LSSTATUS": [
        "ADAPTER",
        "BACKLOG",
        "CONTROL",
        "DESCR",
        "IPADDR",
        "LISTENER",
        "LOCLNAME",
        "NTBNAMES",
        "PID",
        "PORT",
        "SESSIONS",
        "SOCKET",
        "STARTDA",
        "STARTTI",
        "STATUS",
        "TPNAME",
        "TRPTYPE",
    ],
    "DISPLAY MAXSMSGS": ["MAXUMSGS"],
    "DISPLAY POLICY": ["ENCALG", "ENFORCE", "KEYREUSE", "POLICY", "SIGNALG"],
    "DISPLAY TRACE": [
        "ACCTG",
        "CHINIT",
        "CLASS",
        "CMDSCOPE",
        "COMMENT",
        "DEST",
        "DETAIL",
        "GLOBAL",
        "GTF",
        "RES",
        "RMID",
        "SMF",
        "SRV",
        "STAT",
        "TNO",
        "USERID",
    ],
}


@dataclass(frozen=True)
class MQSCCommand:
    name: str
    href: str


@dataclass(frozen=True)
class OutputExtraction:
    name: str
    input_parameters: list[str]
    output_parameters: list[str]


def load_mqsc_commands(path: Path) -> list[MQSCCommand]:  # noqa: C901
    lines = path.read_text(encoding="utf-8").splitlines()
    commands: list[MQSCCommand] = []
    in_yaml = False
    in_mqsc = False
    current_name: str | None = None
    current_href: str | None = None
    for line in lines:
        if line.startswith("```yaml"):
            in_yaml = True
            continue
        if in_yaml and line.startswith("```"):
            in_yaml = False
            in_mqsc = False
            continue
        if not in_yaml:
            continue
        if line.strip() == "mqsc_commands:":
            in_mqsc = True
            continue
        if line.strip() == "pcf_commands:":
            in_mqsc = False
            continue
        if not in_mqsc:
            continue
        if line.startswith("  - name: "):
            if current_name and current_href:
                commands.append(MQSCCommand(name=current_name, href=current_href))
            current_name = line.split(":", 1)[1].strip()
            current_href = None
            continue
        if current_name and line.strip().startswith("href:"):
            current_href = line.split(":", 1)[1].strip()
            continue
    if current_name and current_href:
        commands.append(MQSCCommand(name=current_name, href=current_href))
    return commands


def cached_html_path(href: str) -> Path:
    safe_path = href.replace("/", "__")
    return CACHE_ROOT / f"{safe_path}.html"


def fetch_html(href: str) -> str:
    CACHE_ROOT.mkdir(parents=True, exist_ok=True)
    cache_path = cached_html_path(href)
    if cache_path.exists():
        return cache_path.read_text(encoding="utf-8", errors="ignore")
    url = f"{IBM_DOCS_BASE}{href}"
    context = ssl._create_unverified_context()  # noqa: S323, SLF001
    request = urllib.request.Request(  # noqa: S310
        url,
        headers={
            "User-Agent": "pymqrest-metadata-refresh/1.0",
            "Accept": "text/html",
        },
    )
    with urllib.request.urlopen(request, context=context) as response:  # noqa: S310
        html_bytes = response.read()
    html = html_bytes.decode("utf-8", errors="ignore")
    cache_path.write_text(html, encoding="utf-8")
    return html


def normalize_token(token: str) -> str | None:
    token = token.replace("\xa0", " ").strip()
    token = token.replace("\n", "").strip()
    if not token:
        return None
    if not re.match(r"^[A-Z][A-Z0-9_.()]*$", token):
        return None
    if token in EXCLUDED_TOKENS:
        return None
    return token


def canonicalize_token(token: str) -> str | None:
    normalized = normalize_token(token)
    if not normalized:
        return None
    if "(" in normalized:
        base = normalized.split("(", 1)[0].strip()
        if base:
            return base
        return None
    return normalized


def strip_tags(text: str) -> str:
    return re.sub(r"<[^>]+>", "", text)


def iter_sections(html: str) -> Iterable[tuple[str, str]]:
    headings: list[tuple[int, int, int, str]] = []
    for match in re.finditer(r"<h([1-6])[^>]*>(.*?)</h\1>", html, flags=re.DOTALL | re.IGNORECASE):
        heading_text = strip_tags(match.group(2)).strip()
        headings.append((match.start(), match.end(), int(match.group(1)), heading_text))
    for index, (_start, end, level, heading_text) in enumerate(headings):
        next_start = len(html)
        for next_start_index in range(index + 1, len(headings)):
            if headings[next_start_index][2] <= level:
                next_start = headings[next_start_index][0]
                break
        yield heading_text, html[end:next_start]


def extract_tokens(section_html: str) -> list[str]:
    tokens: set[str] = set()
    for text in re.findall(r"<a [^>]*>(.*?)</a>", section_html, flags=re.DOTALL | re.IGNORECASE):
        token = strip_tags(text).strip()
        normalized = canonicalize_token(token)
        if normalized:
            tokens.add(normalized)
    for text in re.findall(
        r'<span class="keyword parmname">(.*?)</span>',
        section_html,
        flags=re.DOTALL | re.IGNORECASE,
    ):
        token = strip_tags(text).strip()
        normalized = canonicalize_token(token)
        if normalized:
            tokens.add(normalized)
    for text in re.findall(r'<code class="ph code">(.*?)</code>', section_html, flags=re.DOTALL | re.IGNORECASE):
        token = strip_tags(text).strip()
        normalized = canonicalize_token(token)
        if normalized:
            tokens.add(normalized)
    for text in extract_dl_terms(section_html):
        normalized = canonicalize_token(text)
        if normalized:
            tokens.add(normalized)
    return sorted(tokens)


def extract_dl_terms(section_html: str) -> list[str]:  # noqa: C901
    class DefinitionListParser(HTMLParser):
        def __init__(self) -> None:
            super().__init__()
            self.dl_depth = 0
            self.dd_depth = 0
            self.in_dt = False
            self.buffer: list[str] = []
            self.terms: list[str] = []

        def handle_starttag(self, tag: str, _attrs: list[tuple[str, str | None]]) -> None:
            if tag == "dl":
                self.dl_depth += 1
            elif tag == "dd":
                self.dd_depth += 1
            elif tag == "dt":
                self.in_dt = True
                self.buffer = []

        def handle_endtag(self, tag: str) -> None:
            if tag == "dl":
                self.dl_depth = max(self.dl_depth - 1, 0)
            elif tag == "dd":
                self.dd_depth = max(self.dd_depth - 1, 0)
            elif tag == "dt":
                if self.dd_depth == 0 and self.buffer:
                    text = "".join(self.buffer).strip()
                    if text:
                        self.terms.append(text)
                self.in_dt = False
                self.buffer = []

        def handle_data(self, data: str) -> None:
            if self.in_dt:
                self.buffer.append(data)

    parser = DefinitionListParser()
    parser.feed(section_html)
    return [strip_tags(term).strip() for term in parser.terms if term.strip()]


def extract_display_output(html: str, command_name: str) -> OutputExtraction:  # noqa: C901
    sections = list(iter_sections(html))
    input_parameters: list[str] = []
    output_parameters: set[str] = set()
    for heading_text, section_html in sections:
        heading_lower = heading_text.lower()
        if "parameter descriptions" in heading_lower and (command_name in heading_text or not input_parameters):
            input_parameters = extract_tokens(section_html)
        if heading_lower.startswith("display "):
            continue
        if any(heading_lower.startswith(prefix) for prefix in OUTPUT_HEADING_EXCLUDES):
            continue
        if "parameter descriptions" in heading_lower:
            continue
        if any(prefix.lower() in heading_lower for prefix in OUTPUT_HEADING_PREFIXES) or any(
            keyword in heading_lower for keyword in OUTPUT_HEADING_KEYWORDS
        ):
            output_parameters.update(extract_tokens(section_html))
    if not output_parameters:
        for heading_text, section_html in sections:
            if heading_text.lower().startswith("syntax diagram"):
                output_parameters.update(extract_tokens(section_html))
        if not output_parameters and input_parameters:
            meaningful_inputs = {item for item in input_parameters if item not in FALLBACK_IGNORE_TOKENS}
            if meaningful_inputs:
                output_parameters.update(input_parameters)
    return OutputExtraction(
        name=command_name,
        input_parameters=input_parameters,
        output_parameters=sorted(output_parameters),
    )


def build_output_map(commands: list[MQSCCommand]) -> dict[str, OutputExtraction]:
    output_map: dict[str, OutputExtraction] = {}
    for command in commands:
        if not command.name.startswith(DISPLAY_PREFIX):
            continue
        html = fetch_html(command.href)
        extraction = extract_display_output(html, command.name)
        if command.name in MANUAL_OUTPUT_PARAMETERS:
            extraction = OutputExtraction(
                name=command.name,
                input_parameters=extraction.input_parameters,
                output_parameters=MANUAL_OUTPUT_PARAMETERS[command.name],
            )
        if extraction.output_parameters:
            output_map[command.name] = extraction
    return output_map


def update_command_metadata(  # noqa: C901, PLR0912, PLR0915
    path: Path,
    output_map: dict[str, OutputExtraction],
    timestamp: str,
) -> None:
    output_count = len(output_map)
    lines = path.read_text(encoding="utf-8").splitlines()
    updated: list[str] = []
    in_yaml = False
    in_mqsc = False
    current_name: str | None = None
    skip_list = False
    list_indent_prefix = ""

    for _index, line in enumerate(lines):
        if line.startswith("```yaml"):
            in_yaml = True
            updated.append(line)
            continue
        if in_yaml and line.startswith("```"):
            in_yaml = False
            in_mqsc = False
            updated.append(line)
            continue
        if not in_yaml:
            updated.append(line)
            continue
        if line.strip() == "mqsc_commands:":
            in_mqsc = True
            updated.append(line)
            continue
        if line.strip() == "pcf_commands:":
            in_mqsc = False
            updated.append(line)
            continue
        if not in_mqsc:
            updated.append(line)
            continue
        if line.startswith("  - name: "):
            current_name = line.split(":", 1)[1].strip()
            updated.append(line)
            continue
        if not current_name or current_name not in output_map:
            updated.append(line)
            continue

        extraction = output_map[current_name]
        if line.strip().startswith("input_only:"):
            indent = line.split("input_only:")[0]
            input_only = sorted(
                {item for item in extraction.input_parameters if item not in extraction.output_parameters},
            )
            if input_only:
                updated.append(f"{indent}input_only:")
                updated.extend([f"{indent}  - {item}" for item in input_only])
            else:
                updated.append(f"{indent}input_only: []")
            skip_list = True
            list_indent_prefix = indent
            continue
        if skip_list:
            if line.startswith(f"{list_indent_prefix}  - "):
                continue
            skip_list = False

        if line.strip().startswith("output_only:"):
            indent = line.split("output_only:")[0]
            output_only = sorted(
                {item for item in extraction.output_parameters if item not in extraction.input_parameters},
            )
            if output_only:
                updated.append(f"{indent}output_only:")
                updated.extend([f"{indent}  - {item}" for item in output_only])
            else:
                updated.append(f"{indent}output_only: []")
            skip_list = True
            list_indent_prefix = indent
            continue
        if skip_list:
            if line.startswith(f"{list_indent_prefix}  - "):
                continue
            skip_list = False

        if line.strip() in {"- mqsc-output-not-parsed", "- mqsc-display-output-empty"}:
            continue
        updated.append(line)

    new_lines = []
    for line in updated:
        if line.strip().startswith("- Output refresh updated:"):
            continue
        if line.strip().startswith("- MQSC commands with output parameters:"):
            new_lines.append(f"- MQSC commands with output parameters: {output_count}")
            continue
        new_lines.append(line)
    final_lines = []
    skip_blank_after_refresh = False
    for line in new_lines:
        if skip_blank_after_refresh and line.strip() == "":
            continue
        if skip_blank_after_refresh:
            skip_blank_after_refresh = False
        final_lines.append(line)
        if line.strip() == "## Summary":
            final_lines.append("")
            final_lines.append(f"- Output refresh updated: {timestamp}")
            skip_blank_after_refresh = True
    path.write_text("\n".join(final_lines) + "\n", encoding="utf-8")


def update_mqsc_pcf_summary(path: Path, output_count: int) -> None:
    lines = path.read_text(encoding="utf-8").splitlines()
    updated = []
    for line in lines:
        if line.strip().startswith("- MQSC commands with output parameters:"):
            updated.append(f"- MQSC commands with output parameters: {output_count}")
            continue
        updated.append(line)
    path.write_text("\n".join(updated) + "\n", encoding="utf-8")


def update_qualifier_file(  # noqa: C901, PLR0912, PLR0915
    path: Path,
    output_map: dict[str, OutputExtraction],
    timestamp: str,
) -> None:
    original_lines = path.read_text(encoding="utf-8").splitlines()
    lines = []
    in_refresh = False
    for line in original_lines:
        if line.strip() == "## Output-parameter refresh":
            in_refresh = True
            continue
        if in_refresh and line.strip() == "```":
            in_refresh = False
            continue
        if in_refresh:
            continue
        lines.append(line)
    updated: list[str] = []
    in_first_run = False
    in_yaml = False
    current_command: str | None = None
    skip_list = False
    list_indent_prefix = ""

    for line in lines:
        if line.strip() == "## First-run extraction":
            in_first_run = True
            updated.append(line)
            continue
        if in_first_run and line.startswith("```yaml"):
            in_yaml = True
            updated.append(line)
            continue
        if in_first_run and in_yaml and line.startswith("```"):
            in_yaml = False
            in_first_run = False
            updated.append(line)
            continue
        if not in_yaml:
            updated.append(line)
            continue
        if line.strip().startswith("name:") and line.startswith("      name:"):
            current_command = line.split(":", 1)[1].strip()
            updated.append(line)
            continue
        if not current_command or current_command not in output_map:
            updated.append(line)
            continue

        extraction = output_map[current_command]
        if line.strip().startswith("output_parameters:"):
            indent = line.split("output_parameters:")[0]
            output_parameters = sorted(set(extraction.output_parameters))
            if output_parameters:
                updated.append(f"{indent}output_parameters:")
                updated.extend([f"{indent}  - {item}" for item in output_parameters])
            else:
                updated.append(f"{indent}output_parameters: []")
            skip_list = True
            list_indent_prefix = indent
            continue
        if skip_list:
            if line.startswith(f"{list_indent_prefix}  - "):
                continue
            skip_list = False
        updated.append(line)

    while updated and updated[-1] == "":
        updated.pop()
    refresh_commands = [
        (command_name, extraction)
        for command_name, extraction in sorted(output_map.items())
        if command_name in "\n".join(lines)
    ]
    if refresh_commands:
        updated.append("")
        updated.append("## Output-parameter refresh")
        updated.append("")
        updated.append("```yaml")
        updated.append("version: 1")
        updated.append(f"generated_at: {timestamp}")
        updated.append("commands:")
        for command_name, extraction in refresh_commands:
            updated.append(f"  - name: {command_name}")
            updated.append("    output_parameters:")
            updated.extend([f"      - {item}" for item in sorted(set(extraction.output_parameters))])
        updated.append("```")

    path.write_text("\n".join(updated) + "\n", encoding="utf-8")


def main() -> None:
    timestamp = datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")
    commands = load_mqsc_commands(COMMAND_METADATA_PATH)
    output_map = build_output_map(commands)

    update_command_metadata(COMMAND_METADATA_PATH, output_map, timestamp)
    update_mqsc_pcf_summary(
        DOCS_ROOT / "mqsc-pcf-parameter-extraction-first-run.md",
        len(output_map),
    )
    for qualifier_path in sorted(QUALIFIER_ROOT.glob("*.md")):
        update_qualifier_file(qualifier_path, output_map, timestamp)


if __name__ == "__main__":
    main()
