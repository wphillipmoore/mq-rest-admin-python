# Developer setup

This guide covers everything needed to develop and test pymqrest
locally.

## Prerequisites

| Tool | Version | Purpose |
| --- | --- | --- |
| Python | 3.12+ | Runtime |
| `uv` | 0.9.26 | Package and environment management |
| Docker | Latest | Local MQ containers (integration tests) |
| `markdownlint` | Latest | Docs validation |
| `git-cliff` | Latest | Changelog generation (releases only) |

Install `uv`:

```bash
python3 -m pip install uv==0.9.26
```

## Required repositories

pymqrest depends on two sibling repositories:

| Repository | Purpose |
| --- | --- |
| [pymqrest](https://github.com/wphillipmoore/mq-rest-admin-python) | This project |
| [standards-and-conventions](https://github.com/wphillipmoore/standards-and-conventions) | Canonical project standards (referenced by `AGENTS.md` and git hooks) |
| [mq-dev-environment](https://github.com/wphillipmoore/mq-dev-environment) | Dockerized MQ test infrastructure (local and CI) |

## Recommended directory layout

Clone all three repositories as siblings:

```text
~/dev/
├── mq-rest-admin-python/
├── standards-and-conventions/
└── mq-dev-environment/
```

```bash
cd ~/dev
git clone https://github.com/wphillipmoore/mq-rest-admin-python.git
git clone https://github.com/wphillipmoore/standards-and-conventions.git
git clone https://github.com/wphillipmoore/mq-dev-environment.git
```

## Initial setup

```bash
cd pymqrest

# Install all dependencies including dev group
uv sync --group dev

# Enable repository git hooks
git config core.hooksPath scripts/git-hooks
```

## Running validation

The full validation suite matches CI hard gates:

```bash
uv run python3 scripts/dev/validate_local.py
```

This runs:

- Virtual environment validation
- Dependency specification validation
- Version validation
- Repository profile linting
- Markdown standards checking
- Commit message validation
- Lock file verification
- Security audit (`pip-audit`)
- Ruff linting and formatting
- mypy strict type checking
- ty type checking
- pytest with 100% branch coverage

For docs-only changes, a lighter validation is available:

```bash
uv run python3 scripts/dev/validate_docs.py
```

## Running integration tests

Integration tests require running MQ containers. Start the containers,
seed test objects, then run the tests:

```bash
# Start both queue managers
./scripts/dev/mq_start.sh

# Seed deterministic test objects
./scripts/dev/mq_seed.sh

# Run integration tests
PYMQREST_RUN_INTEGRATION=1 uv run pytest -m integration
```

See {doc}`local-mq-container` for full container configuration,
credentials, gateway routing, and troubleshooting.

## CI pipeline overview

CI runs on every pull request and enforces the same gates as local
validation. The pipeline includes:

- **Unit tests** on Python 3.12, 3.13, and 3.14
- **Integration tests** against real MQ queue managers via the shared
  `wphillipmoore/mq-dev-environment/.github/actions/setup-mq` action
- **Standards compliance** (ruff, mypy, ty, markdown lint, commit
  messages, repository profile)
- **Dependency audit** (`pip-audit`)
- **Release gates** (version checks, changelog validation) for PRs
  targeting `main`
