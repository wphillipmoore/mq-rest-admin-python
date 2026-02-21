#!/usr/bin/env bash
# Managed by standard-tooling — DO NOT EDIT in downstream repos.
# Canonical source: https://github.com/wphillipmoore/standard-tooling
# validate_local_java.sh — Java-specific local validation checks.
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"

run() {
  echo "Running: $*"
  "$@"
}

# -- required tools ----------------------------------------------------------

if ! command -v java >/dev/null 2>&1; then
  echo "ERROR: required tool not found: java" >&2
  exit 1
fi

if [[ ! -x "$repo_root/mvnw" ]]; then
  echo "ERROR: Maven wrapper (mvnw) not found or not executable at $repo_root/mvnw" >&2
  exit 1
fi

# -- build + test ------------------------------------------------------------

run "$repo_root/mvnw" verify -B

# -- license compliance ------------------------------------------------------

allowlist_file="$repo_root/.mvn-licenses-allowlist"
if [[ -f "$allowlist_file" ]]; then
  allow_list=""
  while IFS= read -r line; do
    [[ -z "$line" || "$line" =~ ^# ]] && continue
    if [[ -n "$allow_list" ]]; then
      allow_list="$allow_list,$line"
    else
      allow_list="$line"
    fi
  done < "$allowlist_file"

  if [[ -n "$allow_list" ]]; then
    run "$repo_root/mvnw" license:add-third-party \
      -Dlicense.excludedScopes=test \
      -Dlicense.failIfWarning=true \
      "-Dlicense.includedLicenses=$allow_list" \
      -B
  fi
fi
