# Session

## Overview

The `MQRESTSession` class is the main entry point for interacting with
IBM MQ via the REST API. A session encapsulates connection details,
authentication, attribute mapping configuration, and diagnostic state. It
inherits MQSC command methods from `MQRESTCommandMixin` (see
[commands](commands.md)) and idempotent ensure methods from
`MQRESTEnsureMixin` (see [ensure](ensure.md)).

## Creating a session

```python
from pymqrest import MQRESTSession
from pymqrest.auth import LTPAAuth

session = MQRESTSession(
    rest_base_url="https://localhost:9443/ibmmq/rest/v2",
    qmgr_name="QM1",
    credentials=LTPAAuth("mqadmin", "mqadmin"),
)
```

The constructor validates all required fields and constructs the transport,
mapping data, and authentication state at creation time. Errors in
configuration (e.g. invalid mapping overrides) are caught immediately.

## Constructor parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `rest_base_url` | Required | Base URL of the MQ REST API (e.g. `https://host:9443/ibmmq/rest/v2`) |
| `qmgr_name` | Required | Target queue manager name |
| `credentials` | Required | Authentication credentials (`LTPAAuth`, `BasicAuth`, or `CertificateAuth`) |
| `gateway_qmgr` | Optional | Gateway queue manager for remote routing |
| `map_attributes` | Optional | Enable/disable attribute mapping (default: `True`) |
| `mapping_strict` | Optional | Strict or lenient mapping mode (default: `True`) |
| `mapping_overrides` | Optional | Custom mapping overrides (sparse merge) |
| `verify_tls` | Optional | Verify server TLS certificates (default: `True`) |
| `timeout` | Optional | Default request timeout in seconds |
| `csrf_token` | Optional | Custom CSRF token value |
| `transport` | Optional | Custom transport implementation |

### Minimal example

```python
session = MQRESTSession(
    rest_base_url="https://localhost:9443/ibmmq/rest/v2",
    qmgr_name="QM1",
    credentials=LTPAAuth("mqadmin", "mqadmin"),
)
```

### Full example

```python
session = MQRESTSession(
    rest_base_url="https://mq-server.example.com:9443/ibmmq/rest/v2",
    qmgr_name="QM2",
    credentials=LTPAAuth("mqadmin", "mqadmin"),
    gateway_qmgr="QM1",
    map_attributes=True,
    mapping_strict=False,
    mapping_overrides=overrides,
    verify_tls=True,
    timeout=30,
)
```

## Command methods

The session provides ~144 command methods, one for each MQSC verb + qualifier
combination. See [Commands](commands.md) for the full list.

```python
# DISPLAY commands return a list of dicts
queues = session.display_queue("APP.*")

# Queue manager singletons return a single dict or None
qmgr = session.display_qmgr()

# Non-DISPLAY commands return None (raise on error)
session.define_qlocal("MY.QUEUE", request_parameters={"max_queue_depth": 50000})
session.delete_queue("MY.QUEUE")
```

## Ensure methods

The session provides 16 ensure methods for declarative object management. Each
method implements an idempotent upsert: DEFINE if the object does not exist,
ALTER only the attributes that differ, or no-op if already correct.

```python
result = session.ensure_qlocal("MY.QUEUE",
    request_parameters={"max_queue_depth": 50000})
# result.action is EnsureAction.CREATED, UPDATED, or UNCHANGED
```

See [Ensure Methods](../ensure-methods.md) for detailed usage and the full list
of available ensure methods.

## Diagnostic state

The session retains the most recent request and response for inspection. This
is useful for debugging command failures or understanding what the library sent
to the MQ REST API:

```python
session.display_queue("MY.QUEUE")

session.last_command_payload    # the JSON sent to MQ (dict)
session.last_response_payload   # the parsed JSON response (dict)
session.last_http_status        # HTTP status code (int)
session.last_response_text      # raw response body (str)
```

### Diagnostic attributes

| Attribute | Type | Description |
| --- | --- | --- |
| `qmgr_name` | `str` | Queue manager name |
| `gateway_qmgr` | `str \| None` | Gateway queue manager (or `None`) |
| `last_http_status` | `int` | HTTP status code from last command |
| `last_response_text` | `str` | Raw response body from last command |
| `last_response_payload` | `dict` | Parsed response from last command |
| `last_command_payload` | `dict` | Command sent in last request |

## Transport

See [Transport](transport.md) for the transport protocol, response type,
and mock transport examples.

## API reference

::: pymqrest.session.MQRESTSession
    options:
      members: true
      show_bases: true
