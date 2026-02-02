# MQSC to PCF parameter extraction: Listener

## Table of Contents

- [Purpose](#purpose)
- [First-run extraction](#first-run-extraction)
- [Listener command re-parse](#listener-command-re-parse)

## Purpose

Collect MQSC and PCF parameter mappings for listener commands, split from the first-run extraction to keep each qualifier readable.

## First-run extraction

```yaml
version: 1
generated_at: 2026-01-11T23:40:29Z
commands:
  - mqsc:
      name: ALTER LISTENER
      href: SSFKSJ_9.4.0/refadmin/q085280_.html
      positional_parameters:
        - (listener-name)
        - integer
        - listener-name
        - string
      input_parameters:
        - ADAPTER
        - BACKLOG
        - COMMANDS
        - CONTROL
        - DESCR
        - IPADDR
        - LIKE
        - LOCLNAME
        - NTBNAMES
        - PORT
        - SESSIONS
        - SOCKET
        - TPNAME
        - TRPTYPE
      output_parameters: []
      section_sources:
        'Parameter descriptions for ALTER LISTENER':
          - ADAPTER
          - BACKLOG
          - COMMANDS
          - CONTROL
          - DESCR
          - IPADDR
          - LIKE
          - LOCLNAME
          - NTBNAMES
          - PORT
          - SESSIONS
          - SOCKET
          - TPNAME
          - TRPTYPE
    pcf:
      command: MQCMD_CHANGE_LISTENER
      request_href: SSFKSJ_9.4.0/refadmin/q086950_.html
      response_href: null
      request_parameters:
        - name: ListenerName
          pcf_type: MQCFST
          type_hint: str
        - name: TransportType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQXPT_TCP
            - MQXPT_LU62
            - MQXPT_NETBIOS
            - MQXPT_SPX
        - name: FromListenerName
          pcf_type: MQCFST
          type_hint: str
        - name: ToListenerName
          pcf_type: MQCFST
          type_hint: str
        - name: Adapter
          pcf_type: MQCFIN
          type_hint: int
        - name: Backlog
          pcf_type: MQCFIN
          type_hint: int
        - name: Commands
          pcf_type: MQCFIN
          type_hint: int
        - name: IPAddress
          pcf_type: MQCFST
          type_hint: str
        - name: ListenerDesc
          pcf_type: MQCFST
          type_hint: str
        - name: LocalName
          pcf_type: MQCFST
          type_hint: str
        - name: NetbiosNames
          pcf_type: MQCFIN
          type_hint: int
        - name: Port
          pcf_type: MQCFIN
          type_hint: int
        - name: Replace
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQRP_YES
            - MQRP_NO
        - name: Sessions
          pcf_type: MQCFIN
          type_hint: int
        - name: Socket
          pcf_type: MQCFIN
          type_hint: int
        - name: StartMode
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSVC_CONTROL_MANUAL
            - MQSVC_CONTROL_Q_MGR
            - MQSVC_CONTROL_Q_MGR_START
        - name: TPName
          pcf_type: MQCFST
          type_hint: str
      response_parameters: []
    mapping:
      request:
        suggested:
          ADAPTER: Adapter
          BACKLOG: Backlog
          COMMANDS: Commands
          LOCLNAME: LocalName
          PORT: Port
          SESSIONS: Sessions
          SOCKET: Socket
          TPNAME: TPName
        ambiguous:
          {}
        unmapped:
          - CONTROL
          - DESCR
          - IPADDR
          - LIKE
          - NTBNAMES
          - TRPTYPE
        pcf_unmapped:
          - FromListenerName
          - IPAddress
          - ListenerDesc
          - ListenerName
          - NetbiosNames
          - Replace
          - StartMode
          - ToListenerName
          - TransportType
      response:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped: []
    notes: []
  - mqsc:
      name: DEFINE LISTENER
      href: SSFKSJ_9.4.0/refadmin/q085630_.html
      positional_parameters:
        - (listener-name)
        - integer
        - listener-name
        - string
      input_parameters:
        - ADAPTER
        - BACKLOG
        - COMMANDS
        - CONTROL
        - DESCR
        - IPADDR
        - LIKE
        - LOCLNAME
        - NTBNAMES
        - PORT
        - SESSIONS
        - SOCKET
        - TPNAME
        - TRPTYPE
      output_parameters: []
      section_sources:
        'Parameter descriptions for DEFINE LISTENER':
          - ADAPTER
          - BACKLOG
          - COMMANDS
          - CONTROL
          - DESCR
          - IPADDR
          - LIKE
          - LOCLNAME
          - NTBNAMES
          - PORT
          - SESSIONS
          - SOCKET
          - TPNAME
          - TRPTYPE
    pcf:
      command: MQCMD_CREATE_LISTENER
      request_href: SSFKSJ_9.4.0/refadmin/q086950_.html
      response_href: null
      request_parameters:
        - name: ListenerName
          pcf_type: MQCFST
          type_hint: str
        - name: TransportType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQXPT_TCP
            - MQXPT_LU62
            - MQXPT_NETBIOS
            - MQXPT_SPX
        - name: FromListenerName
          pcf_type: MQCFST
          type_hint: str
        - name: ToListenerName
          pcf_type: MQCFST
          type_hint: str
        - name: Adapter
          pcf_type: MQCFIN
          type_hint: int
        - name: Backlog
          pcf_type: MQCFIN
          type_hint: int
        - name: Commands
          pcf_type: MQCFIN
          type_hint: int
        - name: IPAddress
          pcf_type: MQCFST
          type_hint: str
        - name: ListenerDesc
          pcf_type: MQCFST
          type_hint: str
        - name: LocalName
          pcf_type: MQCFST
          type_hint: str
        - name: NetbiosNames
          pcf_type: MQCFIN
          type_hint: int
        - name: Port
          pcf_type: MQCFIN
          type_hint: int
        - name: Replace
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQRP_YES
            - MQRP_NO
        - name: Sessions
          pcf_type: MQCFIN
          type_hint: int
        - name: Socket
          pcf_type: MQCFIN
          type_hint: int
        - name: StartMode
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSVC_CONTROL_MANUAL
            - MQSVC_CONTROL_Q_MGR
            - MQSVC_CONTROL_Q_MGR_START
        - name: TPName
          pcf_type: MQCFST
          type_hint: str
      response_parameters: []
    mapping:
      request:
        suggested:
          ADAPTER: Adapter
          BACKLOG: Backlog
          COMMANDS: Commands
          LOCLNAME: LocalName
          PORT: Port
          SESSIONS: Sessions
          SOCKET: Socket
          TPNAME: TPName
        ambiguous:
          {}
        unmapped:
          - CONTROL
          - DESCR
          - IPADDR
          - LIKE
          - NTBNAMES
          - TRPTYPE
        pcf_unmapped:
          - FromListenerName
          - IPAddress
          - ListenerDesc
          - ListenerName
          - NetbiosNames
          - Replace
          - StartMode
          - ToListenerName
          - TransportType
      response:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped: []
    notes: []
  - mqsc:
      name: DELETE LISTENER
      href: SSFKSJ_9.4.0/refadmin/q085850_.html
      positional_parameters:
        - listener-name
      input_parameters:
        - IGNSTATE
      output_parameters: []
      section_sources:
        'Keyword and parameter descriptions for DELETE LISTENER':
          - IGNSTATE
    pcf:
      command: MQCMD_DELETE_LISTENER
      request_href: SSFKSJ_9.4.0/refadmin/q087140_.html
      response_href: SSFKSJ_9.4.0/refadmin/q087140_.html
      request_parameters:
        - name: ListenerName
          pcf_type: MQCFST
          type_hint: str
        - name: IgnoreState
          pcf_type: MQCFST
          type_hint: str
          enum_values:
            - MQIS_YES
            - MQIS_NO
      response_parameters:
        - name: ListenerName
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
          - ListenerName
      response:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - IgnoreState
          - ListenerName
    notes: []
  - mqsc:
      name: DISPLAY LISTENER
      href: SSFKSJ_9.4.0/refadmin/q086170_.html
      positional_parameters:
        - filter-keyword
        - filter-value
        - generic-listener-name
        - operator
      input_parameters: []
      output_parameters:
        - TRPTYPE
      section_sources:
        {}
    pcf:
      command: MQCMD_INQUIRE_LISTENER
      request_href: SSFKSJ_9.4.0/refadmin/q087480_.html
      response_href: SSFKSJ_9.4.0/refadmin/q087490_.html
      request_parameters:
        - name: ListenerName
          pcf_type: MQCFST
          type_hint: str
        - name: IntegerFilterCommand
          pcf_type: MQCFIF
          type_hint: null
        - name: ListenerAttrs
          pcf_type: MQCFIL
          type_hint: int
          enum_values:
            - MQIACF_ALL
            - MQCA_ALTERATION_DATE
            - MQCA_ALTERATION_TIME
            - MQCACH_IP_ADDRESS
            - MQCACH_LISTENER_DESC
            - MQCACH_LISTENER_NAME
            - MQCACH_LOCAL_NAME
            - MQCACH_TP_NAME
            - MQIACH_ADAPTER
            - MQIACH_BACKLOG
            - MQIACH_COMMAND_COUNT
            - MQIACH_LISTENER_CONTROL
            - MQIACH_NAME_COUNT
            - MQIACH_PORT
            - MQIACH_SESSION_COUNT
            - MQIACH_SOCKET
        - name: StringFilterCommand
          pcf_type: MQCFSF
          type_hint: null
        - name: TransportType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQXPT_ALL
            - MQXPT_LU62
            - MQXPT_NETBIOS
            - MQXPT_SPX
            - MQXPT_TCP
      response_parameters:
        - name: AlterationDate
          pcf_type: MQCFST
          type_hint: str
        - name: AlterationTime
          pcf_type: MQCFST
          type_hint: str
        - name: Adapter
          pcf_type: MQCFIN
          type_hint: int
        - name: Backlog
          pcf_type: MQCFIN
          type_hint: int
        - name: Commands
          pcf_type: MQCFIN
          type_hint: int
        - name: IPAddress
          pcf_type: MQCFST
          type_hint: str
        - name: ListenerDesc
          pcf_type: MQCFST
          type_hint: str
        - name: ListenerName
          pcf_type: MQCFST
          type_hint: str
        - name: LocalName
          pcf_type: MQCFST
          type_hint: str
        - name: NetbiosNames
          pcf_type: MQCFIN
          type_hint: int
        - name: Port
          pcf_type: MQCFIN
          type_hint: int
        - name: Sessions
          pcf_type: MQCFIN
          type_hint: int
        - name: Socket
          pcf_type: MQCFIN
          type_hint: int
        - name: StartMode
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSVC_CONTROL_MANUAL
            - MQSVC_CONTROL_Q_MGR
            - MQSVC_CONTROL_Q_MGR_START
        - name: TPName
          pcf_type: MQCFST
          type_hint: str
        - name: TransportType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQXPT_TCP
            - MQXPT_LU62
            - MQXPT_NETBIOS
            - MQXPT_SPX
    mapping:
      request:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - IntegerFilterCommand
          - ListenerAttrs
          - ListenerName
          - StringFilterCommand
          - TransportType
      response:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - Adapter
          - AlterationDate
          - AlterationTime
          - Backlog
          - Commands
          - IPAddress
          - ListenerDesc
          - ListenerName
          - LocalName
          - NetbiosNames
          - Port
          - Sessions
          - Socket
          - StartMode
          - TPName
          - TransportType
    notes: []
  - mqsc:
      name: DISPLAY LSSTATUS
      href: SSFKSJ_9.4.0/refadmin/q086190_.html
      positional_parameters:
        - filter-keyword
        - filter-value
        - generic-listener-name
        - operator
      input_parameters: []
      output_parameters:
        - ADAPTER
        - BACKLOG
        - CONTROL
        - DESCR
        - IPADDR
        - LISTENER
        - LOCLNAME
        - NTBNAMES
        - PID
        - PORT
        - SESSIONS
        - SOCKET
        - STARTDA
        - STARTTI
        - STATUS
        - TPNAME
        - TRPTYPE
      section_sources:
        {}
    pcf:
      command: MQCMD_INQUIRE_LS_STATUS
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
      name: START LISTENER
      href: SSFKSJ_9.4.0/refadmin/q086700_.html
      positional_parameters:
        - name
        - port-number
        - qmgr-name
        - string
      input_parameters: []
      output_parameters: []
      section_sources:
        {}
    pcf:
      command: MQCMD_START_LISTENER
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
      name: STOP LISTENER
      href: SSFKSJ_9.4.0/refadmin/q086800_.html
      positional_parameters:
        - name
        - qmgr-name
      input_parameters: []
      output_parameters: []
      section_sources:
        {}
    pcf:
      command: MQCMD_STOP_LISTENER
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

## Listener command re-parse

This addendum isolates corrected MQSC and PCF parameter sets. It is intentionally separate from the first-run extraction above and omits mapping heuristics.

```yaml
version: 1
generated_at: 2026-01-12T18:51:34Z
commands:
  - mqsc:
      name: ALTER LISTENER
      href: SSFKSJ_9.4.0/refadmin/q085280_.html
      positional_parameters:
        - (listener-name)
      input_parameters:
        - ADAPTER
        - BACKLOG
        - COMMANDS
        - CONTROL
        - DESCR
        - IPADDR
        - LOCLNAME
        - NTBNAMES
        - PORT
        - SESSIONS
        - SOCKET
        - TPNAME
        - TRPTYPE
      output_parameters: []
      section_sources:
        'Parameter descriptions for ALTER LISTENER':
          - ADAPTER
          - BACKLOG
          - COMMANDS
          - CONTROL
          - DESCR
          - IPADDR
          - LOCLNAME
          - NTBNAMES
          - PORT
          - SESSIONS
          - SOCKET
          - TPNAME
          - TRPTYPE
    pcf:
      command: MQCMD_CHANGE_LISTENER
      request_href: SSFKSJ_9.4.0/refadmin/q086950_.html
      response_href: null
      request_parameters:
        - name: ListenerName
          pcf_type: MQCFST
          type_hint: str
        - name: TransportType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQXPT_TCP
            - MQXPT_LU62
            - MQXPT_NETBIOS
            - MQXPT_SPX
        - name: Adapter
          pcf_type: MQCFIN
          type_hint: int
        - name: Backlog
          pcf_type: MQCFIN
          type_hint: int
        - name: Commands
          pcf_type: MQCFIN
          type_hint: int
        - name: IPAddress
          pcf_type: MQCFST
          type_hint: str
        - name: ListenerDesc
          pcf_type: MQCFST
          type_hint: str
        - name: LocalName
          pcf_type: MQCFST
          type_hint: str
        - name: NetbiosNames
          pcf_type: MQCFIN
          type_hint: int
        - name: Port
          pcf_type: MQCFIN
          type_hint: int
        - name: Replace
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQRP_YES
            - MQRP_NO
        - name: Sessions
          pcf_type: MQCFIN
          type_hint: int
        - name: Socket
          pcf_type: MQCFIN
          type_hint: int
        - name: StartMode
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSVC_CONTROL_MANUAL
            - MQSVC_CONTROL_Q_MGR
            - MQSVC_CONTROL_Q_MGR_START
        - name: TPName
          pcf_type: MQCFST
          type_hint: str
      response_parameters: []
    notes:
      - alter-listener-excludes-like
  - mqsc:
      name: DEFINE LISTENER
      href: SSFKSJ_9.4.0/refadmin/q085630_.html
      positional_parameters:
        - (listener-name)
      input_parameters:
        - ADAPTER
        - BACKLOG
        - COMMANDS
        - CONTROL
        - DESCR
        - IPADDR
        - LIKE
        - LOCLNAME
        - NTBNAMES
        - PORT
        - SESSIONS
        - SOCKET
        - TPNAME
        - TRPTYPE
      output_parameters: []
      section_sources:
        'Parameter descriptions for DEFINE LISTENER':
          - ADAPTER
          - BACKLOG
          - COMMANDS
          - CONTROL
          - DESCR
          - IPADDR
          - LIKE
          - LOCLNAME
          - NTBNAMES
          - PORT
          - SESSIONS
          - SOCKET
          - TPNAME
          - TRPTYPE
    pcf:
      command: MQCMD_CREATE_LISTENER
      request_href: SSFKSJ_9.4.0/refadmin/q086950_.html
      response_href: null
      request_parameters:
        - name: ListenerName
          pcf_type: MQCFST
          type_hint: str
        - name: TransportType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQXPT_TCP
            - MQXPT_LU62
            - MQXPT_NETBIOS
            - MQXPT_SPX
        - name: Adapter
          pcf_type: MQCFIN
          type_hint: int
        - name: Backlog
          pcf_type: MQCFIN
          type_hint: int
        - name: Commands
          pcf_type: MQCFIN
          type_hint: int
        - name: IPAddress
          pcf_type: MQCFST
          type_hint: str
        - name: ListenerDesc
          pcf_type: MQCFST
          type_hint: str
        - name: LocalName
          pcf_type: MQCFST
          type_hint: str
        - name: NetbiosNames
          pcf_type: MQCFIN
          type_hint: int
        - name: Port
          pcf_type: MQCFIN
          type_hint: int
        - name: Replace
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQRP_YES
            - MQRP_NO
        - name: Sessions
          pcf_type: MQCFIN
          type_hint: int
        - name: Socket
          pcf_type: MQCFIN
          type_hint: int
        - name: StartMode
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSVC_CONTROL_MANUAL
            - MQSVC_CONTROL_Q_MGR
            - MQSVC_CONTROL_Q_MGR_START
        - name: TPName
          pcf_type: MQCFST
          type_hint: str
      response_parameters: []
    notes:
      - create-listener-excludes-copy-only-parameters
  - mqsc:
      name: DELETE LISTENER
      href: SSFKSJ_9.4.0/refadmin/q085850_.html
      positional_parameters:
        - (listener-name)
      input_parameters:
        - IGNSTATE
      output_parameters: []
      section_sources:
        'Keyword and parameter descriptions for DELETE LISTENER':
          - IGNSTATE
    pcf:
      command: MQCMD_DELETE_LISTENER
      request_href: SSFKSJ_9.4.0/refadmin/q087140_.html
      response_href: null
      request_parameters:
        - name: ListenerName
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
      - delete-listener-response-doc-not-found
  - mqsc:
      name: DISPLAY LISTENER
      href: SSFKSJ_9.4.0/refadmin/q086170_.html
      positional_parameters:
        - (generic-listener-name)
      input_parameters:
        - ALL
        - TRPTYPE
        - WHERE
      output_parameters:
        - ADAPTER
        - ALTDATE
        - ALTTIME
        - BACKLOG
        - COMMANDS
        - CONTROL
        - DESCR
        - IPADDR
        - LOCLNAME
        - NTBNAMES
        - PORT
        - SESSIONS
        - SOCKET
        - TPNAME
      section_sources:
        'Keyword and parameter descriptions for DISPLAY LISTENER':
          - ALL
          - TRPTYPE
          - WHERE
        Requested parameters:
          - ADAPTER
          - ALTDATE
          - ALTTIME
          - BACKLOG
          - COMMANDS
          - CONTROL
          - DESCR
          - IPADDR
          - LOCLNAME
          - NTBNAMES
          - PORT
          - SESSIONS
          - SOCKET
          - TPNAME
    pcf:
      command: MQCMD_INQUIRE_LISTENER
      request_href: SSFKSJ_9.4.0/refadmin/q087480_.html
      response_href: SSFKSJ_9.4.0/refadmin/q087490_.html
      request_parameters:
        - name: ListenerName
          pcf_type: MQCFST
          type_hint: str
        - name: IntegerFilterCommand
          pcf_type: MQCFIF
          type_hint: null
        - name: ListenerAttrs
          pcf_type: MQCFIL
          type_hint: list[int]
          enum_values:
            - MQIACF_ALL
            - MQCA_ALTERATION_DATE
            - MQCA_ALTERATION_TIME
            - MQCACH_IP_ADDRESS
            - MQCACH_LISTENER_DESC
            - MQCACH_LISTENER_NAME
            - MQCACH_LOCAL_NAME
            - MQCACH_TP_NAME
            - MQIACH_ADAPTER
            - MQIACH_BACKLOG
            - MQIACH_COMMAND_COUNT
            - MQIACH_LISTENER_CONTROL
            - MQIACH_NAME_COUNT
            - MQIACH_PORT
            - MQIACH_SESSION_COUNT
            - MQIACH_SOCKET
        - name: StringFilterCommand
          pcf_type: MQCFSF
          type_hint: null
        - name: TransportType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQXPT_ALL
            - MQXPT_LU62
            - MQXPT_NETBIOS
            - MQXPT_SPX
            - MQXPT_TCP
      response_parameters:
        - name: AlterationDate
          pcf_type: MQCFST
          type_hint: str
        - name: AlterationTime
          pcf_type: MQCFST
          type_hint: str
        - name: Adapter
          pcf_type: MQCFIN
          type_hint: int
        - name: Backlog
          pcf_type: MQCFIN
          type_hint: int
        - name: Commands
          pcf_type: MQCFIN
          type_hint: int
        - name: IPAddress
          pcf_type: MQCFST
          type_hint: str
        - name: ListenerDesc
          pcf_type: MQCFST
          type_hint: str
        - name: ListenerName
          pcf_type: MQCFST
          type_hint: str
        - name: LocalName
          pcf_type: MQCFST
          type_hint: str
        - name: NetbiosNames
          pcf_type: MQCFIN
          type_hint: int
        - name: Port
          pcf_type: MQCFIN
          type_hint: int
        - name: Sessions
          pcf_type: MQCFIN
          type_hint: int
        - name: Socket
          pcf_type: MQCFIN
          type_hint: int
        - name: StartMode
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSVC_CONTROL_MANUAL
            - MQSVC_CONTROL_Q_MGR
            - MQSVC_CONTROL_Q_MGR_START
        - name: TPName
          pcf_type: MQCFST
          type_hint: str
        - name: TransportType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQXPT_TCP
            - MQXPT_LU62
            - MQXPT_NETBIOS
            - MQXPT_SPX
    notes: []
  - mqsc:
      name: DISPLAY LSSTATUS
      href: SSFKSJ_9.4.0/refadmin/q086190_.html
      positional_parameters:
        - (generic-listener-name)
      input_parameters:
        - ALL
        - WHERE
      output_parameters:
        - ADAPTER
        - BACKLOG
        - CONTROL
        - DESCR
        - IPADDR
        - LOCLNAME
        - NTBNAMES
        - PID
        - PORT
        - SESSIONS
        - SOCKET
        - STARTDA
        - STARTTI
        - STATUS
        - TPNAME
        - TRPTYPE
      section_sources:
        'Keyword and parameter descriptions for DISPLAY LSSTATUS':
          - ALL
          - WHERE
        Requested parameters:
          - ADAPTER
          - BACKLOG
          - CONTROL
          - DESCR
          - IPADDR
          - LOCLNAME
          - NTBNAMES
          - PID
          - PORT
          - SESSIONS
          - SOCKET
          - STARTDA
          - STARTTI
          - STATUS
          - TPNAME
          - TRPTYPE
    pcf:
      command: MQCMD_INQUIRE_LISTENER_STATUS
      request_href: SSFKSJ_9.4.0/refadmin/q087500_.html
      response_href: SSFKSJ_9.4.0/refadmin/q087510_.html
      request_parameters:
        - name: ListenerName
          pcf_type: MQCFST
          type_hint: str
        - name: IntegerFilterCommand
          pcf_type: MQCFIF
          type_hint: null
        - name: ListenerStatusAttrs
          pcf_type: MQCFIL
          type_hint: list[int]
          enum_values:
            - MQIACF_ALL
            - MQCACH_IP_ADDRESS
            - MQCACH_LISTENER_DESC
            - MQCACH_LISTENER_NAME
            - MQCACH_LISTENER_START_DATE
            - MQCACH_LISTENER_START_TIME
            - MQCACH_LOCAL_NAME
            - MQCACH_TP_NAME
            - MQIACF_PROCESS_ID
            - MQIACH_ADAPTER
            - MQIACH_BACKLOG
            - MQIACH_COMMAND_COUNT
            - MQIACH_LISTENER_CONTROL
            - MQIACH_LISTENER_STATUS
            - MQIACH_NAME_COUNT
            - MQIACH_PORT
            - MQIACH_SESSION_COUNT
            - MQIACH_SOCKET
            - MQIACH_XMIT_PROTOCOL_TYPE
        - name: StringFilterCommand
          pcf_type: MQCFSF
          type_hint: null
          enum_values:
            - MQRCCF_LSTR_STATUS_NOT_FOUND
      response_parameters:
        - name: Adapter
          pcf_type: MQCFIN
          type_hint: int
        - name: Backlog
          pcf_type: MQCFIN
          type_hint: int
        - name: Commands
          pcf_type: MQCFIN
          type_hint: int
        - name: IPAddress
          pcf_type: MQCFST
          type_hint: str
        - name: ListenerDesc
          pcf_type: MQCFST
          type_hint: str
        - name: ListenerName
          pcf_type: MQCFST
          type_hint: str
        - name: LocalName
          pcf_type: MQCFST
          type_hint: str
        - name: NetbiosNames
          pcf_type: MQCFIN
          type_hint: int
        - name: Port
          pcf_type: MQCFIN
          type_hint: int
        - name: ProcessId
          pcf_type: MQCFIN
          type_hint: int
        - name: Sessions
          pcf_type: MQCFIN
          type_hint: int
        - name: Socket
          pcf_type: MQCFIN
          type_hint: int
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
        - name: TPName
          pcf_type: MQCFST
          type_hint: str
        - name: TransportType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQXPT_TCP
            - MQXPT_LU62
            - MQXPT_NETBIOS
            - MQXPT_SPX
    notes: []
  - mqsc:
      name: START LISTENER
      href: SSFKSJ_9.4.0/refadmin/q086700_.html
      positional_parameters:
        - (name)
      input_parameters:
        - CMDSCOPE
        - INDISP
        - IPADDR
        - LUNAME
        - PORT
        - TRPTYPE
        - IGNSTATE
      output_parameters: []
      section_sources:
        'Parameter descriptions for START LISTENER':
          - CMDSCOPE
          - INDISP
          - IPADDR
          - LUNAME
          - PORT
          - TRPTYPE
          - IGNSTATE
    pcf:
      command: MQCMD_START_CHANNEL_LISTENER
      request_href: SSFKSJ_9.4.0/refadmin/q088450_.html
      response_href: null
      request_parameters:
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: InboundDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQINBD_Q_MGR
            - MQINBD_GROUP
        - name: IPAddress
          pcf_type: MQCFST
          type_hint: str
        - name: ListenerName
          pcf_type: MQCFST
          type_hint: str
        - name: LUName
          pcf_type: MQCFST
          type_hint: str
        - name: Port
          pcf_type: MQCFIN
          type_hint: int
        - name: TransportType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQXPT_LU62
            - MQXPT_TCP
            - MQXPT_NETBIOS
            - MQXPT_SPX
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
      name: STOP LISTENER
      href: SSFKSJ_9.4.0/refadmin/q086800_.html
      positional_parameters:
        - (name)
      input_parameters:
        - CMDSCOPE
        - INDISP
        - IPADDR
        - PORT
        - TRPTYPE
        - IGNSTATE
      output_parameters: []
      section_sources:
        'Parameter descriptions for STOP LISTENER':
          - CMDSCOPE
          - INDISP
          - IPADDR
          - PORT
          - TRPTYPE
          - IGNSTATE
    pcf:
      command: MQCMD_STOP_CHANNEL_LISTENER
      request_href: SSFKSJ_9.4.0/refadmin/q088510_.html
      response_href: null
      request_parameters:
        - name: ListenerName
          pcf_type: MQCFST
          type_hint: str
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: InboundDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQINBD_Q_MGR
            - MQINBD_GROUP
        - name: IPAddress
          pcf_type: MQCFST
          type_hint: str
        - name: Port
          pcf_type: MQCFIN
          type_hint: int
        - name: TransportType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQXPT_LU62
            - MQXPT_TCP
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
  - name: DISPLAY LISTENER
    output_parameters:
      - TRPTYPE
  - name: DISPLAY LSSTATUS
    output_parameters:
      - ADAPTER
      - BACKLOG
      - CONTROL
      - DESCR
      - IPADDR
      - LISTENER
      - LOCLNAME
      - NTBNAMES
      - PID
      - PORT
      - SESSIONS
      - SOCKET
      - STARTDA
      - STARTTI
      - STATUS
      - TPNAME
      - TRPTYPE
```
