# pymqrest Repository Standards

## Table of Contents
- [Pre-flight checklist](#pre-flight-checklist)
- [AI co-authors](#ai-co-authors)
- [Repository profile](#repository-profile)
- [Local validation](#local-validation)
- [Tooling requirement](#tooling-requirement)

## Pre-flight checklist
- Before modifying any files, check the current branch with `git status -sb`.
- If on `develop`, create a short-lived `feature/*` branch or ask for explicit approval to proceed on `develop`.
- If approval is granted to work on `develop`, call it out in the response and proceed only for that user-approved scope.

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
- `python3 scripts/dev/validate_local.py`
- Docs-only changes: `python3 scripts/dev/validate_docs.py`
- Docs-only validation requires `markdownlint` `0.41.0` on the PATH or `npx`
  to run the pinned version.

## Tooling requirement
- `uv` `0.9.26` (install with `python3 -m pip install uv==0.9.26`).
