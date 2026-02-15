# Mapping

## Overview

The mapping module provides bidirectional attribute translation between
developer-friendly `snake_case` names and native MQSC parameter names. The
mapper is used internally by `MQRESTSession` and is not typically called
directly.

See [Mapping Pipeline](../mapping-pipeline.md) for a conceptual overview of
how mapping works.

## Mapping functions

The module exposes three public functions that perform the actual translation.
These are called internally by `MQRESTSession` during command execution:

- **`map_request_attributes()`** — Translates request parameters from
  `snake_case` to MQSC before sending to the REST API. Performs key mapping,
  value mapping, and key-value mapping in sequence.

- **`map_response_attributes()`** — Translates a single response dict from
  MQSC to `snake_case` after receiving from the REST API.

- **`map_response_list()`** — Translates a list of response dicts (the common
  return type for DISPLAY commands).

The mapper performs three types of translation in each direction:

- **Key mapping**: Attribute name translation (e.g. `current_queue_depth` ↔
  `CURDEPTH`)
- **Value mapping**: Enumerated value translation (e.g. `"yes"` ↔ `"YES"`,
  `"server_connection"` ↔ `"SVRCONN"`)
- **Key-value mapping**: Combined name+value translation for cases where both
  key and value change together (e.g. `channel_type="server_connection"` →
  `CHLTYPE("SVRCONN")`)

## Mapping data

The mapping tables are loaded from the JSON resource file at:

```text
pymqrest/mapping_data.json
```

The data is organized by qualifier (e.g. `queue`, `channel`, `qmgr`) with
separate maps for request and response directions. Each qualifier contains:

- `request_key_map` — `snake_case` → MQSC key mapping for requests
- `request_value_map` — value translations for request attributes
- `request_key_value_map` — combined key+value translations for requests
- `response_key_map` — MQSC → `snake_case` key mapping for responses
- `response_value_map` — value translations for response attributes

The mapping data was originally bootstrapped from IBM MQ 9.4 documentation and
covers all standard MQSC attributes across 42 qualifiers.

## Diagnostics

### MappingIssue

Tracks mapping problems encountered during translation:

- Unknown attribute names (not found in key map)
- Unknown attribute values (not found in value map)
- Ambiguous mappings

In strict mode, any `MappingIssue` causes a `MappingError`. In lenient
mode, issues are collected but the unmapped values pass through unchanged.

### MappingError

Raised when attribute mapping fails in strict mode. Contains the list of
`MappingIssue` instances that caused the failure.

```python
try:
    session.display_queue("MY.QUEUE",
        response_parameters=["invalid_attribute_name"])
except MappingError as e:
    # e describes the unmappable attributes
    print(e)
```

## API reference

::: pymqrest.mapping.map_request_attributes

::: pymqrest.mapping.map_response_attributes

::: pymqrest.mapping.map_response_list

::: pymqrest.mapping.MappingIssue

::: pymqrest.mapping.MappingError
    options:
      members: true
      show_bases: true
