#!/usr/bin/env python3
"""Build MQSC -> PCF command mapping from MQSC metadata + PCF index/group pages."""
from __future__ import annotations

import argparse
import re
import ssl
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import TYPE_CHECKING
from urllib.request import Request, urlopen

if TYPE_CHECKING:
    from collections.abc import Iterable

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DOCS_ROOT = PROJECT_ROOT / "docs" / "extraction"
MQSC_METADATA_DIR = DOCS_ROOT / "mqsc-command-metadata"
PCF_COMMANDS_PATH = DOCS_ROOT / "pcf-commands.yaml"
PCF_PAGES_PATH = DOCS_ROOT / "pcf-command-pages.yaml"
OUTPUT_PATH = DOCS_ROOT / "mqsc-pcf-command-map.yaml"

IBM_DOCS_BASE = "https://www.ibm.com/docs/api/v1/content/"
MQCMD_PATTERN = re.compile(r"MQCMD_[A-Z0-9_]+")

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

OBJECT_MAP = {
    "APSTATUS": "APPL_STATUS",
    "ARCHIVE": "ARCHIVE",
    "AUTHINFO": "AUTH_INFO",
    "AUTHREC": "AUTH_REC",
    "AUTHSERV": "AUTH_SERVICE",
    "CFSTATUS": "CF_STRUC_STATUS",
    "CFSTRUCT": "CF_STRUC",
    "CHINIT": "CHANNEL_INIT",
    "CHSTATUS": "CHANNEL_STATUS",
    "CHLAUTH": "CHLAUTH_REC",
    "CLUSQMGR": "CLUSTER_Q_MGR",
    "COMMINFO": "COMM_INFO",
    "CONN": "CONNECTION",
    "ENTAUTH": "ENTITY_AUTH",
    "GROUP": "QSG",
    "LOG": "LOG",
    "LSSTATUS": "LISTENER_STATUS",
    "MAXSMSGS": "MAXSMSGS",
    "POLICY": "PROT_POLICY",
    "PUBSUB": "PUBSUB_STATUS",
    "QMGR": "Q_MGR",
    "QMSTATUS": "Q_MGR_STATUS",
    "QSTATUS": "Q_STATUS",
    "QSTATS": "Q_STATS",
    "QUEUE": "Q",
    "QLOCAL": "Q",
    "QREMOTE": "Q",
    "QALIAS": "Q",
    "QMODEL": "Q",
    "SBSTATUS": "SUB_STATUS",
    "SECURITY": "SECURITY",
    "SMDS": "SMDS",
    "SMDSCONN": "SMDSCONN",
    "STGCLASS": "STG_CLASS",
    "SUB": "SUBSCRIPTION",
    "SVSTATUS": "SERVICE_STATUS",
    "SYSTEM": "SYSTEM",
    "TOPIC": "TOPIC",
    "TOPICSTR": "TOPIC_STRING",
    "TPSTATUS": "TOPIC_STATUS",
    "USAGE": "USAGE",
}

VERB_MAP = {
    "ALTER": "CHANGE",
    "DEFINE": "CREATE",
    "DELETE": "DELETE",
    "DISPLAY": "INQUIRE",
    "RESET": "RESET",
    "REFRESH": "REFRESH",
    "START": "START",
    "STOP": "STOP",
    "SET": "SET",
    "PING": "PING",
    "PURGE": "PURGE",
    "RESOLVE": "RESOLVE",
    "SUSPEND": "SUSPEND",
    "RESUME": "RESUME",
    "MOVE": "MOVE",
    "CLEAR": "CLEAR",
    "RECOVER": "RECOVER",
    "BACKUP": "BACKUP",
    "RVERIFY": "REVERIFY",
}

