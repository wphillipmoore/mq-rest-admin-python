#!/usr/bin/env python3
"""Extract PCF command metadata from IBM Docs content API."""

from __future__ import annotations

import argparse
import re
import ssl
from datetime import UTC, datetime
from html.parser import HTMLParser
from pathlib import Path
from urllib.request import Request, urlopen

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DOCS_ROOT = PROJECT_ROOT / "docs" / "extraction"
PCF_PAGES_PATH = DOCS_ROOT / "pcf-command-pages.yaml"
PCF_MAP_PATH = DOCS_ROOT / "mqsc-pcf-command-map.yaml"
OUTPUT_DIR = DOCS_ROOT / "pcf-command-metadata"

IBM_DOCS_BASE = "https://www.ibm.com/docs/api/v1/content/"

REQUEST_SECTION_PREFIXES = (
    "Required parameters",
    "Optional parameters",
)
RESPONSE_SECTION_PREFIXES = (
    "Response data",
    "Response parameters",
)

GROUP_PREFIX = "Change, Copy, and Create "
GROUP_OBJECT_MAP = {
    "Authentication Information Object": "AUTH_INFO",
    "CF Structure": "CF_STRUC",
    "Channel": "CHANNEL",
    "Channel (MQTT)": "CHANNEL",
    "Channel Listener": "LISTENER",
    "Communication Information Object": "COMM_INFO",
    "Namelist": "NAMELIST",
    "Process": "PROCESS",
    "Queue": "Q",
    "Service": "SERVICE",
    "Storage Class": "STG_CLASS",
    "Subscription": "SUBSCRIPTION",
    "Topic": "TOPIC",
}

VERBS = {"Change": "CHANGE", "Copy": "COPY", "Create": "CREATE"}

EXCLUDED_TOKENS = {
    "Always",
    "Returned",
    "Return",
}
SNAKE_CASE_OVERRIDES: dict[str, str] = {}


class DefinitionListParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.in_dt = False
        self.buffer: list[str] = []
        self.terms: list[str] = []

    def handle_starttag(self, tag: str, _attrs: list[tuple[str, str | None]]) -> None:
        if tag == "dt":
            self.in_dt = True
            self.buffer = []

    def handle_endtag(self, tag: str) -> None:
        if tag == "dt" and self.in_dt:
            text = "".join(self.buffer).strip()
            if text:
                self.terms.append(text)
            self.in_dt = False
            self.buffer = []

    def handle_data(self, data: str) -> None:
        if self.in_dt:
            self.buffer.append(data)


def strip_tags(text: str) -> str:
    return re.sub(r"<[^>]+>", "", text)


def iter_sections(html: str) -> list[tuple[str, str]]:
    headings: list[tuple[int, int, int, str]] = []
    for match in re.finditer(r"<h([1-6])[^>]*>(.*?)</h\1>", html, flags=re.DOTALL | re.IGNORECASE):
        heading_text = strip_tags(match.group(2)).strip()
        headings.append((match.start(), match.end(), int(match.group(1)), heading_text))
    sections: list[tuple[str, str]] = []
    for index, (_start, end, level, heading_text) in enumerate(headings):
        next_start = len(html)
        for next_start_index in range(index + 1, len(headings)):
            if headings[next_start_index][2] <= level:
                next_start = headings[next_start_index][0]
                break
        sections.append((heading_text, html[end:next_start]))
    return sections


def normalize_token(token: str) -> str | None:
    token = token.replace("\xa0", " ").strip()
    token = token.replace("\n", " ").strip()
    token = re.sub(r"\s+", " ", token)
    token = token.strip(" ,.;:")
    if not token:
        return None
    if "(" in token:
        token = token.split("(", 1)[0].strip()
    if " " in token:
        return None
    if not re.fullmatch(r"[A-Z][A-Za-z0-9]*", token):
        return None
    if not re.search(r"[a-z]", token):
        return None
    if token in EXCLUDED_TOKENS:
        return None
    return token


def to_snake_case(token: str) -> str:
    if token in SNAKE_CASE_OVERRIDES:
        return SNAKE_CASE_OVERRIDES[token]
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


