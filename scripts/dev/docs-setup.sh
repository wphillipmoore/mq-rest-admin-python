#!/usr/bin/env bash
# Sets up the local development environment for building documentation.
#
# Creates a symlink from .mq-rest-admin-common to the sibling common repo
# so that MkDocs snippets can resolve shared fragments.
#
# Usage: scripts/dev/docs-setup.sh

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
COMMON_REPO="${MQ_REST_ADMIN_COMMON_PATH:-$PROJECT_ROOT/../mq-rest-admin-common}"
LINK_PATH="$PROJECT_ROOT/.mq-rest-admin-common"

if [ -L "$LINK_PATH" ]; then
    echo "Symlink already exists: $LINK_PATH -> $(readlink "$LINK_PATH")"
    exit 0
fi

if [ -e "$LINK_PATH" ]; then
    echo "Error: $LINK_PATH exists but is not a symlink. Remove it first."
    exit 1
fi

if [ ! -d "$COMMON_REPO" ]; then
    echo "Error: Common repo not found at $COMMON_REPO"
    echo "Clone it with: git clone https://github.com/wphillipmoore/mq-rest-admin-common.git $COMMON_REPO"
    exit 1
fi

ln -s "$COMMON_REPO" "$LINK_PATH"
echo "Created symlink: $LINK_PATH -> $COMMON_REPO"

echo ""
echo "To install documentation tools:"
echo "  uv sync --group docs"
echo ""
echo "To build docs locally:"
echo "  uv run mkdocs build -f docs/site/mkdocs.yml"
echo ""
echo "To preview versioned docs locally:"
echo "  uv run mike serve -F docs/site/mkdocs.yml"
