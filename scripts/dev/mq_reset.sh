#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "$0")/../.." && pwd)"
mq_dev_env="${MQ_DEV_ENV_PATH:-${repo_root}/../mq-dev-environment}"

if [ ! -d "$mq_dev_env" ]; then
  echo "mq-dev-environment not found at: $mq_dev_env" >&2
  echo "Clone it as a sibling directory or set MQ_DEV_ENV_PATH." >&2
  exit 1
fi

cd "$mq_dev_env"
exec scripts/mq_reset.sh
