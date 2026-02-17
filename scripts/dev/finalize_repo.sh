#!/usr/bin/env bash
set -euo pipefail

# Finalize a repository after a PR merge: switch to the target branch,
# fast-forward pull, delete merged local branches, and prune remotes.

# -- defaults ----------------------------------------------------------------

target_branch="develop"
dry_run=false

# -- argument parsing --------------------------------------------------------

usage() {
  cat <<EOF
Usage: $(basename "$0") [OPTIONS]

Finalize a repository after a PR merge.

Options:
  --target-branch BRANCH  Target branch to switch to (default: develop)
  --dry-run               Show what would be done without making changes
  -h, --help              Show this help message
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --target-branch)
      target_branch="$2"
      shift 2
      ;;
    --dry-run)
      dry_run=true
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

# -- eternal branch detection -----------------------------------------------

repo_root="$(git rev-parse --show-toplevel)"
profile_file="$repo_root/docs/repository-standards.md"
branching_model=""

if [[ -f "$profile_file" ]]; then
  while IFS= read -r line; do
    if [[ "$line" =~ ^[[:space:]-]*branching_model:[[:space:]]*(.+)$ ]]; then
      branching_model="${BASH_REMATCH[1]}"
      break
    fi
  done < "$profile_file"
fi

# Build the list of eternal branches to protect from deletion.
eternal_branches=("gh-pages")

case "$branching_model" in
  docs-single-branch)
    eternal_branches+=("develop")
    ;;
  library-release)
    eternal_branches+=("develop" "main")
    ;;
  application-promotion)
    eternal_branches+=("develop" "release" "main")
    ;;
  "")
    echo "WARNING: branching_model not found; protecting develop and main." >&2
    eternal_branches+=("develop" "main")
    ;;
  *)
    echo "ERROR: unrecognized branching_model '$branching_model'." >&2
    exit 1
    ;;
esac

is_eternal() {
  local branch="$1"
  for eternal in "${eternal_branches[@]}"; do
    if [[ "$branch" == "$eternal" ]]; then
      return 0
    fi
  done
  return 1
}

# -- helpers -----------------------------------------------------------------

run() {
  if [[ "$dry_run" == true ]]; then
    echo "  [dry-run] $*"
  else
    "$@"
  fi
}

# -- step 1: switch to target branch ----------------------------------------

current_branch="$(git rev-parse --abbrev-ref HEAD)"

if [[ "$current_branch" != "$target_branch" ]]; then
  echo "Switching to $target_branch..."
  run git checkout "$target_branch"
else
  echo "Already on $target_branch."
fi

# -- step 2: fetch and fast-forward pull ------------------------------------

echo "Pulling latest from origin/$target_branch..."
run git fetch origin "$target_branch"
if [[ "$dry_run" != true ]]; then
  git pull --ff-only origin "$target_branch"
else
  echo "  [dry-run] git pull --ff-only origin $target_branch"
fi

# -- step 3: delete merged local branches -----------------------------------

echo "Checking for merged local branches..."
deleted_branches=()

for branch in $(git branch --merged "$target_branch" --format='%(refname:short)'); do
  if is_eternal "$branch"; then
    continue
  fi
  echo "  Deleting merged branch: $branch"
  run git branch -d "$branch"
  deleted_branches+=("$branch")
done

# -- step 4: prune stale remote-tracking references -------------------------

echo "Pruning stale remote-tracking references..."
run git remote prune origin

# -- summary -----------------------------------------------------------------

echo ""
echo "Finalization complete."
echo "  Branch: $target_branch"
if [[ ${#deleted_branches[@]} -gt 0 ]]; then
  echo "  Deleted: ${deleted_branches[*]}"
else
  echo "  Deleted: (none)"
fi
echo "  Remotes: pruned"
