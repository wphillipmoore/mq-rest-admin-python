# mq-rest-admin-python Agent Instructions

**Standards reference**: <https://github.com/vergil-project/vergil-tooling>
— active standards documentation lives in the vergil-tooling repository under `docs/`.
Repository profile: `vergil.toml`.

## User Overrides (Optional)

If `~/AGENTS.md` exists and is readable, load it and apply it as a
user-specific overlay for this session. If it cannot be read, say so
briefly and continue.

## Canonical Standards

This repository follows the canonical standards and conventions in the
`vergil-tooling` repository.

Resolve the local path (preferred):
- `../vergil-tooling`

If the local path is unavailable, use the canonical web source:
- https://github.com/vergil-project/vergil-tooling

If the canonical standards cannot be retrieved, treat it as a fatal
exception and stop.

## Shared Skills

Replace `<standards-repo-path>` with the resolved local path when available.
- Load all skills from: `<standards-repo-path>/skills/**/SKILL.md`
- Treat every skill found under that directory as available and active.

## Local Overrides

None.
