# Ensure

## Overview

The ensure module provides the return types for the 16 idempotent ensure
methods on `MQRESTSession`. These methods implement a declarative upsert
pattern: DEFINE if the object does not exist, ALTER only attributes that differ,
or no-op if the object already matches the desired state.

## EnsureAction

An enum indicating the action taken by an ensure method:

```python
class EnsureAction(Enum):
    CREATED    = "created"     # Object did not exist; DEFINE was issued
    UPDATED    = "updated"     # Object existed but attributes differed; ALTER was issued
    UNCHANGED  = "unchanged"   # Object already matched the desired state
```

## EnsureResult

A named tuple containing the action taken and the list of attribute names that
triggered the change (if any):

```python
class EnsureResult(NamedTuple):
    action: EnsureAction       # What happened
    changed: list[str]         # Attribute names that differed (empty for CREATED/UNCHANGED)
```

| Attribute | Type | Description |
| --- | --- | --- |
| `action` | `EnsureAction` | What happened: `CREATED`, `UPDATED`, or `UNCHANGED` |
| `changed` | `list[str]` | Attribute names that triggered an ALTER (in the caller's namespace) |

## Usage

```python
result = session.ensure_qlocal("MY.QUEUE",
    request_parameters={"max_queue_depth": 50000, "description": "App queue"})

match result.action:
    case EnsureAction.CREATED:
        print("Queue created")
    case EnsureAction.UPDATED:
        print(f"Changed: {result.changed}")
    case EnsureAction.UNCHANGED:
        print("Already correct")
```

See [Ensure Methods](../ensure-methods.md) for the full conceptual overview,
comparison logic, and the complete list of available ensure methods.

## API reference

::: pymqrest.ensure.EnsureAction
    options:
      members: true

::: pymqrest.ensure.EnsureResult
    options:
      members: true

::: pymqrest.ensure.MQRESTEnsureMixin
    options:
      members: true
      show_bases: true
      filters:
        - "!^_"
