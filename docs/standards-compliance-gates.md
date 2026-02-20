# Standards compliance gates

## Table of Contents

- [Overview](#overview)
- [Gate layers](#gate-layers)
- [Local enforcement](#local-enforcement)
- [CI enforcement](#ci-enforcement)
- [Validation scripts](#validation-scripts)
- [Configuration](#configuration)

## Overview

This repository enforces standards compliance through three layers: local git
hooks for fast pre-commit checks, CI workflow jobs for branch-level gates, and
local validation scripts that mirror CI for pre-push verification.

## Gate layers

| Layer | Trigger | Scope | Speed |
| ----- | ------- | ----- | ----- |
| Git hooks | Pre-commit, commit-msg | Branch naming, commit format | Instant |
| CI `ci: standards-compliance` job | Pull request, push to develop | Repo profile, markdown, commits, issue linkage | Seconds |
| CI `test: unit` job | Pull request, push to develop | Linting, typing, tests, coverage | Minutes |
| CI `ci: dependency-audit` job | Pull request, push to develop | Security vulnerabilities | Seconds |

## Local enforcement

### Pre-commit hook

**File:** `scripts/git-hooks/pre-commit`

Blocks commits on protected branches (`develop`, `release`, `main`,
`release/*`) and enforces branch naming prefixes (`feature/*`, `bugfix/*`,
`hotfix/*`).

Enable with: `git config core.hooksPath scripts/git-hooks`

### Commit message hook

**File:** `scripts/git-hooks/commit-msg`

Delegates to `scripts/lint/commit-message.sh` to validate each commit message
against Conventional Commits format. Allowed types: `feat`, `fix`, `docs`,
`style`, `refactor`, `test`, `chore`.

## CI enforcement

**Workflow:** `.github/workflows/ci.yml`

### `ci: docs-only` detection

Determines whether a pull request contains only documentation changes
(`docs/*`, `README.md`, `CHANGELOG.md`). When true, the `test: unit`
job is skipped.

### `ci: standards-compliance` job

Runs without Python or project dependencies. Steps:

| Step | Script | Condition |
| ---- | ------ | --------- |
| Repository profile validation | `scripts/lint/repo-profile.sh` | Always |
| Markdown standards | `scripts/lint/markdown-standards.sh` | Always |
| Commit message format | `scripts/lint/commit-messages.sh` | Pull requests only |
| Issue linkage | `scripts/lint/pr-issue-linkage.sh` | Pull requests only |

### `ci: dependency-audit` job

Runs `pip-audit` against `requirements.txt` and `requirements-dev.txt` to
detect known vulnerabilities.

### `test: unit` job

Skipped for docs-only changes. Otherwise runs:

- Version string policy (`scripts/dev/validate_version.py`)
- Dependency specification validation (`scripts/dev/validate_dependency_specs.py`)
- Lock file sync (`uv lock --check`)
- Ruff linter and formatter
- mypy and ty type checkers
- pytest with 100% branch coverage requirement

## Validation scripts

### Lint scripts

Located in `scripts/lint/`. These are pure bash scripts with no Python
dependency.

| Script | Purpose |
| ------ | ------- |
| `commit-message.sh` | Validates a single commit message file against Conventional Commits |
| `commit-messages.sh` | Validates all commits between two refs (base and head) |
| `markdown-standards.sh` | Runs markdownlint and custom AWK validation (one H1, TOC required, no heading skips) |
| `repo-profile.sh` | Validates `docs/repository-standards.md` contains required attributes without placeholders |
| `pr-issue-linkage.sh` | Validates PR body includes `Fixes #N` or `Ref #N` (CI only, reads `GITHUB_EVENT_PATH`) |

### Development scripts

Located in `scripts/dev/`. These require Python and are used locally or in CI.

| Script | Purpose |
| ------ | ------- |
| `validate_local.py` | Orchestrates all CI hard gates locally; accepts `--base-ref` for version validation |
| `validate_docs.py` | Docs-only validation; runs markdownlint on discovered markdown files |
| `validate_venv.py` | Validates virtual environment integrity (uv version, tool presence, shebangs) |
| `validate_version.py` | Enforces semantic versioning policy against base branch |
| `validate_dependency_specs.py` | Ensures version-constrained dependencies have anchor documentation |

## Configuration

| File | Purpose |
| ---- | ------- |
| `.markdownlint.json` | Disables MD013 (line length) for markdownlint |
| `docs/repository-standards.md` | Repository profile validated by `repo-profile.sh` |
| `pyproject.toml` | Ruff, mypy, and pytest configuration |
