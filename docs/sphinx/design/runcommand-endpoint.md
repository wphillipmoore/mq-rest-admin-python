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

Some commands return responses with nested `objects` lists. For example,
`DISPLAY CONN TYPE(HANDLE)` returns connection entries where each may
contain multiple handle objects:

```json
{
  "parameters": {
    "conn": "A1B2C3D4E5F6",
    "objects": [
      {"objname": "MY.QUEUE", "hstate": "ACTIVE"},
      {"objname": "MY.OTHER.QUEUE", "hstate": "ACTIVE"}
    ]
  }
}
```

`pymqrest` automatically detects and flattens these nested structures.
Each nested object is merged with the parent attributes to produce flat
dictionaries:

```json
[
  {"conn": "A1B2C3D4E5F6", "objname": "MY.QUEUE", "hstate": "ACTIVE"},
  {"conn": "A1B2C3D4E5F6", "objname": "MY.OTHER.QUEUE", "hstate": "ACTIVE"}
]
```

If a connection has no handles, the `objects` list is empty and the
entry produces no output rows.

## CSRF tokens

The MQ REST API requires a CSRF token header for non-GET requests.
`pymqrest` sends `ibm-mq-rest-csrf-token` with a default value of
`"local"`. This can be overridden at session creation via the
`csrf_token` parameter, or set to `None` to omit the header entirely.

## Authentication

`pymqrest` uses HTTP Basic authentication. The `Authorization` header
is constructed from the username and password provided at session
creation. Other authentication methods (client certificates, token-based
auth) are not currently supported.
