# pymqrest Repository Standards

## Table of Contents

- [Pre-flight checklist](#pre-flight-checklist)
- [AI co-authors](#ai-co-authors)
- [Repository profile](#repository-profile)
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

## AI co-authors

- Co-Authored-By: wphillipmoore-codex <255923655+wphillipmoore-codex@users.noreply.github.com>
- Co-Authored-By: wphillipmoore-claude <255925739+wphillipmoore-claude@users.noreply.github.com>

## Repository profile

- repository_type: library
- versioning_scheme: library
- branching_model: library-release
- release_model: artifact-publishing
- supported_release_lines: current and previous

## Local validation

- `uv run python3 scripts/dev/validate_local.py`
- Docs-only changes: `uv run python3 scripts/dev/validate_docs.py`
- Docs-only validation requires `markdownlint` on the PATH.

## Linting policy

- Ruff linting uses `select = ["ALL"]` with scoped, documented ignores in `pyproject.toml`.
- Ruff formatting is enforced in CI and local validation (`ruff format --check`).

## Python invocation

- All Python invocations must run inside the `uv` environment; use `uv run python3 ...`.

## Tooling requirement

Required for daily workflow:

- `uv` `0.9.26` (install with `python3 -m pip install uv==0.9.26`)
- `markdownlint` (required for docs validation and PR pre-submission)

Required for integration testing:

- Docker (for local MQ container environment)

## Merge strategy override

- This repository uses squash merges (`--squash`) instead of the canonical default (`--merge`).
- Use `gh pr merge --auto --squash --delete-branch` for auto-merge.

## Temporary tooling workaround

- The Codex execution harness may reject `git branch -d` even with `sandbox_mode = "danger-full-access"`.
- Workaround: avoid local branch deletion or use `git update-ref -d refs/heads/<branch>` when cleanup is required.
- Treat this as temporary until a Codex update restores command parity.
