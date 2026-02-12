# Getting started

## Installation

Install `pymqrest` from source using [uv](https://docs.astral.sh/uv/):

```bash
uv add pymqrest
```

Or with pip:

```bash
pip install pymqrest
```

## Creating a session

All interaction with IBM MQ goes through an `MQRESTSession`. You need the
REST API base URL, queue manager name, and credentials:

```python
from pymqrest import MQRESTSession
from pymqrest.auth import LTPAAuth

session = MQRESTSession(
    rest_base_url="https://localhost:9443/ibmmq/rest/v2",
    qmgr_name="QM1",
    credentials=LTPAAuth("mqadmin", "mqadmin"),
    verify_tls=False,  # for local development only
)
```

## Running a command

Every MQSC command has a corresponding method on the session. Method names
follow the pattern `<verb>_<qualifier>` in lowercase:

```python
# DISPLAY QUEUE — returns a list of dicts
queues = session.display_queue(name="SYSTEM.*")

for queue in queues:
    print(queue["queue_name"], queue.get("current_depth"))
```

```python
# DISPLAY QMGR — returns a single dict or None
qmgr = session.display_qmgr()
if qmgr:
    print(qmgr["queue_manager_name"])
```

## Attribute mapping

By default, `pymqrest` maps between Python-friendly `snake_case` names and
MQSC parameter names. This applies to both request and response attributes:

```python
# With mapping enabled (default)
queues = session.display_queue(
    name="MY.QUEUE",
    response_parameters=["current_depth", "max_depth"],
)
# Returns: [{"queue_name": "MY.QUEUE", "current_depth": 0, "max_depth": 5000}]

# With mapping disabled
queues = session.display_queue(
    name="MY.QUEUE",
    response_parameters=["CURDEPTH", "MAXDEPTH"],
    map_attributes=False,
)
# Returns: [{"queue": "MY.QUEUE", "curdepth": 0, "maxdepth": 5000}]
```

Mapping can be disabled at the session level or per method call:

```python
# Disable mapping for the entire session
session = MQRESTSession(
    rest_base_url="https://localhost:9443/ibmmq/rest/v2",
    qmgr_name="QM1",
    credentials=LTPAAuth("mqadmin", "mqadmin"),
    map_attributes=False,
)
```

See {doc}`/mapping-pipeline` for a detailed explanation of how mapping works.

## Strict vs lenient mapping

By default, mapping runs in strict mode. Unknown attribute names or values
raise a `MappingError`. In lenient mode, unknown attributes pass through
unchanged:

```python
# Lenient mode — unknown attributes pass through
session = MQRESTSession(
    rest_base_url="https://localhost:9443/ibmmq/rest/v2",
    qmgr_name="QM1",
    credentials=LTPAAuth("mqadmin", "mqadmin"),
    mapping_strict=False,
)
```

## Custom mapping overrides

Sites with existing naming conventions can override individual entries in the
built-in mapping tables without forking or replacing them entirely. Pass a
`mapping_overrides` dict when creating the session:

```python
session = MQRESTSession(
    rest_base_url="https://localhost:9443/ibmmq/rest/v2",
    qmgr_name="QM1",
    credentials=LTPAAuth("mqadmin", "mqadmin"),
    verify_tls=False,
    mapping_overrides={
        "qualifiers": {
            "queue": {
                "response_key_map": {
                    "CURDEPTH": "queue_depth",        # override built-in "current_queue_depth"
                    "MAXDEPTH": "queue_max_depth",     # override built-in "max_queue_depth"
                },
            },
        },
    },
)

queues = session.display_queue(name="MY.QUEUE")
# Returns: [{"queue_depth": 0, "queue_max_depth": 5000, ...}]
```

Overrides are **sparse** — you only specify the entries you want to change. All
other mappings in the qualifier continue to work as normal. In the example above,
only `CURDEPTH` and `MAXDEPTH` are remapped; every other queue attribute keeps
its default `snake_case` name.

Request-side mappings work the same way:

```python
session = MQRESTSession(
    rest_base_url="https://localhost:9443/ibmmq/rest/v2",
    qmgr_name="QM1",
    credentials=LTPAAuth("mqadmin", "mqadmin"),
    verify_tls=False,
    mapping_overrides={
        "qualifiers": {
            "queue": {
                "request_key_map": {
                    "queue_depth": "CURDEPTH",     # use your name on the request side too
                },
                "response_key_map": {
                    "CURDEPTH": "queue_depth",     # and on the response side
                },
            },
        },
    },
)

# Now "queue_depth" works in WHERE filters, response_parameters, etc.
queues = session.display_queue(where="queue_depth GT 100")
```

Overrides support all five sub-maps per qualifier: `request_key_map`,
`request_value_map`, `request_key_value_map`, `response_key_map`, and
`response_value_map`. See {doc}`/mapping-pipeline` for details on how each
sub-map is used.

Invalid override structures raise `ValueError` or `TypeError` at session
construction time, so errors are caught early.

## Gateway queue manager

The MQ REST API is available on all supported IBM MQ platforms (Linux, AIX,
Windows, z/OS, and IBM i). pymqrest is developed and tested against the
**Linux** implementation only.

In enterprise environments, a **gateway queue manager** can route MQSC
commands to remote queue managers via MQ channels — the same mechanism used
by `runmqsc -w` and the MQ Console.

To use a gateway, pass `gateway_qmgr` when creating the session. The
`qmgr_name` parameter specifies the **target** (remote) queue manager, while
`gateway_qmgr` names the **local** queue manager whose REST API routes the
command:

```python
from pymqrest import MQRESTSession
from pymqrest.auth import BasicAuth

# Route commands to QM2 through QM1's REST API
session = MQRESTSession(
    rest_base_url="https://qm1-host:9443/ibmmq/rest/v2",
    qmgr_name="QM2",           # target queue manager
    credentials=BasicAuth("mqadmin", "mqadmin"),
    gateway_qmgr="QM1",        # local gateway queue manager
    verify_tls=False,
)

qmgr = session.display_qmgr()
# Returns QM2's queue manager attributes, routed through QM1
```

Prerequisites:

- The gateway queue manager must have a running REST API.
- MQ channels must be configured between the gateway and target queue managers.
- A QM alias (QREMOTE with empty RNAME) must map the target QM name to the
  correct transmission queue on the gateway.

## Error handling

`DISPLAY` commands return an empty list when no objects match. Queue manager
display methods return `None` when no match is found. Non-display commands
raise `MQRESTCommandError` on failure:

```python
from pymqrest.exceptions import MQRESTCommandError

# Empty list — no exception
result = session.display_queue(name="NONEXISTENT.*")
assert result == []

# Define raises on error
try:
    session.define_qlocal(name="MY.QUEUE")
except MQRESTCommandError as error:
    print(error)
    print(error.payload)  # full MQ response payload
```

## Diagnostic state

The session retains the most recent request and response for inspection:

```python
session.display_queue(name="MY.QUEUE")

print(session.last_command_payload)    # the JSON sent to MQ
print(session.last_response_payload)   # the parsed JSON response
print(session.last_http_status)        # HTTP status code
print(session.last_response_text)      # raw response body
```
