# MQSC to PCF parameter extraction: Smdsconn

## Table of Contents

- [Purpose](#purpose)
- [First-run extraction](#first-run-extraction)

## Purpose

Collect MQSC and PCF parameter mappings for smdsconn commands, split from the first-run extraction to keep each qualifier readable.

## First-run extraction

```yaml
version: 1
generated_at: 2026-01-11T23:40:29Z
commands:
  - mqsc:
      name: DISPLAY SMDSCONN
      href: SSFKSJ_9.4.0/refadmin/q086320_.html
      positional_parameters:
        - qmgr-name
        - structure-name
      input_parameters: []
      output_parameters:
        - CFSTRUCT
        - CMDSCOPE
        - DESCR
        - RECOVER
        - WHERE
      section_sources:
        {}
    pcf:
      command: MQCMD_INQUIRE_SMDSCONN
      request_href: SSFKSJ_9.4.0/refadmin/q087980_.html
      response_href: SSFKSJ_9.4.0/refadmin/q087990_.html
      request_parameters:
        - name: SMDSCONN
          pcf_type: MQCFST
          type_hint: str
        - name: CFStrucName
          pcf_type: MQCFST
          type_hint: str
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
      response_parameters:
        - name: SMDSCONN
          pcf_type: MQCFST
          type_hint: str
        - name: CFStrucName
          pcf_type: MQCFST
          type_hint: str
        - name: Avail
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQS_AVAIL_NORMAL
            - MQS_AVAIL_ERROR
            - MQS_AVAIL_STOPPED
        - name: ExpandST
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQS_EXPANDST_NORMAL
            - MQS_EXPANDST_FAILED
            - MQS_EXPANDST_MAXIMUM
        - name: OpenMode
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQS_OPENMODE_NONE
            - MQS_OPENMODE_READONLY
            - MQS_OPENMODE_UPDATE
            - MQS_OPENMODE_RECOVERY
        - name: Status
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQS_STATUS_CLOSED
            - MQS_STATUS_CLOSING
            - MQS_STATUS_OPENING
            - MQS_STATUS_OPEN
            - MQS_STATUS_NOTENABLED
            - MQS_STATUS_ALLOCFAIL
            - MQS_STATUS_OPENFAIL
            - MQS_STATUS_STGFAIL
            - MQS_STATUS_DATAFAIL
    mapping:
      request:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - CFStrucName
          - CommandScope
          - SMDSCONN
      response:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - Avail
          - CFStrucName
          - ExpandST
          - OpenMode
          - SMDSCONN
          - Status
    notes: []
  - mqsc:
      name: START SMDSCONN
      href: SSFKSJ_9.4.0/refadmin/q086730_.html
      positional_parameters:
        - qmgr-name
        - structure-name
      input_parameters: []
      output_parameters: []
      section_sources:
        {}
    pcf:
      command: MQCMD_START_SMDSCONN
      request_href: SSFKSJ_9.4.0/refadmin/q088470_.html
      response_href: SSFKSJ_9.4.0/refadmin/q088470_.html
      request_parameters:
        - name: SMDSConn
          pcf_type: MQCFST
          type_hint: str
        - name: CFStrucName
          pcf_type: MQCFST
          type_hint: str
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
      response_parameters:
        - name: SMDSConn
          pcf_type: MQCFST
          type_hint: str
        - name: CFStrucName
          pcf_type: MQCFST
          type_hint: str
        - name: CommandScope
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
          - CommandScope
          - SMDSConn
      response:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - CFStrucName
          - CommandScope
          - SMDSConn
    notes: []
  - mqsc:
      name: STOP SMDSCONN
      href: SSFKSJ_9.4.0/refadmin/q086830_.html
      positional_parameters:
        - qmgr-name
      input_parameters: []
      output_parameters: []
      section_sources:
        {}
    pcf:
      command: MQCMD_STOP_SMDSCONN
      request_href: SSFKSJ_9.4.0/refadmin/q088540_.html
      response_href: SSFKSJ_9.4.0/refadmin/q088540_.html
      request_parameters:
        - name: SMDSConn
          pcf_type: MQCFST
          type_hint: str
        - name: CFStrucName
          pcf_type: MQCFST
          type_hint: str
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
      response_parameters:
        - name: SMDSConn
          pcf_type: MQCFST
          type_hint: str
        - name: CFStrucName
          pcf_type: MQCFST
          type_hint: str
        - name: CommandScope
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
          - CommandScope
          - SMDSConn
      response:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - CFStrucName
          - CommandScope
          - SMDSConn
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
  - name: DISPLAY SMDSCONN
    output_parameters:
      - CFSTRUCT
      - CMDSCOPE
      - DESCR
      - RECOVER
      - WHERE
```
