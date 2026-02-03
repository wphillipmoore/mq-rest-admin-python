# MQSC to PCF parameter extraction: Authrec

## Table of Contents

- [Purpose](#purpose)
- [First-run extraction](#first-run-extraction)
- [Authrec command re-parse](#authrec-command-re-parse)

## Purpose

Collect MQSC and PCF parameter mappings for authrec commands, split from the first-run extraction to keep each qualifier readable.

## First-run extraction

```yaml
version: 1
generated_at: 2026-01-11T23:40:29Z
commands:
  - mqsc:
      name: DELETE AUTHREC
      href: SSFKSJ_9.4.0/refadmin/q085790_.html
      positional_parameters:
        - group-name
        - principal-name
        - profile-name
      input_parameters:
        - GROUP
        - IGNSTATE
        - OBJTYPE
        - PRINCIPAL
        - PROFILE
      output_parameters: []
      section_sources:
        'Parameter descriptions for DELETE AUTHREC':
          - GROUP
          - IGNSTATE
          - OBJTYPE
          - PRINCIPAL
          - PROFILE
    pcf:
      command: MQCMD_DELETE_AUTH_REC
      request_href: SSFKSJ_9.4.0/refadmin/q087100_.html
      response_href: SSFKSJ_9.4.0/refadmin/q087100_.html
      request_parameters:
        - name: ObjectType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQOT_AUTH_INFO
            - MQOT_CHANNEL
            - MQOT_CLNTCONN_CHANNEL
            - MQOT_COMM_INFO
            - MQOT_LISTENER
            - MQOT_NAMELIST
            - MQOT_PROCESS
            - MQOT_Q
            - MQOT_Q_MGR
            - MQOT_REMOTE_Q_MGR_NAME
            - MQOT_SERVICE
            - MQOT_TOPIC
        - name: ProfileName
          pcf_type: MQCFST
          type_hint: str
        - name: GroupNames
          pcf_type: MQCFSL
          type_hint: str
        - name: PrincipalNames
          pcf_type: MQCFSL
          type_hint: str
        - name: IgnoreState
          pcf_type: MQCFST
          type_hint: str
          enum_values:
            - MQIS_YES
            - MQIS_NO
            - MQRC_OBJECT_TYPE_ERROR
            - MQRC_UNKNOWN_ENTITY
            - MQRCCF_ENTITY_NAME_MISSING
            - MQRCCF_OBJECT_TYPE_MISSING
            - MQRCCF_PROFILE_NAME_ERROR
      response_parameters:
        - name: ObjectType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQOT_AUTH_INFO
            - MQOT_CHANNEL
            - MQOT_CLNTCONN_CHANNEL
            - MQOT_COMM_INFO
            - MQOT_LISTENER
            - MQOT_NAMELIST
            - MQOT_PROCESS
            - MQOT_Q
            - MQOT_Q_MGR
            - MQOT_REMOTE_Q_MGR_NAME
            - MQOT_SERVICE
            - MQOT_TOPIC
        - name: ProfileName
          pcf_type: MQCFST
          type_hint: str
        - name: GroupNames
          pcf_type: MQCFSL
          type_hint: str
        - name: PrincipalNames
          pcf_type: MQCFSL
          type_hint: str
        - name: IgnoreState
          pcf_type: MQCFST
          type_hint: str
          enum_values:
            - MQIS_YES
            - MQIS_NO
            - MQRC_OBJECT_TYPE_ERROR
            - MQRC_UNKNOWN_ENTITY
            - MQRCCF_ENTITY_NAME_MISSING
            - MQRCCF_OBJECT_TYPE_MISSING
            - MQRCCF_PROFILE_NAME_ERROR
    mapping:
      request:
        suggested:
          {}
        ambiguous:
          IGNSTATE:
            - IgnoreState
          OBJTYPE:
            - ObjectType
        unmapped:
          - GROUP
          - PRINCIPAL
          - PROFILE
        pcf_unmapped:
          - GroupNames
          - IgnoreState
          - ObjectType
          - PrincipalNames
          - ProfileName
      response:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - GroupNames
          - IgnoreState
          - ObjectType
          - PrincipalNames
          - ProfileName
    notes: []
  - mqsc:
      name: DISPLAY AUTHREC
      href: SSFKSJ_9.4.0/refadmin/q086000_.html
      positional_parameters:
        - group-name
        - principal-name
        - profile-name
        - service-component
      input_parameters: []
      output_parameters:
        - AUTHLIST
        - ENTITY
        - ENTTYPE
      section_sources:
        {}
    pcf:
      command: MQCMD_INQUIRE_AUTH_REC
      request_href: SSFKSJ_9.4.0/refadmin/q087310_.html
      response_href: SSFKSJ_9.4.0/refadmin/q087320_.html
      request_parameters:
        - name: Options
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQAUTHOPT_NAME_ALL_MATCHING
            - MQAUTHOPT_NAME_EXPLICIT
            - MQAUTHOPT_ENTITY_EXPLICIT
            - MQAUTHOPT_ENTITY_SET
            - MQAUTHOPT_NAME_AS_WILDCARD
        - name: ProfileName
          pcf_type: MQCFST
          type_hint: str
        - name: ObjectType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQOT_ALL
            - MQOT_AUTH_INFO
            - MQOT_CHANNEL
            - MQOT_CLNTCONN_CHANNEL
            - MQOT_COMM_INFO
            - MQOT_LISTENER
            - MQOT_NAMELIST
            - MQOT_PROCESS
            - MQOT_Q
            - MQOT_Q_MGR
            - MQOT_REMOTE_Q_MGR_NAME
            - MQOT_SERVICE
            - MQOT_TOPIC
        - name: EntityName
          pcf_type: MQCFST
          type_hint: str
        - name: EntityType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQZAET_GROUP
            - MQZAET_PRINCIPAL
        - name: ProfileAttrs
          pcf_type: MQCFIL
          type_hint: int
          enum_values:
            - MQIACF_ALL
            - MQCACF_ENTITY_NAME
            - MQIACF_AUTHORIZATION_LIST
            - MQIACF_ENTITY_TYPE
        - name: ServiceComponent
          pcf_type: MQCFST
          type_hint: str
          enum_values:
            - MQRC_OBJECT_TYPE_ERROR
            - MQRC_UNKNOWN_ENTITY
            - MQRCCF_CFST_CONFLICTING_PARM
            - MQRCCF_PROFILE_NAME_ERROR
            - MQRCCF_ENTITY_NAME_MISSING
            - MQRCCF_OBJECT_TYPE_MISSING
            - MQRCCF_PROFILE_NAME_MISSING
      response_parameters:
        - name: AuthorizationList
          pcf_type: MQCFIL
          type_hint: int
          enum_values:
            - MQAUTH_NONE
            - MQAUTH_ALT_USER_AUTHORITY
            - MQAUTH_BROWSE
            - MQAUTH_CHANGE
            - MQAUTH_CLEAR
            - MQAUTH_CONNECT
            - MQAUTH_CREATE
            - MQAUTH_DELETE
            - MQAUTH_DISPLAY
            - MQAUTH_INPUT
            - MQAUTH_INQUIRE
            - MQAUTH_OUTPUT
            - MQAUTH_PASS_ALL_CONTEXT
            - MQAUTH_PASS_IDENTITY_CONTEXT
            - MQAUTH_SET
            - MQAUTH_SET_ALL_CONTEXT
            - MQAUTH_SET_IDENTITY_CONTEXT
            - MQAUTH_CONTROL
            - MQAUTH_CONTROL_EXTENDED
            - MQAUTH_PUBLISH
            - MQAUTH_SUBSCRIBE
            - MQAUTH_RESUME
            - MQAUTH_SYSTEM
            - MQAUTH_ALL
            - MQAUTH_ALL_ADMIN
            - MQAUTH_ALL_MQI
        - name: EntityName
          pcf_type: MQCFST
          type_hint: str
        - name: EntityType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQZAET_GROUP
            - MQZAET_PRINCIPAL
            - MQZAET_UNKNOWN
        - name: ObjectType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQOT_AUTH_INFO
            - MQOT_CHANNEL
            - MQOT_CLNTCONN_CHANNEL
            - MQOT_COMM_INFO
            - MQOT_LISTENER
            - MQOT_NAMELIST
            - MQOT_PROCESS
            - MQOT_Q
            - MQOT_Q_MGR
            - MQOT_REMOTE_Q_MGR_NAME
            - MQOT_SERVICE
            - MQOT_TOPIC
        - name: Options
          pcf_type: MQCFIN
          type_hint: int
        - name: ProfileName
          pcf_type: MQCFST
          type_hint: str
        - name: QMgrName
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
          - EntityName
          - EntityType
          - ObjectType
          - Options
          - ProfileAttrs
          - ProfileName
          - ServiceComponent
      response:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - AuthorizationList
          - EntityName
          - EntityType
          - ObjectType
          - Options
          - ProfileName
          - QMgrName
    notes: []
  - mqsc:
      name: SET AUTHREC
      href: SSFKSJ_9.4.0/refadmin/q086620_.html
      positional_parameters:
        - group-name
        - principal-name
        - profile-name
        - service-component
      input_parameters: []
      output_parameters: []
      section_sources:
        {}
    pcf:
      command: MQCMD_SET_AUTH_REC
      request_href: SSFKSJ_9.4.0/refadmin/q088380_.html
      response_href: SSFKSJ_9.4.0/refadmin/q088380_.html
      request_parameters:
        - name: ProfileName
          pcf_type: MQCFST
          type_hint: str
        - name: ObjectType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQOT_AUTH_INFO
            - MQOT_CHANNEL
            - MQOT_CLNTCONN_CHANNEL
            - MQOT_COMM_INFO
            - MQOT_LISTENER
            - MQOT_NAMELIST
            - MQOT_PROCESS
            - MQOT_Q
            - MQOT_Q_MGR
            - MQOT_REMOTE_Q_MGR_NAME
            - MQOT_SERVICE
            - MQOT_TOPIC
        - name: AuthorityAdd
          pcf_type: MQCFIL
          type_hint: int
          enum_values:
            - MQAUTH_NONE
            - MQAUTH_ALT_USER_AUTHORITY
            - MQAUTH_BROWSE
            - MQAUTH_CHANGE
            - MQAUTH_CLEAR
            - MQAUTH_CONNECT
            - MQAUTH_CREATE
            - MQAUTH_DELETE
            - MQAUTH_DISPLAY
            - MQAUTH_INPUT
            - MQAUTH_INQUIRE
            - MQAUTH_OUTPUT
            - MQAUTH_PASS_ALL_CONTEXT
            - MQAUTH_PASS_IDENTITY_CONTEXT
            - MQAUTH_SET
            - MQAUTH_SET_ALL_CONTEXT
            - MQAUTH_SET_IDENTITY_CONTEXT
            - MQAUTH_CONTROL
            - MQAUTH_CONTROL_EXTENDED
            - MQAUTH_PUBLISH
            - MQAUTH_SUBSCRIBE
            - MQAUTH_RESUME
            - MQAUTH_SYSTEM
            - MQAUTH_ALL
            - MQAUTH_ALL_ADMIN
            - MQAUTH_ALL_MQI
        - name: AuthorityRemove
          pcf_type: MQCFIL
          type_hint: int
          enum_values:
            - MQAUTH_NONE
            - MQAUTH_ALT_USER_AUTHORITY
            - MQAUTH_BROWSE
            - MQAUTH_CHANGE
            - MQAUTH_CLEAR
            - MQAUTH_CONNECT
            - MQAUTH_CREATE
            - MQAUTH_DELETE
            - MQAUTH_DISPLAY
            - MQAUTH_INPUT
            - MQAUTH_INQUIRE
            - MQAUTH_OUTPUT
            - MQAUTH_PASS_ALL_CONTEXT
            - MQAUTH_PASS_IDENTITY_CONTEXT
            - MQAUTH_SET
            - MQAUTH_SET_ALL_CONTEXT
            - MQAUTH_SET_IDENTITY_CONTEXT
            - MQAUTH_CONTROL
            - MQAUTH_CONTROL_EXTENDED
            - MQAUTH_PUBLISH
            - MQAUTH_SUBSCRIBE
            - MQAUTH_RESUME
            - MQAUTH_SYSTEM
            - MQAUTH_ALL
            - MQAUTH_ALL_ADMIN
            - MQAUTH_ALL_MQI
        - name: GroupNames
          pcf_type: MQCFSL
          type_hint: str
        - name: PrincipalNames
          pcf_type: MQCFSL
          type_hint: str
        - name: ServiceComponent
          pcf_type: MQCFST
          type_hint: str
          enum_values:
            - MQRC_UNKNOWN_ENTITY
            - MQRCCF_AUTH_VALUE_ERROR
            - MQRCCF_AUTH_VALUE_MISSING
            - MQRCCF_ENTITY_NAME_MISSING
            - MQRCCF_OBJECT_TYPE_MISSING
            - MQRCCF_PROFILE_NAME_ERROR
      response_parameters:
        - name: ProfileName
          pcf_type: MQCFST
          type_hint: str
        - name: ObjectType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQOT_AUTH_INFO
            - MQOT_CHANNEL
            - MQOT_CLNTCONN_CHANNEL
            - MQOT_COMM_INFO
            - MQOT_LISTENER
            - MQOT_NAMELIST
            - MQOT_PROCESS
            - MQOT_Q
            - MQOT_Q_MGR
            - MQOT_REMOTE_Q_MGR_NAME
            - MQOT_SERVICE
            - MQOT_TOPIC
        - name: AuthorityAdd
          pcf_type: MQCFIL
          type_hint: int
          enum_values:
            - MQAUTH_NONE
            - MQAUTH_ALT_USER_AUTHORITY
            - MQAUTH_BROWSE
            - MQAUTH_CHANGE
            - MQAUTH_CLEAR
            - MQAUTH_CONNECT
            - MQAUTH_CREATE
            - MQAUTH_DELETE
            - MQAUTH_DISPLAY
            - MQAUTH_INPUT
            - MQAUTH_INQUIRE
            - MQAUTH_OUTPUT
            - MQAUTH_PASS_ALL_CONTEXT
            - MQAUTH_PASS_IDENTITY_CONTEXT
            - MQAUTH_SET
            - MQAUTH_SET_ALL_CONTEXT
            - MQAUTH_SET_IDENTITY_CONTEXT
            - MQAUTH_CONTROL
            - MQAUTH_CONTROL_EXTENDED
            - MQAUTH_PUBLISH
            - MQAUTH_SUBSCRIBE
            - MQAUTH_RESUME
            - MQAUTH_SYSTEM
            - MQAUTH_ALL
            - MQAUTH_ALL_ADMIN
            - MQAUTH_ALL_MQI
        - name: AuthorityRemove
          pcf_type: MQCFIL
          type_hint: int
          enum_values:
            - MQAUTH_NONE
            - MQAUTH_ALT_USER_AUTHORITY
            - MQAUTH_BROWSE
            - MQAUTH_CHANGE
            - MQAUTH_CLEAR
            - MQAUTH_CONNECT
            - MQAUTH_CREATE
            - MQAUTH_DELETE
            - MQAUTH_DISPLAY
            - MQAUTH_INPUT
            - MQAUTH_INQUIRE
            - MQAUTH_OUTPUT
            - MQAUTH_PASS_ALL_CONTEXT
            - MQAUTH_PASS_IDENTITY_CONTEXT
            - MQAUTH_SET
            - MQAUTH_SET_ALL_CONTEXT
            - MQAUTH_SET_IDENTITY_CONTEXT
            - MQAUTH_CONTROL
            - MQAUTH_CONTROL_EXTENDED
            - MQAUTH_PUBLISH
            - MQAUTH_SUBSCRIBE
            - MQAUTH_RESUME
            - MQAUTH_SYSTEM
            - MQAUTH_ALL
            - MQAUTH_ALL_ADMIN
            - MQAUTH_ALL_MQI
        - name: GroupNames
          pcf_type: MQCFSL
          type_hint: str
        - name: PrincipalNames
          pcf_type: MQCFSL
          type_hint: str
        - name: ServiceComponent
          pcf_type: MQCFST
          type_hint: str
          enum_values:
            - MQRC_UNKNOWN_ENTITY
            - MQRCCF_AUTH_VALUE_ERROR
            - MQRCCF_AUTH_VALUE_MISSING
            - MQRCCF_ENTITY_NAME_MISSING
            - MQRCCF_OBJECT_TYPE_MISSING
            - MQRCCF_PROFILE_NAME_ERROR
    mapping:
      request:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - AuthorityAdd
          - AuthorityRemove
          - GroupNames
          - ObjectType
          - PrincipalNames
          - ProfileName
          - ServiceComponent
      response:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - AuthorityAdd
          - AuthorityRemove
          - GroupNames
          - ObjectType
          - PrincipalNames
          - ProfileName
          - ServiceComponent
    notes: []
```

## Authrec command re-parse

This addendum isolates corrected MQSC and PCF parameter sets. It is intentionally separate from the first-run extraction above and omits mapping heuristics.

```yaml
version: 1
generated_at: 2026-01-12T20:52:18Z
commands:
  - mqsc:
      name: DELETE AUTHREC
      href: SSFKSJ_9.4.0/refadmin/q085790_.html
      positional_parameters: []
      input_parameters:
        - PROFILE
        - OBJTYPE
        - PRINCIPAL
        - GROUP
        - IGNSTATE
      output_parameters: []
      section_sources:
        'Parameter descriptions for DELETE AUTHREC':
          - PROFILE
          - OBJTYPE
          - PRINCIPAL
          - GROUP
          - IGNSTATE
    pcf:
      command: MQCMD_DELETE_AUTH_REC
      request_href: SSFKSJ_9.4.0/refadmin/q087100_.html
      response_href: SSFKSJ_9.4.0/refadmin/q087100_.html
      request_parameters:
        - name: ObjectType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQOT_AUTH_INFO
            - MQOT_CHANNEL
            - MQOT_CLNTCONN_CHANNEL
            - MQOT_COMM_INFO
            - MQOT_LISTENER
            - MQOT_NAMELIST
            - MQOT_PROCESS
            - MQOT_Q
            - MQOT_Q_MGR
            - MQOT_REMOTE_Q_MGR_NAME
            - MQOT_SERVICE
            - MQOT_TOPIC
        - name: ProfileName
          pcf_type: MQCFST
          type_hint: str
        - name: GroupNames
          pcf_type: MQCFSL
          type_hint: str
        - name: PrincipalNames
          pcf_type: MQCFSL
          type_hint: str
        - name: IgnoreState
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQIS_NO
            - MQIS_YES
      response_parameters:
        - name: ObjectType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQOT_AUTH_INFO
            - MQOT_CHANNEL
            - MQOT_CLNTCONN_CHANNEL
            - MQOT_COMM_INFO
            - MQOT_LISTENER
            - MQOT_NAMELIST
            - MQOT_PROCESS
            - MQOT_Q
            - MQOT_Q_MGR
            - MQOT_REMOTE_Q_MGR_NAME
            - MQOT_SERVICE
            - MQOT_TOPIC
        - name: ProfileName
          pcf_type: MQCFST
          type_hint: str
        - name: GroupNames
          pcf_type: MQCFSL
          type_hint: list[str]
        - name: PrincipalNames
          pcf_type: MQCFSL
          type_hint: list[str]
        - name: IgnoreState
          pcf_type: MQCFST
          type_hint: str
          enum_values:
            - MQIS_YES
            - MQIS_NO
            - MQRC_OBJECT_TYPE_ERROR
            - MQRC_UNKNOWN_ENTITY
            - MQRCCF_ENTITY_NAME_MISSING
            - MQRCCF_OBJECT_TYPE_MISSING
            - MQRCCF_PROFILE_NAME_ERROR
    notes:
      - ignore-state-type-inferred-from-mqsc-ignstate
      - ignore-state-name-normalized
  - mqsc:
      name: DISPLAY AUTHREC
      href: SSFKSJ_9.4.0/refadmin/q086000_.html
      positional_parameters: []
      input_parameters:
        - PROFILE
        - OBJTYPE
        - PRINCIPAL
        - GROUP
        - MATCH
        - SERVCOMP
        - ALL
      output_parameters:
        - AUTHLIST
        - ENTITY
        - ENTTYPE
      section_sources:
        'Parameter descriptions for DISPLAY AUTHREC':
          - PROFILE
          - OBJTYPE
          - PRINCIPAL
          - GROUP
          - MATCH
          - SERVCOMP
          - ALL
        'Requested parameters':
          - AUTHLIST
          - ENTITY
          - ENTTYPE
    pcf:
      command: MQCMD_INQUIRE_AUTH_RECS
      request_href: SSFKSJ_9.4.0/refadmin/q087310_.html
      response_href: SSFKSJ_9.4.0/refadmin/q087320_.html
      request_parameters:
        - name: Options
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQAUTHOPT_NAME_ALL_MATCHING
            - MQAUTHOPT_NAME_EXPLICIT
            - MQAUTHOPT_ENTITY_EXPLICIT
            - MQAUTHOPT_ENTITY_SET
            - MQAUTHOPT_NAME_AS_WILDCARD
        - name: ProfileName
          pcf_type: MQCFST
          type_hint: str
        - name: ObjectType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQOT_ALL
            - MQOT_AUTH_INFO
            - MQOT_CHANNEL
            - MQOT_CLNTCONN_CHANNEL
            - MQOT_COMM_INFO
            - MQOT_LISTENER
            - MQOT_NAMELIST
            - MQOT_PROCESS
            - MQOT_Q
            - MQOT_Q_MGR
            - MQOT_REMOTE_Q_MGR_NAME
            - MQOT_SERVICE
            - MQOT_TOPIC
        - name: EntityName
          pcf_type: MQCFST
          type_hint: str
        - name: EntityType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQZAET_GROUP
            - MQZAET_PRINCIPAL
        - name: ProfileAttrs
          pcf_type: MQCFIL
          type_hint: int
          enum_values:
            - MQIACF_ALL
            - MQCACF_ENTITY_NAME
            - MQIACF_AUTHORIZATION_LIST
            - MQIACF_ENTITY_TYPE
        - name: ServiceComponent
          pcf_type: MQCFST
          type_hint: str
      response_parameters:
        - name: AuthorizationList
          pcf_type: MQCFIL
          type_hint: int
          enum_values:
            - MQAUTH_NONE
            - MQAUTH_ALT_USER_AUTHORITY
            - MQAUTH_BROWSE
            - MQAUTH_CHANGE
            - MQAUTH_CLEAR
            - MQAUTH_CONNECT
            - MQAUTH_CREATE
            - MQAUTH_DELETE
            - MQAUTH_DISPLAY
            - MQAUTH_INPUT
            - MQAUTH_INQUIRE
            - MQAUTH_OUTPUT
            - MQAUTH_PASS_ALL_CONTEXT
            - MQAUTH_PASS_IDENTITY_CONTEXT
            - MQAUTH_SET
            - MQAUTH_SET_ALL_CONTEXT
            - MQAUTH_SET_IDENTITY_CONTEXT
            - MQAUTH_CONTROL
            - MQAUTH_CONTROL_EXTENDED
            - MQAUTH_PUBLISH
            - MQAUTH_SUBSCRIBE
            - MQAUTH_RESUME
            - MQAUTH_SYSTEM
            - MQAUTH_ALL
            - MQAUTH_ALL_ADMIN
            - MQAUTH_ALL_MQI
        - name: EntityName
          pcf_type: MQCFST
          type_hint: str
        - name: EntityType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQZAET_GROUP
            - MQZAET_PRINCIPAL
            - MQZAET_UNKNOWN
        - name: ObjectType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQOT_AUTH_INFO
            - MQOT_CHANNEL
            - MQOT_CLNTCONN_CHANNEL
            - MQOT_COMM_INFO
            - MQOT_LISTENER
            - MQOT_NAMELIST
            - MQOT_PROCESS
            - MQOT_Q
            - MQOT_Q_MGR
            - MQOT_REMOTE_Q_MGR_NAME
            - MQOT_SERVICE
            - MQOT_TOPIC
        - name: Options
          pcf_type: MQCFIN
          type_hint: int
        - name: ProfileName
          pcf_type: MQCFST
          type_hint: str
        - name: QMgrName
          pcf_type: MQCFST
          type_hint: str
    notes: []
  - mqsc:
      name: SET AUTHREC
      href: SSFKSJ_9.4.0/refadmin/q086620_.html
      positional_parameters: []
      input_parameters:
        - PROFILE
        - OBJTYPE
        - PRINCIPAL
        - GROUP
        - AUTHADD
        - AUTHRMV
        - SERVCOMP
      output_parameters: []
      section_sources:
        'Parameter descriptions for SET AUTHREC':
          - PROFILE
          - OBJTYPE
          - PRINCIPAL
          - GROUP
          - AUTHADD
          - AUTHRMV
          - SERVCOMP
    pcf:
      command: MQCMD_SET_AUTH_REC
      request_href: SSFKSJ_9.4.0/refadmin/q088380_.html
      response_href: SSFKSJ_9.4.0/refadmin/q088380_.html
      request_parameters:
        - name: ProfileName
          pcf_type: MQCFST
          type_hint: str
        - name: ObjectType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQOT_AUTH_INFO
            - MQOT_CHANNEL
            - MQOT_CLNTCONN_CHANNEL
            - MQOT_COMM_INFO
            - MQOT_LISTENER
            - MQOT_NAMELIST
            - MQOT_PROCESS
            - MQOT_Q
            - MQOT_Q_MGR
            - MQOT_REMOTE_Q_MGR_NAME
            - MQOT_SERVICE
            - MQOT_TOPIC
        - name: AuthorityAdd
          pcf_type: MQCFIL
          type_hint: int
          enum_values:
            - MQAUTH_NONE
            - MQAUTH_ALT_USER_AUTHORITY
            - MQAUTH_BROWSE
            - MQAUTH_CHANGE
            - MQAUTH_CLEAR
            - MQAUTH_CONNECT
            - MQAUTH_CREATE
            - MQAUTH_DELETE
            - MQAUTH_DISPLAY
            - MQAUTH_INPUT
            - MQAUTH_INQUIRE
            - MQAUTH_OUTPUT
            - MQAUTH_PASS_ALL_CONTEXT
            - MQAUTH_PASS_IDENTITY_CONTEXT
            - MQAUTH_SET
            - MQAUTH_SET_ALL_CONTEXT
            - MQAUTH_SET_IDENTITY_CONTEXT
            - MQAUTH_CONTROL
            - MQAUTH_CONTROL_EXTENDED
            - MQAUTH_PUBLISH
            - MQAUTH_SUBSCRIBE
            - MQAUTH_RESUME
            - MQAUTH_SYSTEM
            - MQAUTH_ALL
            - MQAUTH_ALL_ADMIN
            - MQAUTH_ALL_MQI
        - name: AuthorityRemove
          pcf_type: MQCFIL
          type_hint: int
          enum_values:
            - MQAUTH_NONE
            - MQAUTH_ALT_USER_AUTHORITY
            - MQAUTH_BROWSE
            - MQAUTH_CHANGE
            - MQAUTH_CLEAR
            - MQAUTH_CONNECT
            - MQAUTH_CREATE
            - MQAUTH_DELETE
            - MQAUTH_DISPLAY
            - MQAUTH_INPUT
            - MQAUTH_INQUIRE
            - MQAUTH_OUTPUT
            - MQAUTH_PASS_ALL_CONTEXT
            - MQAUTH_PASS_IDENTITY_CONTEXT
            - MQAUTH_SET
            - MQAUTH_SET_ALL_CONTEXT
            - MQAUTH_SET_IDENTITY_CONTEXT
            - MQAUTH_CONTROL
            - MQAUTH_CONTROL_EXTENDED
            - MQAUTH_PUBLISH
            - MQAUTH_SUBSCRIBE
            - MQAUTH_RESUME
            - MQAUTH_SYSTEM
            - MQAUTH_ALL
            - MQAUTH_ALL_ADMIN
            - MQAUTH_ALL_MQI
        - name: GroupNames
          pcf_type: MQCFSL
          type_hint: str
        - name: PrincipalNames
          pcf_type: MQCFSL
          type_hint: str
        - name: ServiceComponent
          pcf_type: MQCFST
          type_hint: str
      response_parameters:
        - name: ProfileName
          pcf_type: MQCFST
          type_hint: str
        - name: ObjectType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQOT_AUTH_INFO
            - MQOT_CHANNEL
            - MQOT_CLNTCONN_CHANNEL
            - MQOT_COMM_INFO
            - MQOT_LISTENER
            - MQOT_NAMELIST
            - MQOT_PROCESS
            - MQOT_Q
            - MQOT_Q_MGR
            - MQOT_REMOTE_Q_MGR_NAME
            - MQOT_SERVICE
            - MQOT_TOPIC
        - name: AuthorityAdd
          pcf_type: MQCFIL
          type_hint: list[int]
          enum_values:
            - MQAUTH_NONE
            - MQAUTH_ALT_USER_AUTHORITY
            - MQAUTH_BROWSE
            - MQAUTH_CHANGE
            - MQAUTH_CLEAR
            - MQAUTH_CONNECT
            - MQAUTH_CREATE
            - MQAUTH_DELETE
            - MQAUTH_DISPLAY
            - MQAUTH_INPUT
            - MQAUTH_INQUIRE
            - MQAUTH_OUTPUT
            - MQAUTH_PASS_ALL_CONTEXT
            - MQAUTH_PASS_IDENTITY_CONTEXT
            - MQAUTH_SET
            - MQAUTH_SET_ALL_CONTEXT
            - MQAUTH_SET_IDENTITY_CONTEXT
            - MQAUTH_CONTROL
            - MQAUTH_CONTROL_EXTENDED
            - MQAUTH_PUBLISH
            - MQAUTH_SUBSCRIBE
            - MQAUTH_RESUME
            - MQAUTH_SYSTEM
            - MQAUTH_ALL
            - MQAUTH_ALL_ADMIN
            - MQAUTH_ALL_MQI
        - name: AuthorityRemove
          pcf_type: MQCFIL
          type_hint: list[int]
          enum_values:
            - MQAUTH_NONE
            - MQAUTH_ALT_USER_AUTHORITY
            - MQAUTH_BROWSE
            - MQAUTH_CHANGE
            - MQAUTH_CLEAR
            - MQAUTH_CONNECT
            - MQAUTH_CREATE
            - MQAUTH_DELETE
            - MQAUTH_DISPLAY
            - MQAUTH_INPUT
            - MQAUTH_INQUIRE
            - MQAUTH_OUTPUT
            - MQAUTH_PASS_ALL_CONTEXT
            - MQAUTH_PASS_IDENTITY_CONTEXT
            - MQAUTH_SET
            - MQAUTH_SET_ALL_CONTEXT
            - MQAUTH_SET_IDENTITY_CONTEXT
            - MQAUTH_CONTROL
            - MQAUTH_CONTROL_EXTENDED
            - MQAUTH_PUBLISH
            - MQAUTH_SUBSCRIBE
            - MQAUTH_RESUME
            - MQAUTH_SYSTEM
            - MQAUTH_ALL
            - MQAUTH_ALL_ADMIN
            - MQAUTH_ALL_MQI
        - name: GroupNames
          pcf_type: MQCFSL
          type_hint: list[str]
        - name: PrincipalNames
          pcf_type: MQCFSL
          type_hint: list[str]
        - name: ServiceComponent
          pcf_type: MQCFST
          type_hint: str
          enum_values:
            - MQRC_UNKNOWN_ENTITY
            - MQRCCF_AUTH_VALUE_ERROR
            - MQRCCF_AUTH_VALUE_MISSING
            - MQRCCF_ENTITY_NAME_MISSING
            - MQRCCF_OBJECT_TYPE_MISSING
            - MQRCCF_PROFILE_NAME_ERROR
    notes: []
```

## Output-parameter refresh

```yaml
version: 1
generated_at: 2026-02-02T19:46:59Z
commands:
  - name: DISPLAY AUTHREC
    output_parameters:
      - AUTHLIST
      - ENTITY
      - ENTTYPE
```
