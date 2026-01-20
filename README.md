# pymqrest

Python wrapper for the IBM MQ REST API.

## Table of Contents
- [Purpose](#purpose)
- [Status](#status)
- [Development](#development)
- [License](#license)

## Purpose
Provide a Python mapping layer for MQ REST API attribute translations and
command metadata experiments.

## Status
Experimental. The current focus is on attribute mapping and metadata modeling.

## Development
Set up the environment and run the canonical validation command:

```bash
poetry install
poetry run python3 scripts/dev/validate_local.py
```

Docs-only changes can use:

```bash
python3 scripts/dev/validate_docs.py
```

## License
GPL-3.0-or-later. See `LICENSE`.
