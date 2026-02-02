# MQSC to PCF parameter extraction: Stgclass

## Table of Contents

- [Purpose](#purpose)
- [First-run extraction](#first-run-extraction)

## Purpose

Collect MQSC and PCF parameter mappings for stgclass commands, split from the first-run extraction to keep each qualifier readable.

## First-run extraction

```yaml
version: 1
generated_at: 2026-01-11T23:40:29Z
commands:
  - mqsc:
      name: ALTER STGCLASS
      href: SSFKSJ_9.4.0/refadmin/q085410_.html
      positional_parameters:
        - (storage-class)
        - application name
        - description
        - group name
        - integer
        - member name
        - qmgr-name
      input_parameters:
        - CMDSCOPE
        - DESCR
        - PASSTKTA
        - PSID
        - QSGDISP
        - XCFGNAME
        - XCFMNAME
      output_parameters: []
      section_sources:
        'Parameter descriptions for ALTER STGCLASS':
          - CMDSCOPE
          - DESCR
          - PASSTKTA
          - PSID
          - QSGDISP
          - XCFGNAME
          - XCFMNAME
    pcf:
      command: MQCMD_CHANGE_STGCLASS
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
        unmapped:
          - CMDSCOPE
          - DESCR
          - PASSTKTA
          - PSID
          - QSGDISP
          - XCFGNAME
          - XCFMNAME
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
      name: DEFINE STGCLASS
      href: SSFKSJ_9.4.0/refadmin/q085750_.html
      positional_parameters:
        - application name
        - description
        - group name
        - integer
        - member name
        - qmgr-name
        - stgclass-name
        - storage-class
      input_parameters:
        - CMDSCOPE
        - DESCR
        - LIKE
        - NOREPLACE
        - PASSTKTA
        - PSID
        - QSGDISP
        - REPLACE
        - XCFGNAME
        - XCFMNAME
      output_parameters: []
      section_sources:
        'Parameter descriptions for DEFINE STGCLASS':
          - CMDSCOPE
          - DESCR
          - LIKE
          - NOREPLACE
          - PASSTKTA
          - PSID
          - QSGDISP
          - REPLACE
          - XCFGNAME
          - XCFMNAME
    pcf:
      command: MQCMD_CREATE_STGCLASS
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
        unmapped:
          - CMDSCOPE
          - DESCR
          - LIKE
          - NOREPLACE
          - PASSTKTA
          - PSID
          - QSGDISP
          - REPLACE
          - XCFGNAME
          - XCFMNAME
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
      name: DELETE STGCLASS
      href: SSFKSJ_9.4.0/refadmin/q085960_.html
      positional_parameters:
        - name
        - qmgr-name
      input_parameters:
        - CMDSCOPE
        - QSGDISP
      output_parameters: []
      section_sources:
        'Parameter descriptions for DELETE STGCLASS':
          - CMDSCOPE
          - QSGDISP
    pcf:
      command: MQCMD_DELETE_STGCLASS
      request_href: SSFKSJ_9.4.0/refadmin/q087200_.html
      response_href: null
      request_parameters:
        - name: StorageClassName
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
      response_parameters: []
    mapping:
      request:
        suggested:
          {}
        ambiguous:
          {}
        unmapped:
          - CMDSCOPE
          - QSGDISP
        pcf_unmapped:
          - CommandScope
          - QSGDisposition
          - StorageClassName
      response:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped: []
    notes: []
  - mqsc:
      name: DISPLAY STGCLASS
      href: SSFKSJ_9.4.0/refadmin/q086330_.html
      positional_parameters:
        - (generic-class)
        - filter-keyword
        - filter-value
        - integer
        - operator
        - qmgr-name
      input_parameters: []
      output_parameters:
        - XCFGNAME
      section_sources:
        {}
    pcf:
      command: MQCMD_INQUIRE_STGCLASS
      request_href: SSFKSJ_9.4.0/refadmin/q088010_.html
      response_href: null
      request_parameters:
        - name: AlterationDate
          pcf_type: MQCFST
          type_hint: str
        - name: AlterationTime
          pcf_type: MQCFST
          type_hint: str
        - name: PageSetId
          pcf_type: MQCFIN
          type_hint: int
        - name: PassTicketApplication
          pcf_type: MQCFST
          type_hint: str
        - name: QSGDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSGD_COPY
            - MQQSGD_GROUP
            - MQQSGD_Q_MGR
        - name: StorageClassDesc
          pcf_type: MQCFST
          type_hint: str
        - name: StgClassName
          pcf_type: MQCFST
          type_hint: str
        - name: XCFGroupName
          pcf_type: MQCFST
          type_hint: str
        - name: XCFMemberName
          pcf_type: MQCFST
          type_hint: str
      response_parameters: []
    mapping:
      request:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - AlterationDate
          - AlterationTime
          - PageSetId
          - PassTicketApplication
          - QSGDisposition
          - StgClassName
          - StorageClassDesc
          - XCFGroupName
          - XCFMemberName
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
  - name: DISPLAY STGCLASS
    output_parameters:
      - XCFGNAME
```
