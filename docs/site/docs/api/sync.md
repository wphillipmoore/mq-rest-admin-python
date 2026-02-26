# Sync

## The problem with fire-and-forget

All MQSC `START` and `STOP` commands are fire-and-forget — they return
immediately without waiting for the object to reach its target state.
In practice, tooling that provisions infrastructure needs to wait until
a channel is `RUNNING` or a listener is `STOPPED` before proceeding to
the next step. Writing polling loops by hand is error-prone and
clutters business logic with retry mechanics.

## The sync pattern

The `*_sync` and `restart_*` methods wrap the fire-and-forget commands
with a polling loop that issues `DISPLAY *STATUS` until the object
reaches a stable state or the timeout expires.

## SyncOperation

An enum indicating the operation that was performed:

```python
class SyncOperation(Enum):
    STARTED    = "started"     # Object confirmed running
    STOPPED    = "stopped"     # Object confirmed stopped
    RESTARTED  = "restarted"   # Stop-then-start completed
```

## SyncConfig

Configuration controlling the polling behaviour:

```python
@dataclass
class SyncConfig:
    timeout: float = 30.0         # Max seconds before raising
    poll_interval: float = 1.0    # Seconds between polls
```

| Attribute | Type | Description |
| --- | --- | --- |
| `timeout` | `float` | Maximum seconds to wait before raising `MQRESTTimeoutError` |
| `poll_interval` | `float` | Seconds between `DISPLAY *STATUS` polls |

## SyncResult

Contains the outcome of a sync operation:

```python
class SyncResult(NamedTuple):
    operation: SyncOperation   # What happened
    polls: int                 # Number of status polls issued
    elapsed: float             # Wall-clock seconds from command to confirmation
```

| Attribute | Type | Description |
| --- | --- | --- |
| `operation` | `SyncOperation` | What happened: `STARTED`, `STOPPED`, or `RESTARTED` |
| `polls` | `int` | Number of status polls issued |
| `elapsed` | `float` | Wall-clock seconds from command to confirmation |

## Method signature pattern

All 9 sync methods follow the same signature pattern:

```python
def start_channel_sync(
    self,
    name: str,
    *,
    config: SyncConfig | None = None,
) -> SyncResult:
```

The `config` parameter is keyword-only for API clarity.

## Basic usage

```python
from pymqrest import SyncConfig, SyncOperation

# Start a channel and wait until it is RUNNING
result = session.start_channel_sync("TO.PARTNER")
assert result.operation is SyncOperation.STARTED
print(f"Channel running after {result.polls} poll(s), {result.elapsed:.1f}s")

# Stop a listener and wait until it is STOPPED
result = session.stop_listener_sync("TCP.LISTENER")
assert result.operation is SyncOperation.STOPPED
```

## Custom timeout and poll interval

Pass a `SyncConfig` to override the defaults:

```python
from pymqrest import SyncConfig

# Aggressive polling for fast local development
fast = SyncConfig(timeout_seconds=10.0, poll_interval_seconds=0.25)
result = session.start_service_sync("MY.SVC", config=fast)

# Patient polling for remote queue managers
patient = SyncConfig(timeout_seconds=120.0, poll_interval_seconds=5.0)
result = session.start_channel_sync("REMOTE.CHL", config=patient)
```

## Restart convenience

The `restart_*` methods perform a synchronous stop followed by a
synchronous start. Each phase gets the full timeout independently —
worst case is 2x the configured timeout.

The returned `SyncResult` reports **total** polls and **total** elapsed
time across both phases:

```python
result = session.restart_channel("TO.PARTNER")
assert result.operation is SyncOperation.RESTARTED
print(f"Restarted in {result.elapsed:.1f}s ({result.polls} total polls)")
```

## Timeout handling

When the timeout expires, `MQRESTTimeoutError` is raised with
diagnostic attributes:

