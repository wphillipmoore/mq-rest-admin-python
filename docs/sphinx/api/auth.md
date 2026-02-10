# Authentication

The authentication module provides credential types for the three
authentication modes supported by the IBM MQ REST API: HTTP Basic,
LTPA token, and mutual TLS (mTLS) client certificates.

Pass a credential object to `MQRESTSession` via the `credentials`
keyword argument.

```python
from pymqrest import MQRESTSession, BasicAuth, LTPAAuth, CertificateAuth

# Basic auth
session = MQRESTSession("https://...", "QM1", credentials=BasicAuth("user", "pass"))

# LTPA token auth (login at construction)
session = MQRESTSession("https://...", "QM1", credentials=LTPAAuth("user", "pass"))

# mTLS client certificate auth
session = MQRESTSession("https://...", "QM1", credentials=CertificateAuth("/cert.pem", "/key.pem"))
```

## Credential Types

```{eval-rst}
.. autoclass:: pymqrest.auth.BasicAuth
   :exclude-members: username, password
```

```{eval-rst}
.. autoclass:: pymqrest.auth.LTPAAuth
   :exclude-members: username, password
```

```{eval-rst}
.. autoclass:: pymqrest.auth.CertificateAuth
   :exclude-members: cert_path, key_path
```

## Type Alias

```{eval-rst}
.. autodata:: pymqrest.auth.Credentials
```

## LTPA Login

```{eval-rst}
.. autofunction:: pymqrest.auth.perform_ltpa_login
```
