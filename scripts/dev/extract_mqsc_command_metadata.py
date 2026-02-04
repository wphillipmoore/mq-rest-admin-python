#!/usr/bin/env python3
"""Extract MQSC command metadata from IBM Docs content API."""
from __future__ import annotations

import argparse
import re
import ssl
import urllib.request
from datetime import UTC, datetime
from html.parser import HTMLParser
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DOCS_ROOT = PROJECT_ROOT / "docs" / "extraction"
IBM_DOCS_BASE = "https://www.ibm.com/docs/api/v1/content/"
QUEUE_FAMILY_DEFINITIONS = {
    "alter-queues": {
        "command": "ALTER",
        "href": "SSFKSJ_9.4.0/refadmin/q085330_.html",
        "caption": "ALTER queues parameters",
        "section_title": "Parameter descriptions for ALTER queues",
        "mode": "table",
    },
    "define-queues": {
        "command": "DEFINE",
        "href": "SSFKSJ_9.4.0/refadmin/q085690_.html",
        "caption": "DEFINE queues parameters",
        "section_title": "Parameter descriptions for DEFINE queues",
        "mode": "table",
    },
    "delete-queues": {
        "command": "DELETE",
        "href": "SSFKSJ_9.4.0/refadmin/q085890_.html",
        "section_title": "Parameter descriptions for DELETE queues",
        "mode": "section",
    },
}
QUEUE_FAMILY_QUALIFIERS = {
    "local queue": "QLOCAL",
    "model queue": "QMODEL",
    "alias queue": "QALIAS",
    "remote queue": "QREMOTE",
}

INPUT_HEADING_PREFIXES = (
    "Parameter descriptions",
    "Keyword and parameter descriptions",
)
OUTPUT_HEADING_PREFIXES = (
    "Requested parameters",
    "Returned parameters",
    "Response parameters",
)
SYNTAX_HEADING_PREFIX = "Syntax diagram"

EXCLUDED_TOKENS = {"IBM", "AMQ", "CSQ", "MQ", "MQSC", "NO", "YES"}
DEFERRED_INPUT_TOKENS = {
    "WHERE": "WHERE filtering is deferred; tracked in issue #71.",
    "ALL": "ALL requests all attributes and is implied when no specific attributes are listed.",
}
DEFERRED_OUTPUT_TOKENS = {
    "ALL": "ALL requests all attributes and is implied when no specific attributes are listed.",
    "WHERE": "WHERE filtering is deferred; tracked in issue #71.",
}
DEFERRED_POSITIONAL_TOKENS = {
    "filter-keyword",
    "filter-value",
    "operator",
}

