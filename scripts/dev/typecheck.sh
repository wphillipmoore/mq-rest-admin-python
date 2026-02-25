#!/usr/bin/env bash
set -euo pipefail

export DOCKER_DEV_IMAGE="${DOCKER_DEV_IMAGE:-dev-python:3.14}"
export DOCKER_TEST_CMD="${DOCKER_TEST_CMD:-uv sync --frozen --group dev && uv run mypy src/ && uv run ty check src}"

if command -v docker-test >/dev/null 2>&1; then
  exec docker-test
fi

# Fallback: run docker directly if docker-test is not on PATH.
repo_root="$(cd "$(dirname "$0")/../.." && pwd)"

echo "Image:   ${DOCKER_DEV_IMAGE}"
echo "Command: ${DOCKER_TEST_CMD}"
echo "---"

exec docker run --rm \
  -v "${repo_root}:/workspace" \
  -w /workspace \
  "${DOCKER_DEV_IMAGE}" \
  bash -c "${DOCKER_TEST_CMD}"
