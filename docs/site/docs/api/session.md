# Session

The `MQRESTSession` class is the main entry point for interacting with
IBM MQ via the REST API. It inherits MQSC command methods from
`MQRESTCommandMixin` (see [commands](commands.md)) and idempotent ensure methods
from `MQRESTEnsureMixin` (see [ensure](ensure.md)).

## MQRESTSession

::: pymqrest.session.MQRESTSession
    options:
      members: true
      show_bases: true

## Transport

See [Transport](transport.md) for the transport protocol, response type,
and mock transport examples.
