#!/usr/bin/env bash
set -euo pipefail

docker compose -f scripts/dev/mq/docker-compose.yml exec -T mq runmqsc QM1 < scripts/dev/mq/seed.mqsc
