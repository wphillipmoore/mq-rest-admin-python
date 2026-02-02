# MQSC to PCF parameter extraction: Comminfo

## Table of Contents

- [Purpose](#purpose)
- [First-run extraction](#first-run-extraction)

## Purpose

Collect MQSC and PCF parameter mappings for comminfo commands, split from the first-run extraction to keep each qualifier readable.

## First-run extraction

```yaml
version: 1
generated_at: 2026-01-11T23:40:29Z
commands:
  - mqsc:
      name: ALTER COMMINFO
      href: SSFKSJ_9.4.0/refadmin/q085270_.html
      positional_parameters:
        - (comminfo name)
        - integer
        - string
      input_parameters:
        - BRIDGE
        - CCSID
        - COMMEV
        - DESCR
        - ENCODING
        - GRPADDR
        - MCHBINT
        - MCPROP
        - MONINT
        - MSGHIST
        - NSUBHIST
        - PORT
      output_parameters: []
      section_sources:
        'Parameter descriptions for ALTER COMMINFO':
          - BRIDGE
          - CCSID
          - COMMEV
          - DESCR
          - ENCODING
          - GRPADDR
          - MCHBINT
          - MCPROP
          - MONINT
          - MSGHIST
          - NSUBHIST
          - PORT
    pcf:
      command: MQCMD_CHANGE_COMM_INFO
      request_href: SSFKSJ_9.4.0/reference/q049820_.html
      response_href: SSFKSJ_9.4.0/refadmin/q086960_.html
      request_parameters: []
      response_parameters:
        - name: ComminfoName
          pcf_type: MQCFST
          type_hint: str
        - name: FromComminfoName
          pcf_type: MQCFST
          type_hint: str
        - name: ToComminfoName
          pcf_type: MQCFST
          type_hint: str
        - name: ComminfoName
          pcf_type: MQCFST
          type_hint: str
        - name: Bridge
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMCB_DISABLED
            - MQMCB_ENABLED
        - name: CCSID
          pcf_type: MQCFIN
          type_hint: int
        - name: CommEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
            - MQEVR_EXCEPTION
        - name: Description
          pcf_type: MQCFST
          type_hint: str
        - name: Encoding
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQENC_AS_PUBLISHED
            - MQENC_NORMAL
            - MQENC_REVERSED
            - MQENC_S390
            - MQENC_TNS
        - name: GrpAddress
          pcf_type: MQCFST
          type_hint: str
        - name: MonitorInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: MsgHistory
          pcf_type: MQCFIN
          type_hint: int
        - name: MulticastHeartbeat
          pcf_type: MQCFIN
          type_hint: int
        - name: MulticastPropControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMCP_ALL
            - MQMCP_REPLY
            - MQMCP_USER
            - MQMCP_NONE
            - MQMCP_COMPAT
        - name: NewSubHistory
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQNSH_NONE
            - MQNSH_ALL
        - name: PortNumber
          pcf_type: MQCFIN
          type_hint: int
        - name: Type
          pcf_type: MQCFIN
          type_hint: int
    mapping:
      request:
        suggested:
          {}
        ambiguous:
          {}
        unmapped:
          - BRIDGE
          - CCSID
          - COMMEV
          - DESCR
          - ENCODING
          - GRPADDR
          - MCHBINT
          - MCPROP
          - MONINT
          - MSGHIST
          - NSUBHIST
          - PORT
        pcf_unmapped: []
      response:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - Bridge
          - CCSID
          - CommEvent
          - ComminfoName
          - ComminfoName
          - Description
          - Encoding
          - FromComminfoName
          - GrpAddress
          - MonitorInterval
          - MsgHistory
          - MulticastHeartbeat
          - MulticastPropControl
          - NewSubHistory
          - PortNumber
          - ToComminfoName
          - Type
    notes: []
  - mqsc:
      name: DEFINE COMMINFO
      href: SSFKSJ_9.4.0/refadmin/q085620_.html
      positional_parameters:
        - authinfo-name
        - comminfo name
        - integer
        - string
      input_parameters:
        - BRIDGE
        - CCSID
        - COMMEV
        - DESCR
        - ENCODING
        - GRPADDR
        - LIKE
        - MCHBINT
        - MCPROP
        - MONINT
        - MSGHIST
        - NOREPLACE
        - NSUBHIST
        - PORT
        - REPLACE
        - TYPE
      output_parameters: []
      section_sources:
        'Parameter descriptions for DEFINE COMMINFO':
          - BRIDGE
          - CCSID
          - COMMEV
          - DESCR
          - ENCODING
          - GRPADDR
          - LIKE
          - MCHBINT
          - MCPROP
          - MONINT
          - MSGHIST
          - NOREPLACE
          - NSUBHIST
          - PORT
          - REPLACE
          - TYPE
    pcf:
      command: MQCMD_CREATE_COMM_INFO
      request_href: SSFKSJ_9.4.0/reference/q049820_.html
      response_href: SSFKSJ_9.4.0/refadmin/q086960_.html
      request_parameters: []
      response_parameters:
        - name: ComminfoName
          pcf_type: MQCFST
          type_hint: str
        - name: FromComminfoName
          pcf_type: MQCFST
          type_hint: str
        - name: ToComminfoName
          pcf_type: MQCFST
          type_hint: str
        - name: ComminfoName
          pcf_type: MQCFST
          type_hint: str
        - name: Bridge
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMCB_DISABLED
            - MQMCB_ENABLED
        - name: CCSID
          pcf_type: MQCFIN
          type_hint: int
        - name: CommEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
            - MQEVR_EXCEPTION
        - name: Description
          pcf_type: MQCFST
          type_hint: str
        - name: Encoding
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQENC_AS_PUBLISHED
            - MQENC_NORMAL
            - MQENC_REVERSED
            - MQENC_S390
            - MQENC_TNS
        - name: GrpAddress
          pcf_type: MQCFST
          type_hint: str
        - name: MonitorInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: MsgHistory
          pcf_type: MQCFIN
          type_hint: int
        - name: MulticastHeartbeat
          pcf_type: MQCFIN
          type_hint: int
        - name: MulticastPropControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMCP_ALL
            - MQMCP_REPLY
            - MQMCP_USER
            - MQMCP_NONE
            - MQMCP_COMPAT
        - name: NewSubHistory
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQNSH_NONE
            - MQNSH_ALL
        - name: PortNumber
          pcf_type: MQCFIN
          type_hint: int
        - name: Type
          pcf_type: MQCFIN
          type_hint: int
    mapping:
      request:
        suggested:
          {}
        ambiguous:
          {}
        unmapped:
          - BRIDGE
          - CCSID
          - COMMEV
          - DESCR
          - ENCODING
          - GRPADDR
          - LIKE
          - MCHBINT
          - MCPROP
          - MONINT
          - MSGHIST
          - NOREPLACE
          - NSUBHIST
          - PORT
          - REPLACE
          - TYPE
        pcf_unmapped: []
      response:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - Bridge
          - CCSID
          - CommEvent
          - ComminfoName
          - ComminfoName
          - Description
          - Encoding
          - FromComminfoName
          - GrpAddress
          - MonitorInterval
          - MsgHistory
          - MulticastHeartbeat
          - MulticastPropControl
          - NewSubHistory
          - PortNumber
          - ToComminfoName
          - Type
    notes: []
  - mqsc:
      name: DELETE COMMINFO
      href: SSFKSJ_9.4.0/refadmin/q085840_.html
      positional_parameters:
        - comminfo_name
      input_parameters:
        - IGNSTATE
      output_parameters: []
      section_sources:
        'Parameter descriptions for DELETE COMMINFO':
          - IGNSTATE
    pcf:
      command: MQCMD_DELETE_COMM_INFO
      request_href: SSFKSJ_9.4.0/refadmin/q087150_.html
      response_href: SSFKSJ_9.4.0/refadmin/q087150_.html
      request_parameters:
        - name: ComminfoName
          pcf_type: MQCFST
          type_hint: str
        - name: IgnoreState
          pcf_type: MQCFST
          type_hint: str
          enum_values:
            - MQIS_YES
            - MQIS_NO
      response_parameters:
        - name: ComminfoName
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
          - ComminfoName
          - IgnoreState
      response:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - ComminfoName
          - IgnoreState
    notes: []
  - mqsc:
      name: DISPLAY COMMINFO
      href: SSFKSJ_9.4.0/refadmin/q086130_.html
      positional_parameters:
        - (generic-comminfo-name)
        - filter-keyword
        - filter-value
        - operator
        - string
      input_parameters: []
      output_parameters:
        - ALL
        - TYPE
      section_sources:
        {}
    pcf:
      command: MQCMD_INQUIRE_COMM_INFO
      request_href: SSFKSJ_9.4.0/refadmin/q087600_.html
      response_href: SSFKSJ_9.4.0/refadmin/q087610_.html
      request_parameters:
        - name: ComminfoName
          pcf_type: MQCFST
          type_hint: str
        - name: ComminfoAttrs
          pcf_type: MQCFIL
          type_hint: int
          enum_values:
            - MQIACF_ALL
            - MQIA_CODED_CHAR_SET_ID
            - MQIA_COMM_EVENT
            - MQIA_MCAST_BRIDGE
            - MQIA_MONITOR_INTERVAL
            - MQIACF_ENCODING
            - MQIACH_MC_HB_INTERVAL
            - MQIACH_MSG_HISTORY
            - MQIACH_MULTICAST_PROPERTIES
            - MQIACH_NEW_SUBSCRIBER_HISTORY
            - MQIACH_PORT
            - MQCA_ALTERATION_DATE
            - MQCA_ALTERATION_TIME
            - MQCA_COMM_INFO_DESC
            - MQCA_COMM_INFO_TYPE
            - MQCACH_GROUP_ADDRESS
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
        - name: Bridge
          pcf_type: MQCFIN
          type_hint: int
        - name: CCSID
          pcf_type: MQCFIN
          type_hint: int
        - name: CommEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
            - MQEVR_EXCEPTION
        - name: ComminfoName
          pcf_type: MQCFST
          type_hint: str
        - name: Description
          pcf_type: MQCFST
          type_hint: str
        - name: Encoding
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQENC_AS_PUBLISHED
            - MQENC_NORMAL
            - MQENC_REVERSED
            - MQENC_S390
            - MQENC_TNS
        - name: GrpAddress
          pcf_type: MQCFST
          type_hint: str
        - name: MonitorInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: MulticastHeartbeat
          pcf_type: MQCFIN
          type_hint: int
        - name: MulticastPropControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMCP_ALL
            - MQMAP_REPLY
            - MQMAP_USER
            - MQMAP_NONE
            - MQMAP_COMPAT
        - name: MsgHistory
          pcf_type: MQCFIN
          type_hint: int
        - name: NewSubHistory
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQNSH_NONE
            - MQNSH_ALL
        - name: PortNumber
          pcf_type: MQCFIN
          type_hint: int
        - name: Type
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCIT_MULTICAST
    mapping:
      request:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - ComminfoAttrs
          - ComminfoName
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
          - Bridge
          - CCSID
          - CommEvent
          - ComminfoName
          - Description
          - Encoding
          - GrpAddress
          - MonitorInterval
          - MsgHistory
          - MulticastHeartbeat
          - MulticastPropControl
          - NewSubHistory
          - PortNumber
          - Type
    notes: []
```

## Output-parameter refresh

```yaml
version: 1
generated_at: 2026-01-27T20:30:57Z
commands:
  - name: DISPLAY COMMINFO
    output_parameters:
      - ALL
      - TYPE
```
