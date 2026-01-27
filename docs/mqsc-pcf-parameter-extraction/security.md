# MQSC to PCF parameter extraction: Security

## Table of Contents
- [Purpose](#purpose)
- [First-run extraction](#first-run-extraction)

## Purpose
Collect MQSC and PCF parameter mappings for security commands, split from the first-run extraction to keep each qualifier readable.

## First-run extraction
```yaml
version: 1
generated_at: 2026-01-11T23:40:29Z
commands:
  - mqsc:
      name: ALTER SECURITY
      href: SSFKSJ_9.4.0/refadmin/q085380_.html
      positional_parameters:
        - integer
        - qmgr-name
      input_parameters:
        - CMDSCOPE
        - INTERVAL
        - TIMEOUT
      output_parameters: []
      section_sources:
        'Parameter descriptions for ALTER SECURITY':
          - CMDSCOPE
          - INTERVAL
          - TIMEOUT
    pcf:
      command: MQCMD_CHANGE_SECURITY
      request_href: SSFKSJ_9.4.0/refadmin/q087010_.html
      response_href: SSFKSJ_9.4.0/refadmin/q087010_.html
      request_parameters:
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: SecurityInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: SecurityTimeout
          pcf_type: MQCFIN
          type_hint: int
      response_parameters:
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: SecurityInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: SecurityTimeout
          pcf_type: MQCFIN
          type_hint: int
    mapping:
      request:
        suggested:
          {}
        ambiguous:
          {}
        unmapped:
          - CMDSCOPE
          - INTERVAL
          - TIMEOUT
        pcf_unmapped:
          - CommandScope
          - SecurityInterval
          - SecurityTimeout
      response:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - CommandScope
          - SecurityInterval
          - SecurityTimeout
    notes: []
  - mqsc:
      name: DISPLAY SECURITY
      href: SSFKSJ_9.4.0/refadmin/q086290_.html
      positional_parameters:
        - qmgr-name
      input_parameters: []
      output_parameters:
        - CMDSCOPE
        - CSQH037I
        - CSQH038I
        - CSQH040I
        - CSQH042I
        - INTERVAL
        - SWITCHES
        - TIMEOUT
      section_sources:
        {}
    pcf:
      command: MQCMD_INQUIRE_SECURITY
      request_href: SSFKSJ_9.4.0/refadmin/q087900_.html
      response_href: SSFKSJ_9.4.0/refadmin/q087910_.html
      request_parameters:
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: SecurityAttrs
          pcf_type: MQCFIL
          type_hint: int
          enum_values:
            - MQIACF_ALL
            - MQIACF_SECURITY_SWITCH
            - MQIACF_SECURITY_TIMEOUT
            - MQIACF_SECURITY_INTERVAL
      response_parameters:
        - name: SecurityInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: SecuritySwitch
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSECSW_SUBSYSTEM
            - MQSECSW_Q_MGR
            - MQSECSW_QSG
            - MQSECSW_CONNECTION
            - MQSECSW_COMMAND
            - MQSECSW_CONTEXT
            - MQSECSW_ALTERNATE_USER
            - MQSECSW_PROCESS
            - MQSECSW_NAMELIST
            - MQSECSW_TOPIC
            - MQSECSW_Q
            - MQSECSW_COMMAND_RESOURCES
        - name: SecuritySwitchProfile
          pcf_type: MQCFST
          type_hint: str
        - name: SecuritySwitchSetting
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSECSW_ON_FOUND
            - MQSECSW_OFF_FOUND
            - MQSECSW_ON_NOT_FOUND
            - MQSECSW_OFF_NOT_FOUND
            - MQSECSW_OFF_ERROR
            - MQSECSW_ON_OVERRIDDEN
        - name: SecurityTimeout
          pcf_type: MQCFIN
          type_hint: int
    mapping:
      request:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - CommandScope
          - SecurityAttrs
      response:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - SecurityInterval
          - SecuritySwitch
          - SecuritySwitchProfile
          - SecuritySwitchSetting
          - SecurityTimeout
    notes: []
  - mqsc:
      name: REFRESH SECURITY
      href: SSFKSJ_9.4.0/refadmin/q086490_.html
      positional_parameters:
        - qmgr-name
      input_parameters: []
      output_parameters: []
      section_sources:
        {}
    pcf:
      command: MQCMD_REFRESH_SECURITY
      request_href: SSFKSJ_9.4.0/refadmin/q088250_.html
      response_href: SSFKSJ_9.4.0/refadmin/q088250_.html
      request_parameters:
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: SecurityItem
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSECITEM_ALL
            - MQSECITEM_MQADMIN
            - MQSECITEM_MQNLIST
            - MQSECITEM_MQPROC
            - MQSECITEM_MQQUEUE
            - MQSECITEM_MXADMIN
            - MQSECITEM_MXNLIST
            - MQSECITEM_MXPROC
            - MQSECITEM_MXQUEUE
            - MQSECITEM_MXTOPIC
        - name: SecurityType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSECTYPE_AUTHSERV
            - MQSECTYPE_CLASSES
            - MQSECTYPE_CONNAUTH
            - MQSECTYPE_SSL
      response_parameters:
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: SecurityItem
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSECITEM_ALL
            - MQSECITEM_MQADMIN
            - MQSECITEM_MQNLIST
            - MQSECITEM_MQPROC
            - MQSECITEM_MQQUEUE
            - MQSECITEM_MXADMIN
            - MQSECITEM_MXNLIST
            - MQSECITEM_MXPROC
            - MQSECITEM_MXQUEUE
            - MQSECITEM_MXTOPIC
        - name: SecurityType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSECTYPE_AUTHSERV
            - MQSECTYPE_CLASSES
            - MQSECTYPE_CONNAUTH
            - MQSECTYPE_SSL
    mapping:
      request:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - CommandScope
          - SecurityItem
          - SecurityType
      response:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - CommandScope
          - SecurityItem
          - SecurityType
    notes: []
  - mqsc:
      name: RVERIFY SECURITY
      href: SSFKSJ_9.4.0/refadmin/q086600_.html
      positional_parameters:
        - (userids...)
        - qmgr-name
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
```












## Output-parameter refresh
```yaml
version: 1
generated_at: 2026-01-27T20:30:57Z
commands:
  - name: DISPLAY SECURITY
    output_parameters:
      - CMDSCOPE
      - CSQH037I
      - CSQH038I
      - CSQH040I
      - CSQH042I
      - INTERVAL
      - SWITCHES
      - TIMEOUT
```
