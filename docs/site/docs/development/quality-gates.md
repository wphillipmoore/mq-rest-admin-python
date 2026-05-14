# Quality gates

--8<-- "development/quality-gates.md"

## Python-specific validation

The validation pipeline runs via `vrg-validate` inside the dev container:

```bash
vrg-docker-run -- vrg-validate
```

This executes:

1. **ruff check** — Lint with all rule categories enabled
2. **ruff format** — Formatting check
3. **mypy** — Strict type checking (`src/`)
4. **ty** — Additional type checking (`src/`, `tests/`)
5. **pytest** — Unit tests with 100% line and branch coverage enforcement
6. **pip-audit** — Dependency vulnerability scanning
7. **uv lock --check** — Lock file synchronization verification

The CI matrix tests against Python 3.12, 3.13, and 3.14.
