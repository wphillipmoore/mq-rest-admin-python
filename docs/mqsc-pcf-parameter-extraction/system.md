# MQSC to PCF parameter extraction: System

## Table of Contents
- [Purpose](#purpose)
- [First-run extraction](#first-run-extraction)

## Purpose
Collect MQSC and PCF parameter mappings for system commands, split from the first-run extraction to keep each qualifier readable.

## First-run extraction
```yaml
version: 1
generated_at: 2026-01-11T23:40:29Z
commands:
  - mqsc:
      name: DISPLAY SYSTEM
      href: SSFKSJ_9.4.0/refadmin/q086360_.html
      positional_parameters:
        - qmgr-name
      input_parameters: []
      output_parameters:
        - CMDSCOPE
      section_sources:
        {}
    pcf:
      command: MQCMD_INQUIRE_SYSTEM
      request_href: SSFKSJ_9.4.0/refadmin/q088080_.html
      response_href: SSFKSJ_9.4.0/refadmin/q088090_.html
      request_parameters:
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
      response_parameters:
        - name: CheckpointCount
          pcf_type: MQCFIN
          type_hint: int
        - name: ClusterCacheType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCLCT_STATIC
            - MQCLCT_DYNAMIC
        - name: CodedCharSetId
          pcf_type: MQCFIN
          type_hint: int
        - name: CommandUserId
          pcf_type: MQCFST
          type_hint: str
        - name: DB2BlobTasks
          pcf_type: MQCFIN
          type_hint: int
        - name: DB2Name
          pcf_type: MQCFST
          type_hint: str
        - name: DB2Tasks
          pcf_type: MQCFIN
          type_hint: int
        - name: DSGName
          pcf_type: MQCFST
          type_hint: str
        - name: Exclmsg
          pcf_type: MQCFSL
          type_hint: str
        - name: ExitInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: ExitTasks
          pcf_type: MQCFIN
          type_hint: int
        - name: MaximumAcePool
          pcf_type: MQCFIN
          type_hint: int
        - name: MULCCapture
          pcf_type: MQCFIN
          type_hint: int
        - name: OTMADruExit
          pcf_type: MQCFST
          type_hint: str
        - name: OTMAGroup
          pcf_type: MQCFST
          type_hint: str
        - name: OTMAInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: OTMAMember
          pcf_type: MQCFST
          type_hint: str
        - name: OTMSTpipePrefix
          pcf_type: MQCFST
          type_hint: str
        - name: QIndexDefer
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSYSP_YES
            - MQSYSP_NO
        - name: QSGName
          pcf_type: MQCFST
          type_hint: str
        - name: RESLEVELAudit
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSYSP_YES
            - MQSYSP_NO
        - name: RoutingCode
          pcf_type: MQCFIL
          type_hint: int
        - name: Service
          pcf_type: MQCFST
          type_hint: str
        - name: SMFAccounting
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSYSP_YES
            - MQSYSP_NO
        - name: SMFAcctIntervalMins
          pcf_type: MQCFIN
          type_hint: int
        - name: SMFAcctIntervalSecs
          pcf_type: MQCFIN
          type_hint: int
        - name: SMFInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: SMFStatistics
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSYSP_YES
            - MQSYSP_NO
        - name: SMFStatsIntervalMins
          pcf_type: MQCFIN
          type_hint: int
        - name: SMFStatsIntervalSecs
          pcf_type: MQCFIN
          type_hint: int
        - name: Splcap
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCAP_SUPPORTED
            - MQCAP_NOT_SUPPORTED
        - name: TraceClass
          pcf_type: MQCFIL
          type_hint: int
        - name: TraceSize
          pcf_type: MQCFIN
          type_hint: int
        - name: WLMInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: WLMIntervalUnits
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQTIME_UNITS_SEC
            - MQTIME_UNITS_MINS
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
          - CheckpointCount
          - ClusterCacheType
          - CodedCharSetId
          - CommandUserId
          - DB2BlobTasks
          - DB2Name
          - DB2Tasks
          - DSGName
          - Exclmsg
          - ExitInterval
          - ExitTasks
          - MULCCapture
          - MaximumAcePool
          - OTMADruExit
          - OTMAGroup
          - OTMAInterval
          - OTMAMember
          - OTMSTpipePrefix
          - QIndexDefer
          - QSGName
          - RESLEVELAudit
          - RoutingCode
          - SMFAccounting
          - SMFAcctIntervalMins
          - SMFAcctIntervalSecs
          - SMFInterval
          - SMFStatistics
          - SMFStatsIntervalMins
          - SMFStatsIntervalSecs
          - Service
          - Splcap
          - TraceClass
          - TraceSize
          - WLMInterval
          - WLMIntervalUnits
    notes: []
  - mqsc:
      name: SET SYSTEM
      href: SSFKSJ_9.4.0/refadmin/q086650_.html
      positional_parameters:
        - qmgr-name
      input_parameters: []
      output_parameters: []
      section_sources:
        {}
    pcf:
      command: MQCMD_SET_SYSTEM
      request_href: SSFKSJ_9.4.0/refadmin/q088410_.html
      response_href: SSFKSJ_9.4.0/refadmin/q088410_.html
      request_parameters:
        - name: ParameterType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSYSP_TYPE_INITIAL
            - MQSYSP_TYPE_SET
        - name: CheckpointCount
          pcf_type: MQCFIN
          type_hint: int
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: Exclmsg
          pcf_type: MQCFSL
          type_hint: str
        - name: Service
          pcf_type: MQCFST
          type_hint: str
        - name: SMFAcctIntervalMins
          pcf_type: MQCFIN
          type_hint: int
        - name: SMFAcctIntervalSecs
          pcf_type: MQCFIN
          type_hint: int
        - name: SMFStatsIntervalMins
          pcf_type: MQCFIN
          type_hint: int
        - name: SMFStatsIntervalSecs
          pcf_type: MQCFIN
          type_hint: int
        - name: TraceSize
          pcf_type: MQCFIN
          type_hint: int
      response_parameters:
        - name: ParameterType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSYSP_TYPE_INITIAL
            - MQSYSP_TYPE_SET
        - name: CheckpointCount
          pcf_type: MQCFIN
          type_hint: int
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: Exclmsg
          pcf_type: MQCFSL
          type_hint: str
        - name: Service
          pcf_type: MQCFST
          type_hint: str
        - name: SMFAcctIntervalMins
          pcf_type: MQCFIN
          type_hint: int
        - name: SMFAcctIntervalSecs
          pcf_type: MQCFIN
          type_hint: int
        - name: SMFStatsIntervalMins
          pcf_type: MQCFIN
          type_hint: int
        - name: SMFStatsIntervalSecs
          pcf_type: MQCFIN
          type_hint: int
        - name: TraceSize
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
          - CheckpointCount
          - CommandScope
          - Exclmsg
          - ParameterType
          - SMFAcctIntervalMins
          - SMFAcctIntervalSecs
          - SMFStatsIntervalMins
          - SMFStatsIntervalSecs
          - Service
          - TraceSize
      response:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - CheckpointCount
          - CommandScope
          - Exclmsg
          - ParameterType
          - SMFAcctIntervalMins
          - SMFAcctIntervalSecs
          - SMFStatsIntervalMins
          - SMFStatsIntervalSecs
          - Service
          - TraceSize
    notes: []
```












## Output-parameter refresh
```yaml
version: 1
generated_at: 2026-01-27T20:30:57Z
commands:
  - name: DISPLAY SYSTEM
    output_parameters:
      - CMDSCOPE
```
