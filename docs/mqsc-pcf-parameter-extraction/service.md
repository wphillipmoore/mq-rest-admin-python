# MQSC to PCF parameter extraction: Service

## Table of Contents

- [Purpose](#purpose)
- [First-run extraction](#first-run-extraction)
- [Service command re-parse](#service-command-re-parse)

## Purpose

Collect MQSC and PCF parameter mappings for service commands, split from the first-run extraction to keep each qualifier readable.

## First-run extraction

```yaml
version: 1
generated_at: 2026-01-11T23:40:29Z
commands:
  - mqsc:
      name: ALTER SERVICE
      href: SSFKSJ_9.4.0/refadmin/q085390_.html
      positional_parameters:
        - (service-name)
        - service-name
        - string
      input_parameters:
        - CONTROL
        - DESCR
        - LIKE
        - NOREPLACE
        - REPLACE
        - SERVTYPE
        - STARTARG
        - STARTCMD
        - STDERR
        - STDOUT
        - STOPARG
        - STOPCMD
      output_parameters: []
      section_sources:
        'Parameter descriptions for ALTER SERVICE':
          - CONTROL
          - DESCR
          - LIKE
          - NOREPLACE
          - REPLACE
          - SERVTYPE
          - STARTARG
          - STARTCMD
          - STDERR
          - STDOUT
          - STOPARG
          - STOPCMD
    pcf:
      command: MQCMD_CHANGE_SERVICE
      request_href: SSFKSJ_9.4.0/refadmin/q087030_.html
      response_href: null
      request_parameters:
        - name: ServiceName
          pcf_type: MQCFST
          type_hint: str
        - name: FromServiceName
          pcf_type: MQCFST
          type_hint: str
        - name: ToServiceName
          pcf_type: MQCFST
          type_hint: str
        - name: Replace
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQRP_YES
            - MQRP_NO
        - name: ServiceDesc
          pcf_type: MQCFST
          type_hint: str
        - name: ServiceType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSVC_TYPE_SERVER
            - MQSVC_TYPE_COMMAND
        - name: StartArguments
          pcf_type: MQCFST
          type_hint: str
        - name: StartCommand
          pcf_type: MQCFST
          type_hint: str
        - name: StartMode
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSVC_CONTROL_MANUAL
            - MQSVC_CONTROL_Q_MGR
            - MQSVC_CONTROL_Q_MGR_START
        - name: StderrDestination
          pcf_type: MQCFST
          type_hint: str
        - name: StdoutDestination
          pcf_type: MQCFST
          type_hint: str
        - name: StopArguments
          pcf_type: MQCFST
          type_hint: str
        - name: StopCommand
          pcf_type: MQCFST
          type_hint: str
      response_parameters: []
    mapping:
      request:
        suggested:
          REPLACE: Replace
        ambiguous:
          NOREPLACE:
            - Replace
          SERVTYPE:
            - ServiceType
        unmapped:
          - CONTROL
          - DESCR
          - LIKE
          - STARTARG
          - STARTCMD
          - STDERR
          - STDOUT
          - STOPARG
          - STOPCMD
        pcf_unmapped:
          - FromServiceName
          - ServiceDesc
          - ServiceName
          - ServiceType
          - StartArguments
          - StartCommand
          - StartMode
          - StderrDestination
          - StdoutDestination
          - StopArguments
          - StopCommand
          - ToServiceName
      response:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped: []
    notes: []
  - mqsc:
      name: DEFINE SERVICE
      href: SSFKSJ_9.4.0/refadmin/q085740_.html
      positional_parameters:
        - (service-name)
        - service-name
        - string
      input_parameters:
        - CONTROL
        - DESCR
        - LIKE
        - NOREPLACE
        - REPLACE
        - SERVTYPE
        - STARTARG
        - STARTCMD
        - STDERR
        - STDOUT
        - STOPARG
        - STOPCMD
      output_parameters: []
      section_sources:
        'Parameter descriptions for DEFINE SERVICE':
          - CONTROL
          - DESCR
          - LIKE
          - NOREPLACE
          - REPLACE
          - SERVTYPE
          - STARTARG
          - STARTCMD
          - STDERR
          - STDOUT
          - STOPARG
          - STOPCMD
    pcf:
      command: MQCMD_CREATE_SERVICE
      request_href: SSFKSJ_9.4.0/refadmin/q087030_.html
      response_href: null
      request_parameters:
        - name: ServiceName
          pcf_type: MQCFST
          type_hint: str
        - name: FromServiceName
          pcf_type: MQCFST
          type_hint: str
        - name: ToServiceName
          pcf_type: MQCFST
          type_hint: str
        - name: Replace
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQRP_YES
            - MQRP_NO
        - name: ServiceDesc
          pcf_type: MQCFST
          type_hint: str
        - name: ServiceType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSVC_TYPE_SERVER
            - MQSVC_TYPE_COMMAND
        - name: StartArguments
          pcf_type: MQCFST
          type_hint: str
        - name: StartCommand
          pcf_type: MQCFST
          type_hint: str
        - name: StartMode
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSVC_CONTROL_MANUAL
            - MQSVC_CONTROL_Q_MGR
            - MQSVC_CONTROL_Q_MGR_START
        - name: StderrDestination
          pcf_type: MQCFST
          type_hint: str
        - name: StdoutDestination
          pcf_type: MQCFST
          type_hint: str
        - name: StopArguments
          pcf_type: MQCFST
          type_hint: str
        - name: StopCommand
          pcf_type: MQCFST
          type_hint: str
      response_parameters: []
    mapping:
      request:
        suggested:
          REPLACE: Replace
        ambiguous:
          NOREPLACE:
            - Replace
          SERVTYPE:
            - ServiceType
        unmapped:
          - CONTROL
          - DESCR
          - LIKE
          - STARTARG
          - STARTCMD
          - STDERR
          - STDOUT
          - STOPARG
          - STOPCMD
        pcf_unmapped:
          - FromServiceName
          - ServiceDesc
          - ServiceName
          - ServiceType
          - StartArguments
          - StartCommand
          - StartMode
          - StderrDestination
          - StdoutDestination
          - StopArguments
          - StopCommand
          - ToServiceName
      response:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped: []
    notes: []
  - mqsc:
      name: DELETE SERVICE
      href: SSFKSJ_9.4.0/refadmin/q085940_.html
      positional_parameters:
        - service-name
      input_parameters:
        - IGNSTATE
      output_parameters: []
      section_sources:
        'Keyword and parameter descriptions for DELETE SERVICE':
          - IGNSTATE
    pcf:
      command: MQCMD_DELETE_SERVICE
      request_href: SSFKSJ_9.4.0/refadmin/q087190_.html
      response_href: SSFKSJ_9.4.0/refadmin/q087190_.html
      request_parameters:
        - name: ServiceName
          pcf_type: MQCFST
          type_hint: str
        - name: IgnoreState
          pcf_type: MQCFST
          type_hint: str
          enum_values:
            - MQIS_YES
            - MQIS_NO
      response_parameters:
        - name: ServiceName
          pcf_type: MQCFST
          type_hint: str
        - name: IgnoreState
          pcf_type: MQCFST
          type_hint: str
          enum_values:
            - MQIS_YES
            - MQIS_NO
    mapping:
      request:
        suggested:
          {}
        ambiguous:
          IGNSTATE:
            - IgnoreState
        unmapped: []
        pcf_unmapped:
          - IgnoreState
          - ServiceName
      response:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - IgnoreState
          - ServiceName
    notes: []
  - mqsc:
      name: DISPLAY SERVICE
      href: SSFKSJ_9.4.0/refadmin/q086300_.html
      positional_parameters:
        - filter-keyword
        - filter-value
        - generic-service-name
        - operator
      input_parameters: []
      output_parameters:
        - CONTROL
        - WHERE
      section_sources:
        {}
    pcf:
      command: MQCMD_INQUIRE_SERVICE
      request_href: SSFKSJ_9.4.0/refadmin/q087920_.html
      response_href: SSFKSJ_9.4.0/refadmin/q087930_.html
      request_parameters:
        - name: ServiceName
          pcf_type: MQCFST
          type_hint: str
        - name: IntegerFilterCommand
          pcf_type: MQCFIF
          type_hint: null
        - name: ServiceAttrs
          pcf_type: MQCFIL
          type_hint: int
          enum_values:
            - MQIACF_ALL
            - MQCA_ALTERATION_DATE
            - MQCA_ALTERATION_TIME
            - MQCA_SERVICE_DESC
            - MQCA_SERVICE_NAME
            - MQCA_SERVICE_START_ARGS
            - MQCA_SERVICE_START_COMMAND
            - MQCA_SERVICE_STOP_ARGS
            - MQCA_STDERR_DESTINATION
            - MQCA_STDOUT_DESTINATION
            - MQIA_SERVICE_CONTROL
            - MQIA_SERVICE_TYPE
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
        - name: ServiceDesc
          pcf_type: MQCFST
          type_hint: str
        - name: ServiceName
          pcf_type: MQCFST
          type_hint: str
        - name: ServiceType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSVC_TYPE_SERVER
            - MQSVC_TYPE_COMMAND
        - name: StartArguments
          pcf_type: MQCFST
          type_hint: str
        - name: StartCommand
          pcf_type: MQCFST
          type_hint: str
        - name: StartMode
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSVC_CONTROL_MANUAL
            - MQSVC_CONTROL_Q_MGR
            - MQSVC_CONTROL_Q_MGR_START
        - name: StderrDestination
          pcf_type: MQCFST
          type_hint: str
        - name: StdoutDestination
          pcf_type: MQCFST
          type_hint: str
        - name: StopArguments
          pcf_type: MQCFST
          type_hint: str
        - name: StopCommand
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
          - IntegerFilterCommand
          - ServiceAttrs
          - ServiceName
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
          - ServiceDesc
          - ServiceName
          - ServiceType
          - StartArguments
          - StartCommand
          - StartMode
          - StderrDestination
          - StdoutDestination
          - StopArguments
          - StopCommand
    notes: []
  - mqsc:
      name: DISPLAY SVSTATUS
      href: SSFKSJ_9.4.0/refadmin/q086350_.html
      positional_parameters:
        - filter-keyword
        - filter-value
        - generic-service-name
        - operator
      input_parameters: []
      output_parameters:
        - SERVTYPE
        - SERVTYPE(SERVER)
      section_sources:
        {}
    pcf:
      command: MQCMD_INQUIRE_SV_STATUS
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
  - mqsc:
      name: START SERVICE
      href: SSFKSJ_9.4.0/refadmin/q086720_.html
      positional_parameters:
        - service-name
      input_parameters: []
      output_parameters: []
      section_sources:
        {}
    pcf:
      command: MQCMD_START_SERVICE
      request_href: SSFKSJ_9.4.0/refadmin/q088460_.html
      response_href: SSFKSJ_9.4.0/refadmin/q088460_.html
      request_parameters:
        - name: ServiceName
          pcf_type: MQCFST
          type_hint: str
          enum_values:
            - MQIACF_IGNORE_STATE
            - MQIS_NO
            - MQIS_YES
            - MQRCCF_NO_START_CMD
            - MQRCCF_SERVICE_RUNNING
      response_parameters:
        - name: ServiceName
          pcf_type: MQCFST
          type_hint: str
          enum_values:
            - MQIACF_IGNORE_STATE
            - MQIS_NO
            - MQIS_YES
            - MQRCCF_NO_START_CMD
            - MQRCCF_SERVICE_RUNNING
    mapping:
      request:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - ServiceName
      response:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - ServiceName
    notes: []
  - mqsc:
      name: STOP SERVICE
      href: SSFKSJ_9.4.0/refadmin/q086820_.html
      positional_parameters:
        - service-name
      input_parameters: []
      output_parameters: []
      section_sources:
        {}
    pcf:
      command: MQCMD_STOP_SERVICE
      request_href: SSFKSJ_9.4.0/refadmin/q088530_.html
      response_href: SSFKSJ_9.4.0/refadmin/q088530_.html
      request_parameters:
        - name: ServiceName
          pcf_type: MQCFST
          type_hint: str
          enum_values:
            - MQIACF_IGNORE_STATE
            - MQIS_NO
            - MQIS_YES
            - MQRCCF_NO_STOP_CMD
            - MQRCCF_SERVICE_STOPPED
      response_parameters:
        - name: ServiceName
          pcf_type: MQCFST
          type_hint: str
          enum_values:
            - MQIACF_IGNORE_STATE
            - MQIS_NO
            - MQIS_YES
            - MQRCCF_NO_STOP_CMD
            - MQRCCF_SERVICE_STOPPED
    mapping:
      request:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - ServiceName
      response:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - ServiceName
    notes: []
```

## Service command re-parse

This addendum isolates corrected MQSC and PCF parameter sets. It is intentionally separate from the first-run extraction above and omits mapping heuristics.

```yaml
version: 1
generated_at: 2026-01-12T17:42:34Z
commands:
  - mqsc:
      name: ALTER SERVICE
      href: SSFKSJ_9.4.0/refadmin/q085390_.html
      positional_parameters:
        - (service-name)
      input_parameters:
        - CONTROL
        - DESCR
        - SERVTYPE
        - STARTARG
        - STARTCMD
        - STDERR
        - STDOUT
        - STOPARG
        - STOPCMD
      output_parameters: []
      section_sources:
        'Parameter descriptions for ALTER SERVICE':
          - CONTROL
          - DESCR
          - SERVTYPE
          - STARTARG
          - STARTCMD
          - STDERR
          - STDOUT
          - STOPARG
          - STOPCMD
    pcf:
      command: MQCMD_CHANGE_SERVICE
      request_href: SSFKSJ_9.4.0/refadmin/q087030_.html
      response_href: null
      request_parameters:
        - name: ServiceName
          pcf_type: MQCFST
          type_hint: str
        - name: Replace
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQRP_YES
            - MQRP_NO
        - name: ServiceDesc
          pcf_type: MQCFST
          type_hint: str
        - name: ServiceType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSVC_TYPE_SERVER
            - MQSVC_TYPE_COMMAND
        - name: StartArguments
          pcf_type: MQCFST
          type_hint: str
        - name: StartCommand
          pcf_type: MQCFST
          type_hint: str
        - name: StartMode
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSVC_CONTROL_MANUAL
            - MQSVC_CONTROL_Q_MGR
            - MQSVC_CONTROL_Q_MGR_START
        - name: StderrDestination
          pcf_type: MQCFST
          type_hint: str
        - name: StdoutDestination
          pcf_type: MQCFST
          type_hint: str
        - name: StopArguments
          pcf_type: MQCFST
          type_hint: str
        - name: StopCommand
          pcf_type: MQCFST
          type_hint: str
      response_parameters: []
    notes:
      - change-service-excludes-copy-only-parameters
  - mqsc:
      name: DEFINE SERVICE
      href: SSFKSJ_9.4.0/refadmin/q085740_.html
      positional_parameters:
        - (service-name)
      input_parameters:
        - CONTROL
        - DESCR
        - LIKE
        - NOREPLACE
        - REPLACE
        - SERVTYPE
        - STARTARG
        - STARTCMD
        - STDERR
        - STDOUT
        - STOPARG
        - STOPCMD
      output_parameters: []
      section_sources:
        'Parameter descriptions for DEFINE SERVICE':
          - CONTROL
          - DESCR
          - LIKE
          - NOREPLACE
          - REPLACE
          - SERVTYPE
          - STARTARG
          - STARTCMD
          - STDERR
          - STDOUT
          - STOPARG
          - STOPCMD
    pcf:
      command: MQCMD_CREATE_SERVICE
      request_href: SSFKSJ_9.4.0/refadmin/q087030_.html
      response_href: null
      request_parameters:
        - name: ServiceName
          pcf_type: MQCFST
          type_hint: str
        - name: Replace
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQRP_YES
            - MQRP_NO
        - name: ServiceDesc
          pcf_type: MQCFST
          type_hint: str
        - name: ServiceType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSVC_TYPE_SERVER
            - MQSVC_TYPE_COMMAND
        - name: StartArguments
          pcf_type: MQCFST
          type_hint: str
        - name: StartCommand
          pcf_type: MQCFST
          type_hint: str
        - name: StartMode
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSVC_CONTROL_MANUAL
            - MQSVC_CONTROL_Q_MGR
            - MQSVC_CONTROL_Q_MGR_START
        - name: StderrDestination
          pcf_type: MQCFST
          type_hint: str
        - name: StdoutDestination
          pcf_type: MQCFST
          type_hint: str
        - name: StopArguments
          pcf_type: MQCFST
          type_hint: str
        - name: StopCommand
          pcf_type: MQCFST
          type_hint: str
      response_parameters: []
    notes:
      - create-service-excludes-copy-only-parameters
  - mqsc:
      name: DELETE SERVICE
      href: SSFKSJ_9.4.0/refadmin/q085940_.html
      positional_parameters:
        - (service-name)
      input_parameters:
        - IGNSTATE
      output_parameters: []
      section_sources:
        'Keyword and parameter descriptions for DELETE SERVICE':
          - IGNSTATE
    pcf:
      command: MQCMD_DELETE_SERVICE
      request_href: SSFKSJ_9.4.0/refadmin/q087190_.html
      response_href: null
      request_parameters:
        - name: ServiceName
          pcf_type: MQCFST
          type_hint: str
        - name: IgnoreState
          pcf_type: MQCFST
          type_hint: str
          enum_values:
            - MQIS_YES
            - MQIS_NO
      response_parameters: []
    notes:
      - delete-service-response-doc-not-found
  - mqsc:
      name: DISPLAY SERVICE
      href: SSFKSJ_9.4.0/refadmin/q086300_.html
      positional_parameters:
        - (generic-service-name)
      input_parameters:
        - ALL
        - WHERE
      output_parameters:
        - ALTDATE
        - ALTTIME
        - CONTROL
        - DESCR
        - SERVTYPE
        - STARTARG
        - STARTCMD
        - STDERR
        - STDOUT
        - STOPARG
        - STOPCMD
      section_sources:
        'Keyword and parameter descriptions for DISPLAY SERVICE':
          - ALL
          - WHERE
        Requested parameters:
          - ALTDATE
          - ALTTIME
          - CONTROL
          - DESCR
          - SERVTYPE
          - STARTARG
          - STARTCMD
          - STDERR
          - STDOUT
          - STOPARG
          - STOPCMD
    pcf:
      command: MQCMD_INQUIRE_SERVICE
      request_href: SSFKSJ_9.4.0/refadmin/q087920_.html
      response_href: SSFKSJ_9.4.0/refadmin/q087930_.html
      request_parameters:
        - name: ServiceName
          pcf_type: MQCFST
          type_hint: str
        - name: IntegerFilterCommand
          pcf_type: MQCFIF
          type_hint: null
        - name: ServiceAttrs
          pcf_type: MQCFIL
          type_hint: list[int]
          enum_values:
            - MQIACF_ALL
            - MQCA_ALTERATION_DATE
            - MQCA_ALTERATION_TIME
            - MQCA_SERVICE_DESC
            - MQCA_SERVICE_NAME
            - MQCA_SERVICE_START_ARGS
            - MQCA_SERVICE_START_COMMAND
            - MQCA_SERVICE_STOP_ARGS
            - MQCA_STDERR_DESTINATION
            - MQCA_STDOUT_DESTINATION
            - MQIA_SERVICE_CONTROL
            - MQIA_SERVICE_TYPE
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
        - name: ServiceDesc
          pcf_type: MQCFST
          type_hint: str
        - name: ServiceName
          pcf_type: MQCFST
          type_hint: str
        - name: ServiceType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSVC_TYPE_SERVER
            - MQSVC_TYPE_COMMAND
        - name: StartArguments
          pcf_type: MQCFST
          type_hint: str
        - name: StartCommand
          pcf_type: MQCFST
          type_hint: str
        - name: StartMode
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSVC_CONTROL_MANUAL
            - MQSVC_CONTROL_Q_MGR
            - MQSVC_CONTROL_Q_MGR_START
        - name: StderrDestination
          pcf_type: MQCFST
          type_hint: str
        - name: StdoutDestination
          pcf_type: MQCFST
          type_hint: str
        - name: StopArguments
          pcf_type: MQCFST
          type_hint: str
        - name: StopCommand
          pcf_type: MQCFST
          type_hint: str
    notes:
      - serviceattrs-duplicate-mqca-service-start-args-deduped
      - serviceattrs-omits-mqca-service-stop-command
  - mqsc:
      name: DISPLAY SVSTATUS
      href: SSFKSJ_9.4.0/refadmin/q086350_.html
      positional_parameters:
        - (generic-service-name)
      input_parameters:
        - ALL
        - WHERE
      output_parameters:
        - CONTROL
        - DESCR
        - PID
        - SERVTYPE
        - STARTARG
        - STARTCMD
        - STARTDA
        - STARTTI
        - STATUS
        - STDERR
        - STDOUT
        - STOPARG
        - STOPCMD
      section_sources:
        'Keyword and parameter descriptions for DISPLAY SVSTATUS':
          - ALL
          - WHERE
        Requested parameters:
          - CONTROL
          - DESCR
          - PID
          - SERVTYPE
          - STARTARG
          - STARTCMD
          - STARTDA
          - STARTTI
          - STATUS
          - STDERR
          - STDOUT
          - STOPARG
          - STOPCMD
    pcf:
      command: MQCMD_INQUIRE_SERVICE_STATUS
      request_href: SSFKSJ_9.4.0/refadmin/q087940_.html
      response_href: SSFKSJ_9.4.0/refadmin/q087950_.html
      request_parameters:
        - name: ServiceName
          pcf_type: MQCFST
          type_hint: str
        - name: IntegerFilterCommand
          pcf_type: MQCFIF
          type_hint: null
        - name: ServiceStatusAttrs
          pcf_type: MQCFIL
          type_hint: list[int]
          enum_values:
            - MQIACF_ALL
            - MQCA_SERVICE_DESC
            - MQCA_SERVICE_NAME
            - MQCA_SERVICE_START_ARGS
            - MQCA_SERVICE_START_COMMAND
            - MQCA_SERVICE_STOP_ARGS
            - MQCA_SERVICE_STOP_COMMAND
            - MQCA_STDERR_DESTINATION
            - MQCA_STDOUT_DESTINATION
            - MQCACF_SERVICE_START_DATE
            - MQCACF_SERVICE_START_TIME
            - MQIA_SERVICE_CONTROL
            - MQIA_SERVICE_TYPE
            - MQIACF_PROCESS_ID
            - MQIACF_SERVICE_STATUS
        - name: StringFilterCommand
          pcf_type: MQCFSF
          type_hint: null
      response_parameters:
        - name: ProcessId
          pcf_type: MQCFIN
          type_hint: int
        - name: ServiceDesc
          pcf_type: MQCFST
          type_hint: str
        - name: ServiceName
          pcf_type: MQCFST
          type_hint: str
        - name: StartArguments
          pcf_type: MQCFST
          type_hint: str
        - name: StartCommand
          pcf_type: MQCFST
          type_hint: str
        - name: StartDate
          pcf_type: MQCFST
          type_hint: str
        - name: StartMode
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSVC_CONTROL_MANUAL
            - MQSVC_CONTROL_Q_MGR
            - MQSVC_CONTROL_Q_MGR_START
        - name: StartTime
          pcf_type: MQCFST
          type_hint: str
        - name: Status
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSVC_STATUS_STARTING
            - MQSVC_STATUS_RUNNING
            - MQSVC_STATUS_STOPPING
        - name: StderrDestination
          pcf_type: MQCFST
          type_hint: str
        - name: StdoutDestination
          pcf_type: MQCFST
          type_hint: str
        - name: StopArguments
          pcf_type: MQCFST
          type_hint: str
        - name: StopCommand
          pcf_type: MQCFST
          type_hint: str
    notes: []
  - mqsc:
      name: START SERVICE
      href: SSFKSJ_9.4.0/refadmin/q086720_.html
      positional_parameters:
        - (service-name)
      input_parameters:
        - IGNSTATE
      output_parameters: []
      section_sources:
        'Parameter descriptions for START SERVICE':
          - IGNSTATE
    pcf:
      command: MQCMD_START_SERVICE
      request_href: SSFKSJ_9.4.0/refadmin/q088460_.html
      response_href: null
      request_parameters:
        - name: ServiceName
          pcf_type: MQCFST
          type_hint: str
        - name: IgnoreState
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQIS_NO
            - MQIS_YES
      response_parameters: []
    notes:
      - ignore-state-type-inferred-from-mqsc-ignstate
      - ignore-state-name-normalized
  - mqsc:
      name: STOP SERVICE
      href: SSFKSJ_9.4.0/refadmin/q086820_.html
      positional_parameters:
        - (service-name)
      input_parameters:
        - IGNSTATE
      output_parameters: []
      section_sources:
        'Parameter descriptions for STOP SERVICE':
          - IGNSTATE
    pcf:
      command: MQCMD_STOP_SERVICE
      request_href: SSFKSJ_9.4.0/refadmin/q088530_.html
      response_href: null
      request_parameters:
        - name: ServiceName
          pcf_type: MQCFST
          type_hint: str
        - name: IgnoreState
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQIS_NO
            - MQIS_YES
      response_parameters: []
    notes:
      - ignore-state-type-inferred-from-mqsc-ignstate
      - ignore-state-name-normalized
```

## Output-parameter refresh

```yaml
version: 1
generated_at: 2026-01-27T20:30:57Z
commands:
  - name: DISPLAY SERVICE
    output_parameters:
      - CONTROL
      - WHERE
  - name: DISPLAY SVSTATUS
    output_parameters:
      - SERVTYPE
      - SERVTYPE(SERVER)
```
