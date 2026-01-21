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


def parse_requirement_name(requirement: str) -> str | None:
    """Extract the dependency name from a PEP 508 requirement string."""
    match = re.match(r"^[A-Za-z0-9_.-]+", requirement.strip())
    return match.group(0) if match else None


def parse_requirement_string(line: str) -> str | None:
    """Extract a requirement string from a TOML list line."""
    match = re.match(r"^\s*\"([^\"]+)\"", line)
    if match:
        return match.group(1)
    match = re.match(r"^\s*'([^']+)'", line)
    if match:
        return match.group(1)
    return None


def collect_dependency_lines(lines: list[str]) -> dict[tuple[str, str], int]:
    current_section: str | None = None
    dependency_lines: dict[tuple[str, str], int] = {}
    in_project_dependencies = False
    in_dependency_group: str | None = None

    section_pattern = re.compile(r"^\[(.+)]\s*$")

    for index, line in enumerate(lines):
        section_match = section_pattern.match(line.strip())
        if section_match:
            current_section = section_match.group(1)
            in_project_dependencies = False
            in_dependency_group = None
            continue

        if current_section == "project":
            if line.strip().startswith("dependencies = ["):
                in_project_dependencies = True
                continue
            if in_project_dependencies:
                if line.strip().startswith("]"):
                    in_project_dependencies = False
                    continue
                requirement = parse_requirement_string(line)
                if requirement:
                    name = parse_requirement_name(requirement)
                    if name:
                        dependency_lines[("project.dependencies", name)] = index
            continue

        if current_section == "dependency-groups":
            group_match = re.match(r"^\s*([A-Za-z0-9_.-]+)\s*=\s*\[", line)
            if group_match:
                in_dependency_group = group_match.group(1)
                continue
            if in_dependency_group:
                if line.strip().startswith("]"):
                    in_dependency_group = None
                    continue
                requirement = parse_requirement_string(line)
                if requirement:
                    name = parse_requirement_name(requirement)
                    if name:
                        dependency_lines[(f"dependency-groups.{in_dependency_group}", name)] = index
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
    project_section = pyproject.get("project")
    if not isinstance(project_section, dict):
        raise DependencySpecError("Missing [project] section in pyproject.toml.")

    dependencies_section = project_section.get("dependencies")
    if dependencies_section is None:
        raise DependencySpecError("Missing [project.dependencies] in pyproject.toml.")
    if not isinstance(dependencies_section, list):
        raise DependencySpecError("[project.dependencies] must be a list.")

    group_section = pyproject.get("dependency-groups", {})
    if not isinstance(group_section, dict):
        raise DependencySpecError("Invalid [dependency-groups] section in pyproject.toml.")

    lines = PYPROJECT_PATH.read_text().splitlines()
    dependency_lines = collect_dependency_lines(lines)
    errors: list[str] = []

    def requires_anchor(requirement: str) -> bool:
        return bool(re.search(r"[<>=!~]", requirement) or "@" in requirement or ";" in requirement)

    def validate_section(section_name: str, dependencies: list[str]) -> None:
        for requirement in sorted(dependencies):
            dependency_name = parse_requirement_name(requirement)
            if not dependency_name:
                errors.append(f"{section_name} has invalid requirement: {requirement}")
                continue

            if dependency_name == "python":
                continue

            if not requires_anchor(requirement):
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

    validate_section("project.dependencies", dependencies_section)

    for group_name, group_value in group_section.items():
        if not isinstance(group_value, list):
            errors.append(f"dependency-groups.{group_name} must be a list.")
            continue
        section_name = f"dependency-groups.{group_name}"
        validate_section(section_name, group_value)

    if errors:
        message = "Dependency specification validation failed:\n" + "\n".join(f"- {error}" for error in errors)
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
