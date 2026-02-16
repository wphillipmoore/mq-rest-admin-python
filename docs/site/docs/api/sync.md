# Sync

## Overview

The sync module provides the types for the 9 synchronous start/stop/restart
methods on `MQRESTSession`. These methods wrap fire-and-forget `START` and
`STOP` commands with a polling loop that waits until the object reaches its
target state or the timeout expires.

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
result = session.start_channel_sync("TO.PARTNER")
result = session.start_channel_sync("TO.PARTNER", config=SyncConfig(timeout=60))
```

## Usage

```python
from pymqrest.sync import SyncConfig

result = session.start_channel_sync("TO.PARTNER")

match result.operation:
    case SyncOperation.STARTED:
        print(f"Running after {result.polls} polls")
    case SyncOperation.STOPPED:
        print("Stopped")
    case SyncOperation.RESTARTED:
        print(f"Restarted in {result.elapsed:.1f}s")
```

See [Sync Methods](../sync-methods.md) for the full conceptual overview,
polling behaviour, and the complete list of available methods.

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