COMMAND_OVERRIDES: dict[str, dict[str, object]] = {
    "DISPLAY APSTATUS": {
        "output_section_titles": [
            "Application status parameters",
            "Queue manager status parameters",
            "Local status parameters",
        ],
        "notes": [
            "Returned attributes depend on TYPE; capture all parameters but do not model the dependency yet.",
        ],
    },
    "DISPLAY ARCHIVE": {
        "notes": [
            "CMDSCOPE accepts ' ' (single space), qmgr-name, or * on z/OS.",
        ],
    },
    "DISPLAY COMMINFO": {
        "input_remove": ["COMMEV"],
        "output_add": ["DESCR"],
    },
    "DISPLAY CONN": {
        "output_section_titles": [
            "Connection attributes",
            "Handle attributes",
        ],
    },
    "DISPLAY AUTHREC": {
        "input_add": ["SERVCOMP"],
    },
    "DISPLAY CFSTATUS": {
        "output_section_titles": [
            "Summary status",
            "Connection status",
            "Backup status",
            "SMDS status",
        ],
    },
    "DISPLAY CFSTRUCT": {
        "input_remove": ["DESCR", "RECOVER"],
    },
    "DISPLAY CHANNEL": {
        "input_add": ["TYPE"],
        "input_remove": ["CHLTYPE", "DESCR", "MCANAME"],
        "notes": [
            "TYPE is a synonym for CHLTYPE in DISPLAY CHANNEL; use TYPE as the input parameter.",
        ],
    },
    "DISPLAY CHLAUTH": {
        "input_section_titles": ["Parameters for DISPLAY CHLAUTH"],
    },
    "DISPLAY CHSTATUS": {
        "output_section_titles": [
            "Common status",
            "Current-only status",
            "Short status",
        ],
    },
    "DISPLAY CLUSQMGR": {
        "input_add": ["CLUSTER", "CHANNEL"],
        "input_remove": ["STATUS"],
    },
    "ALTER CHANNEL": {
        "input_section_titles": [
            "Parameter descriptions for ALTER CHANNEL",
            "Parameter descriptions for ALTER CHANNEL (MQTT)",
        ],
        "extra_hrefs": ["SSFKSJ_9.4.0/refadmin/q085260_.html"],
        "input_remove": ["LIKE"],
    },
    "ALTER BUFFPOOL": {
        "input_remove": ["LOC"],
    },
    "ALTER CFSTRUCT": {
        "input_remove": ["SMDS"],
    },
    "ALTER QMGR": {
        "input_section_titles": [
            "Parameter descriptions for ALTER QMGR",
            "Queue manager parameters",
        ],
    },
    "DISPLAY ENTAUTH": {
        "input_add": ["OBJNAME", "SERVCOMP"],
    },
    "DISPLAY LOG": {
        "output_add": ["COMMANDS"],
    },
    "DISPLAY NAMELIST": {
        "output_remove": ["NLTYPE", "QSGDISP"],
    },
    "DISPLAY PROCESS": {
        "input_remove": ["APPLTYPE"],
    },
    "DISPLAY PUBSUB": {
        "output_remove": ["TYPE"],
    },
    "DISPLAY QMGR": {
        "input_remove": ["CHINIT", "CLUSTER", "EVENT", "PUBSUB", "SYSTEM"],
        "notes": [
            "CHINIT/CLUSTER/EVENT/PUBSUB/SYSTEM are selector keywords for requested attributes; they are not returned keys.",
        ],
    },
    "DISPLAY QMSTATUS": {
        "input_remove": ["LOG"],
        "notes": [
            "LOG is a selector keyword for requested attributes; it is not a returned key.",
        ],
    },
    "DISPLAY QSTATUS": {
        "input_set": ["CMDSCOPE"],
        "output_section_titles": [
            "Queue status",
            "Handle status",
        ],
        "output_remove": ["MONITOR"],
        "notes": [
            "MONITOR is a selector keyword for requested attributes; it is not a returned key.",
        ],
    },
    "DISPLAY QUEUE": {
        "input_set": [
            "CFSTRUCT",
            "CLUSNL",
            "CLUSTER",
            "CMDSCOPE",
            "PSID",
            "QSGDISP",
            "STGCLASS",
            "TARGTYPE",
            "TYPE",
        ],
        "notes": [
            "CLUSINFO is a selector keyword for requested attributes; it is not a returned key.",
        ],
    },
    "DISPLAY SBSTATUS": {
        "input_remove": ["QSGDISP", "SUBUSER"],
        "output_remove": ["COMMEV"],
        "output_add": ["SUBID", "SUBUSER"],
    },
    "DISPLAY SECURITY": {
        "input_remove": [
            "CSQH037I",
            "CSQH038I",
            "CSQH040I",
            "CSQH042I",
            "INTERVAL",
            "SWITCHES",
            "TIMEOUT",
        ],
    },
    "DISPLAY SERVICE": {
        "input_remove": ["CONTROL"],
    },
    "DISPLAY SMDS": {
        "input_remove": ["DESCR", "RECOVER"],
        "input_add": ["CFSTRUCT"],
    },
    "DISPLAY SMDSCONN": {
        "input_remove": ["DESCR", "RECOVER"],
    },
    "DISPLAY SUB": {
        "output_from_input_sections": True,
        "notes": [
            "Output section header missing; using parameter descriptions to seed output attributes.",
        ],
    },
    "DISPLAY SVSTATUS": {
        "input_remove": ["CONTROL"],
    },
    "DISPLAY TCLUSTER": {
        "output_section_titles": ["Requested attributes"],
    },
    "DISPLAY TOPIC": {
        "input_remove": ["CLUSINFO", "DESCR"],
    },
    "DISPLAY TPSTATUS": {
        "output_section_titles": [
            "Topic status parameters",
            "Sub status parameters",
            "Pub status parameters",
        ],
    },
    "DISPLAY TRACE": {
        "input_remove": ["ACCTG", "CHINIT", "GLOBAL", "STAT"],
        "input_add": ["CLASS", "COMMENT", "DEST", "DETAIL", "RMID", "TNO", "USERID"],
    },
    "DISPLAY USAGE": {
        "input_remove": ["CSQE280I", "CSQE285I"],
    },
}


