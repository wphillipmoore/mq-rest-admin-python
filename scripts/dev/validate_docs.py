#!/usr/bin/env python3
"""Docs-only validation helper."""

from __future__ import annotations

import argparse
import shutil
import subprocess
from pathlib import Path


def parse_arguments() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Run docs-only validation.")
    parser.add_argument(
        "--paths",
        nargs="*",
        default=None,
        help="Optional list of markdown files to validate.",
    )
    return parser.parse_args()


def ensure_project_root() -> None:
    """Fail fast if invoked outside the repository root."""
    if not Path("pyproject.toml").is_file():
        message = "Run from the repository root (pyproject.toml missing)."
        raise SystemExit(message)


def gather_default_paths() -> list[str]:
    """Collect default markdown files for docs-only validation."""
    candidates: list[Path] = []
    docs_root = Path("docs")
    if docs_root.exists():
        candidates.extend(docs_root.rglob("*.md"))

    for filename in ("README.md", "CHANGELOG.md"):
        path = Path(filename)
        if path.is_file():
            candidates.append(path)

    unique_paths = sorted(set(candidates))
    return [str(path) for path in unique_paths]


def resolve_markdownlint() -> str:
    """Resolve markdownlint binary."""
    markdownlint = shutil.which("markdownlint")
    if markdownlint:
        return markdownlint

    message = (
        "markdownlint is required for docs-only validation. Install markdownlint-cli and ensure it is on your PATH."
    )
    raise SystemExit(message)


def run_markdownlint(paths: list[str]) -> int:
    """Run markdownlint using the resolved toolchain."""
    markdownlint_cmd = resolve_markdownlint()

    if not paths:
        print("No markdown files found to validate.")
        return 0

    command = (markdownlint_cmd, *paths)
    print(f"Running: {' '.join(command)}")
    return subprocess.run(command, check=False).returncode  # noqa: S603


def main() -> int:
    arguments = parse_arguments()
    ensure_project_root()

    paths = arguments.paths or gather_default_paths()
    return run_markdownlint(paths)


if __name__ == "__main__":
    raise SystemExit(main())
