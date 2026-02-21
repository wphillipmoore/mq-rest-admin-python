#!/usr/bin/env python3
# Managed by standard-tooling — DO NOT EDIT in downstream repos.
# Canonical source: https://github.com/wphillipmoore/standard-tooling
"""Automate release preparation: branch, changelog, PR, auto-merge.

Shared script for library repositories using the library-release branching
model. Auto-detects the ecosystem to find the version source of truth.

Supported ecosystems:
  - Python: reads version from pyproject.toml
  - Maven:  reads version from pom.xml
  - Go:     reads version from **/version.go
  - VERSION file: reads version from VERSION (fallback)

Usage:
  scripts/dev/prepare_release.py --issue 42
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

# -- helpers -----------------------------------------------------------------


def read_command_output(command: tuple[str, ...]) -> str:
    """Run a command and return its stdout."""
    result = subprocess.run(command, check=True, text=True, capture_output=True)  # noqa: S603
    return result.stdout.strip()


def run_command(command: tuple[str, ...]) -> None:
    """Run a command and raise on failure."""
    subprocess.run(command, check=True)  # noqa: S603


def ensure_tool_available(name: str) -> None:
    """Fail if a required tool is not on PATH."""
    if not shutil.which(name):
        message = f"Required tool '{name}' not found on PATH."
        raise SystemExit(message)


# -- ecosystem detection -----------------------------------------------------


def detect_python() -> str | None:
    """Return the version if pyproject.toml declares one."""
    path = Path("pyproject.toml")
    if not path.is_file():
        return None
    text = path.read_text(encoding="utf-8")
    match = re.search(r'^version\s*=\s*"([^"]+)"', text, re.MULTILINE)
    if not match:
        return None
    return match.group(1)


def detect_maven() -> str | None:
    """Return the version from pom.xml."""
    path = Path("pom.xml")
    if not path.is_file():
        return None
    text = path.read_text(encoding="utf-8")
    match = re.search(
        r"<artifactId>[^<]+</artifactId>\s*<version>([^<]+)</version>",
        text,
    )
    if not match:
        return None
    return match.group(1)


def detect_go() -> str | None:
    """Return the version from **/version.go."""
    if not Path("go.mod").is_file():
        return None
    for path in Path().rglob("version.go"):
        text = path.read_text(encoding="utf-8")
        match = re.search(r'(?:const\s+)?Version\s*=\s*"([^"]+)"', text)
        if match:
            return match.group(1)
    return None


def detect_version_file() -> str | None:
    """Return the version from a VERSION file at the repo root (fallback)."""
    path = Path("VERSION")
    if not path.is_file():
        return None
    version = path.read_text(encoding="utf-8").strip()
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        message = (
            f"VERSION file contains '{version}' which is not valid semver.\n"
            f"Expected format: MAJOR.MINOR.PATCH (e.g. 1.2.3)"
        )
        raise SystemExit(message)
    return version


DETECTORS = [
    ("python", detect_python),
    ("maven", detect_maven),
    ("go", detect_go),
    ("version-file", detect_version_file),
]


def detect_ecosystem() -> tuple[str, str]:
    """Return (ecosystem_name, version) or fail."""
    for name, detector in DETECTORS:
        version = detector()
        if version is not None:
            return name, version
    message = (
        "Could not detect ecosystem. Expected one of:\n"
        "  - pyproject.toml with version (Python)\n"
        "  - pom.xml with version (Maven)\n"
        "  - go.mod + **/version.go (Go)\n"
        "  - VERSION file with MAJOR.MINOR.PATCH"
    )
    raise SystemExit(message)


# -- precondition checks ----------------------------------------------------


def ensure_on_develop() -> None:
    """Fail if not on the develop branch."""
    branch = read_command_output(("git", "rev-parse", "--abbrev-ref", "HEAD"))
    if branch != "develop":
        message = f"Must be on develop branch (currently on '{branch}')."
        raise SystemExit(message)


def ensure_clean_tree() -> None:
    """Fail if the working tree has uncommitted changes."""
    status = read_command_output(("git", "status", "--porcelain"))
    if status:
        message = "Working tree is not clean. Commit or stash changes first."
        raise SystemExit(message)


def ensure_develop_up_to_date() -> None:
    """Fail if local develop is behind origin/develop."""
    run_command(("git", "fetch", "origin", "develop"))
    local_sha = read_command_output(("git", "rev-parse", "HEAD"))
    remote_sha = read_command_output(("git", "rev-parse", "origin/develop"))
    if local_sha != remote_sha:
        message = (
            f"Local develop ({local_sha[:8]}) does not match "
            f"origin/develop ({remote_sha[:8]}). "
            f"Pull latest changes before preparing a release."
        )
        raise SystemExit(message)


def branch_exists(name: str) -> bool:
    """Return True if a branch exists locally or on origin."""
    for ref in (name, f"origin/{name}"):
        result = subprocess.run(  # noqa: S603
            ("git", "rev-parse", "--verify", "--quiet", ref),
            check=False,
        )
        if result.returncode == 0:
            return True
    return False


# -- release steps -----------------------------------------------------------


def create_release_branch(branch: str) -> None:
    """Create a release branch from the current develop HEAD."""
    if branch_exists(branch):
        message = f"Release branch '{branch}' already exists."
        raise SystemExit(message)
    print(f"Creating branch: {branch} (from develop)")
    run_command(("git", "checkout", "-b", branch))


def merge_main(version: str) -> None:
    """Merge main into the release branch to incorporate prior release history.

    This prevents CHANGELOG.md merge conflicts by ensuring the release branch
    has main's version of the changelog before git-cliff regenerates it.
    Uses a conventional commit message to satisfy commit-msg hooks.
    Uses ``-X ours`` to auto-resolve conflicts (only CHANGELOG.md should
    conflict, and git-cliff regenerates it in the next step).
    """
    print("Merging main into release branch...")
    run_command(("git", "fetch", "origin", "main"))
    run_command(
        (
            "git",
            "merge",
            "origin/main",
            "-X",
            "ours",
            "-m",
            f"chore: merge main into release/{version}",
        )
    )


def generate_changelog(version: str) -> bool:
    """Generate changelog via git-cliff. Return True if generated."""
    for tool in ("git-cliff", "markdownlint"):
        if not shutil.which(tool):
            raise SystemExit(f"Required tool '{tool}' not found. Install it before releasing.")
    tag = f"develop-v{version}"
    print(f"Generating changelog with boundary tag: {tag}")
    run_command(("git-cliff", "--tag", tag, "-o", "CHANGELOG.md"))
    changelog = Path("CHANGELOG.md")
    changelog.write_text(
        changelog.read_text(encoding="utf-8").rstrip() + "\n",
        encoding="utf-8",
    )
    result = subprocess.run(
        ("markdownlint", "CHANGELOG.md"),
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(result.stdout)
        print(result.stderr)
        raise SystemExit(
            "CHANGELOG.md failed markdownlint validation. "
            "Fix cliff.toml template or CHANGELOG content before releasing."
        )
    run_command(("git", "add", "CHANGELOG.md"))
    status = read_command_output(("git", "status", "--porcelain"))
    if not status:
        message = (
            f"No publishable changes since the last release.\n"
            f"All commits after develop-v{version} are filtered by git-cliff.\n"
            f"Aborting release preparation."
        )
        raise SystemExit(message)
    run_command(("git", "commit", "-m", f"chore: prepare release {version}"))
    return True


def push_branch(branch: str) -> None:
    """Push the release branch to origin."""
    print(f"Pushing branch: {branch}")
    run_command(("git", "push", "-u", "origin", branch))


def create_pr(version: str, issue: int) -> str:
    """Create a PR to main and return the PR URL."""
    print("Creating pull request to main...")
    title = f"release: {version}"
    body = f"## Summary\n\nRelease {version}\n\nRef #{issue}\n\nGenerated with `prepare_release.py`\n"
    result = subprocess.run(  # noqa: S603
        (
            "gh",
            "pr",
            "create",
            "--base",
            "main",
            "--title",
            title,
            "--body",
            body,
        ),
        check=True,
        text=True,
        capture_output=True,
    )
    url = result.stdout.strip()
    print(f"PR created: {url}")
    return url


def enable_auto_merge(url: str) -> None:
    """Enable auto-merge on the PR (regular merge, not squash)."""
    print("Enabling auto-merge...")
    run_command(("gh", "pr", "merge", url, "--auto", "--merge", "--delete-branch"))


# -- main --------------------------------------------------------------------


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Prepare a release.")
    parser.add_argument(
        "--issue",
        type=int,
        required=True,
        help="GitHub issue number for release tracking (used for PR linkage).",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    ensure_on_develop()
    ensure_clean_tree()
    ensure_develop_up_to_date()
    ensure_tool_available("gh")

    ecosystem, version = detect_ecosystem()
    branch = f"release/{version}"

    print(f"Preparing release {version} ({ecosystem})")

    create_release_branch(branch)
    merge_main(version)
    generate_changelog(version)
    push_branch(branch)
    url = create_pr(version, args.issue)
    enable_auto_merge(url)

    run_command(("git", "checkout", "develop"))

    print(f"Release {version} preparation complete.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
