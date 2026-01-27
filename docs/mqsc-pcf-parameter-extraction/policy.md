# MQSC to PCF parameter extraction: Policy

## Table of Contents
- [Purpose](#purpose)
- [First-run extraction](#first-run-extraction)
- [Notes](#notes)

## Purpose
Collect MQSC and PCF parameter mappings for policy commands, split from the first-run extraction to keep each qualifier readable.

## First-run extraction
```yaml
version: 1
generated_at: 2026-01-11T23:40:29Z
commands:
  - mqsc:
      name: DELETE POLICY
      href: SSFKSJ_9.4.0/refadmin/q120810_.html
      positional_parameters:
        - policy-name
      input_parameters:
        - IGNSTATE
      output_parameters: []
      section_sources:
        'Parameter descriptions for DELETE POLICY':
          - IGNSTATE
    pcf:
      command: MQCMD_DELETE_POLICY
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
          - IGNSTATE
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
      name: DISPLAY POLICY
      href: SSFKSJ_9.4.0/refadmin/q120820_.html
      positional_parameters:
        - (policy-name)
      input_parameters: []
      output_parameters:
        - ENCALG
        - ENFORCE
        - KEYREUSE
        - POLICY
        - SIGNALG
      section_sources:
        {}
    pcf:
      command: MQCMD_INQUIRE_POLICY
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
      name: SET POLICY
      href: SSFKSJ_9.4.0/refadmin/q120800_.html
      positional_parameters:
        - (distinguished-name)
        - (policy-name)
      input_parameters: []
      output_parameters: []
      section_sources:
        {}
    pcf:
      command: MQCMD_SET_POLICY
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
generated_at: 2026-01-27T20:30:57Z
commands:
  - name: DISPLAY POLICY
    output_parameters:
      - ENCALG
      - ENFORCE
      - KEYREUSE
      - POLICY
      - SIGNALG
```

## Notes
- `DISPLAY POLICY(*)` returned overallReasonCode 3328 in local MQ REST tests; use explicit policy names for validation (for example, `DISPLAY POLICY(PYMQREST.QLOCAL)`).