def strip_tags(text: str) -> str:
    return re.sub(r"<[^>]+>", "", text)


def iter_sections(html: str) -> list[tuple[str, str]]:
    headings: list[tuple[int, int, int, str]] = []
    for match in re.finditer(r"<h([1-6])[^>]*>(.*?)</h\1>", html, flags=re.S | re.I):
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
    token = token.replace("\n", "").strip()
    token = re.sub(r"\s+", " ", token)
    token = re.sub(r"\(\s*", "(", token)
    token = re.sub(r"\s*\)", ")", token)
    if token.endswith(":"):
        return None
    token = token.strip(" ,.;:")
    if not token:
        return None
    if "(" in token:
        token = token.split("(", 1)[0].strip()
    if len(token) < 2:
        return None
    if not re.fullmatch(r"[A-Z][A-Z0-9]*", token):
        return None
    if token in EXCLUDED_TOKENS:
        return None
    return token


def canonicalize_token(token: str) -> str | None:
    return normalize_token(token)


def extract_dl_terms(section_html: str) -> list[str]:
    class DefinitionListParser(HTMLParser):
        def __init__(self) -> None:
            super().__init__()
            self.dd_depth = 0
            self.in_dt = False
            self.buffer: list[str] = []
            self.terms: list[str] = []

        def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
            if tag == "dd":
                self.dd_depth += 1
            elif tag == "dt":
                self.in_dt = True
                self.buffer = []

        def handle_endtag(self, tag: str) -> None:
            if tag == "dd":
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


def extract_parmname_terms(section_html: str) -> list[str]:
    class ParmnameParser(HTMLParser):
        def __init__(self) -> None:
            super().__init__()
            self.dd_depth = 0
            self.in_parmname = False
            self.allowed = False
            self.buffer: list[str] = []
            self.terms: list[str] = []

        def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
            if tag == "dd":
                self.dd_depth += 1
                return
            if tag != "span":
                return
            classes = ""
            for key, value in attrs:
                if key == "class" and value:
                    classes = value
                    break
            if "parmname" in classes and "keyword" in classes:
                self.in_parmname = True
                self.allowed = self.dd_depth == 0
                self.buffer = []

        def handle_endtag(self, tag: str) -> None:
            if tag == "dd":
                self.dd_depth = max(self.dd_depth - 1, 0)
                return
            if tag == "span" and self.in_parmname:
                if self.allowed and self.buffer:
                    text = "".join(self.buffer).strip()
                    if text:
                        self.terms.append(text)
                self.in_parmname = False
                self.allowed = False
                self.buffer = []

        def handle_data(self, data: str) -> None:
            if self.in_parmname:
                self.buffer.append(data)

    parser = ParmnameParser()
    parser.feed(section_html)
    return [strip_tags(term).strip() for term in parser.terms if term.strip()]


def extract_tokens(section_html: str) -> list[str]:
    tokens: set[str] = set()

    def iter_raw_tokens(text: str) -> list[str]:
        if not text:
            return []
        return [part for part in re.split(r"\s+", text.strip()) if part]

    for text in extract_parmname_terms(section_html):
        for token in iter_raw_tokens(text):
            normalized = canonicalize_token(token)
            if normalized:
                tokens.add(normalized)
    for text in re.findall(r'<code class="ph code">(.*?)</code>', section_html, flags=re.S | re.I):
        for token in iter_raw_tokens(strip_tags(text)):
            normalized = canonicalize_token(token)
            if normalized:
                tokens.add(normalized)
    for text in extract_dl_terms(section_html):
        for token in iter_raw_tokens(text):
            normalized = canonicalize_token(token)
            if normalized:
                tokens.add(normalized)
    return sorted(tokens)


