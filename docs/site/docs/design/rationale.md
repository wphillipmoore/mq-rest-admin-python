# Design Rationale

--8<-- "design/rationale.md"

## Python-specific design choices

### Return type annotations

**DISPLAY commands** return `list[dict[str, object]]`. An empty list
means no objects matched -- this is not an error. The caller can iterate
without checking for `None`.

**Queue manager singletons** (`display_qmgr`, `display_qmstatus`, etc.)
return `dict[str, object] | None`. These commands always return zero or
one result, so a list would be misleading.

**Non-DISPLAY commands** (`DEFINE`, `DELETE`, `ALTER`, etc.) return
`None` on success and raise `MQRESTCommandError` on failure.

### Beta status

`pymqrest` is in beta. The API surface, mapping tables, and return
shapes are stable but may evolve. The project builds on an approach to
MQ administration tooling that dates back over 25 years.
