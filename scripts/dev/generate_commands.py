#!/usr/bin/env python3
"""Generate MQSC command wrapper methods with docstrings for commands.py."""

from __future__ import annotations

import importlib.util
from dataclasses import dataclass
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
MAPPING_DATA_PATH = PROJECT_ROOT / "src" / "pymqrest" / "mapping_data.py"
COMMANDS_PATH = PROJECT_ROOT / "src" / "pymqrest" / "commands.py"

BEGIN_MARKER = "    # BEGIN GENERATED MQSC METHODS"
END_MARKER = "    # END GENERATED MQSC METHODS"

MQSC_REF_URL = "https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-mqsc-commands"
DOCS_BASE_URL = "https://wphillipmoore.github.io/mq-rest-admin-python"

# Hand-written methods that appear before the markers.
HAND_WRITTEN_METHODS = frozenset(
    {
        "display_qmgr",
        "display_qmstatus",
        "display_cmdserv",
        "display_queue",
        "display_channel",
        "define_qlocal",
        "define_qremote",
        "define_qalias",
        "define_qmodel",
        "delete_queue",
        "define_channel",
        "delete_channel",
    }
)

# Qualifiers where the command targets the queue manager itself (no name
# parameter).  The method signature omits `name` and passes `name=None`.
NO_NAME_QUALIFIERS = frozenset(
    {
        "QMGR",
        "CMDSERV",
        "QMSTATUS",
    }
)

# Mapping-data qualifiers that have a corresponding Sphinx docs page.
MAPPINGS_DIR = PROJECT_ROOT / "docs" / "sphinx" / "mappings"


@dataclass(frozen=True)
class CommandSpec:
    """Describes one MQSC command for code generation."""

    verb: str
    mqsc_qualifier: str
    qualifier: str
    is_display: bool
    has_name: bool
    has_mapping_page: bool


def load_mapping_data() -> dict[str, object]:
    spec = importlib.util.spec_from_file_location("mapping_data", MAPPING_DATA_PATH)
    if spec is None or spec.loader is None:
        message = "Unable to load mapping_data module"
        raise RuntimeError(message)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.MAPPING_DATA


def available_mapping_pages() -> frozenset[str]:
    if not MAPPINGS_DIR.is_dir():
        return frozenset()
    return frozenset(path.stem for path in MAPPINGS_DIR.iterdir() if path.suffix == ".md" and path.stem != "index")


def _build_args_section(cmd: CommandSpec) -> list[str]:
    lines = ["        Args:"]
    if cmd.has_name:
        name_desc = "Object name or generic pattern." if cmd.is_display else "Object name."
        lines.append(f"            name: {name_desc}")
    lines.append("            request_parameters: Request attributes as a dict. Mapped")
    lines.append("                from ``snake_case`` when mapping is enabled.")
    lines.append("            response_parameters: Response attributes to return.")
    lines.append('                Defaults to ``["all"]``.')
    if cmd.is_display and cmd.has_name:
        lines.append('            where: Filter expression (e.g. ``"current_depth GT 100"``).')
        lines.append("                The keyword is mapped from ``snake_case`` when mapping")
        lines.append("                is enabled.")
    return lines


def _build_result_section(cmd: CommandSpec) -> list[str]:
    if not cmd.is_display:
        return [
            "        Raises:",
            "            MQRESTCommandError: If the command fails.",
        ]
    if cmd.has_name:
        return [
            "        Returns:",
            "            List of parameter dicts, one per matching object. Empty",
            "            list if no objects match.",
        ]
    return [
        "        Returns:",
        "            Parameter dict, or ``None``.",
    ]


def build_docstring(cmd: CommandSpec) -> str:
    command_label = f"{cmd.verb} {cmd.mqsc_qualifier}"
    lines = [f'        """Execute the MQSC ``{command_label}`` command.']
    lines.append("")
    lines.append(f"        See `MQSC reference <{MQSC_REF_URL}>`__")
    lines.append("        for command details.")
    if cmd.has_mapping_page:
        lines.append(
            f"        See `{cmd.qualifier} attribute mappings <{DOCS_BASE_URL}/mappings/{cmd.qualifier}.html>`__."
        )
    lines.append("")
    lines.extend(_build_args_section(cmd))
    lines.append("")
    lines.extend(_build_result_section(cmd))
    lines.append("")
    lines.append('        """')
    return "\n".join(lines)


