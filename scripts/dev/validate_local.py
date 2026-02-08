#!/usr/bin/env python3
"""Local validation helper mirroring CI hard gates."""

from __future__ import annotations

import argparse
import subprocess
from pathlib import Path


def parse_arguments() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Run local validation matching CI hard gates.")
    parser.add_argument(
        "--base-ref",
        default=None,
        help="Base branch for version validation (defaults to origin/HEAD).",
    )
    return parser.parse_args()


def ensure_project_root() -> None:
    """Fail fast if invoked outside the repository root."""
    if not Path("pyproject.toml").is_file():
        message = "Run from the repository root (pyproject.toml missing)."
        raise SystemExit(message)


def read_command_output(command: tuple[str, ...]) -> str:
    """Run a command and return its stdout."""
    result = subprocess.run(command, check=True, text=True, capture_output=True)  # noqa: S603
    return result.stdout.strip()


def resolve_default_base_ref() -> str | None:
    """Resolve the default base ref from origin/HEAD."""
    try:
        reference = read_command_output(("git", "symbolic-ref", "--quiet", "refs/remotes/origin/HEAD"))
    except subprocess.CalledProcessError:
        return None
    return reference.rsplit("/", maxsplit=1)[-1] if reference else None


def git_reference_exists(reference: str) -> bool:
    """Return True if the git reference exists."""
    return (
        subprocess.run(("git", "rev-parse", "--verify", "--quiet", reference), check=False).returncode == 0  # noqa: S603
    )


def resolve_fallback_base_ref() -> str | None:
    """Fallback to develop when origin/HEAD is missing or stale."""
    if git_reference_exists("develop") or git_reference_exists("origin/develop"):
        return "develop"
    return None


def build_commands(base_ref: str) -> tuple[tuple[str, ...], ...]:
    """Build validation commands matching CI hard gates."""
    commands: list[tuple[str, ...]] = [
        ("uv", "run", "python3", "scripts/dev/validate_venv.py"),
        ("uv", "run", "python3", "scripts/dev/validate_dependency_specs.py"),
        ("uv", "run", "python3", "scripts/dev/validate_version.py", "--base-ref", base_ref),
        ("bash", "scripts/lint/repo-profile.sh"),
        ("bash", "scripts/lint/markdown-standards.sh"),
        ("bash", "scripts/lint/commit-messages.sh", base_ref, "HEAD"),
        ("uv", "lock", "--check"),
        ("uv", "sync", "--check", "--frozen", "--group", "dev"),
        ("uv", "run", "pip-audit", "-r", "requirements.txt", "-r", "requirements-dev.txt"),
        ("uv", "run", "ruff", "check"),
        ("uv", "run", "ruff", "format", "--check", "."),
        ("uv", "run", "mypy", "src/"),
        ("uv", "run", "ty", "check", "src"),
        (
            "uv",
            "run",
            "pytest",
            "--cov=pymqrest",
            "--cov-report=term-missing",
            "--cov-branch",
            "--cov-fail-under=100",
        ),
    ]
    return tuple(commands)


def run_command(command: tuple[str, ...]) -> int:
    """Run a command and return its exit code."""
    return subprocess.run(command, check=False).returncode  # noqa: S603


def main() -> int:
    arguments = parse_arguments()
    ensure_project_root()

    base_ref = arguments.base_ref or resolve_default_base_ref()
    if not base_ref:
        base_ref = resolve_fallback_base_ref()
    if base_ref and not git_reference_exists(base_ref) and not git_reference_exists(f"origin/{base_ref}"):
        base_ref = resolve_fallback_base_ref()
    if not base_ref:
        message = "Base ref required for version validation. Pass --base-ref or ensure refs/remotes/origin/HEAD exists."
        raise SystemExit(message)

    for command in build_commands(base_ref):
        print(f"Running: {' '.join(command)}")
        exit_code = run_command(command)
        if exit_code != 0:
            return exit_code

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
