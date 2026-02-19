#!/usr/bin/env bash
# Commit wrapper that constructs standards-compliant commit messages.
# Resolves Co-Authored-By identities from docs/repository-standards.md.

set -euo pipefail

repo_root="$(git rev-parse --show-toplevel)"

# --- Defaults ---
type=""
scope=""
message=""
body=""
agent=""

# --- Argument parsing ---
usage() {
  cat >&2 <<'EOF'
Usage: scripts/dev/commit.sh --type TYPE --message MESSAGE --agent AGENT [options]

Required:
  --type TYPE       Conventional commit type (feat|fix|docs|style|refactor|test|chore|ci|build)
  --message MESSAGE Commit description (text after "type: ")
  --agent AGENT     AI tool identity: claude or codex

Optional:
  --scope SCOPE     Conventional commit scope
  --body BODY       Detailed commit body
  -h, --help        Show this help
EOF
  exit 1
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --type)    type="$2";    shift 2 ;;
    --scope)   scope="$2";   shift 2 ;;
    --message) message="$2"; shift 2 ;;
    --body)    body="$2";    shift 2 ;;
    --agent)   agent="$2";   shift 2 ;;
    -h|--help) usage ;;
    *)
      echo "ERROR: unknown argument: $1" >&2
      usage
      ;;
  esac
done

# --- Validation ---

# Required arguments.
if [[ -z "$type" ]]; then
  echo "ERROR: --type is required." >&2
  usage
fi
if [[ -z "$message" ]]; then
  echo "ERROR: --message is required." >&2
  usage
fi
if [[ -z "$agent" ]]; then
  echo "ERROR: --agent is required." >&2
  usage
fi

# Validate type.
allowed_types="feat|fix|docs|style|refactor|test|chore|ci|build"
if [[ ! "$type" =~ ^(feat|fix|docs|style|refactor|test|chore|ci|build)$ ]]; then
  echo "ERROR: invalid --type '$type'. Allowed: $allowed_types" >&2
  exit 1
fi

# Resolve agent identity from docs/repository-standards.md.
profile_file="$repo_root/docs/repository-standards.md"
if [[ ! -f "$profile_file" ]]; then
  echo "ERROR: repository profile not found at $profile_file" >&2
  exit 1
fi

# Look for the identity whose username contains -<agent> (e.g., -claude, -codex).
identity=""
while IFS= read -r line; do
  # Lines look like: - Co-Authored-By: name <email>
  stripped="${line#- }"
  if echo "$stripped" | grep -qi "\-${agent}[[:space:]]"; then
    identity="$stripped"
    break
  fi
done < <(grep -i '^\- Co-Authored-By:' "$profile_file" || true)

if [[ -z "$identity" ]]; then
  echo "ERROR: no approved identity found for agent '$agent' in $profile_file." >&2
  echo "Approved identities are listed under 'AI co-authors'." >&2
  exit 1
fi

# Verify there are staged changes.
if git diff --cached --quiet; then
  echo "ERROR: no staged changes. Stage files with 'git add' before committing." >&2
  exit 1
fi

# --- Construct commit message ---
subject="$type"
if [[ -n "$scope" ]]; then
  subject="${subject}(${scope})"
fi
subject="${subject}: ${message}"

# Use a temporary file to preserve formatting (per AGENTS.md guidance).
tmp_file="$(mktemp)"
trap 'rm -f "$tmp_file"' EXIT

printf '%s\n' "$subject" > "$tmp_file"
if [[ -n "$body" ]]; then
  printf '\n%s\n' "$body" >> "$tmp_file"
fi
printf '\n%s\n' "$identity" >> "$tmp_file"

# --- Commit ---
git commit --file "$tmp_file"