def extract_dl_terms(section_html: str) -> list[str]:
    parser = DefinitionListParser()
    parser.feed(section_html)
    return [strip_tags(term).strip() for term in parser.terms if term.strip()]


def extract_parameters(section_html: str) -> list[str]:
    tokens: set[str] = set()
    for text in extract_dl_terms(section_html):
        normalized = normalize_token(text)
        if normalized:
            tokens.add(normalized)
    return sorted(tokens)


def fetch_html(href: str) -> str:
    url = IBM_DOCS_BASE + href
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    req = Request(  # noqa: S310
        url,
        headers={"User-Agent": "pymqrest-pcf-metadata/1.0", "Accept": "text/html"},
    )
    with urlopen(req, context=ctx) as resp:  # noqa: S310
        return resp.read().decode("utf-8", errors="replace")


def read_pcf_pages() -> list[dict[str, str]]:
    entries: list[dict[str, str]] = []
    current: dict[str, str] | None = None
    for line in PCF_PAGES_PATH.read_text(encoding="utf-8").splitlines():
        if line.startswith("- "):
            if current:
                entries.append(current)
            current = {}
            entry_line = line[2:]
        else:
            entry_line = line
        if current is None:
            continue
        if ":" in entry_line:
            key, value = entry_line.split(":", 1)
            current[key.strip()] = value.strip().strip('"')
    if current:
        entries.append(current)
    return entries


def read_mqsc_pcf_map() -> dict[str, list[str]]:
    mapping: dict[str, list[str]] = {}
    current_mqsc: str | None = None
    current_pcf: str | None = None
    for line in PCF_MAP_PATH.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if stripped.startswith("- mqsc:"):
            current_mqsc = stripped.split(":", 1)[1].strip().strip('"')
            current_pcf = None
            continue
        if stripped.startswith("pcf:"):
            value = stripped.split(":", 1)[1].strip()
            if value == "null":
                current_pcf = None
                continue
            current_pcf = value.strip('"')
            if current_pcf and current_mqsc:
                mapping.setdefault(current_pcf, []).append(current_mqsc)
    return mapping


def build_group_index(entries: list[dict[str, str]]) -> dict[str, list[dict[str, str]]]:
    group_index: dict[str, list[dict[str, str]]] = {}
    for entry in entries:
        group = entry.get("group")
        href = entry.get("href")
        if not group or not href:
            continue
        if not group.startswith(GROUP_PREFIX):
            continue
        obj = group[len(GROUP_PREFIX) :]
        suffix = GROUP_OBJECT_MAP.get(obj)
        if not suffix:
            continue
        group_index.setdefault(suffix, []).append(entry)
    return group_index


def extract_page_parameters(html: str) -> tuple[set[str], list[str]]:
    parameters: set[str] = set()
    section_sources: list[str] = []
    for heading, section_html in iter_sections(html):
        for prefix in REQUEST_SECTION_PREFIXES:
            if heading.startswith(prefix):
                section_sources.append(heading)
                parameters.update(extract_parameters(section_html))
                break
    return parameters, section_sources


def extract_response_parameters(html: str) -> tuple[set[str], list[str]]:
    parameters: set[str] = set()
    section_sources: list[str] = []
    for heading, section_html in iter_sections(html):
        for prefix in RESPONSE_SECTION_PREFIXES:
            if heading.startswith(prefix):
                section_sources.append(heading)
                parameters.update(extract_parameters(section_html))
                break
    return parameters, section_sources


def extract_group_parameters(html: str, suffix: str) -> tuple[dict[str, set[str]], dict[str, list[str]]]:
    parameters_by_command: dict[str, set[str]] = {}
    sources_by_command: dict[str, list[str]] = {}
    for heading, section_html in iter_sections(html):
        if not any(heading.startswith(prefix) for prefix in REQUEST_SECTION_PREFIXES):
            continue
        verbs = {verb for verb in VERBS if verb in heading}
        if not verbs:
            continue
        params = extract_parameters(section_html)
        for verb in verbs:
            command = f"MQCMD_{VERBS[verb]}_{suffix}"
            parameters_by_command.setdefault(command, set()).update(params)
            sources_by_command.setdefault(command, []).append(heading)
    return parameters_by_command, sources_by_command


