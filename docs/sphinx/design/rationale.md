# Design rationale

## Why wrap the REST API

IBM MQ provides an administrative REST API, but working with it directly
requires constructing JSON payloads with MQSC-specific parameter names,
handling CSRF tokens, parsing nested response structures, and
interpreting completion/reason code pairs.

`pymqrest` wraps this complexity behind Python methods that map 1:1 to
MQSC commands, translate attribute names to `snake_case`, and surface
errors as exceptions with full diagnostic context.

## Single-endpoint design

All MQSC operations go through a single REST endpoint:

```
POST /ibmmq/rest/v2/admin/action/qmgr/{qmgr}/mqsc
```

The `runCommandJSON` payload structure carries the command verb,
qualifier, object name, and parameters:

```json
{
  "type": "runCommandJSON",
  "command": "DISPLAY",
  "qualifier": "QLOCAL",
  "name": "MY.QUEUE",
  "responseParameters": ["all"]
}
```

This means `pymqrest` needs exactly one HTTP method, one URL pattern,
and one payload schema to cover the entire MQSC command surface.

## Method naming conventions

Command methods follow the pattern `<verb>_<qualifier>` in lowercase
with spaces converted to underscores:

| MQSC command | Python method |
| --- | --- |
| `DISPLAY QUEUE` | `display_queue()` |
| `DEFINE QLOCAL` | `define_qlocal()` |
| `DELETE CHANNEL` | `delete_channel()` |
| `ALTER QMGR` | `alter_qmgr()` |

This convention provides a predictable, discoverable API without
inventing new abstractions over the MQSC command set.

## Return shape decisions

**DISPLAY commands** return `list[dict[str, object]]`. An empty list
means no objects matched — this is not an error. The caller can iterate
without checking for `None`.

**Queue manager singletons** (`display_qmgr`, `display_qmstatus`, etc.)
return `dict[str, object] | None`. These commands always return zero or
one result, so a list would be misleading.

**Non-DISPLAY commands** (`DEFINE`, `DELETE`, `ALTER`, etc.) return
`None` on success and raise `MQRESTCommandError` on failure.

## Attribute mapping complexity

The mapping layer is the most complex part of `pymqrest`. This
complexity exists because IBM MQ uses terse uppercase tokens (`CURDEPTH`,
`DEFPSIST`, `CHLTYPE`) that are unfriendly in Python code. The mapping
pipeline translates these to readable `snake_case` names
(`current_depth`, `default_persistence`, `channel_type`) and back.

The translation is not a simple case conversion. The mapping tables were
originally bootstrapped from IBM MQ 9.4 documentation, then customized
and rationalized. They are now maintained directly in `mapping_data.py`
as the sole authoritative source (see {doc}`/development/namespace-origin`).
The tables contain:

- **Key maps**: Attribute name translations (e.g. `CURDEPTH` ↔
  `current_depth`).
- **Value maps**: Enumerated value translations (e.g. `"YES"` ↔
  `"yes"`, `"SVRCONN"` ↔ `"server_connection"`).
- **Key-value maps**: Cases where both key and value change together.

See {doc}`/mapping-pipeline` for full details.

## Beta status

`pymqrest` is in beta. The API surface, mapping tables, and return
shapes are stable but may evolve. The project builds on an approach to
MQ administration tooling that dates back over 25 years.
