# Quality gates

--8<-- "development/quality-gates.md"

## Python-specific validation

The Python validation pipeline runs via a local validation script:

```bash
scripts/dev/validate_local.py
```

This executes:

1. **ruff check** — Lint with all rule categories enabled
2. **ruff format** — Formatting check
3. **mypy** — Strict type checking (`src/`)
4. **ty** — Additional type checking (`src/`)
5. **pytest** — Unit tests with 100% line and branch coverage enforcement
6. **pip-audit** — Dependency vulnerability scanning
7. **uv lock --check** — Lock file synchronization verification

The CI matrix tests against Python 3.12, 3.13, and 3.14.
