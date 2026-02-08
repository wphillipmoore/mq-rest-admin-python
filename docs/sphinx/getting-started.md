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

session = MQRESTSession(
    rest_base_url="https://localhost:9443/ibmmq/rest/v2",
    qmgr_name="QM1",
    username="mqadmin",
    password="mqadmin",
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
    username="mqadmin",
    password="mqadmin",
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
    username="mqadmin",
    password="mqadmin",
    mapping_strict=False,
)
```

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
