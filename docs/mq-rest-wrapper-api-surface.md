# MQ REST API surface (draft)

## Table of Contents

- [Purpose](#purpose)
- [Scope](#scope)
- [Public class](#public-class)
- [Method conventions](#method-conventions)
- [Session lifecycle](#session-lifecycle)
- [Queue manager methods](#queue-manager-methods)
- [Queue methods](#queue-methods)
- [Channel methods](#channel-methods)
- [Internal bridge to metadata](#internal-bridge-to-metadata)
- [Future extensions](#future-extensions)

## Purpose

Define the developer-facing API surface for the MQ administrative REST wrapper.
This is a living draft focused on names, signatures, return shapes, and defaults.

## Scope

- IBM MQ administrative REST `runCommandJSON` endpoint.
- MQSC-aligned method names and signatures only.
- Public API shape; implementation details live elsewhere.

## Public class

`MQRESTSession` is a placeholder class name. The final class name will be
selected later, but the public surface described here should remain stable.

## Method conventions

- One public method per MQSC command.
- Method names match MQSC commands and qualifiers, for example
  `display_queue`, `define_qlocal`, `delete_channel`.
- Display-style methods return objects; other command methods return `None` on
  success and raise on error.
- Define-style methods may later return the created object once validated
  against live MQ behavior; treat current `None` returns as provisional.
- Most display methods return a list of objects; queue manager display-style
  methods return a single object or `None` as a convenience.
- `request_parameters` is optional and provides MQSC key/value pairs passed to
  the command.
- `response_parameters` is optional and defaults to `["all"]` when omitted.
  It is a list of MQSC attribute names to return in the response.

Type aliases used below are illustrative and may tighten as metadata typing
stabilizes:

```python
from typing import Any

RequestParametersType = dict[str, Any]
ResponseParametersType = list[str]
ResponseObject = object
```

## Session lifecycle

```python
class MQRESTSession:
    def __init__(self, ...) -> None:
        """Args TBD, but only values needed to configure a requests session and login."""
```

Draft inputs (non-binding):

- Connection: host, port, base path.
- Credentials: username, password.
- Session options: TLS verify, timeouts, connection pooling.

## Queue manager methods

Queue manager display-style commands return a single object or `None`.

```python
def display_qmgr(
    self,
    name: str | None = None,
    request_parameters: RequestParametersType | None = None,
    response_parameters: ResponseParametersType | None = None,
) -> ResponseObject | None:
    ...


def display_qmstatus(
    self,
    name: str | None = None,
    request_parameters: RequestParametersType | None = None,
    response_parameters: ResponseParametersType | None = None,
) -> ResponseObject | None:
    ...


def display_cmdserv(
    self,
    name: str | None = None,
    request_parameters: RequestParametersType | None = None,
    response_parameters: ResponseParametersType | None = None,
) -> ResponseObject | None:
    ...
```

## Queue methods

Queue display-style commands return a list of objects. The default name is
`"*"` when omitted.

```python
def display_queue(
    self,
    name: str | None = None,
    request_parameters: RequestParametersType | None = None,
    response_parameters: ResponseParametersType | None = None,
) -> list[ResponseObject]:
    ...
```

Queue definition and deletion commands return `None` on success:

```python
def define_qlocal(
    self,
    name: str,
    request_parameters: RequestParametersType | None = None,
    response_parameters: ResponseParametersType | None = None,
) -> None:
    ...


def define_qremote(
    self,
    name: str,
    request_parameters: RequestParametersType | None = None,
    response_parameters: ResponseParametersType | None = None,
) -> None:
    ...


def define_qalias(
    self,
    name: str,
    request_parameters: RequestParametersType | None = None,
    response_parameters: ResponseParametersType | None = None,
) -> None:
    ...


def define_qmodel(
    self,
    name: str,
    request_parameters: RequestParametersType | None = None,
    response_parameters: ResponseParametersType | None = None,
) -> None:
    ...


def delete_queue(
    self,
    name: str,
    request_parameters: RequestParametersType | None = None,
    response_parameters: ResponseParametersType | None = None,
) -> None:
    ...
```

## Channel methods

Channel display-style commands return a list of objects. The default name is
`"*"` when omitted.

```python
def display_channel(
    self,
    name: str | None = None,
    request_parameters: RequestParametersType | None = None,
    response_parameters: ResponseParametersType | None = None,
) -> list[ResponseObject]:
    ...
```

Channel definition and deletion commands return `None` on success:

```python
def define_channel(
    self,
    name: str,
    request_parameters: RequestParametersType | None = None,
    response_parameters: ResponseParametersType | None = None,
) -> None:
    ...


def delete_channel(
    self,
    name: str,
    request_parameters: RequestParametersType | None = None,
    response_parameters: ResponseParametersType | None = None,
) -> None:
    ...
```

`define_channel` expects `request_parameters` to include `channel_type`; the
client does not validate required parameters yet.

## MQSC namespace coverage

`MQRESTSession` now exposes wrappers for every MQSC command listed in
`docs/mqsc-pcf-command-mapping.md`. Method names follow the pattern
`<verb>_<qualifier>` with tokens lowercased and spaces converted to underscores.

All generated methods accept:

- `name: str | None = None`
- `request_parameters: RequestParametersType | None = None`
- `response_parameters: ResponseParametersType | None = None`

Return shapes follow these rules:

- `DISPLAY` commands return a list of objects.
- `display_qmgr`, `display_qmstatus`, and `display_cmdserv` return a single
  object or `None`.
- Non-`DISPLAY` commands return `None`.

Queue/channel convenience methods keep their existing defaults (for example,
`display_queue` and `display_channel` default `name` to `"*"`).

## Internal bridge to metadata

Public methods are thin wrappers over an internal command executor. The
internal executor accepts MQSC command data and uses collected metadata to
translate and validate request parameters before calling the REST endpoint.

Constraints for the bridge layer:

- Default `response_parameters` to `["all"]` when omitted.
- Preserve the return shapes described above (list vs single object).

## Future extensions

- Expose optional response parameter selection once metadata coverage is
  validated.
- Add additional MQSC qualifiers and commands to expand the public namespace.
- Rename `PYMQRESTSession` to a final class name without changing signatures.
