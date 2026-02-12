# Synchronous start/stop/restart

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

Each call returns a `SyncResult` describing what happened:

```python
from pymqrest import SyncConfig, SyncOperation, SyncResult

class SyncOperation(enum.Enum):
    STARTED = "started"      # Object confirmed running
    STOPPED = "stopped"      # Object confirmed stopped
    RESTARTED = "restarted"  # Stop-then-start completed

@dataclass(frozen=True)
class SyncResult:
    operation: SyncOperation
    polls: int                # Number of status polls issued
    elapsed_seconds: float    # Wall-clock time from command to confirmation
```

Polling is controlled by a `SyncConfig` dataclass:

```python
@dataclass(frozen=True)
class SyncConfig:
    timeout_seconds: float = 30.0      # Max wait before raising
    poll_interval_seconds: float = 1.0  # Seconds between polls
```

If the object does not reach the target state within the timeout,
`MQRESTTimeoutError` is raised.

## Basic usage

```python
from pymqrest import MQRESTSession, SyncConfig, SyncOperation
from pymqrest.auth import BasicAuth

session = MQRESTSession(
    rest_base_url="https://localhost:9443/ibmmq/rest/v2",
    qmgr_name="QM1",
    credentials=BasicAuth("mqadmin", "mqadmin"),
    verify_tls=False,
)

# Start a channel and wait until it is RUNNING
result = session.start_channel_sync("TO.PARTNER")
assert result.operation is SyncOperation.STARTED
print(f"Channel running after {result.polls} poll(s), {result.elapsed_seconds:.1f}s")

# Stop a listener and wait until it is STOPPED
result = session.stop_listener_sync("TCP.LISTENER")
assert result.operation is SyncOperation.STOPPED
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
print(f"Restarted in {result.elapsed_seconds:.1f}s ({result.polls} total polls)")
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

All methods share the same signature:

```python
def start_channel_sync(
    self,
    name: str,
    *,
    config: SyncConfig | None = None,
) -> SyncResult:
```

The `config` parameter is keyword-only for API clarity.

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
in the same {doc}`mapping pipeline </mapping-pipeline>` as all other
command methods. The status key is checked using both the mapped
`snake_case` name and the raw MQSC name, so polling works correctly
regardless of whether mapping is enabled or disabled.

## Provisioning example

The sync methods pair naturally with the
{doc}`ensure methods </ensure-methods>` for end-to-end provisioning:

```python
from pymqrest import SyncConfig

config = SyncConfig(timeout_seconds=60.0)

# Ensure objects exist
session.ensure_listener("TCP.LISTENER", request_parameters={
    "transport_type": "TCP",
    "port": 1415,
    "start_mode": "MQSVC_CONTROL_Q_MGR",
})
session.ensure_channel("PARTNER.SVRCONN", request_parameters={
    "channel_type": "SVRCONN",
    "description": "Partner application channel",
})

# Start them synchronously
session.start_listener_sync("TCP.LISTENER", config=config)
session.start_channel_sync("PARTNER.SVRCONN", config=config)

print("Infrastructure ready")
```

## Rolling restart example

Restart all server-connection channels with error handling:

```python
from pymqrest import MQRESTTimeoutError, SyncConfig

channels = ["APP.SVRCONN", "ADMIN.SVRCONN", "PARTNER.SVRCONN"]
config = SyncConfig(timeout_seconds=30.0, poll_interval_seconds=2.0)

for name in channels:
    try:
        result = session.restart_channel(name, config=config)
        print(f"{name}: restarted in {result.elapsed_seconds:.1f}s")
    except MQRESTTimeoutError as err:
        print(f"{name}: timed out after {err.elapsed:.1f}s")
```
