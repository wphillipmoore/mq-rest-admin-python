# Local MQ container

A containerized IBM MQ queue manager provides a local environment for
development and integration testing.

## Prerequisites

- Docker Desktop or compatible Docker Engine.
- IBM MQ container image access (license acceptance required).

## Configuration

| Setting | Value |
| --- | --- |
| Queue manager | `QM1` |
| MQ listener port | `1414` |
| REST API port | `9443` |
| Admin credentials | `mqadmin` / `mqadmin` |
| Read-only credentials | `mqreader` / `mqreader` |
| REST base URL | `https://localhost:9443/ibmmq/rest/v2` |

The Docker Compose file is at `scripts/dev/mq/docker-compose.yml`.

## Quick start

Start the queue manager:

```bash
./scripts/dev/mq_start.sh
```

Seed deterministic test objects (all prefixed with `PYMQREST.`):

```bash
./scripts/dev/mq_seed.sh
```

Verify REST-based MQSC responses:

```bash
./scripts/dev/mq_verify.sh
```

## Lifecycle scripts

| Script | Purpose |
| --- | --- |
| `scripts/dev/mq_start.sh` | Start the containerized queue manager |
| `scripts/dev/mq_seed.sh` | Seed deterministic test objects |
| `scripts/dev/mq_verify.sh` | Verify REST-based MQSC responses |
| `scripts/dev/mq_stop.sh` | Stop the queue manager |
| `scripts/dev/mq_reset.sh` | Reset to clean state (removes data volume) |

The seed script uses `REPLACE` so it can be re-run at any time without
side effects.

## Integration testing

Integration tests are opt-in and require a running MQ container:

```bash
PYMQREST_RUN_INTEGRATION=1 uv run pytest -m integration
```

When enabled, the test session:

1. Starts the local MQ container.
2. Waits for the REST endpoint to become ready.
3. Seeds deterministic test objects.
4. Runs DISPLAY checks plus define/alter/delete lifecycles.
5. Stops the container after the session.

## Environment variables

| Variable | Default | Description |
| --- | --- | --- |
| `MQ_REST_BASE_URL` | `https://localhost:9443/ibmmq/rest/v2` | REST API base URL |
| `MQ_ADMIN_USER` | `mqadmin` | Admin username |
| `MQ_ADMIN_PASSWORD` | `mqadmin` | Admin password |
| `MQ_IMAGE` | `icr.io/ibm-messaging/mq:latest` | Container image |

## Reset workflow

To return to a completely clean state (removes the data volume):

```bash
./scripts/dev/mq_reset.sh
```

## Troubleshooting

If the REST API is not reachable, ensure the embedded web server is
binding to all interfaces:

```bash
docker compose -f scripts/dev/mq/docker-compose.yml exec -T mq \
    setmqweb properties -k httpHost -v "*"
```

Then restart the container and retry the verification workflow.
