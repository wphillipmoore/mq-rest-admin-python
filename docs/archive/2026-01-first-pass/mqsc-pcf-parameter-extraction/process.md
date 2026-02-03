# MQSC to PCF parameter extraction: Process

## Table of Contents

- [Purpose](#purpose)
- [First-run extraction](#first-run-extraction)
- [Process command re-parse](#process-command-re-parse)

## Purpose

Collect MQSC and PCF parameter mappings for process commands, split from the first-run extraction to keep each qualifier readable.

## First-run extraction

```yaml
version: 1
generated_at: 2026-01-11T23:40:29Z
commands:
  - mqsc:
      name: ALTER PROCESS
      href: SSFKSJ_9.4.0/refadmin/q085300_.html
      positional_parameters:
        - process-name
        - qmgr-name
        - string
      input_parameters:
        - APPLICID
        - APPLTYPE
        - CMDSCOPE
        - DESCR
        - ENVRDATA
        - QSGDISP
        - USERDATA
      output_parameters: []
      section_sources:
        'Parameter descriptions for ALTER PROCESS':
          - APPLICID
          - APPLTYPE
          - CMDSCOPE
          - DESCR
          - ENVRDATA
          - QSGDISP
          - USERDATA
    pcf:
      command: MQCMD_CHANGE_PROCESS
      request_href: SSFKSJ_9.4.0/refdev/q091020_.html
      response_href: null
      request_parameters: []
      response_parameters: []
    mapping:
      request:
        suggested:
          {}
        ambiguous:
          {}
        unmapped:
          - APPLICID
          - APPLTYPE
          - CMDSCOPE
          - DESCR
          - ENVRDATA
          - QSGDISP
          - USERDATA
        pcf_unmapped: []
      response:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped: []
    notes: []
  - mqsc:
      name: DEFINE PROCESS
      href: SSFKSJ_9.4.0/refadmin/q085670_.html
      positional_parameters:
        - integer
        - process-name
        - qmgr-name
        - string
      input_parameters:
        - APPLICID
        - APPLTYPE
        - CMDSCOPE
        - DESCR
        - ENVRDATA
        - LIKE
        - NOREPLACE
        - QSGDISP
        - REPLACE
        - USERDATA
      output_parameters: []
      section_sources:
        'Parameter descriptions for DEFINE PROCESS':
          - APPLICID
          - APPLTYPE
          - CMDSCOPE
          - DESCR
          - ENVRDATA
          - LIKE
          - NOREPLACE
          - QSGDISP
          - REPLACE
          - USERDATA
    pcf:
      command: MQCMD_CREATE_PROCESS
      request_href: SSFKSJ_9.4.0/refdev/q091020_.html
      response_href: null
      request_parameters: []
      response_parameters: []
    mapping:
      request:
        suggested:
          {}
        ambiguous:
          {}
        unmapped:
          - APPLICID
          - APPLTYPE
          - CMDSCOPE
          - DESCR
          - ENVRDATA
          - LIKE
          - NOREPLACE
          - QSGDISP
          - REPLACE
          - USERDATA
        pcf_unmapped: []
      response:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped: []
    notes: []
  - mqsc:
      name: DELETE PROCESS
      href: SSFKSJ_9.4.0/refadmin/q085870_.html
      positional_parameters:
        - process-name
        - qmgr-name
      input_parameters:
        - CMDSCOPE
        - IGNSTATE
        - QSGDISP
      output_parameters: []
      section_sources:
        'Parameter descriptions for DELETE PROCESS':
          - CMDSCOPE
          - IGNSTATE
          - QSGDISP
    pcf:
      command: MQCMD_DELETE_PROCESS
      request_href: SSFKSJ_9.4.0/refadmin/q087170_.html
      response_href: SSFKSJ_9.4.0/refadmin/q087170_.html
      request_parameters:
        - name: ProcessName
          pcf_type: MQCFST
          type_hint: str
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: QSGDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSGD_COPY
            - MQQSGD_GROUP
            - MQQSGD_Q_MGR
        - name: IgnoreState
          pcf_type: MQCFST
          type_hint: str
          enum_values:
            - MQIS_YES
            - MQIS_NO
      response_parameters:
        - name: ProcessName
          pcf_type: MQCFST
          type_hint: str
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: QSGDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSGD_COPY
            - MQQSGD_GROUP
            - MQQSGD_Q_MGR
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
        unmapped:
          - CMDSCOPE
          - QSGDISP
        pcf_unmapped:
          - CommandScope
          - IgnoreState
          - ProcessName
          - QSGDisposition
      response:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - CommandScope
          - IgnoreState
          - ProcessName
          - QSGDisposition
    notes: []
  - mqsc:
      name: DISPLAY PROCESS
      href: SSFKSJ_9.4.0/refadmin/q086220_.html
      positional_parameters:
        - (generic-process-name)
        - filter-keyword
        - filter-value
        - operator
        - qmgr-name
      input_parameters: []
      output_parameters:
        - ALL
        - ALTDATE
        - ALTTIME
        - APPLICID
        - APPLTYPE
        - DESCR
        - ENVRDATA
        - USERDATA
      section_sources:
        {}
    pcf:
      command: MQCMD_INQUIRE_PROCESS
      request_href: SSFKSJ_9.4.0/refadmin/q087740_.html
      response_href: SSFKSJ_9.4.0/refadmin/q087750_.html
      request_parameters:
        - name: ProcessName
          pcf_type: MQCFST
          type_hint: str
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: IntegerFilterCommand
          pcf_type: MQCFIF
          type_hint: null
        - name: ProcessAttrs
          pcf_type: MQCFIL
          type_hint: int
          enum_values:
            - MQIACF_ALL
            - MQCA_ALTERATION_DATE
            - MQCA_ALTERATION_TIME
            - MQCA_APPL_ID
            - MQCA_ENV_DATA
            - MQCA_PROCESS_DESC
            - MQCA_PROCESS_NAME
            - MQCA_USER_DATA
            - MQIA_APPL_TYPE
        - name: QSGDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSGD_LIVE
            - MQQSGD_ALL
            - MQQSGD_COPY
            - MQQSGD_GROUP
            - MQQSGD_Q_MGR
            - MQQSGD_PRIVATE
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
        - name: ApplId
          pcf_type: MQCFST
          type_hint: str
        - name: ApplType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQAT_AIX
            - MQAT_CICS
            - MQAT_DOS
            - MQAT_MVS
            - MQAT_OS400
            - MQAT_QMGR
            - MQAT_UNIX
            - MQAT_WINDOWS
            - MQAT_WINDOWS_NT
        - name: EnvData
          pcf_type: MQCFST
          type_hint: str
        - name: ProcessDesc
          pcf_type: MQCFST
          type_hint: str
        - name: ProcessName
          pcf_type: MQCFST
          type_hint: str
        - name: QSGDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSGD_COPY
            - MQQSGD_GROUP
            - MQQSGD_Q_MGR
        - name: UserData
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
          - CommandScope
          - IntegerFilterCommand
          - ProcessAttrs
          - ProcessName
          - QSGDisposition
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
          - ApplId
          - ApplType
          - EnvData
          - ProcessDesc
          - ProcessName
          - QSGDisposition
          - UserData
    notes: []
```

## Process command re-parse

This addendum isolates corrected MQSC and PCF parameter sets. It is intentionally separate from the first-run extraction above and omits mapping heuristics.

```yaml
version: 1
generated_at: 2026-01-12T19:12:11Z
commands:
  - mqsc:
      name: ALTER PROCESS
      href: SSFKSJ_9.4.0/refadmin/q085300_.html
      positional_parameters:
        - (process-name)
      input_parameters:
        - APPLICID
        - APPLTYPE
        - CMDSCOPE
        - DESCR
        - ENVRDATA
        - QSGDISP
        - USERDATA
      output_parameters: []
      section_sources:
        'Parameter descriptions for ALTER PROCESS':
          - APPLICID
          - APPLTYPE
          - CMDSCOPE
          - DESCR
          - ENVRDATA
          - QSGDISP
          - USERDATA
    pcf:
      command: MQCMD_CHANGE_PROCESS
      request_href: SSFKSJ_9.4.0/refadmin/q086980_.html
      response_href: null
      request_parameters:
        - name: ProcessName
          pcf_type: MQCFST
          type_hint: str
        - name: ApplId
          pcf_type: MQCFST
          type_hint: str
        - name: ApplType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQAT_OS400
            - MQAT_DOS
            - MQAT_WINDOWS
            - MQAT_AIX
            - MQAT_CICS
            - MQAT_ZOS
            - MQAT_DEFAULT
            - MQAT_UNIX
            - MQAT_OS2
            - MQAT_WINDOWS_NT
            - MQAT_IMS
            - MQAT_MVS
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: EnvData
          pcf_type: MQCFST
          type_hint: str
        - name: ProcessDesc
          pcf_type: MQCFST
          type_hint: str
        - name: QSGDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSGD_COPY
            - MQQSGD_GROUP
            - MQQSGD_PRIVATE
            - MQQSGD_Q_MGR
        - name: Replace
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQRP_YES
            - MQRP_NO
        - name: UserData
          pcf_type: MQCFST
          type_hint: str
      response_parameters: []
    notes:
      - change-process-excludes-copy-only-parameters
  - mqsc:
      name: DEFINE PROCESS
      href: SSFKSJ_9.4.0/refadmin/q085670_.html
      positional_parameters:
        - (process-name)
      input_parameters:
        - APPLICID
        - APPLTYPE
        - CMDSCOPE
        - DESCR
        - ENVRDATA
        - LIKE
        - QSGDISP
        - REPLACE
        - NOREPLACE
        - USERDATA
      output_parameters: []
      section_sources:
        'Parameter descriptions for DEFINE PROCESS':
          - APPLICID
          - APPLTYPE
          - CMDSCOPE
          - DESCR
          - ENVRDATA
          - LIKE
          - QSGDISP
          - REPLACE
          - NOREPLACE
          - USERDATA
    pcf:
      command: MQCMD_CREATE_PROCESS
      request_href: SSFKSJ_9.4.0/refadmin/q086980_.html
      response_href: null
      request_parameters:
        - name: ProcessName
          pcf_type: MQCFST
          type_hint: str
        - name: ApplId
          pcf_type: MQCFST
          type_hint: str
        - name: ApplType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQAT_OS400
            - MQAT_DOS
            - MQAT_WINDOWS
            - MQAT_AIX
            - MQAT_CICS
            - MQAT_ZOS
            - MQAT_DEFAULT
            - MQAT_UNIX
            - MQAT_OS2
            - MQAT_WINDOWS_NT
            - MQAT_IMS
            - MQAT_MVS
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: EnvData
          pcf_type: MQCFST
          type_hint: str
        - name: ProcessDesc
          pcf_type: MQCFST
          type_hint: str
        - name: QSGDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSGD_COPY
            - MQQSGD_GROUP
            - MQQSGD_PRIVATE
            - MQQSGD_Q_MGR
        - name: Replace
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQRP_YES
            - MQRP_NO
        - name: UserData
          pcf_type: MQCFST
          type_hint: str
      response_parameters: []
    notes:
      - create-process-excludes-copy-only-parameters
  - mqsc:
      name: DELETE PROCESS
      href: SSFKSJ_9.4.0/refadmin/q085870_.html
      positional_parameters:
        - (process-name)
      input_parameters:
        - CMDSCOPE
        - QSGDISP
        - IGNSTATE
      output_parameters: []
      section_sources:
        'Parameter descriptions for DELETE PROCESS':
          - CMDSCOPE
          - QSGDISP
          - IGNSTATE
    pcf:
      command: MQCMD_DELETE_PROCESS
      request_href: SSFKSJ_9.4.0/refadmin/q087170_.html
      response_href: SSFKSJ_9.4.0/refadmin/q087170_.html
      request_parameters:
        - name: ProcessName
          pcf_type: MQCFST
          type_hint: str
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: QSGDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSGD_COPY
            - MQQSGD_GROUP
            - MQQSGD_Q_MGR
        - name: IgnoreState
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQIS_NO
            - MQIS_YES
      response_parameters:
        - name: ProcessName
          pcf_type: MQCFST
          type_hint: str
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: QSGDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSGD_COPY
            - MQQSGD_GROUP
            - MQQSGD_Q_MGR
        - name: IgnoreState
          pcf_type: MQCFST
          type_hint: str
          enum_values:
            - MQIS_YES
            - MQIS_NO
    notes:
      - ignore-state-type-inferred-from-mqsc-ignstate
      - ignore-state-name-normalized
  - mqsc:
      name: DISPLAY PROCESS
      href: SSFKSJ_9.4.0/refadmin/q086220_.html
      positional_parameters:
        - (generic-process-name)
      input_parameters:
        - ALL
        - WHERE
        - CMDSCOPE
        - QSGDISP
      output_parameters:
        - ALTDATE
        - ALTTIME
        - APPLICID
        - APPLTYPE
        - DESCR
        - ENVRDATA
        - USERDATA
      section_sources:
        'Parameter descriptions for DISPLAY PROCESS':
          - ALL
          - WHERE
          - CMDSCOPE
          - QSGDISP
        Requested parameters:
          - ALTDATE
          - ALTTIME
          - APPLICID
          - APPLTYPE
          - DESCR
          - ENVRDATA
          - USERDATA
    pcf:
      command: MQCMD_INQUIRE_PROCESS
      request_href: SSFKSJ_9.4.0/refadmin/q087740_.html
      response_href: SSFKSJ_9.4.0/refadmin/q087750_.html
      request_parameters:
        - name: ProcessName
          pcf_type: MQCFST
          type_hint: str
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: IntegerFilterCommand
          pcf_type: MQCFIF
          type_hint: null
        - name: ProcessAttrs
          pcf_type: MQCFIL
          type_hint: list[int]
          enum_values:
            - MQIACF_ALL
            - MQCA_ALTERATION_DATE
            - MQCA_ALTERATION_TIME
            - MQCA_APPL_ID
            - MQCA_ENV_DATA
            - MQCA_PROCESS_DESC
            - MQCA_PROCESS_NAME
            - MQCA_USER_DATA
            - MQIA_APPL_TYPE
        - name: QSGDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSGD_LIVE
            - MQQSGD_ALL
            - MQQSGD_COPY
            - MQQSGD_GROUP
            - MQQSGD_Q_MGR
            - MQQSGD_PRIVATE
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
        - name: ApplId
          pcf_type: MQCFST
          type_hint: str
        - name: ApplType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQAT_AIX
            - MQAT_CICS
            - MQAT_DOS
            - MQAT_MVS
            - MQAT_OS400
            - MQAT_QMGR
            - MQAT_UNIX
            - MQAT_WINDOWS
            - MQAT_WINDOWS_NT
        - name: EnvData
          pcf_type: MQCFST
          type_hint: str
        - name: ProcessDesc
          pcf_type: MQCFST
          type_hint: str
        - name: ProcessName
          pcf_type: MQCFST
          type_hint: str
        - name: QSGDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSGD_COPY
            - MQQSGD_GROUP
            - MQQSGD_Q_MGR
        - name: UserData
          pcf_type: MQCFST
          type_hint: str
    notes: []
```

## Output-parameter refresh

```yaml
version: 1
generated_at: 2026-02-02T19:46:59Z
commands:
  - name: DISPLAY PROCESS
    output_parameters:
      - ALL
      - ALTDATE
      - ALTTIME
      - APPLICID
      - APPLTYPE
      - DESCR
      - ENVRDATA
      - USERDATA
```
