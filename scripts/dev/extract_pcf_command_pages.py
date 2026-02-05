#!/usr/bin/env python3
"""Extract PCF command index entries from the IBM MQ PCF reference page."""
from __future__ import annotations

import argparse
import re
import ssl
from dataclasses import dataclass
from datetime import UTC, datetime
from html.parser import HTMLParser
from pathlib import Path
from typing import TYPE_CHECKING
from urllib.parse import parse_qs, urlparse
from urllib.request import Request, urlopen

if TYPE_CHECKING:
    from collections.abc import Iterable

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DOCS_ROOT = PROJECT_ROOT / "docs" / "extraction"
DEFAULT_INDEX_URL = (
    "https://www.ibm.com/docs/en/ibm-mq/9.4.x?topic=reference-definitions-programmable-command-formats"
)
PCF_CONTENT_PREFIX = "SSFKSJ_9.4.0/refadmin/"

MQCMD_PATTERN = re.compile(r"MQCMD_[A-Z0-9_]+")
GROUP_PREFIX = "Change, Copy, and Create "


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
        text = "".join(self._text_parts).strip()
        if text:
            self.anchors.append(Anchor(text=text, href=self._current_href))
        self._current_href = None
        self._text_parts = []

    def handle_data(self, data: str) -> None:
        if self._current_href is not None:
            self._text_parts.append(data)


def fetch_index(url: str) -> str:
    context = ssl._create_unverified_context()
    request = Request(
        url,
        headers={"User-Agent": "pymqrest-pcf-index/1.0", "Accept": "text/html"},
    )
    with urlopen(request, context=context) as response:
        html_bytes = response.read()
    return html_bytes.decode("utf-8", errors="ignore")


def normalize_href(href: str) -> str | None:
    if href.startswith("#"):
        return None
    parsed = urlparse(href)
    if parsed.query:
        query = parse_qs(parsed.query)
        topic = query.get("topic", [None])[0]
        if topic:
            return topic
    if parsed.path:
        path = parsed.path.lstrip("/")
        if path:
            if "/" not in path:
                return f"{PCF_CONTENT_PREFIX}{path}"
            return path
    return None


def parse_platform(title: str) -> tuple[str, str | None]:
    if " on " not in title:
        return title, None
    base, platform = title.rsplit(" on ", 1)
    platform = platform.strip()
    if platform:
        return base.strip(), platform
    return title, None


def parse_index(html: str) -> list[Anchor]:
    parser = AnchorParser()
    parser.feed(html)
    return parser.anchors


def classify_anchor(anchor: Anchor) -> dict[str, object] | None:
    href = normalize_href(anchor.href)
    if not href:
        return None

    text = " ".join(anchor.text.split())
    command_match = MQCMD_PATTERN.search(text)
    is_group = text.startswith(GROUP_PREFIX)
    if not command_match and not is_group:
        return None

    title, platform = parse_platform(text)
    response = " response" in title.lower()

    entry: dict[str, object] = {
        "title": title,
        "href": href,
    }
    if platform:
        entry["platform"] = platform
    if command_match:
        entry["command"] = command_match.group(0)
    if is_group and not command_match:
        entry["group"] = title
    if response:
        entry["response"] = True
    return entry


def write_pages(output_path: Path, *, index_url: str, entries: Iterable[dict[str, object]]) -> None:
    now = datetime.now(UTC)
    generated_at = now.isoformat(timespec="seconds").replace("+00:00", "Z")
    retrieved_at = now.date().isoformat()

    lines: list[str] = []

    def add(line: str, indent: int = 0) -> None:
        lines.append(" " * indent + line)

    add("version: 1")
    add(f"generated_at: {generated_at}")
    add("source:")
    add("  product: \"IBM MQ\"")
    add("  version: \"9.4.x\"")
    add(f"  index_url: \"{index_url}\"")
    add(f"  retrieved_at: \"{retrieved_at}\"")
    add("entries:")
    for entry in entries:
        add("- title: \"" + str(entry["title"]).replace("\"", "\\\"") + "\"", 0)
        add(f"  href: \"{entry['href']}\"")
        if "command" in entry:
            add(f"  command: \"{entry['command']}\"")
        if "group" in entry:
            add(f"  group: \"{entry['group']}\"")
        if "platform" in entry:
            add(f"  platform: \"{entry['platform']}\"")
        if entry.get("response"):
            add("  response: true")

    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_commands(
    output_path: Path,
    *,
    index_url: str,
    commands: Iterable[str],
    groups: Iterable[str],
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
    add("  product: \"IBM MQ\"")
    add("  version: \"9.4.x\"")
    add(f"  index_url: \"{index_url}\"")
    add(f"  retrieved_at: \"{retrieved_at}\"")
    add("pcf_commands:")
    for command in commands:
        add(f"- \"{command}\"")
    add("pcf_groups:")
    for group in groups:
        add(f"- \"{group}\"")
    add("notes:")
    add("- \"Response topics are excluded from pcf_commands; they remain in entries for mapping.\"")

    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Extract PCF command index entries from IBM MQ docs."
    )
    parser.add_argument("--index-url", default=DEFAULT_INDEX_URL)
    parser.add_argument("--input", type=Path, help="Path to a pre-downloaded index HTML file")
    parser.add_argument(
        "--output-pages",
        type=Path,
        default=DOCS_ROOT / "pcf-command-pages.yaml",
    )
    parser.add_argument(
        "--output-commands",
        type=Path,
        default=DOCS_ROOT / "pcf-commands.yaml",
    )
    args = parser.parse_args()

    html = (
        args.input.read_text(encoding="utf-8")
        if args.input
        else fetch_index(args.index_url)
    )
    anchors = parse_index(html)
    entries = []
    for anchor in anchors:
        entry = classify_anchor(anchor)
        if entry:
            entries.append(entry)

    commands = sorted(
        {
            entry["command"]
            for entry in entries
            if entry.get("command") and not entry.get("response")
        }
    )
    groups = sorted(
        {
            entry["group"]
            for entry in entries
            if entry.get("group")
        }
    )

    write_pages(args.output_pages, index_url=args.index_url, entries=entries)
    write_commands(args.output_commands, index_url=args.index_url, commands=commands, groups=groups)


if __name__ == "__main__":
    main()
