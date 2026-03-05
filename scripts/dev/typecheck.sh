#!/usr/bin/env bash
set -euo pipefail

export DOCKER_DEV_IMAGE="${DOCKER_DEV_IMAGE:-dev-python:3.14}"
export DOCKER_TEST_CMD="${DOCKER_TEST_CMD:-uv sync --frozen --group dev && uv run mypy src/ && uv run ty check src}"

if ! command -v docker-test >/dev/null 2>&1; then
  echo "ERROR: docker-test not found on PATH." >&2
  echo "Set up standard-tooling: export PATH=../standard-tooling/scripts/bin:\$PATH" >&2
  exit 1
fi
exec docker-test
