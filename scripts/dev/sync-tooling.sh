#!/usr/bin/env bash
set -euo pipefail

# sync-tooling.sh — keep local copies of shared scripts in sync with
# the canonical versions in the standard-tooling repository.
#
# Usage:
#   sync-tooling.sh [--check | --fix] [--ref TAG] [--actions-compat]
#
# --check           Compare local copies against standard-tooling (default)
# --fix             Overwrite local copies with canonical versions
# --ref TAG         Standard-tooling tag to sync to (default: latest tag)
# --actions-compat  Also sync lint scripts to actions/standards-compliance/scripts/

TOOLING_REPO="https://github.com/wphillipmoore/standard-tooling.git"

# Managed files — paths relative to the repo root.
MANAGED_FILES=(
  scripts/git-hooks/commit-msg
  scripts/git-hooks/pre-commit
  scripts/lint/co-author.sh
  scripts/lint/commit-message.sh
  scripts/lint/commit-messages.sh
  scripts/lint/markdown-standards.sh
  scripts/lint/pr-issue-linkage.sh
  scripts/lint/repo-profile.sh
  scripts/dev/commit.sh
  scripts/dev/submit-pr.sh
  scripts/dev/prepare_release.py
  scripts/dev/finalize_repo.sh
  scripts/dev/sync-tooling.sh
  scripts/dev/validate_local.sh
  scripts/dev/validate_local_common.sh
  scripts/dev/validate_local_python.sh
  scripts/dev/validate_local_go.sh
  scripts/dev/validate_local_java.sh
)

# Lint scripts that also get copied to the actions path.
ACTIONS_LINT_FILES=(
  scripts/lint/commit-messages.sh
  scripts/lint/markdown-standards.sh
  scripts/lint/pr-issue-linkage.sh
  scripts/lint/repo-profile.sh
)
ACTIONS_SCRIPTS_DIR="actions/standards-compliance/scripts"

# -- argument parsing --------------------------------------------------------

mode="check"
ref=""
actions_compat=""

usage() {
  cat <<EOF
Usage: $(basename "$0") [OPTIONS]

Keep local copies of shared scripts in sync with standard-tooling.

Options:
  --check           Compare local copies (default)
  --fix             Overwrite local copies with canonical versions
  --ref TAG         Standard-tooling tag to sync to (default: latest tag)
  --actions-compat  Also sync lint scripts to actions/standards-compliance/scripts/
  -h, --help        Show this help message
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --check)
      mode="check"
      shift
      ;;
    --fix)
      mode="fix"
      shift
      ;;
    --ref)
      ref="$2"
      shift 2
      ;;
    --actions-compat)
      actions_compat=true
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "ERROR: unknown option '$1'" >&2
      usage >&2
      exit 1
      ;;
  esac
done

# -- resolve repo root -------------------------------------------------------

repo_root="$(git rev-parse --show-toplevel)"

# -- clone canonical source ---------------------------------------------------

tmpdir="$(mktemp -d)"
trap 'rm -rf "$tmpdir"' EXIT

if [[ -n "$ref" ]]; then
  clone_ref="$ref"
else
  # Discover the latest tag without a full clone.
  clone_ref="$(git ls-remote --tags --sort=-v:refname "$TOOLING_REPO" 'v*' \
    | head -n 1 | sed 's|.*refs/tags/||')"
  if [[ -z "$clone_ref" ]]; then
    echo "ERROR: no tags found in $TOOLING_REPO" >&2
    exit 1
  fi
fi

echo "Syncing against standard-tooling @ $clone_ref"
git clone --depth 1 --branch "$clone_ref" "$TOOLING_REPO" "$tmpdir/standard-tooling" 2>/dev/null

canonical="$tmpdir/standard-tooling"

# -- self-update check -------------------------------------------------------

self_path="scripts/dev/sync-tooling.sh"
self_local="$repo_root/$self_path"
self_canonical="$canonical/$self_path"

if [[ -f "$self_canonical" && -f "$self_local" ]]; then
  if ! diff -q "$self_local" "$self_canonical" >/dev/null 2>&1; then
    if [[ "$mode" == "fix" ]]; then
      echo "Updating sync-tooling.sh itself and re-executing..."
      cp "$self_canonical" "$self_local"
      chmod +x "$self_local"
      # Re-exec with the same arguments.
      exec "$self_local" --fix ${ref:+--ref "$ref"} ${actions_compat:+--actions-compat}
    else
      echo "STALE: $self_path"
    fi
  fi
fi

# -- compare / fix -----------------------------------------------------------

stale=0

for file in "${MANAGED_FILES[@]}"; do
  local_file="$repo_root/$file"
  canonical_file="$canonical/$file"

  # Skip files that don't exist in canonical (repo-specific scripts).
  if [[ ! -f "$canonical_file" ]]; then
    continue
  fi

  if [[ ! -f "$local_file" ]]; then
    if [[ "$mode" == "fix" ]]; then
      echo "ADDING: $file"
      mkdir -p "$(dirname "$local_file")"
      cp "$canonical_file" "$local_file"
      chmod --reference="$canonical_file" "$local_file" 2>/dev/null || chmod +x "$local_file"
    else
      echo "MISSING: $file"
      stale=1
    fi
    continue
  fi

  if ! diff -q "$local_file" "$canonical_file" >/dev/null 2>&1; then
    if [[ "$mode" == "fix" ]]; then
      echo "UPDATING: $file"
      cp "$canonical_file" "$local_file"
      chmod --reference="$canonical_file" "$local_file" 2>/dev/null || chmod +x "$local_file"
    else
      echo "STALE: $file"
      stale=1
    fi
  fi
done

# -- actions compat ----------------------------------------------------------

if [[ "$actions_compat" == true ]]; then
  for file in "${ACTIONS_LINT_FILES[@]}"; do
    basename="$(basename "$file")"
    local_file="$repo_root/$ACTIONS_SCRIPTS_DIR/$basename"
    canonical_file="$canonical/$file"

    if [[ ! -f "$canonical_file" ]]; then
      continue
    fi

    if [[ ! -f "$local_file" ]]; then
      if [[ "$mode" == "fix" ]]; then
        echo "ADDING (actions): $ACTIONS_SCRIPTS_DIR/$basename"
        mkdir -p "$(dirname "$local_file")"
        cp "$canonical_file" "$local_file"
        chmod --reference="$canonical_file" "$local_file" 2>/dev/null || chmod +x "$local_file"
      else
        echo "MISSING (actions): $ACTIONS_SCRIPTS_DIR/$basename"
        stale=1
      fi
      continue
    fi

    if ! diff -q "$local_file" "$canonical_file" >/dev/null 2>&1; then
      if [[ "$mode" == "fix" ]]; then
        echo "UPDATING (actions): $ACTIONS_SCRIPTS_DIR/$basename"
        cp "$canonical_file" "$local_file"
        chmod --reference="$canonical_file" "$local_file" 2>/dev/null || chmod +x "$local_file"
      else
        echo "STALE (actions): $ACTIONS_SCRIPTS_DIR/$basename"
        stale=1
      fi
    fi
  done
fi

# -- result ------------------------------------------------------------------

if [[ "$mode" == "check" ]]; then
  if [[ $stale -ne 0 ]]; then
    echo ""
    echo "Shared scripts are stale. Run 'scripts/dev/sync-tooling.sh --fix' to update."
    exit 1
  else
    echo "All shared scripts are up to date."
  fi
else
  echo "Sync complete."
fi
