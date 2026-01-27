# MQSC to PCF parameter extraction: Subscription

## Table of Contents
- [Purpose](#purpose)
- [First-run extraction](#first-run-extraction)
- [Subscription command re-parse](#subscription-command-re-parse)

## Purpose
Collect MQSC and PCF parameter mappings for subscription commands, split from the first-run extraction to keep each qualifier readable.

## First-run extraction
```yaml
version: 1
generated_at: 2026-01-11T23:40:29Z
commands:
  - mqsc:
      name: ALTER SUB
      href: SSFKSJ_9.4.0/refadmin/q085420_.html
      positional_parameters:
        - integer
        - qmgr-name
        - string
      input_parameters:
        - CMDSCOPE
        - DEST
        - DESTCORL
        - DESTQMGR
        - EXPIRY
        - PSPROP
        - PUBACCT
        - PUBAPPID
        - PUBPRTY
        - REQONLY
        - SUBUSER
        - USERDATA
        - VARUSER
      output_parameters: []
      section_sources:
        'Parameter descriptions for ALTER SUB':
          - CMDSCOPE
          - DEST
          - DESTCORL
          - DESTQMGR
          - EXPIRY
          - PSPROP
          - PUBACCT
          - PUBAPPID
          - PUBPRTY
          - REQONLY
          - SUBUSER
          - USERDATA
          - VARUSER
    pcf:
      command: MQCMD_CHANGE_SUB
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
          - DEST
          - DESTCORL
          - DESTQMGR
          - EXPIRY
          - PSPROP
          - PUBACCT
          - PUBAPPID
          - PUBPRTY
          - REQONLY
          - SUBUSER
          - USERDATA
          - VARUSER
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
      name: DEFINE SUB
      href: SSFKSJ_9.4.0/refadmin/q085760_.html
      positional_parameters:
        - integer
        - qmgr-name
        - string
        - subscription-name
      input_parameters:
        - CMDSCOPE
        - DEST
        - DESTCLAS
        - DESTCORL
        - DESTQMGR
        - EXPIRY
        - LIKE
        - NOREPLACE
        - PSPROP
        - PUBACCT
        - PUBAPPID
        - PUBPRTY
        - REPLACE
        - REQONLY
        - SELECTOR
        - SUBLEVEL
        - SUBNAME
        - SUBSCOPE
        - SUBUSER
        - TOPICOBJ
        - TOPICSTR
        - USERDATA
        - VARUSER
        - WSCHEMA
      output_parameters: []
      section_sources:
        'Parameter descriptions for DEFINE SUB':
          - CMDSCOPE
          - DEST
          - DESTCLAS
          - DESTCORL
          - DESTQMGR
          - EXPIRY
          - LIKE
          - NOREPLACE
          - PSPROP
          - PUBACCT
          - PUBAPPID
          - PUBPRTY
          - REPLACE
          - REQONLY
          - SELECTOR
          - SUBLEVEL
          - SUBNAME
          - SUBSCOPE
          - SUBUSER
          - TOPICOBJ
          - TOPICSTR
          - USERDATA
          - VARUSER
          - WSCHEMA
    pcf:
      command: MQCMD_CREATE_SUB
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
          - DEST
          - DESTCLAS
          - DESTCORL
          - DESTQMGR
          - EXPIRY
          - LIKE
          - NOREPLACE
          - PSPROP
          - PUBACCT
          - PUBAPPID
          - PUBPRTY
          - REPLACE
          - REQONLY
          - SELECTOR
          - SUBLEVEL
          - SUBNAME
          - SUBSCOPE
          - SUBUSER
          - TOPICOBJ
          - TOPICSTR
          - USERDATA
          - VARUSER
          - WSCHEMA
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
      name: DELETE SUB
      href: SSFKSJ_9.4.0/refadmin/q085950_.html
      positional_parameters:
        - qmgr-name
        - string
        - subscription-name
      input_parameters:
        - CMDSCOPE
        - IGNSTATE
        - SUBID
      output_parameters: []
      section_sources:
        'Parameter descriptions for DELETE SUB':
          - CMDSCOPE
          - IGNSTATE
          - SUBID
    pcf:
      command: MQCMD_DELETE_SUB
      request_href: SSFKSJ_9.4.0/refadmin/q087210_.html
      response_href: null
      request_parameters:
        - name: SubName
          pcf_type: MQCFST
          type_hint: str
        - name: SubId
          pcf_type: MQCFBS
          type_hint: bytes
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: IgnoreState
          pcf_type: MQCFST
          type_hint: str
          enum_values:
            - MQIS_YES
            - MQIS_NO
      response_parameters: []
    mapping:
      request:
        suggested:
          SUBID: SubId
        ambiguous:
          IGNSTATE:
            - IgnoreState
        unmapped:
          - CMDSCOPE
        pcf_unmapped:
          - CommandScope
          - IgnoreState
          - SubName
      response:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped: []
    notes: []
  - mqsc:
      name: DISPLAY SBSTATUS
      href: SSFKSJ_9.4.0/refadmin/q086280_.html
      positional_parameters:
        - (generic-name)
        - string
      input_parameters: []
      output_parameters:
        - COMMEV
      section_sources:
        {}
    pcf:
      command: MQCMD_INQUIRE_SB_STATUS
      request_href: SSFKSJ_9.4.0/refadmin/q087880_.html
      response_href: null
      request_parameters:
        - name: QName
          pcf_type: MQCFST
          type_hint: str
        - name: ByteStringFilterCommand
          pcf_type: MQCFBF
          type_hint: null
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: IntegerFilterCommand
          pcf_type: MQCFIF
          type_hint: null
        - name: OpenType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSOT_ALL
            - MQQSOT_INPUT
            - MQQSOT_OUTPUT
        - name: QSGDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSGD_COPY
            - MQQSGD_Q_MGR
            - MQQSGD_SHARED
        - name: QStatusAttrs
          pcf_type: MQCFIL
          type_hint: int
          enum_values:
            - MQIACF_ALL
            - MQCA_Q_NAME
            - MQCACF_LAST_GET_DATE
            - MQCACF_LAST_GET_TIME
            - MQCACF_LAST_PUT_DATE
            - MQCACF_LAST_PUT_TIME
            - MQCACF_MEDIA_LOG_EXTENT_NAME
            - MQIA_CURRENT_Q_DEPTH
            - MQIA_MONITORING_Q
            - MQIA_OPEN_INPUT_COUNT
            - MQIA_OPEN_OUTPUT_COUNT
            - MQIACF_HANDLE_STATE
            - MQIACF_MONITORING
            - MQIACF_CUR_MAX_FILE_SIZE
            - MQIACF_OLDEST_MSG_AGE
            - MQIACF_Q_TIME_INDICATOR
            - MQIACF_UNCOMMITTED_MSGS
            - MQBACF_EXTERNAL_UOW_ID
            - MQBACF_Q_MGR_UOW_ID
            - MQCACF_APPL_TAG
            - MQCACF_ASID
            - MQCACF_PSB_NAME
            - MQCACF_PSTID
            - MQCACF_TASK_NUMBER
            - MQCACF_TRANSACTION_ID
            - MQCACF_USER_IDENTIFIER
            - MQCACH_CHANNEL_NAME
            - MQCACH_CONNECTION_NAME
            - MQIA_APPL_TYPE
            - MQIACF_OPEN_BROWSE
            - MQIACF_OPEN_INPUT_TYPE
            - MQIACF_OPEN_INQUIRE
            - MQIACF_OPEN_OPTIONS
            - MQIACF_OPEN_OUTPUT
            - MQIACF_OPEN_SET
            - MQIACF_PROCESS_ID
            - MQIACF_ASYNC_STATE
            - MQIACF_THREAD_ID
            - MQIACF_UOW_TYPE
        - name: StatusType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQIACF_Q_STATUS
            - MQIACF_Q_HANDLE
        - name: StringFilterCommand
          pcf_type: MQCFSF
          type_hint: null
          enum_values:
            - MQRCCF_Q_TYPE_ERROR
      response_parameters: []
    mapping:
      request:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - ByteStringFilterCommand
          - CommandScope
          - IntegerFilterCommand
          - OpenType
          - QName
          - QSGDisposition
          - QStatusAttrs
          - StatusType
          - StringFilterCommand
      response:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped: []
    notes: []
  - mqsc:
      name: DISPLAY SUB
      href: SSFKSJ_9.4.0/refadmin/q086340_.html
      positional_parameters:
        - (generic-name)
        - filter-keyword
        - filter-value
        - integer
        - operator
        - qmgr-name
        - string
      input_parameters:
        - CMDSCOPE
        - DEST
        - DESTCLAS
        - DESTCORL
        - EXPIRY
        - PSPROP
        - PUBACCT
        - PUBAPPID
        - PUBPRTY
        - REQONLY
        - SELECTOR
        - SUBLEVEL
        - SUBSCOPE
        - SUBUSER
        - TOPICOBJ
        - USERDATA
        - VARUSER
        - WSCHEMA
      output_parameters:
        - CLUSQT
        - CMDSCOPE
        - DESCR
        - DEST
        - DESTCLAS
        - DESTCORL
        - DISTYPE
        - EXPIRY
        - HARDENBO
        - PSPROP
        - PUBACCT
        - PUBAPPID
        - PUBPRTY
        - REQONLY
        - SELECTOR
        - SHARE
        - SUBID
        - SUBLEVEL
        - SUBSCOPE
        - SUBTYPE
        - SUBUSER
        - TOPICOBJ
        - TOPICSTR
        - TRIGGER
        - USERDATA
        - VARUSER
        - WHERE
        - WSCHEMA
      section_sources:
        'Parameter descriptions for DISPLAY SUB':
          - CMDSCOPE
          - DEST
          - DESTCLAS
          - DESTCORL
          - EXPIRY
          - PSPROP
          - PUBACCT
          - PUBAPPID
          - PUBPRTY
          - REQONLY
          - SELECTOR
          - SUBLEVEL
          - SUBSCOPE
          - SUBUSER
          - TOPICOBJ
          - USERDATA
          - VARUSER
          - WSCHEMA
    pcf:
      command: MQCMD_INQUIRE_SUB
      request_href: SSFKSJ_9.4.0/refadmin/q088040_.html
      response_href: null
      request_parameters:
        - name: SubName
          pcf_type: MQCFST
          type_hint: str
        - name: SubId
          pcf_type: MQCFBS
          type_hint: bytes
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: Durable
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSUB_DURABLE_YES
            - MQSUB_DURABLE_NO
            - MQSUB_DURABLE_ALL
        - name: SubscriptionAttrs
          pcf_type: MQCFIL
          type_hint: int
          enum_values:
            - MQIACF_ALL
            - MQIACF_SUMMARY
            - MQBACF_ACCOUNTING_TOKEN
            - MQBACF_DESTINATION_CORREL_ID
            - MQBACF_SUB_ID
            - MQCA_ALTERATION_DATE
            - MQCA_ALTERATION_TIME
            - MQCA_CREATION_DATE
            - MQCA_CREATION_TIME
            - MQCA_TOPIC_STRING
            - MQCACF_APPL_IDENTITY_DATA
            - MQCACF_DESTINATION
            - MQCACF_DESTINATION_Q_MGR
            - MQCACF_SUB_NAME
            - MQCACF_SUB_SELECTOR
            - MQCACF_SUB_USER_DATA
            - MQCACF_SUB_USER_ID
            - MQCA_TOPIC_NAME
            - MQIACF_DESTINATION_CLASS
            - MQIACF_DURABLE_SUBSCRIPTION
            - MQIACF_EXPIRY
            - MQIACF_PUB_PRIORITY
            - MQIACF_PUBSUB_PROPERTIES
            - MQIACF_REQUEST_ONLY
            - MQIACF_SUB_TYPE
            - MQIACF_SUBSCRIPTION_SCOPE
            - MQIACF_SUB_LEVEL
            - MQIACF_VARIABLE_USER_ID
            - MQIACF_WILDCARD_SCHEMA
            - MQIA_DISPLAY_TYPE
        - name: SubscriptionType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSUBTYPE_ADMIN
            - MQSUBTYPE_ALL
            - MQSUBTYPE_API
            - MQSUBTYPE_PROXY
            - MQSUBTYPE_USER
        - name: DisplayType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQDOPT_RESOLVED
            - MQDOPT_DEFINED
      response_parameters: []
    mapping:
      request:
        suggested:
          {}
        ambiguous:
          {}
        unmapped:
          - CMDSCOPE
          - DEST
          - DESTCLAS
          - DESTCORL
          - EXPIRY
          - PSPROP
          - PUBACCT
          - PUBAPPID
          - PUBPRTY
          - REQONLY
          - SELECTOR
          - SUBLEVEL
          - SUBSCOPE
          - SUBUSER
          - TOPICOBJ
          - USERDATA
          - VARUSER
          - WSCHEMA
        pcf_unmapped:
          - CommandScope
          - DisplayType
          - Durable
          - SubId
          - SubName
          - SubscriptionAttrs
          - SubscriptionType
      response:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped: []
    notes:
      - display-parameter-descriptions-treated-as-input
```

## Subscription command re-parse
This addendum isolates corrected MQSC and PCF parameter sets. It is intentionally separate from the first-run extraction above and omits mapping heuristics.

```yaml
version: 1
generated_at: 2026-01-12T19:34:26Z
commands:
  - mqsc:
      name: ALTER SUB
      href: SSFKSJ_9.4.0/refadmin/q085420_.html
      positional_parameters:
        - (string)
      input_parameters:
        - CMDSCOPE
        - DEST
        - DESTCORL
        - DESTQMGR
        - EXPIRY
        - PSPROP
        - PUBACCT
        - PUBAPPID
        - PUBPRTY
        - REQONLY
        - SUBID
        - SUBUSER
        - USERDATA
        - VARUSER
      output_parameters: []
      section_sources:
        'Parameter descriptions for ALTER SUB':
          - CMDSCOPE
          - DEST
          - DESTCORL
          - DESTQMGR
          - EXPIRY
          - PSPROP
          - PUBACCT
          - PUBAPPID
          - PUBPRTY
          - REQONLY
          - SUBUSER
          - USERDATA
          - VARUSER
    pcf:
      command: MQCMD_CHANGE_SUBSCRIPTION
      request_href: SSFKSJ_9.4.0/refadmin/q087050_.html
      response_href: null
      request_parameters:
        - name: SubName
          pcf_type: MQCFST
          type_hint: str
        - name: SubId
          pcf_type: MQCFBS
          type_hint: bytes
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: TopicObject
          pcf_type: MQCFST
          type_hint: str
        - name: TopicString
          pcf_type: MQCFST
          type_hint: str
        - name: Destination
          pcf_type: MQCFST
          type_hint: str
        - name: DestinationClass
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQDC_MANAGED
            - MQDC_PROVIDED
        - name: DestinationCorrelId
          pcf_type: MQCFBS
          type_hint: bytes
        - name: DestinationQueueManager
          pcf_type: MQCFST
          type_hint: str
        - name: Expiry
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEI_UNLIMITED
        - name: PublishedAccountingToken
          pcf_type: MQCFBS
          type_hint: bytes
        - name: PublishedApplicationIdentifier
          pcf_type: MQCFST
          type_hint: str
        - name: PublishPriority
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPRI_PRIORITY_AS_PUBLISHED
            - MQPRI_PRIORITY_AS_QDEF
        - name: PublishSubscribeProperties
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPSPROP_COMPAT
            - MQPSPROP_NONE
            - MQPSPROP_RFH2
        - name: Selector
          pcf_type: MQCFST
          type_hint: str
        - name: SubscriptionLevel
          pcf_type: MQCFIN
          type_hint: int
        - name: SubscriptionScope
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQTSCOPE_ALL
            - MQTSCOPE_QMGR
        - name: SubscriptionUser
          pcf_type: MQCFST
          type_hint: str
        - name: Userdata
          pcf_type: MQCFST
          type_hint: str
        - name: VariableUser
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQVU_ANY_USER
            - MQVU_FIXED_USER
        - name: WildcardSchema
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQWS_CHAR
            - MQWS_TOPIC
      response_parameters: []
    notes:
      - change-subscription-excludes-copy-only-parameters
      - sub-and-subscription-terminology-mixed-in-docs
      - subid-accepted-via-syntax-diagram
      - variable-user-type-inferred-from-enum
  - mqsc:
      name: DEFINE SUB
      href: SSFKSJ_9.4.0/refadmin/q085760_.html
      positional_parameters:
        - (string)
      input_parameters:
        - CMDSCOPE
        - DEST
        - DESTCLAS
        - DESTCORL
        - DESTQMGR
        - EXPIRY
        - LIKE
        - NOREPLACE
        - PSPROP
        - PUBACCT
        - PUBAPPID
        - PUBPRTY
        - REPLACE
        - REQONLY
        - SELECTOR
        - SUBLEVEL
        - SUBNAME
        - SUBSCOPE
        - SUBUSER
        - TOPICOBJ
        - TOPICSTR
        - USERDATA
        - VARUSER
        - WSCHEMA
      output_parameters: []
      section_sources:
        'Parameter descriptions for DEFINE SUB':
          - CMDSCOPE
          - DEST
          - DESTCLAS
          - DESTCORL
          - DESTQMGR
          - EXPIRY
          - LIKE
          - NOREPLACE
          - PSPROP
          - PUBACCT
          - PUBAPPID
          - PUBPRTY
          - REPLACE
          - REQONLY
          - SELECTOR
          - SUBLEVEL
          - SUBNAME
          - SUBSCOPE
          - SUBUSER
          - TOPICOBJ
          - TOPICSTR
          - USERDATA
          - VARUSER
          - WSCHEMA
    pcf:
      command: MQCMD_CREATE_SUBSCRIPTION
      request_href: SSFKSJ_9.4.0/refadmin/q087050_.html
      response_href: null
      request_parameters:
        - name: SubName
          pcf_type: MQCFST
          type_hint: str
        - name: SubId
          pcf_type: MQCFBS
          type_hint: bytes
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: TopicObject
          pcf_type: MQCFST
          type_hint: str
        - name: TopicString
          pcf_type: MQCFST
          type_hint: str
        - name: Destination
          pcf_type: MQCFST
          type_hint: str
        - name: DestinationClass
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQDC_MANAGED
            - MQDC_PROVIDED
        - name: DestinationCorrelId
          pcf_type: MQCFBS
          type_hint: bytes
        - name: DestinationQueueManager
          pcf_type: MQCFST
          type_hint: str
        - name: Expiry
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEI_UNLIMITED
        - name: PublishedAccountingToken
          pcf_type: MQCFBS
          type_hint: bytes
        - name: PublishedApplicationIdentifier
          pcf_type: MQCFST
          type_hint: str
        - name: PublishPriority
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPRI_PRIORITY_AS_PUBLISHED
            - MQPRI_PRIORITY_AS_QDEF
        - name: PublishSubscribeProperties
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPSPROP_COMPAT
            - MQPSPROP_NONE
            - MQPSPROP_RFH2
        - name: Selector
          pcf_type: MQCFST
          type_hint: str
        - name: SubscriptionLevel
          pcf_type: MQCFIN
          type_hint: int
        - name: SubscriptionScope
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQTSCOPE_ALL
            - MQTSCOPE_QMGR
        - name: SubscriptionUser
          pcf_type: MQCFST
          type_hint: str
        - name: Userdata
          pcf_type: MQCFST
          type_hint: str
        - name: VariableUser
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQVU_ANY_USER
            - MQVU_FIXED_USER
        - name: WildcardSchema
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQWS_CHAR
            - MQWS_TOPIC
      response_parameters: []
    notes:
      - create-subscription-excludes-copy-only-parameters
      - variable-user-type-inferred-from-enum
  - mqsc:
      name: DELETE SUB
      href: SSFKSJ_9.4.0/refadmin/q085950_.html
      positional_parameters:
        - (subscription-name)
      input_parameters:
        - CMDSCOPE
        - SUBID
        - IGNSTATE
      output_parameters: []
      section_sources:
        'Parameter descriptions for DELETE SUB':
          - CMDSCOPE
          - SUBID
          - IGNSTATE
    pcf:
      command: MQCMD_DELETE_SUBSCRIPTION
      request_href: SSFKSJ_9.4.0/refadmin/q087210_.html
      response_href: null
      request_parameters:
        - name: SubName
          pcf_type: MQCFST
          type_hint: str
        - name: SubId
          pcf_type: MQCFBS
          type_hint: bytes
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: IgnoreState
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQIS_NO
            - MQIS_YES
      response_parameters: []
    notes:
      - delete-subscription-response-doc-not-found
      - ignore-state-type-inferred-from-mqsc-ignstate
      - ignore-state-name-normalized
  - mqsc:
      name: DISPLAY SUB
      href: SSFKSJ_9.4.0/refadmin/q086340_.html
      positional_parameters:
        - (generic-subscription-name)
      input_parameters:
        - ALL
        - WHERE
        - SUMMARY
        - CMDSCOPE
        - DISTYPE
        - SUBID
      output_parameters:
        - ALTDATE
        - ALTTIME
        - CRDATE
        - CRTIME
        - DEST
        - DESTCLAS
        - DESTCORL
        - DESTQMGR
        - DURABLE
        - EXPIRY
        - PSPROP
        - PUBACCT
        - PUBAPPID
        - PUBPRTY
        - REQONLY
        - SELECTOR
        - SUB
        - SUBID
        - SUBLEVEL
        - SUBSCOPE
        - SUBTYPE
        - SUBUSER
        - TOPICOBJ
        - TOPICSTR
        - USERDATA
        - VARUSER
        - WSCHEMA
      section_sources:
        'Parameter descriptions for DISPLAY SUB':
          - ALL
          - WHERE
          - SUMMARY
          - CMDSCOPE
          - DISTYPE
          - SUBID
          - ALTDATE
          - ALTTIME
          - CRDATE
          - CRTIME
          - DEST
          - DESTCLAS
          - DESTCORL
          - DESTQMGR
          - DURABLE
          - EXPIRY
          - PSPROP
          - PUBACCT
          - PUBAPPID
          - PUBPRTY
          - REQONLY
          - SELECTOR
          - SUB
          - SUBLEVEL
          - SUBSCOPE
          - SUBTYPE
          - SUBUSER
          - TOPICOBJ
          - TOPICSTR
          - USERDATA
          - VARUSER
          - WSCHEMA
    pcf:
      command: MQCMD_INQUIRE_SUBSCRIPTION
      request_href: SSFKSJ_9.4.0/refadmin/q088040_.html
      response_href: SSFKSJ_9.4.0/refadmin/q088050_.html
      request_parameters:
        - name: SubName
          pcf_type: MQCFST
          type_hint: str
        - name: SubId
          pcf_type: MQCFBS
          type_hint: bytes
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: Durable
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSUB_DURABLE_YES
            - MQSUB_DURABLE_NO
            - MQSUB_DURABLE_ALL
        - name: IntegerFilterCommand
          pcf_type: MQCFIF
          type_hint: null
        - name: SubscriptionAttrs
          pcf_type: MQCFIL
          type_hint: list[int]
          enum_values:
            - MQIACF_ALL
            - MQIACF_SUMMARY
            - MQBACF_ACCOUNTING_TOKEN
            - MQBACF_DESTINATION_CORREL_ID
            - MQBACF_SUB_ID
            - MQCA_ALTERATION_DATE
            - MQCA_ALTERATION_TIME
            - MQCA_CREATION_DATE
            - MQCA_CREATION_TIME
            - MQCA_TOPIC_STRING
            - MQCACF_APPL_IDENTITY_DATA
            - MQCACF_DESTINATION
            - MQCACF_DESTINATION_Q_MGR
            - MQCACF_SUB_NAME
            - MQCACF_SUB_SELECTOR
            - MQCACF_SUB_USER_DATA
            - MQCACF_SUB_USER_ID
            - MQCA_TOPIC_NAME
            - MQIACF_DESTINATION_CLASS
            - MQIACF_DURABLE_SUBSCRIPTION
            - MQIACF_EXPIRY
            - MQIACF_PUB_PRIORITY
            - MQIACF_PUBSUB_PROPERTIES
            - MQIACF_REQUEST_ONLY
            - MQIACF_SUB_TYPE
            - MQIACF_SUBSCRIPTION_SCOPE
            - MQIACF_SUB_LEVEL
            - MQIACF_VARIABLE_USER_ID
            - MQIACF_WILDCARD_SCHEMA
            - MQIA_DISPLAY_TYPE
        - name: SubscriptionType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSUBTYPE_ADMIN
            - MQSUBTYPE_ALL
            - MQSUBTYPE_API
            - MQSUBTYPE_PROXY
            - MQSUBTYPE_USER
        - name: DisplayType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQDOPT_RESOLVED
            - MQDOPT_DEFINED
        - name: StringFilterCommand
          pcf_type: MQCFSF
          type_hint: null
      response_parameters:
        - name: SubName
          pcf_type: MQCFST
          type_hint: str
        - name: SubId
          pcf_type: MQCFBS
          type_hint: bytes
        - name: AlterationDate
          pcf_type: MQCFST
          type_hint: str
        - name: AlterationTime
          pcf_type: MQCFST
          type_hint: str
        - name: CreationDate
          pcf_type: MQCFST
          type_hint: str
        - name: CreationTime
          pcf_type: MQCFST
          type_hint: str
        - name: Destination
          pcf_type: MQCFST
          type_hint: str
        - name: DestinationClass
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQDC_MANAGED
            - MQDC_PROVIDED
        - name: DestinationCorrelId
          pcf_type: MQCFBS
          type_hint: bytes
        - name: DestinationQueueManager
          pcf_type: MQCFST
          type_hint: str
        - name: DisplayType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQDOPT_RESOLVED
            - MQDOPT_DEFINED
        - name: Durable
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSUB_DURABLE_YES
            - MQSUB_DURABLE_NO
        - name: Expiry
          pcf_type: MQCFIN
          type_hint: int
        - name: PublishedAccountingToken
          pcf_type: MQCFBS
          type_hint: bytes
        - name: PublishedApplicationIdentityData
          pcf_type: MQCFST
          type_hint: str
        - name: PublishPriority
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPRI_PRIORITY_AS_PUBLISHED
            - MQPRI_PRIORITY_AS_QDEF
        - name: PublishSubscribeProperties
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPSPROP_NONE
            - MQPSPROP_MSGPROP
            - MQPSPROP_COMPAT
            - MQPSPROP_RFH2
        - name: Requestonly
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQRU_PUBLISH_ALL
            - MQRU_PUBLISH_ON_REQUEST
        - name: Selector
          pcf_type: MQCFST
          type_hint: str
        - name: SelectorType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSELTYPE_NONE
            - MQSELTYPE_STANDARD
            - MQSELTYPE_EXTENDED
        - name: SubscriptionLevel
          pcf_type: MQCFIN
          type_hint: int
        - name: SubscriptionScope
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQTSCOPE_ALL
            - MQTSCOPE_QMGR
        - name: SubscriptionType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSUBTYPE_PROXY
            - MQSUBTYPE_ADMIN
            - MQSUBTYPE_API
        - name: SubscriptionUser
          pcf_type: MQCFST
          type_hint: str
        - name: TopicObject
          pcf_type: MQCFST
          type_hint: str
        - name: TopicString
          pcf_type: MQCFST
          type_hint: str
        - name: Userdata
          pcf_type: MQCFST
          type_hint: str
        - name: VariableUser
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQVU_ANY_USER
            - MQVU_FIXED_USER
        - name: WildcardSchema
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQWS_CHAR
            - MQWS_TOPIC
    notes:
      - display-sub-output-from-parameter-descriptions
      - subid-accepted-as-selector
```













## Output-parameter refresh
```yaml
version: 1
generated_at: 2026-01-27T20:30:57Z
commands:
  - name: DISPLAY SBSTATUS
    output_parameters:
      - COMMEV
  - name: DISPLAY SUB
    output_parameters:
      - CLUSQT
      - CMDSCOPE
      - DESCR
      - DEST
      - DESTCLAS
      - DESTCORL
      - DISTYPE
      - EXPIRY
      - HARDENBO
      - PSPROP
      - PUBACCT
      - PUBAPPID
      - PUBPRTY
      - REQONLY
      - SELECTOR
      - SHARE
      - SUBID
      - SUBLEVEL
      - SUBSCOPE
      - SUBTYPE
      - SUBUSER
      - TOPICOBJ
      - TOPICSTR
      - TRIGGER
      - USERDATA
      - VARUSER
      - WHERE
      - WSCHEMA
```
