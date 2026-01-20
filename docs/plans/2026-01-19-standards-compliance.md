# Standards compliance plan (2026-01-19)

## Table of Contents
- [Purpose](#purpose)
- [Scope](#scope)
- [Completed work](#completed-work)
- [Remaining work](#remaining-work)
- [Acceptance criteria](#acceptance-criteria)

## Purpose
Bring pymqrest into compliance with the canonical standards and conventions.

## Scope
Documentation-only alignment, plus a concrete plan for required repository
configuration changes.

## Completed work
- Added `docs/standards-and-conventions.md` with canonical references and local
  overlay.
- Updated `AGENTS.md` to reference canonical standards and shared skills.
- Added GitHub Issue Forms:
  - `.github/ISSUE_TEMPLATE/issue.yml`
  - `.github/ISSUE_TEMPLATE/config.yml` with `blank_issues_enabled: false`
- Added pull request template:
  - `.github/pull_request_template.md`
- Implemented CI hard gates with docs-only skip support.
- Documented the canonical local validation command.

## Remaining work
None.

## Acceptance criteria
- Required documentation is in place and references the canonical standards.
- Issue and PR templates exist and match the canonical workflow rules.
- CI hard gates are implemented and enforced as required status checks on the
  protected branches.
