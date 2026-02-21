#!/usr/bin/env bash
# Managed by standard-tooling — DO NOT EDIT in downstream repos.
# Canonical source: https://github.com/wphillipmoore/standard-tooling
set -euo pipefail

base_ref="${1:-}"
head_ref="${2:-}"

if [[ -z "$base_ref" || -z "$head_ref" ]]; then
  echo "ERROR: base and head refs are required." >&2
  echo "Usage: commit-messages.sh <base-ref> <head-ref>" >&2
  exit 2
fi

# Resolve bare branch names to origin/ when the local branch doesn't exist.
if ! git rev-parse --verify --quiet "$base_ref" >/dev/null 2>&1; then
  if git rev-parse --verify --quiet "origin/$base_ref" >/dev/null 2>&1; then
    base_ref="origin/$base_ref"
  fi
fi

conventional_regex='^(feat|fix|docs|style|refactor|test|chore|ci|build)(\([^\)]+\))?: .+'

# Commits at or before the cutoff SHA predate the conventional commits
# convention and are excluded from validation.  Consuming repos pass their
# own cutoff via the COMMIT_CUTOFF_SHA environment variable.
CUTOFF_SHA="${COMMIT_CUTOFF_SHA:-}"

failed=0

while IFS= read -r commit_sha; do
  # Skip commits that predate the conventional commits convention.
  if [[ -n "$CUTOFF_SHA" ]] && git merge-base --is-ancestor "$commit_sha" "$CUTOFF_SHA" 2>/dev/null; then
    continue
  fi
  subject_line="$(git log -n 1 --format=%s "$commit_sha")"
  if [[ ! "$subject_line" =~ $conventional_regex ]]; then
    echo "ERROR: commit $commit_sha does not follow Conventional Commits." >&2
    echo "Expected: <type>(optional-scope): <description>" >&2
    echo "Allowed types: feat, fix, docs, style, refactor, test, chore, ci, build" >&2
    echo "Got: $subject_line" >&2
    failed=1
  fi
  if [[ $failed -ne 0 ]]; then
    break
  fi
done < <(git rev-list --no-merges "${base_ref}..${head_ref}")

exit $failed
