#!/usr/bin/env bash
# Canonical source: standard-tooling
# validate_local_common.sh — shared checks run for ALL repos.
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"

run() {
  echo "Running: $*"
  "$@"
}

# -- required tools ----------------------------------------------------------

missing=()
command -v shellcheck >/dev/null 2>&1 || missing+=("shellcheck")
command -v markdownlint >/dev/null 2>&1 || missing+=("markdownlint")

if [[ ${#missing[@]} -gt 0 ]]; then
  echo "ERROR: required tools not found: ${missing[*]}" >&2
  exit 1
fi

# -- repo profile validation -------------------------------------------------

if [[ -f "$repo_root/scripts/lint/repo-profile.sh" ]]; then
  run "$repo_root/scripts/lint/repo-profile.sh"
fi

# -- markdown lint -----------------------------------------------------------

if [[ -f "$repo_root/scripts/lint/markdown-standards.sh" ]]; then
  run "$repo_root/scripts/lint/markdown-standards.sh"
fi

# -- shellcheck on all shell scripts -----------------------------------------

shell_files=()
while IFS= read -r f; do
  shell_files+=("$f")
done < <(
  find "$repo_root/scripts" -type f -name '*.sh' 2>/dev/null
  find "$repo_root/scripts/git-hooks" -type f 2>/dev/null
)

if [[ ${#shell_files[@]} -gt 0 ]]; then
  run shellcheck "${shell_files[@]}"
fi
