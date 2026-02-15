# Exceptions

All exceptions inherit from `MQRESTError`.

```text
Exception
└── MQRESTError
    ├── MQRESTAuthError        — authentication failures
    ├── MQRESTTransportError   — network/connection failures
    ├── MQRESTResponseError    — malformed responses
    ├── MQRESTCommandError     — MQSC command failures
    └── MQRESTTimeoutError     — sync operation timeouts
```

## MQRESTError

The base exception class. All library exceptions inherit from this class.

::: pymqrest.exceptions.MQRESTError
    options:
      show_bases: true

## MQRESTTransportError

Thrown when the HTTP request fails at the network level — connection refused,
DNS resolution failure, TLS handshake error, etc.

```python
from pymqrest.exceptions import MQRESTTransportError

try:
    session.display_queue("MY.QUEUE")
except MQRESTTransportError as err:
    print(f"Cannot reach MQ: {err}")
    print(f"Cause: {err.__cause__}")
```

::: pymqrest.exceptions.MQRESTTransportError
    options:
      members: true
      show_bases: true

## MQRESTResponseError

Thrown when the HTTP request succeeds but the response cannot be parsed —
invalid JSON, missing expected fields, unexpected response structure.

::: pymqrest.exceptions.MQRESTResponseError
    options:
      members: true
      show_bases: true

## MQRESTAuthError

Thrown when authentication or authorization fails — invalid credentials,
expired tokens, insufficient permissions (HTTP 401/403).

```python
from pymqrest.exceptions import MQRESTAuthError

try:
    session.display_qmgr()
except MQRESTAuthError as err:
    print(f"Authentication failed: {err}")
```

::: pymqrest.exceptions.MQRESTAuthError
    options:
      members: true
      show_bases: true

## MQRESTCommandError

Thrown when the MQSC command returns a non-zero completion or reason code. This
is the most commonly caught exception — it indicates the command was delivered
to MQ but the queue manager rejected it.

```python
from pymqrest.exceptions import MQRESTCommandError

try:
    session.define_qlocal("MY.QUEUE")
except MQRESTCommandError as err:
    print(f"Command failed: {err}")
    print(f"Response payload: {err.payload}")
```

!!! note
    For DISPLAY commands with no matches, MQ returns reason code 2085
    (MQRC_UNKNOWN_OBJECT_NAME). The library treats this as an empty list
    rather than raising an exception.

::: pymqrest.exceptions.MQRESTCommandError
    options:
      members: true
      show_bases: true

## MQRESTTimeoutError

Thrown when a polling operation exceeds the configured timeout duration.

```python
from pymqrest.exceptions import MQRESTTimeoutError

try:
    session.start_channel_sync("BROKEN.CHL")
except MQRESTTimeoutError as err:
    print(f"Object: {err.name}")
    print(f"Operation: {err.operation}")
    print(f"Elapsed: {err.elapsed:.1f}s")
```

::: pymqrest.exceptions.MQRESTTimeoutError
    options:
      members: true
      show_bases: true

## Catching exceptions

Catch the base class for broad error handling, or specific subtypes for
targeted recovery:

```python
from pymqrest.exceptions import (
    MQRESTCommandError,
    MQRESTAuthError,
    MQRESTTransportError,
    MQRESTError,
)

try:
    session.define_qlocal("MY.QUEUE", request_parameters={"max_queue_depth": 50000})
except MQRESTCommandError as err:
    # MQSC command failed — check reason code in payload
    print(f"Command failed: {err}")
except MQRESTAuthError:
    # Credentials rejected
    print("Not authorized")
except MQRESTTransportError:
    # Network error
    print("Connection failed")
except MQRESTError as err:
    # Catch-all for any other library exception
    print(f"Unexpected error: {err}")
```
