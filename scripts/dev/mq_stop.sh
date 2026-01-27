#!/usr/bin/env bash
set -euo pipefail

docker compose -f scripts/dev/mq/docker-compose.yml down
