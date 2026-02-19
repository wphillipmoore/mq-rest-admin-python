#!/usr/bin/env bash
set -euo pipefail

commit_message_file="${1:-}"

if [[ -z "$commit_message_file" || ! -f "$commit_message_file" ]]; then
  echo "ERROR: commit message file path is required." >&2
  exit 2
fi

subject_line="$(head -n 1 "$commit_message_file")"

conventional_regex='^(feat|fix|docs|style|refactor|test|chore|ci|build)(\([^\)]+\))?: .+'

if [[ ! "$subject_line" =~ $conventional_regex ]]; then
  echo "ERROR: commit message does not follow Conventional Commits." >&2
  echo "Expected: <type>(optional-scope): <description>" >&2
  echo "Allowed types: feat, fix, docs, style, refactor, test, chore, ci, build" >&2
  echo "Got: $subject_line" >&2
  exit 1
fi