```python
from pymqrest import MQRESTTimeoutError, SyncConfig

try:
    session.start_channel_sync(
        "BROKEN.CHL",
        config=SyncConfig(timeout_seconds=15.0),
    )
except MQRESTTimeoutError as err:
    print(f"Object: {err.name}")       # "BROKEN.CHL"
    print(f"Operation: {err.operation}")  # "start"
    print(f"Elapsed: {err.elapsed:.1f}s")  # 15.0
```

`MQRESTTimeoutError` inherits from `MQRESTError`, so existing
`except MQRESTError` handlers will catch it.

## Available methods

| Method | Operation | START/STOP qualifier | Status qualifier |
| --- | --- | --- | --- |
| `start_channel_sync()` | Start | `CHANNEL` | `CHSTATUS` |
| `stop_channel_sync()` | Stop | `CHANNEL` | `CHSTATUS` |
| `restart_channel()` | Restart | `CHANNEL` | `CHSTATUS` |
| `start_listener_sync()` | Start | `LISTENER` | `LSSTATUS` |
| `stop_listener_sync()` | Stop | `LISTENER` | `LSSTATUS` |
| `restart_listener()` | Restart | `LISTENER` | `LSSTATUS` |
| `start_service_sync()` | Start | `SERVICE` | `SVSTATUS` |
| `stop_service_sync()` | Stop | `SERVICE` | `SVSTATUS` |
| `restart_service()` | Restart | `SERVICE` | `SVSTATUS` |

## Status detection

The polling loop checks the `STATUS` attribute in the `DISPLAY *STATUS`
response. The target values are:

- **Start**: `RUNNING`
- **Stop**: `STOPPED`

### Channel stop edge case

When a channel stops, its `CHSTATUS` record may disappear entirely
(the `DISPLAY CHSTATUS` response returns no rows). The channel sync
methods treat an empty status result as successfully stopped. Listener
and service status records are always present, so empty results are not
treated as stopped for those object types.

## Attribute mapping

The sync methods call `_mqsc_command` internally, so they participate
in the same [mapping pipeline](mapping-pipeline.md) as all other
command methods. The status key is checked using both the mapped
`snake_case` name and the raw MQSC name, so polling works correctly
regardless of whether mapping is enabled or disabled.

## Provisioning example

The sync methods pair naturally with the
[ensure methods](ensure.md) for end-to-end provisioning:

```python
from pymqrest import SyncConfig

config = SyncConfig(timeout_seconds=60.0)

# Ensure listeners exist for application and admin traffic
session.ensure_listener("APP.LISTENER", request_parameters={
    "transport_type": "TCP",
    "port": 1415,
    "start_mode": "MQSVC_CONTROL_Q_MGR",
})
session.ensure_listener("ADMIN.LISTENER", request_parameters={
    "transport_type": "TCP",
    "port": 1416,
    "start_mode": "MQSVC_CONTROL_Q_MGR",
})

# Start them synchronously
session.start_listener_sync("APP.LISTENER", config=config)
session.start_listener_sync("ADMIN.LISTENER", config=config)

print("Listeners ready")
```

## Rolling restart example

Restart all listeners with error handling — useful when a queue
manager serves multiple TCP ports for different client populations:

```python
from pymqrest import MQRESTTimeoutError, SyncConfig

listeners = ["APP.LISTENER", "ADMIN.LISTENER", "PARTNER.LISTENER"]
config = SyncConfig(timeout_seconds=30.0, poll_interval_seconds=2.0)

for name in listeners:
    try:
        result = session.restart_listener(name, config=config)
        print(f"{name}: restarted in {result.elapsed:.1f}s")
    except MQRESTTimeoutError as err:
        print(f"{name}: timed out after {err.elapsed:.1f}s")
```

## API reference

::: pymqrest.sync.SyncConfig
    options:
      members: true

::: pymqrest.sync.SyncOperation
    options:
      members: true

::: pymqrest.sync.SyncResult
    options:
      members: true

::: pymqrest.sync.MQRESTSyncMixin
    options:
      members: true
      show_bases: true
      filters:
        - "!^_"
