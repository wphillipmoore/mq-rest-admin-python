#!/usr/bin/env bash
# Managed by standard-tooling — DO NOT EDIT in downstream repos.
# Canonical source: https://github.com/wphillipmoore/standard-tooling
# validate_local_go.sh — Go-specific local validation checks.
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"

run() {
  echo "Running: $*"
  "$@"
}

# -- required tools ----------------------------------------------------------

missing=()
command -v go >/dev/null 2>&1 || missing+=("go")
command -v golangci-lint >/dev/null 2>&1 || missing+=("golangci-lint")
command -v gocyclo >/dev/null 2>&1 || missing+=("gocyclo")
command -v govulncheck >/dev/null 2>&1 || missing+=("govulncheck")
command -v go-licenses >/dev/null 2>&1 || missing+=("go-licenses")

if [[ ${#missing[@]} -gt 0 ]]; then
  echo "ERROR: required tools not found: ${missing[*]}" >&2
  exit 1
fi

# -- auto-discover module directory from go.mod ------------------------------

module_dir=""
if [[ -f "$repo_root/go.mod" ]]; then
  module_dir="$repo_root"
else
  # Search one level down for go.mod.
  while IFS= read -r f; do
    module_dir="$(dirname "$f")"
    break
  done < <(find "$repo_root" -maxdepth 2 -name go.mod -not -path '*/vendor/*' 2>/dev/null)
fi

if [[ -z "$module_dir" ]]; then
  echo "ERROR: could not find go.mod" >&2
  exit 1
fi

echo "Go module directory: $module_dir"
cd "$module_dir"

# -- vet ---------------------------------------------------------------------

run go vet ./...

# -- lint --------------------------------------------------------------------

run golangci-lint run ./...

# -- cyclomatic complexity ---------------------------------------------------

run gocyclo -over 15 .

# -- unit tests --------------------------------------------------------------

run go test -race -count=1 ./...

# -- coverage ----------------------------------------------------------------

if [[ -f "$module_dir/.testcoverage.yml" ]]; then
  if command -v go-test-coverage >/dev/null 2>&1; then
    run go-test-coverage --config .testcoverage.yml
  fi
fi

# -- vulnerability scan ------------------------------------------------------

run govulncheck ./...

# -- license compliance ------------------------------------------------------

allowlist_file="$module_dir/.go-licenses-allowlist"
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
    run go-licenses check ./... --allowed_licenses="$allow_list"
  fi
fi
