#!/usr/bin/env bash
# Managed by standard-tooling — DO NOT EDIT in downstream repos.
# Canonical source: https://github.com/wphillipmoore/standard-tooling
# shellcheck disable=SC2034
# Variables are read via indirect expansion (${!key}).
set -euo pipefail

profile_file="docs/repository-standards.md"

if [[ ! -f "$profile_file" ]]; then
  echo "ERROR: repository profile file not found at $profile_file" >&2
  exit 2
fi

repository_type=""
versioning_scheme=""
branching_model=""
release_model=""
supported_release_lines=""
primary_language=""

while IFS= read -r line; do
  if [[ "$line" =~ ^[[:space:]-]*repository_type:[[:space:]]*(.+)$ ]]; then
    repository_type="${BASH_REMATCH[1]}"
  elif [[ "$line" =~ ^[[:space:]-]*versioning_scheme:[[:space:]]*(.+)$ ]]; then
    versioning_scheme="${BASH_REMATCH[1]}"
  elif [[ "$line" =~ ^[[:space:]-]*branching_model:[[:space:]]*(.+)$ ]]; then
    branching_model="${BASH_REMATCH[1]}"
  elif [[ "$line" =~ ^[[:space:]-]*release_model:[[:space:]]*(.+)$ ]]; then
    release_model="${BASH_REMATCH[1]}"
  elif [[ "$line" =~ ^[[:space:]-]*supported_release_lines:[[:space:]]*(.+)$ ]]; then
    supported_release_lines="${BASH_REMATCH[1]}"
  elif [[ "$line" =~ ^[[:space:]-]*primary_language:[[:space:]]*(.+)$ ]]; then
    primary_language="${BASH_REMATCH[1]}"
  fi
done < "$profile_file"

failed=0

for key in repository_type versioning_scheme branching_model release_model supported_release_lines primary_language; do
  value="${!key}"
  if [[ -z "$value" ]]; then
    echo "ERROR: repository profile missing required attribute '$key' in $profile_file" >&2
    failed=1
    continue
  fi

  if [[ "$value" == *"<"* || "$value" == *">"* || "$value" == *"|"* ]]; then
    echo "ERROR: repository profile attribute '$key' appears to be a placeholder: $value" >&2
    failed=1
  fi
done

exit $failed
