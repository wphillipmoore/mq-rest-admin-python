#!/usr/bin/env bash
set -euo pipefail

mq_admin_user="${MQ_ADMIN_USER:-mqadmin}"
mq_admin_password="${MQ_ADMIN_PASSWORD:-mqadmin}"
qm1_rest_base_url="${MQ_REST_BASE_URL:-https://localhost:9443/ibmmq/rest/v2}"
qm2_rest_base_url="${MQ_REST_BASE_URL_QM2:-https://localhost:9444/ibmmq/rest/v2}"

echo "=== QM1: PYMQREST.QLOCAL ==="
curl -sS -k -u "${mq_admin_user}:${mq_admin_password}" \
  -H "Content-Type: application/json" \
  -H "ibm-mq-rest-csrf-token: local" \
  -d '{"type": "runCommandJSON", "command": "DISPLAY", "qualifier": "QLOCAL", "name": "PYMQREST.QLOCAL"}' \
  "${qm1_rest_base_url}/admin/action/qmgr/QM1/mqsc"

echo ""
echo "---"
echo ""

echo "=== QM1: PYMQREST.SVRCONN ==="
curl -sS -k -u "${mq_admin_user}:${mq_admin_password}" \
  -H "Content-Type: application/json" \
  -H "ibm-mq-rest-csrf-token: local" \
  -d '{"type": "runCommandJSON", "command": "DISPLAY", "qualifier": "CHANNEL", "name": "PYMQREST.SVRCONN"}' \
  "${qm1_rest_base_url}/admin/action/qmgr/QM1/mqsc"

echo ""
echo "---"
echo ""

echo "=== QM2: PYMQREST.QLOCAL ==="
curl -sS -k -u "${mq_admin_user}:${mq_admin_password}" \
  -H "Content-Type: application/json" \
  -H "ibm-mq-rest-csrf-token: local" \
  -d '{"type": "runCommandJSON", "command": "DISPLAY", "qualifier": "QLOCAL", "name": "PYMQREST.QLOCAL"}' \
  "${qm2_rest_base_url}/admin/action/qmgr/QM2/mqsc"
