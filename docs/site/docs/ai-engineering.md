# AI-assisted engineering

--8<-- "ai-engineering.md"

## Python-specific quality standards

**100% test coverage**: Every line and branch of production code is
covered by unit tests. Coverage is enforced as a CI hard gate.

**Strict typing**: Both mypy and ty type checkers run in strict mode
against the entire source tree.

**Comprehensive linting**: Ruff runs with all rule categories enabled.
The few per-file exceptions (like missing docstrings in generated code)
are explicitly configured.

**Validation pipeline**: `scripts/dev/validate_local.py` runs the same
checks as CI, including dependency auditing, lock file verification,
and commit message validation.
