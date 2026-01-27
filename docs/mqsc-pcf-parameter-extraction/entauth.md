# MQSC to PCF parameter extraction: Entauth

## Table of Contents
- [Purpose](#purpose)
- [First-run extraction](#first-run-extraction)

## Purpose
Collect MQSC and PCF parameter mappings for entauth commands, split from the first-run extraction to keep each qualifier readable.

## First-run extraction
```yaml
version: 1
generated_at: 2026-01-11T23:40:29Z
commands:
  - mqsc:
      name: DISPLAY ENTAUTH
      href: SSFKSJ_9.4.0/refadmin/q086150_.html
      positional_parameters:
        - group-name
        - object-name
        - principal-name
        - service-component
      input_parameters: []
      output_parameters:
        - GROUP
        - OBJTYPE
        - PRINCIPAL
      section_sources:
        {}
    pcf:
      command: MQCMD_INQUIRE_ENTAUTH
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
  - name: DISPLAY ENTAUTH
    output_parameters:
      - GROUP
      - OBJTYPE
      - PRINCIPAL
```
