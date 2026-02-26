# Architecture

## Component overview

--8<-- "architecture/component-overview.md"

In the Python implementation, the core components map to these modules:

- **`MQRESTSession`** (`session.py`): The main entry point. Owns
  authentication, base URL construction, request/response handling, and
  diagnostic state. Inherits generated command methods from
  `MQRESTCommandMixin`.
- **`MQRESTCommandMixin`** (`commands.py`): Provides ~144 generated MQSC
  command methods. Each method is a thin wrapper that calls `_mqsc_command`
  with the correct command verb and qualifier.
- **`MQRESTEnsureMixin`** (`ensure.py`): Provides 16 idempotent `ensure_*`
  methods for declarative object management. `ensure_qmgr()` is a special
  singleton variant (no name, no DEFINE).
- **Mapping pipeline** (`mapping.py`, `mapping_data.py`): Bidirectional
  attribute translation between Python `snake_case` names and native MQSC
  parameter names. See the [mapping pipeline](mapping-pipeline.md) for
  details.
- **Exception hierarchy** (`exceptions.py`): Structured error types rooted
  at `MQRESTError`. All exceptions carry diagnostic context.

## Request lifecycle

--8<-- "architecture/request-lifecycle.md"

In Python, the command dispatcher is the internal `_mqsc_command()` method on
`MQRESTSession`. Every public command method (e.g. `display_queue()`,
`define_qlocal()`) delegates to it with the appropriate verb and qualifier.

The session retains diagnostic state from the most recent command for
inspection:

```python
session.display_queue("MY.QUEUE")

session.last_command_payload    # the JSON sent to MQ
session.last_response_payload   # the parsed JSON response
session.last_http_status        # HTTP status code
session.last_response_text      # raw response body
```

## Transport abstraction

--8<-- "architecture/transport-abstraction.md"

In Python, the transport is defined by the `MQRESTTransport` protocol:

```python
class MQRESTTransport(Protocol):
    def post_json(
        self,
        url: str,
        payload: Mapping[str, object],
        *,
        headers: Mapping[str, str],
        timeout_seconds: float | None,
        verify_tls: bool,
    ) -> TransportResponse: ...
```

The default implementation, `RequestsTransport`, wraps the `requests`
library.

For testing, inject a mock transport:

```python
from unittest.mock import MagicMock

mock_transport = MagicMock(spec=MQRESTTransport)
mock_transport.post_json.return_value = TransportResponse(
    status_code=200,
    text='{"commandResponse": []}',
    headers={},
)

session = MQRESTSession(
    rest_base_url="https://localhost:9443/ibmmq/rest/v2",
    qmgr_name="QM1",
    credentials=LTPAAuth("admin", "passw0rd"),
    transport=mock_transport,
)
```

This makes the entire command pipeline testable without an MQ server.

## Single-endpoint design

--8<-- "architecture/single-endpoint-design.md"

In Python, this means every command method on `MQRESTSession` ultimately calls
the same `post_json()` method on the transport with the same URL pattern. The
only variation is the JSON payload content.

## Gateway routing

--8<-- "architecture/gateway-routing.md"

In Python, configure gateway routing via the `gateway_qmgr` parameter:

```python
session = MQRESTSession(
    rest_base_url="https://qm1-host:9443/ibmmq/rest/v2",
    qmgr_name="QM2",           # target (remote) queue manager
    credentials=LTPAAuth("mqadmin", "mqadmin"),
    gateway_qmgr="QM1",        # local gateway queue manager
)
```

## Zero runtime dependencies

The library uses only the Python standard library plus `requests` for HTTP.
No other runtime dependencies are required.

## Generated command methods

The 144 command methods in `MQRESTCommandMixin` are generated from
`MAPPING_DATA["commands"]` by `scripts/dev/generate_commands.py`. Each
method:

- Accepts `name`, `request_parameters`, `response_parameters`, and
  `where` (for DISPLAY commands).
- Calls `self._mqsc_command()` with the correct verb and qualifier.
- Returns `list[dict[str, object]]` for DISPLAY commands, `None` for
  others.

Queue manager commands (`DISPLAY QMGR`, `DISPLAY QMSTATUS`, etc.)
have singleton helpers that return `dict | None` instead of a list.

## Ensure pipeline

See [ensure](api/ensure.md) for details on the idempotent
create-or-update pipeline.

## Sync pipeline

See [sync](api/sync.md) for details on the synchronous
polling pipeline.
