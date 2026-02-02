# MQSC to PCF parameter extraction: Buffpool

## Table of Contents

- [Purpose](#purpose)
- [First-run extraction](#first-run-extraction)

## Purpose

Collect MQSC and PCF parameter mappings for buffpool commands, split from the first-run extraction to keep each qualifier readable.

## First-run extraction

```yaml
version: 1
generated_at: 2026-01-11T23:40:29Z
commands:
  - mqsc:
      name: ALTER BUFFPOOL
      href: SSFKSJ_9.4.0/refadmin/q085150_.html
      positional_parameters:
        - (buf-pool-id)
        - integer
      input_parameters:
        - BUFFERS
        - LOC
        - LOCATION
        - PAGECLAS
      output_parameters: []
      section_sources:
        'Parameter descriptions for ALTER BUFFPOOL':
          - BUFFERS
          - LOC
          - LOCATION
          - PAGECLAS
    pcf:
      command: MQCMD_CHANGE_BUFFPOOL
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
          - BUFFERS
          - LOC
          - LOCATION
          - PAGECLAS
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
      name: DEFINE BUFFPOOL
      href: SSFKSJ_9.4.0/refadmin/q085500_.html
      positional_parameters:
        - (buf-pool-id)
        - 4KB
        - ABOVE
        - BELOW
        - FIXED4KB
        - integer
      input_parameters:
        - BUFFERS
        - LOC
        - LOCATION
        - NOREPLACE
        - PAGECLAS
        - REPLACE
      output_parameters: []
      section_sources:
        'Parameter descriptions for DEFINE BUFFPOOL':
          - BUFFERS
          - LOC
          - LOCATION
          - NOREPLACE
          - PAGECLAS
          - REPLACE
    pcf:
      command: MQCMD_CREATE_BUFFPOOL
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
          - BUFFERS
          - LOC
          - LOCATION
          - NOREPLACE
          - PAGECLAS
          - REPLACE
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
      name: DELETE BUFFPOOL
      href: SSFKSJ_9.4.0/refadmin/q085800_.html
      positional_parameters:
        - integer
      input_parameters: []
      output_parameters: []
      section_sources:
        {}
    pcf:
      command: MQCMD_DELETE_BUFFPOOL
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
