# MQSC to PCF parameter extraction: Thread

## Table of Contents

- [Purpose](#purpose)
- [First-run extraction](#first-run-extraction)

## Purpose

Collect MQSC and PCF parameter mappings for thread commands, split from the first-run extraction to keep each qualifier readable.

## First-run extraction

```yaml
version: 1
generated_at: 2026-01-11T23:40:29Z
commands:
  - mqsc:
      name: DISPLAY THREAD
      href: SSFKSJ_9.4.0/refadmin/q086370_.html
      positional_parameters:
        - (*)
        - (connection-name)
        - qmgr-name
      input_parameters: []
      output_parameters:
        - CMDSCOPE
        - QMNAME
        - TYPE
      section_sources:
        {}
    pcf:
      command: MQCMD_INQUIRE_THREAD
      request_href: SSFKSJ_9.4.0/refdev/q091020_.html
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
    notes: []
```

## Output-parameter refresh

```yaml
version: 1
generated_at: 2026-02-02T19:46:59Z
commands:
  - name: DISPLAY THREAD
    output_parameters:
      - CMDSCOPE
      - QMNAME
      - TYPE
```
