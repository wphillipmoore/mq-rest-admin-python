# MQSC to PCF parameter extraction: Cfstruct

## Table of Contents
- [Purpose](#purpose)
- [First-run extraction](#first-run-extraction)

## Purpose
Collect MQSC and PCF parameter mappings for cfstruct commands, split from the first-run extraction to keep each qualifier readable.

## First-run extraction
```yaml
version: 1
generated_at: 2026-01-11T23:40:29Z
commands:
  - mqsc:
      name: ALTER CFSTRUCT
      href: SSFKSJ_9.4.0/refadmin/q085160_.html
      positional_parameters:
        - (structure-name)
        - data.set.name.*
        - integer
        - string
      input_parameters:
        - CFCONLOS
        - CFLEVEL
        - DESCR
        - DSBLOCK
        - DSBUFS
        - DSEXPAND
        - DSGROUP
        - OFFLD1SZ
        - OFFLD1TH
        - OFFLD2SZ
        - OFFLD2TH
        - OFFLD3SZ
        - OFFLD3TH
        - OFFLOAD
        - RECAUTO
        - RECOVER
      output_parameters: []
      section_sources:
        'Parameter descriptions for ALTER CFSTRUCT':
          - CFCONLOS
          - CFLEVEL
          - DESCR
          - DSBLOCK
          - DSBUFS
          - DSEXPAND
          - DSGROUP
          - OFFLD1SZ
          - OFFLD1TH
          - OFFLD2SZ
          - OFFLD2TH
          - OFFLD3SZ
          - OFFLD3TH
          - OFFLOAD
          - RECAUTO
          - RECOVER
    pcf:
      command: MQCMD_CHANGE_CF_STRUC
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
          - CFCONLOS
          - CFLEVEL
          - DESCR
          - DSBLOCK
          - DSBUFS
          - DSEXPAND
          - DSGROUP
          - OFFLD1SZ
          - OFFLD1TH
          - OFFLD2SZ
          - OFFLD2TH
          - OFFLD3SZ
          - OFFLD3TH
          - OFFLOAD
          - RECAUTO
          - RECOVER
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
      name: BACKUP CFSTRUCT
      href: SSFKSJ_9.4.0/refadmin/q085460_.html
      positional_parameters:
        - integer
        - structure-name
      input_parameters:
        - CMDSCOPE
        - EXCLINT
      output_parameters: []
      section_sources:
        'Keyword and parameter descriptions for BACKUP CFSTRUCT':
          - CMDSCOPE
          - EXCLINT
    pcf:
      command: null
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
          - EXCLINT
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
      name: DEFINE CFSTRUCT
      href: SSFKSJ_9.4.0/refadmin/q085510_.html
      positional_parameters:
        - (structure-name)
        - cfstruct-name
        - dsname.prefix.*.dsname.suffix
        - integer
        - percentage
        - size
        - string
      input_parameters:
        - CFCONLOS
        - CFLEVEL
        - DESCR
        - DSBLOCK
        - DSBUFS
        - DSEXPAND
        - DSGROUP
        - LIKE
        - NOREPLACE
        - OFFLD1SZ
        - OFFLD1TH
        - OFFLD2SZ
        - OFFLD2TH
        - OFFLD3SZ
        - OFFLD3TH
        - OFFLOAD
        - RECAUTO
        - RECOVER
        - REPLACE
      output_parameters: []
      section_sources:
        'Parameter descriptions for DEFINE CFSTRUCT':
          - CFCONLOS
          - CFLEVEL
          - DESCR
          - DSBLOCK
          - DSBUFS
          - DSEXPAND
          - DSGROUP
          - LIKE
          - NOREPLACE
          - OFFLD1SZ
          - OFFLD1TH
          - OFFLD2SZ
          - OFFLD2TH
          - OFFLD3SZ
          - OFFLD3TH
          - OFFLOAD
          - RECAUTO
          - RECOVER
          - REPLACE
    pcf:
      command: MQCMD_CREATE_CF_STRUC
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
          - CFCONLOS
          - CFLEVEL
          - DESCR
          - DSBLOCK
          - DSBUFS
          - DSEXPAND
          - DSGROUP
          - LIKE
          - NOREPLACE
          - OFFLD1SZ
          - OFFLD1TH
          - OFFLD2SZ
          - OFFLD2TH
          - OFFLD3SZ
          - OFFLD3TH
          - OFFLOAD
          - RECAUTO
          - RECOVER
          - REPLACE
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
      name: DELETE CFSTRUCT
      href: SSFKSJ_9.4.0/refadmin/q085810_.html
      positional_parameters:
        - structure-name
      input_parameters: []
      output_parameters: []
      section_sources:
        {}
    pcf:
      command: MQCMD_DELETE_CF_STRUC
      request_href: SSFKSJ_9.4.0/refadmin/q087110_.html
      response_href: SSFKSJ_9.4.0/refadmin/q087110_.html
      request_parameters:
        - name: CFStrucName
          pcf_type: MQCFST
          type_hint: str
      response_parameters:
        - name: CFStrucName
          pcf_type: MQCFST
          type_hint: str
    mapping:
      request:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
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
    notes: []
  - mqsc:
      name: DISPLAY CFSTRUCT
      href: SSFKSJ_9.4.0/refadmin/q086030_.html
      positional_parameters:
        - generic-structure-name
      input_parameters: []
      output_parameters:
        - ALL
        - CFLEVEL
        - OFFLD1SZ
        - OFFLD1TH
        - OFFLD2SZ
        - OFFLD2TH
        - OFFLD3SZ
        - OFFLD3TH
      section_sources:
        {}
    pcf:
      command: MQCMD_INQUIRE_CF_STRUC
      request_href: SSFKSJ_9.4.0/refadmin/q087350_.html
      response_href: SSFKSJ_9.4.0/refadmin/q087360_.html
      request_parameters:
        - name: CFStrucName
          pcf_type: MQCFST
          type_hint: str
        - name: CFStrucAttrs
          pcf_type: MQCFIL
          type_hint: int
          enum_values:
            - MQIACF_ALL
            - MQCA_ALTERATION_DATE
            - MQCA_ALTERATION_TIME
            - MQIA_CF_CFCONLOS
            - MQIA_CF_LEVEL
            - MQIA_CF_OFFLOAD
            - MQIA_CF_RECOVER
            - MQIA_CF_RECAUTO
            - MQIACF_CF_SMDS_BLOCK_SIZE
            - MQIA_CF_SMDS_BUFFERS
            - MQIACF_CF_SMDS_EXPAND
            - MQCACF_CF_SMDS_GENERIC_NAME
            - MQCA_CF_STRUC_DESC
            - MQCA_CF_STRUC_NAME
        - name: IntegerFilterCommand
          pcf_type: MQCFIF
          type_hint: null
        - name: StringFilterCommand
          pcf_type: MQCFSF
          type_hint: null
      response_parameters:
        - name: AlterationDate
          pcf_type: MQCFST
          type_hint: str
        - name: AlterationTime
          pcf_type: MQCFST
          type_hint: str
        - name: CFConlos
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCFCONLOS_TERMINATE
            - MQCFCONLOS_TOLERATE
            - MQCFCONLOS_ASQMGR
        - name: CFLevel
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - 1
            - 2
            - 3
            - 4
            - 5
        - name: CFStrucDesc
          pcf_type: MQCFST
          type_hint: str
        - name: CFStrucName
          pcf_type: MQCFST
          type_hint: str
        - name: DSBLOCK
          pcf_type: MQCFIN
          type_hint: int
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
        - name: DSGROUP
          pcf_type: MQCFST
          type_hint: str
        - name: OFFLD1SZ
          pcf_type: MQCFST
          type_hint: str
        - name: OFFLD2SZ
          pcf_type: MQCFST
          type_hint: str
        - name: OFFLD3SZ
          pcf_type: MQCFST
          type_hint: str
        - name: OFFLD1TH
          pcf_type: MQCFIN
          type_hint: int
        - name: OFFLD2TH
          pcf_type: MQCFIN
          type_hint: int
        - name: OFFLD3TH
          pcf_type: MQCFIN
          type_hint: int
        - name: Offload
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCFOFFLD_DB2
            - MQCFOFFLD_SMDS
            - MQCFOFFLD_NONE
        - name: RCVDATE
          pcf_type: MQCFST
          type_hint: str
        - name: RCVTIME
          pcf_type: MQCFST
          type_hint: str
        - name: Recauto
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQRECAUTO_YES
            - MQRECAUTO_NO
        - name: Recovery
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCFR_YES
            - MQCFR_NO
    mapping:
      request:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - CFStrucAttrs
          - CFStrucName
          - IntegerFilterCommand
          - StringFilterCommand
      response:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - AlterationDate
          - AlterationTime
          - CFConlos
          - CFLevel
          - CFStrucDesc
          - CFStrucName
          - DSBLOCK
          - DSBUFS
          - DSEXPAND
          - DSGROUP
          - OFFLD1SZ
          - OFFLD1TH
          - OFFLD2SZ
          - OFFLD2TH
          - OFFLD3SZ
          - OFFLD3TH
          - Offload
          - RCVDATE
          - RCVTIME
          - Recauto
          - Recovery
    notes: []
  - mqsc:
      name: RECOVER CFSTRUCT
      href: SSFKSJ_9.4.0/refadmin/q086460_.html
      positional_parameters:
        - qmgr-name
        - structure-names ...
      input_parameters: []
      output_parameters: []
      section_sources:
        {}
    pcf:
      command: null
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
    notes: []
  - mqsc:
      name: RESET CFSTRUCT
      href: SSFKSJ_9.4.0/refadmin/q086500_.html
      positional_parameters:
        - structure-name
      input_parameters: []
      output_parameters: []
      section_sources:
        {}
    pcf:
      command: MQCMD_RESET_CF_STRUC
      request_href: SSFKSJ_9.4.0/refadmin/q088260_.html
      response_href: SSFKSJ_9.4.0/refadmin/q088260_.html
      request_parameters:
        - name: CFStructName
          pcf_type: MQCFST
          type_hint: str
        - name: Action
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQACT_FAIL
      response_parameters:
        - name: CFStructName
          pcf_type: MQCFST
          type_hint: str
        - name: Action
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQACT_FAIL
    mapping:
      request:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - Action
          - CFStructName
      response:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - Action
          - CFStructName
    notes: []
```













## Output-parameter refresh
```yaml
version: 1
generated_at: 2026-01-27T20:30:57Z
commands:
  - name: DISPLAY CFSTRUCT
    output_parameters:
      - ALL
      - CFLEVEL
      - OFFLD1SZ
      - OFFLD1TH
      - OFFLD2SZ
      - OFFLD2TH
      - OFFLD3SZ
      - OFFLD3TH
```
