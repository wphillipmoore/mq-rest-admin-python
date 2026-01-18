# Mapping data structures (minimal set)

## Table of Contents
- [Purpose](#purpose)
- [Scope](#scope)
- [Design goals](#design-goals)
- [Compiled artifact](#compiled-artifact)
- [Minimal dataset](#minimal-dataset)
  - [Command map](#command-map)
  - [Key maps](#key-maps)
  - [Value maps](#value-maps)
- [Python shape](#python-shape)
- [Mapping behavior](#mapping-behavior)
- [Strictness and error handling](#strictness-and-error-handling)
- [Derivation from metadata](#derivation-from-metadata)
- [Validation checks](#validation-checks)
- [Open questions](#open-questions)

## Purpose
Define the minimal runtime data structures needed to translate MQSC request/response attributes to snake_case and back again for wrapper inputs.

## Scope
- Runtime mapping only (no documentation metadata, URLs, or extraction logs).
- Enough information to map request parameters and response attributes.
- Versioned schema that can be regenerated from the metadata set.
- YAML and extraction artifacts are build-time only and are not read at runtime.

## Design goals
- Minimal cardinality: store only fields required for mapping.
- Symmetry: the same dataset supports request and response mapping.
- Deterministic: stable ordering is not required; keys must be explicit.
- Regenerable: derived from the extraction outputs without manual edits.
- Minimal runtime work: import precompiled dicts; no parsing or inversion.

## Compiled artifact
The runtime code imports a precompiled Python module that contains only dict literals. The detailed YAML and extraction files are used only by a build-time generator and are not part of the runtime code path.

## Minimal dataset
The minimal dataset is split into a command map and qualifier-scoped key/value maps. Value maps are optional and only appear when symbolic token translation is required.

### Command map
Each entry maps an MQSC verb + object to a qualifier.

Required fields:
- `mqsc`: MQSC command name (e.g., `DISPLAY QUEUE`).
- `qualifier`: qualifier key for attribute mapping (e.g., `queue`).
- `status`: `confirmed`, `provisional`, or `no-equivalent`.

### Key maps
Key maps are stored per qualifier and named by mapping direction.

Required fields:
- `request_key_map`: snake_case name -> MQSC attribute token.
- `response_key_map`: MQSC attribute token -> snake_case name.

Optional fields:
- `notes`: short string for conflicts or overrides.

### Value maps
Value maps are optional and apply only when MQSC uses symbolic tokens that must translate to snake_case values.

Required fields:
- `request_value_map`: attribute -> {snake -> mqsc_token}.
- `response_value_map`: attribute -> {mqsc_token -> snake}.

## Python shape
The runtime structures can be represented as nested dictionaries with explicit keys and no class machinery.

```python
MAPPING_DATA = {
    "version": 1,
    "commands": {
        "DISPLAY QUEUE": {
            "qualifier": "queue",
            "status": "provisional",
        },
        "CLEAR QLOCAL": {
            "qualifier": "queue",
            "status": "provisional",
        },
    },
    "qualifiers": {
        "queue": {
            "request_key_map": {
                "current_q_depth": "CURDEPTH",
                "def_persistence": "DEFPSIST",
            },
            "response_key_map": {
                "CURDEPTH": "current_q_depth",
                "DEFPSIST": "def_persistence",
            },
            "request_value_map": {
                "def_persistence": {
                    "def": "DEF",
                    "not_fixed": "NOTFIXED",
                }
            },
            "response_value_map": {
                "DEFPSIST": {
                    "DEF": "def",
                    "NOTFIXED": "not_fixed",
                }
            },
        },
        "channel": {
            "request_key_map": {
                "channel_type": "CHLTYPE",
            },
            "response_key_map": {
                "CHLTYPE": "channel_type",
            },
        },
    },
}
```

Notes:
- The keys under `commands` are MQSC command names.
- The keys under `request_key_map` are snake_case names; the keys under `response_key_map` are MQSC attribute tokens.
- The structure is intentionally flat to keep lookups fast and predictable.

## Mapping behavior
- REST requests use MQSC attributes; wrapper inputs use snake_case. Map inputs using `request_key_map` and `request_value_map`.
- REST responses are MQSC attributes; wrapper outputs are snake_case. Map outputs using `response_key_map` and `response_value_map`.

## Strictness and error handling
- Strictness is configurable and defaults to true.
- When mapping a dict, collect all key/value mapping failures and raise a single error after processing all keys.
- When mapping a list of dicts, collect per-item errors and raise a single aggregated error after processing the entire list.
- The error payload should include the object index (or identifier), attribute name, direction, and reason.

## Derivation from metadata
- Start from `docs/mqsc-pcf-command-mapping.md` for the command list and qualifier assignment.
- Use the qualifier-specific extraction files under `docs/mqsc-pcf-parameter-extraction/` to identify request/response attribute candidates.
- Normalize MQSC attribute tokens to canonical uppercase and map to snake_case based on the PCF-derived name.
- Emit `request_key_map` as snake_case -> MQSC for request mapping.
- Emit `response_key_map` as MQSC -> snake_case for response mapping.
- Emit `request_value_map` and `response_value_map` only when symbolic tokens require translation.
- Apply a curated override layer derived from integration test results to correct doc mismatches.

## Validation checks
- Every MQSC command with `status != no-equivalent` has a `qualifier`.
- Every qualifier has both `request_key_map` and `response_key_map`.
- Attribute entries are unique per qualifier and MQSC token.
- All `request_key_map` and `response_key_map` entries are one-to-one.
- All value mappings are one-to-one and lower_snake_case.

## Open questions
- Are qualifier-level overrides needed for commands that reuse a qualifier but expose distinct attribute sets?
- Should unknown MQSC tokens pass through untouched or raise mapping errors?
