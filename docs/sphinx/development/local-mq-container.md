# Local MQ container

A containerized IBM MQ environment provides two queue managers for
development and integration testing.

## Prerequisites

- Docker Desktop or compatible Docker Engine.
- IBM MQ container image access (license acceptance required).

## Configuration

The Docker Compose file at `scripts/dev/mq/docker-compose.yml` runs two
queue managers on a shared network (`pymqrest-net`):

| Setting | QM1 | QM2 |
| --- | --- | --- |
| Queue manager | `QM1` | `QM2` |
| MQ listener port | `1414` | `1415` |
| REST API port | `9443` | `9444` |
| Container name | `pymqrest-qm1` | `pymqrest-qm2` |

Both queue managers share the same credentials:

| Setting | Value |
| --- | --- |
| Admin credentials | `mqadmin` / `mqadmin` |
| Read-only credentials | `mqreader` / `mqreader` |
| QM1 REST base URL | `https://localhost:9443/ibmmq/rest/v2` |
| QM2 REST base URL | `https://localhost:9444/ibmmq/rest/v2` |

## Quick start

Start both queue managers:

```bash
./scripts/dev/mq_start.sh
```

Seed deterministic test objects on both QMs (all prefixed with `PYMQREST.`):

```bash
./scripts/dev/mq_seed.sh
```

Verify REST-based MQSC responses on both QMs:

```bash
./scripts/dev/mq_verify.sh
```

## Seed objects

QM1 receives the full set of test objects (queues, channels, topics,
namelists, listeners, processes) plus cross-QM objects for communicating
with QM2. QM2 receives a smaller set of objects plus the reciprocal
cross-QM definitions.

The seed scripts are at `scripts/dev/mq/seed-qm1.mqsc` and
`scripts/dev/mq/seed-qm2.mqsc`. Both use `REPLACE` so they can be
re-run at any time without side effects.

## Lifecycle scripts

| Script | Purpose |
| --- | --- |
| `scripts/dev/mq_start.sh` | Start both queue managers and wait for REST readiness |
| `scripts/dev/mq_seed.sh` | Seed deterministic test objects on both QMs |
| `scripts/dev/mq_verify.sh` | Verify REST-based MQSC responses on both QMs |
| `scripts/dev/mq_stop.sh` | Stop both queue managers |
| `scripts/dev/mq_reset.sh` | Reset to clean state (removes data volumes) |

## Integration testing

Integration tests are opt-in and require running MQ containers:

```bash
PYMQREST_RUN_INTEGRATION=1 uv run pytest -m integration
```

When enabled, the test session:

1. Starts both local MQ containers.
2. Waits for both REST endpoints to become ready.
3. Seeds deterministic test objects on both QMs.
4. Runs DISPLAY checks plus define/alter/delete lifecycles.
5. Stops both containers after the session.

## Environment variables

| Variable | Default | Description |
| --- | --- | --- |
| `MQ_REST_BASE_URL` | `https://localhost:9443/ibmmq/rest/v2` | QM1 REST API base URL |
| `MQ_REST_BASE_URL_QM2` | `https://localhost:9444/ibmmq/rest/v2` | QM2 REST API base URL |
| `MQ_ADMIN_USER` | `mqadmin` | Admin username |
| `MQ_ADMIN_PASSWORD` | `mqadmin` | Admin password |
| `MQ_IMAGE` | `icr.io/ibm-messaging/mq:latest` | Container image |

## Gateway routing

The two-QM local setup supports gateway routing out of the box. The seed
scripts create QM aliases and sender/receiver channels so each queue manager
can route MQSC commands to the other.

### curl example

Query QM2's queue manager attributes through QM1's REST API:

```bash
curl -k -u mqadmin:mqadmin \
  -H "Content-Type: application/json" \
  -H "ibm-mq-rest-csrf-token: local" \
  -H "ibm-mq-rest-gateway-qmgr: QM1" \
  -d '{"type": "runCommandJSON", "command": "DISPLAY", "qualifier": "QMGR"}' \
  https://localhost:9443/ibmmq/rest/v2/admin/action/qmgr/QM2/mqsc
```

### pymqrest example

```python
from pymqrest import MQRESTSession
from pymqrest.auth import BasicAuth

# Route commands to QM2 through QM1
session = MQRESTSession(
    rest_base_url="https://localhost:9443/ibmmq/rest/v2",
    qmgr_name="QM2",
    credentials=BasicAuth("mqadmin", "mqadmin"),
    gateway_qmgr="QM1",
    verify_tls=False,
)

qmgr = session.display_qmgr()
print(qmgr)  # QM2's attributes, routed through QM1
```

## Reset workflow

To return to a completely clean state (removes both data volumes):

```bash
./scripts/dev/mq_reset.sh
```

## Troubleshooting

If the REST API is not reachable, ensure the embedded web server is
binding to all interfaces:

```bash
docker compose -f scripts/dev/mq/docker-compose.yml exec -T qm1 \
    setmqweb properties -k httpHost -v "*"
```

Then restart the containers and retry the verification workflow.
