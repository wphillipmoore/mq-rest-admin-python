# MQSC to PCF parameter extraction: Trace

## Table of Contents

- [Purpose](#purpose)
- [First-run extraction](#first-run-extraction)

## Purpose

Collect MQSC and PCF parameter mappings for trace commands, split from the first-run extraction to keep each qualifier readable.

## First-run extraction

```yaml
version: 1
generated_at: 2026-01-11T23:40:29Z
commands:
  - mqsc:
      name: ALTER TRACE
      href: SSFKSJ_9.4.0/refadmin/q085440_.html
      positional_parameters:
        - ifcid
        - integer
        - string
      input_parameters:
        - ACCTG
        - CMDSCOPE
        - GLOBAL
        - STAT
        - TNO
      output_parameters: []
      section_sources:
        'Parameter descriptions for ALTER TRACE':
          - ACCTG
          - CMDSCOPE
          - GLOBAL
          - STAT
          - TNO
        'Trace parameters':
          - CLASS
          - COMMENT
          - IFCID
    pcf:
      command: MQCMD_CHANGE_TRACE
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
        unmapped:
          - ACCTG
          - CMDSCOPE
          - GLOBAL
          - STAT
          - TNO
        pcf_unmapped: []
      response:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped: []
    notes: []
  - mqsc:
      name: DISPLAY TRACE
      href: SSFKSJ_9.4.0/refadmin/q086400_.html
      positional_parameters:
        - integer
        - output-type
        - qmgr-name
        - string
      input_parameters: []
      output_parameters:
        - ACCTG
        - CHINIT
        - CLASS
        - CMDSCOPE
        - COMMENT
        - DEST
        - DETAIL
        - GLOBAL
        - GTF
        - RES
        - RMID
        - SMF
        - SRV
        - STAT
        - TNO
        - USERID
      section_sources:
        {}
    pcf:
      command: MQCMD_INQUIRE_TRACE
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
  - mqsc:
      name: START TRACE
      href: SSFKSJ_9.4.0/refadmin/q086740_.html
      positional_parameters:
        - integer
        - qmgr-name
        - string
        - userid
      input_parameters: []
      output_parameters: []
      section_sources:
        {}
    pcf:
      command: MQCMD_START_TRACE
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
  - mqsc:
      name: STOP TRACE
      href: SSFKSJ_9.4.0/refadmin/q086840_.html
      positional_parameters:
        - integer
        - qmgr-name
        - string
      input_parameters: []
      output_parameters: []
      section_sources:
        {}
    pcf:
      command: MQCMD_STOP_TRACE
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
generated_at: 2026-01-27T20:30:57Z
commands:
  - name: DISPLAY TRACE
    output_parameters:
      - ACCTG
      - CHINIT
      - CLASS
      - CMDSCOPE
      - COMMENT
      - DEST
      - DETAIL
      - GLOBAL
      - GTF
      - RES
      - RMID
      - SMF
      - SRV
      - STAT
      - TNO
      - USERID
```
