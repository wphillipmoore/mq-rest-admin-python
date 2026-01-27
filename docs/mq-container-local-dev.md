# IBM MQ containerized queue manager

## Table of Contents
- [Purpose](#purpose)
- [Files](#files)
- [Prerequisites](#prerequisites)
- [Configuration](#configuration)
- [Quick start](#quick-start)
- [Seed objects](#seed-objects)
- [Verification workflow](#verification-workflow)
- [Integration test scaffolding](#integration-test-scaffolding)
- [Reset workflow](#reset-workflow)
- [Troubleshooting](#troubleshooting)

## Purpose
Provide a repeatable, containerized IBM MQ queue manager for local development
and integration testing so MQSC/PCF mapping assumptions can be verified against
real command responses.

## Files
- `scripts/dev/mq/docker-compose.yml`
- `scripts/dev/mq/mqwebuser.xml`
- `scripts/dev/mq/seed.mqsc`
- `scripts/dev/mq_start.sh`
- `scripts/dev/mq_stop.sh`
- `scripts/dev/mq_reset.sh`
- `scripts/dev/mq_seed.sh`
- `scripts/dev/mq_verify.sh`

## Prerequisites
- Docker Desktop or compatible Docker Engine.
- IBM MQ container image access (license acceptance required).

## Configuration
- Image: `MQ_IMAGE` (defaults to `icr.io/ibm-messaging/mq:latest`).
- Queue manager: `QM1` (`MQ_QMGR_NAME` in `scripts/dev/mq/docker-compose.yml`).
- Ports:
  - `1414`: MQ listener.
  - `9443`: mqweb console + REST API.
- Embedded web server: `MQ_ENABLE_EMBEDDED_WEB_SERVER=true` in the compose file.
- Credentials (REST + console):
  - `mqadmin` / `mqadmin` (admin)
  - `mqreader` / `mqreader` (read-only)
- The compose file sets `LICENSE=accept`. You must accept the IBM MQ container
  license before running the image.

## Quick start
1. Start the queue manager:
   ```bash
   ./scripts/dev/mq_start.sh
   ```
2. Seed deterministic objects:
   ```bash
   ./scripts/dev/mq_seed.sh
   ```
3. Verify REST-based MQSC responses:
   ```bash
   ./scripts/dev/mq_verify.sh
   ```

## Seed objects
The seed script defines a small, deterministic set of queues, channels, and
related objects with a `PYMQREST.` prefix. Re-run the seed at any time; all
definitions use `REPLACE` to stay idempotent.

## Verification workflow
The verification script posts `runCommandJSON` requests to the admin REST API
and prints structured JSON responses for:
- `DISPLAY QLOCAL(PYMQREST.QLOCAL)`
- `DISPLAY CHANNEL(PYMQREST.SVRCONN)`

Payload shape (validated in this container):
```json
{
  "type": "runCommandJSON",
  "command": "DISPLAY",
  "qualifier": "QLOCAL",
  "name": "PYMQREST.QLOCAL"
}
```

Notes:
- `command` must be the MQSC verb (for example, `DISPLAY`).
- `qualifier` selects the object type (`QMGR`, `QLOCAL`, `CHANNEL`, etc.).
- `name` is required for object-specific queries (not required for `QMGR`).

Queue manager example (no `name` required):
```json
{
  "type": "runCommandJSON",
  "command": "DISPLAY",
  "qualifier": "QMGR"
}
```

Response shape (abbreviated):
```json
{
  "commandResponse": [
    {
      "completionCode": 0,
      "reasonCode": 0,
      "parameters": {
        "queue": "PYMQREST.QLOCAL",
        "defpsist": "YES",
        "descr": "pymqrest local queue"
      }
    }
  ],
  "overallReasonCode": 0,
  "overallCompletionCode": 0
}
```

Defaults:
- REST base URL: `https://localhost:9443/ibmmq/rest/v2`
- Admin user: `mqadmin`
- Admin password: `mqadmin`

Override these via environment variables if needed:
- `MQ_REST_BASE_URL`
- `MQ_ADMIN_USER`
- `MQ_ADMIN_PASSWORD`

## Integration test scaffolding
An integration test scaffold exists at `tests/integration/test_mq_integration.py`.
The tests are skipped by default and require an explicit opt-in:

```bash
PYMQREST_RUN_INTEGRATION=1 pytest -m integration
```

These tests are placeholders until the REST client API is implemented. They
provide a shared place to add real MQSC/PCF validation once the API is ready.

## Reset workflow
To return to a clean, known state (including removing the queue manager data
volume):
```bash
./scripts/dev/mq_reset.sh
```

## Troubleshooting
- If the REST API is not reachable from the host, run:
  ```bash
  docker compose -f scripts/dev/mq/docker-compose.yml exec -T mq \
    setmqweb properties -k httpHost -v "*"
  ```
  Then restart the container and retry the verification workflow.
