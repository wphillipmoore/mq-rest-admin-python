# MQSC to PCF parameter extraction: Topic

## Table of Contents
- [Purpose](#purpose)
- [First-run extraction](#first-run-extraction)
- [Topic command re-parse](#topic-command-re-parse)

## Purpose
Collect MQSC and PCF parameter mappings for topic commands, split from the first-run extraction to keep each qualifier readable.

## First-run extraction
```yaml
version: 1
generated_at: 2026-01-11T23:40:29Z
commands:
  - mqsc:
      name: ALTER TOPIC
      href: SSFKSJ_9.4.0/refadmin/q085430_.html
      positional_parameters:
        - (topic-name)
        - comminfo-name
        - integer
        - qmgr-name
        - string
      input_parameters:
        - CAPEXPRY
        - CLROUTE
        - CLUSTER
        - CMDSCOPE
        - COMMINFO
        - CUSTOM
        - DEFPRESP
        - DEFPRTY
        - DEFPSIST
        - DESCR
        - DURSUB
        - MCAST
        - MDURMDL
        - MNDURMDL
        - NPMSGDLV
        - PMSGDLV
        - PROXYSUB
        - PUB
        - PUBSCOPE
        - QSGDISP
        - SUB
        - SUBSCOPE
        - TOPICSTR
        - TYPE
        - USEDLQ
      output_parameters: []
      section_sources:
        'Parameter descriptions for ALTER TOPIC':
          - CAPEXPRY
          - CLROUTE
          - CLUSTER
          - CMDSCOPE
          - COMMINFO
          - CUSTOM
          - DEFPRESP
          - DEFPRTY
          - DEFPSIST
          - DESCR
          - DURSUB
          - MCAST
          - MDURMDL
          - MNDURMDL
          - NPMSGDLV
          - PMSGDLV
          - PROXYSUB
          - PUB
          - PUBSCOPE
          - QSGDISP
          - SUB
          - SUBSCOPE
          - TOPICSTR
          - TYPE
          - USEDLQ
    pcf:
      command: MQCMD_CHANGE_TOPIC
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
          - CAPEXPRY
          - CLROUTE
          - CLUSTER
          - CMDSCOPE
          - COMMINFO
          - CUSTOM
          - DEFPRESP
          - DEFPRTY
          - DEFPSIST
          - DESCR
          - DURSUB
          - MCAST
          - MDURMDL
          - MNDURMDL
          - NPMSGDLV
          - PMSGDLV
          - PROXYSUB
          - PUB
          - PUBSCOPE
          - QSGDISP
          - SUB
          - SUBSCOPE
          - TOPICSTR
          - TYPE
          - USEDLQ
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
      name: CLEAR TOPICSTR
      href: SSFKSJ_9.4.0/refadmin/q085480_.html
      positional_parameters:
        - (topic-string)
        - qmgr-name
      input_parameters:
        - CLRTYPE
        - CMDSCOPE
        - SCOPE
      output_parameters: []
      section_sources:
        'Parameter descriptions for CLEAR TOPICSTR':
          - CLRTYPE
          - CMDSCOPE
          - SCOPE
    pcf:
      command: MQCMD_CLEAR_TOPICSTR
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
          - CLRTYPE
          - CMDSCOPE
          - SCOPE
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
      name: DEFINE TOPIC
      href: SSFKSJ_9.4.0/refadmin/q085770_.html
      positional_parameters:
        - comminfo-name
        - integer
        - string
        - topic-name
        - topic-type
      input_parameters:
        - CAPEXPRY
        - CLROUTE
        - CLUSTER
        - CMDSCOPE
        - COMMINFO
        - CUSTOM
        - DEFPRESP
        - DEFPRTY
        - DEFPSIST
        - DESCR
        - DURSUB
        - LIKE
        - MCAST
        - MDURMDL
        - MNDURMDL
        - NOREPLACE
        - NPMSGDLV
        - PMSGDLV
        - PROXYSUB
        - PUB
        - PUBSCOPE
        - QSGDISP
        - REPLACE
        - SUB
        - SUBSCOPE
        - TOPICSTR
        - TYPE
        - USEDLQ
        - WILDCARD
      output_parameters: []
      section_sources:
        'Parameter descriptions for DEFINE TOPIC':
          - CAPEXPRY
          - CLROUTE
          - CLUSTER
          - CMDSCOPE
          - COMMINFO
          - CUSTOM
          - DEFPRESP
          - DEFPRTY
          - DEFPSIST
          - DESCR
          - DURSUB
          - LIKE
          - MCAST
          - MDURMDL
          - MNDURMDL
          - NOREPLACE
          - NPMSGDLV
          - PMSGDLV
          - PROXYSUB
          - PUB
          - PUBSCOPE
          - QSGDISP
          - REPLACE
          - SUB
          - SUBSCOPE
          - TOPICSTR
          - TYPE
          - USEDLQ
          - WILDCARD
    pcf:
      command: MQCMD_CREATE_TOPIC
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
          - CAPEXPRY
          - CLROUTE
          - CLUSTER
          - CMDSCOPE
          - COMMINFO
          - CUSTOM
          - DEFPRESP
          - DEFPRTY
          - DEFPSIST
          - DESCR
          - DURSUB
          - LIKE
          - MCAST
          - MDURMDL
          - MNDURMDL
          - NOREPLACE
          - NPMSGDLV
          - PMSGDLV
          - PROXYSUB
          - PUB
          - PUBSCOPE
          - QSGDISP
          - REPLACE
          - SUB
          - SUBSCOPE
          - TOPICSTR
          - TYPE
          - USEDLQ
          - WILDCARD
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
      name: DELETE TOPIC
      href: SSFKSJ_9.4.0/refadmin/q085970_.html
      positional_parameters:
        - qmgr-name
        - topic-name
      input_parameters:
        - AUTHREC
        - CMDSCOPE
        - IGNSTATE
        - QSGDISP
      output_parameters: []
      section_sources:
        'Parameter descriptions for DELETE TOPIC':
          - AUTHREC
          - CMDSCOPE
          - IGNSTATE
          - QSGDISP
    pcf:
      command: MQCMD_DELETE_TOPIC
      request_href: SSFKSJ_9.4.0/refadmin/q087220_.html
      response_href: SSFKSJ_9.4.0/refadmin/q087220_.html
      request_parameters:
        - name: TopicName
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
        - name: Authrec
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQRAR_YES
            - MQRAR_NO
        - name: IgnoreState
          pcf_type: MQCFST
          type_hint: str
          enum_values:
            - MQIS_YES
            - MQIS_NO
      response_parameters:
        - name: TopicName
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
        - name: Authrec
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQRAR_YES
            - MQRAR_NO
        - name: IgnoreState
          pcf_type: MQCFST
          type_hint: str
          enum_values:
            - MQIS_YES
            - MQIS_NO
    mapping:
      request:
        suggested:
          AUTHREC: Authrec
        ambiguous:
          IGNSTATE:
            - IgnoreState
        unmapped:
          - CMDSCOPE
          - QSGDISP
        pcf_unmapped:
          - CommandScope
          - IgnoreState
          - QSGDisposition
          - TopicName
      response:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - Authrec
          - CommandScope
          - IgnoreState
          - QSGDisposition
          - TopicName
    notes: []
  - mqsc:
      name: DISPLAY TOPIC
      href: SSFKSJ_9.4.0/refadmin/q086380_.html
      positional_parameters:
        - (generic-topic-name)
        - filter-keyword
        - filter-value
        - integer
        - operator
        - qmgr-name
      input_parameters: []
      output_parameters:
        - ALTDATE
        - ALTTIME
        - CAPEXPRY
        - CLROUTE
        - CLSTATE
        - CLUSDATE
        - CLUSQMGR
        - CLUSTER
        - CLUSTIME
        - COMMINFO
        - CUSTOM
        - DEFPRESP
        - DEFPRTY
        - DEFPSIST
        - DESCR
        - DURSUB
        - MCAST
        - MDURMDL
        - MNDURMDL
        - MQ
        - NPMSGDLV
        - PAGEVAL
        - PMSGDLV
        - PROXYSUB
        - PUB
        - PUBSCOPE
        - QMID
        - SQGETTMR
        - SUB
        - SUBSCOPE
        - TOPICSTR
        - TYPE
        - USEDLQ
        - WILDCARD
      section_sources:
        {}
    pcf:
      command: MQCMD_INQUIRE_TOPIC
      request_href: SSFKSJ_9.4.0/refadmin/q088100_.html
      response_href: SSFKSJ_9.4.0/refadmin/q088110_.html
      request_parameters:
        - name: TopicName
          pcf_type: MQCFST
          type_hint: str
        - name: CapExpiry
          pcf_type: MQCFIN
          type_hint: int
        - name: ClusterInfo
          pcf_type: MQCFIN
          type_hint: int
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: IntegerFilterCommand
          pcf_type: MQCFIF
          type_hint: null
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
        - name: TopicAttrs
          pcf_type: MQCFIL
          type_hint: int
          enum_values:
            - MQIACF_ALL
            - MQCA_ALTERATION_DATE
            - MQCA_ALTERATION_TIME
            - MQCA_CLUSTER_NAME
            - MQCA_CLUSTER_DATE
            - MQCA_CLUSTER_TIME
            - MQCA_CLUSTER_Q_MGR_NAME
            - MQCA_CUSTOM
            - MQCA_MODEL_DURABLE_Q
            - MQCA_MODEL_NON_DURABLE_Q
            - MQCA_TOPIC_DESC
            - MQCA_TOPIC_NAME
            - MQCA_TOPIC_STRING
            - MQIA_CLUSTER_OBJECT_STATE
            - MQIA_CLUSTER_PUB_ROUTE
            - MQIA_DEF_PRIORITY
            - MQIA_DEF_PUT_RESPONSE_TYPE
            - MQIA_DURABLE_SUB
            - MQIA_INHIBIT_PUB
            - MQIA_INHIBIT_SUB
            - MQIA_NPM_DELIVERY
            - MQIA_PM_DELIVERY
            - MQIA_PROXY_SUB
            - MQIA_PUB_SCOPE
            - MQIA_SUB_SCOPE
            - MQIA_TOPIC_DEF_PERSISTENCE
            - MQIA_USE_DEAD_LETTER_Q
        - name: TopicType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQTOPT_ALL
            - MQTOPT_CLUSTER
            - MQTOPT_LOCAL
      response_parameters:
        - name: AlterationDate
          pcf_type: MQCFST
          type_hint: str
        - name: AlterationTime
          pcf_type: MQCFST
          type_hint: str
        - name: CapExpiry
          pcf_type: MQCFIN
          type_hint: int
        - name: ClusterName
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterObjectState
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCLST_ACTIVE
            - MQCLST_PENDING
            - MQCLST_INVALID
            - MQCLST_ERROR
        - name: ClusterPubRoute
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCLROUTE_DIRECT
            - MQCLROUTE_TOPIC_HOST
        - name: CommInfo
          pcf_type: MQCFST
          type_hint: str
        - name: Custom
          pcf_type: MQCFST
          type_hint: str
        - name: DefPersistence
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPER_PERSISTENCE_AS_PARENT
            - MQPER_PERSISTENT
            - MQPER_NOT_PERSISTENT
        - name: DefPriority
          pcf_type: MQCFIN
          type_hint: int
        - name: DefPutResponse
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPRT_ASYNC_RESPONSE
            - MQPRT_RESPONSE_AS_PARENT
            - MQPRT_SYNC_RESPONSE
        - name: DurableModelQName
          pcf_type: MQCFST
          type_hint: str
        - name: DurableSubscriptions
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSUB_DURABLE_AS_PARENT
            - MQSUB_DURABLE_ALLOWED
            - MQSUB_DURABLE_INHIBITED
        - name: InhibitPublications
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQTA_PUB_AS_PARENT
            - MQTA_PUB_INHIBITED
            - MQTA_PUB_ALLOWED
        - name: InhibitSubscriptions
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQTA_SUB_AS_PARENT
            - MQTA_SUB_INHIBITED
            - MQTA_SUB_ALLOWED
        - name: Multicast
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMC_ENABLED
            - MQMC_DISABLED
            - MQMC_ONLY
        - name: NonDurableModelQName
          pcf_type: MQCFST
          type_hint: str
        - name: NonPersistentMsgDelivery
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQDLV_AS_PARENT
            - MQDLV_ALL
            - MQDLV_ALL_DUR
            - MQDLV_ALL_AVAIL
        - name: PersistentMsgDelivery
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQDLV_AS_PARENT
            - MQDLV_ALL
            - MQDLV_ALL_DUR
            - MQDLV_ALL_AVAIL
        - name: ProxySubscriptions
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQTA_PROXY_SUB_FORCE
            - MQTA_PROXY_SUB_FIRSTUSE
        - name: PublicationScope
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSCOPE_ALL
            - MQSCOPE_AS_PARENT
            - MQSCOPE_QMGR
        - name: QMgrName
          pcf_type: MQCFST
          type_hint: str
        - name: SubscriptionScope
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSCOPE_ALL
            - MQSCOPE_AS_PARENT
            - MQSCOPE_QMGR
        - name: TopicDesc
          pcf_type: MQCFST
          type_hint: str
        - name: TopicName
          pcf_type: MQCFST
          type_hint: str
        - name: TopicString
          pcf_type: MQCFST
          type_hint: str
        - name: TopicType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQTOPT_LOCAL
            - MQTOPT_CLUSTER
        - name: UseDLQ
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQUSEDLQ_NO
            - MQUSEDLQ_YES
            - MQUSEDLQ_AS_PARENT
        - name: WildcardOperation
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQTA_PASSTHRU
            - MQTA_BLOCK
    mapping:
      request:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - CapExpiry
          - ClusterInfo
          - CommandScope
          - IntegerFilterCommand
          - QSGDisposition
          - StringFilterCommand
          - TopicAttrs
          - TopicName
          - TopicType
      response:
        suggested:
          COMMINFO: CommInfo
          CUSTOM: Custom
          USEDLQ: UseDLQ
        ambiguous:
          TOPICSTR:
            - TopicString
        unmapped:
          - ALTDATE
          - ALTTIME
          - CLROUTE
          - CLSTATE
          - CLUSDATE
          - CLUSQMGR
          - CLUSTER
          - CLUSTIME
          - DEFPRESP
          - DEFPRTY
          - DEFPSIST
          - DESCR
          - DURSUB
          - MCAST
          - MDURMDL
          - MNDURMDL
          - NPMSGDLV
          - PMSGDLV
          - PROXYSUB
          - PUB
          - PUBSCOPE
          - QMID
          - SUB
          - SUBSCOPE
          - TYPE
          - WILDCARD
        pcf_unmapped:
          - AlterationDate
          - AlterationTime
          - CapExpiry
          - ClusterName
          - ClusterObjectState
          - ClusterPubRoute
          - DefPersistence
          - DefPriority
          - DefPutResponse
          - DurableModelQName
          - DurableSubscriptions
          - InhibitPublications
          - InhibitSubscriptions
          - Multicast
          - NonDurableModelQName
          - NonPersistentMsgDelivery
          - PersistentMsgDelivery
          - ProxySubscriptions
          - PublicationScope
          - QMgrName
          - SubscriptionScope
          - TopicDesc
          - TopicName
          - TopicString
          - TopicType
          - WildcardOperation
    notes:
      - display-requested-parameters-table
```

## Topic command re-parse
This addendum isolates corrected MQSC and PCF parameter sets. It is intentionally separate from the first-run extraction above and omits mapping heuristics.

```yaml
version: 1
generated_at: 2026-01-12T19:34:26Z
commands:
  - mqsc:
      name: ALTER TOPIC
      href: SSFKSJ_9.4.0/refadmin/q085430_.html
      positional_parameters:
        - (topic-name)
      input_parameters:
        - CAPEXPRY
        - CLROUTE
        - CLUSTER
        - CMDSCOPE
        - COMMINFO
        - CUSTOM
        - DEFPRESP
        - DEFPRTY
        - DEFPSIST
        - DESCR
        - DURSUB
        - MCAST
        - MDURMDL
        - MNDURMDL
        - NPMSGDLV
        - PMSGDLV
        - PROXYSUB
        - PUB
        - PUBSCOPE
        - QSGDISP
        - SUB
        - SUBSCOPE
        - TOPICSTR
        - TYPE
        - USEDLQ
      output_parameters: []
      section_sources:
        'Parameter descriptions for ALTER TOPIC':
          - CAPEXPRY
          - CLROUTE
          - CLUSTER
          - CMDSCOPE
          - COMMINFO
          - CUSTOM
          - DEFPRESP
          - DEFPRTY
          - DEFPSIST
          - DESCR
          - DURSUB
          - MCAST
          - MDURMDL
          - MNDURMDL
          - NPMSGDLV
          - PMSGDLV
          - PROXYSUB
          - PUB
          - PUBSCOPE
          - QSGDISP
          - SUB
          - SUBSCOPE
          - TOPICSTR
          - TYPE
          - USEDLQ
    pcf:
      command: MQCMD_CHANGE_TOPIC
      request_href: SSFKSJ_9.4.0/refadmin/q087060_.html
      response_href: null
      request_parameters:
        - name: TopicName
          pcf_type: MQCFST
          type_hint: str
        - name: TopicString
          pcf_type: MQCFST
          type_hint: str
        - name: CapExpiry
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCEX_NOLIMIT
            - MQCEX_AS_PARENT
        - name: ClusterName
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterPubRoute
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCLROUTE_DIRECT
            - MQCLROUTE_TOPIC_HOST
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: CommunicationInformation
          pcf_type: MQCFST
          type_hint: str
        - name: Custom
          pcf_type: MQCFST
          type_hint: str
        - name: DefPersistence
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPER_PERSISTENCE_AS_PARENT
            - MQPER_PERSISTENT
            - MQPER_NOT_PERSISTENT
        - name: DefPriority
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPRI_PRIORITY_AS_PARENT
        - name: DefPutResponse
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPRT_ASYNC_RESPONSE
            - MQPRT_RESPONSE_AS_PARENT
            - MQPRT_SYNC_RESPONSE
        - name: DurableModelQName
          pcf_type: MQCFST
          type_hint: str
        - name: DurableSubscriptions
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSUB_DURABLE_AS_PARENT
            - MQSUB_DURABLE_ALLOWED
            - MQSUB_DURABLE_INHIBITED
        - name: InhibitPublications
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQTA_PUB_AS_PARENT
            - MQTA_PUB_INHIBITED
            - MQTA_PUB_ALLOWED
        - name: InhibitSubscriptions
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQTA_SUB_AS_PARENT
            - MQTA_SUB_INHIBITED
            - MQTA_SUB_ALLOWED
        - name: Multicast
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMC_AS_PARENT
            - MQMC_ENABLED
            - MQMC_DISABLED
            - MQMC_ONLY
        - name: NonDurableModelQName
          pcf_type: MQCFST
          type_hint: str
        - name: NonPersistentMsgDelivery
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQDLV_AS_PARENT
            - MQDLV_ALL
            - MQDLV_ALL_DUR
            - MQDLV_ALL_AVAIL
        - name: PersistentMsgDelivery
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQDLV_AS_PARENT
            - MQDLV_ALL
            - MQDLV_ALL_DUR
            - MQDLV_ALL_AVAIL
        - name: ProxySubscriptions
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQTA_PROXY_SUB_FORCE
            - MQTA_PROXY_SUB_FIRSTUSE
        - name: PublicationScope
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSCOPE_AS_PARENT
            - MQSCOPE_QMGR
            - MQSCOPE_ALL
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
        - name: SubscriptionScope
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSCOPE_AS_PARENT
            - MQSCOPE_QMGR
            - MQSCOPE_ALL
        - name: TopicDesc
          pcf_type: MQCFST
          type_hint: str
        - name: TopicType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQTOPT_LOCAL
        - name: UseDLQ
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQUSEDLQ_AS_PARENT
            - MQUSEDLQ_NO
            - MQUSEDLQ_YES
        - name: WildcardOperation
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQTA_PASSTHRU
            - MQTA_BLOCK
      response_parameters: []
    notes:
      - change-topic-excludes-copy-only-parameters
  - mqsc:
      name: DEFINE TOPIC
      href: SSFKSJ_9.4.0/refadmin/q085770_.html
      positional_parameters:
        - (topic-name)
      input_parameters:
        - CAPEXPRY
        - CLROUTE
        - CLUSTER
        - CMDSCOPE
        - COMMINFO
        - CUSTOM
        - DEFPRESP
        - DEFPRTY
        - DEFPSIST
        - DESCR
        - DURSUB
        - LIKE
        - MCAST
        - MDURMDL
        - MNDURMDL
        - NOREPLACE
        - NPMSGDLV
        - PMSGDLV
        - PROXYSUB
        - PUB
        - PUBSCOPE
        - QSGDISP
        - REPLACE
        - SUB
        - SUBSCOPE
        - TOPICSTR
        - TYPE
        - USEDLQ
        - WILDCARD
      output_parameters: []
      section_sources:
        'Parameter descriptions for DEFINE TOPIC':
          - CAPEXPRY
          - CLROUTE
          - CLUSTER
          - CMDSCOPE
          - COMMINFO
          - CUSTOM
          - DEFPRESP
          - DEFPRTY
          - DEFPSIST
          - DESCR
          - DURSUB
          - LIKE
          - MCAST
          - MDURMDL
          - MNDURMDL
          - NOREPLACE
          - NPMSGDLV
          - PMSGDLV
          - PROXYSUB
          - PUB
          - PUBSCOPE
          - QSGDISP
          - REPLACE
          - SUB
          - SUBSCOPE
          - TOPICSTR
          - TYPE
          - USEDLQ
          - WILDCARD
    pcf:
      command: MQCMD_CREATE_TOPIC
      request_href: SSFKSJ_9.4.0/refadmin/q087060_.html
      response_href: null
      request_parameters:
        - name: TopicName
          pcf_type: MQCFST
          type_hint: str
        - name: TopicString
          pcf_type: MQCFST
          type_hint: str
        - name: CapExpiry
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCEX_NOLIMIT
            - MQCEX_AS_PARENT
        - name: ClusterName
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterPubRoute
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCLROUTE_DIRECT
            - MQCLROUTE_TOPIC_HOST
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: CommunicationInformation
          pcf_type: MQCFST
          type_hint: str
        - name: Custom
          pcf_type: MQCFST
          type_hint: str
        - name: DefPersistence
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPER_PERSISTENCE_AS_PARENT
            - MQPER_PERSISTENT
            - MQPER_NOT_PERSISTENT
        - name: DefPriority
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPRI_PRIORITY_AS_PARENT
        - name: DefPutResponse
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPRT_ASYNC_RESPONSE
            - MQPRT_RESPONSE_AS_PARENT
            - MQPRT_SYNC_RESPONSE
        - name: DurableModelQName
          pcf_type: MQCFST
          type_hint: str
        - name: DurableSubscriptions
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSUB_DURABLE_AS_PARENT
            - MQSUB_DURABLE_ALLOWED
            - MQSUB_DURABLE_INHIBITED
        - name: InhibitPublications
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQTA_PUB_AS_PARENT
            - MQTA_PUB_INHIBITED
            - MQTA_PUB_ALLOWED
        - name: InhibitSubscriptions
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQTA_SUB_AS_PARENT
            - MQTA_SUB_INHIBITED
            - MQTA_SUB_ALLOWED
        - name: Multicast
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMC_AS_PARENT
            - MQMC_ENABLED
            - MQMC_DISABLED
            - MQMC_ONLY
        - name: NonDurableModelQName
          pcf_type: MQCFST
          type_hint: str
        - name: NonPersistentMsgDelivery
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQDLV_AS_PARENT
            - MQDLV_ALL
            - MQDLV_ALL_DUR
            - MQDLV_ALL_AVAIL
        - name: PersistentMsgDelivery
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQDLV_AS_PARENT
            - MQDLV_ALL
            - MQDLV_ALL_DUR
            - MQDLV_ALL_AVAIL
        - name: ProxySubscriptions
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQTA_PROXY_SUB_FORCE
            - MQTA_PROXY_SUB_FIRSTUSE
        - name: PublicationScope
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSCOPE_AS_PARENT
            - MQSCOPE_QMGR
            - MQSCOPE_ALL
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
        - name: SubscriptionScope
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSCOPE_AS_PARENT
            - MQSCOPE_QMGR
            - MQSCOPE_ALL
        - name: TopicDesc
          pcf_type: MQCFST
          type_hint: str
        - name: TopicType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQTOPT_LOCAL
        - name: UseDLQ
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQUSEDLQ_AS_PARENT
            - MQUSEDLQ_NO
            - MQUSEDLQ_YES
        - name: WildcardOperation
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQTA_PASSTHRU
            - MQTA_BLOCK
      response_parameters: []
    notes:
      - create-topic-excludes-copy-only-parameters
  - mqsc:
      name: DELETE TOPIC
      href: SSFKSJ_9.4.0/refadmin/q085970_.html
      positional_parameters:
        - (topic-name)
      input_parameters:
        - AUTHREC
        - CMDSCOPE
        - QSGDISP
        - IGNSTATE
      output_parameters: []
      section_sources:
        'Parameter descriptions for DELETE TOPIC':
          - AUTHREC
          - CMDSCOPE
          - QSGDISP
          - IGNSTATE
    pcf:
      command: MQCMD_DELETE_TOPIC
      request_href: SSFKSJ_9.4.0/refadmin/q087220_.html
      response_href: null
      request_parameters:
        - name: TopicName
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
        - name: Authrec
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQRAR_YES
            - MQRAR_NO
        - name: IgnoreState
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQIS_NO
            - MQIS_YES
      response_parameters: []
    notes:
      - delete-topic-response-doc-not-found
      - ignore-state-type-inferred-from-mqsc-ignstate
      - ignore-state-name-normalized
  - mqsc:
      name: DISPLAY TOPIC
      href: SSFKSJ_9.4.0/refadmin/q086380_.html
      positional_parameters:
        - (generic-topic-name)
      input_parameters:
        - WHERE
        - ALL
        - CMDSCOPE
        - QSGDISP
        - CLUSINFO
        - CLUSTER
        - TYPE
      output_parameters:
        - ALTDATE
        - ALTTIME
        - CAPEXPRY
        - CLROUTE
        - CLSTATE
        - CLUSDATE
        - CLUSQMGR
        - CLUSTER
        - CLUSTIME
        - COMMINFO
        - CUSTOM
        - DEFPRESP
        - DEFPRTY
        - DEFPSIST
        - DESCR
        - DURSUB
        - MCAST
        - MDURMDL
        - MNDURMDL
        - NPMSGDLV
        - PMSGDLV
        - PROXYSUB
        - PUB
        - PUBSCOPE
        - QMID
        - SUB
        - SUBSCOPE
        - TOPICSTR
        - TYPE
        - USEDLQ
        - WILDCARD
      section_sources:
        'Parameter descriptions for DISPLAY TOPIC':
          - WHERE
          - ALL
          - CMDSCOPE
          - QSGDISP
          - CLUSINFO
          - CLUSTER
          - TYPE
        Requested parameters:
          - ALTDATE
          - ALTTIME
          - CAPEXPRY
          - CLROUTE
          - CLSTATE
          - CLUSDATE
          - CLUSQMGR
          - CLUSTER
          - CLUSTIME
          - COMMINFO
          - CUSTOM
          - DEFPRESP
          - DEFPRTY
          - DEFPSIST
          - DESCR
          - DURSUB
          - MCAST
          - MDURMDL
          - MNDURMDL
          - NPMSGDLV
          - PMSGDLV
          - PROXYSUB
          - PUB
          - PUBSCOPE
          - QMID
          - SUB
          - SUBSCOPE
          - TOPICSTR
          - TYPE
          - USEDLQ
          - WILDCARD
    pcf:
      command: MQCMD_INQUIRE_TOPIC
      request_href: SSFKSJ_9.4.0/refadmin/q088100_.html
      response_href: SSFKSJ_9.4.0/refadmin/q088110_.html
      request_parameters:
        - name: TopicName
          pcf_type: MQCFST
          type_hint: str
        - name: CapExpiry
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCEX_NOLIMIT
            - MQCEX_AS_PARENT
        - name: ClusterInfo
          pcf_type: MQCFIN
          type_hint: int
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: IntegerFilterCommand
          pcf_type: MQCFIF
          type_hint: null
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
        - name: TopicAttrs
          pcf_type: MQCFIL
          type_hint: list[int]
          enum_values:
            - MQIACF_ALL
            - MQCA_ALTERATION_DATE
            - MQCA_ALTERATION_TIME
            - MQCA_CLUSTER_NAME
            - MQCA_CLUSTER_DATE
            - MQCA_CLUSTER_TIME
            - MQCA_CLUSTER_Q_MGR_NAME
            - MQCA_CUSTOM
            - MQCA_MODEL_DURABLE_Q
            - MQCA_MODEL_NON_DURABLE_Q
            - MQCA_TOPIC_DESC
            - MQCA_TOPIC_NAME
            - MQCA_TOPIC_STRING
            - MQIA_CLUSTER_OBJECT_STATE
            - MQIA_CLUSTER_PUB_ROUTE
            - MQIA_DEF_PRIORITY
            - MQIA_DEF_PUT_RESPONSE_TYPE
            - MQIA_DURABLE_SUB
            - MQIA_INHIBIT_PUB
            - MQIA_INHIBIT_SUB
            - MQIA_NPM_DELIVERY
            - MQIA_PM_DELIVERY
            - MQIA_PROXY_SUB
            - MQIA_PUB_SCOPE
            - MQIA_SUB_SCOPE
            - MQIA_TOPIC_DEF_PERSISTENCE
            - MQIA_USE_DEAD_LETTER_Q
        - name: TopicType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQTOPT_ALL
            - MQTOPT_CLUSTER
            - MQTOPT_LOCAL
      response_parameters:
        - name: TopicName
          pcf_type: MQCFST
          type_hint: str
        - name: TopicType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQTOPT_LOCAL
            - MQTOPT_CLUSTER
        - name: QSGDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSGD_COPY
            - MQQSGD_GROUP
            - MQQSGD_Q_MGR
        - name: AlterationDate
          pcf_type: MQCFST
          type_hint: str
        - name: AlterationTime
          pcf_type: MQCFST
          type_hint: str
        - name: CapExpiry
          pcf_type: MQCFIN
          type_hint: int
        - name: ClusterName
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterObjectState
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCLST_ACTIVE
            - MQCLST_PENDING
            - MQCLST_INVALID
            - MQCLST_ERROR
        - name: ClusterPubRoute
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCLROUTE_DIRECT
            - MQCLROUTE_TOPIC_HOST
        - name: CommInfo
          pcf_type: MQCFST
          type_hint: str
        - name: Custom
          pcf_type: MQCFST
          type_hint: str
        - name: DefPersistence
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPER_PERSISTENCE_AS_PARENT
            - MQPER_PERSISTENT
            - MQPER_NOT_PERSISTENT
        - name: DefPriority
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPRI_PRIORITY_AS_PARENT
        - name: DefPutResponse
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPRT_ASYNC_RESPONSE
            - MQPRT_RESPONSE_AS_PARENT
            - MQPRT_SYNC_RESPONSE
        - name: DurableModelQName
          pcf_type: MQCFST
          type_hint: str
        - name: DurableSubscriptions
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSUB_DURABLE_AS_PARENT
            - MQSUB_DURABLE_ALLOWED
            - MQSUB_DURABLE_INHIBITED
        - name: InhibitPublications
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQTA_PUB_AS_PARENT
            - MQTA_PUB_INHIBITED
            - MQTA_PUB_ALLOWED
        - name: InhibitSubscriptions
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQTA_SUB_AS_PARENT
            - MQTA_SUB_INHIBITED
            - MQTA_SUB_ALLOWED
        - name: Multicast
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMC_ENABLED
            - MQMC_DISABLED
            - MQMC_ONLY
        - name: NonDurableModelQName
          pcf_type: MQCFST
          type_hint: str
        - name: NonPersistentMsgDelivery
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQDLV_AS_PARENT
            - MQDLV_ALL
            - MQDLV_ALL_DUR
            - MQDLV_ALL_AVAIL
        - name: PersistentMsgDelivery
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQDLV_AS_PARENT
            - MQDLV_ALL
            - MQDLV_ALL_DUR
            - MQDLV_ALL_AVAIL
        - name: ProxySubscriptions
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQTA_PROXY_SUB_FORCE
            - MQTA_PROXY_SUB_FIRSTUSE
        - name: PublicationScope
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSCOPE_ALL
            - MQSCOPE_AS_PARENT
            - MQSCOPE_QMGR
        - name: QMgrName
          pcf_type: MQCFST
          type_hint: str
        - name: SubscriptionScope
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSCOPE_ALL
            - MQSCOPE_AS_PARENT
            - MQSCOPE_QMGR
        - name: TopicDesc
          pcf_type: MQCFST
          type_hint: str
        - name: TopicString
          pcf_type: MQCFST
          type_hint: str
        - name: UseDLQ
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQUSEDLQ_NO
            - MQUSEDLQ_YES
            - MQUSEDLQ_AS_PARENT
        - name: WildcardOperation
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQTA_PASSTHRU
            - MQTA_BLOCK
    notes:
      - qsgdisposition-returned-on-zos-only
```













## Output-parameter refresh
```yaml
version: 1
generated_at: 2026-01-27T20:30:57Z
commands:
  - name: DISPLAY TOPIC
    output_parameters:
      - ALTDATE
      - ALTTIME
      - CAPEXPRY
      - CLROUTE
      - CLSTATE
      - CLUSDATE
      - CLUSQMGR
      - CLUSTER
      - CLUSTIME
      - COMMINFO
      - CUSTOM
      - DEFPRESP
      - DEFPRTY
      - DEFPSIST
      - DESCR
      - DURSUB
      - MCAST
      - MDURMDL
      - MNDURMDL
      - MQ
      - NPMSGDLV
      - PAGEVAL
      - PMSGDLV
      - PROXYSUB
      - PUB
      - PUBSCOPE
      - QMID
      - SQGETTMR
      - SUB
      - SUBSCOPE
      - TOPICSTR
      - TYPE
      - USEDLQ
      - WILDCARD
```
