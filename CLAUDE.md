# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Auto-memory policy

**Do NOT use MEMORY.md.** Claude Code's auto-memory feature stores behavioral
rules outside of version control, making them invisible to code review,
inconsistent across repos, and unreliable across sessions. All behavioral rules,
conventions, and workflow instructions belong in managed, version-controlled
documentation (CLAUDE.md, AGENTS.md, skills, or docs/).

If you identify a pattern, convention, or rule worth preserving:

1. **Stop.** Do not write to MEMORY.md.
2. **Discuss with the user** what you want to capture and why.
3. **Together, decide** the correct managed location (CLAUDE.md, a skill file,
   standards docs, or a new issue to track the gap).

This policy exists because MEMORY.md is per-directory and per-machine — it
creates divergent agent behavior across the multi-repo environment this project
operates in. Consistency requires all guidance to live in shared, reviewable
documentation.

## Shell command policy

**Do NOT use heredocs** (`<<EOF` / `<<'EOF'`) for multi-line arguments to CLI
tools such as `gh`, `git commit`, or `curl`. Heredocs routinely fail due to
shell escaping issues with apostrophes, backticks, and special characters.
Always write multi-line content to a temporary file and pass it via `--body-file`
or `--file` instead.

## Documentation Strategy

This repository uses two complementary approaches for AI agent guidance:

- **AGENTS.md**: Generic AI agent instructions using include directives to force documentation indexing. Contains canonical standards references, shared skills loading, and user override support.
- **CLAUDE.md** (this file): Claude Code-specific guidance with prescriptive commands, architecture details, and development workflows optimized for `/init`.

### Integration Approach

**For Claude Code** (`/init` command):
1. Read CLAUDE.md (this file) first for optimized quick-start guidance
2. Process include directives to load repository standards
3. Reference AGENTS.md for shared skills and canonical standards location
4. Apply layered standards: canonical → project-specific → user overrides

**For other AI agents** (Codex, generic LLMs):
1. Read AGENTS.md first as the primary entry point
2. Process include directives to load all referenced documentation
3. Resolve canonical standards repo path (local or GitHub)
4. Load shared skills from standards repo
5. Apply user overrides from `~/AGENTS.md` if present

**Key differences**:
- **CLAUDE.md**: Prescriptive, command-focused, optimized for `/init`
- **AGENTS.md**: Declarative, include-directive-driven, forces full documentation indexing

Both files share the same underlying standards via include directives, ensuring consistency across all AI agents working in this repository.

### Best Practices for Dual-File Approach

**What goes in AGENTS.md**:
- Include directives for documentation indexing
- Canonical standards repository references
- Shared skills loading instructions
- User override mechanisms
- Minimal, declarative content

**What goes in CLAUDE.md**:
- Claude Code-specific quick-start commands
- Detailed architecture and design patterns
- Implementation notes and common workflows
- Integration guidance between the two files
- More verbose, prescriptive content

**What goes in neither (use includes instead)**:
- Repository standards (keep in `docs/repository-standards.md`)
- Canonical standards (reference external repo)
- Project-specific conventions (keep in referenced docs)

**Maintenance strategy**:
- Update standards in source files, not in AGENTS.md or CLAUDE.md
- Use include directives to pull in shared content
- Keep AGENTS.md minimal and CLAUDE.md focused on Claude Code workflows
- Test both entry points when updating documentation structure

<!-- include: docs/standards-and-conventions.md -->
<!-- include: docs/repository-standards.md -->

## Project Overview

`pymqrest` is a Python wrapper for the IBM MQ administrative REST API. The project provides a Python mapping layer for MQ REST API attribute translations and command metadata experiments. The current focus is on attribute mapping and metadata modeling.

**Status**: Beta

**Canonical Standards**: This repository follows standards at https://github.com/wphillipmoore/standards-and-conventions (local path: `../standards-and-conventions` if available)

## Development Commands

### Standard Tooling

```bash
cd ../standard-tooling && uv sync                                                # Install standard-tooling
export PATH="../standard-tooling/.venv/bin:../standard-tooling/scripts/bin:$PATH" # Put tools on PATH
git config core.hooksPath ../standard-tooling/scripts/lib/git-hooks               # Enable git hooks
```

### Environment Setup

```bash
# Install dependencies and sync environment
uv sync --group dev
```

### Three-Tier CI Model

Testing is split across three tiers with increasing scope and cost:

**Tier 1 — Local pre-commit (seconds):** Fast smoke tests in a single
container. Run before every commit. No MQ, no matrix.

```bash
./scripts/dev/test.sh        # Unit tests in dev-python:3.14
./scripts/dev/lint.sh        # Ruff check + format in dev-python:3.14
./scripts/dev/typecheck.sh   # mypy + ty in dev-python:3.14
./scripts/dev/audit.sh       # pip-audit in dev-python:3.14
```

