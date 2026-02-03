# MQSC to PCF parameter extraction: Usage

## Table of Contents

- [Purpose](#purpose)
- [First-run extraction](#first-run-extraction)

## Purpose

Collect MQSC and PCF parameter mappings for usage commands, split from the first-run extraction to keep each qualifier readable.

## First-run extraction

```yaml
version: 1
generated_at: 2026-01-11T23:40:29Z
commands:
  - mqsc:
      name: DISPLAY USAGE
      href: SSFKSJ_9.4.0/refadmin/q086410_.html
      positional_parameters:
        - integer
        - qmgr-name
      input_parameters: []
      output_parameters:
        - CMDSCOPE
        - CSQE280I
        - CSQE285I
        - PSID
        - TYPE
      section_sources:
        {}
    pcf:
      command: MQCMD_INQUIRE_USAGE
      request_href: SSFKSJ_9.4.0/refadmin/q088160_.html
      response_href: SSFKSJ_9.4.0/refadmin/q088170_.html
      request_parameters:
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: PageSetId
          pcf_type: MQCFIN
          type_hint: int
        - name: UsageType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQIACF_USAGE_PAGESET
            - MQIACF_USAGE_DATA_SET
            - MQIACF_ALL
            - MQIACF_USAGE_SMDS
      response_parameters:
        - name: BufferPoolId
          pcf_type: MQCFIN
          type_hint: int
        - name: Encrypted
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSYSP_YES
            - MQSYSP_NO
        - name: ExpandCount
          pcf_type: MQCFIN
          type_hint: int
        - name: ExpandType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQUSAGE_EXPAND_NONE
            - MQUSAGE_EXPAND_USER
            - MQUSAGE_EXPAND_SYSTEM
        - name: NonPersistentDataPages
          pcf_type: MQCFIN
          type_hint: int
        - name: PageSetId
          pcf_type: MQCFIN
          type_hint: int
        - name: PageSetStatus
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQUSAGE_PS_AVAILABLE
            - MQUSAGE_PS_DEFINED
            - MQUSAGE_PS_OFFLINE
            - MQUSAGE_PS_NOT_DEFINED
            - MQUSAGE_PS_SUSPENDED
        - name: PersistentDataPages
          pcf_type: MQCFIN
          type_hint: int
        - name: TotalPages
          pcf_type: MQCFIN
          type_hint: int
        - name: UnusedPages
          pcf_type: MQCFIN
          type_hint: int
        - name: LogRBA
          pcf_type: MQCFST
          type_hint: str
        - name: BufferPoolId
          pcf_type: MQCFIN
          type_hint: int
        - name: FreeBuffers
          pcf_type: MQCFIN
          type_hint: int
        - name: FreeBuffersPercentage
          pcf_type: MQCFIN
          type_hint: int
        - name: TotalBuffers
          pcf_type: MQCFIN
          type_hint: int
        - name: BufferPoolLocation
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQBPLOCATION_ABOVE
            - MQBPLOCATION_BELOW
            - MQBPLOCATION_SWITCHING_ABOVE
            - MQBPLOCATION_SWITCHING_BELOW
        - name: PageClass
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPAGECLAS_4KB
            - MQPAGECLAS_FIXED4KB
        - name: DataSetName
          pcf_type: MQCFST
          type_hint: str
        - name: DataSetType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQUSAGE_DS_OLDEST_ACTIVE_UOW
            - MQUSAGE_DS_OLDEST_PS_RECOVERY
            - MQUSAGE__DS_OLDEST_CF_RECOVERY
        - name: LogRBA
          pcf_type: MQCFST
          type_hint: str
        - name: LogLRSN
          pcf_type: MQCFST
          type_hint: str
        - name: Encrypted
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSYSP_YES
            - MQSYSP_NO
        - name: SMDSStatus
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQUSAGE_SMDS_NO_DATA
            - MQUSAGE_SMDS_AVAILABLE
            - A
        - name: CFStrucNames
          pcf_type: MQCFSL
          type_hint: str
        - name: MQIACF_USAGE_OFFLOAD_MSGS
          pcf_type: MQCFIN
          type_hint: int
        - name: MQIACF_USAGE_TOTAL_BLOCKS
          pcf_type: MQCFIN
          type_hint: int
        - name: MQIACF_USAGE_DATA_BLOCKS
          pcf_type: MQCFIN
          type_hint: int
        - name: MQIACF_USAGE_USED_BLOCKS
          pcf_type: MQCFIN
          type_hint: int
        - name: MQIACF_USAGE_USED_RATE
          pcf_type: MQCFIN
          type_hint: int
        - name: MQIACF_SMDS_STATUS
          pcf_type: MQCFIN
          type_hint: int
        - name: MQIACF_USAGE_TYPE
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - B
        - name: CFStrucNames
          pcf_type: MQCFSL
          type_hint: str
        - name: MQIACF_USAGE_BLOCK_SIZE
          pcf_type: MQCFIN
          type_hint: int
        - name: MQIACF_USAGE_TOTAL_BUFFERS
          pcf_type: MQCFIN
          type_hint: int
        - name: MQIACF_USAGE_INUSE_BUFFERS
          pcf_type: MQCFIN
          type_hint: int
        - name: MQIACF_USAGE_SAVED_BUFFERS
          pcf_type: MQCFIN
          type_hint: int
        - name: MQIACF_USAGE_EMPTY_BUFFERS
          pcf_type: MQCFIN
          type_hint: int
        - name: MQIACF_USAGE_READS_SAVED
          pcf_type: MQCFIN
          type_hint: int
        - name: MQIACF_USAGE_LOWEST_FREE
          pcf_type: MQCFIN
          type_hint: int
        - name: MQIACF_USAGE_WAIT_RATE
          pcf_type: MQCFIN
          type_hint: int
        - name: MQIACF_SMDS_STATUS
          pcf_type: MQCFIN
          type_hint: int
        - name: MQIACF_USAGE_TYPE
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
          - PageSetId
          - UsageType
      response:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - BufferPoolId
          - BufferPoolId
          - BufferPoolLocation
          - CFStrucNames
          - CFStrucNames
          - DataSetName
          - DataSetType
          - Encrypted
          - Encrypted
          - ExpandCount
          - ExpandType
          - FreeBuffers
          - FreeBuffersPercentage
          - LogLRSN
          - LogRBA
          - LogRBA
          - MQIACF_SMDS_STATUS
          - MQIACF_SMDS_STATUS
          - MQIACF_USAGE_BLOCK_SIZE
          - MQIACF_USAGE_DATA_BLOCKS
          - MQIACF_USAGE_EMPTY_BUFFERS
          - MQIACF_USAGE_INUSE_BUFFERS
          - MQIACF_USAGE_LOWEST_FREE
          - MQIACF_USAGE_OFFLOAD_MSGS
          - MQIACF_USAGE_READS_SAVED
          - MQIACF_USAGE_SAVED_BUFFERS
          - MQIACF_USAGE_TOTAL_BLOCKS
          - MQIACF_USAGE_TOTAL_BUFFERS
          - MQIACF_USAGE_TYPE
          - MQIACF_USAGE_TYPE
          - MQIACF_USAGE_USED_BLOCKS
          - MQIACF_USAGE_USED_RATE
          - MQIACF_USAGE_WAIT_RATE
          - NonPersistentDataPages
          - PageClass
          - PageSetId
          - PageSetStatus
          - PersistentDataPages
          - SMDSStatus
          - TotalBuffers
          - TotalPages
          - UnusedPages
    notes: []
```

## Output-parameter refresh

```yaml
version: 1
generated_at: 2026-02-02T19:46:59Z
commands:
  - name: DISPLAY USAGE
    output_parameters:
      - CMDSCOPE
      - CSQE280I
      - CSQE285I
      - PSID
      - TYPE
```
