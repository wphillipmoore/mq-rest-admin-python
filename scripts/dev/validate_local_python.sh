#!/usr/bin/env bash
# Managed by standard-tooling — DO NOT EDIT in downstream repos.
# Canonical source: https://github.com/wphillipmoore/standard-tooling
# validate_local_python.sh — Python-specific local validation checks.
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"

run() {
  echo "Running: $*"
  "$@"
}

# -- required tools ----------------------------------------------------------

if ! command -v uv >/dev/null 2>&1; then
  echo "ERROR: required tool not found: uv" >&2
  exit 1
fi

# -- auto-discover package name from pyproject.toml --------------------------

pkg_name=""
if [[ -f "$repo_root/pyproject.toml" ]]; then
  while IFS= read -r line; do
    if [[ "$line" =~ ^name[[:space:]]*=[[:space:]]*\"([^\"]+)\" ]]; then
      pkg_name="${BASH_REMATCH[1]}"
      # Convert hyphens to underscores for Python import name.
      pkg_name="${pkg_name//-/_}"
      break
    fi
  done < "$repo_root/pyproject.toml"
fi

if [[ -z "$pkg_name" ]]; then
  echo "ERROR: could not discover package name from pyproject.toml" >&2
  exit 1
fi

echo "Python package: $pkg_name"

# -- lock integrity ----------------------------------------------------------

run uv lock --check

# -- sync check --------------------------------------------------------------

run uv sync --check --frozen --group dev

# -- vulnerability scan ------------------------------------------------------

req_files=()
for f in requirements.txt requirements-dev.txt; do
  if [[ -f "$repo_root/$f" ]]; then
    req_files+=(-r "$f")
  fi
done

if [[ ${#req_files[@]} -gt 0 ]]; then
  run uv run pip-audit "${req_files[@]}"
fi

# -- license compliance ------------------------------------------------------

allowlist_file="$repo_root/.pip-licenses-allowlist"
if [[ -f "$allowlist_file" ]]; then
  allow_list=""
  while IFS= read -r line; do
    # Skip blank lines and comments.
    [[ -z "$line" || "$line" =~ ^# ]] && continue
    if [[ -n "$allow_list" ]]; then
      allow_list="$allow_list;$line"
    else
      allow_list="$line"
    fi
  done < "$allowlist_file"

  if [[ -n "$allow_list" ]]; then
    run uv run pip-licenses --allow-only="$allow_list"
  fi
fi

# -- linting -----------------------------------------------------------------

run uv run ruff check

# -- formatting --------------------------------------------------------------

run uv run ruff format --check .

# -- type checking (mypy) ----------------------------------------------------

if [[ -d "$repo_root/src" ]]; then
  run uv run mypy src/
fi

# -- type checking (ty) ------------------------------------------------------

if uv run ty --version >/dev/null 2>&1; then
  if [[ -d "$repo_root/src" ]]; then
    run uv run ty check src
  fi
fi

# -- unit tests + coverage ---------------------------------------------------

run uv run pytest --cov="$pkg_name" --cov-branch --cov-fail-under=100