def _build_signature(cmd: CommandSpec) -> list[str]:
    method_name = f"{cmd.verb.lower()}_{cmd.mqsc_qualifier.lower()}"
    lines = [f"    def {method_name}(", "        self,"]
    if cmd.has_name:
        lines.append("        name: str | None = None,")
    lines.append("        request_parameters: Mapping[str, object] | None = None,")
    lines.append("        response_parameters: Sequence[str] | None = None,")
    if cmd.is_display and cmd.has_name:
        lines.append("        where: str | None = None,")
    if cmd.is_display and cmd.has_name:
        lines.append("    ) -> list[dict[str, object]]:")
    elif cmd.is_display:
        lines.append("    ) -> dict[str, object] | None:")
    else:
        lines.append("    ) -> None:")
    return lines


def _build_body(cmd: CommandSpec) -> list[str]:
    if cmd.is_display and cmd.has_name:
        call_prefix = "return self._mqsc_command("
    elif cmd.is_display:
        call_prefix = "objects = self._mqsc_command("
    else:
        call_prefix = "self._mqsc_command("

    lines = [f"        {call_prefix}"]
    lines.append(f'            command="{cmd.verb}",')
    lines.append(f'            mqsc_qualifier="{cmd.mqsc_qualifier}",')
    lines.append("            name=name," if cmd.has_name else "            name=None,")
    lines.append("            request_parameters=request_parameters,")
    lines.append("            response_parameters=response_parameters,")
    if cmd.is_display and cmd.has_name:
        lines.append("            where=where,")
    lines.append("        )")

    if cmd.is_display and not cmd.has_name:
        lines.extend(["        if objects:", "            return objects[0]", "        return None"])

    return lines


def generate_method(cmd: CommandSpec) -> str:
    lines = _build_signature(cmd)
    lines.append(build_docstring(cmd))
    lines.extend(_build_body(cmd))
    return "\n".join(lines)


def main() -> None:
    mapping_data = load_mapping_data()
    commands = mapping_data.get("commands", {})
    if not isinstance(commands, dict):
        print("No commands found in MAPPING_DATA")
        return

    mapping_pages = available_mapping_pages()

    # Read current commands.py
    source = COMMANDS_PATH.read_text(encoding="utf-8")

    begin_idx = source.index(BEGIN_MARKER)
    end_idx = source.index(END_MARKER)

    # Collect generated methods
    methods: list[str] = []
    for command_key in sorted(commands.keys()):
        parts = command_key.split(" ", 1)
        if len(parts) != 2:  # noqa: PLR2004
            continue
        verb, mqsc_qualifier = parts
        method_name = f"{verb.lower()}_{mqsc_qualifier.lower()}"

        if method_name in HAND_WRITTEN_METHODS:
            continue

        entry = commands[command_key]
        if not isinstance(entry, dict):
            continue

        qualifier = entry.get("qualifier", mqsc_qualifier.lower())
        if not isinstance(qualifier, str):
            qualifier = mqsc_qualifier.lower()

        cmd = CommandSpec(
            verb=verb,
            mqsc_qualifier=mqsc_qualifier,
            qualifier=qualifier,
            is_display=verb == "DISPLAY",
            has_name=mqsc_qualifier not in NO_NAME_QUALIFIERS,
            has_mapping_page=qualifier in mapping_pages,
        )
        methods.append(generate_method(cmd))

    generated_block = "\n\n".join(methods)

    new_source = (
        source[:begin_idx]
        + BEGIN_MARKER
        + "\n"
        + generated_block
        + "\n\n"
        + END_MARKER
        + source[end_idx + len(END_MARKER) :]
    )

    COMMANDS_PATH.write_text(new_source, encoding="utf-8")
    print(f"Regenerated {len(methods)} methods in {COMMANDS_PATH.relative_to(PROJECT_ROOT)}")


if __name__ == "__main__":
    main()
