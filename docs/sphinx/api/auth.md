# Authentication

The authentication module provides credential types for the three
authentication modes supported by the IBM MQ REST API: mutual TLS (mTLS)
client certificates, LTPA token, and HTTP Basic.

Pass a credential object to `MQRESTSession` via the `credentials`
keyword argument. Always use TLS (`https://`) for production
deployments to protect credentials and data in transit.

```python
from pymqrest import MQRESTSession, BasicAuth, LTPAAuth, CertificateAuth

# mTLS client certificate auth — strongest; no shared secrets
session = MQRESTSession("https://...", "QM1", credentials=CertificateAuth("/cert.pem", "/key.pem"))

# LTPA token auth — credentials sent once at login, then cookie-based
session = MQRESTSession("https://...", "QM1", credentials=LTPAAuth("user", "pass"))

# Basic auth — credentials sent with every request
session = MQRESTSession("https://...", "QM1", credentials=BasicAuth("user", "pass"))
```

## Credential Types

```{eval-rst}
.. autoclass:: pymqrest.auth.CertificateAuth
   :exclude-members: cert_path, key_path
```

```{eval-rst}
.. autoclass:: pymqrest.auth.LTPAAuth
   :exclude-members: username, password
```

```{eval-rst}
.. autoclass:: pymqrest.auth.BasicAuth
   :exclude-members: username, password
```

## Choosing between LTPA and Basic authentication

Both LTPA and Basic authentication use a username and password. The key
difference is how often those credentials cross the wire.

**LTPA is the recommended choice for username/password authentication.**
Credentials are sent once during the `/login` request; subsequent API
calls carry only the LTPA cookie. This reduces credential exposure and
is more efficient for sessions that issue many commands. All examples
and documentation in this project use LTPA as the default.

**Use Basic authentication as a fallback when:**

- The mqweb configuration does not enable the `/login` endpoint (for
  example, minimal container images that only expose the REST API).
- A reverse proxy or API gateway handles authentication and forwards a
  Basic auth header; cookie-based flows may not survive the proxy.
- Single-command scripts where the login round-trip doubles the request
  count for no security benefit.
- Long-running sessions where LTPA token expiry (typically two hours)
  could cause mid-operation failures; pymqrest does not currently
  re-authenticate automatically.
- Local development or CI against a `localhost` container, where
  transport security is not a concern.

## Type Alias

```{eval-rst}
.. autodata:: pymqrest.auth.Credentials
```
