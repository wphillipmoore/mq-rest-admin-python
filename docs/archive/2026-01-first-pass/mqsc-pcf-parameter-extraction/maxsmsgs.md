# MQSC to PCF parameter extraction: Maxsmsgs

## Table of Contents

- [Purpose](#purpose)
- [First-run extraction](#first-run-extraction)

## Purpose

Collect MQSC and PCF parameter mappings for maxsmsgs commands, split from the first-run extraction to keep each qualifier readable.

## First-run extraction

```yaml
version: 1
generated_at: 2026-01-11T23:40:29Z
commands:
  - mqsc:
      name: DEFINE MAXSMSGS
      href: SSFKSJ_9.4.0/refadmin/q085650_.html
      positional_parameters:
        - integer
        - qmgr-name
      input_parameters:
        - CMDSCOPE
      output_parameters: []
      section_sources:
        'Parameter descriptions for DEFINE MAXSMSGS':
          - CMDSCOPE
    pcf:
      command: MQCMD_CREATE_MAXSMSGS
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
        unmapped:
          - CMDSCOPE
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
  - mqsc:
      name: DISPLAY MAXSMSGS
      href: SSFKSJ_9.4.0/refadmin/q086200_.html
      positional_parameters:
        - qmgr-name
      input_parameters: []
      output_parameters:
        - MAXUMSGS
      section_sources:
        {}
    pcf:
      command: MQCMD_INQUIRE_MAXSMSGS
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
  - name: DISPLAY MAXSMSGS
    output_parameters:
      - MAXUMSGS
```
