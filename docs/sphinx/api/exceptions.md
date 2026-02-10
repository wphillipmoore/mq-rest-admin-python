# Exceptions

All exceptions inherit from `MQRESTError`.

```text
Exception
└── MQRESTError
    ├── MQRESTAuthError        — authentication failures
    ├── MQRESTTransportError   — network/connection failures
    ├── MQRESTResponseError    — malformed responses
    └── MQRESTCommandError     — MQSC command failures
```

```{eval-rst}
.. autoclass:: pymqrest.exceptions.MQRESTError
   :show-inheritance:
```

```{eval-rst}
.. autoclass:: pymqrest.exceptions.MQRESTAuthError
   :members:
   :show-inheritance:
```

```{eval-rst}
.. autoclass:: pymqrest.exceptions.MQRESTTransportError
   :members:
   :show-inheritance:
```

```{eval-rst}
.. autoclass:: pymqrest.exceptions.MQRESTResponseError
   :members:
   :show-inheritance:
```

```{eval-rst}
.. autoclass:: pymqrest.exceptions.MQRESTCommandError
   :members:
   :show-inheritance:
```
