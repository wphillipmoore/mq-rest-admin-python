# Contributing

This project welcomes contributions from humans working with or without
AI assistance. AI tooling is available but not required.

## Branching and workflow

All contributors follow the same branching model:

- Branch from `develop` using `feature/*`, `bugfix/*`, `hotfix/*`, or
  `chore/*` prefixes.
- Commit messages follow
  [conventional commits](https://www.conventionalcommits.org/) and are
  validated by CI.
- PR body must include `Fixes #N` or `Ref #N` (validated by CI).
- Feature PRs: squash merge to `develop`.
- Release PRs: regular merge to `main` (preserves shared ancestry).

See [release workflow](release-workflow.md) for the full release process.

## Code quality gates

Every PR must pass these gates, enforced both locally and in CI:

| Gate | Tool |
| --- | --- |
| Linting | Ruff with all rules enabled (`select = ["ALL"]`) |
| Formatting | Ruff format |
| Type checking | mypy (strict) and ty |
| Test coverage | pytest with 100% branch coverage |
| Security audit | pip-audit |
| Markdown lint | markdownlint |
| Commit messages | Conventional commit validation |

Run the full suite locally before pushing:

```bash
uv run python3 scripts/dev/validate_local.py
```

For docs-only changes:

```bash
uv run python3 scripts/dev/validate_docs.py
```

## For human contributors

- Run `validate_local.py` before pushing to catch issues early.
- Reference `docs/repository-standards.md` for the full standards
  specification.
- The `CLAUDE.md` and `AGENTS.md` files document architecture,
  patterns, and key design decisions. They are useful as reference
  material even when not using an AI agent.
- After changing mapping data in `mapping_data.py`, regenerate
  downstream artifacts. See [generation scripts](generation-scripts.md) for the
  regeneration workflow.

## For AI agent contributors

### Agent entry points

- **Claude Code**: reads `CLAUDE.md`, which loads repository standards
  via include directives.
- **Codex and other agents**: reads `AGENTS.md`, which loads the same
  standards plus shared skills from the `standards-and-conventions`
  repository.

### Quality expectations

AI-generated code must pass all the same validation gates listed
above. There are no exceptions.

### What AI agents handle well

- Code generation from mapping data
- Test writing and coverage gap filling
- Linting and formatting fixes
- Refactoring with consistent patterns
- PR creation and submission

### What requires human judgment

- Architectural decisions and API design
- MQ domain knowledge and MQSC semantics
- Release decisions and version management
- Mapping data curation (attribute names, value translations)

### Co-author trailers

AI agents add co-author trailers to commits automatically when
following the repository standards.