def parse_queue_family_table(html: str, caption_keyword: str) -> tuple[dict[str, list[str]], str]:
    tables = re.findall(r"<table[^>]*>.*?</table>", html, flags=re.S | re.I)
    target_table = None
    caption_text = ""
    for table in tables:
        caption_match = re.search(r"<caption[^>]*>(.*?)</caption>", table, flags=re.S | re.I)
        if not caption_match:
            continue
        caption_text = strip_tags(caption_match.group(1)).strip()
        if caption_keyword.lower() in caption_text.lower():
            target_table = table
            break
    if not target_table:
        raise ValueError(f"Queue family table not found for caption {caption_keyword!r}")

    rows = re.findall(r"<tr>(.*?)</tr>", target_table, flags=re.S | re.I)
    if not rows:
        raise ValueError("Queue family table has no rows")

    header_cells = re.findall(r"<t[hd][^>]*>(.*?)</t[hd]>", rows[0], flags=re.S | re.I)
    columns = [strip_tags(cell).strip().lower() for cell in header_cells]
    qualifier_indexes: dict[int, str] = {}
    for idx, column in enumerate(columns):
        qualifier = QUEUE_FAMILY_QUALIFIERS.get(column)
        if qualifier:
            qualifier_indexes[idx] = qualifier

    if not qualifier_indexes:
        raise ValueError("Queue family table headers did not include queue qualifiers")

    parameters_by_qualifier: dict[str, list[str]] = {
        qualifier: [] for qualifier in qualifier_indexes.values()
    }

    for row in rows[1:]:
        cells = re.findall(r"<t[hd][^>]*>(.*?)</t[hd]>", row, flags=re.S | re.I)
        if not cells:
            continue
        raw_param = strip_tags(cells[0]).strip()
        param_tokens = [
            token
            for token in (canonicalize_token(part) for part in re.split(r"\s+", raw_param))
            if token
        ]
        if not param_tokens:
            continue
        param = param_tokens[0]
        for idx, qualifier in qualifier_indexes.items():
            if idx >= len(cells):
                continue
            cell_html = cells[idx]
            if "tick.gif" in cell_html or "alt=\"X\"" in cell_html:
                parameters_by_qualifier[qualifier].append(param)

    return parameters_by_qualifier, caption_text


def parse_queue_family_section(
    html: str,
    section_title: str,
) -> tuple[dict[str, list[str]], str]:
    section_html = None
    for heading, section in iter_sections(html):
        if heading.strip().lower() == section_title.lower():
            section_html = section
            break
    if not section_html:
        raise ValueError(f"Queue family section not found for {section_title!r}")

    parameters = extract_tokens(section_html)
    parameters_by_qualifier = {
        qualifier: list(parameters) for qualifier in QUEUE_FAMILY_QUALIFIERS.values()
    }
    return parameters_by_qualifier, section_title


def extract_varnames(section_html: str) -> list[str]:
    varnames: list[str] = []
    for text in re.findall(r'<var class="keyword varname">(.*?)</var>', section_html):
        token = strip_tags(text).strip()
        if token:
            varnames.append(token)
    return varnames


def extract_syntax_vars(section_html: str) -> list[str]:
    vars_found: list[str] = []
    for text in re.findall(r'<text class="syntaxvar">(.*?)</text>', section_html):
        token = strip_tags(text).strip()
        if token:
            vars_found.append(token)
    return vars_found


def unique_in_order(values: list[str]) -> list[str]:
    seen: set[str] = set()
    ordered: list[str] = []
    for value in values:
        if value in seen:
            continue
        seen.add(value)
        ordered.append(value)
    return ordered


def add_note(notes: list[str], note: str) -> None:
    if note not in notes:
        notes.append(note)


def extract_command_name(html: str) -> str | None:
    match = re.search(r"<h1[^>]*>(.*?)</h1>", html, flags=re.S | re.I)
    if not match:
        return None
    heading = strip_tags(match.group(1)).strip()
    if " (" in heading:
        return heading.split(" (", 1)[0].strip()
    if " on " in heading:
        return heading.split(" on ", 1)[0].strip()
    return heading


def fetch_html(href: str) -> str:
    url = f"{IBM_DOCS_BASE}{href}"
    context = ssl._create_unverified_context()
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "pymqrest-metadata-extract/1.0",
            "Accept": "text/html",
        },
    )
    with urllib.request.urlopen(request, context=context) as response:
        html_bytes = response.read()
    return html_bytes.decode("utf-8", errors="ignore")


def slugify_command(name: str) -> str:
    slug = name.strip().lower().replace(" ", "_")
    slug = re.sub(r"[^a-z0-9_]+", "", slug)
    slug = re.sub(r"_+", "_", slug).strip("_")
    return slug or "unknown"


