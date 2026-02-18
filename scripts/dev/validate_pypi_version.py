#!/usr/bin/env python3
"""Validate that the local version is publishable to PyPI."""

from __future__ import annotations

import argparse
import json
import re
import ssl
import tomllib
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Sequence

VERSION_PATTERN = re.compile(r"^(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)$")
PYPI_PROJECT_URL = "https://pypi.org/pypi/pymqrest/json"


@dataclass(frozen=True)
class Version:
    """Semantic version without a build component."""

    major: int
    minor: int
    patch: int

    def as_string(self) -> str:
        """Return the version formatted as MAJOR.MINOR.PATCH."""
        return f"{self.major}.{self.minor}.{self.patch}"

    def as_tuple(self) -> tuple[int, int, int]:
        """Return the version as a comparison tuple."""
        return (self.major, self.minor, self.patch)


def parse_version(version_value: str) -> Version:
    """Parse and validate a version string."""
    match = VERSION_PATTERN.match(version_value)
    if not match:
        message = f"Invalid version format: {version_value}"
        raise SystemExit(message)
    major, minor, patch = (int(match.group(index)) for index in range(1, 4))
    return Version(major=major, minor=minor, patch=patch)


def load_local_version() -> Version:
    """Load the version from the working tree pyproject.toml."""
    pyproject_path = Path("pyproject.toml")
    if not pyproject_path.is_file():
        message = "Run from the repository root (pyproject.toml missing)."
        raise SystemExit(message)
    data = tomllib.loads(pyproject_path.read_text(encoding="utf-8"))
    project_section = data.get("project")
    if not isinstance(project_section, dict):
        message = "Missing [project] section in pyproject.toml."
        raise SystemExit(message)
    version_value = project_section.get("version")
    if not isinstance(version_value, str):
        message = "Missing or invalid project.version in pyproject.toml."
        raise SystemExit(message)
    return parse_version(version_value)


def _build_ssl_context() -> ssl.SSLContext:
    """Build an SSL context, using certifi CA bundle if available."""
    try:
        import certifi  # type: ignore[import-untyped]  # noqa: PLC0415

        return ssl.create_default_context(cafile=certifi.where())
    except ImportError:
        return ssl.create_default_context()


def fetch_pypi_versions() -> list[Version] | None:
    """Fetch all released versions from PyPI.

    Returns None if the package does not exist on PyPI (404).
    """
    context = _build_ssl_context()
    request = urllib.request.Request(PYPI_PROJECT_URL, headers={"Accept": "application/json"})  # noqa: S310
    try:
        with urllib.request.urlopen(request, timeout=30, context=context) as response:  # noqa: S310
            data = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        if exc.code == 404:  # noqa: PLR2004
            return None
        raise
    releases = data.get("releases", {})
    versions: list[Version] = []
    for version_string in releases:
        match = VERSION_PATTERN.match(version_string)
        if match:
            major, minor, patch = (int(match.group(index)) for index in range(1, 4))
            versions.append(Version(major=major, minor=minor, patch=patch))
    return versions


def check_not_exists(local: Version, pypi_versions: list[Version] | None) -> bool:
    """Verify the local version is not already published on PyPI."""
    if pypi_versions is None:
        print(f"Package not found on PyPI; version {local.as_string()} is available.")
        return True
    for published in pypi_versions:
        if published.as_tuple() == local.as_tuple():
            print(f"FAIL: Version {local.as_string()} already exists on PyPI.")
            return False
    print(f"OK: Version {local.as_string()} is not yet on PyPI.")
    return True


def check_greater_than_latest(local: Version, pypi_versions: list[Version] | None) -> bool:
    """Verify the local version is greater than the latest on PyPI."""
    if pypi_versions is None:
        print(f"Package not found on PyPI; version {local.as_string()} is the first release.")
        return True
    if not pypi_versions:
        print(f"No valid releases on PyPI; version {local.as_string()} is the first release.")
        return True
    latest = max(pypi_versions, key=lambda v: v.as_tuple())
    if local.as_tuple() > latest.as_tuple():
        print(f"OK: Version {local.as_string()} > latest PyPI version {latest.as_string()}.")
        return True
    print(f"FAIL: Version {local.as_string()} is not greater than latest PyPI version {latest.as_string()}.")
    return False


def parse_arguments(argument_list: Sequence[str] | None = None) -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Validate that the local version is publishable to PyPI.",
    )
    parser.add_argument(
        "--check-not-exists",
        action="store_true",
        help="Verify the local version is not already on PyPI.",
    )
    parser.add_argument(
        "--check-greater-than-latest",
        action="store_true",
        help="Verify the local version is greater than the latest on PyPI.",
    )
    return parser.parse_args(list(argument_list) if argument_list is not None else None)


def main() -> int:
    arguments = parse_arguments()
    if not arguments.check_not_exists and not arguments.check_greater_than_latest:
        print("No check mode specified. Use --check-not-exists and/or --check-greater-than-latest.")
        return 1

    local_version = load_local_version()
    pypi_versions = fetch_pypi_versions()

    passed = True
    if arguments.check_not_exists and not check_not_exists(local_version, pypi_versions):
        passed = False
    if arguments.check_greater_than_latest and not check_greater_than_latest(local_version, pypi_versions):
        passed = False

    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
