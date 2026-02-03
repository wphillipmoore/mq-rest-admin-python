# MQSC to PCF parameter extraction: Conn

## Table of Contents

- [Purpose](#purpose)
- [First-run extraction](#first-run-extraction)

## Purpose

Collect MQSC and PCF parameter mappings for conn commands, split from the first-run extraction to keep each qualifier readable.

## First-run extraction

```yaml
version: 1
generated_at: 2026-01-11T23:40:29Z
commands:
  - mqsc:
      name: DISPLAY CONN
      href: SSFKSJ_9.4.0/refadmin/q086140_.html
      positional_parameters:
        - generic-connid
        - qmgr-name
      input_parameters: []
      output_parameters:
        - APPLDESC
        - APPLTAG
        - APPLTYPE
        - ASID
        - ASTATE
        - CHANNEL
        - CLIENTID
        - CONN
        - CONNAME
        - CONNOPTS
        - CONNTAG
        - DEFREADA
        - DEST
        - DESTQMGR
        - EXTURID
        - HSTATE
        - NID
        - OBJNAME
        - OBJTYPE
        - OPENOPTS
        - PID
        - PSBNAME
        - PSTID
        - QMURID
        - QSGDISP
        - READA
        - SUBID
        - SUBNAME
        - TASKNO
        - TID
        - TOPICSTR
        - TRANSID
        - TYPE
        - UOWLOG
        - UOWLOGDA
        - UOWLOGTI
        - UOWSTATE
        - UOWSTDA
        - UOWSTTI
        - URTYPE
        - USERID
        - WHERE
      section_sources:
        {}
    pcf:
      command: MQCMD_INQUIRE_CONN
      request_href: SSFKSJ_9.4.0/refadmin/q087620_.html
      response_href: null
      request_parameters:
        - name: ConnectionId
          pcf_type: MQCFBS
          type_hint: bytes
        - name: GenericConnectionId
          pcf_type: MQCFBS
          type_hint: bytes
        - name: ByteStringFilterCommand
          pcf_type: MQCFBF
          type_hint: null
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: ConnectionAttrs
          pcf_type: MQCFIL
          type_hint: int
          enum_values:
            - MQIACF_ALL
            - MQBACF_CONNECTION_ID
            - MQBACF_CONN_TAG
            - MQBACF_EXTERNAL_UOW_ID
            - MQBACF_ORIGIN_UOW_ID
            - MQBACF_Q_MGR_UOW_ID
            - MQCACF_APPL_TAG
            - MQCACF_ASID
            - MQCACF_ORIGIN_NAME
            - MQCACF_PSB_NAME
            - MQCACF_PST_ID
            - MQCACF_TASK_NUMBER
            - MQCACF_TRANSACTION_ID
            - MQCACF_UOW_LOG_EXTENT_NAME
            - MQCACF_UOW_LOG_START_DATE
            - MQCACF_UOW_LOG_START_TIME
            - MQCACF_UOW_START_DATE
            - MQCACF_UOW_START_TIME
            - MQCACF_USER_IDENTIFIER
            - MQCACH_CHANNEL_NAME
            - MQCACH_CONNECTION_NAME
            - MQIA_APPL_TYPE
            - MQIACF_CONNECT_OPTIONS
            - MQIACF_PROCESS_ID
            - MQIACF_THREAD_ID
            - MQIACF_UOW_STATE
            - MQIACF_UOW_TYPE
            - MQCACF_OBJECT_NAME
            - MQIA_QSG_DISP
            - MQIA_READ_AHEAD
            - MQIA_UR_DISP
            - MQIACF_HANDLE_STATE
            - MQIACF_OBJECT_TYPE
            - MQIACF_OPEN_OPTIONS
        - name: ConnInfoType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQIACF_CONN_INFO_CONN
            - MQIACF_CONN_INFO_HANDLE
            - MQIACF_CONN_INFO_ALL
        - name: IntegerFilterCommand
          pcf_type: MQCFIF
          type_hint: null
        - name: StringFilterCommand
          pcf_type: MQCFSF
          type_hint: null
        - name: URDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSGD_ALL
            - MQQSGD_GROUP
            - MQQSGD_Q_MGR
            - MQRCCF_CONNECTION_ID_ERROR
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
          - ConnInfoType
          - ConnectionAttrs
          - ConnectionId
          - GenericConnectionId
          - IntegerFilterCommand
          - StringFilterCommand
          - URDisposition
      response:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped: []
    notes: []
  - mqsc:
      name: STOP CONN
      href: SSFKSJ_9.4.0/refadmin/q086790_.html
      positional_parameters:
        - connection-identifier
      input_parameters: []
      output_parameters: []
      section_sources:
        {}
    pcf:
      command: MQCMD_STOP_CONN
      request_href: SSFKSJ_9.4.0/refadmin/q088520_.html
      response_href: null
      request_parameters:
        - name: ConnectionId
          pcf_type: MQCFBS
          type_hint: bytes
      response_parameters: []
    mapping:
      request:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - ConnectionId
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
  - name: DISPLAY CONN
    output_parameters:
      - APPLDESC
      - APPLTAG
      - APPLTYPE
      - ASID
      - ASTATE
      - CHANNEL
      - CLIENTID
      - CONN
      - CONNAME
      - CONNOPTS
      - CONNTAG
      - DEFREADA
      - DEST
      - DESTQMGR
      - EXTURID
      - HSTATE
      - NID
      - OBJNAME
      - OBJTYPE
      - OPENOPTS
      - PID
      - PSBNAME
      - PSTID
      - QMURID
      - QSGDISP
      - READA
      - SUBID
      - SUBNAME
      - TASKNO
      - TID
      - TOPICSTR
      - TRANSID
      - TYPE
      - UOWLOG
      - UOWLOGDA
      - UOWLOGTI
      - UOWSTATE
      - UOWSTDA
      - UOWSTTI
      - URTYPE
      - USERID
      - WHERE
```
