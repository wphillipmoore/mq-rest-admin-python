# Session

The `MQRESTSession` class is the main entry point for interacting with
IBM MQ via the REST API. It inherits MQSC command methods from
`MQRESTCommandMixin` (see {doc}`commands`) and idempotent ensure methods
from `MQRESTEnsureMixin` (see {doc}`ensure`).

## MQRESTSession

```{eval-rst}
.. autoclass:: pymqrest.session.MQRESTSession
   :members:
   :show-inheritance:
```

## Transport

The transport layer abstracts HTTP communication. The default
`RequestsTransport` uses the `requests` library. Custom transports
can be injected for testing or alternative HTTP clients.

```{eval-rst}
.. autoclass:: pymqrest.session.TransportResponse
   :exclude-members: status_code, text, headers
```

```{eval-rst}
.. autoclass:: pymqrest.session.MQRESTTransport
   :members:
```

```{eval-rst}
.. autoclass:: pymqrest.session.RequestsTransport
   :members:
```
