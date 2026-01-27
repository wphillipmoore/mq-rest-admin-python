#!/usr/bin/env bash
set -euo pipefail

mq_admin_user="${MQ_ADMIN_USER:-mqadmin}"
mq_admin_password="${MQ_ADMIN_PASSWORD:-mqadmin}"
rest_base_url="${MQ_REST_BASE_URL:-https://localhost:9443/ibmmq/rest/v2}"

curl -sS -k -u "${mq_admin_user}:${mq_admin_password}" \
  -H "Content-Type: application/json" \
  -H "ibm-mq-rest-csrf-token: local" \
  -d '{"type": "runCommandJSON", "command": "DISPLAY", "qualifier": "QLOCAL", "name": "PYMQREST.QLOCAL"}' \
  "${rest_base_url}/admin/action/qmgr/QM1/mqsc"

echo ""

echo "---"

echo ""

curl -sS -k -u "${mq_admin_user}:${mq_admin_password}" \
  -H "Content-Type: application/json" \
  -H "ibm-mq-rest-csrf-token: local" \
  -d '{"type": "runCommandJSON", "command": "DISPLAY", "qualifier": "CHANNEL", "name": "PYMQREST.SVRCONN"}' \
  "${rest_base_url}/admin/action/qmgr/QM1/mqsc"
