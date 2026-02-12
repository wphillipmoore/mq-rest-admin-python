#!/usr/bin/env bash
set -euo pipefail

# runmqsc returns the count of failed commands as its exit code.
# START CHANNEL fails harmlessly when the channel is already running,
# so tolerate non-zero exits here.  Output is still printed for
# inspection.
docker compose -f scripts/dev/mq/docker-compose.yml exec -T qm1 runmqsc QM1 < scripts/dev/mq/seed-qm1.mqsc || true
docker compose -f scripts/dev/mq/docker-compose.yml exec -T qm2 runmqsc QM2 < scripts/dev/mq/seed-qm2.mqsc || true
