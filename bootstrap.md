# Python Wrapper for the IBM MQ REST API

This document describes the design of the pymqrest python library, a convenience wrapper for working with the IBM MQ REST API.

## Table of Contents
- [Examples](#examples)
- [Milestone: v1 scope and plan](#milestone-v1-scope-and-plan)
  - [Scope](#scope)
  - [Method set](#method-set)
  - [Error handling](#error-handling)
  - [Mapping strategy](#mapping-strategy)
  - [Integration tests](#integration-tests)
- [Mapping MQSC to Python methods](#mapping-mqsc-to-python-methods)
  - [Method names](#method-names)
  - [Method signatures](#method-signatures)
- [Return values](#return-values)
- [Exception handling](#exception-handling)
- [Attribute mapping MQSC to PCF](#attribute-mapping-mqsc-to-pcf)
- [Test and development infrastructure](#test-and-development-infrastructure)
- [References](#references)
  - [IBM MQ reference material](#ibm-mq-reference-material)

## Examples

Code speaks louder than words:

```python
from pymqrest import MQRESTSession

session = MQRESTSession(...)

qmstatus = session.display_qmstatus()

for queue_name in session.display_qnames():
    queue_status = session.display_qstatus(queue_name)
    # queue_status is a dict[str, Any]
```

```python
from requests import Session as RESTSession

class MQRESTSession:

    rest_session: RESTSession

    def __init__(
        self,
        hostname: str,
        port: str,
        username: str,
        password: str,
        ...
        # Arguments required to connect to the MQ REST endpoint and authenticate
    ) -> None:
    """MQRESTSession __init__.
    
    Instantiate the RESTSession object and authenticate with the MQ REST endpoint

    cf. https://www.ibm.com/docs/en/ibm-mq/9.4.x?topic=login-post
    """
```

## Milestone: v1 scope and plan

### Scope
- IBM MQ 9.4 administrative REST API, using the `runCommandJSON` MQSC endpoint.
- Objects: queues, channels, and queue manager.
- Authentication: start with basic auth only; expand later if needed.

### Method set
- Queue methods: `define_qlocal`, `define_qremote`, `define_qalias`, `define_qmodel`, `display_queue`, `delete_queue`.
- Channel methods: `define_channel` (requires `channel_type`), `display_channel`, `delete_channel`.
- Queue manager methods: `display_qmgr`.
- Queue types: `QLOCAL`, `QREMOTE`, `QALIAS`, `QMODEL`.
- Channel types: `SVRCONN`, `SDR`, `RCVR`, `RQR`, `CLNTCONN`, `CLUSRCVR`, `CLUSSDR`.

### Error handling
- Display: missing objects return an empty list for queue/channel displays and `None` for `display_qmgr`; no exception.
- Define/delete: raise on errors; keep the last response payload accessible for diagnostics.

### Mapping strategy
- Build the mapping pipeline (MQSC -> PCF -> snake_case) with dummy tables for scaffolding.
- Enable mapping by default, with opt-out at session init and per-method.
- Iterate on mapping rules and tables using real MQ responses.

### Integration tests
- Containerized MQ 9.4 queue manager with the REST API enabled.
- Integration tests covering define/display/delete for queues and channels, plus `display_qmgr`.
- Use real MQ responses to refine mapping tables and error rules.

## Mapping MQSC to Python methods

### Method names

Each method of this class is a 1:1 mapping to an IBM MQ MQSC command.   These are documented here:

https://www.ibm.com/docs/en/ibm-mq/9.4.x?topic=reference-mqsc-commands

The mapping is straight forward.   The MQSC command "DISPLAY CHANNEL" maps to anm instance method "display_channel"

The entire implementation will be built using type=runCommandJSON and the generic mqsc endpoint, which exposes the entire MQSC namespace.

https://www.ibm.com/docs/en/ibm-mq/9.4.x?topic=adminactionqmgrqmgrnamemqsc-post-json-formatted-command

An internal method will wrap this and handle the generic error handling.

```python
def _run_command_JSON(
    self,
    command: str, # eg. "define"
    qualifier: str, # eg. "channel"
    name: str | None = None,
    parameters: ParameterType | None = None,
    response_parameters: ResponseParameterType | None = None,
) -> list[ResponseObjects]: # typing TBD
```

### Method signatures

Each specific instance method will wrap this, for example:

```python
    def display_channel(
        self,
        name: str | None = None,
        parameters: ParameterType | None = None,
        response_parameters: ResponseParameterType | None = None,
    ) -> list[ChannelObjects]: # typing TBD
        return self._run_command_JSON("display", "channel", name or "*", parameters or {}, response_parameters or ["ALL"])
```

The specific calling semantics and return values will vary.  We will figure tjhis all out via expermintation with a real queue manager.

These will end up being grouped according to their function signature, with some subtle differences in default arguments and return values.

For example, because each session object is a connection to a specific queue manager, methods such as display_qmgr and display_qmstatus return a single dictionary of key/value pairs, while comamnds for objects such as queues and channels, and most other MQ objects, will return a list of dictionaries.

## Return values

The default return value for methods which perform an action such as creating and object or starting a service will return None, and raise exceptions when errors occur.   We will make the complete response payload accessible as object attribute and/or methods which give access to the state of the latest query.

Display methods will return a single dictionary, or a list of dictionaries, depending on the context.    display_qmgr and display_qmstatus will return a single dictionary, but display_queue, display_channel. etc will return lists.

We want to wrap the dictionaries in objects, so that we can properly type the individual attributes, rather then the ambiguity of "dict[str, str | int | bool | ...]".   These wrapper classes will be usable as inputs to the methods as well, so that a Queue returned by display_queue() can be passed as an argument to create_queue(), with nothing more than some attribute slicing.

Whenever possible, these objects should have dict-like, or list-like behavior, as appropriate.

## Exception handling

The constructor will always return a valid object with a successfully authenticated connection to the specified endpoint, and raise a fatal exception otherwise.   We will likely need to be able to control this behavior with method arguments for more complex error handling scenarios.   Most display commands will raise an exception when you query a spercific object that doesn't exist; runmqsc exits non-zero, for example.   We would simply like to return an empty list to indicate absense, and save the exceptions for real failure.

Error handling and exceptions for the indivudual methods will be a little more complex.

Specific documentation about error handling:

https://www.ibm.com/docs/en/ibm-mq/9.4.x?topic=mura-rest-api-error-handling

## Attribute mapping MQSC to PCF

The default keys used in the parameters passed to the REST API are expected to be the arguments to the actual MQSC commands.   This namespace is anchored in the ancient history of the mainframe systems, and limited to eight characters.  The responses are similarly encoded in shorthand and familiar only to MQ administrators.

There is a much more user and developer (and therefore database column name) friendly namespace in the PCF commands.   We want to be able to specify a PCF-style keyword and translate it (and possibly it's values) tp the MQSC namespace.    Historically, these namespace transformation were maintained by hand, but we are going to develop a playbook for AI to reproduce our mappings by analyzing the IBM documentation for us.

For the majority of the MQSC commands there is an equivalent PCF command.   These are documented here:

https://www.ibm.com/docs/en/ibm-mq/9.4.x?topic=reference-definitions-programmable-command-formats

These mappings will share a common namespace for each specific qualifier (eg. queue, channel, etc) but there will also be command specific (eg. display, stop, start, etc) names to manage as well.

For example, the DISPLAY QSTATUS MQSC command and it's PCF equivalent:

- https://www.ibm.com/docs/en/ibm-mq/9.4.x?topic=reference-display-qstatus-display-queue-status
- https://www.ibm.com/docs/en/ibm-mq/9.4.x?topic=formats-mqcmd-inquire-q-status-inquire-queue-status
- https://www.ibm.com/docs/en/ibm-mq/9.4.x?topic=dpcf-mqcmd-inquire-q-status-inquire-queue-status-response

The input parameters would be mapped as follows, just using a couple of examples:

    CURDEPTH -> CurrentQDepth -> current_q_depth
    CONNAME -> ConnectionName -> connection_name

Every APP CAPS MQSC attribute maps to a CamelCase PCF attribute, which we will map to a snake_case attirbute.

We want the inputs and outputs to be (optionally, see below) translated to/from the snake_case namespace.

This behavior will be enabled by default, with a kwargs option to __init__ to disable it for a specific object, and another kwargs option to disable it for an individual method call.

## Test and development infrastructure

We will need to be able to setup an IBM MQ queue manager, using their free developer release of MQ 9.4 for Linux.  We will also need to setup the REST API service as well.   This will be done in a docker container, and we will develop and integration test which exercises our API against a real queue manager with real objects.

# References

## IBM MQ reference material

The REST API we will be wrapping is documented in several places:
- https://www.ibm.com/docs/en/ibm-mq/9.4.x?topic=reference-administrative-rest-api
- https://www.ibm.com/docs/en/ibm-mq/9.4.x?topic=reference-rest-api-resources
- https://www.ibm.com/docs/en/ibm-mq/9.4.x?topic=mq-messaging-using-rest-api
