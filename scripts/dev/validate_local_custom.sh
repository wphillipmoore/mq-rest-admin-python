#!/usr/bin/env bash
# validate_local_custom.sh — mq-rest-admin-python repo-specific checks.
# This file is NOT synced from standard-tooling.
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"

run() {
  echo "Running: $*"
  "$@"
}

# -- resolve base ref for version validation ---------------------------------

base_ref=""
if git symbolic-ref --quiet refs/remotes/origin/HEAD >/dev/null 2>&1; then
  ref="$(git symbolic-ref --quiet refs/remotes/origin/HEAD)"
  base_ref="${ref##*/}"
fi

if [[ -z "$base_ref" ]]; then
  if git rev-parse --verify --quiet develop >/dev/null 2>&1 ||
     git rev-parse --verify --quiet origin/develop >/dev/null 2>&1; then
    base_ref="develop"
  fi
fi

if [[ -z "$base_ref" ]]; then
  echo "ERROR: could not resolve base ref for version validation" >&2
  exit 1
fi

# -- repo-specific validation scripts ---------------------------------------

run uv run python3 "$repo_root/scripts/dev/validate_venv.py"
run uv run python3 "$repo_root/scripts/dev/validate_dependency_specs.py"
run uv run python3 "$repo_root/scripts/dev/validate_version.py" --base-ref "$base_ref"

# -- type checking on examples/ (beyond what synced python script covers) ----

if [[ -d "$repo_root/examples" ]]; then
  run uv run mypy examples/
  if uv run ty --version >/dev/null 2>&1; then
    run uv run ty check examples
  fi
fi
