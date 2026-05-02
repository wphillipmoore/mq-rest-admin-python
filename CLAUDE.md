# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

**Standards reference**: <https://github.com/wphillipmoore/standards-and-conventions>
— active standards documentation lives in the standard-tooling repository under `docs/`.
Repository profile: `standard-tooling.toml`.

## Memory management

Memory is allowed with human approval. The authoritative policy is in
the user's global `~/.claude/CLAUDE.md` — agents must propose memory
writes and suggest a destination (repo memory, global CLAUDE.md, or
plugin/skill issue) before writing. See that file for the full
workflow.

Available skills:
- `/standard-tooling:memory-init` — set up or update the policy header
  in a project's `MEMORY.md`.
- `/standard-tooling:memory-audit` — structured collaborative review
  of memory files.

## Parallel AI agent development

This repository supports running multiple Claude Code agents in parallel via
git worktrees. The convention keeps parallel agents' working trees isolated
while preserving shared project memory (which Claude Code derives from the
session's starting CWD).

**Canonical spec:**
[`standard-tooling/docs/specs/worktree-convention.md`](https://github.com/wphillipmoore/standard-tooling/blob/develop/docs/specs/worktree-convention.md)
— full rationale, trust model, failure modes, and memory-path implications.
The canonical text lives in `standard-tooling`; this section is the local
on-ramp.

### Structure

```text
~/dev/github/mq-rest-admin-python/        ← sessions ALWAYS start here
  .git/
  CLAUDE.md, src/, tests/, …              ← main worktree (usually `develop`)
  .worktrees/                             ← container for parallel worktrees
    issue-454-adopt-worktree-convention/  ← worktree on feature/454-...
    …
```

### Rules

1. **Sessions always start at the project root.**
   `cd ~/dev/github/mq-rest-admin-python && claude` — never from inside
   `.worktrees/<name>/`. This keeps the memory-path slug stable and shared.
2. **Each parallel agent is assigned exactly one worktree.** The session
   prompt names the worktree (see Agent prompt contract below).
   - For Read / Edit / Write tools: use the worktree's absolute path.
   - For Bash commands that touch files: `cd` into the worktree first,
     or use absolute paths.
3. **The main worktree is read-only.** All edits flow through a worktree
   on a feature branch — the logical endpoint of the standing
   "no direct commits to `develop`" policy.
4. **One worktree per issue.** Don't stack in-flight issues. When a
   branch lands, remove the worktree before starting the next.
5. **Naming: `issue-<N>-<short-slug>`.** `<N>` is the GitHub issue
   number; `<short-slug>` is 2–4 kebab-case tokens.

### Agent prompt contract

When launching a parallel-agent session, use this template (fill in the
placeholders):

```text
You are working on issue #<N>: <issue title>.

Your worktree is: /Users/pmoore/dev/github/mq-rest-admin-python/.worktrees/issue-<N>-<slug>/
Your branch is:   feature/<N>-<slug>

Rules for this session:
- Do all git operations from inside your worktree:
    cd <absolute-worktree-path> && git <command>
- For Read / Edit / Write tools, use the absolute worktree path.
- For Bash commands that touch files, cd into the worktree first
  or use absolute paths.
- Do not edit files at the project root. The main worktree is
  read-only — all changes flow through your worktree on your
  feature branch.
```

All fields are required.

## Project Overview

`pymqrest` is a Python wrapper for the IBM MQ administrative REST API. The project provides a Python mapping layer for MQ REST API attribute translations and command metadata experiments. The current focus is on attribute mapping and metadata modeling.

**Status**: Beta

**Canonical Standards**: This repository follows standards at https://github.com/wphillipmoore/standards-and-conventions (local path: `../standards-and-conventions` if available)

## Development Commands

### Standard Tooling

```bash
git config core.hooksPath ../standard-tooling/scripts/lib/git-hooks  # Enable git hooks
```

Standard-tooling CLI tools (`st-commit`, `st-validate-local`, etc.) are
pre-installed in the dev container images. No local setup required.

### Environment Setup

```bash
# Install dependencies and sync environment
uv sync --group dev
```

### Two-Tier CI Model

Testing is split across two tiers with increasing scope and cost:

**Tier 1 — Local pre-commit (seconds):** Fast smoke tests in a single
container. Enforced via the `.githooks` pre-commit gate on every commit.
No MQ, no matrix.

```bash
./scripts/dev/test.sh        # Unit tests in dev-python:3.14
./scripts/dev/lint.sh        # Ruff check + format in dev-python:3.14
./scripts/dev/typecheck.sh   # mypy + ty in dev-python:3.14
./scripts/dev/audit.sh       # pip-audit in dev-python:3.14
```

**Tier 2 — PR CI (~8-10 min):** Triggers on `pull_request`. Full Python
matrix (3.12, 3.13, 3.14), all integration tests, security scanners (CodeQL,
Trivy, Semgrep), standards compliance, and release gates. Workflow:
`.github/workflows/ci.yml`.

Push-CI was retired once `st-validate-local` reached parity with PR-CI.
See wphillipmoore/standard-actions#176 for the parity audit and rationale.

### Validation

```bash
# Run full validation suite (matches CI hard gates)
uv run python3 scripts/dev/validate_local.py

# Docs-only validation (requires markdownlint on PATH)
uv run python3 scripts/dev/validate_docs.py
```

The full validation suite includes:
- Virtual environment validation
- Dependency specification validation
- Version validation
- Repository profile linting
- Markdown standards checking
- Commit message validation
- Lock file verification
- Security audit (pip-audit)
- Ruff linting and formatting
- mypy type checking
- ty type checking
- pytest with 100% coverage requirement

### Testing

```bash
# Run tests with coverage
uv run pytest --cov=pymqrest --cov-report=term-missing --cov-branch --cov-fail-under=100

# Run specific test file
uv run pytest tests/pymqrest/test_session.py

# Run integration tests (requires local MQ container)
MQ_REST_ADMIN_RUN_INTEGRATION=1 uv run pytest -m integration
```

### Linting and Formatting

```bash
# Run Ruff linter
uv run ruff check

# Run Ruff formatter (check only)
uv run ruff format --check .

# Run Ruff formatter (fix)
uv run ruff format .

# Run mypy type checker
uv run mypy src/

# Run ty type checker
uv run ty check src
```

### Publishing

The `publish.yml` workflow triggers on push to `main` and publishes to PyPI via OIDC trusted publishing. It builds with `uv build`, publishes via `pypa/gh-action-pypi-publish`, creates a git tag, and a GitHub Release. The release flow is: `develop` → `release/*` → `main` (merge commit). See `docs/sphinx/development/release-workflow.md` for the full process.

### Local MQ Container

The MQ development environment is owned by the
[mq-rest-admin-dev-environment](https://github.com/wphillipmoore/mq-rest-admin-dev-environment)
repository. Clone it as a sibling directory before running lifecycle
scripts:

```bash
# Prerequisite (one-time)
git clone https://github.com/wphillipmoore/mq-rest-admin-dev-environment.git ../mq-rest-admin-dev-environment

# Start the containerized MQ queue managers
./scripts/dev/mq_start.sh

# Seed deterministic test objects (DEV.* prefix)
./scripts/dev/mq_seed.sh

# Verify REST-based MQSC responses
./scripts/dev/mq_verify.sh

# Stop the queue managers
./scripts/dev/mq_stop.sh

# Reset to clean state (removes data volumes)
./scripts/dev/mq_reset.sh
```

The lifecycle scripts are thin wrappers that delegate to
`../mq-rest-admin-dev-environment`. Override the path with `MQ_DEV_ENV_PATH`.

Container details:
- Queue managers: `QM1` and `QM2`
- QM1 ports: `1414` (MQ listener), `9443` (mqweb console + REST API)
- QM2 ports: `1415` (MQ listener), `9444` (mqweb console + REST API)
- Admin credentials: `mqadmin` / `mqadmin`
- Read-only credentials: `mqreader` / `mqreader`
- QM1 REST base URL: `https://localhost:9443/ibmmq/rest/v2`
- QM2 REST base URL: `https://localhost:9444/ibmmq/rest/v2`
- Object prefix: `DEV.*`

Port assignments are explicit in each `scripts/dev/mq_*.sh` script via
`QM1_REST_PORT`, `QM2_REST_PORT`, `QM1_MQ_PORT`, and `QM2_MQ_PORT` exports.
Python uses the base ports (9443/9444, 1414/1415). See the
[port allocation table](https://github.com/wphillipmoore/mq-rest-admin-common)
in mq-rest-admin-common for the full cross-language map.

## Architecture

### Core Components

**Session Management** (`src/pymqrest/session.py`):
- `MQRESTSession` owns authentication, base URL construction, and request/response handling
- `_run_command_json` is the single internal executor for MQSC commands via `runCommandJSON`
- Supports basic auth and CSRF token handling
- Transport abstraction via `MQRESTTransport` protocol

**Command Methods** (`src/pymqrest/commands.py`):
- `MQRESTCommandMixin` provides ~2000 lines of generated MQSC command wrappers
- Method naming: `<verb>_<qualifier>` (lowercase, spaces to underscores)
- All methods accept optional `name`, `request_parameters`, and `response_parameters`
- `DISPLAY` commands return lists of dict-like objects
- Non-`DISPLAY` commands return `None`

**Attribute Mapping** (`src/pymqrest/mapping.py`):
- Runtime attribute mapping: MQSC ↔ PCF ↔ snake_case translations
- `map_request_attributes()` converts Python-friendly names to MQSC format
- `map_response_attributes()` converts MQSC responses to Python-friendly format
- `MappingIssue` captures translation problems for diagnostics
- `MappingError` raised on mapping failures with detailed issue list

**Mapping Data** (`src/pymqrest/mapping_data.py` + `src/pymqrest/mapping-data.json`):
- `mapping_data.py` is a thin loader that reads `mapping-data.json` at import time
- The JSON file contains all qualifier and attribute mappings
- `_mapping_merge.py` provides `MappingOverrideMode` for runtime mapping overrides

**Authentication** (`src/pymqrest/auth.py`):
- `CertificateAuth` - mutual TLS client certificates
- `LTPAAuth` - LTPA token login (automatic at session creation)
- `BasicAuth` - HTTP Basic authentication
- `Credentials` - union type for all credential types

**Ensure Methods** (`src/pymqrest/ensure.py`):
- Idempotent `ensure_*` methods: DEFINE if missing, ALTER if different, no-op if matching
- `EnsureAction` enum: `CREATED`, `UPDATED`, `UNCHANGED`
- `EnsureResult` dataclass with `action` and `changed` attributes

**Sync Wrappers** (`src/pymqrest/sync.py`):
- Synchronous start/stop/restart with polling until target state is reached
- `SyncConfig` for timeout and poll interval settings
- `SyncResult` with operation performed and timing

**Exceptions** (`src/pymqrest/exceptions.py`):
- `MQRESTError` - base exception
- `MQRESTTransportError` - network/connection failures
- `MQRESTAuthError` - authentication failures
- `MQRESTTimeoutError` - sync polling timeouts
- `MQRESTResponseError` - invalid response format
- `MQRESTCommandError` - MQSC command execution failures

### Key Design Patterns

1. **Single Endpoint**: All MQSC operations go through the `runCommandJSON` REST endpoint
2. **Attribute Mapping Pipeline**: MQSC → PCF → snake_case (bidirectional)
3. **Mapping Opt-Out**: Can be disabled at session creation or per method call
4. **Error Payloads**: Captured for diagnostics
5. **Response Parameters Default**: `["all"]` when omitted

### Generated Code

- `src/pymqrest/commands.py` is generated (methods omit per-method docstrings per ruff config)
- Generation scripts in `scripts/dev/` regenerate code from `MAPPING_DATA`

## Important Implementation Notes

### MQSC Command Execution

The `runCommandJSON` payload structure:
```json
{
  "type": "runCommandJSON",
  "command": "DISPLAY",
  "qualifier": "QLOCAL",
  "name": "QUEUE.NAME",
  "parameters": {},
  "responseParameters": ["all"]
}
```

For queue manager queries, `name` is omitted.

### Mapping Pipeline

When mapping is enabled (default):
1. Request: Python snake_case → MQSC names
2. MQ REST API execution
3. Response: MQSC names → Python snake_case

Mapping can be disabled per-session or per-call with `map_attributes=False`.

### Error Handling

- `DISPLAY` methods return empty lists for missing objects (no exception)
- Queue manager `DISPLAY` methods return `None` for missing objects
- `DEFINE` and `DELETE` methods raise on errors
- Error payloads stored on session for diagnostics

## Key References

**External Documentation**:
- IBM MQ 9.4 administrative REST API
- MQSC command reference
- PCF command formats

## Temporary Workarounds

**Codex Branch Deletion**: The Codex execution harness may reject `git branch -d` even with `sandbox_mode = "danger-full-access"`. Workaround: use `git update-ref -d refs/heads/<branch>` when cleanup is required.
