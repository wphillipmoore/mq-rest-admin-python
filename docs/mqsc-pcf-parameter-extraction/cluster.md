# MQSC to PCF parameter extraction: Cluster

## Table of Contents
- [Purpose](#purpose)
- [First-run extraction](#first-run-extraction)

## Purpose
Collect MQSC and PCF parameter mappings for cluster commands, split from the first-run extraction to keep each qualifier readable.

## First-run extraction
```yaml
version: 1
generated_at: 2026-01-11T23:40:29Z
commands:
  - mqsc:
      name: REFRESH CLUSTER
      href: SSFKSJ_9.4.0/refadmin/q086470_.html
      positional_parameters:
        - generic-clustername
        - qmgr-name
      input_parameters: []
      output_parameters: []
      section_sources:
        {}
    pcf:
      command: MQCMD_REFRESH_CLUSTER
      request_href: SSFKSJ_9.4.0/refadmin/q088230_.html
      response_href: SSFKSJ_9.4.0/refadmin/q088230_.html
      request_parameters:
        - name: ClusterName
          pcf_type: MQCFST
          type_hint: str
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: RefreshRepository
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCFO_REFRESH_REPOSITORY_YES
            - MQCFO_REFRESH_REPOSITORY
      response_parameters:
        - name: ClusterName
          pcf_type: MQCFST
          type_hint: str
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: RefreshRepository
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCFO_REFRESH_REPOSITORY_YES
            - MQCFO_REFRESH_REPOSITORY
    mapping:
      request:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - ClusterName
          - CommandScope
          - RefreshRepository
      response:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - ClusterName
          - CommandScope
          - RefreshRepository
    notes: []
  - mqsc:
      name: RESET CLUSTER
      href: SSFKSJ_9.4.0/refadmin/q086520_.html
      positional_parameters:
        - (clustername)
        - qmgr-name
        - qmid
        - qmname
      input_parameters: []
      output_parameters: []
      section_sources:
        {}
    pcf:
      command: MQCMD_RESET_CLUSTER
      request_href: SSFKSJ_9.4.0/refadmin/q088280_.html
      response_href: SSFKSJ_9.4.0/refadmin/q088280_.html
      request_parameters:
        - name: ClusterName
          pcf_type: MQCFST
          type_hint: str
        - name: QMgrIdentifier
          pcf_type: MQCFST
          type_hint: str
        - name: QMgrName
          pcf_type: MQCFST
          type_hint: str
        - name: Action
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQACT_FORCE_REMOVE
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: RemoveQueues
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCFO_REMOVE_QUEUES_YES
            - MQCFO_REMOVE_QUEUES_NO
            - MQRCCF_ACTION_VALUE_ERROR
      response_parameters:
        - name: ClusterName
          pcf_type: MQCFST
          type_hint: str
        - name: QMgrIdentifier
          pcf_type: MQCFST
          type_hint: str
        - name: QMgrName
          pcf_type: MQCFST
          type_hint: str
        - name: Action
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQACT_FORCE_REMOVE
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: RemoveQueues
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCFO_REMOVE_QUEUES_YES
            - MQCFO_REMOVE_QUEUES_NO
            - MQRCCF_ACTION_VALUE_ERROR
    mapping:
      request:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - Action
          - ClusterName
          - CommandScope
          - QMgrIdentifier
          - QMgrName
          - RemoveQueues
      response:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - Action
          - ClusterName
          - CommandScope
          - QMgrIdentifier
          - QMgrName
          - RemoveQueues
    notes: []
```







