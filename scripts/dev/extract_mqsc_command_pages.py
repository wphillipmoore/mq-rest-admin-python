#!/usr/bin/env python3
"""Extract MQSC command → IBM doc page mappings from the MQSC index."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from datetime import UTC, datetime
from html.parser import HTMLParser
from pathlib import Path
from typing import TYPE_CHECKING
from urllib.request import urlopen

if TYPE_CHECKING:
    from collections.abc import Iterable

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DOCS_ROOT = PROJECT_ROOT / "docs" / "extraction"
COMMAND_LIST_PATH = DOCS_ROOT / "mqsc-commands.yaml"
DEFAULT_INDEX_URL = "https://www.ibm.com/docs/en/ibm-mq/9.4.x?topic=reference-mqsc-commands"
BASE_URL = "https://www.ibm.com/docs/en/ibm-mq/9.4.x?topic="

COMMAND_PREFIXES = (
    "ALTER ",
    "DEFINE ",
    "DELETE ",
    "DISPLAY ",
    "START ",
    "STOP ",
    "SET ",
    "RESET ",
    "REFRESH ",
    "CLEAR ",
    "PING ",
    "PURGE ",
    "RESOLVE ",
    "SUSPEND ",
    "RESUME ",
    "MOVE ",
    "RECOVER ",
    "ARCHIVE ",
    "BACKUP ",
    "RVERIFY ",
)

QUEUE_FAMILY_ENTRIES = {
    "ALTER queues",
    "DEFINE queues",
    "DELETE queues",
}

QUEUE_FAMILY_QUALIFIERS = [
    "QLOCAL",
    "QREMOTE",
    "QALIAS",
    "QMODEL",
]


@dataclass(frozen=True)
class Anchor:
    text: str
    href: str


class AnchorParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self._current_href: str | None = None
        self._text_parts: list[str] = []
        self.anchors: list[Anchor] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag != "a":
            return
        href = dict(attrs).get("href")
        if not href:
            return
        self._current_href = href
        self._text_parts = []

    def handle_endtag(self, tag: str) -> None:
        if tag != "a" or self._current_href is None:
            return
        text = " ".join("".join(self._text_parts).split())
        self.anchors.append(Anchor(text=text, href=self._current_href))
        self._current_href = None
        self._text_parts = []

    def handle_data(self, data: str) -> None:
        if self._current_href is None:
            return
        self._text_parts.append(data)


def fetch_index(url: str) -> str:
    try:
        with urlopen(url) as response:  # nosec B310  # noqa: S310
            return response.read().decode("utf-8")
    except Exception as exc:
        message = f"Failed to fetch {url}. Use --input with a downloaded HTML file."
        raise RuntimeError(message) from exc


def parse_index(html: str) -> list[Anchor]:
    parser = AnchorParser()
    parser.feed(html)
    anchors: list[Anchor] = []
    for anchor in parser.anchors:
        if not anchor.text:
            continue
        if not anchor.href.endswith(".html"):
            continue
        if not anchor.text.startswith(COMMAND_PREFIXES):
            continue
        anchors.append(anchor)
    return anchors


def normalize_command(text: str) -> str:
    if "(" in text:
        return text.split("(", 1)[0].strip()
    return text.strip()


def parse_page_metadata(text: str) -> tuple[str | None, str | None]:
    variant = None
    platform = None
    if "MQTT" in text:
        variant = "MQTT"
    elif "AMQP" in text:
        variant = "AMQP"
    if " on " in text:
        platform = text.split(" on ", 1)[1].strip()
    return platform, variant


def load_command_list(path: Path) -> list[str]:
    commands: list[str] = []
    in_commands = False
    for line in path.read_text().splitlines():
        if line.startswith("commands:"):
            in_commands = True
            continue
        if not in_commands:
            continue
        if line and not line.startswith(" "):
            break
        if line.strip().startswith("-"):
            commands.append(line.split("-", 1)[1].strip())
    return commands


def yaml_quote(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def write_mapping(  # noqa: C901, PLR0912, PLR0915
    *,
    output_path: Path,
    output_md_path: Path,
    index_url: str,
    command_list_path: Path,
    anchors: Iterable[Anchor],
) -> None:
    anchors_list = list(anchors)
    pages_by_command: dict[str, list[dict[str, str]]] = {}
    queue_families: list[dict[str, object]] = []

    for anchor in anchors_list:
        command = normalize_command(anchor.text)
        platform, variant = parse_page_metadata(anchor.text)
        page: dict[str, str] = {"title": anchor.text, "href": anchor.href}
        if platform:
            page["platform"] = platform
        if variant:
            page["variant"] = variant

        if command in QUEUE_FAMILY_ENTRIES:
            queue_families.append(
                {
                    "index_entry": command,
                    "title": anchor.text,
                    "href": anchor.href,
                },
            )
            continue

        pages_by_command.setdefault(command, []).append(page)

    commands = load_command_list(command_list_path)
    command_set = set(commands)
    missing_commands = [command for command in commands if command not in pages_by_command]
    extra_commands = sorted(command for command in pages_by_command if command not in command_set)

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
    add(f"  index_url: {yaml_quote(index_url)}")
    add(f"  base_url: {yaml_quote(BASE_URL)}")
    add(f"  retrieved_at: {yaml_quote(retrieved_at)}")
    add("command_list:")
    add(f"  path: {yaml_quote(str(command_list_path.relative_to(PROJECT_ROOT)))}")
    add("notes:")
    add(
        f"  - {yaml_quote('Derived from the IBM MQSC commands reference index (anchor text + href).')}",
    )
    add(
        f"  - {yaml_quote('Commands are normalized by taking the text before the first ( in the index entry.')}",
    )
    add(
        f"  - {yaml_quote('When multiple pages exist for a command, use platform/variant fields to select the correct page.')}",
    )
    add(
        f"  - {yaml_quote('Queue-family entries are captured separately because the canonical command list omits generic queues entries.')}",
    )

    add("selection_rules:")
    add(f"  - name: {yaml_quote('platform')}")
    add(
        f"    description: {yaml_quote('If a command has platform-specific pages, select the page matching the target platform (for example, z/OS vs Multiplatforms).')}",
    )
    add(f"  - name: {yaml_quote('variant')}")
    add(
        f"    description: {yaml_quote('If a command has protocol-specific pages (MQTT/AMQP), select the page matching the protocol; otherwise use the base page.')}",
    )
    add(f"  - name: {yaml_quote('queue_family')}")
    add(
        f"    description: {yaml_quote('Queue-family index entries map to multiple MQSC qualifiers; select the qualifier-specific section on the shared page.')}",
    )

    add("queue_families:")
    for family in queue_families:
        add(f"  - index_entry: {yaml_quote(str(family['index_entry']))}")
        add(f"    title: {yaml_quote(str(family['title']))}")
        add(f"    href: {yaml_quote(str(family['href']))}")
        add("    qualifiers:")
        for qualifier in QUEUE_FAMILY_QUALIFIERS:
            add(f"      - {yaml_quote(qualifier)}")
        verb = str(family["index_entry"]).split()[0].upper()
        add("    derived_commands:")
        for qualifier in QUEUE_FAMILY_QUALIFIERS:
            add(f"      - {yaml_quote(f'{verb} {qualifier}')}")
        add(
            f"    selection_rule: {yaml_quote('Use the MQSC qualifier (QLOCAL/QREMOTE/QALIAS/QMODEL) to select the relevant section on this page.')}",
        )

    add("commands:")
    for command in commands:
        pages = pages_by_command.get(command, [])
        add(f"  - command: {yaml_quote(command)}")
        if not pages:
            add("    pages: []")
            continue
        add("    pages:")
        for page in pages:
            add(f"      - title: {yaml_quote(page['title'])}")
            add(f"        href: {yaml_quote(page['href'])}")
            if "platform" in page:
                add(f"        platform: {yaml_quote(page['platform'])}")
            if "variant" in page:
                add(f"        variant: {yaml_quote(page['variant'])}")

    if missing_commands:
        add("missing_pages:")
        for command in missing_commands:
            add(f"  - {yaml_quote(command)}")
    else:
        add("missing_pages: []")

    if extra_commands:
        add("unmapped_index_entries:")
        for command in extra_commands:
            add(f"  - {yaml_quote(command)}")
    else:
        add("unmapped_index_entries: []")

    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    duplicates = sorted(
        ((command, len(pages)) for command, pages in pages_by_command.items() if len(pages) > 1),
        key=lambda item: item[0],
    )

    md_lines: list[str] = []
    md_lines.append("# MQSC command → IBM doc page mapping (issue #65)")
    md_lines.append("")
    md_lines.append("## Source")
    md_lines.append("")
    md_lines.append(f"- IBM MQSC commands reference index: {index_url}")
    md_lines.append("")
    md_lines.append("## Extraction notes")
    md_lines.append("")
    md_lines.append(f"- Generated at (UTC): {generated_at}")
    md_lines.append(f"- Raw command entries detected: {len(anchors_list)}")
    md_lines.append(f"- Commands in canonical list: {len(commands)}")
    md_lines.append(f"- Queue-family entries captured: {len(queue_families)}")
    md_lines.append("")
    md_lines.append("## Duplicate command entries")
    md_lines.append("")
    if duplicates:
        for command, count in duplicates:
            md_lines.append(f"- {command}: {count} entries")
    else:
        md_lines.append("- None")
    md_lines.append("")
    md_lines.append("## Output artifact")
    md_lines.append("")
    md_lines.append(f"- {output_path.relative_to(PROJECT_ROOT)}")
    md_lines.append("")
    md_lines.append("## Maintenance")
    md_lines.append("")
    md_lines.append(
        "Re-run the extraction script when IBM updates the MQSC commands index or when the MQSC command list changes.",
    )
    md_lines.append("")

    output_md_path.write_text("\n".join(md_lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Extract MQSC command → IBM doc page mappings from the MQSC index.",
    )
    parser.add_argument("--index-url", default=DEFAULT_INDEX_URL)
    parser.add_argument("--input", type=Path, help="Path to a pre-downloaded index HTML file")
    parser.add_argument(
        "--output-yaml",
        type=Path,
        default=DOCS_ROOT / "mqsc-command-pages.yaml",
    )
    parser.add_argument(
        "--output-md",
        type=Path,
        default=DOCS_ROOT / "mqsc-command-pages.md",
    )
    args = parser.parse_args()

    html = args.input.read_text(encoding="utf-8") if args.input else fetch_index(args.index_url)

    anchors = parse_index(html)
    write_mapping(
        output_path=args.output_yaml,
        output_md_path=args.output_md,
        index_url=args.index_url,
        command_list_path=COMMAND_LIST_PATH,
        anchors=anchors,
    )


if __name__ == "__main__":
    main()
