# pymqrest

Python wrapper for the IBM MQ administrative REST API.

`pymqrest` provides typed Python methods for every MQSC command exposed
by the IBM MQ 9.4 `runCommandJSON` REST endpoint. Attribute names are
automatically translated between Python `snake_case` and native MQSC
parameter names, so you work with Pythonic identifiers throughout.

## Table of Contents

- [Installation](#installation)
- [Quick start](#quick-start)
- [API overview](#api-overview)
- [Documentation](#documentation)
- [Development](#development)
- [License](#license)

## Installation

```bash
pip install pymqrest
```

Requires Python 3.12+.

## Quick start

```python
from pymqrest import MQRESTSession, LTPAAuth

session = MQRESTSession(
    rest_base_url="https://localhost:9443/ibmmq/rest/v2",
    qmgr_name="QM1",
    credentials=LTPAAuth("mqadmin", "mqadmin"),
    verify_tls=False,
)

# Query the queue manager
qmgr = session.display_qmgr()
print(qmgr["queue_manager_name"])

# List all local queues
queues = session.display_qlocal(name="*")
for q in queues:
    print(q["queue_name"], q.get("current_queue_depth", 0))

# Idempotent object management
result = session.ensure_qlocal(
    name="APP.REQUESTS",
    request_parameters={"max_queue_depth": "50000"},
)
print(result.action)  # EnsureAction.CREATED, UPDATED, or UNCHANGED
```

## API overview

### Session

`MQRESTSession` manages authentication, connection settings, and
attribute mapping. All command methods are called directly on the
session object.

```python
MQRESTSession(
    rest_base_url="https://host:9443/ibmmq/rest/v2",
    qmgr_name="QM1",
    credentials=LTPAAuth("user", "pass"),  # or CertificateAuth / BasicAuth
    map_attributes=True,      # snake_case <-> MQSC translation (default)
    mapping_strict=True,      # raise on unknown attributes (default)
    verify_tls=True,          # TLS certificate verification (default)
    timeout_seconds=30.0,     # HTTP request timeout (default)
)
```

### Commands

Over 130 generated methods cover the MQSC command set:

| Verb | Methods | Returns | Example |
| --- | --- | --- | --- |
| `display_*` | 44 | `list[dict]` or `dict \| None` | `session.display_qlocal(name="*")` |
| `define_*` | 19 | `None` | `session.define_qlocal(name="Q1")` |
| `alter_*` | 17 | `None` | `session.alter_qlocal(name="Q1", ...)` |
| `delete_*` | 16 | `None` | `session.delete_qlocal(name="Q1")` |
| Other | 41 | `None` | `start_channel`, `stop_listener`, `clear_qlocal`, ... |

All methods accept optional `request_parameters` and
`response_parameters` dicts. `DISPLAY` commands default to returning
all attributes.

### Ensure methods

Idempotent `ensure_*` methods implement a declarative upsert pattern
for 15 object types (queues, channels, topics, listeners, and more):

- **DEFINE** when the object does not exist
- **ALTER** only the attributes that differ
- **No-op** when all specified attributes already match

Returns an `EnsureResult` whose `action` attribute is
`EnsureAction.CREATED`, `UPDATED`, or `UNCHANGED`. When the action is
`UPDATED`, `result.changed` contains the attribute names that differed.

### Attribute mapping

When `map_attributes=True` (the default), attribute names and values
are translated automatically:

| Direction | From | To | Example |
| --- | --- | --- | --- |
| Request | `max_queue_depth` | `MAXDEPTH` | snake_case to MQSC |
| Response | `MAXDEPTH` | `max_queue_depth` | MQSC to snake_case |

Disable per-session (`map_attributes=False`) or per-call for raw MQSC
parameter access.

### Authentication

Three credential types are supported:

- `CertificateAuth(cert_path, key_path)` — mutual TLS client
  certificates
- `LTPAAuth(username, password)` — LTPA token login (automatic at
  session creation)
- `BasicAuth(username, password)` — HTTP Basic authentication

## Documentation

Full documentation: <https://wphillipmoore.github.io/pymqrest/>

## Development

```bash
uv sync --group dev
uv run python3 scripts/dev/validate_local.py
```

## License

GPL-3.0-or-later. See `LICENSE`.
