# MQSC to PCF parameter extraction: Smds

## Table of Contents

- [Purpose](#purpose)
- [First-run extraction](#first-run-extraction)

## Purpose

Collect MQSC and PCF parameter mappings for smds commands, split from the first-run extraction to keep each qualifier readable.

## First-run extraction

```yaml
version: 1
generated_at: 2026-01-11T23:40:29Z
commands:
  - mqsc:
      name: ALTER SMDS
      href: SSFKSJ_9.4.0/refadmin/q085400_.html
      positional_parameters:
        - qmgr-name
        - structure-name
      input_parameters:
        - CFSTRUCT
        - DSBUFS
        - DSEXPAND
        - SMDS
      output_parameters: []
      section_sources:
        'Parameter descriptions for ALTER SMDS':
          - CFSTRUCT
          - DSBUFS
          - DSEXPAND
          - SMDS
    pcf:
      command: MQCMD_CHANGE_SMDS
      request_href: SSFKSJ_9.4.0/refadmin/q087020_.html
      response_href: SSFKSJ_9.4.0/refadmin/q087020_.html
      request_parameters:
        - name: SMDS
          pcf_type: MQCFST
          type_hint: str
        - name: CFStrucName
          pcf_type: MQCFST
          type_hint: str
        - name: DSBufs
          pcf_type: MQCFIN
          type_hint: int
        - name: DSEXPAND
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQDSE_YES
            - MQDSE_NO
            - MQDSE_DEFAULT
      response_parameters:
        - name: SMDS
          pcf_type: MQCFST
          type_hint: str
        - name: CFStrucName
          pcf_type: MQCFST
          type_hint: str
        - name: DSBufs
          pcf_type: MQCFIN
          type_hint: int
        - name: DSEXPAND
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQDSE_YES
            - MQDSE_NO
            - MQDSE_DEFAULT
    mapping:
      request:
        suggested:
          DSBUFS: DSBufs
          DSEXPAND: DSEXPAND
          SMDS: SMDS
        ambiguous:
          {}
        unmapped:
          - CFSTRUCT
        pcf_unmapped:
          - CFStrucName
      response:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - CFStrucName
          - DSBufs
          - DSEXPAND
          - SMDS
    notes: []
  - mqsc:
      name: DISPLAY SMDS
      href: SSFKSJ_9.4.0/refadmin/q086310_.html
      positional_parameters:
        - filter-keyword
        - filter-value
        - operator
        - qmgr-name
        - structure-name
      input_parameters: []
      output_parameters:
        - CFSTRUCT
        - DSBUFS
        - DSEXPAND
        - SMDS
      section_sources:
        {}
    pcf:
      command: MQCMD_INQUIRE_SMDS
      request_href: SSFKSJ_9.4.0/refadmin/q087960_.html
      response_href: SSFKSJ_9.4.0/refadmin/q087970_.html
      request_parameters:
        - name: CFStrucName
          pcf_type: MQCFST
          type_hint: str
        - name: CFSMDSAttrs
          pcf_type: MQCFIL
          type_hint: int
          enum_values:
            - MQIACF_ALL
            - MQIA_CF_SMDS_BUFFERS
            - MQIACF_CF_SMDS_EXPAND
      response_parameters:
        - name: SMDS
          pcf_type: MQCFST
          type_hint: str
        - name: CFStrucName
          pcf_type: MQCFST
          type_hint: str
        - name: DSBUFS
          pcf_type: MQCFIN
          type_hint: int
        - name: DSEXPAND
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQDSE_YES
            - MQDSE_NO
            - MQDSE_DEFAULT
    mapping:
      request:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - CFSMDSAttrs
          - CFStrucName
      response:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - CFStrucName
          - DSBUFS
          - DSEXPAND
          - SMDS
    notes: []
  - mqsc:
      name: RESET SMDS
      href: SSFKSJ_9.4.0/refadmin/q086550_.html
      positional_parameters:
        - qmgr-name
        - structure-name
      input_parameters: []
      output_parameters: []
      section_sources:
        {}
    pcf:
      command: MQCMD_RESET_SMDS
      request_href: SSFKSJ_9.4.0/refadmin/q088320_.html
      response_href: SSFKSJ_9.4.0/refadmin/q088320_.html
      request_parameters:
        - name: SMDS
          pcf_type: MQCFST
          type_hint: str
        - name: CFStrucName
          pcf_type: MQCFST
          type_hint: str
        - name: Access
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCFACCESS_ENABLED
            - MQCFACCESS_DISABLED
        - name: Status
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCFSTATUS_FAILED
            - MQCFSTATUS_RECOVERED
      response_parameters:
        - name: SMDS
          pcf_type: MQCFST
          type_hint: str
        - name: CFStrucName
          pcf_type: MQCFST
          type_hint: str
        - name: Access
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCFACCESS_ENABLED
            - MQCFACCESS_DISABLED
        - name: Status
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCFSTATUS_FAILED
            - MQCFSTATUS_RECOVERED
    mapping:
      request:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - Access
          - CFStrucName
          - SMDS
          - Status
      response:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - Access
          - CFStrucName
          - SMDS
          - Status
    notes: []
```

## Output-parameter refresh

```yaml
version: 1
generated_at: 2026-02-02T19:46:59Z
commands:
  - name: DISPLAY SMDS
    output_parameters:
      - CFSTRUCT
      - DSBUFS
      - DSEXPAND
      - SMDS
```
