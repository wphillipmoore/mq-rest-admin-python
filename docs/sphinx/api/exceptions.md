# Exceptions

All exceptions inherit from `MQRESTError`.

```
Exception
└── MQRESTError
    ├── MQRESTTransportError   — network/connection failures
    ├── MQRESTResponseError    — malformed responses
    └── MQRESTCommandError     — MQSC command failures
```

```{autoclass} pymqrest.exceptions.MQRESTError
:show-inheritance:
```

```{autoclass} pymqrest.exceptions.MQRESTTransportError
:members:
:show-inheritance:
```

```{autoclass} pymqrest.exceptions.MQRESTResponseError
:members:
:show-inheritance:
```

```{autoclass} pymqrest.exceptions.MQRESTCommandError
:members:
:show-inheritance:
```
