# pymqrest

## Overview

**pymqrest** provides a Python-friendly interface to IBM MQ queue manager
administration via the `runCommandJSON` REST endpoint. It translates between
Python `snake_case` attribute names and native MQSC parameter names, wraps
every MQSC command as a typed method, and handles authentication, CSRF tokens,
and error propagation.

## Key features

- **~144 command methods** covering all MQSC verbs and qualifiers
- **Bidirectional attribute mapping** between developer-friendly names and MQSC parameters
- **Idempotent ensure methods** for declarative object management
- **Bulk sync operations** for configuration-as-code workflows
- **Zero runtime dependencies** — stdlib only
- **Transport abstraction** for easy testing with mock transports

## Quick links

- [Getting Started](getting-started.md) — Installation and first session
- [Architecture](architecture.md) — How the library is organized
- [Mapping Pipeline](mapping-pipeline.md) — Attribute translation details
- [API Reference](api/index.md) — Class and method documentation
- [Examples](examples.md) — Practical scripts for common tasks

## Installation

```bash
pip install pymqrest
```

Or with [uv](https://docs.astral.sh/uv/):

```bash
uv add pymqrest
```

## Status

This project is in **beta**. The API surface, mapping tables, and return
shapes are stable but may evolve.

## License

GNU General Public License v3.0
