# Architecture

## Component overview

`pymqrest` is organized around four core components:

**MQRESTSession** (`session.py`)
: The main entry point. Owns authentication, base URL construction,
  request/response handling, and diagnostic state. Inherits generated
  command methods from `MQRESTCommandMixin`.

**MQRESTCommandMixin** (`commands.py`)
: Provides ~144 generated MQSC command methods. Each method is a thin
  wrapper that calls `_mqsc_command` with the correct command verb and
  qualifier.

**MQRESTEnsureMixin** (`ensure.py`)
: Provides 16 idempotent `ensure_*` methods for declarative object
  management. Each method checks current state with DISPLAY, then
  DEFINE, ALTER, or no-ops as needed. Returns an `EnsureResult` enum.
  `ensure_qmgr()` is a special singleton variant (no name, no DEFINE).
  See {doc}`/ensure-methods` for details.

**Mapping pipeline** (`mapping.py`, `mapping_data.py`)
: Bidirectional attribute translation between Python `snake_case` names
  and native MQSC parameter names. Includes key mapping (attribute names),
  value mapping (enumerated values), and key-value mapping (combined
  name+value translations).

**Exception hierarchy** (`exceptions.py`)
: Structured error types for transport failures, malformed responses,
  and MQSC command errors.

## Request lifecycle

Every MQSC command follows the same path through the system:

```text
Method call (e.g. display_queue)
  → _mqsc_command()
    → Map request attributes (snake_case → MQSC)
    → Map response parameter names
    → Map WHERE keyword
    → Build runCommandJSON payload
    → Transport POST
    → Parse JSON response
    → Extract commandResponse items
    → Flatten nested objects
    → Map response attributes (MQSC → snake_case)
  → Return list[dict]
```

### Build phase

1. The command method calls `_mqsc_command` with the MQSC verb (e.g.
   `DISPLAY`), qualifier (e.g. `QUEUE`), and user-supplied parameters.
2. If mapping is enabled, request attributes are translated from
   `snake_case` to MQSC parameter names via the qualifier's
   `request_key_map` and `request_value_map`.
3. Response parameter names are mapped similarly.
4. A `WHERE` clause keyword, if provided, is mapped through the same
   qualifier key maps.
5. The `runCommandJSON` payload is assembled and sent via the transport.

### Parse phase

1. The JSON response is parsed and validated.
2. Error codes (`overallCompletionCode`, `overallReasonCode`, per-item
   `completionCode`/`reasonCode`) are checked. Errors raise
   `MQRESTCommandError`.
3. The `parameters` dict is extracted from each `commandResponse` item.
4. Nested `objects` lists (e.g. from `DISPLAY CONN TYPE(HANDLE)`) are
   flattened into the parent parameter set.
5. If mapping is enabled, response attributes are translated from MQSC
   to `snake_case`.

## Transport abstraction

`MQRESTSession` does not call `requests` directly. Instead, it delegates
to a `MQRESTTransport` protocol:

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
library. Tests inject a mock transport to avoid network calls.

## Single-endpoint design

All MQSC operations go through a single REST endpoint:

```text
POST /ibmmq/rest/v2/admin/action/qmgr/{qmgr}/mqsc
```

The `runCommandJSON` payload specifies the MQSC verb, qualifier, object
name, parameters, and response parameters. This design means `pymqrest`
needs exactly one HTTP method and one URL pattern to cover all MQSC
commands.

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
