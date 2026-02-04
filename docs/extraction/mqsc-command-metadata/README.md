# MQSC command metadata (per-command)

## Table of Contents

- [Purpose](#purpose)
- [Generic name handling](#generic-name-handling)

## Purpose

This directory contains per-command MQSC metadata extracted from IBM Docs and
normalized for mapping work.

## Generic name handling

Many MQSC commands accept a positional object name (for example,
`generic-listener-name` for `DISPLAY LISTENER`). This name is the first
positional argument in our Python methods (for example, `display_listener()`).

Notes and assumptions:

- The positional name is passed as a special value in the REST JSON payload.
- The returned object dictionaries include the object name attribute even when
  it is not listed in the "Requested parameters" section of the MQSC docs.
- The returned attribute name is typically the MQSC object identifier (for
  example, `LISTENER`), which maps to the PCF snake_case name
  (for example, `listener_name`).
- Support for `*` (all objects) varies by command; treat it as command-specific
  and verify against IBM documentation or integration tests.

These behaviors must be verified against the dockerized queue manager and
tracked per command as needed.
