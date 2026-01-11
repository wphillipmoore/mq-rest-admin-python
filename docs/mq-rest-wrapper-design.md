# MQ REST wrapper design

This document defines the design and initial delivery plan for a Python wrapper around the IBM MQ administrative REST API.

## Table of Contents
- [Purpose](#purpose)
- [Scope](#scope)
- [Goals](#goals)
- [Non-goals](#non-goals)
- [Architecture](#architecture)
- [Public API](#public-api)
  - [Session lifecycle](#session-lifecycle)
  - [Method signatures](#method-signatures)
  - [Queue methods](#queue-methods)
  - [Channel methods](#channel-methods)
  - [Queue manager methods](#queue-manager-methods)
- [Mapping and typing](#mapping-and-typing)
  - [Mapping schema](#mapping-schema)
  - [Dummy tables](#dummy-tables)
- [Error handling](#error-handling)
- [Testing and development](#testing-and-development)
  - [Integration test matrix](#integration-test-matrix)
- [Milestones](#milestones)
- [References](#references)

## Purpose
Define a stable, minimal design for a Python wrapper that exposes IBM MQ administrative REST capabilities through MQSC-aligned methods, with predictable error handling and optional attribute mapping.

## Scope
- IBM MQ 9.4 administrative REST API.
- `runCommandJSON` endpoint for all MQSC operations.
- Objects: queues, channels, and the queue manager.
- Authentication: basic auth only for the first release.

## Goals
- Provide method names that map 1:1 to MQSC commands.
- Offer consistent defaults and return shapes across methods.
- Wrap response dictionaries in typed, dict-like objects.
- Support optional MQSC -> PCF -> snake_case attribute mapping.
- Capture response metadata for diagnostics.

## Non-goals
- Full MQSC coverage beyond queues, channels, and queue manager.
- Non-basic auth modes, proxy support, or advanced TLS configuration.
- Abstracted workflows that hide MQSC semantics.

## Architecture
- `MQRESTSession` owns authentication, base URL construction, and request/response handling.
- `_run_command_json` is the single internal executor for MQSC commands via `runCommandJSON`.
- Public methods are thin wrappers over `_run_command_json` with method-specific defaults.
- The most recent response payload is retained for inspection.

```python
# Signature sketch, not final typing.
def _run_command_json(
    command: str,
    qualifier: str,
    name: str | None = None,
    parameters: dict[str, object] | None = None,
    response_parameters: list[str] | None = None,
) -> list[object]:
    ...
```

## Public API

### Session lifecycle
- `MQRESTSession(...)` accepts hostname, port, credentials, and mapping options.
- Session creation authenticates and fails fast on invalid credentials.
- Mapping options are set at session creation and can be overridden per call.

### Method signatures
Signature sketches are intentionally minimal and focus on method contracts rather than final typing.

```python
ParameterType = dict[str, object]
ResponseParameterType = list[str]

def display_queue(
    name: str | None = None,
    parameters: ParameterType | None = None,
    response_parameters: ResponseParameterType | None = None,
    *,
    map_attributes: bool | None = None,
) -> list[Queue]:
    ...

def define_qlocal(
    name: str,
    parameters: ParameterType | None = None,
    *,
    map_attributes: bool | None = None,
) -> None:
    ...

def define_channel(
    name: str,
    channel_type: str,
    parameters: ParameterType | None = None,
    *,
    map_attributes: bool | None = None,
) -> None:
    ...

def display_qmgr(
    name: str | None = None,
    parameters: ParameterType | None = None,
    response_parameters: ResponseParameterType | None = None,
    *,
    map_attributes: bool | None = None,
) -> QMgr | None:
    ...
```

Conventions:
- `parameters` and `response_parameters` use the mapped namespace when mapping is enabled.
- `map_attributes=None` means use the session default; `True` or `False` overrides per call.
- Define and delete methods return `None` on success.

### Queue methods
- `define_qlocal`, `define_qremote`, `define_qalias`, `define_qmodel`.
- `display_queue` returns a list; empty list when no objects match.
- `delete_queue` raises on failure.
- Queue types supported: `QLOCAL`, `QREMOTE`, `QALIAS`, `QMODEL`.

### Channel methods
- `define_channel` requires `channel_type`.
- `display_channel` returns a list; empty list when no objects match.
- `delete_channel` raises on failure.
- Channel types supported: `SVRCONN`, `SDR`, `RCVR`, `RQR`, `CLNTCONN`, `CLUSRCVR`, `CLUSSDR`.

### Queue manager methods
- `display_qmgr` returns a single dict-like object.
- Missing queue manager returns `None` without raising.

## Mapping and typing
- Attribute mapping pipeline: MQSC -> PCF -> snake_case.
- Mapping is enabled by default, with opt-out at session init and per-method.
- Initial mapping tables are placeholders for scaffolding and will be iterated using real MQ responses.
- Response objects provide dict-like access and typed attributes; they can be reused as inputs for define or delete methods by extracting attributes.

### Mapping schema
The mapping layer uses a simple schema that is easy to load, validate, and evolve. The schema is intentionally minimal so it can be refined once real MQ responses are observed.

```yaml
version: 1
qualifiers:
  queue:
    attributes:
      - mqsc: CURDEPTH
        pcf: CurrentQDepth
        snake: current_q_depth
        values: {}
      - mqsc: DEFPSIST
        pcf: DefPersistence
        snake: def_persistence
        values:
          DEF: def
          NOTFIXED: not_fixed
  channel:
    attributes:
      - mqsc: CHLTYPE
        pcf: ChannelType
        snake: channel_type
        values: {}
  qmgr:
    attributes:
      - mqsc: QMNAME
        pcf: QMgrName
        snake: qmgr_name
        values: {}
```

Notes:
- `mqsc` is the MQSC attribute name; `pcf` is the PCF attribute; `snake` is the preferred external name.
- `values` maps MQSC value tokens to snake_case equivalents, if needed.
- Missing attributes fall back to pass-through behavior unless strict validation is enabled.

### Dummy tables
Initial tables are placeholders to validate the mapping pipeline, not authoritative mappings. They are expected to change once integration tests against a real queue manager are in place.

Example placeholder entries:
- Queue: `CURDEPTH` -> `CurrentQDepth` -> `current_q_depth`.
- Queue: `DEFPSIST` -> `DefPersistence` -> `def_persistence`.
- Channel: `CHLTYPE` -> `ChannelType` -> `channel_type`.
- Queue manager: `QMNAME` -> `QMgrName` -> `qmgr_name`.

Rules for placeholder usage:
- Clearly tag any mapping table as placeholder until validated.
- Prefer a small set of attributes that exercise name and value translations.
- Replace placeholders with observed mappings as soon as integration tests are running.

## Error handling
- Display methods return empty lists for missing queue or channel objects and `None` for missing queue manager; no exception.
- Define and delete methods raise on errors.
- Error payloads are stored on the session for diagnostics.

## Testing and development
- Use a containerized IBM MQ 9.4 queue manager with REST enabled.
- Integration tests cover define/display/delete for queues and channels, plus `display_qmgr`.
- Mapping rules and tables are refined based on observed MQ responses.

### Integration test matrix
Queues (each queue type: `QLOCAL`, `QREMOTE`, `QALIAS`, `QMODEL`):
- Define -> display -> delete -> display; verify list contains the object after define and is empty after delete.
- Display missing object returns empty list and no exception.
- Delete missing object raises an error and captures the payload.

Channels (each channel type: `SVRCONN`, `SDR`, `RCVR`, `RQR`, `CLNTCONN`, `CLUSRCVR`, `CLUSSDR`):
- Define -> display -> delete -> display; verify list contains the object after define and is empty after delete.
- Display missing object returns empty list and no exception.
- Delete missing object raises an error and captures the payload.

Queue manager:
- `display_qmgr` returns a dict-like object for the active queue manager.
- `display_qmgr` for an unknown name returns `None` and no exception.

## Milestones
- V1: deliver session core, `_run_command_json`, queue/channel/qmgr methods, mapping scaffolding, and integration tests.
- V1 follow-up: tighten mapping rules based on real responses and document edge cases.

## References
- IBM MQ administrative REST API: https://www.ibm.com/docs/en/ibm-mq/9.4.x?topic=reference-administrative-rest-api
- MQSC command reference: https://www.ibm.com/docs/en/ibm-mq/9.4.x?topic=reference-mqsc-commands
- `runCommandJSON` endpoint: https://www.ibm.com/docs/en/ibm-mq/9.4.x?topic=adminactionqmgrqmgrnamemqsc-post-json-formatted-command
- REST API error handling: https://www.ibm.com/docs/en/ibm-mq/9.4.x?topic=mura-rest-api-error-handling
- PCF command formats: https://www.ibm.com/docs/en/ibm-mq/9.4.x?topic=reference-definitions-programmable-command-formats
