#!/usr/bin/env bash
set -euo pipefail

commit_message_file="${1:-}"

if [[ -z "$commit_message_file" || ! -f "$commit_message_file" ]]; then
  echo "ERROR: commit message file path is required." >&2
  exit 2
fi

# Extract Co-Authored-By trailers from the commit message (case-insensitive match).
trailers=()
while IFS= read -r line; do
  trailers+=("$line")
done < <(grep -i '^Co-Authored-By:' "$commit_message_file" || true)

# Human-only commits (no trailers) are valid.
if [[ ${#trailers[@]} -eq 0 ]]; then
  exit 0
fi

# Read approved identities from the repository profile.
repo_root="$(git rev-parse --show-toplevel)"
profile_file="$repo_root/docs/repository-standards.md"

if [[ ! -f "$profile_file" ]]; then
  echo "ERROR: repository profile not found at $profile_file; cannot validate co-author trailers." >&2
  exit 1
fi

approved=()
while IFS= read -r line; do
  approved+=("$line")
done < <(grep -i '^\- Co-Authored-By:' "$profile_file" | sed 's/^- //' || true)

if [[ ${#approved[@]} -eq 0 ]]; then
  echo "ERROR: no approved co-author identities found in $profile_file." >&2
  exit 1
fi

# Validate each trailer against the approved list.
failed=0
for trailer in "${trailers[@]}"; do
  # Normalize whitespace for comparison.
  normalized="$(echo "$trailer" | sed 's/[[:space:]][[:space:]]*/ /g; s/^ //; s/ $//')"
  match=0
  for identity in "${approved[@]}"; do
    normalized_identity="$(echo "$identity" | sed 's/[[:space:]][[:space:]]*/ /g; s/^ //; s/ $//')"
    if [[ "$normalized" == "$normalized_identity" ]]; then
      match=1
      break
    fi
  done
  if [[ $match -eq 0 ]]; then
    echo "ERROR: unapproved co-author trailer: $trailer" >&2
    echo "Approved identities are listed in $profile_file under 'AI co-authors'." >&2
    failed=1
  fi
done

exit $failed
