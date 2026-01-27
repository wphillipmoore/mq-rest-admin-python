# MQSC to PCF parameter extraction: Log

## Table of Contents
- [Purpose](#purpose)
- [First-run extraction](#first-run-extraction)

## Purpose
Collect MQSC and PCF parameter mappings for log commands, split from the first-run extraction to keep each qualifier readable.

## First-run extraction
```yaml
version: 1
generated_at: 2026-01-11T23:40:29Z
commands:
  - mqsc:
      name: ARCHIVE LOG
      href: SSFKSJ_9.4.0/refadmin/q085450_.html
      positional_parameters:
        - nnn
        - qmgr-name
      input_parameters:
        - CANCEL OFFLOAD
        - CMDSCOPE
        - MODE(QUIESCE)
        - TIME
        - WAIT
      output_parameters: []
      section_sources:
        'Parameter descriptions for ARCHIVE LOG':
          - CANCEL OFFLOAD
          - CMDSCOPE
          - MODE(QUIESCE)
          - TIME
          - WAIT
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
        unmapped:
          - CANCEL OFFLOAD
          - CMDSCOPE
          - MODE(QUIESCE)
          - TIME
          - WAIT
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
      name: DEFINE LOG
      href: SSFKSJ_9.4.0/refadmin/q085640_.html
      positional_parameters:
        - name
        - qmgr-name
      input_parameters:
        - CMDSCOPE
        - COPY
      output_parameters: []
      section_sources:
        'Parameter descriptions for DEFINE LOG':
          - CMDSCOPE
          - COPY
    pcf:
      command: MQCMD_CREATE_LOG
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
          - COPY
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
      name: DISPLAY LOG
      href: SSFKSJ_9.4.0/refadmin/q086180_.html
      positional_parameters:
        - qmgr-name
      input_parameters: []
      output_parameters:
        - CMDSCOPE
      section_sources:
        {}
    pcf:
      command: MQCMD_INQUIRE_LOG
      request_href: SSFKSJ_9.4.0/refadmin/q087680_.html
      response_href: SSFKSJ_9.4.0/refadmin/q087690_.html
      request_parameters:
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
      response_parameters:
        - name: DeallocateInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: DualActive
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSYSP_YES
            - MQSYSP_NO
        - name: DualArchive
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSYSP_YES
            - MQSYSP_NO
        - name: DualBSDS
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSYSP_YES
            - MQSYSP_NO
        - name: InputBufferSize
          pcf_type: MQCFIN
          type_hint: int
        - name: LogArchive
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSYSP_YES
            - MQSYSP_NO
        - name: LogCompression
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCOMPRESS_NONE
            - MQCOMPRESS_RLE
            - MQCOMPRESS_ANY
        - name: MaxArchiveLog
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxConcurrentOffloads
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxReadTapeUnits
          pcf_type: MQCFIN
          type_hint: int
        - name: OutputBufferCount
          pcf_type: MQCFIN
          type_hint: int
        - name: OutputBufferSize
          pcf_type: MQCFIN
          type_hint: int
        - name: ZHyperWrite
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSYSP_YES
            - MQSYSP_NO
        - name: ZHyperLink
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSYSP_YES
            - MQSYSP_NO
        - name: DataSetName
          pcf_type: MQCFST
          type_hint: str
        - name: Encrypted
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSYSP_YES
            - MQSYSP_NO
        - name: FullLogs
          pcf_type: MQCFIN
          type_hint: int
        - name: LogCompression
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCOMPRESS_NONE
            - MQCOMPRESS_RLE
            - MQCOMPRESS_ANY
        - name: LogCopyNumber
          pcf_type: MQCFIN
          type_hint: int
        - name: LogRBA
          pcf_type: MQCFST
          type_hint: str
        - name: LogSuspend
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSYSP_YES
            - MQSYSP_NO
        - name: LogUsed
          pcf_type: MQCFIN
          type_hint: int
        - name: OffloadStatus
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSYSP_STATUS_ALLOCATING_ARCHIVE
            - MQSYSP_STATUS_COPYING_BSDS
            - MQSYSP_STATUS_COPYING_LOG
            - MQSYSP_STATUS_BUSY
            - MQSYSP_STATUS_AVAILABLE
        - name: QMgrStartDate
          pcf_type: MQCFST
          type_hint: str
        - name: QMgrStartRBA
          pcf_type: MQCFST
          type_hint: str
        - name: QMgrStartTime
          pcf_type: MQCFST
          type_hint: str
        - name: TotalLogs
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
      response:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - DataSetName
          - DeallocateInterval
          - DualActive
          - DualArchive
          - DualBSDS
          - Encrypted
          - FullLogs
          - InputBufferSize
          - LogArchive
          - LogCompression
          - LogCompression
          - LogCopyNumber
          - LogRBA
          - LogSuspend
          - LogUsed
          - MaxArchiveLog
          - MaxConcurrentOffloads
          - MaxReadTapeUnits
          - OffloadStatus
          - OutputBufferCount
          - OutputBufferSize
          - QMgrStartDate
          - QMgrStartRBA
          - QMgrStartTime
          - TotalLogs
          - ZHyperLink
          - ZHyperWrite
    notes: []
  - mqsc:
      name: SET LOG
      href: SSFKSJ_9.4.0/refadmin/q129100_.html
      positional_parameters:
        - name
      input_parameters: []
      output_parameters: []
      section_sources:
        {}
    pcf:
      command: MQCMD_SET_LOG
      request_href: SSFKSJ_9.4.0/refadmin/q129110_.html
      response_href: SSFKSJ_9.4.0/refadmin/q129110_.html
      request_parameters:
        - name: ParameterType
          pcf_type: MQCFIN
          type_hint: int
        - name: Archive
          pcf_type: MQCFST
          type_hint: str
          enum_values:
            - MQRCCF_LOG_EXTENT_NOT_FOUND
            - MQRCCF_CURRENT_LOG_EXTENT
            - MQRCCF_LOG_TYPE_ERROR
            - MQRCCF_LOG_EXTENT_ERROR
      response_parameters:
        - name: ParameterType
          pcf_type: MQCFIN
          type_hint: int
        - name: Archive
          pcf_type: MQCFST
          type_hint: str
          enum_values:
            - MQRCCF_LOG_EXTENT_NOT_FOUND
            - MQRCCF_CURRENT_LOG_EXTENT
            - MQRCCF_LOG_TYPE_ERROR
            - MQRCCF_LOG_EXTENT_ERROR
    mapping:
      request:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - Archive
          - ParameterType
      response:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - Archive
          - ParameterType
    notes: []
```












## Output-parameter refresh
```yaml
version: 1
generated_at: 2026-01-27T20:30:57Z
commands:
  - name: DISPLAY LOG
    output_parameters:
      - CMDSCOPE
```
