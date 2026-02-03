# MQSC to PCF parameter extraction: Authserv

## Table of Contents

- [Purpose](#purpose)
- [First-run extraction](#first-run-extraction)

## Purpose

Collect MQSC and PCF parameter mappings for authserv commands, split from the first-run extraction to keep each qualifier readable.

## First-run extraction

```yaml
version: 1
generated_at: 2026-01-11T23:40:29Z
commands:
  - mqsc:
      name: DISPLAY AUTHSERV
      href: SSFKSJ_9.4.0/refadmin/q086010_.html
      positional_parameters: []
      input_parameters: []
      output_parameters:
        - ALL
        - IFVER
        - SERVCOMP
        - UIDSUPP
      section_sources:
        {}
    pcf:
      command: MQCMD_INQUIRE_AUTHSERV
      request_href: null
      response_href: null
      request_parameters: []
      response_parameters: []
    mapping:
      request:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped: []
      response:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped: []
    notes:
      - pcf-request-doc-not-found
```

## Output-parameter refresh

```yaml
version: 1
generated_at: 2026-02-02T19:46:59Z
commands:
  - name: DISPLAY AUTHSERV
    output_parameters:
      - ALL
      - IFVER
      - SERVCOMP
      - UIDSUPP
```
