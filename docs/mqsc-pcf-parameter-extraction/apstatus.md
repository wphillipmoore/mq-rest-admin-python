# MQSC to PCF parameter extraction: Apstatus

## Table of Contents

- [Purpose](#purpose)
- [First-run extraction](#first-run-extraction)

## Purpose

Collect MQSC and PCF parameter mappings for apstatus commands, split from the first-run extraction to keep each qualifier readable.

## First-run extraction

```yaml
version: 1
generated_at: 2026-01-11T23:40:29Z
commands:
  - mqsc:
      name: DISPLAY APSTATUS
      href: SSFKSJ_9.4.0/refadmin/q133100_.html
      positional_parameters:
        - applicationnamestr
        - value
      input_parameters:
        - ALL
        - TYPE
        - WHERE
      output_parameters:
        - ALL
        - TYPE
        - WHERE
      section_sources:
        'Parameter descriptions for DISPLAY APSTATUS':
          - ALL
          - TYPE
          - WHERE
        'Application status parameters':
          - BALANCED
          - CLUSTER
          - COUNT
          - MOVCOUNT
        'Queue manager status parameters':
          - ACTIVE
          - BALSTATE
          - COUNT
          - LMSGDATE
          - LMSGTIME
          - MOVCOUNT
          - QMID
          - QMNAME
        'Local status parameters':
          - BALOPTS
          - BALTMOUT
          - BALTYPE
          - CONNS
          - CONNTAG
          - IMMCOUNT
          - IMMDATE
          - IMMREASN
          - IMMTIME
          - MOVABLE
    pcf:
      command: MQCMD_INQUIRE_AP_STATUS
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
        unmapped:
          - ALL
          - TYPE
          - WHERE
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
    notes:
      - display-parameter-descriptions-treated-as-input
```

## Output-parameter refresh

```yaml
version: 1
generated_at: 2026-01-27T20:30:57Z
commands:
  - name: DISPLAY APSTATUS
    output_parameters:
      - ALL
      - TYPE
      - WHERE
```
