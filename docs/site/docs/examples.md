# Examples

The `examples/` directory contains practical scripts that demonstrate common
MQ administration tasks using `pymqrest`. Each script is self-contained and
can be run against the local Docker environment.

## Prerequisites

Start the multi-queue-manager Docker environment and seed both queue managers:

```bash
./scripts/dev/mq_start.sh
./scripts/dev/mq_seed.sh
```

This starts two queue managers (`QM1` on port 9443, `QM2` on port 9444) on a
shared Docker network. See [local MQ container](development/local-mq-container.md) for details.

## Running examples

Each script reads connection details from environment variables with sensible
defaults for the local Docker setup:

```bash
uv run python3 examples/health_check.py
uv run python3 examples/queue_depth_monitor.py
uv run python3 examples/channel_status.py
uv run python3 examples/queue_status.py
uv run python3 examples/dlq_inspector.py
uv run python3 examples/provision_environment.py
```

## Health check

`examples/health_check.py` connects to one or more queue managers and checks:

- Queue manager attributes via `display_qmgr()`
- Running status via `display_qmstatus()`
- Command server availability via `display_cmdserv()`
- Listener definitions via `display_listener()`

Produces a pass/fail summary for each queue manager. Set
`MQ_REST_BASE_URL_QM2` to also check QM2:

```bash
MQ_REST_BASE_URL_QM2=https://localhost:9444/ibmmq/rest/v2 \
    uv run python3 examples/health_check.py
```

## Queue depth monitor

`examples/queue_depth_monitor.py` displays all local queues with their current
depth and flags queues approaching capacity:

- Lists all local queues via `display_queue()`
- Calculates depth percentage (`current_queue_depth / max_queue_depth`)
- Flags queues above a configurable threshold (default 80%)

Set `DEPTH_THRESHOLD_PCT` to change the warning threshold:

```bash
DEPTH_THRESHOLD_PCT=50 uv run python3 examples/queue_depth_monitor.py
```

## Channel status report

`examples/channel_status.py` cross-references channel definitions with live
channel status:

- Retrieves definitions via `display_channel()`
- Retrieves live status via `display_chstatus()`
- Identifies channels that are defined but not running

## Queue status and connection handles

`examples/queue_status.py` demonstrates how `pymqrest` handles the nested
`objects` response structure returned by `TYPE(HANDLE)` queries:

- Retrieves per-handle queue status via `display_qstatus()` with
  `request_parameters={"type": "HANDLE"}`
- Retrieves per-handle connection details via `display_conn()` with
  `request_parameters={"connection_info_type": "HANDLE"}`
- Shows that `pymqrest` transparently flattens the nested response into
  uniform flat dicts — each result contains both parent-scoped and
  per-handle attributes

The results may be empty if no applications have active handles on the
queue manager.

## Dead letter queue inspector

`examples/dlq_inspector.py` inspects the dead letter queue configuration:

- Reads the DLQ name from `display_qmgr()`
- Queries DLQ depth and capacity via `display_queue()`
- Suggests actions based on queue state

## Environment provisioner

`examples/provision_environment.py` demonstrates bulk provisioning across two
queue managers:

- Defines local queues, transmission queues, and remote queue definitions
- Creates sender/receiver channel pairs between QM1 and QM2
- Verifies provisioned objects with display commands
- Includes a teardown function that removes all created objects

Requires both QM1 and QM2:

```bash
uv run python3 examples/provision_environment.py
```

## Testability

Each example exposes its core logic as a function that accepts an
`MQRESTSession` and returns structured data. The `__main__` block handles
session construction from environment variables. This allows integration tests
to call the functions directly:

```python
from pymqrest import MQRESTSession
from pymqrest.auth import LTPAAuth
from examples.health_check import check_health

session = MQRESTSession(
    rest_base_url="https://localhost:9443/ibmmq/rest/v2",
    qmgr_name="QM1",
    credentials=LTPAAuth("mqadmin", "mqadmin"),
    verify_tls=False,
)

result = check_health(session)
assert result.passed
```

Integration tests for all examples are in `tests/integration/test_examples.py`
and run with:

```bash
MQ_REST_ADMIN_RUN_INTEGRATION=1 uv run pytest tests/integration/test_examples.py
```
