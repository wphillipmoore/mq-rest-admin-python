#!/usr/bin/env python3
"""
Validate dependency specification rules for pyproject.toml.
"""

from __future__ import annotations

import re
import tomllib
from pathlib import Path

ANCHOR_PREFIX = "# Anchor:"
DEPENDENCY_RECORDS_DIR = Path("docs/dependencies")
PYPROJECT_PATH = Path("pyproject.toml")


class DependencySpecError(Exception):
    """Raised when dependency specification validation fails."""


def ensure_project_root() -> None:
    """Fail fast if invoked outside the repository root."""
    if not PYPROJECT_PATH.is_file():
        raise SystemExit("Run from the repository root (pyproject.toml missing).")


def load_pyproject() -> dict[str, object]:
    with PYPROJECT_PATH.open("rb") as handle:
        return tomllib.load(handle)


def collect_dependency_lines(lines: list[str]) -> dict[tuple[str, str], int]:
    current_section: str | None = None
    dependency_lines: dict[tuple[str, str], int] = {}

    section_pattern = re.compile(r"^\[(.+)]\s*$")
    dependency_pattern = re.compile(r"^([A-Za-z0-9_.-]+)\s*=")

    for index, line in enumerate(lines):
        section_match = section_pattern.match(line.strip())
        if section_match:
            current_section = section_match.group(1)
            continue

        if current_section is None:
            continue

        if current_section == "tool.poetry.dependencies":
            dependency_match = dependency_pattern.match(line)
            if dependency_match:
                dependency_lines[(current_section, dependency_match.group(1))] = index
            continue

        if current_section.startswith("tool.poetry.group.") and current_section.endswith(".dependencies"):
            dependency_match = dependency_pattern.match(line)
            if dependency_match:
                dependency_lines[(current_section, dependency_match.group(1))] = index
            continue

    return dependency_lines


def anchor_comment_for(lines: list[str], line_index: int) -> str | None:
    if line_index == 0:
        return None
    comment_line = lines[line_index - 1].strip()
    if not comment_line.startswith(ANCHOR_PREFIX):
        return None
    return comment_line


def dependency_record_path(dependency_name: str) -> Path:
    return DEPENDENCY_RECORDS_DIR / f"{dependency_name}.md"


def validate_dependency_specs() -> None:
    pyproject = load_pyproject()
    tool_section = pyproject.get("tool")
    if not isinstance(tool_section, dict):
        raise DependencySpecError("Missing [tool] section in pyproject.toml.")

    poetry_section = tool_section.get("poetry")
    if not isinstance(poetry_section, dict):
        raise DependencySpecError("Missing [tool.poetry] section in pyproject.toml.")

    dependencies_section = poetry_section.get("dependencies")
    if not isinstance(dependencies_section, dict):
        raise DependencySpecError("Missing [tool.poetry.dependencies] section in pyproject.toml.")

    group_section = poetry_section.get("group", {})
    if not isinstance(group_section, dict):
        raise DependencySpecError("Invalid [tool.poetry.group] section in pyproject.toml.")

    lines = PYPROJECT_PATH.read_text().splitlines()
    dependency_lines = collect_dependency_lines(lines)
    errors: list[str] = []

    def validate_section(section_name: str, dependencies: dict[str, object]) -> None:
        for dependency_name, dependency_spec in sorted(dependencies.items()):
            if dependency_name == "python":
                continue

            spec_text: str | None = None
            if isinstance(dependency_spec, str):
                spec_text = dependency_spec.strip()
            elif isinstance(dependency_spec, dict):
                version_value = dependency_spec.get("version")
                if isinstance(version_value, str):
                    spec_text = version_value.strip()
            else:
                errors.append(f"{section_name}:{dependency_name} has unsupported spec format.")
                continue

            if not spec_text:
                errors.append(f"{section_name}:{dependency_name} has no version specifier.")
                continue

            if spec_text == "*":
                continue

            line_index = dependency_lines.get((section_name, dependency_name))
            if line_index is None:
                errors.append(f"{section_name}:{dependency_name} missing in pyproject.toml lines.")
                continue

            anchor_comment = anchor_comment_for(lines, line_index)
            record_path = dependency_record_path(dependency_name)

            if anchor_comment is None:
                errors.append(
                    f"{section_name}:{dependency_name} uses a non-default spec and requires anchor comment "
                    f"'{ANCHOR_PREFIX}' with record reference."
                )
            elif f"docs/dependencies/{dependency_name}.md" not in anchor_comment:
                errors.append(
                    f"{section_name}:{dependency_name} anchor comment must reference docs/dependencies/{dependency_name}.md."
                )

            if not record_path.is_file():
                errors.append(
                    f"{section_name}:{dependency_name} missing dependency record at {record_path}."
                )

    validate_section("tool.poetry.dependencies", dependencies_section)

    for group_name, group_value in group_section.items():
        if not isinstance(group_value, dict):
            errors.append(f"tool.poetry.group.{group_name} must be a table.")
            continue
        group_dependencies = group_value.get("dependencies")
        if not isinstance(group_dependencies, dict):
            continue
        section_name = f"tool.poetry.group.{group_name}.dependencies"
        validate_section(section_name, group_dependencies)

    if errors:
        message = "Dependency specification validation failed:\n" + "\n".join(
            f"- {error}" for error in errors
        )
        raise DependencySpecError(message)


def main() -> int:
    ensure_project_root()
    try:
        validate_dependency_specs()
    except DependencySpecError as error:
        raise SystemExit(str(error)) from error
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