OVERRIDES = {
    "CLEAR QLOCAL": "MQCMD_CLEAR_Q",
    "CLEAR TOPICSTR": "MQCMD_CLEAR_TOPIC_STRING",
    "MOVE QLOCAL": "MQCMD_MOVE_Q",
    "PING CHANNEL": "MQCMD_PING_CHANNEL",
    "PING QMGR": "MQCMD_PING_Q_MGR",
    "PURGE CHANNEL": "MQCMD_PURGE_CHANNEL",
    "RESOLVE CHANNEL": "MQCMD_RESOLVE_CHANNEL",
    "RESOLVE INDOUBT": "MQCMD_RESOLVE_INDOUBT",
    "REFRESH CLUSTER": "MQCMD_REFRESH_CLUSTER",
    "REFRESH QMGR": "MQCMD_REFRESH_Q_MGR",
    "REFRESH SECURITY": "MQCMD_REFRESH_SECURITY",
    "RESET QSTATS": "MQCMD_RESET_Q_STATS",
    "RESET SMDS": "MQCMD_RESET_SMDS",
    "RESET CFSTRUCT": "MQCMD_RESET_CF_STRUC",
    "RESET QMGR": "MQCMD_RESET_Q_MGR",
    "RESET CHANNEL": "MQCMD_RESET_CHANNEL",
    "RESET CLUSTER": "MQCMD_RESET_CLUSTER",
    "RVERIFY SECURITY": "MQCMD_REVERIFY_SECURITY",
    "SET ARCHIVE": "MQCMD_SET_ARCHIVE",
    "SET AUTHREC": "MQCMD_SET_AUTH_REC",
    "SET CHLAUTH": "MQCMD_SET_CHLAUTH_REC",
    "SET LOG": "MQCMD_SET_LOG",
    "SET SYSTEM": "MQCMD_SET_SYSTEM",
    "SET POLICY": "MQCMD_CHANGE_PROT_POLICY",
    "BACKUP CFSTRUCT": "MQCMD_BACKUP_CF_STRUC",
    "RECOVER CFSTRUCT": "MQCMD_RECOVER_CF_STRUC",
    "START CHANNEL": "MQCMD_START_CHANNEL",
    "STOP CHANNEL": "MQCMD_STOP_CHANNEL",
    "START CHINIT": "MQCMD_START_CHANNEL_INIT",
    "STOP CHINIT": "MQCMD_STOP_CHANNEL_INIT",
    "START LISTENER": "MQCMD_START_CHANNEL_LISTENER",
    "STOP LISTENER": "MQCMD_STOP_CHANNEL_LISTENER",
    "STOP CONN": "MQCMD_STOP_CONNECTION",
    "START SERVICE": "MQCMD_START_SERVICE",
    "STOP SERVICE": "MQCMD_STOP_SERVICE",
    "START SMDSCONN": "MQCMD_START_SMDSCONN",
    "STOP SMDSCONN": "MQCMD_STOP_SMDSCONN",
    "SUSPEND QMGR": "MQCMD_SUSPEND_Q_MGR",
    "RESUME QMGR": "MQCMD_RESUME_Q_MGR",
    "DISPLAY GROUP": "MQCMD_INQUIRE_QSG",
    "DISPLAY PUBSUB": "MQCMD_INQUIRE_PUBSUB_STATUS",
    "DISPLAY SBSTATUS": "MQCMD_INQUIRE_SUB_STATUS",
    "DISPLAY LSSTATUS": "MQCMD_INQUIRE_LISTENER_STATUS",
    "DISPLAY SVSTATUS": "MQCMD_INQUIRE_SERVICE_STATUS",
    "DISPLAY TPSTATUS": "MQCMD_INQUIRE_TOPIC_STATUS",
    "DISPLAY QMSTATUS": "MQCMD_INQUIRE_Q_MGR_STATUS",
    "DISPLAY QSTATUS": "MQCMD_INQUIRE_Q_STATUS",
    "DISPLAY QMGR": "MQCMD_INQUIRE_Q_MGR",
    "DISPLAY QUEUE": "MQCMD_INQUIRE_Q",
    "DISPLAY AUTHSERV": "MQCMD_INQUIRE_AUTH_SERVICE",
    "DISPLAY AUTHREC": "MQCMD_INQUIRE_AUTH_RECS",
    "DISPLAY ENTAUTH": "MQCMD_INQUIRE_ENTITY_AUTH",
    "DISPLAY ARCHIVE": "MQCMD_INQUIRE_ARCHIVE",
    "DISPLAY APSTATUS": "MQCMD_INQUIRE_APPL_STATUS",
    "DISPLAY CFSTATUS": "MQCMD_INQUIRE_CF_STRUC_STATUS",
    "DISPLAY CFSTRUCT": "MQCMD_INQUIRE_CF_STRUC",
    "DISPLAY CHINIT": "MQCMD_INQUIRE_CHANNEL_INIT",
    "DISPLAY CHSTATUS": "MQCMD_INQUIRE_CHANNEL_STATUS",
    "DISPLAY CHLAUTH": "MQCMD_INQUIRE_CHLAUTH_RECS",
    "DISPLAY CLUSQMGR": "MQCMD_INQUIRE_CLUSTER_Q_MGR",
    "DISPLAY COMMINFO": "MQCMD_INQUIRE_COMM_INFO",
    "DISPLAY CONN": "MQCMD_INQUIRE_CONNECTION",
    "DISPLAY LISTENER": "MQCMD_INQUIRE_LISTENER",
    "DISPLAY LOG": "MQCMD_INQUIRE_LOG",
    "DISPLAY NAMELIST": "MQCMD_INQUIRE_NAMELIST",
    "DISPLAY PROCESS": "MQCMD_INQUIRE_PROCESS",
    "DISPLAY SECURITY": "MQCMD_INQUIRE_SECURITY",
    "DISPLAY SERVICE": "MQCMD_INQUIRE_SERVICE",
    "DISPLAY SMDS": "MQCMD_INQUIRE_SMDS",
    "DISPLAY SMDSCONN": "MQCMD_INQUIRE_SMDSCONN",
    "DISPLAY STGCLASS": "MQCMD_INQUIRE_STG_CLASS",
    "DISPLAY SUB": "MQCMD_INQUIRE_SUBSCRIPTION",
    "DISPLAY SYSTEM": "MQCMD_INQUIRE_SYSTEM",
    "DISPLAY TOPIC": "MQCMD_INQUIRE_TOPIC",
    "DISPLAY USAGE": "MQCMD_INQUIRE_USAGE",
    "DISPLAY AUTHINFO": "MQCMD_INQUIRE_AUTH_INFO",
    "DISPLAY QMG R": "MQCMD_INQUIRE_Q_MGR",
}


