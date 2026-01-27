# MQSC to PCF parameter extraction: Cmdserv

## Table of Contents
- [Purpose](#purpose)
- [First-run extraction](#first-run-extraction)

## Purpose
Collect MQSC and PCF parameter mappings for cmdserv commands, split from the first-run extraction to keep each qualifier readable.

## First-run extraction
```yaml
version: 1
generated_at: 2026-01-11T23:40:29Z
commands:
  - mqsc:
      name: DISPLAY CMDSERV
      href: SSFKSJ_9.4.0/refadmin/q086120_.html
      positional_parameters: []
      input_parameters: []
      output_parameters: []
      section_sources:
        {}
    pcf:
      command: MQCMD_INQUIRE_CMDSERV
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
  - mqsc:
      name: START CMDSERV
      href: SSFKSJ_9.4.0/refadmin/q086690_.html
      positional_parameters: []
      input_parameters: []
      output_parameters: []
      section_sources:
        {}
    pcf:
      command: MQCMD_START_CMDSERV
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
  - mqsc:
      name: STOP CMDSERV
      href: SSFKSJ_9.4.0/refadmin/q086780_.html
      positional_parameters: []
      input_parameters: []
      output_parameters: []
      section_sources:
        {}
    pcf:
      command: MQCMD_STOP_CMDSERV
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







