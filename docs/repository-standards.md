# pymqrest Repository Standards

## Table of Contents

- [Pre-flight checklist](#pre-flight-checklist)
- [Local validation](#local-validation)
- [Linting policy](#linting-policy)
- [Python invocation](#python-invocation)
- [Tooling requirement](#tooling-requirement)
- [Merge strategy override](#merge-strategy-override)
- [Temporary tooling workaround](#temporary-tooling-workaround)

## Pre-flight checklist

- Before modifying any files, check the current branch with `git status -sb`.
- If on `develop`, create a short-lived `feature/*` branch or ask for explicit approval to proceed on `develop`.
- If approval is granted to work on `develop`, call it out in the response and proceed only for that user-approved scope.
- Enable repository git hooks before committing: `git config core.hooksPath scripts/git-hooks`.

## Local validation

- `vrg-docker-run -- vrg-validate`

## Linting policy

- Ruff linting uses `select = ["ALL"]` with scoped, documented ignores in `pyproject.toml`.
- Ruff formatting is enforced in CI and local validation (`ruff format --check`).

## Python invocation

- All Python invocations must run inside the `uv` environment; use `uv run python3 ...`.

## Tooling requirement

Required for daily workflow:

- `uv` `0.10.4` (install with `python3 -m pip install uv==0.10.4`)
- `markdownlint` (required for docs validation and PR pre-submission)

Required for integration testing:

- Docker (for local MQ container environment)

## Merge strategy override

- Feature, bugfix, and chore PRs targeting `develop` use squash merges (`--squash`).
- Release PRs targeting `main` use regular merges (`--merge`) to preserve shared
  ancestry between `main` and `develop`.
- Auto-merge commands:
  - Feature PRs: `gh pr merge --auto --squash --delete-branch`
  - Release PRs: `gh pr merge --auto --merge --delete-branch`

## Commit and PR scripts

AI agents **must** use the wrapper scripts for commits and PR
submission. Do not construct commit messages or PR bodies manually.

### Committing

```bash
vrg-commit \
  --type TYPE --message MESSAGE --agent AGENT \
  [--scope SCOPE] [--body BODY]
```

- `--type` (required): one of
  `feat|fix|docs|style|refactor|test|chore|ci|build`
- `--message` (required): commit description
- `--agent` (required): `claude` or `codex`
- `--scope` (optional): conventional commit scope
- `--body` (optional): detailed commit body

The script resolves the correct `Co-Authored-By` identity from
`vergil.toml` and the git hooks validate the result.

### Submitting PRs

```bash
vrg-submit-pr \
  --issue NUMBER --summary TEXT \
  [--linkage KEYWORD] [--title TEXT] \
  [--notes TEXT] [--docs-only] [--dry-run]
```

- `--issue` (required): GitHub issue number (just the number)
- `--summary` (required): one-line PR summary
- `--linkage` (optional, default: `Fixes`):
  `Fixes|Closes|Resolves|Ref`
- `--title` (optional): PR title (default: most recent commit
  subject)
- `--notes` (optional): additional notes
- `--docs-only` (optional): applies docs-only testing exception
- `--dry-run` (optional): print generated PR without executing

The script detects the target branch and merge strategy
automatically.

## Temporary tooling workaround

- The Codex execution harness may reject `git branch -d` even with `sandbox_mode = "danger-full-access"`.
- Workaround: avoid local branch deletion or use `git update-ref -d refs/heads/<branch>` when cleanup is required.
- Treat this as temporary until a Codex update restores command parity.
