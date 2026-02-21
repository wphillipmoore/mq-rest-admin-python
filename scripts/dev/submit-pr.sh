#!/usr/bin/env bash
# Managed by standard-tooling — DO NOT EDIT in downstream repos.
# Canonical source: https://github.com/wphillipmoore/standard-tooling
# PR submission wrapper that constructs standards-compliant PR bodies.
# Populates .github/pull_request_template.md programmatically.

set -euo pipefail

repo_root="$(git rev-parse --show-toplevel)"

# --- Defaults ---
issue=""
linkage="Fixes"
summary=""
notes=""
title=""
docs_only=false
dry_run=false

# --- Argument parsing ---
usage() {
  cat >&2 <<'EOF'
Usage: scripts/dev/submit-pr.sh --issue NUMBER --summary TEXT [options]

Required:
  --issue REF       Issue reference: a number (42) for same-repo, or
                    a cross-repo ref (owner/repo#42)
  --summary TEXT    One-line PR summary (goes under ## Summary)

Optional:
  --linkage KEYWORD Issue linkage keyword (default: Fixes)
                    Allowed: Fixes, Closes, Resolves, Ref
  --notes TEXT      Additional notes for the PR
  --title TEXT      PR title (default: most recent commit subject)
  --docs-only       Apply docs-only exception to testing section
  --dry-run         Print the PR body and command without executing
  -h, --help        Show this help
EOF
  exit 1
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --issue)    issue="$2";   shift 2 ;;
    --linkage)  linkage="$2"; shift 2 ;;
    --summary)  summary="$2"; shift 2 ;;
    --notes)    notes="$2";   shift 2 ;;
    --title)    title="$2";   shift 2 ;;
    --docs-only) docs_only=true; shift ;;
    --dry-run)  dry_run=true; shift ;;
    -h|--help)  usage ;;
    *)
      echo "ERROR: unknown argument: $1" >&2
      usage
      ;;
  esac
done

# --- Validation ---

if [[ -z "$issue" ]]; then
  echo "ERROR: --issue is required." >&2
  usage
fi
if [[ -z "$summary" ]]; then
  echo "ERROR: --summary is required." >&2
  usage
fi

# Validate issue reference: plain number or owner/repo#number.
if [[ "$issue" =~ ^[1-9][0-9]*$ ]]; then
  issue_ref="#${issue}"
elif [[ "$issue" =~ ^[A-Za-z0-9._-]+/[A-Za-z0-9._-]+#[1-9][0-9]*$ ]]; then
  issue_ref="${issue}"
else
  echo "ERROR: --issue must be a number (42) or cross-repo ref (owner/repo#42), got '$issue'." >&2
  exit 1
fi

# Validate linkage keyword.
if [[ ! "$linkage" =~ ^(Fixes|Closes|Resolves|Ref)$ ]]; then
  echo "ERROR: invalid --linkage '$linkage'. Allowed: Fixes, Closes, Resolves, Ref" >&2
  exit 1
fi

# --- Detect branch and target ---
current_branch="$(git rev-parse --abbrev-ref HEAD)"

if [[ "$current_branch" == release/* ]]; then
  target_branch="main"
  merge_strategy="--merge"
else
  target_branch="develop"
  merge_strategy="--squash"
fi

# --- Generate PR title ---
if [[ -z "$title" ]]; then
  title="$(git log -1 --pretty=%s)"
fi

# --- Build testing section ---
# Read the testing section from the PR template as the default.
template_file="$repo_root/.github/pull_request_template.md"
testing_section=""
if [[ -f "$template_file" ]]; then
  # Extract lines between ## Testing and the next ## heading.
  in_testing=false
  while IFS= read -r line; do
    if [[ "$line" =~ ^##[[:space:]]+Testing ]]; then
      in_testing=true
      continue
    fi
    if [[ "$in_testing" == true && "$line" =~ ^##[[:space:]] ]]; then
      break
    fi
    if [[ "$in_testing" == true ]]; then
      testing_section="${testing_section}${line}
"
    fi
  done < "$template_file"
  # Trim leading/trailing blank lines.
  # Remove leading blank lines.
  while [[ "$testing_section" == $'\n'* ]]; do
    testing_section="${testing_section#$'\n'}"
  done
  # Remove trailing blank lines and whitespace.
  while [[ "$testing_section" == *$'\n' ]]; do
    testing_section="${testing_section%$'\n'}"
  done
fi

if [[ "$docs_only" == true ]]; then
  changed_files="$(git diff --name-only "${target_branch}...HEAD" 2>/dev/null || git diff --name-only HEAD~1)"
  prefixed_files=""
  while IFS= read -r file; do
    prefixed_files="${prefixed_files}- ${file}
"
  done <<< "$changed_files"
  testing_section="Docs-only: tests skipped

Changed files:
${prefixed_files%
}"
fi

# --- Build notes section ---
notes_section="${notes:--}"

# --- Construct PR body ---
pr_body="# Pull Request

## Summary

- ${summary}

## Issue Linkage

- ${linkage} ${issue_ref}

## Testing

${testing_section}

## Notes

- ${notes_section}"

# --- Execute or dry-run ---
if [[ "$dry_run" == true ]]; then
  echo "=== PR Title ==="
  echo "$title"
  echo ""
  echo "=== Target Branch ==="
  echo "$target_branch (strategy: $merge_strategy)"
  echo ""
  echo "=== PR Body ==="
  echo "$pr_body"
  exit 0
fi

# Push branch to origin.
echo "Pushing branch '$current_branch' to origin..."
git push -u origin "$current_branch"

# Use a temporary file for the PR body to preserve formatting.
tmp_body="$(mktemp)"
trap 'rm -f "$tmp_body"' EXIT
printf '%s\n' "$pr_body" > "$tmp_body"

# Create PR.
echo "Creating PR..."
pr_url="$(gh pr create \
  --base "$target_branch" \
  --title "$title" \
  --body-file "$tmp_body")"

echo "PR created: $pr_url"

# Enable auto-merge.
echo "Enabling auto-merge ($merge_strategy)..."
gh pr merge --auto "$merge_strategy" --delete-branch

echo "Done. PR URL: $pr_url"
