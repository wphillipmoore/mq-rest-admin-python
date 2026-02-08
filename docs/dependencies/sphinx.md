# sphinx

## Table of Contents

- [Summary](#summary)
- [Current constraint](#current-constraint)
- [Failure history](#failure-history)
- [Exit criteria](#exit-criteria)

## Summary

Sphinx 8.0 introduced improved MyST Markdown integration and fenced
directive support used by the pymqrest documentation. The `>=8.0`
constraint ensures compatibility with MyST-Parser 4.x and the `furo`
theme.

## Current constraint

`sphinx>=8.0` — added 2026-02-07 when Sphinx documentation was
introduced to the project.

## Failure history

- 2026-02-07: Sphinx 7.x not tested; constraint set proactively to
  match MyST-Parser 4.x compatibility requirements.

## Exit criteria

The lower bound can be removed when either:

- The project no longer requires MyST-Parser 4.x features, or
- Sphinx 7.x is confirmed compatible with the full documentation build.
