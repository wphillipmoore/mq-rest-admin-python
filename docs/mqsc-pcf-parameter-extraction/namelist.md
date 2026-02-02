# MQSC to PCF parameter extraction: Namelist

## Table of Contents

- [Purpose](#purpose)
- [First-run extraction](#first-run-extraction)
- [Namelist command re-parse](#namelist-command-re-parse)

## Purpose

Collect MQSC and PCF parameter mappings for namelist commands, split from the first-run extraction to keep each qualifier readable.

## First-run extraction

```yaml
version: 1
generated_at: 2026-01-11T23:40:29Z
commands:
  - mqsc:
      name: ALTER NAMELIST
      href: SSFKSJ_9.4.0/refadmin/q085290_.html
      positional_parameters:
        - (name)
        - name, ...
        - qmgr-name
        - string
      input_parameters:
        - CMDSCOPE
        - DESCR
        - NAMES
        - NLTYPE
        - QSGDISP
      output_parameters: []
      section_sources:
        'Parameter descriptions for ALTER NAMELIST':
          - CMDSCOPE
          - DESCR
          - NAMES
          - NLTYPE
          - QSGDISP
    pcf:
      command: MQCMD_CHANGE_NAMELIST
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
          - CMDSCOPE
          - DESCR
          - NAMES
          - NLTYPE
          - QSGDISP
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
      name: DEFINE NAMELIST
      href: SSFKSJ_9.4.0/refadmin/q085660_.html
      positional_parameters:
        - name
        - name, ...
        - namelist-name
        - qmgr-name
        - string
      input_parameters:
        - CMDSCOPE
        - DESCR
        - LIKE
        - NAMES
        - NLTYPE
        - NOREPLACE
        - QSGDISP
        - REPLACE
      output_parameters: []
      section_sources:
        'Parameter descriptions for DEFINE NAMELIST':
          - CMDSCOPE
          - DESCR
          - LIKE
          - NAMES
          - NLTYPE
          - NOREPLACE
          - QSGDISP
          - REPLACE
    pcf:
      command: MQCMD_CREATE_NAMELIST
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
          - CMDSCOPE
          - DESCR
          - LIKE
          - NAMES
          - NLTYPE
          - NOREPLACE
          - QSGDISP
          - REPLACE
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
      name: DELETE NAMELIST
      href: SSFKSJ_9.4.0/refadmin/q085860_.html
      positional_parameters:
        - name
        - qmgr-name
      input_parameters:
        - CMDSCOPE
        - IGNSTATE
        - QSGDISP
      output_parameters: []
      section_sources:
        'Parameter descriptions for DELETE NAMELIST':
          - CMDSCOPE
          - IGNSTATE
          - QSGDISP
    pcf:
      command: MQCMD_DELETE_NAMELIST
      request_href: SSFKSJ_9.4.0/refadmin/q087160_.html
      response_href: SSFKSJ_9.4.0/refadmin/q087160_.html
      request_parameters:
        - name: NamelistName
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
        - name: NamelistName
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
          - NamelistName
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
          - NamelistName
          - QSGDisposition
    notes: []
  - mqsc:
      name: DISPLAY NAMELIST
      href: SSFKSJ_9.4.0/refadmin/q086210_.html
      positional_parameters:
        - filter-keyword
        - filter-value
        - generic-namelist-name
        - operator
        - qmgr-name
      input_parameters: []
      output_parameters:
        - NLTYPE
        - QSGDISP
      section_sources:
        {}
    pcf:
      command: MQCMD_INQUIRE_NAMELIST
      request_href: SSFKSJ_9.4.0/refadmin/q087700_.html
      response_href: SSFKSJ_9.4.0/refadmin/q087710_.html
      request_parameters:
        - name: NamelistName
          pcf_type: MQCFST
          type_hint: str
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: IntegerFilterCommand
          pcf_type: MQCFIF
          type_hint: null
        - name: NamelistAttrs
          pcf_type: MQCFIL
          type_hint: int
          enum_values:
            - MQIACF_ALL
            - MQCA_NAMELIST_NAME
            - MQCA_NAMELIST_DESC
            - MQCA_NAMES
            - MQCA_ALTERATION_DATE
            - MQCA_ALTERATION_TIME
            - MQIA_NAME_COUNT
            - MQIA_NAMELIST_TYPE
        - name: NamelistType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQNT_NONE
            - MQNT_Q
            - MQNT_CLUSTER
            - MQNT_AUTH_INFO
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
        - name: NameCount
          pcf_type: MQCFIN
          type_hint: int
        - name: NamelistDesc
          pcf_type: MQCFST
          type_hint: str
        - name: NamelistName
          pcf_type: MQCFST
          type_hint: str
        - name: NamelistType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQNT_NONE
            - MQNT_Q
            - MQNT_CLUSTER
            - MQNT_AUTH_INFO
        - name: Names
          pcf_type: MQCFSL
          type_hint: str
        - name: QSGDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSGD_COPY
            - MQQSGD_GROUP
            - MQQSGD_Q_MGR
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
          - NamelistAttrs
          - NamelistName
          - NamelistType
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
          - NameCount
          - NamelistDesc
          - NamelistName
          - NamelistType
          - Names
          - QSGDisposition
    notes: []
```

## Namelist command re-parse

This addendum isolates corrected MQSC and PCF parameter sets. It is intentionally separate from the first-run extraction above and omits mapping heuristics.

```yaml
version: 1
generated_at: 2026-01-12T19:12:11Z
commands:
  - mqsc:
      name: ALTER NAMELIST
      href: SSFKSJ_9.4.0/refadmin/q085290_.html
      positional_parameters:
        - (name)
      input_parameters:
        - CMDSCOPE
        - DESCR
        - NAMES
        - NLTYPE
        - QSGDISP
      output_parameters: []
      section_sources:
        'Parameter descriptions for ALTER NAMELIST':
          - CMDSCOPE
          - DESCR
          - NAMES
          - NLTYPE
          - QSGDISP
    pcf:
      command: MQCMD_CHANGE_NAMELIST
      request_href: SSFKSJ_9.4.0/refadmin/q086970_.html
      response_href: null
      request_parameters:
        - name: NamelistName
          pcf_type: MQCFST
          type_hint: str
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: NamelistDesc
          pcf_type: MQCFST
          type_hint: str
        - name: NamelistType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQNT_NONE
            - MQNT_Q
            - MQNT_CLUSTER
            - MQNT_AUTH_INFO
        - name: Names
          pcf_type: MQCFSL
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
      response_parameters: []
    notes:
      - change-namelist-excludes-copy-only-parameters
  - mqsc:
      name: DEFINE NAMELIST
      href: SSFKSJ_9.4.0/refadmin/q085660_.html
      positional_parameters:
        - (name)
      input_parameters:
        - CMDSCOPE
        - DESCR
        - LIKE
        - NAMES
        - NLTYPE
        - QSGDISP
        - REPLACE
        - NOREPLACE
      output_parameters: []
      section_sources:
        'Parameter descriptions for DEFINE NAMELIST':
          - CMDSCOPE
          - DESCR
          - LIKE
          - NAMES
          - NLTYPE
          - QSGDISP
          - REPLACE
          - NOREPLACE
    pcf:
      command: MQCMD_CREATE_NAMELIST
      request_href: SSFKSJ_9.4.0/refadmin/q086970_.html
      response_href: null
      request_parameters:
        - name: NamelistName
          pcf_type: MQCFST
          type_hint: str
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: NamelistDesc
          pcf_type: MQCFST
          type_hint: str
        - name: NamelistType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQNT_NONE
            - MQNT_Q
            - MQNT_CLUSTER
            - MQNT_AUTH_INFO
        - name: Names
          pcf_type: MQCFSL
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
      response_parameters: []
    notes:
      - create-namelist-excludes-copy-only-parameters
  - mqsc:
      name: DELETE NAMELIST
      href: SSFKSJ_9.4.0/refadmin/q085860_.html
      positional_parameters:
        - (name)
      input_parameters:
        - CMDSCOPE
        - QSGDISP
        - IGNSTATE
      output_parameters: []
      section_sources:
        'Parameter descriptions for DELETE NAMELIST':
          - CMDSCOPE
          - QSGDISP
          - IGNSTATE
    pcf:
      command: MQCMD_DELETE_NAMELIST
      request_href: SSFKSJ_9.4.0/refadmin/q087160_.html
      response_href: null
      request_parameters:
        - name: NamelistName
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
      response_parameters: []
    notes:
      - delete-namelist-response-doc-not-found
      - ignore-state-type-inferred-from-mqsc-ignstate
      - ignore-state-name-normalized
  - mqsc:
      name: DISPLAY NAMELIST
      href: SSFKSJ_9.4.0/refadmin/q086210_.html
      positional_parameters:
        - (generic-namelist-name)
      input_parameters:
        - ALL
        - WHERE
        - CMDSCOPE
        - QSGDISP
        - NLTYPE
      output_parameters:
        - ALTDATE
        - ALTTIME
        - DESCR
        - NAMCOUNT
        - NAMES
      section_sources:
        'Parameter descriptions for DISPLAY NAMELIST':
          - ALL
          - WHERE
          - CMDSCOPE
          - QSGDISP
          - NLTYPE
        Requested parameters:
          - ALTDATE
          - ALTTIME
          - DESCR
          - NAMCOUNT
          - NAMES
    pcf:
      command: MQCMD_INQUIRE_NAMELIST
      request_href: SSFKSJ_9.4.0/refadmin/q087700_.html
      response_href: SSFKSJ_9.4.0/refadmin/q087710_.html
      request_parameters:
        - name: NamelistName
          pcf_type: MQCFST
          type_hint: str
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: IntegerFilterCommand
          pcf_type: MQCFIF
          type_hint: null
        - name: NamelistAttrs
          pcf_type: MQCFIL
          type_hint: list[int]
          enum_values:
            - MQIACF_ALL
            - MQCA_NAMELIST_NAME
            - MQCA_NAMELIST_DESC
            - MQCA_NAMES
            - MQCA_ALTERATION_DATE
            - MQCA_ALTERATION_TIME
            - MQIA_NAME_COUNT
            - MQIA_NAMELIST_TYPE
        - name: NamelistType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQNT_NONE
            - MQNT_Q
            - MQNT_CLUSTER
            - MQNT_AUTH_INFO
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
        - name: NameCount
          pcf_type: MQCFIN
          type_hint: int
        - name: NamelistDesc
          pcf_type: MQCFST
          type_hint: str
        - name: NamelistName
          pcf_type: MQCFST
          type_hint: str
        - name: NamelistType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQNT_NONE
            - MQNT_Q
            - MQNT_CLUSTER
            - MQNT_AUTH_INFO
        - name: Names
          pcf_type: MQCFSL
          type_hint: str
        - name: QSGDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSGD_COPY
            - MQQSGD_GROUP
            - MQQSGD_Q_MGR
    notes: []
```

## Output-parameter refresh

```yaml
version: 1
generated_at: 2026-01-27T20:30:57Z
commands:
  - name: DISPLAY NAMELIST
    output_parameters:
      - NLTYPE
      - QSGDISP
```
