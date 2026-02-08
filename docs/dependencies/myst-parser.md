# myst-parser

## Table of Contents

- [Summary](#summary)
- [Current constraint](#current-constraint)
- [Failure history](#failure-history)
- [Exit criteria](#exit-criteria)

## Summary

MyST-Parser 4.0 provides Sphinx 8+ compatibility and the fenced
directive syntax (`colon_fence`, `deflist`, `fieldlist`) used throughout
the pymqrest documentation. The `>=4.0` constraint ensures these
features are available.

## Current constraint

`myst-parser>=4.0` — added 2026-02-07 when Sphinx documentation was
introduced to the project.

## Failure history

- 2026-02-07: MyST-Parser 3.x not tested; constraint set proactively to
  ensure Sphinx 8+ compatibility and fenced directive support.

## Exit criteria

The lower bound can be removed when either:

- The project no longer requires Sphinx 8+ or fenced directives, or
- MyST-Parser 3.x is confirmed compatible with the full documentation
  build.