@dataclass(frozen=True)
class GroupEntry:
    title: str
    href: str


def read_mqsc_commands() -> list[str]:
    commands: list[str] = []
    for path in sorted(MQSC_METADATA_DIR.glob("*.yaml")):
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.strip().startswith("- name:"):
                name = line.split(":", 1)[1].strip().strip('"')
                commands.append(name)
                break
    return sorted(set(commands))


def read_pcf_commands() -> list[str]:
    commands: list[str] = []
    in_list = False
    for line in PCF_COMMANDS_PATH.read_text(encoding="utf-8").splitlines():
        if line.startswith("pcf_commands:"):
            in_list = True
            continue
        if in_list:
            if line.startswith("pcf_groups:"):
                break
            if line.startswith("- "):
                commands.append(line[2:].strip().strip('"'))
    return sorted(set(commands))


def read_group_entries() -> list[GroupEntry]:
    entries: list[GroupEntry] = []
    current: dict[str, str] = {}
    for line in PCF_PAGES_PATH.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if stripped.startswith("- title:"):
            if current.get("title") and current.get("href") and current.get("group"):
                entries.append(GroupEntry(title=current["title"], href=current["href"]))
            current = {}
            current["title"] = stripped.split(":", 1)[1].strip().strip('"')
            continue
        if stripped.startswith("href:"):
            current["href"] = stripped.split(":", 1)[1].strip().strip('"')
            continue
        if stripped.startswith("group:"):
            current["group"] = stripped.split(":", 1)[1].strip().strip('"')
            continue
    if current.get("title") and current.get("href") and current.get("group"):
        entries.append(GroupEntry(title=current["title"], href=current["href"]))
    return entries


def fetch_html(href: str) -> str:
    url = f"{IBM_DOCS_BASE}{href}"
    context = ssl._create_unverified_context()
    request = Request(
        url,
        headers={"User-Agent": "pymqrest-pcf-map/1.0", "Accept": "text/html"},
    )
    with urlopen(request, context=context) as response:
        html_bytes = response.read()
    return html_bytes.decode("utf-8", errors="ignore")