def yaml_quote(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace('"', "\\\"")
    return f'"{escaped}"'


def write_yaml(
    *,
    output_path: Path,
    name: str,
    href: str,
    input_parameters: list[str],
    output_parameters: list[str],
    input_sections: list[str],
    output_sections: list[str],
    notes: list[str],
) -> None:
    now = datetime.now(UTC)
    generated_at = now.isoformat(timespec="seconds").replace("+00:00", "Z")
    retrieved_at = now.date().isoformat()

    lines: list[str] = []

    def add(line: str, indent: int = 0) -> None:
        lines.append(" " * indent + line)

    add("version: 1")
    add(f"generated_at: {generated_at}")
    add("source:")
    add(f"  product: {yaml_quote('IBM MQ')}")
    add(f"  version: {yaml_quote('9.4.x')}")
    add(f"  content_api: {yaml_quote(IBM_DOCS_BASE)}")
    add(f"  retrieved_at: {yaml_quote(retrieved_at)}")
    add("mqsc_commands:")
    add(f"  - name: {yaml_quote(name)}")
    add(f"    href: {yaml_quote(href)}")
    if input_parameters:
        add("    input_parameters:")
        for token in input_parameters:
            add(f"      - {yaml_quote(token)}")
    else:
        add("    input_parameters: []")
    if output_parameters:
        add("    output_parameters:")
        for token in output_parameters:
            add(f"      - {yaml_quote(token)}")
    else:
        add("    output_parameters: []")
    add("    section_sources:")
    if input_sections:
        add("      input:")
        for title in input_sections:
            add(f"        - {yaml_quote(title)}")
    if output_sections:
        add("      output:")
        for title in output_sections:
            add(f"        - {yaml_quote(title)}")
    if notes:
        add("    notes:")
        for note in notes:
            add(f"      - {yaml_quote(note)}")
    else:
        add("    notes: []")

    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Extract MQSC command metadata from IBM Docs content API."
    )
    parser.add_argument("--href", help="IBM Docs content path")
    parser.add_argument(
        "--queue-family",
        choices=sorted(QUEUE_FAMILY_DEFINITIONS.keys()),
        help="Generate queue-family command metadata.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Output YAML path (overrides --output-dir).",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DOCS_ROOT / "mqsc-command-metadata",
        help="Directory for per-command YAML outputs.",
    )
    args = parser.parse_args()

    if not args.href and not args.queue_family:
        parser.error("Either --href or --queue-family is required.")

    if args.queue_family:
        definition = QUEUE_FAMILY_DEFINITIONS[args.queue_family]
        href = definition["href"]
        html = fetch_html(href)
        mode = definition["mode"]
        if mode == "table":
            parameters_by_qualifier, caption = parse_queue_family_table(
                html, definition["caption"]
            )
        else:
            parameters_by_qualifier, caption = parse_queue_family_section(
                html, definition["section_title"]
            )
        command = definition["command"]
        for qualifier, parameters in parameters_by_qualifier.items():
            name = f"{command} {qualifier}"
            slug = slugify_command(name)
            output_path = args.output_dir / f"{slug}.yaml"
            write_yaml(
                output_path=output_path,
                name=name,
                href=href,
                input_parameters=sorted(set(parameters)),
                output_parameters=[],
                input_sections=[caption] if caption else [],
                output_sections=[],
                notes=[],
            )
        return

    if not args.href:
        parser.error("--href is required when --queue-family is not set.")

    html = fetch_html(args.href)
    name = extract_command_name(html) or "UNKNOWN"
    overrides = COMMAND_OVERRIDES.get(name, {})
    extra_hrefs = overrides.get("extra_hrefs", [])
    html_pages = [(args.href, html)]
    for href in extra_hrefs:  # type: ignore[not-an-iterable]
        html_pages.append((href, fetch_html(href)))

    input_section_titles = {
        title.lower() for title in overrides.get("input_section_titles", [])  # type: ignore[arg-type]
    }
    output_section_titles = {
        title.lower() for title in overrides.get("output_section_titles", [])  # type: ignore[arg-type]
    }

    input_sections: list[tuple[str, str]] = []
    output_sections: list[tuple[str, str]] = []
    syntax_sections: list[tuple[str, str]] = []

    for _href, page_html in html_pages:
        sections = iter_sections(page_html)
        page_input_sections: list[tuple[str, str]] = []
        page_output_sections: list[tuple[str, str]] = []
        page_syntax_section: tuple[str, str] | None = None

        for heading, section in sections:
            lower = heading.lower()
            if input_section_titles:
                if lower in input_section_titles:
                    page_input_sections.append((heading, section))
            else:
                if not page_input_sections and any(
                    lower.startswith(prefix.lower()) for prefix in INPUT_HEADING_PREFIXES
                ):
                    page_input_sections.append((heading, section))
            if output_section_titles:
                if lower in output_section_titles:
                    page_output_sections.append((heading, section))
            else:
                if not page_output_sections and any(
                    lower.startswith(prefix.lower()) for prefix in OUTPUT_HEADING_PREFIXES
                ):
                    page_output_sections.append((heading, section))
            if page_syntax_section is None and lower.startswith(SYNTAX_HEADING_PREFIX.lower()):
                page_syntax_section = (heading, section)

        input_sections.extend(page_input_sections)
        output_sections.extend(page_output_sections)
        if page_syntax_section is not None:
            syntax_sections.append(page_syntax_section)

    input_parameters: list[str] = []
    output_parameters: list[str] = []
    varname_tokens: list[str] = []
    syntax_tokens: list[str] = []
    notes: list[str] = []

    for heading, section in input_sections:
        input_parameters.extend(extract_tokens(section))
        varname_tokens.extend(extract_varnames(section))
    for heading, section in output_sections:
        output_parameters.extend(extract_tokens(section))
    if syntax_sections:
        for _heading, section in syntax_sections:
            syntax_tokens.extend(extract_syntax_vars(section))

    input_parameters = sorted(set(input_parameters))
    output_parameters = sorted(set(output_parameters))
    input_parameters_raw = list(input_parameters)

    if "FilterCondition" in varname_tokens and any(
        token.startswith("filter-") for token in varname_tokens
    ):
        varname_tokens = [token for token in varname_tokens if token != "FilterCondition"]
    if any(token in DEFERRED_POSITIONAL_TOKENS for token in varname_tokens + syntax_tokens):
        add_note(notes, "WHERE filtering is deferred; tracked in issue #71.")

    if overrides.get("output_from_input_sections") and not output_parameters:
        output_parameters = list(input_parameters_raw)

    if not name.startswith("DISPLAY "):
        input_parameters = sorted(set(input_parameters).union(output_parameters))
        output_parameters = []

    input_set = overrides.get("input_set")
    output_set = overrides.get("output_set")
    if input_set is not None:
        input_parameters = list(input_set)  # type: ignore[arg-type]
    if output_set is not None:
        output_parameters = list(output_set)  # type: ignore[arg-type]

    input_add = overrides.get("input_add", [])
    input_remove = overrides.get("input_remove", [])
    output_add = overrides.get("output_add", [])
    output_remove = overrides.get("output_remove", [])
    for token in input_add:  # type: ignore[not-an-iterable]
        if token not in input_parameters:
            input_parameters.append(token)
    for token in input_remove:  # type: ignore[not-an-iterable]
        if token in input_parameters:
            input_parameters.remove(token)
    for token in output_add:  # type: ignore[not-an-iterable]
        if token not in output_parameters:
            output_parameters.append(token)
    for token in output_remove:  # type: ignore[not-an-iterable]
        if token in output_parameters:
            output_parameters.remove(token)
    input_parameters = sorted(set(input_parameters))
    output_parameters = sorted(set(output_parameters))

    if input_parameters:
        deferred = [token for token in input_parameters if token in DEFERRED_INPUT_TOKENS]
        if deferred:
            input_parameters = [token for token in input_parameters if token not in DEFERRED_INPUT_TOKENS]
            for token in deferred:
                add_note(notes, DEFERRED_INPUT_TOKENS[token])

    if output_parameters:
        deferred = [token for token in output_parameters if token in DEFERRED_OUTPUT_TOKENS]
        if deferred:
            output_parameters = [token for token in output_parameters if token not in DEFERRED_OUTPUT_TOKENS]
            for token in deferred:
                add_note(notes, DEFERRED_OUTPUT_TOKENS[token])

    for note in overrides.get("notes", []):  # type: ignore[not-an-iterable]
        add_note(notes, str(note))
    output_path = args.output
    if output_path is None:
        slug = slugify_command(name)
        output_path = args.output_dir / f"{slug}.yaml"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    write_yaml(
        output_path=output_path,
        name=name,
        href=args.href,
        input_parameters=input_parameters,
        output_parameters=output_parameters,
        input_sections=[heading for heading, _section in input_sections],
        output_sections=[heading for heading, _section in output_sections],
        notes=notes,
    )


if __name__ == "__main__":
    main()
