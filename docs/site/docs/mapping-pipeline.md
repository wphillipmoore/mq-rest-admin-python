# Mapping pipeline

## The three-namespace problem

IBM MQ uses multiple naming conventions depending on the interface:

**MQSC names** (e.g. `CURDEPTH`, `DEFPSIST`)
: Short, uppercase tokens used in MQSC commands and the REST API's
  `runCommandJSON` endpoint.

**PCF names** (e.g. `CurrentQDepth`, `DefPersistence`)
: CamelCase names from the Programmable Command Formats. Not used
  directly by `pymqrest`, but they form the intermediate namespace in
  the mapping pipeline.

**Python names** (e.g. `current_queue_depth`, `default_persistence`)
: Human-readable `snake_case` names for use in Python code.

The mapping pipeline translates between MQSC and Python names. PCF names
were used as an intermediate reference during the original extraction
process that bootstrapped the mapping tables but do not appear at
runtime.

## Qualifier-based mapping

Mappings are organized by **qualifier** (e.g. `queue`, `channel`, `qmgr`),
not by command. A single qualifier's mapping tables serve all commands
that operate on that object type. For example, the `queue` qualifier
covers `DISPLAY QUEUE`, `DEFINE QLOCAL`, `DELETE QALIAS`, and all other
queue-related commands.

This design avoids duplicating mapping data across commands and reflects
how MQSC attributes are shared across command verbs.

See [qualifier mapping reference](mappings/index.md) for the complete per-qualifier reference.

## Request mapping flow

When mapping is enabled, request attributes are translated before sending
to the MQ REST API:

1. **Key mapping**: Each `snake_case` attribute name is looked up in the
   qualifier's `request_key_map`. If found, the key is replaced with the
   MQSC parameter name.

2. **Value mapping**: For attributes with enumerated values, the
   qualifier's `request_value_map` translates Python values to MQSC
   values (e.g. `"yes"` → `"YES"`).

3. **Key-value mapping**: Some attributes require both key and value to
   change simultaneously. The `request_key_value_map` handles cases
   where a single Python attribute expands to a different MQSC key+value
   pair (e.g. `channel_type="server_connection"` →
   `CHLTYPE("SVRCONN")`).

## Response mapping flow

Response attributes are translated after receiving the MQ REST response:

1. **Key mapping**: Each MQSC parameter name from the response is looked
   up in the qualifier's `response_key_map`. If found, the key is
   replaced with the `snake_case` name.

2. **Value mapping**: Enumerated MQSC values are translated to
   Python-friendly values via the `response_value_map` (e.g. `"YES"` →
   `"yes"`).

## Response parameter mapping

When the caller specifies `response_parameters` (the list of attributes
to return), those names are also mapped from `snake_case` to MQSC before
being sent in the request. This allows callers to request specific
attributes using Python names.

Response parameter macros (like `CFCONLOS` for channel status) are
recognized and passed through without mapping.

## WHERE keyword mapping

The `where` parameter on DISPLAY methods accepts a filter expression
like `"current_queue_depth GT 100"`. The first token (the keyword) is mapped
from `snake_case` to the MQSC name. The rest of the expression is
passed through unchanged.

## Strict vs lenient mode

**Strict mode** (default): Any attribute name or value that cannot be
mapped raises a `MappingError`. This catches typos and unsupported
attributes early.

**Lenient mode** (`mapping_strict=False`): Unknown attribute names and
values pass through unchanged. This is useful when working with
attributes not yet covered by the mapping tables.

The mode is set at session creation and applies to all mapping
operations. It cannot be overridden per-call.

## Qualifier resolution

When a command is executed, the mapping qualifier is resolved by:

1. Looking up the command key (e.g. `"DISPLAY QUEUE"`) in
   `MAPPING_DATA["commands"]` for an explicit qualifier.
2. Falling back to a hardcoded default map (e.g. `QLOCAL` → `queue`,
   `CHANNEL` → `channel`).
3. As a last resort, lowercasing the MQSC qualifier.

This means `DEFINE QLOCAL`, `DEFINE QREMOTE`, and `DISPLAY QUEUE` all
resolve to the `queue` qualifier and share the same mapping tables.

## Custom mapping overrides

The built-in mapping tables cover all standard MQSC attributes, but sites may
use different `snake_case` conventions. The `mapping_overrides` parameter on
`MQRESTSession` lets you layer sparse changes on top of the built-in data
without replacing it.

### How merging works

Overrides are merged at the **key level** within each sub-map:

```python
mapping_overrides = {
    "qualifiers": {
        "queue": {
            "response_key_map": {
                "CURDEPTH": "queue_depth",   # replaces the built-in mapping for CURDEPTH
            },
        },
    },
}
```

When this override is applied:

1. The built-in `MAPPING_DATA` is deep-copied (the original is never mutated).
2. The `queue` qualifier's `response_key_map` is updated: the entry for
   `CURDEPTH` changes from `"current_queue_depth"` to `"queue_depth"`.
3. All other entries in `response_key_map` (and all other sub-maps) remain
   unchanged.

This means you only specify the entries you want to change. A single override
entry doesn't affect the hundreds of other mappings.

### Supported override keys

The top level of `mapping_overrides` accepts two keys:

- **`commands`**: Override command-level metadata (e.g. which qualifier a
  command resolves to). Each command entry is shallow-merged.
- **`qualifiers`**: Override qualifier mapping tables. Each qualifier supports
  five sub-maps:
  - `request_key_map` — `snake_case` → MQSC key mapping for requests
  - `request_value_map` — value translations for request attributes
  - `request_key_value_map` — combined key+value translations for requests
  - `response_key_map` — MQSC → `snake_case` key mapping for responses
  - `response_value_map` — value translations for response attributes

### Adding new qualifiers

You can add mappings for qualifiers not yet covered by the built-in data:

```python
mapping_overrides = {
    "qualifiers": {
        "custom_object": {
            "request_key_map": {"my_attr": "MYATTR"},
            "response_key_map": {"MYATTR": "my_attr"},
            "request_value_map": {},
            "response_value_map": {},
        },
    },
}
```

### Validation

The override structure is validated at session construction time. Invalid
shapes raise `TypeError` (wrong types) or `ValueError` (unknown keys)
immediately, so errors are caught before any commands are sent.

## Opting out

Mapping can be disabled entirely or selectively:

**Session-level**: Pass `map_attributes=False` when creating the session.

**Per-call**: Pass `map_attributes=False` to any command method. This
overrides the session default for that single call.

When mapping is disabled, attributes pass through in their native MQSC
form.