def derive_group_commands(entries: Iterable[GroupEntry]) -> dict[str, dict[str, str]]:
    commands: dict[str, dict[str, str]] = {}
    for entry in entries:
        title = entry.title
        if not title.startswith(GROUP_PREFIX):
            continue
        object_title = title[len(GROUP_PREFIX) :].strip()
        object_key = GROUP_OBJECT_MAP.get(object_title)
        if not object_key:
            continue
        try:
            html = fetch_html(entry.href)
        except Exception:
            continue
        found = sorted(set(MQCMD_PATTERN.findall(html)))
        for cmd in found:
            if cmd.startswith("MQCMD_CHANGE_"):
                commands.setdefault(object_key, {})["CHANGE"] = cmd
            if cmd.startswith("MQCMD_COPY_"):
                commands.setdefault(object_key, {})["COPY"] = cmd
            if cmd.startswith("MQCMD_CREATE_"):
                commands.setdefault(object_key, {})["CREATE"] = cmd
    return commands


def object_to_pcf_suffix(obj: str, verb: str) -> str:
    if verb == "DISPLAY":
        if obj == "CHLAUTH":
            return "CHLAUTH_RECS"
        if obj == "AUTHREC":
            return "AUTH_RECS"
    if verb == "SET" and obj == "CHLAUTH":
        return "CHLAUTH_REC"
    return OBJECT_MAP.get(obj, obj)


def build_mapping(
    mqsc_commands: Iterable[str],
    pcf_commands: set[str],
    group_commands: dict[str, dict[str, str]],
) -> list[dict[str, object]]:
    mappings: list[dict[str, object]] = []
    for mqsc in sorted(mqsc_commands):
        entry: dict[str, object] = {"mqsc": mqsc}
        if mqsc in OVERRIDES:
            entry["pcf"] = OVERRIDES[mqsc]
            entry["status"] = "mapped" if OVERRIDES[mqsc] in pcf_commands else "derived"
            mappings.append(entry)
            continue

        parts = mqsc.split()
        if len(parts) < 2:
            entry["pcf"] = None
            entry["status"] = "unmapped"
            mappings.append(entry)
            continue

        verb = parts[0]
        obj = parts[1]
        pcf_verb = VERB_MAP.get(verb)
        if not pcf_verb:
            entry["pcf"] = None
            entry["status"] = "unmapped"
            mappings.append(entry)
            continue

        obj_suffix = object_to_pcf_suffix(obj, verb)

        if pcf_verb in {"CHANGE", "CREATE"} and obj_suffix in group_commands:
            cmd = group_commands[obj_suffix].get(pcf_verb)
            if cmd:
                entry["pcf"] = cmd
                entry["status"] = "derived"
                mappings.append(entry)
                continue

        candidate = f"MQCMD_{pcf_verb}_{obj_suffix}"
        if candidate in pcf_commands:
            entry["pcf"] = candidate
            entry["status"] = "mapped"
        else:
            entry["pcf"] = None
            entry["status"] = "unmapped"
        mappings.append(entry)
    return mappings


def write_yaml(output_path: Path, *, mappings: Iterable[dict[str, object]]) -> None:
    now = datetime.now(UTC)
    generated_at = now.isoformat(timespec="seconds").replace("+00:00", "Z")
    retrieved_at = now.date().isoformat()

    lines: list[str] = []

    def add(line: str, indent: int = 0) -> None:
        lines.append(" " * indent + line)

    add("version: 1")
    add(f"generated_at: {generated_at}")
    add("source:")
    add(f"  mqsc_metadata_dir: \"{MQSC_METADATA_DIR}\"")
    add(f"  pcf_commands: \"{PCF_COMMANDS_PATH}\"")
    add(f"  pcf_index: \"{PCF_PAGES_PATH}\"")
    add(f"  retrieved_at: \"{retrieved_at}\"")
    add("mappings:")
    for entry in mappings:
        add(f"- mqsc: \"{entry['mqsc']}\"")
        pcf = entry.get("pcf")
        if pcf:
            add(f"  pcf: \"{pcf}\"")
        else:
            add("  pcf: null")
        add(f"  status: \"{entry['status']}\"")

    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Build MQSC -> PCF command mapping."
    )
    parser.add_argument("--output", type=Path, default=OUTPUT_PATH)
    args = parser.parse_args()

    mqsc_commands = read_mqsc_commands()
    pcf_commands = set(read_pcf_commands())
    group_entries = read_group_entries()
    group_commands = derive_group_commands(group_entries)
    pcf_commands.update(cmd for mapping in group_commands.values() for cmd in mapping.values())

    mappings = build_mapping(mqsc_commands, pcf_commands, group_commands)
    write_yaml(args.output, mappings=mappings)


if __name__ == "__main__":
    main()
