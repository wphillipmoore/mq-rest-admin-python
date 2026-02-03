# MQSC to PCF parameter extraction: Archive

## Table of Contents

- [Purpose](#purpose)
- [First-run extraction](#first-run-extraction)

## Purpose

Collect MQSC and PCF parameter mappings for archive commands, split from the first-run extraction to keep each qualifier readable.

## First-run extraction

```yaml
version: 1
generated_at: 2026-01-11T23:40:29Z
commands:
  - mqsc:
      name: DISPLAY ARCHIVE
      href: SSFKSJ_9.4.0/refadmin/q085980_.html
      positional_parameters:
        - qmgr-name
      input_parameters:
        - CMDSCOPE
      output_parameters:
        - CMDSCOPE
      section_sources:
        'Parameter descriptions for DISPLAY ARCHIVE':
          - CMDSCOPE
    pcf:
      command: MQCMD_INQUIRE_ARCHIVE
      request_href: SSFKSJ_9.4.0/refadmin/q087250_.html
      response_href: SSFKSJ_9.4.0/refadmin/q087260_.html
      request_parameters:
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
      response_parameters:
        - name: AllocPrimary
          pcf_type: MQCFIN
          type_hint: int
        - name: AllocSecondary
          pcf_type: MQCFIN
          type_hint: int
        - name: AllocUnits
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSYSP_ALLOC_BLK
            - MQSYSP_ALLOC_TRK
            - MQSYSP_ALLOC_CYL
        - name: ArchivePrefix1
          pcf_type: MQCFST
          type_hint: str
        - name: ArchivePrefix2
          pcf_type: MQCFST
          type_hint: str
        - name: ArchiveRetention
          pcf_type: MQCFIN
          type_hint: int
        - name: ArchiveUnit1
          pcf_type: MQCFST
          type_hint: str
        - name: ArchiveUnit2
          pcf_type: MQCFST
          type_hint: str
        - name: ArchiveWTOR
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSYSP_YES
            - MQSYSP_NO
        - name: BlockSize
          pcf_type: MQCFIN
          type_hint: int
        - name: Catalog
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSYSP_YES
            - MQSYSP_NO
        - name: Compact
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSYSP_YES
            - MQSYSP_NO
        - name: Protect
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSYSP_YES
            - MQSYSP_NO
        - name: QuiesceInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: RoutingCode
          pcf_type: MQCFIL
          type_hint: int
        - name: TimeStampFormat
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSYSP_YES
            - MQSYSP_NO
            - MQSYSP_EXTENDED
        - name: DataSetName
          pcf_type: MQCFST
          type_hint: str
        - name: LogCorrelId
          pcf_type: MQCFST
          type_hint: str
        - name: UnitAddress
          pcf_type: MQCFIN
          type_hint: int
        - name: UnitStatus
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSYSP_STATUS_BUSY
            - MQSYSP_STATUS_PREMOUNT
            - MQSYSP_STATUS_AVAILABLE
            - MQSYSP_STATUS_UNKNOWN
        - name: UnitVolser
          pcf_type: MQCFST
          type_hint: str
    mapping:
      request:
        suggested:
          {}
        ambiguous:
          {}
        unmapped:
          - CMDSCOPE
        pcf_unmapped:
          - CommandScope
      response:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - AllocPrimary
          - AllocSecondary
          - AllocUnits
          - ArchivePrefix1
          - ArchivePrefix2
          - ArchiveRetention
          - ArchiveUnit1
          - ArchiveUnit2
          - ArchiveWTOR
          - BlockSize
          - Catalog
          - Compact
          - DataSetName
          - LogCorrelId
          - Protect
          - QuiesceInterval
          - RoutingCode
          - TimeStampFormat
          - UnitAddress
          - UnitStatus
          - UnitVolser
    notes:
      - display-parameter-descriptions-treated-as-input
  - mqsc:
      name: SET ARCHIVE
      href: SSFKSJ_9.4.0/refadmin/q086610_.html
      positional_parameters:
        - qmgr-name
      input_parameters: []
      output_parameters: []
      section_sources:
        {}
    pcf:
      command: MQCMD_SET_ARCHIVE
      request_href: SSFKSJ_9.4.0/refadmin/q088370_.html
      response_href: SSFKSJ_9.4.0/refadmin/q086890_.html
      request_parameters:
        - name: ParameterType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSYSP_TYPE_INITIAL
            - MQSYSP_TYPE_SET
        - name: AllocPrimary
          pcf_type: MQCFIN
          type_hint: int
        - name: AllocSecondary
          pcf_type: MQCFIN
          type_hint: int
        - name: AllocUnits
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSYSP_ALLOC_BLK
            - MQSYSP_ALLOC_TRK
            - MQSYSP_ALLOC_CYL
        - name: ArchivePrefix1
          pcf_type: MQCFST
          type_hint: str
        - name: ArchivePrefix2
          pcf_type: MQCFST
          type_hint: str
        - name: ArchiveRetention
          pcf_type: MQCFIN
          type_hint: int
        - name: ArchiveUnit1
          pcf_type: MQCFST
          type_hint: str
        - name: ArchiveUnit2
          pcf_type: MQCFST
          type_hint: str
        - name: ArchiveWTOR
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSYSP_YES
            - MQSYSP_NO
        - name: BlockSize
          pcf_type: MQCFIN
          type_hint: int
        - name: Catalog
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSYSP_YES
            - MQSYSP_NO
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: Compact
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSYSP_YES
            - MQSYSP_NO
        - name: Protect
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSYSP_YES
            - MQSYSP_NO
        - name: QuiesceInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: RoutingCode
          pcf_type: MQCFIL
          type_hint: int
        - name: TimeStampFormat
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSYSP_YES
            - MQSYSP_NO
            - MQSYSP_EXTENDED
      response_parameters: []
    mapping:
      request:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - AllocPrimary
          - AllocSecondary
          - AllocUnits
          - ArchivePrefix1
          - ArchivePrefix2
          - ArchiveRetention
          - ArchiveUnit1
          - ArchiveUnit2
          - ArchiveWTOR
          - BlockSize
          - Catalog
          - CommandScope
          - Compact
          - ParameterType
          - Protect
          - QuiesceInterval
          - RoutingCode
          - TimeStampFormat
      response:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped: []
    notes: []
```
