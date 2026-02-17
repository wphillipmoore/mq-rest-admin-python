#!/usr/bin/env bash
set -euo pipefail

if [[ -z "${GITHUB_EVENT_PATH:-}" ]]; then
  echo "ERROR: GITHUB_EVENT_PATH is not set." >&2
  exit 2
fi

if [[ ! -f "$GITHUB_EVENT_PATH" ]]; then
  echo "ERROR: event payload not found at $GITHUB_EVENT_PATH" >&2
  exit 2
fi

pr_body="$(jq -r '.pull_request.body // ""' "$GITHUB_EVENT_PATH")"

if [[ -z "$pr_body" ]]; then
  echo "ERROR: pull request body is empty; issue linkage is required." >&2
  exit 1
fi

if ! printf '%s\n' "$pr_body" | grep -Eq '^[[:space:]]*[-*]?[[:space:]]*(Fixes|Closes|Resolves|Ref):?[[:space:]]+#[0-9]+'; then
  echo "ERROR: pull request body must include primary issue linkage (Fixes #123, Closes #123, Resolves #123, or Ref #123)." >&2
  exit 1
fi
