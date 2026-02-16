# Transport

## Overview

The transport layer abstracts HTTP communication from the session logic. The
session builds `runCommandJSON` payloads and delegates HTTP delivery to a
transport implementation. This separation enables testing the entire command
pipeline without an MQ server by injecting a mock transport.

## MQRESTTransport

The transport protocol defines a single method for posting JSON payloads:

::: pymqrest.session.MQRESTTransport
    options:
      members: true

## TransportResponse

An immutable result containing the HTTP response data:

::: pymqrest.session.TransportResponse
    options:
      members: true

## RequestsTransport

The default transport implementation using the `requests` library:

::: pymqrest.session.RequestsTransport
    options:
      members: true

## Custom transport

Implement the `MQRESTTransport` protocol to provide custom HTTP behavior or
for testing. Because the protocol has a single method, a mock works naturally:

```python
from unittest.mock import MagicMock
from pymqrest.session import MQRESTTransport, TransportResponse

mock_transport = MagicMock(spec=MQRESTTransport)
mock_transport.post_json.return_value = TransportResponse(
    status_code=200,
    text='{"commandResponse": []}',
    headers={},
)

session = MQRESTSession(
    rest_base_url="https://localhost:9443/ibmmq/rest/v2",
    qmgr_name="QM1",
    credentials=LTPAAuth("admin", "passw0rd"),
    transport=mock_transport,
)
```

This pattern is used extensively in the library's own test suite to verify
command payload construction, response parsing, and error handling without
network access.
