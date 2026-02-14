# Nested object flattening

## Problem statement

Most MQSC commands return a flat list of parameter objects — one dict per
matched MQ object. However, two commands return a **nested** structure
when queried with `TYPE(HANDLE)`:

- `DISPLAY CONN TYPE(HANDLE)` — connection handles
- `DISPLAY QSTATUS TYPE(HANDLE)` — queue status handles

In these responses each `commandResponse` item represents a parent
entity (a connection or a queue) that may own multiple handles. The
per-handle attributes are nested inside an `objects` array, while
parent-scoped attributes sit alongside it.

Without intervention this would force every caller to detect and unpack
the nesting manually. `pymqrest` instead applies transparent flattening
so that all commands — nested or not — return uniform flat dicts.

## Raw API response format

A `DISPLAY CONN TYPE(HANDLE)` response with two handles looks like this:

```json
{
  "commandResponse": [
    {
      "completionCode": 0,
      "reasonCode": 0,
      "parameters": {
        "conn": "A1B2C3D4E5F6",
        "extconn": "G7H8I9J0K1L2",
        "objects": [
          {"objname": "MY.QUEUE", "hstate": "ACTIVE", "openopts": 8225},
          {"objname": "MY.OTHER.QUEUE", "hstate": "INACTIVE", "openopts": 8193}
        ]
      }
    }
  ],
  "overallCompletionCode": 0,
  "overallReasonCode": 0
}
```

| Level | Keys | Description |
| --- | --- | --- |
| Parent | `conn`, `extconn` | Connection-scoped attributes shared by all handles |
| Nested | `objname`, `hstate`, `openopts` | Per-handle attributes inside `objects` |

## Flattening algorithm

The `_flatten_nested_objects()` function in `session.py` processes the
parameter objects list **after** extraction from the response but
**before** attribute mapping:

1. For each parameter dict, check whether an `objects` key exists and
   its value is a `list`.
2. If **yes**: collect all other keys into a `shared` dict, then for
   each dict-typed entry in `objects`, merge `shared | nested_item` to
   produce a flat output row. Non-dict entries in `objects` are silently
   skipped.
3. If **no** (the key is absent, or the value is not a list): pass the
   item through unchanged.

The merge uses Python's `dict | dict` syntax, so nested-item keys
override any same-named parent keys.

## Flattened result

After flattening, the example above produces two flat dicts:

```json
[
  {
    "conn": "A1B2C3D4E5F6",
    "extconn": "G7H8I9J0K1L2",
    "objname": "MY.QUEUE",
    "hstate": "ACTIVE",
    "openopts": 8225
  },
  {
    "conn": "A1B2C3D4E5F6",
    "extconn": "G7H8I9J0K1L2",
    "objname": "MY.OTHER.QUEUE",
    "hstate": "INACTIVE",
    "openopts": 8193
  }
]
```

When attribute mapping is enabled (the default), the MQSC names are then
translated to `snake_case`:

```python
[
    {
        "object_name": "MY.QUEUE",
        "handle_state": "ACTIVE",
        ...
    },
    {
        "object_name": "MY.OTHER.QUEUE",
        "handle_state": "INACTIVE",
        ...
    },
]
```

## Edge cases

The flattening logic handles several edge cases, each covered by unit
tests in `test_session.py`:

| Scenario | Behaviour |
| --- | --- |
| Empty `objects` list | Parent produces **no** output rows |
| `objects` value is not a list (e.g. a string) | Item passes through unchanged — treated as a regular flat parameter |
| Mixed flat and nested items in the same response | Both handled correctly — flat items pass through, nested items are expanded |
| Non-dict entries inside `objects` array | Silently skipped — only dict-typed entries become output rows |
| Single nested entry | Works identically to multiple — produces one flat dict |

## Where flattening occurs in the pipeline

```text
HTTP response
  → JSON parse
  → extract commandResponse items
  → collect parameter dicts
  → _flatten_nested_objects()     ← here
  → normalise attribute case
  → map_response_list() (if mapping enabled)
  → return to caller
```

Flattening happens before attribute mapping so that the mapping layer
sees a uniform list of flat dicts regardless of the original response
shape.

## See also

- {doc}`runcommand-endpoint` — general `runCommandJSON` request/response
  structure
- {doc}`rationale` — overall design rationale
- [DISPLAY CONN](https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-display-conn) —
  IBM MQ documentation
- [DISPLAY QSTATUS](https://www.ibm.com/docs/en/ibm-mq/9.4?topic=reference-display-qstatus) —
  IBM MQ documentation
