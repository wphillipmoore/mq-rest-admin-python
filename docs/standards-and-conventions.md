# pymqrest Standards and Conventions

This repository follows the canonical standards at:
https://github.com/wphillipmoore/standards-and-conventions

## Table of Contents
- [Canonical references](#canonical-references)
  - [Core references (always required)](#core-references-always-required)
  - [Repository-type references (required for the declared type)](#repository-type-references-required-for-the-declared-type)
  - [Additional required references](#additional-required-references)
- [Project-specific overlay](#project-specific-overlay)
  - [AI co-authors](#ai-co-authors)
  - [Repository profile](#repository-profile)
  - [Local validation](#local-validation)
  - [Tooling requirement](#tooling-requirement)

## Canonical references

### Core references (always required)
- https://github.com/wphillipmoore/standards-and-conventions/blob/develop/docs/foundation/markdown-standards.md
- https://github.com/wphillipmoore/standards-and-conventions/blob/develop/docs/code-management/repository-types-and-attributes.md
- https://github.com/wphillipmoore/standards-and-conventions/blob/develop/docs/code-management/commit-messages-and-authorship.md
- https://github.com/wphillipmoore/standards-and-conventions/blob/develop/docs/code-management/github-issues.md
- https://github.com/wphillipmoore/standards-and-conventions/blob/develop/docs/code-management/pull-request-workflow.md
- https://github.com/wphillipmoore/standards-and-conventions/blob/develop/docs/code-management/source-control-guidelines.md

### Repository-type references (required for the declared type)
- https://github.com/wphillipmoore/standards-and-conventions/blob/develop/docs/code-management/library-branching-and-release.md
- https://github.com/wphillipmoore/standards-and-conventions/blob/develop/docs/code-management/library-versioning-scheme.md

### Additional required references
- https://github.com/wphillipmoore/standards-and-conventions/blob/develop/docs/development/environment-and-tooling.md
- https://github.com/wphillipmoore/standards-and-conventions/blob/develop/docs/development/python/overview.md

## Project-specific overlay

### AI co-authors

- Co-Authored-By: wphillipmoore-codex <255923655+wphillipmoore-codex@users.noreply.github.com>
- Co-Authored-By: wphillipmoore-claude <255925739+wphillipmoore-claude@users.noreply.github.com>

### Repository profile

- repository_type: library
- versioning_scheme: library
- branching_model: library-release
- release_model: artifact-publishing
- supported_release_lines: current and previous

### Local validation

- `python3 scripts/dev/validate_local.py`
- Docs-only changes: `python3 scripts/dev/validate_docs.py`
- Docs-only validation requires `markdownlint` `0.41.0` on the PATH or `npx`
  to run the pinned version.

### Tooling requirement

- `uv` `0.9.26` (install with `python3 -m pip install uv==0.9.26`).
