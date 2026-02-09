# Declarative object management

## The problem with ALTER

Every `alter_*()` call sends an `ALTER` command to the queue manager,
even when every specified attribute already matches the current state.
MQ updates `ALTDATE` and `ALTTIME` on every `ALTER`, regardless of
whether any values actually changed. This makes `ALTER` unsuitable for
declarative configuration management where idempotency matters — running
the same configuration twice should not corrupt audit timestamps.

## The ensure pattern

The `ensure_*()` methods implement a declarative upsert pattern:

1. **DEFINE** the object when it does not exist.
2. **ALTER** only the attributes that differ from the current state.
3. **Do nothing** when all specified attributes already match,
   preserving `ALTDATE` and `ALTTIME`.

Each call returns an `EnsureResult` indicating what action was taken:

```python
from pymqrest import EnsureResult

class EnsureResult(enum.Enum):
    CREATED = "created"    # Object did not exist, was defined
    UPDATED = "updated"    # Object existed, attributes were altered
    UNCHANGED = "unchanged"  # Object existed, no changes needed
```

## Basic usage

```python
from pymqrest import MQRESTSession, EnsureResult

session = MQRESTSession(
    rest_base_url="https://localhost:9443/ibmmq/rest/v2",
    qmgr_name="QM1",
    username="mqadmin",
    password="mqadmin",
    verify_tls=False,
)

# First call — queue does not exist yet
result = session.ensure_qlocal(
    "APP.REQUEST.Q",
    request_parameters={
        "max_q_depth": 50000,
        "description": "Application request queue",
    },
)
assert result is EnsureResult.CREATED

# Second call — same attributes, nothing to change
result = session.ensure_qlocal(
    "APP.REQUEST.Q",
    request_parameters={
        "max_q_depth": 50000,
        "description": "Application request queue",
    },
)
assert result is EnsureResult.UNCHANGED

# Third call — description changed, only that attribute is altered
result = session.ensure_qlocal(
    "APP.REQUEST.Q",
    request_parameters={
        "max_q_depth": 50000,
        "description": "Updated request queue",
    },
)
assert result is EnsureResult.UPDATED
```

## Comparison logic

The ensure methods compare only the attributes the caller passes in
`request_parameters` against the current state returned by `DISPLAY`.
Attributes not specified by the caller are ignored.

Comparison is:

- **Case-insensitive** — `"ENABLED"` matches `"enabled"`.
- **Type-normalizing** — integer `5000` matches string `"5000"`.
- **Whitespace-trimming** — `" YES "` matches `"YES"`.

An attribute present in `request_parameters` but absent from the
`DISPLAY` response is treated as changed and included in the `ALTER`.

## Selective ALTER

When an update is needed, only the changed attributes are sent in the
`ALTER` command. Attributes that already match are excluded from the
request. This minimizes the scope of each `ALTER` to the strict delta.

## Available methods

Each method targets a specific MQ object type with the correct
MQSC qualifier triple (DISPLAY / DEFINE / ALTER):

| Method | Object type | DISPLAY | DEFINE | ALTER |
| --- | --- | --- | --- | --- |
| `ensure_qmgr()` | Queue manager | `QMGR` | — | `QMGR` |
| `ensure_qlocal()` | Local queue | `QUEUE` | `QLOCAL` | `QLOCAL` |
| `ensure_qremote()` | Remote queue | `QUEUE` | `QREMOTE` | `QREMOTE` |
| `ensure_qalias()` | Alias queue | `QUEUE` | `QALIAS` | `QALIAS` |
| `ensure_qmodel()` | Model queue | `QUEUE` | `QMODEL` | `QMODEL` |
| `ensure_channel()` | Channel | `CHANNEL` | `CHANNEL` | `CHANNEL` |
| `ensure_authinfo()` | Auth info | `AUTHINFO` | `AUTHINFO` | `AUTHINFO` |
| `ensure_listener()` | Listener | `LISTENER` | `LISTENER` | `LISTENER` |
| `ensure_namelist()` | Namelist | `NAMELIST` | `NAMELIST` | `NAMELIST` |
| `ensure_process()` | Process | `PROCESS` | `PROCESS` | `PROCESS` |
| `ensure_service()` | Service | `SERVICE` | `SERVICE` | `SERVICE` |
| `ensure_topic()` | Topic | `TOPIC` | `TOPIC` | `TOPIC` |
| `ensure_sub()` | Subscription | `SUB` | `SUB` | `SUB` |
| `ensure_stgclass()` | Storage class | `STGCLASS` | `STGCLASS` | `STGCLASS` |
| `ensure_comminfo()` | Comm info | `COMMINFO` | `COMMINFO` | `COMMINFO` |
| `ensure_cfstruct()` | CF structure | `CFSTRUCT` | `CFSTRUCT` | `CFSTRUCT` |

Most methods share the same signature:

```python
def ensure_qlocal(
    self,
    name: str,
    request_parameters: Mapping[str, object] | None = None,
) -> EnsureResult:
```

`response_parameters` is not exposed — the ensure logic always requests
`["all"]` internally so it can compare the full current state.

### Queue manager (singleton)

`ensure_qmgr()` has no `name` parameter because the queue manager is a
singleton that always exists.  It can only return `UPDATED` or
`UNCHANGED` (never `CREATED`):

```python
def ensure_qmgr(
    self,
    request_parameters: Mapping[str, object] | None = None,
) -> EnsureResult:
```

This makes it ideal for asserting queue manager-level settings such as
statistics, monitoring, events, and logging attributes without
corrupting `ALTDATE`/`ALTTIME` on every run.

## Attribute mapping

The ensure methods participate in the same
{doc}`mapping pipeline </mapping-pipeline>` as all other command methods.
Pass `snake_case` attribute names in `request_parameters` and the
mapping layer translates them to MQSC names for the DISPLAY, DEFINE,
and ALTER commands automatically.

## Configuration management example

The ensure pattern is designed for scripts that declare desired state:

```python
def configure_queue_manager(session):
    """Ensure queue manager attributes are set for production."""
    result = session.ensure_qmgr(request_parameters={
        "statistics_queue": "on",
        "statistics_channel": "on",
        "monitoring_queue": "medium",
        "monitoring_channel": "medium",
    })
    print(f"Queue manager: {result.value}")

    queues = {
        "APP.REQUEST.Q": {"max_q_depth": 50000, "def_persistence": "yes"},
        "APP.REPLY.Q": {"max_q_depth": 10000, "def_persistence": "no"},
        "APP.DLQ": {"max_q_depth": 100000, "def_persistence": "yes"},
    }

    for name, attrs in queues.items():
        result = session.ensure_qlocal(name, request_parameters=attrs)
        print(f"{name}: {result.value}")
```

Running this script repeatedly produces no side effects when the
configuration is already correct. Only genuine changes trigger `ALTER`
commands, keeping `ALTDATE`/`ALTTIME` accurate.