def slugify_command(name: str) -> str:
    return name.lower()


def main() -> None:  # noqa: C901, PLR0912, PLR0915
    parser = argparse.ArgumentParser(description="Extract PCF command metadata.")
    parser.add_argument("--output-dir", type=Path, default=OUTPUT_DIR)
    args = parser.parse_args()

    output_dir = args.output_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    entries = read_pcf_pages()
    mqsc_map = read_mqsc_pcf_map()
    group_index = build_group_index(entries)

    request_pages: dict[str, list[dict[str, str]]] = {}
    response_pages: dict[str, list[dict[str, str]]] = {}
    for entry in entries:
        command = entry.get("command")
        if not command:
            continue
        if entry.get("response") == "true":
            response_pages.setdefault(command, []).append(entry)
        else:
            request_pages.setdefault(command, []).append(entry)

    generated_at = datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")

    for command in sorted(mqsc_map):
        input_params: set[str] = set()
        output_params: set[str] = set()
        input_sources: list[str] = []
        output_sources: list[str] = []
        hrefs: list[str] = []
        response_hrefs: list[str] = []

        for entry in request_pages.get(command, []):
            href = entry.get("href")
            if not href:
                continue
            hrefs.append(href)
            html = fetch_html(href)
            params, sources = extract_page_parameters(html)
            input_params.update(params)
            input_sources.extend(sources)

        for entry in response_pages.get(command, []):
            href = entry.get("href")
            if not href:
                continue
            response_hrefs.append(href)
            html = fetch_html(href)
            params, sources = extract_response_parameters(html)
            output_params.update(params)
            output_sources.extend(sources)

        if not hrefs:
            suffix = command.split("MQCMD_", 1)[-1]
            for verb in VERBS.values():
                prefix = f"{verb}_"
                if suffix.startswith(prefix):
                    suffix = suffix[len(prefix) :]
                    break
            group_entries = group_index.get(suffix, [])
            for group_entry in group_entries:
                href = group_entry.get("href")
                if not href:
                    continue
                hrefs.append(href)
                html = fetch_html(href)
                group_params, group_sources = extract_group_parameters(html, suffix)
                input_params.update(group_params.get(command, set()))
                input_sources.extend(group_sources.get(command, []))

        lines: list[str] = []
        lines.append("version: 1")
        lines.append(f"generated_at: {generated_at}")
        lines.append("source:")
        lines.append('  product: "IBM MQ"')
        lines.append('  version: "9.4.x"')
        lines.append(f'  content_api: "{IBM_DOCS_BASE}"')
        lines.append(f'  retrieved_at: "{datetime.now(UTC).date()}"')
        lines.append("pcf_commands:")
        lines.append(f'  - name: "{command}"')
        mqsc_commands = sorted(set(mqsc_map.get(command, [])))
        if mqsc_commands:
            lines.append("    mqsc_commands:")
            lines.extend([f'      - "{mqsc}"' for mqsc in mqsc_commands])
        if hrefs:
            lines.append("    hrefs:")
            lines.extend([f'      - "{href}"' for href in hrefs])
        if response_hrefs:
            lines.append("    response_hrefs:")
            lines.extend([f'      - "{href}"' for href in response_hrefs])
        lines.append("    input_parameters:")
        lines.extend(
            [f'      - "{param}:{to_snake_case(param)}"' for param in sorted(input_params)],
        )
        lines.append("    output_parameters:")
        lines.extend(
            [f'      - "{param}:{to_snake_case(param)}"' for param in sorted(output_params)],
        )
        lines.append("    section_sources:")
        lines.append("      input:")
        lines.extend([f'        - "{source}"' for source in sorted(set(input_sources))])
        lines.append("      output:")
        lines.extend([f'        - "{source}"' for source in sorted(set(output_sources))])
        lines.append("    notes: []")

        path = output_dir / f"{slugify_command(command)}.yaml"
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
