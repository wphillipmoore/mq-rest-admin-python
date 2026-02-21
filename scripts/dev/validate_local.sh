#!/usr/bin/env bash
# Managed by standard-tooling — DO NOT EDIT in downstream repos.
# Canonical source: https://github.com/wphillipmoore/standard-tooling
# validate_local.sh — shared driver for pre-PR local validation.
#
# Reads primary_language from docs/repository-standards.md, then runs:
#   1. validate_local_common.sh   (always)
#   2. validate_local_<lang>.sh   (if primary_language is set and script exists)
#   3. validate_local_custom.sh   (if exists — repo-specific escape hatch)
set -euo pipefail

scripts_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(cd "$scripts_dir/../.." && pwd)"
profile_file="$repo_root/docs/repository-standards.md"

# -- helpers -----------------------------------------------------------------

run() {
  echo "Running: $*"
  "$@"
}

# -- read primary_language from repo profile ---------------------------------

primary_language=""
if [[ -f "$profile_file" ]]; then
  while IFS= read -r line; do
    if [[ "$line" =~ ^[[:space:]-]*primary_language:[[:space:]]*(.+)$ ]]; then
      primary_language="${BASH_REMATCH[1]}"
      break
    fi
  done < "$profile_file"
fi

echo "========================================"
echo "validate_local.sh"
echo "primary_language: ${primary_language:-<not set>}"
echo "========================================"
echo ""

# -- common checks (always) -------------------------------------------------

common_script="$scripts_dir/validate_local_common.sh"
if [[ -f "$common_script" ]]; then
  run "$common_script"
else
  echo "WARNING: $common_script not found; skipping common checks" >&2
fi

# -- language-specific checks ------------------------------------------------

if [[ -n "$primary_language" && "$primary_language" != "none" ]]; then
  lang_script="$scripts_dir/validate_local_${primary_language}.sh"
  if [[ -f "$lang_script" ]]; then
    echo ""
    run "$lang_script"
  fi
fi

# -- repo-specific custom checks --------------------------------------------

custom_script="$scripts_dir/validate_local_custom.sh"
if [[ -f "$custom_script" ]]; then
  echo ""
  run "$custom_script"
fi

echo ""
echo "========================================"
echo "validate_local.sh: all checks passed"
echo "========================================"
