# MQSC to PCF parameter extraction: Cfstatus

## Table of Contents

- [Purpose](#purpose)
- [First-run extraction](#first-run-extraction)

## Purpose

Collect MQSC and PCF parameter mappings for cfstatus commands, split from the first-run extraction to keep each qualifier readable.

## First-run extraction

```yaml
version: 1
generated_at: 2026-01-11T23:40:29Z
commands:
  - mqsc:
      name: DISPLAY CFSTATUS
      href: SSFKSJ_9.4.0/refadmin/q086020_.html
      positional_parameters:
        - (date)
        - (generic-structure-name)
        - (hexadecimal)
        - (integer)
        - (qmgrname)
        - (qmgrname-list)
        - (size)
        - (systemname)
        - (time)
      input_parameters: []
      output_parameters:
        - ACCESS
        - CFTYPE
        - FAILDATE
        - FAILTIME
        - OFFLDUSE
        - RCVDATE
        - RCVTIME
        - SIZEUSED
        - SMDS
        - STATUS
        - TYPE
        - TYPEPURGE
      section_sources:
        {}
    pcf:
      command: MQCMD_INQUIRE_CF_STATUS
      request_href: SSFKSJ_9.4.0/refadmin/q087880_.html
      response_href: null
      request_parameters:
        - name: QName
          pcf_type: MQCFST
          type_hint: str
        - name: ByteStringFilterCommand
          pcf_type: MQCFBF
          type_hint: null
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: IntegerFilterCommand
          pcf_type: MQCFIF
          type_hint: null
        - name: OpenType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSOT_ALL
            - MQQSOT_INPUT
            - MQQSOT_OUTPUT
        - name: QSGDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSGD_COPY
            - MQQSGD_Q_MGR
            - MQQSGD_SHARED
        - name: QStatusAttrs
          pcf_type: MQCFIL
          type_hint: int
          enum_values:
            - MQIACF_ALL
            - MQCA_Q_NAME
            - MQCACF_LAST_GET_DATE
            - MQCACF_LAST_GET_TIME
            - MQCACF_LAST_PUT_DATE
            - MQCACF_LAST_PUT_TIME
            - MQCACF_MEDIA_LOG_EXTENT_NAME
            - MQIA_CURRENT_Q_DEPTH
            - MQIA_MONITORING_Q
            - MQIA_OPEN_INPUT_COUNT
            - MQIA_OPEN_OUTPUT_COUNT
            - MQIACF_HANDLE_STATE
            - MQIACF_MONITORING
            - MQIACF_CUR_MAX_FILE_SIZE
            - MQIACF_OLDEST_MSG_AGE
            - MQIACF_Q_TIME_INDICATOR
            - MQIACF_UNCOMMITTED_MSGS
            - MQBACF_EXTERNAL_UOW_ID
            - MQBACF_Q_MGR_UOW_ID
            - MQCACF_APPL_TAG
            - MQCACF_ASID
            - MQCACF_PSB_NAME
            - MQCACF_PSTID
            - MQCACF_TASK_NUMBER
            - MQCACF_TRANSACTION_ID
            - MQCACF_USER_IDENTIFIER
            - MQCACH_CHANNEL_NAME
            - MQCACH_CONNECTION_NAME
            - MQIA_APPL_TYPE
            - MQIACF_OPEN_BROWSE
            - MQIACF_OPEN_INPUT_TYPE
            - MQIACF_OPEN_INQUIRE
            - MQIACF_OPEN_OPTIONS
            - MQIACF_OPEN_OUTPUT
            - MQIACF_OPEN_SET
            - MQIACF_PROCESS_ID
            - MQIACF_ASYNC_STATE
            - MQIACF_THREAD_ID
            - MQIACF_UOW_TYPE
        - name: StatusType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQIACF_Q_STATUS
            - MQIACF_Q_HANDLE
        - name: StringFilterCommand
          pcf_type: MQCFSF
          type_hint: null
          enum_values:
            - MQRCCF_Q_TYPE_ERROR
      response_parameters: []
    mapping:
      request:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - ByteStringFilterCommand
          - CommandScope
          - IntegerFilterCommand
          - OpenType
          - QName
          - QSGDisposition
          - QStatusAttrs
          - StatusType
          - StringFilterCommand
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
generated_at: 2026-02-02T19:46:59Z
commands:
  - name: DISPLAY CFSTATUS
    output_parameters:
      - ACCESS
      - CFTYPE
      - FAILDATE
      - FAILTIME
      - OFFLDUSE
      - RCVDATE
      - RCVTIME
      - SIZEUSED
      - SMDS
      - STATUS
      - TYPE
      - TYPEPURGE
```
