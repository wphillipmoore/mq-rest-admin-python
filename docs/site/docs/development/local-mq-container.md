# Local MQ Container

--8<-- "development/local-mq-container.md"

## Python-specific notes

### Integration tests

Integration tests are opt-in and require running MQ containers:

```bash
MQ_REST_ADMIN_RUN_INTEGRATION=1 uv run pytest -m integration
```

When enabled, the test session:

1. Starts both local MQ containers.
2. Waits for both REST endpoints to become ready.
3. Seeds deterministic test objects on both QMs.
4. Runs DISPLAY checks plus define/alter/delete lifecycles.
5. Stops both containers after the session.

### Environment variables

| Variable | Default | Description |
| --- | --- | --- |
| `MQ_REST_BASE_URL` | `https://localhost:9443/ibmmq/rest/v2` | QM1 REST API base URL |
| `MQ_REST_BASE_URL_QM2` | `https://localhost:9444/ibmmq/rest/v2` | QM2 REST API base URL |
| `MQ_ADMIN_USER` | `mqadmin` | Admin username |
| `MQ_ADMIN_PASSWORD` | `mqadmin` | Admin password |
| `MQ_IMAGE` | `icr.io/ibm-messaging/mq:latest` | Container image |

### Gateway routing with pymqrest

```python
from pymqrest import MQRESTSession
from pymqrest.auth import BasicAuth

# Route commands to QM2 through QM1
session = MQRESTSession(
    rest_base_url="https://localhost:9443/ibmmq/rest/v2",
    qmgr_name="QM2",
    credentials=BasicAuth("mqadmin", "mqadmin"),
    gateway_qmgr="QM1",
    verify_tls=False,
)

qmgr = session.display_qmgr()
print(qmgr)  # QM2's attributes, routed through QM1
```
