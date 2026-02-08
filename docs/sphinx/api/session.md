# Session

The `MQRESTSession` class is the main entry point for interacting with
IBM MQ via the REST API. It inherits all MQSC command methods from
`MQRESTCommandMixin` (see {doc}`commands`).

## MQRESTSession

```{autoclass} pymqrest.session.MQRESTSession
:members:
:show-inheritance:
```

## Transport

The transport layer abstracts HTTP communication. The default
`RequestsTransport` uses the `requests` library. Custom transports
can be injected for testing or alternative HTTP clients.

```{autoclass} pymqrest.session.TransportResponse
:members:
```

```{autoclass} pymqrest.session.MQRESTTransport
:members:
```

```{autoclass} pymqrest.session.RequestsTransport
:members:
```
