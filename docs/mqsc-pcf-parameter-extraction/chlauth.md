# MQSC to PCF parameter extraction: Chlauth

## Table of Contents
- [Purpose](#purpose)
- [First-run extraction](#first-run-extraction)

## Purpose
Collect MQSC and PCF parameter mappings for chlauth commands, split from the first-run extraction to keep each qualifier readable.

## First-run extraction
```yaml
version: 1
generated_at: 2026-01-11T23:40:29Z
commands:
  - mqsc:
      name: DISPLAY CHLAUTH
      href: SSFKSJ_9.4.0/refadmin/q086070_.html
      positional_parameters:
        - qmgr-name
      input_parameters: []
      output_parameters:
        - ADDRESS
        - CLNTUSER
        - MATCH
        - MATCH(EXACT)
        - MATCH(GENERIC)
        - QMNAME
        - REVDNS(ENABLED)
        - SSLCERTI
        - SSLPEER
        - TYPE(ALL)
        - TYPE(USERMAP)
        - WARN
      section_sources:
        {}
    pcf:
      command: MQCMD_INQUIRE_CHLAUTH_RECS
      request_href: SSFKSJ_9.4.0/refadmin/q087440_.html
      response_href: SSFKSJ_9.4.0/refadmin/q087450_.html
      request_parameters:
        - name: Address
          pcf_type: MQCFST
          type_hint: str
        - name: ByteStringFilterCommand
          pcf_type: MQCFBF
          type_hint: null
        - name: ChannelAuthAttrs
          pcf_type: MQCFIL
          type_hint: int
          enum_values:
            - MQIACF_ALL
            - MQCA_ALTERATION_DATE
            - MQCA_ALTERATION_TIME
            - MQCA_CHLAUTH_DESC
            - MQCA_CUSTOM
            - MQCACH_CONNECTION_NAME
            - MQCACH_MCA_USER_ID
            - MQIACH_USER_SOURCE
            - MQIACH_WARNING
        - name: CheckClient
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHK_REQUIRED_ADMIN
            - MQCHK_REQUIRED
            - MQCHK_AS_Q_MGR
        - name: ClntUser
          pcf_type: MQCFST
          type_hint: str
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: IntegerFilterCommand
          pcf_type: MQCFIF
          type_hint: null
        - name: Match
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMATCH_RUNCHECK
            - MQMATCH_EXACT
            - MQMATCH_GENERIC
            - MQMATCH_ALL
        - name: QMName
          pcf_type: MQCFST
          type_hint: str
        - name: SSLCertIssuer
          pcf_type: MQCFST
          type_hint: str
        - name: SSLPeer
          pcf_type: MQCFST
          type_hint: str
        - name: StringFilterCommand
          pcf_type: MQCFSF
          type_hint: null
        - name: Type
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCAUT_BLOCKUSER
            - MQCAUT_BLOCKADDR
            - MQCAUT_SSLPEERMAP
            - MQCAUT_ADDRESSMAP
            - MQCAUT_USERMAP
            - MQCAUT_QMGRMAP
            - MQCAUT_ALL
      response_parameters:
        - name: AlterationDate
          pcf_type: MQCFST
          type_hint: str
        - name: AlterationTime
          pcf_type: MQCFST
          type_hint: str
        - name: Address
          pcf_type: MQCFST
          type_hint: str
        - name: AddrList
          pcf_type: MQCFSL
          type_hint: str
        - name: Chlauth
          pcf_type: MQCFST
          type_hint: str
        - name: CheckClient
          pcf_type: MQCFIN
          type_hint: int
        - name: ClntUser
          pcf_type: MQCFST
          type_hint: str
        - name: Description
          pcf_type: MQCFST
          type_hint: str
        - name: MCAUser
          pcf_type: MQCFST
          type_hint: str
        - name: QMName
          pcf_type: MQCFST
          type_hint: str
        - name: SSLCertIssuer
          pcf_type: MQCFST
          type_hint: str
        - name: SSLPeer
          pcf_type: MQCFST
          type_hint: str
        - name: Type
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCAUT_BLOCKUSER
            - MQCAUT_BLOCKADDR
            - MQCAUT_SSLPEERMAP
            - MQCAUT_ADDRESSMAP
            - MQCAUT_USERMAP
            - MQCAUT_QMGRMAP
        - name: UserList
          pcf_type: MQCFSL
          type_hint: str
        - name: UserSrc
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQUSRC_MAP
            - MQUSRC_NOACCESS
            - MQUSRC_CHANNEL
        - name: Warn
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQWARN_NO
            - MQWARN_YES
    mapping:
      request:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - Address
          - ByteStringFilterCommand
          - ChannelAuthAttrs
          - CheckClient
          - ClntUser
          - CommandScope
          - IntegerFilterCommand
          - Match
          - QMName
          - SSLCertIssuer
          - SSLPeer
          - StringFilterCommand
          - Type
      response:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - AddrList
          - Address
          - AlterationDate
          - AlterationTime
          - CheckClient
          - Chlauth
          - ClntUser
          - Description
          - MCAUser
          - QMName
          - SSLCertIssuer
          - SSLPeer
          - Type
          - UserList
          - UserSrc
          - Warn
    notes: []
  - mqsc:
      name: SET CHLAUTH
      href: SSFKSJ_9.4.0/refadmin/q086630_.html
      positional_parameters:
        - channel-profile-name
        - qmgr-name
      input_parameters: []
      output_parameters: []
      section_sources:
        {}
    pcf:
      command: MQCMD_SET_CHLAUTH_REC
      request_href: SSFKSJ_9.4.0/refadmin/q088390_.html
      response_href: SSFKSJ_9.4.0/refadmin/q088390_.html
      request_parameters:
        - name: ProfileName
          pcf_type: MQCFST
          type_hint: str
        - name: Type
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCAUT_BLOCKUSER
            - MQCAUT_BLOCKADDR
            - MQCAUT_SSLPEERMAP
            - MQCAUT_ADDRESSMAP
            - MQCAUT_USERMAP
            - MQCAUT_QMGRMAP
        - name: Action
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQACT_ADD
            - MQACT_REPLACE
            - MQACT_REMOVE
            - MQACT_REMOVEALL
        - name: Address
          pcf_type: MQCFST
          type_hint: str
        - name: AddrList
          pcf_type: MQCFSL
          type_hint: str
        - name: CheckClient
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHK_REQUIRED_ADMIN
            - MQCHK_REQUIRED
            - MQCHK_AS_Q_MGR
        - name: ClntUser
          pcf_type: MQCFST
          type_hint: str
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: Custom
          pcf_type: MQCFST
          type_hint: str
        - name: Description
          pcf_type: MQCFST
          type_hint: str
        - name: MCAUser
          pcf_type: MQCFST
          type_hint: str
        - name: QMName
          pcf_type: MQCFST
          type_hint: str
        - name: SSLCertIssuer
          pcf_type: MQCFST
          type_hint: str
        - name: SSLPeer
          pcf_type: MQCFST
          type_hint: str
        - name: UserList
          pcf_type: MQCFSL
          type_hint: str
        - name: UserSrc
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQUSRC_MAP
            - MQUSRC_NOACCESS
            - MQUSRC_CHANNEL
        - name: Warn
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQWARN_NO
            - MQWARN_YES
            - MQRCCF_CHLAUTH_TYPE_ERROR
            - MQRCCF_CHLAUTH_ACTION_ERROR
            - MQRCCF_CHLAUTH_USERSRC_ERROR
            - MQRCCF_WRONG_CHLAUTH_TYPE
            - MQRCCF_CHLAUTH_ALREADY_EXISTS
      response_parameters:
        - name: ProfileName
          pcf_type: MQCFST
          type_hint: str
        - name: Type
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCAUT_BLOCKUSER
            - MQCAUT_BLOCKADDR
            - MQCAUT_SSLPEERMAP
            - MQCAUT_ADDRESSMAP
            - MQCAUT_USERMAP
            - MQCAUT_QMGRMAP
        - name: Action
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQACT_ADD
            - MQACT_REPLACE
            - MQACT_REMOVE
            - MQACT_REMOVEALL
        - name: Address
          pcf_type: MQCFST
          type_hint: str
        - name: AddrList
          pcf_type: MQCFSL
          type_hint: str
        - name: CheckClient
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHK_REQUIRED_ADMIN
            - MQCHK_REQUIRED
            - MQCHK_AS_Q_MGR
        - name: ClntUser
          pcf_type: MQCFST
          type_hint: str
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: Custom
          pcf_type: MQCFST
          type_hint: str
        - name: Description
          pcf_type: MQCFST
          type_hint: str
        - name: MCAUser
          pcf_type: MQCFST
          type_hint: str
        - name: QMName
          pcf_type: MQCFST
          type_hint: str
        - name: SSLCertIssuer
          pcf_type: MQCFST
          type_hint: str
        - name: SSLPeer
          pcf_type: MQCFST
          type_hint: str
        - name: UserList
          pcf_type: MQCFSL
          type_hint: str
        - name: UserSrc
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQUSRC_MAP
            - MQUSRC_NOACCESS
            - MQUSRC_CHANNEL
        - name: Warn
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQWARN_NO
            - MQWARN_YES
            - MQRCCF_CHLAUTH_TYPE_ERROR
            - MQRCCF_CHLAUTH_ACTION_ERROR
            - MQRCCF_CHLAUTH_USERSRC_ERROR
            - MQRCCF_WRONG_CHLAUTH_TYPE
            - MQRCCF_CHLAUTH_ALREADY_EXISTS
    mapping:
      request:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - Action
          - AddrList
          - Address
          - CheckClient
          - ClntUser
          - CommandScope
          - Custom
          - Description
          - MCAUser
          - ProfileName
          - QMName
          - SSLCertIssuer
          - SSLPeer
          - Type
          - UserList
          - UserSrc
          - Warn
      response:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - Action
          - AddrList
          - Address
          - CheckClient
          - ClntUser
          - CommandScope
          - Custom
          - Description
          - MCAUser
          - ProfileName
          - QMName
          - SSLCertIssuer
          - SSLPeer
          - Type
          - UserList
          - UserSrc
          - Warn
    notes: []
```










## Output-parameter refresh
```yaml
version: 1
generated_at: 2026-01-27T20:30:57Z
commands:
  - name: DISPLAY CHLAUTH
    output_parameters:
      - ADDRESS
      - CLNTUSER
      - MATCH
      - MATCH(EXACT)
      - MATCH(GENERIC)
      - QMNAME
      - REVDNS(ENABLED)
      - SSLCERTI
      - SSLPEER
      - TYPE(ALL)
      - TYPE(USERMAP)
      - WARN
```
