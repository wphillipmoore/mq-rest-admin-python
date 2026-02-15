# The runCommandJSON endpoint

## Payload structure

The IBM MQ administrative REST API provides a `runCommandJSON` endpoint
that accepts MQSC commands as structured JSON:

```text
POST /ibmmq/rest/v2/admin/action/qmgr/{qmgr}/mqsc
```

The request payload has this shape:

```json
{
  "type": "runCommandJSON",
  "command": "DISPLAY",
  "qualifier": "QLOCAL",
  "name": "MY.QUEUE",
  "parameters": {
    "DESCR": "Updated description"
  },
  "responseParameters": ["all"]
}
```

| Field | Required | Description |
| --- | --- | --- |
| `type` | Yes | Always `"runCommandJSON"` |
| `command` | Yes | MQSC verb: `DISPLAY`, `DEFINE`, `DELETE`, `ALTER`, etc. |
| `qualifier` | Yes | Object type: `QLOCAL`, `CHANNEL`, `QMGR`, etc. |
| `name` | No | Object name or pattern. Omitted for queue manager commands. |
| `parameters` | No | Request attributes as key-value pairs. |
| `responseParameters` | No | List of attribute names to return. |

## Response structure

The response contains an array of command results:

```json
{
  "commandResponse": [
    {
      "completionCode": 0,
      "reasonCode": 0,
      "parameters": {
        "queue": "MY.QUEUE",
        "curdepth": 0,
        "maxdepth": 5000
      }
    }
  ],
  "overallCompletionCode": 0,
  "overallReasonCode": 0
}
```

Each item in `commandResponse` represents one matched object and carries
its own completion/reason code pair plus a `parameters` dict.

## Error handling

Errors are indicated by non-zero completion and reason codes at two
levels:

**Overall codes**: `overallCompletionCode` and `overallReasonCode` on
the top-level response. A non-zero overall code means the command itself
failed.

**Per-item codes**: Each `commandResponse` item has `completionCode`
and `reasonCode`. These indicate per-object errors (e.g. object not
found in a wildcard display).

`pymqrest` raises `MQRESTCommandError` when any error codes are
detected. The full response payload is attached to the exception for
diagnostic use.

For `DISPLAY` commands with no matches, MQ returns an error response
with reason code 2085 (MQRC_UNKNOWN_OBJECT_NAME). `pymqrest`
intentionally treats this as an empty list rather than an exception.

## Nested object flattening

Some commands (`DISPLAY CONN TYPE(HANDLE)`, `DISPLAY QSTATUS
TYPE(HANDLE)`) return responses where each `commandResponse` item
contains an `objects` array of per-handle attributes alongside
parent-scoped attributes. `pymqrest` automatically detects and flattens
these structures so that every command returns uniform flat dicts:

```json
{"conn": "A1B2C3D4E5F6", "objname": "MY.QUEUE", "hstate": "ACTIVE"}
```

See [nested object flattening](nested-object-flattening.md) for the full algorithm, edge cases,
and before/after examples.

## CSRF tokens

The MQ REST API requires a CSRF token header for non-GET requests.
`pymqrest` sends `ibm-mq-rest-csrf-token` with a default value of
`"local"`. This can be overridden at session creation via the
`csrf_token` parameter, or set to `None` to omit the header entirely.

## Authentication

`pymqrest` supports three authentication methods:

- **LTPA** (`LTPAAuth`): Cookie-based authentication via an initial login
  request. This is the recommended method and the default used in all
  examples and documentation.
- **Basic** (`BasicAuth`): HTTP Basic authentication via the `Authorization`
  header.
- **Certificate** (`CertificateAuth`): Mutual TLS with client certificates.

See [authentication](../api/auth.md) for details on each method.
