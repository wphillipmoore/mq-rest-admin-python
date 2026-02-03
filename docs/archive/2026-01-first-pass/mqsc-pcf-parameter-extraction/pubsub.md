# MQSC to PCF parameter extraction: Pubsub

## Table of Contents

- [Purpose](#purpose)
- [First-run extraction](#first-run-extraction)

## Purpose

Collect MQSC and PCF parameter mappings for pubsub commands, split from the first-run extraction to keep each qualifier readable.

## First-run extraction

```yaml
version: 1
generated_at: 2026-01-11T23:40:29Z
commands:
  - mqsc:
      name: DISPLAY PUBSUB
      href: SSFKSJ_9.4.0/refadmin/q086230_.html
      positional_parameters:
        - qmgr-name
      input_parameters: []
      output_parameters:
        - CLUSRCVR
        - QMNAME
        - STATUS
        - SUBCOUNT
        - TPCOUNT
        - TYPE
      section_sources:
        {}
    pcf:
      command: MQCMD_INQUIRE_PUBSUB
      request_href: SSFKSJ_9.4.0/refadmin/q087780_.html
      response_href: null
      request_parameters:
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: PubSubStatusAttrs
          pcf_type: MQCFIL
          type_hint: int
          enum_values:
            - MQIACF_ALL
            - MQIA_SUB_COUNT
            - MQIA_TOPIC_NODE_COUNT
            - MQIACF_PUBSUB_STATUS
            - MQIACF_PS_STATUS_TYPE
        - name: Type
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPSST_ALL
            - MQPSST_LOCAL
            - MQPSST_PARENT
            - MQPSST_CHILD
      response_parameters: []
    mapping:
      request:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - CommandScope
          - PubSubStatusAttrs
          - Type
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
generated_at: 2026-02-02T19:46:59Z
commands:
  - name: DISPLAY PUBSUB
    output_parameters:
      - CLUSRCVR
      - QMNAME
      - STATUS
      - SUBCOUNT
      - TPCOUNT
      - TYPE
```
