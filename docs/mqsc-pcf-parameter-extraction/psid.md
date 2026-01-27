# MQSC to PCF parameter extraction: Psid

## Table of Contents
- [Purpose](#purpose)
- [First-run extraction](#first-run-extraction)

## Purpose
Collect MQSC and PCF parameter mappings for psid commands, split from the first-run extraction to keep each qualifier readable.

## First-run extraction
```yaml
version: 1
generated_at: 2026-01-11T23:40:29Z
commands:
  - mqsc:
      name: ALTER PSID
      href: SSFKSJ_9.4.0/refadmin/q085310_.html
      positional_parameters:
        - (psid-number)
      input_parameters:
        - EXPAND
      output_parameters: []
      section_sources:
        'Parameter descriptions for ALTER PSID':
          - EXPAND
    pcf:
      command: MQCMD_CHANGE_PSID
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
          - EXPAND
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
      name: DEFINE PSID
      href: SSFKSJ_9.4.0/refadmin/q085680_.html
      positional_parameters:
        - data set name
        - integer
        - psid-number
      input_parameters:
        - BUFFPOOL
        - DSN
        - EXPAND
      output_parameters: []
      section_sources:
        'Parameter descriptions for DEFINE PSID':
          - BUFFPOOL
          - DSN
          - EXPAND
    pcf:
      command: MQCMD_CREATE_PSID
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
          - BUFFPOOL
          - DSN
          - EXPAND
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
      name: DELETE PSID
      href: SSFKSJ_9.4.0/refadmin/q085880_.html
      positional_parameters:
        - psid-number
      input_parameters: []
      output_parameters: []
      section_sources:
        {}
    pcf:
      command: MQCMD_DELETE_PSID
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