**Tier 2 — Push CI (~3-5 min):** Triggers automatically on push to
`feature/**`, `bugfix/**`, `hotfix/**`, `chore/**`. Single Python version
(3.14), includes integration tests, no security scanners or release gates.
Workflow: `.github/workflows/ci-push.yml` (calls `ci.yml`).

**Tier 3 — PR CI (~8-10 min):** Triggers on `pull_request`. Full Python
matrix (3.12, 3.13, 3.14), all integration tests, security scanners (CodeQL,
Trivy, Semgrep), standards compliance, and release gates. Workflow:
`.github/workflows/ci.yml`.

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
PYMQREST_RUN_INTEGRATION=1 uv run pytest -m integration
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

## Repository Standards Quick Reference

The include directives at the top of this file load the full repository standards. Key highlights for quick reference:

**Pre-flight Checklist**:
- Check current branch: `git status -sb`
- If on `develop`, create `feature/*` branch or get explicit approval
- Enable git hooks: `git config core.hooksPath ../standard-tooling/scripts/lib/git-hooks`

**Python Invocation**: Always use `uv run python3 <script>`

**Tooling**: `uv` version `0.10.4`

**Code Quality**: Ruff (all rules), mypy (strict), 100% test coverage, Python 3.14+

**Repository Profile**: library, library-release branching, artifact-publishing

See `docs/repository-standards.md` for complete details.

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

## Documentation Indexing Strategy

This repository uses `<!-- include: path/to/file.md -->` directives to force documentation indexing. When you encounter these directives:

1. **Read the referenced files** to understand the full context
2. **Apply layered standards** in order:
   - Canonical standards (from `standards-and-conventions` repo)
   - Project-specific standards (`docs/repository-standards.md`)
   - User overrides (`~/AGENTS.md` if present)
3. **Load shared skills** from `<standards-repo-path>/skills/**/SKILL.md`

The include directives appear in:
- `AGENTS.md` - Includes repository standards and conventions
- `CLAUDE.md` - Includes same standards for Claude Code
- `docs/standards-and-conventions.md` - Includes canonical standards reference

This approach ensures all AI agents (Codex, Claude, etc.) have access to the same foundational documentation.

## Documentation Structure

- `README.md` - Project overview and quick start
- `AGENTS.md` - Generic AI agent instructions with include directives
- `CLAUDE.md` - This file, Claude Code-specific guidance
- `docs/mq-rest-wrapper-design.md` - Detailed design document
- `docs/mq-container-local-dev.md` - Local development with MQ container
- `docs/repository-standards.md` - Project-specific standards (included from AGENTS.md)
- `docs/standards-and-conventions.md` - Canonical standards reference (includes external repo)

## Commit and PR Scripts

**NEVER use raw `git commit`** — always use `st-commit`.
**NEVER use raw `gh pr create`** — always use `st-submit-pr`.

### Committing

```bash
st-commit --type feat --scope session --message "add retry logic" --agent claude
st-commit --type fix --message "correct attribute mapping" --agent claude
```

- `--type` (required): `feat|fix|docs|style|refactor|test|chore|ci|build`
- `--message` (required): commit description
- `--agent` (required): `claude` or `codex` — resolves the correct `Co-Authored-By` identity
- `--scope` (optional): conventional commit scope
- `--body` (optional): detailed commit body

### Submitting PRs

```bash
st-submit-pr --issue 42 --summary "Add retry logic to session"
st-submit-pr --issue 42 --linkage Ref --summary "Update docs" --docs-only
```

- `--issue` (required): GitHub issue number (just the number)
- `--summary` (required): one-line PR summary
- `--linkage` (optional, default: `Fixes`): `Fixes|Closes|Resolves|Ref`
- `--title` (optional): PR title (default: most recent commit subject)
- `--notes` (optional): additional notes
- `--docs-only` (optional): applies docs-only testing exception
- `--dry-run` (optional): print generated PR without executing

## Key References

**Canonical Standards**: https://github.com/wphillipmoore/standards-and-conventions
- Local path (preferred): `../standards-and-conventions`
- Load all skills from: `<standards-repo-path>/skills/**/SKILL.md`

**External Documentation**:
- IBM MQ 9.4 administrative REST API
- MQSC command reference
- PCF command formats

**User Overrides**: `~/AGENTS.md` (optional, applied if present and readable)

## Temporary Workarounds

**Codex Branch Deletion**: The Codex execution harness may reject `git branch -d` even with `sandbox_mode = "danger-full-access"`. Workaround: use `git update-ref -d refs/heads/<branch>` when cleanup is required.
