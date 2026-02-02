# pymqrest

Python wrapper for the IBM MQ REST API.

## Table of Contents

- [Purpose](#purpose)
- [Status](#status)
- [Development](#development)
- [Local MQ container](#local-mq-container)
- [License](#license)

## Purpose

Provide a Python mapping layer for MQ REST API attribute translations and
command metadata experiments.

## Status

Experimental. The current focus is on attribute mapping and metadata modeling.

## Development

Set up the environment and run the canonical validation command:

```bash
uv sync --group dev
uv run python3 scripts/dev/validate_local.py
```

Docs-only changes can use:

```bash
uv run python3 scripts/dev/validate_docs.py
```

## Local MQ container

For local MQSC/PCF command validation against a real queue manager, see
`docs/mq-container-local-dev.md`.

## License

GPL-3.0-or-later. See `LICENSE`.
