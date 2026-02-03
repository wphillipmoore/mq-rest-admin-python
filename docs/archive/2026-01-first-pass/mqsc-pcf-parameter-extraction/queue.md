# MQSC to PCF parameter extraction: Queue

## Table of Contents

- [Purpose](#purpose)
- [First-run extraction](#first-run-extraction)
- [Queue command re-parse](#queue-command-re-parse)

## Purpose

Collect MQSC and PCF parameter mappings for queue commands, split from the first-run extraction to keep each qualifier readable.

## First-run extraction

```yaml
version: 1
generated_at: 2026-01-11T23:40:29Z
commands:
  - mqsc:
      name: CLEAR QLOCAL
      href: SSFKSJ_9.4.0/refadmin/q085470_.html
      positional_parameters:
        - (q-name)
      input_parameters:
        - CMDSCOPE
        - QSGDISP
      output_parameters: []
      section_sources:
        'Parameter descriptions for CLEAR QLOCAL':
          - CMDSCOPE
          - QSGDISP
    pcf:
      command: MQCMD_CLEAR_Q
      request_href: SSFKSJ_9.4.0/refadmin/q087070_.html
      response_href: SSFKSJ_9.4.0/refadmin/q087070_.html
      request_parameters:
        - name: QName
          pcf_type: MQCFST
          type_hint: str
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: QSGDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSGD_PRIVATE
            - MQQSGD_SHARED
            - MQRC_Q_NOT_EMPTY
            - MQRCCF_Q_WRONG_TYPE
      response_parameters:
        - name: QName
          pcf_type: MQCFST
          type_hint: str
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: QSGDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSGD_PRIVATE
            - MQQSGD_SHARED
            - MQRC_Q_NOT_EMPTY
            - MQRCCF_Q_WRONG_TYPE
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
          - QName
          - QSGDisposition
      response:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - CommandScope
          - QName
          - QSGDisposition
    notes: []
  - mqsc:
      name: DISPLAY QSTATUS
      href: SSFKSJ_9.4.0/refadmin/q086260_.html
      positional_parameters:
        - generic-qname
        - n
      input_parameters: []
      output_parameters:
        - APPLDESC
        - APPLTAG
        - APPLTYPE
        - ASID
        - ASTATE
        - BROWSE
        - CHANNEL
        - CONNAME
        - CURDEPTH
        - CURFSIZE
        - CURMAXFS
        - EXTURID
        - HSTATE
        - INPUT
        - INQUIRE
        - IPPROCS
        - LGETDATE
        - LGETTIME
        - LPUTDATE
        - LPUTTIME
        - MAXFSIZE
        - MEDIALOG
        - MONITOR
        - MONQ
        - MSGAGE
        - OFF
        - OPPROCS
        - OUTPUT
        - PID
        - PSBNAME
        - PSTID
        - QMURID
        - QSGDISP
        - QTIME
        - SET
        - TASKNO
        - TID
        - TRANSID
        - TYPE
        - UNCOM
        - URID
        - URTYPE
        - USERID
      section_sources:
        {}
    pcf:
      command: MQCMD_INQUIRE_Q_STATUS
      request_href: SSFKSJ_9.4.0/refadmin/q087880_.html
      response_href: SSFKSJ_9.4.0/refadmin/q087890_.html
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
      response_parameters:
        - name: CurrentMaxQFileSize
          pcf_type: MQCFIN
          type_hint: int
        - name: CurrentQFileSize
          pcf_type: MQCFIN
          type_hint: int
        - name: CurrentQDepth
          pcf_type: MQCFIN
          type_hint: int
        - name: LastGetDate
          pcf_type: MQCFST
          type_hint: str
        - name: LastGetTime
          pcf_type: MQCFST
          type_hint: str
        - name: LastPutDate
          pcf_type: MQCFST
          type_hint: str
        - name: LastPutTime
          pcf_type: MQCFST
          type_hint: str
        - name: MediaRecoveryLogExtent
          pcf_type: MQCFST
          type_hint: str
        - name: OldestMsgAge
          pcf_type: MQCFIN
          type_hint: int
        - name: OnQTime
          pcf_type: MQCFIL
          type_hint: int
        - name: OpenInputCount
          pcf_type: MQCFIN
          type_hint: int
        - name: OpenOutputCount
          pcf_type: MQCFIN
          type_hint: int
        - name: QName
          pcf_type: MQCFST
          type_hint: str
        - name: QSGDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSGD_COPY
            - MQQSGD_Q_MGR
            - MQQSGD_SHARED
        - name: QueueMonitoring
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_OFF
            - MQMON_LOW
            - MQMON_MEDIUM
            - MQMON_HIGH
        - name: StatusType
          pcf_type: MQCFST
          type_hint: str
        - name: UncommittedMsgs
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSUM_YES
            - MQQSUM_NO
        - name: ApplDesc
          pcf_type: MQCFST
          type_hint: str
        - name: ApplTag
          pcf_type: MQCFST
          type_hint: str
        - name: ApplType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQAT_QMGR
            - MQAT_CHANNEL_INITIATOR
            - MQAT_USER
            - MQAT_BATCH
            - MQAT_RRS_BATCH
            - MQAT_CICS
            - MQAT_IMS
            - MQAT_SYSTEM_EXTENSION
        - name: ASId
          pcf_type: MQCFST
          type_hint: str
        - name: AsynchronousState
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQAS_ACTIVE
            - MQAS_INACTIVE
            - MQAS_SUSPENDED
            - MQAS_SUSPENDED_TEMPORARY
            - MQAS_NONE
        - name: ChannelName
          pcf_type: MQCFST
          type_hint: str
        - name: ConnectionName
          pcf_type: MQCFST
          type_hint: str
        - name: ExternalUOWId
          pcf_type: MQCFBS
          type_hint: bytes
        - name: HandleState
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQHSTATE_ACTIVE
            - MQHSTATE_INACTIVE
        - name: OpenBrowse
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSO_YES
            - MQQSO_NO
        - name: OpenInputType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSO_NO
            - MQQSO_SHARED
            - MQQSO_EXCLUSIVE
        - name: OpenInquire
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSO_YES
            - MQQSO_NO
        - name: OpenOptions
          pcf_type: MQCFIN
          type_hint: int
        - name: OpenOutput
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSO_YES
            - MQQSO_NO
        - name: OpenSet
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSO_YES
            - MQQSO_NO
        - name: ProcessId
          pcf_type: MQCFIN
          type_hint: int
        - name: PSBName
          pcf_type: MQCFST
          type_hint: str
        - name: PSTId
          pcf_type: MQCFST
          type_hint: str
        - name: QMgrUOWId
          pcf_type: MQCFBS
          type_hint: bytes
        - name: QName
          pcf_type: MQCFST
          type_hint: str
        - name: QSGDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSGD_COPY
            - MQQSGD_Q_MGR
            - MQQSGD_SHARED
        - name: StatusType
          pcf_type: MQCFST
          type_hint: str
        - name: TaskNumber
          pcf_type: MQCFST
          type_hint: str
        - name: ThreadId
          pcf_type: MQCFIN
          type_hint: int
        - name: TransactionId
          pcf_type: MQCFST
          type_hint: str
        - name: UOWIdentifier
          pcf_type: MQCFBS
          type_hint: bytes
        - name: UOWType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQUOWT_Q_MGR
            - MQUOWT_CICS
            - MQUOWT_XA
        - name: UserIdentifier
          pcf_type: MQCFST
          type_hint: str
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
        pcf_unmapped:
          - ASId
          - ApplDesc
          - ApplTag
          - ApplType
          - AsynchronousState
          - ChannelName
          - ConnectionName
          - CurrentMaxQFileSize
          - CurrentQDepth
          - CurrentQFileSize
          - ExternalUOWId
          - HandleState
          - LastGetDate
          - LastGetTime
          - LastPutDate
          - LastPutTime
          - MediaRecoveryLogExtent
          - OldestMsgAge
          - OnQTime
          - OpenBrowse
          - OpenInputCount
          - OpenInputType
          - OpenInquire
          - OpenOptions
          - OpenOutput
          - OpenOutputCount
          - OpenSet
          - PSBName
          - PSTId
          - ProcessId
          - QMgrUOWId
          - QName
          - QName
          - QSGDisposition
          - QSGDisposition
          - QueueMonitoring
          - StatusType
          - StatusType
          - TaskNumber
          - ThreadId
          - TransactionId
          - UOWIdentifier
          - UOWType
          - UncommittedMsgs
          - UserIdentifier
    notes: []
  - mqsc:
      name: DISPLAY QUEUE
      href: SSFKSJ_9.4.0/refadmin/q086270_.html
      positional_parameters:
        - filter-keyword
        - filter-value
        - generic-name
        - generic-name)
        - integer
        - operator
        - qmgr-name
        - queue-name
        - queue-type
        - target-type
      input_parameters:
        - ALL
        - CLUSINFO
        - CLUSNL
        - CLUSTER
        - CMDSCOPE
        - COPY
        - EQ
        - GE
        - GROUP
        - GT
        - LE
        - LIVE
        - LK
        - LT
        - NE
        - NL
        - PRIVATE
        - PSID
        - QALIAS
        - QLOCAL
        - QMGR
        - QMODEL
        - QREMOTE
        - QSGDISP
        - SHARED
        - STGCLASS
        - TARGTYPE
        - TYPE
        - WHERE
      output_parameters:
        - ACCTQ
        - ALL
        - ALTDATE
        - ALTTIME
        - BOQNAME
        - BOTHRESH
        - CAPEXPRY
        - CFSTRUCT
        - CLCHNAME
        - CLUSDATE
        - CLUSNL
        - CLUSQMGR
        - CLUSQT
        - CLUSTER
        - CLUSTIME
        - CLWLPRTY
        - CLWLRANK
        - CLWLUSEQ
        - COMPAT
        - CRDATE
        - CRTIME
        - CURDEPTH
        - CUSTOM
        - DEFBIND
        - DEFPRESP
        - DEFPRTY
        - DEFPSIST
        - DEFREADA
        - DEFSOPT
        - DEFTYPE
        - DESCR
        - DISTL
        - FORCE
        - GET
        - HARDENBO
        - IMGRCOVQ
        - INDXTYPE
        - INITQ
        - IPPROCS
        - MAXDEPTH
        - MAXFSIZE
        - MAXMSGL
        - MONQ
        - MQPMO
        - MSGDLVSQ
        - NONE
        - NPMCLASS
        - OPPROCS
        - OTELPCTL
        - OTELTRAC
        - PAGEVAL
        - PROCESS
        - PROPCTL
        - PSID
        - PUT
        - QALIAS
        - QDEPTHHI
        - QDEPTHLO
        - QDPHIEV
        - QDPLOEV
        - QDPMAXEV
        - QLOCAL
        - QMGR
        - QMID
        - QREMOTE
        - QSGDISP
        - QSVCIEV
        - QSVCINT
        - QTYPE
        - RETINTVL
        - RNAME
        - RQMNAME
        - SCOPE
        - SHARE
        - SQGETTMR
        - STATQ
        - STGCLASS
        - STREAMQ
        - STRMQOS
        - TARGET
        - TARGTYPE
        - TPIPE
        - TRIGDATA
        - TRIGDPTH
        - TRIGGER
        - TRIGMPRI
        - TRIGTYPE
        - USAGE
        - XMITQ
      section_sources:
        'Parameter descriptions for DISPLAY QUEUE':
          - ALL
          - CLUSINFO
          - CLUSNL
          - CLUSTER
          - CMDSCOPE
          - COPY
          - EQ
          - GE
          - GROUP
          - GT
          - LE
          - LIVE
          - LK
          - LT
          - NE
          - NL
          - PRIVATE
          - PSID
          - QALIAS
          - QLOCAL
          - QMGR
          - QMODEL
          - QREMOTE
          - QSGDISP
          - SHARED
          - STGCLASS
          - TARGTYPE
          - TYPE
          - WHERE
        'Requested parameters':
          - ACCTQ
          - ALL
          - ALTDATE
          - ALTTIME
          - BOQNAME
          - BOTHRESH
          - CAPEXPRY
          - CLCHNAME
          - CLUSDATE
          - CLUSNL
          - CLUSQMGR
          - CLUSQT
          - CLUSTER
          - CLUSTIME
          - CLWLPRTY
          - CLWLRANK
          - CLWLUSEQ
          - COMPAT
          - CRDATE
          - CRTIME
          - CURDEPTH
          - CUSTOM
          - DEFBIND
          - DEFPRESP
          - DEFPRTY
          - DEFPSIST
          - DEFREADA
          - DEFSOPT
          - DEFTYPE
          - DESCR
          - DISTL
          - FORCE
          - GET
          - HARDENBO
          - IMGRCOVQ
          - INDXTYPE
          - INITQ
          - IPPROCS
          - MAXDEPTH
          - MAXFSIZE
          - MAXMSGL
          - MONQ
          - MSGDLVSQ
          - NONE
          - NPMCLASS
          - OPPROCS
          - OTELPCTL
          - OTELTRAC
          - PROCESS
          - PROPCTL
          - PUT
          - QALIAS
          - QDEPTHHI
          - QDEPTHLO
          - QDPHIEV
          - QDPLOEV
          - QDPMAXEV
          - QLOCAL
          - QMGR
          - QMID
          - QREMOTE
          - QSVCIEV
          - QSVCINT
          - QTYPE
          - RETINTVL
          - RNAME
          - RQMNAME
          - SCOPE
          - SHARE
          - STATQ
          - STGCLASS
          - STREAMQ
          - STRMQOS
          - TARGET
          - TARGTYPE
          - TPIPE
          - TRIGDATA
          - TRIGDPTH
          - TRIGGER
          - TRIGMPRI
          - TRIGTYPE
          - USAGE
          - XMITQ
    pcf:
      command: MQCMD_INQUIRE_Q
      request_href: SSFKSJ_9.4.0/refadmin/q087800_.html
      response_href: SSFKSJ_9.4.0/refadmin/q087810_.html
      request_parameters:
        - name: QName
          pcf_type: MQCFST
          type_hint: str
        - name: CapExpiry
          pcf_type: MQCFIN
          type_hint: int
        - name: CFStructure
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterInfo
          pcf_type: MQCFIN
          type_hint: int
        - name: ClusterName
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterNamelist
          pcf_type: MQCFST
          type_hint: str
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: IntegerFilterCommand
          pcf_type: MQCFIF
          type_hint: null
        - name: PageSetID
          pcf_type: MQCFIN
          type_hint: int
        - name: QAttrs
          pcf_type: MQCFIL
          type_hint: int
          enum_values:
            - MQIACF_ALL
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
            - MQQSGD_SHARED
        - name: QType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQT_ALL
            - MQQT_LOCAL
            - MQQT_ALIAS
            - MQQT_REMOTE
            - MQQT_CLUSTER
            - MQQT_MODEL
        - name: StorageClass
          pcf_type: MQCFST
          type_hint: str
        - name: StringFilterCommand
          pcf_type: MQCFSF
          type_hint: null
          enum_values:
            - MQRCCF_Q_TYPE_ERROR
      response_parameters:
        - name: AlterationDate
          pcf_type: MQCFST
          type_hint: str
        - name: AlterationTime
          pcf_type: MQCFST
          type_hint: str
        - name: BackoutRequeueName
          pcf_type: MQCFST
          type_hint: str
        - name: BackoutThreshold
          pcf_type: MQCFIN
          type_hint: int
        - name: BaseQName
          pcf_type: MQCFST
          type_hint: str
        - name: CapExpiry
          pcf_type: MQCFIN
          type_hint: int
        - name: CFStructure
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterChannelName
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterDate
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterName
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterNamelist
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterQType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCQT_LOCAL_Q
            - MQCQT_ALIAS_Q
            - MQCQT_REMOTE_Q
            - MQCQT_Q_MGR_ALIAS
        - name: ClusterTime
          pcf_type: MQCFST
          type_hint: str
        - name: CLWLQueuePriority
          pcf_type: MQCFIN
          type_hint: int
        - name: CLWLQueueRank
          pcf_type: MQCFIN
          type_hint: int
        - name: CLWLUseQ
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCLWL_USEQ_AS_Q_MGR
            - MQCLWL_USEQ_ANY
            - MQCLWL_USEQ_LOCAL
        - name: CreationDate
          pcf_type: MQCFST
          type_hint: str
        - name: CreationTime
          pcf_type: MQCFST
          type_hint: str
        - name: CurrentQDepth
          pcf_type: MQCFIN
          type_hint: int
        - name: Custom
          pcf_type: MQCFST
          type_hint: str
        - name: DefaultPutResponse
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPRT_SYNC_RESPONSE
            - MQPRT_ASYNC_RESPONSE
        - name: DefBind
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQBND_BIND_ON_OPEN
            - MQBND_BIND_NOT_FIXED
            - MQBND_BIND_ON_GROUP
        - name: DefinitionType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQDT_PREDEFINED
            - MQQDT_PERMANENT_DYNAMIC
            - MQQDT_SHARED_DYNAMIC
            - MQQDT_TEMPORARY_DYNAMIC
        - name: DefInputOpenOption
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQOO_INPUT_EXCLUSIVE
            - MQOO_INPUT_SHARED
        - name: DefPersistence
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPER_PERSISTENT
            - MQPER_NOT_PERSISTENT
        - name: DefPriority
          pcf_type: MQCFIN
          type_hint: int
        - name: DefReadAhead
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQREADA_NO
            - MQREADA_YES
            - MQREADA_DISABLED
        - name: DistLists
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQDL_SUPPORTED
            - MQDL_NOT_SUPPORTED
        - name: HardenGetBackout
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQA_BACKOUT_HARDENED
            - MQQA_BACKOUT_NOT_HARDENED
        - name: ImageRecoverQueue
          pcf_type: MQCFST
          type_hint: str
          enum_values:
            - MQIMGRCOV_YES
            - MQIMGRCOV_NO
            - MQIMGRCOV_AS_Q_MGR
        - name: IndexType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQIT_NONE
            - MQIT_MSG_ID
            - MQIT_CORREL_ID
            - MQIT_MSG_TOKEN
            - MQIT_GROUP_ID
        - name: InhibitGet
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQA_GET_ALLOWED
            - MQQA_GET_INHIBITED
        - name: InhibitPut
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQA_PUT_ALLOWED
            - MQQA_PUT_INHIBITED
        - name: InitiationQName
          pcf_type: MQCFST
          type_hint: str
        - name: MaxMsgLength
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxQDepth
          pcf_type: MQCFIN
          type_hint: int
        - name: MsgDeliverySequence
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMDS_PRIORITY
            - MQMDS_FIFO
        - name: NonPersistentMessageClass
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQNPM_CLASS_NORMAL
            - MQNPM_CLASS_HIGH
        - name: OpenInputCount
          pcf_type: MQCFIN
          type_hint: int
        - name: OpenOutputCount
          pcf_type: MQCFIN
          type_hint: int
        - name: OTELPropagationControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQOTEL_PCTL_QMGR
            - MQOTEL_PCTL_MANUAL
            - MQOTEL_PCTL_AUTO
        - name: OTELTrace
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQOTEL_TRACE_QMGR
            - MQOTEL_TRACE_OFF
            - MQOTEL_TRACE_ON
        - name: PageSetID
          pcf_type: MQCFIN
          type_hint: int
        - name: ProcessName
          pcf_type: MQCFST
          type_hint: str
        - name: PropertyControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPROP_COMPATIBILITY
            - MQPROP_NONE
            - MQPROP_ALL
        - name: QDepthHighEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
        - name: QDepthHighLimit
          pcf_type: MQCFIN
          type_hint: int
        - name: QDepthLowEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
        - name: QDepthLowLimit
          pcf_type: MQCFIN
          type_hint: int
        - name: QDepthMaxEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
        - name: QDesc
          pcf_type: MQCFST
          type_hint: str
        - name: QMgrIdentifier
          pcf_type: MQCFST
          type_hint: str
        - name: QMgrName
          pcf_type: MQCFST
          type_hint: str
        - name: QName
          pcf_type: MQCFST
          type_hint: str
        - name: QServiceInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: QServiceIntervalEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSIE_HIGH
            - MQQSIE_OK
            - MQQSIE_NONE
        - name: QSGDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSGD_COPY
            - MQQSGD_GROUP
            - MQQSGD_Q_MGR
            - MQQSGD_SHARED
        - name: QType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQT_ALIAS
            - MQQT_CLUSTER
            - MQQT_LOCAL
            - MQQT_REMOTE
            - MQQT_MODEL
        - name: QueueAccounting
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_Q_MGR
            - MQMON_OFF
            - MQMON_ON
        - name: QueueMonitoring
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_OFF
            - MQMON_Q_MGR
            - MQMON_LOW
            - MQMON_MEDIUM
            - MQMON_HIGH
        - name: QueueStatistics
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_Q_MGR
            - MQMON_OFF
            - MQMON_ON
        - name: RemoteQMgrName
          pcf_type: MQCFST
          type_hint: str
        - name: RemoteQName
          pcf_type: MQCFST
          type_hint: str
        - name: RetentionInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: Scope
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSCO_Q_MGR
            - MQSCO_CELL
        - name: Shareability
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQA_SHAREABLE
            - MQQA_NOT_SHAREABLE
        - name: StorageClass
          pcf_type: MQCFST
          type_hint: str
        - name: StreamQ
          pcf_type: MQCFST
          type_hint: str
        - name: StreamQService
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQST_BEST_EFFORT
            - MQST_MUST_DUP
        - name: TpipeNames
          pcf_type: MQCFSL
          type_hint: str
        - name: TriggerControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQTC_OFF
            - MQTC_ON
        - name: TriggerData
          pcf_type: MQCFST
          type_hint: str
        - name: TriggerDepth
          pcf_type: MQCFIN
          type_hint: int
        - name: TriggerMsgPriority
          pcf_type: MQCFIN
          type_hint: int
        - name: TriggerType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQTT_NONE
            - MQTT_FIRST
            - MQTT_EVERY
            - MQTT_DEPTH
        - name: Usage
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQUS_NORMAL
            - MQUS_TRANSMISSION
        - name: XmitQName
          pcf_type: MQCFST
          type_hint: str
    mapping:
      request:
        suggested:
          {}
        ambiguous:
          CLUSINFO:
            - ClusterInfo
          TYPE:
            - QType
        unmapped:
          - ALL
          - CLUSNL
          - CLUSTER
          - CMDSCOPE
          - COPY
          - EQ
          - GE
          - GROUP
          - GT
          - LE
          - LIVE
          - LK
          - LT
          - NE
          - NL
          - PRIVATE
          - PSID
          - QALIAS
          - QLOCAL
          - QMGR
          - QMODEL
          - QREMOTE
          - QSGDISP
          - SHARED
          - STGCLASS
          - TARGTYPE
          - WHERE
        pcf_unmapped:
          - CFStructure
          - CapExpiry
          - ClusterInfo
          - ClusterName
          - ClusterNamelist
          - CommandScope
          - IntegerFilterCommand
          - PageSetID
          - QAttrs
          - QName
          - QSGDisposition
          - QType
          - StorageClass
          - StringFilterCommand
      response:
        suggested:
          CAPEXPRY: CapExpiry
          CLWLUSEQ: CLWLUseQ
          CUSTOM: Custom
          DEFBIND: DefBind
          INDXTYPE: IndexType
          MAXDEPTH: MaxQDepth
          OTELTRAC: OTELTrace
          QTYPE: QType
          SCOPE: Scope
          STREAMQ: StreamQ
          USAGE: Usage
        ambiguous:
          BOQNAME:
            - QName
            - BaseQName
          CFSTRUCT:
            - CFStructure
          CLUSDATE:
            - ClusterDate
          CLUSTIME:
            - ClusterTime
          QSVCINT:
            - QServiceInterval
          RNAME:
            - QName
          RQMNAME:
            - QName
          TRIGDATA:
            - TriggerData
          TRIGTYPE:
            - TriggerType
        unmapped:
          - ACCTQ
          - ALL
          - ALTDATE
          - ALTTIME
          - BOTHRESH
          - CLCHNAME
          - CLUSNL
          - CLUSQMGR
          - CLUSQT
          - CLUSTER
          - CLWLPRTY
          - CLWLRANK
          - COMPAT
          - CRDATE
          - CRTIME
          - CURDEPTH
          - DEFPRESP
          - DEFPRTY
          - DEFPSIST
          - DEFREADA
          - DEFSOPT
          - DEFTYPE
          - DESCR
          - DISTL
          - FORCE
          - GET
          - HARDENBO
          - IMGRCOVQ
          - INITQ
          - IPPROCS
          - MAXFSIZE
          - MAXMSGL
          - MONQ
          - MSGDLVSQ
          - NONE
          - NPMCLASS
          - OPPROCS
          - OTELPCTL
          - PROCESS
          - PROPCTL
          - PSID
          - PUT
          - QALIAS
          - QDEPTHHI
          - QDEPTHLO
          - QDPHIEV
          - QDPLOEV
          - QDPMAXEV
          - QLOCAL
          - QMGR
          - QMID
          - QREMOTE
          - QSGDISP
          - QSVCIEV
          - RETINTVL
          - SHARE
          - STATQ
          - STGCLASS
          - STRMQOS
          - TARGET
          - TARGTYPE
          - TPIPE
          - TRIGDPTH
          - TRIGGER
          - TRIGMPRI
          - XMITQ
        pcf_unmapped:
          - AlterationDate
          - AlterationTime
          - BackoutRequeueName
          - BackoutThreshold
          - BaseQName
          - CFStructure
          - CLWLQueuePriority
          - CLWLQueueRank
          - ClusterChannelName
          - ClusterDate
          - ClusterName
          - ClusterNamelist
          - ClusterQType
          - ClusterTime
          - CreationDate
          - CreationTime
          - CurrentQDepth
          - DefInputOpenOption
          - DefPersistence
          - DefPriority
          - DefReadAhead
          - DefaultPutResponse
          - DefinitionType
          - DistLists
          - HardenGetBackout
          - ImageRecoverQueue
          - InhibitGet
          - InhibitPut
          - InitiationQName
          - MaxMsgLength
          - MsgDeliverySequence
          - NonPersistentMessageClass
          - OTELPropagationControl
          - OpenInputCount
          - OpenOutputCount
          - PageSetID
          - ProcessName
          - PropertyControl
          - QDepthHighEvent
          - QDepthHighLimit
          - QDepthLowEvent
          - QDepthLowLimit
          - QDepthMaxEvent
          - QDesc
          - QMgrIdentifier
          - QMgrName
          - QName
          - QSGDisposition
          - QServiceInterval
          - QServiceIntervalEvent
          - QueueAccounting
          - QueueMonitoring
          - QueueStatistics
          - RemoteQMgrName
          - RemoteQName
          - RetentionInterval
          - Shareability
          - StorageClass
          - StreamQService
          - TpipeNames
          - TriggerControl
          - TriggerData
          - TriggerDepth
          - TriggerMsgPriority
          - TriggerType
          - XmitQName
    notes:
      - display-parameter-descriptions-treated-as-input
      - display-requested-parameters-table
  - mqsc:
      name: MOVE QLOCAL
      href: SSFKSJ_9.4.0/refadmin/q086420_.html
      positional_parameters:
        - qmgr-name
        - source
        - target
      input_parameters: []
      output_parameters: []
      section_sources:
        {}
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
        unmapped: []
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
      name: RESET QSTATS
      href: SSFKSJ_9.4.0/refadmin/q086540_.html
      positional_parameters:
        - generic-qname
        - qmgr-name
      input_parameters: []
      output_parameters: []
      section_sources:
        {}
    pcf:
      command: MQCMD_RESET_Q_STATS
      request_href: SSFKSJ_9.4.0/refadmin/q088300_.html
      response_href: SSFKSJ_9.4.0/refadmin/q088310_.html
      request_parameters:
        - name: QName
          pcf_type: MQCFST
          type_hint: str
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
          enum_values:
            - MQRCCF_Q_WRONG_TYPE
            - MQRCCF_EVENTS_DISABLED
      response_parameters:
        - name: HighQDepth
          pcf_type: MQCFIN
          type_hint: int
        - name: MsgDeqCount
          pcf_type: MQCFIN
          type_hint: int
        - name: MsgEnqCount
          pcf_type: MQCFIN
          type_hint: int
        - name: QName
          pcf_type: MQCFST
          type_hint: str
        - name: QSGDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSGD_COPY
            - MQQSGD_SHARED
            - MQQSGD_Q_MGR
        - name: TimeSinceReset
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
          - QName
      response:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - HighQDepth
          - MsgDeqCount
          - MsgEnqCount
          - QName
          - QSGDisposition
          - TimeSinceReset
    notes: []
```

## Queue command re-parse

This addendum isolates corrected MQSC and PCF parameter sets. It is intentionally separate from the first-run extraction above and omits mapping heuristics.

```yaml
version: 1
generated_at: 2026-01-12T23:10:00Z
commands:
  - mqsc:
      name: ALTER QLOCAL
      href: SSFKSJ_9.4.0/refadmin/q085330_.html
      positional_parameters:
        - (queue-name)
      input_parameters:
        - ACCTQ
        - BOQNAME
        - BOTHRESH
        - CAPEXPRY
        - CFSTRUCT
        - CLCHNAME
        - CLUSNL
        - CLUSTER
        - CLWLPRTY
        - CLWLRANK
        - CLWLUSEQ
        - CMDSCOPE
        - CUSTOM
        - DEFBIND
        - DEFPRESP
        - DEFPRTY
        - DEFPSIST
        - DEFREADA
        - DEFSOPT
        - DEFTYPE
        - DESCR
        - DISTL
        - FORCE
        - GET
        - HARDENBO
        - NOHARDENBO
        - IMGRCOVQ
        - INDXTYPE
        - INITQ
        - LIKE
        - MAXDEPTH
        - MAXFSIZE
        - MAXMSGL
        - MONQ
        - MSGDLVSQ
        - NPMCLASS
        - OTELPCTL
        - OTELTRAC
        - PROCESS
        - PROPCTL
        - PUT
        - QDEPTHHI
        - QDEPTHLO
        - QDPHIEV
        - QDPLOEV
        - QDPMAXEV
        - QSGDISP
        - QSVCIEV
        - QSVCINT
        - RETINTVL
        - SCOPE
        - SHARE
        - NOSHARE
        - STATQ
        - STGCLASS
        - STREAMQ
        - STRMQOS
        - TRIGDATA
        - TRIGDPTH
        - TRIGGER
        - NOTRIGGER
        - TRIGMPRI
        - TRIGTYPE
        - USAGE
      output_parameters:
        []
      section_sources:
        Parameter descriptions for ALTER queues:
          - ACCTQ
          - BOQNAME
          - BOTHRESH
          - CAPEXPRY
          - CFSTRUCT
          - CLCHNAME
          - CLUSNL
          - CLUSTER
          - CLWLPRTY
          - CLWLRANK
          - CLWLUSEQ
          - CMDSCOPE
          - CUSTOM
          - DEFBIND
          - DEFPRESP
          - DEFPRTY
          - DEFPSIST
          - DEFREADA
          - DEFSOPT
          - DEFTYPE
          - DESCR
          - DISTL
          - FORCE
          - GET
          - HARDENBO
          - NOHARDENBO
          - IMGRCOVQ
          - INDXTYPE
          - INITQ
          - LIKE
          - MAXDEPTH
          - MAXFSIZE
          - MAXMSGL
          - MONQ
          - MSGDLVSQ
          - NPMCLASS
          - OTELPCTL
          - OTELTRAC
          - PROCESS
          - PROPCTL
          - PUT
          - QDEPTHHI
          - QDEPTHLO
          - QDPHIEV
          - QDPLOEV
          - QDPMAXEV
          - QSGDISP
          - QSVCIEV
          - QSVCINT
          - RETINTVL
          - SCOPE
          - SHARE
          - NOSHARE
          - STATQ
          - STGCLASS
          - STREAMQ
          - STRMQOS
          - TRIGDATA
          - TRIGDPTH
          - TRIGGER
          - NOTRIGGER
          - TRIGMPRI
          - TRIGTYPE
          - USAGE
    pcf:
      command: MQCMD_CHANGE_Q
      request_href: SSFKSJ_9.4.0/refadmin/q086990_.html
      response_href: null
      request_parameters:
        - name: QName
          pcf_type: MQCFST
          type_hint: str
        - name: QType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQT_ALIAS
            - MQQT_LOCAL
            - MQQT_REMOTE
            - MQQT_MODEL
        - name: BackoutRequeueName
          pcf_type: MQCFST
          type_hint: str
        - name: BackoutThreshold
          pcf_type: MQCFIN
          type_hint: int
        - name: BaseObjectName
          pcf_type: MQCFST
          type_hint: str
        - name: BaseQName
          pcf_type: MQCFST
          type_hint: str
        - name: CapExpiry
          pcf_type: MQCFIN
          type_hint: int
        - name: CFStructure
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterChannelName
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterName
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterNamelist
          pcf_type: MQCFST
          type_hint: str
        - name: CLWLQueuePriority
          pcf_type: MQCFIN
          type_hint: int
        - name: CLWLQueueRank
          pcf_type: MQCFIN
          type_hint: int
        - name: CLWLUseQ
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCLWL_USEQ_AS_Q_MGR
            - MQCLWL_USEQ_ANY
            - MQCLWL_USEQ_LOCAL
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: Custom
          pcf_type: MQCFST
          type_hint: str
        - name: DefaultPutResponse
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPRT_SYNC_RESPONSE
            - MQPRT_ASYNC_RESPONSE
        - name: DefBind
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQBND_BIND_ON_OPEN
            - MQBND_BIND_NOT_FIXED
            - MQBND_BIND_ON_GROUP
        - name: DefinitionType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQDT_PERMANENT_DYNAMIC
            - MQQDT_SHARED_DYNAMIC
            - MQQDT_TEMPORARY_DYNAMIC
        - name: DefInputOpenOption
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQOO_INPUT_EXCLUSIVE
            - MQOO_INPUT_SHARED
        - name: DefPersistence
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPER_PERSISTENT
            - MQPER_NOT_PERSISTENT
        - name: DefPriority
          pcf_type: MQCFIN
          type_hint: int
        - name: DefReadAhead
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQREADA_NO
            - MQREADA_YES
            - MQREADA_DISABLED
        - name: DistLists
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQDL_SUPPORTED
            - MQDL_NOT_SUPPORTED
        - name: Force
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQFC_YES
            - MQFC_NO
        - name: HardenGetBackout
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQA_BACKOUT_HARDENED
            - MQQA_BACKOUT_NOT_HARDENED
        - name: ImageRecoverQueue
          pcf_type: MQCFST
          type_hint: str
          enum_values:
            - MQIMGRCOV_YES
            - MQIMGRCOV_NO
            - MQIMGRCOV_AS_Q_MGR
        - name: IndexType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQIT_NONE
            - MQIT_MSG_ID
            - MQIT_CORREL_ID
            - MQIT_MSG_TOKEN
            - MQIT_GROUP_ID
        - name: InhibitGet
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQA_GET_ALLOWED
            - MQQA_GET_INHIBITED
        - name: InhibitPut
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQA_PUT_ALLOWED
            - MQQA_PUT_INHIBITED
        - name: InitiationQName
          pcf_type: MQCFST
          type_hint: str
        - name: MaxMsgLength
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxQDepth
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxQFileSize
          pcf_type: MQCFIN
          type_hint: int
        - name: MsgDeliverySequence
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMDS_PRIORITY
            - MQMDS_FIFO
        - name: NonPersistentMessageClass
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQNPM_CLASS_NORMAL
            - MQNPM_CLASS_HIGH
        - name: OTELPropagationControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQOTEL_PCTL_QMGR
            - MQOTEL_PCTL_MANUAL
            - MQOTEL_PCTL_AUTO
        - name: OTELTrace
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQOTEL_TRACE_QMGR
            - MQOTEL_TRACE_OFF
            - MQOTEL_TRACE_ON
        - name: ProcessName
          pcf_type: MQCFST
          type_hint: str
        - name: PropertyControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPROP_COMPATIBILITY
            - MQPROP_NONE
            - MQPROP_ALL
            - MQPROP_FORCE_MQRFH2
            - MQPROP_V6COMPAT
        - name: QDepthHighEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
        - name: QDepthHighLimit
          pcf_type: MQCFIN
          type_hint: int
        - name: QDepthLowEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
        - name: QDepthLowLimit
          pcf_type: MQCFIN
          type_hint: int
        - name: QDepthMaxEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
        - name: QDesc
          pcf_type: MQCFST
          type_hint: str
        - name: QServiceInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: QServiceIntervalEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSIE_HIGH
            - MQQSIE_OK
            - MQQSIE_NONE
        - name: QSGDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSGD_COPY
            - MQQSGD_Q_MGR
            - MQQSGD_GROUP
            - MQQSGD_PRIVATE
            - MQQSGD_SHARED
        - name: QueueAccounting
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_Q_MGR
            - MQMON_OFF
            - MQMON_ON
        - name: QueueMonitoring
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_OFF
            - MQMON_Q_MGR
            - MQMON_LOW
            - MQMON_MEDIUM
            - MQMON_HIGH
        - name: QueueStatistics
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_Q_MGR
            - MQMON_OFF
            - MQMON_ON
        - name: RemoteQMgrName
          pcf_type: MQCFST
          type_hint: str
        - name: RemoteQName
          pcf_type: MQCFST
          type_hint: str
        - name: RetentionInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: Scope
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSCO_Q_MGR
            - MQSCO_CELL
        - name: Shareability
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQA_SHAREABLE
            - MQQA_NOT_SHAREABLE
        - name: StorageClass
          pcf_type: MQCFST
          type_hint: str
        - name: StreamQ
          pcf_type: MQCFST
          type_hint: str
        - name: StreamQService
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQST_BEST_EFFORT
            - MQST_MUST_DUP
        - name: TargetType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQOT_Q
            - MQOT_TOPIC
        - name: TriggerControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQTC_OFF
            - MQTC_ON
        - name: TriggerData
          pcf_type: MQCFST
          type_hint: str
        - name: TriggerDepth
          pcf_type: MQCFIN
          type_hint: int
        - name: TriggerMsgPriority
          pcf_type: MQCFIN
          type_hint: int
        - name: TriggerType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQTT_NONE
            - MQTT_EVERY
            - MQTT_FIRST
            - MQTT_DEPTH
        - name: Usage
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQUS_NORMAL
            - MQUS_TRANSMISSION
        - name: XmitQName
          pcf_type: MQCFST
          type_hint: str
      response_parameters:
        []
    notes:
      - change-queue-excludes-copy-only-parameters
      - change-queue-excludes-replace-parameter
  - mqsc:
      name: DEFINE QLOCAL
      href: SSFKSJ_9.4.0/refadmin/q085690_.html
      positional_parameters:
        - (queue-name)
      input_parameters:
        - ACCTQ
        - BOQNAME
        - BOTHRESH
        - CAPEXPRY
        - CFSTRUCT
        - CLCHNAME
        - CLUSNL
        - CLUSTER
        - CLWLPRTY
        - CLWLRANK
        - CLWLUSEQ
        - CMDSCOPE
        - CUSTOM
        - DEFBIND
        - DEFPRESP
        - DEFPRTY
        - DEFPSIST
        - DEFREADA
        - DEFSOPT
        - DESCR
        - DISTL
        - FORCE
        - GET
        - HARDENBO
        - NOHARDENBO
        - IMGRCOVQ
        - INDXTYPE
        - INITQ
        - LIKE
        - MAXDEPTH
        - MAXFSIZE
        - MAXMSGL
        - MONQ
        - MSGDLVSQ
        - NOREPLACE
        - NPMCLASS
        - OTELPCTL
        - OTELTRAC
        - PROCESS
        - PROPCTL
        - PUT
        - QDEPTHHI
        - QDEPTHLO
        - QDPHIEV
        - QDPLOEV
        - QDPMAXEV
        - QSGDISP
        - QSVCIEV
        - QSVCINT
        - REPLACE
        - RETINTVL
        - SCOPE
        - SHARE
        - NOSHARE
        - STATQ
        - STGCLASS
        - STREAMQ
        - STRMQOS
        - TRIGDATA
        - TRIGDPTH
        - TRIGGER
        - NOTRIGGER
        - TRIGMPRI
        - TRIGTYPE
        - USAGE
      output_parameters:
        []
      section_sources:
        Parameter descriptions for DEFINE queues:
          - ACCTQ
          - BOQNAME
          - BOTHRESH
          - CAPEXPRY
          - CFSTRUCT
          - CLCHNAME
          - CLUSNL
          - CLUSTER
          - CLWLPRTY
          - CLWLRANK
          - CLWLUSEQ
          - CMDSCOPE
          - CUSTOM
          - DEFBIND
          - DEFPRESP
          - DEFPRTY
          - DEFPSIST
          - DEFREADA
          - DEFSOPT
          - DESCR
          - DISTL
          - FORCE
          - GET
          - HARDENBO
          - NOHARDENBO
          - IMGRCOVQ
          - INDXTYPE
          - INITQ
          - LIKE
          - MAXDEPTH
          - MAXFSIZE
          - MAXMSGL
          - MONQ
          - MSGDLVSQ
          - NOREPLACE
          - NPMCLASS
          - OTELPCTL
          - OTELTRAC
          - PROCESS
          - PROPCTL
          - PUT
          - QDEPTHHI
          - QDEPTHLO
          - QDPHIEV
          - QDPLOEV
          - QDPMAXEV
          - QSGDISP
          - QSVCIEV
          - QSVCINT
          - REPLACE
          - RETINTVL
          - SCOPE
          - SHARE
          - NOSHARE
          - STATQ
          - STGCLASS
          - STREAMQ
          - STRMQOS
          - TRIGDATA
          - TRIGDPTH
          - TRIGGER
          - NOTRIGGER
          - TRIGMPRI
          - TRIGTYPE
          - USAGE
    pcf:
      command: MQCMD_CREATE_Q
      request_href: SSFKSJ_9.4.0/refadmin/q086990_.html
      response_href: null
      request_parameters:
        - name: QName
          pcf_type: MQCFST
          type_hint: str
        - name: QType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQT_ALIAS
            - MQQT_LOCAL
            - MQQT_REMOTE
            - MQQT_MODEL
        - name: BackoutRequeueName
          pcf_type: MQCFST
          type_hint: str
        - name: BackoutThreshold
          pcf_type: MQCFIN
          type_hint: int
        - name: BaseObjectName
          pcf_type: MQCFST
          type_hint: str
        - name: BaseQName
          pcf_type: MQCFST
          type_hint: str
        - name: CapExpiry
          pcf_type: MQCFIN
          type_hint: int
        - name: CFStructure
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterChannelName
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterName
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterNamelist
          pcf_type: MQCFST
          type_hint: str
        - name: CLWLQueuePriority
          pcf_type: MQCFIN
          type_hint: int
        - name: CLWLQueueRank
          pcf_type: MQCFIN
          type_hint: int
        - name: CLWLUseQ
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCLWL_USEQ_AS_Q_MGR
            - MQCLWL_USEQ_ANY
            - MQCLWL_USEQ_LOCAL
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: Custom
          pcf_type: MQCFST
          type_hint: str
        - name: DefaultPutResponse
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPRT_SYNC_RESPONSE
            - MQPRT_ASYNC_RESPONSE
        - name: DefBind
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQBND_BIND_ON_OPEN
            - MQBND_BIND_NOT_FIXED
            - MQBND_BIND_ON_GROUP
        - name: DefinitionType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQDT_PERMANENT_DYNAMIC
            - MQQDT_SHARED_DYNAMIC
            - MQQDT_TEMPORARY_DYNAMIC
        - name: DefInputOpenOption
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQOO_INPUT_EXCLUSIVE
            - MQOO_INPUT_SHARED
        - name: DefPersistence
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPER_PERSISTENT
            - MQPER_NOT_PERSISTENT
        - name: DefPriority
          pcf_type: MQCFIN
          type_hint: int
        - name: DefReadAhead
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQREADA_NO
            - MQREADA_YES
            - MQREADA_DISABLED
        - name: DistLists
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQDL_SUPPORTED
            - MQDL_NOT_SUPPORTED
        - name: Force
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQFC_YES
            - MQFC_NO
        - name: HardenGetBackout
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQA_BACKOUT_HARDENED
            - MQQA_BACKOUT_NOT_HARDENED
        - name: ImageRecoverQueue
          pcf_type: MQCFST
          type_hint: str
          enum_values:
            - MQIMGRCOV_YES
            - MQIMGRCOV_NO
            - MQIMGRCOV_AS_Q_MGR
        - name: IndexType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQIT_NONE
            - MQIT_MSG_ID
            - MQIT_CORREL_ID
            - MQIT_MSG_TOKEN
            - MQIT_GROUP_ID
        - name: InhibitGet
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQA_GET_ALLOWED
            - MQQA_GET_INHIBITED
        - name: InhibitPut
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQA_PUT_ALLOWED
            - MQQA_PUT_INHIBITED
        - name: InitiationQName
          pcf_type: MQCFST
          type_hint: str
        - name: MaxMsgLength
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxQDepth
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxQFileSize
          pcf_type: MQCFIN
          type_hint: int
        - name: MsgDeliverySequence
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMDS_PRIORITY
            - MQMDS_FIFO
        - name: NonPersistentMessageClass
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQNPM_CLASS_NORMAL
            - MQNPM_CLASS_HIGH
        - name: OTELPropagationControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQOTEL_PCTL_QMGR
            - MQOTEL_PCTL_MANUAL
            - MQOTEL_PCTL_AUTO
        - name: OTELTrace
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQOTEL_TRACE_QMGR
            - MQOTEL_TRACE_OFF
            - MQOTEL_TRACE_ON
        - name: ProcessName
          pcf_type: MQCFST
          type_hint: str
        - name: PropertyControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPROP_COMPATIBILITY
            - MQPROP_NONE
            - MQPROP_ALL
            - MQPROP_FORCE_MQRFH2
            - MQPROP_V6COMPAT
        - name: QDepthHighEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
        - name: QDepthHighLimit
          pcf_type: MQCFIN
          type_hint: int
        - name: QDepthLowEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
        - name: QDepthLowLimit
          pcf_type: MQCFIN
          type_hint: int
        - name: QDepthMaxEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
        - name: QDesc
          pcf_type: MQCFST
          type_hint: str
        - name: QServiceInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: QServiceIntervalEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSIE_HIGH
            - MQQSIE_OK
            - MQQSIE_NONE
        - name: QSGDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSGD_COPY
            - MQQSGD_Q_MGR
            - MQQSGD_GROUP
            - MQQSGD_PRIVATE
            - MQQSGD_SHARED
        - name: QueueAccounting
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_Q_MGR
            - MQMON_OFF
            - MQMON_ON
        - name: QueueMonitoring
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_OFF
            - MQMON_Q_MGR
            - MQMON_LOW
            - MQMON_MEDIUM
            - MQMON_HIGH
        - name: QueueStatistics
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_Q_MGR
            - MQMON_OFF
            - MQMON_ON
        - name: RemoteQMgrName
          pcf_type: MQCFST
          type_hint: str
        - name: RemoteQName
          pcf_type: MQCFST
          type_hint: str
        - name: Replace
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQRP_YES
            - MQRP_NO
        - name: RetentionInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: Scope
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSCO_Q_MGR
            - MQSCO_CELL
        - name: Shareability
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQA_SHAREABLE
            - MQQA_NOT_SHAREABLE
        - name: StorageClass
          pcf_type: MQCFST
          type_hint: str
        - name: StreamQ
          pcf_type: MQCFST
          type_hint: str
        - name: StreamQService
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQST_BEST_EFFORT
            - MQST_MUST_DUP
        - name: TargetType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQOT_Q
            - MQOT_TOPIC
        - name: TriggerControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQTC_OFF
            - MQTC_ON
        - name: TriggerData
          pcf_type: MQCFST
          type_hint: str
        - name: TriggerDepth
          pcf_type: MQCFIN
          type_hint: int
        - name: TriggerMsgPriority
          pcf_type: MQCFIN
          type_hint: int
        - name: TriggerType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQTT_NONE
            - MQTT_EVERY
            - MQTT_FIRST
            - MQTT_DEPTH
        - name: Usage
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQUS_NORMAL
            - MQUS_TRANSMISSION
        - name: XmitQName
          pcf_type: MQCFST
          type_hint: str
      response_parameters:
        []
    notes:
      - create-queue-excludes-copy-only-parameters
  - mqsc:
      name: DELETE QLOCAL
      href: SSFKSJ_9.4.0/refadmin/q085890_.html
      positional_parameters:
        - (q-name)
      input_parameters:
        - AUTHREC
        - CMDSCOPE
        - IGNSTATE
        - QSGDISP
        - PURGE
        - NOPURGE
      output_parameters:
        []
      section_sources:
        Parameter descriptions for DELETE queues:
          - AUTHREC
          - CMDSCOPE
          - IGNSTATE
          - QSGDISP
          - PURGE
          - NOPURGE
    pcf:
      command: MQCMD_DELETE_Q
      request_href: SSFKSJ_9.4.0/refadmin/q087180_.html
      response_href: SSFKSJ_9.4.0/refadmin/q087180_.html
      request_parameters:
        - name: QName
          pcf_type: MQCFST
          type_hint: str
        - name: Authrec
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQRAR_YES
            - MQRAR_NO
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: Purge
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPO_YES
            - MQPO_NO
        - name: QSGDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSGD_COPY
            - MQQSGD_GROUP
            - MQQSGD_Q_MGR
            - MQQSGD_SHARED
        - name: QType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQT_ALIAS
            - MQQT_LOCAL
            - MQQT_REMOTE
            - MQQT_MODEL
        - name: IgnoreState
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQIS_NO
            - MQIS_YES
      response_parameters:
        []
    notes:
      - ignore-state-type-inferred-from-mqsc-ignstate
      - ignore-state-name-normalized
  - mqsc:
      name: DISPLAY QLOCAL
      href: SSFKSJ_9.4.0/refadmin/q086270_.html
      positional_parameters:
        - (generic-qname)
      input_parameters:
        - WHERE
        - ALL
        - CFSTRUCT
        - CLUSINFO
        - CLUSNL
        - CLUSTER
        - CMDSCOPE
        - PSID
        - QSGDISP
        - STGCLASS
        - TARGTYPE
      output_parameters:
        - ACCTQ
        - ALTDATE
        - ALTTIME
        - BOQNAME
        - BOTHRESH
        - CAPEXPRY
        - CFSTRUCT
        - CLCHNAME
        - CLUSNL
        - CLUSTER
        - CLWLPRTY
        - CLWLRANK
        - CLWLUSEQ
        - CRDATE
        - CRTIME
        - CURDEPTH
        - CUSTOM
        - DEFBIND
        - DEFPRESP
        - DEFPRTY
        - DEFPSIST
        - DEFREADA
        - DEFSOPT
        - DEFTYPE
        - DESCR
        - DISTL
        - GET
        - HARDENBO
        - IMGRCOVQ
        - INDXTYPE
        - INITQ
        - IPPROCS
        - MAXDEPTH
        - MAXFSIZE
        - MAXMSGL
        - MONQ
        - MSGDLVSQ
        - NPMCLASS
        - OPPROCS
        - OTELPCTL
        - OTELTRAC
        - PROCESS
        - PROPCTL
        - PSID
        - PUT
        - QDEPTHHI
        - QDEPTHLO
        - QDPHIEV
        - QDPLOEV
        - QDPMAXEV
        - QSGDISP
        - QSVCIEV
        - QSVCINT
        - QTYPE
        - RETINTVL
        - SCOPE
        - SHARE
        - STATQ
        - STGCLASS
        - STREAMQ
        - STRMQOS
        - TPIPE
        - TRIGDATA
        - TRIGDPTH
        - TRIGGER
        - TRIGMPRI
        - TRIGTYPE
        - USAGE
      section_sources:
        Parameter descriptions for DISPLAY QUEUE:
          - WHERE
          - ALL
          - CFSTRUCT
          - CLUSINFO
          - CLUSNL
          - CLUSTER
          - CMDSCOPE
          - PSID
          - QSGDISP
          - STGCLASS
          - TARGTYPE
        Requested parameters:
          - ACCTQ
          - ALTDATE
          - ALTTIME
          - BOQNAME
          - BOTHRESH
          - CAPEXPRY
          - CFSTRUCT
          - CLCHNAME
          - CLUSNL
          - CLUSTER
          - CLWLPRTY
          - CLWLRANK
          - CLWLUSEQ
          - CRDATE
          - CRTIME
          - CURDEPTH
          - CUSTOM
          - DEFBIND
          - DEFPRESP
          - DEFPRTY
          - DEFPSIST
          - DEFREADA
          - DEFSOPT
          - DEFTYPE
          - DESCR
          - DISTL
          - GET
          - HARDENBO
          - IMGRCOVQ
          - INDXTYPE
          - INITQ
          - IPPROCS
          - MAXDEPTH
          - MAXFSIZE
          - MAXMSGL
          - MONQ
          - MSGDLVSQ
          - NPMCLASS
          - OPPROCS
          - OTELPCTL
          - OTELTRAC
          - PROCESS
          - PROPCTL
          - PSID
          - PUT
          - QDEPTHHI
          - QDEPTHLO
          - QDPHIEV
          - QDPLOEV
          - QDPMAXEV
          - QSGDISP
          - QSVCIEV
          - QSVCINT
          - QTYPE
          - RETINTVL
          - SCOPE
          - SHARE
          - STATQ
          - STGCLASS
          - STREAMQ
          - STRMQOS
          - TPIPE
          - TRIGDATA
          - TRIGDPTH
          - TRIGGER
          - TRIGMPRI
          - TRIGTYPE
          - USAGE
    pcf:
      command: MQCMD_INQUIRE_Q
      request_href: SSFKSJ_9.4.0/refadmin/q087800_.html
      response_href: SSFKSJ_9.4.0/refadmin/q087810_.html
      request_parameters:
        - name: QName
          pcf_type: MQCFST
          type_hint: str
        - name: CapExpiry
          pcf_type: MQCFIN
          type_hint: int
        - name: CFStructure
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterInfo
          pcf_type: MQCFIN
          type_hint: int
        - name: ClusterName
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterNamelist
          pcf_type: MQCFST
          type_hint: str
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: IntegerFilterCommand
          pcf_type: MQCFIF
          type_hint: null
        - name: PageSetID
          pcf_type: MQCFIN
          type_hint: int
        - name: QAttrs
          pcf_type: MQCFIL
          type_hint: int
          enum_values:
            - MQIACF_ALL
            - MQCA_ALTERATION_DATE
            - MQCA_ALTERATION_TIME
            - MQCA_BACKOUT_REQ_Q_NAME
            - MQCA_BASE_NAME
            - MQCA_CF_STRUC_NAME
            - MQCA_CLUS_CHL_NAME
            - MQCA_CLUSTER_DATE
            - MQCA_CLUSTER_NAME
            - MQCA_CLUSTER_NAMELIST
            - MQCA_CLUSTER_Q_MGR_NAME
            - MQCA_CLUSTER_TIME
            - MQCA_CREATION_DATE
            - MQCA_CREATION_TIME
            - MQCA_CUSTOM
            - MQCA_INITIATION_Q_NAME
            - MQCA_PROCESS_NAME
            - MQCA_Q_DESC
            - MQCA_Q_MGR_IDENTIFIER
            - MQCA_Q_NAME
            - MQCA_REMOTE_Q_MGR_NAME
            - MQCA_REMOTE_Q_NAME
            - MQCA_STORAGE_CLASS
            - MQCA_STREAM_QUEUE_NAME
            - MQCA_TPIPE_NAME
            - MQCA_TRIGGER_DATA
            - MQCA_XMIT_Q_NAME
            - MQIA_ACCOUNTING_Q
            - MQIA_BACKOUT_THRESHOLD
            - MQIA_BASE_TYPE
            - MQIA_CLUSTER_Q_TYPE
            - MQIA_CLWL_Q_PRIORITY
            - MQIA_CLWL_Q_RANK
            - MQIA_CLWL_USEQ
            - MQIA_CURRENT_Q_DEPTH
            - MQIA_DEF_BIND
            - MQIA_DEF_INPUT_OPEN_OPTION
            - MQIA_DEF_PERSISTENCE
            - MQIA_DEF_PRIORITY
            - MQIA_DEF_PUT_RESPONSE_TYPE
            - MQIA_DEF_READ_AHEAD
            - MQIA_DEFINITION_TYPE
            - MQIA_DIST_LISTS
            - MQIA_HARDEN_GET_BACKOUT
            - MQIA_INDEX_TYPE
            - MQIA_INHIBIT_GET
            - MQIA_INHIBIT_PUT
            - MQIA_MAX_MSG_LENGTH
            - MQIA_MAX_Q_DEPTH
            - MQIA_MEDIA_IMAGE_RECOVER_Q
            - MQIA_MONITORING_Q
            - MQIA_MSG_DELIVERY_SEQUENCE
            - MQIA_NPM_CLASS
            - MQIA_OPEN_INPUT_COUNT
            - MQIA_OPEN_OUTPUT_COUNT
            - MQIA_OTEL_PROPAGATION_CONTROL
            - MQIA_OTEL_TRACE
            - MQIA_PAGESET_ID
            - MQIA_PROPERTY_CONTROL
            - MQIA_Q_DEPTH_HIGH_EVENT
            - MQIA_Q_DEPTH_HIGH_LIMIT
            - MQIA_Q_DEPTH_LOW_EVENT
            - MQIA_Q_DEPTH_LOW_LIMIT
            - MQIA_Q_DEPTH_MAX_EVENT
            - MQIA_Q_SERVICE_INTERVAL
            - MQIA_Q_SERVICE_INTERVAL_EVENT
            - MQIA_Q_TYPE
            - MQIA_RETENTION_INTERVAL
            - MQIA_SCOPE
            - MQIA_SHAREABILITY
            - MQIA_STATISTICS_Q
            - MQIA_STREAM_QUEUE_QOS
            - MQIA_TRIGGER_CONTROL
            - MQIA_TRIGGER_DEPTH
            - MQIA_TRIGGER_MSG_PRIORITY
            - MQIA_TRIGGER_MTYPE
            - MQIA_USAGE
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
            - MQQSGD_SHARED
        - name: QType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQT_ALL
            - MQQT_LOCAL
            - MQQT_ALIAS
            - MQQT_REMOTE
            - MQQT_CLUSTER
            - MQQT_MODEL
        - name: StorageClass
          pcf_type: MQCFST
          type_hint: str
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
        - name: BackoutRequeueName
          pcf_type: MQCFST
          type_hint: str
        - name: BackoutThreshold
          pcf_type: MQCFIN
          type_hint: int
        - name: BaseQName
          pcf_type: MQCFST
          type_hint: str
        - name: CapExpiry
          pcf_type: MQCFIN
          type_hint: int
        - name: CFStructure
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterChannelName
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterDate
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterName
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterNamelist
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterQType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCQT_LOCAL_Q
            - MQCQT_ALIAS_Q
            - MQCQT_REMOTE_Q
            - MQCQT_Q_MGR_ALIAS
        - name: ClusterTime
          pcf_type: MQCFST
          type_hint: str
        - name: CLWLQueuePriority
          pcf_type: MQCFIN
          type_hint: int
        - name: CLWLQueueRank
          pcf_type: MQCFIN
          type_hint: int
        - name: CLWLUseQ
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCLWL_USEQ_AS_Q_MGR
            - MQCLWL_USEQ_ANY
            - MQCLWL_USEQ_LOCAL
        - name: CreationDate
          pcf_type: MQCFST
          type_hint: str
        - name: CreationTime
          pcf_type: MQCFST
          type_hint: str
        - name: CurrentQDepth
          pcf_type: MQCFIN
          type_hint: int
        - name: Custom
          pcf_type: MQCFST
          type_hint: str
        - name: DefaultPutResponse
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPRT_SYNC_RESPONSE
            - MQPRT_ASYNC_RESPONSE
        - name: DefBind
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQBND_BIND_ON_OPEN
            - MQBND_BIND_NOT_FIXED
            - MQBND_BIND_ON_GROUP
        - name: DefinitionType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQDT_PREDEFINED
            - MQQDT_PERMANENT_DYNAMIC
            - MQQDT_SHARED_DYNAMIC
            - MQQDT_TEMPORARY_DYNAMIC
        - name: DefInputOpenOption
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQOO_INPUT_EXCLUSIVE
            - MQOO_INPUT_SHARED
        - name: DefPersistence
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPER_PERSISTENT
            - MQPER_NOT_PERSISTENT
        - name: DefPriority
          pcf_type: MQCFIN
          type_hint: int
        - name: DefReadAhead
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQREADA_NO
            - MQREADA_YES
            - MQREADA_DISABLED
        - name: DistLists
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQDL_SUPPORTED
            - MQDL_NOT_SUPPORTED
        - name: HardenGetBackout
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQA_BACKOUT_HARDENED
            - MQQA_BACKOUT_NOT_HARDENED
        - name: ImageRecoverQueue
          pcf_type: MQCFST
          type_hint: str
          enum_values:
            - MQIMGRCOV_YES
            - MQIMGRCOV_NO
            - MQIMGRCOV_AS_Q_MGR
        - name: IndexType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQIT_NONE
            - MQIT_MSG_ID
            - MQIT_CORREL_ID
            - MQIT_MSG_TOKEN
            - MQIT_GROUP_ID
        - name: InhibitGet
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQA_GET_ALLOWED
            - MQQA_GET_INHIBITED
        - name: InhibitPut
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQA_PUT_ALLOWED
            - MQQA_PUT_INHIBITED
        - name: InitiationQName
          pcf_type: MQCFST
          type_hint: str
        - name: MaxMsgLength
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxQDepth
          pcf_type: MQCFIN
          type_hint: int
        - name: MsgDeliverySequence
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMDS_PRIORITY
            - MQMDS_FIFO
        - name: NonPersistentMessageClass
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQNPM_CLASS_NORMAL
            - MQNPM_CLASS_HIGH
        - name: OpenInputCount
          pcf_type: MQCFIN
          type_hint: int
        - name: OpenOutputCount
          pcf_type: MQCFIN
          type_hint: int
        - name: OTELPropagationControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQOTEL_PCTL_QMGR
            - MQOTEL_PCTL_MANUAL
            - MQOTEL_PCTL_AUTO
        - name: OTELTrace
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQOTEL_TRACE_QMGR
            - MQOTEL_TRACE_OFF
            - MQOTEL_TRACE_ON
        - name: PageSetID
          pcf_type: MQCFIN
          type_hint: int
        - name: ProcessName
          pcf_type: MQCFST
          type_hint: str
        - name: PropertyControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPROP_COMPATIBILITY
            - MQPROP_NONE
            - MQPROP_ALL
            - MQPROP_FORCE_MQRFH2
        - name: QDepthHighEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
        - name: QDepthHighLimit
          pcf_type: MQCFIN
          type_hint: int
        - name: QDepthLowEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
        - name: QDepthLowLimit
          pcf_type: MQCFIN
          type_hint: int
        - name: QDepthMaxEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
        - name: QDesc
          pcf_type: MQCFST
          type_hint: str
        - name: QMgrIdentifier
          pcf_type: MQCFST
          type_hint: str
        - name: QMgrName
          pcf_type: MQCFST
          type_hint: str
        - name: QName
          pcf_type: MQCFST
          type_hint: str
        - name: QServiceInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: QServiceIntervalEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSIE_HIGH
            - MQQSIE_OK
            - MQQSIE_NONE
        - name: QSGDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSGD_COPY
            - MQQSGD_GROUP
            - MQQSGD_Q_MGR
            - MQQSGD_SHARED
        - name: QType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQT_ALIAS
            - MQQT_CLUSTER
            - MQQT_LOCAL
            - MQQT_REMOTE
            - MQQT_MODEL
        - name: QueueAccounting
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_Q_MGR
            - MQMON_OFF
            - MQMON_ON
        - name: QueueMonitoring
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_OFF
            - MQMON_Q_MGR
            - MQMON_LOW
            - MQMON_MEDIUM
            - MQMON_HIGH
        - name: QueueStatistics
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_Q_MGR
            - MQMON_OFF
            - MQMON_ON
        - name: RemoteQMgrName
          pcf_type: MQCFST
          type_hint: str
        - name: RemoteQName
          pcf_type: MQCFST
          type_hint: str
        - name: RetentionInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: Scope
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSCO_Q_MGR
            - MQSCO_CELL
        - name: Shareability
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQA_SHAREABLE
            - MQQA_NOT_SHAREABLE
        - name: StorageClass
          pcf_type: MQCFST
          type_hint: str
        - name: StreamQ
          pcf_type: MQCFST
          type_hint: str
        - name: StreamQService
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQST_BEST_EFFORT
            - MQST_MUST_DUP
        - name: TpipeNames
          pcf_type: MQCFSL
          type_hint: str
        - name: TriggerControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQTC_OFF
            - MQTC_ON
        - name: TriggerData
          pcf_type: MQCFST
          type_hint: str
        - name: TriggerDepth
          pcf_type: MQCFIN
          type_hint: int
        - name: TriggerMsgPriority
          pcf_type: MQCFIN
          type_hint: int
        - name: TriggerType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQTT_NONE
            - MQTT_FIRST
            - MQTT_EVERY
            - MQTT_DEPTH
        - name: Usage
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQUS_NORMAL
            - MQUS_TRANSMISSION
        - name: XmitQName
          pcf_type: MQCFST
          type_hint: str
    notes:
      - display-queue-type-synonyms
      - qsgdisposition-returned-on-zos-only
  - mqsc:
      name: DISPLAY QUEUE
      href: SSFKSJ_9.4.0/refadmin/q086270_.html
      positional_parameters:
        - (generic-qname)
      input_parameters:
        - WHERE
        - ALL
        - CFSTRUCT
        - CLUSINFO
        - CLUSNL
        - CLUSTER
        - CMDSCOPE
        - PSID
        - QSGDISP
        - STGCLASS
        - TARGTYPE
        - TYPE
      output_parameters:
        - ACCTQ
        - ALTDATE
        - ALTTIME
        - BOQNAME
        - BOTHRESH
        - CAPEXPRY
        - CFSTRUCT
        - CLCHNAME
        - CLUSDATE
        - CLUSNL
        - CLUSQMGR
        - CLUSQT
        - CLUSTER
        - CLUSTIME
        - CLWLPRTY
        - CLWLRANK
        - CLWLUSEQ
        - CRDATE
        - CRTIME
        - CURDEPTH
        - CUSTOM
        - DEFBIND
        - DEFPRESP
        - DEFPRTY
        - DEFPSIST
        - DEFREADA
        - DEFSOPT
        - DEFTYPE
        - DESCR
        - DISTL
        - GET
        - HARDENBO
        - IMGRCOVQ
        - INDXTYPE
        - INITQ
        - IPPROCS
        - MAXDEPTH
        - MAXFSIZE
        - MAXMSGL
        - MONQ
        - MSGDLVSQ
        - NPMCLASS
        - OPPROCS
        - OTELPCTL
        - OTELTRAC
        - PROCESS
        - PROPCTL
        - PSID
        - PUT
        - QDEPTHHI
        - QDEPTHLO
        - QDPHIEV
        - QDPLOEV
        - QDPMAXEV
        - QMID
        - QSGDISP
        - QSVCIEV
        - QSVCINT
        - QTYPE
        - RETINTVL
        - RNAME
        - RQMNAME
        - SCOPE
        - SHARE
        - STATQ
        - STGCLASS
        - STREAMQ
        - STRMQOS
        - TARGET
        - TARGTYPE
        - TPIPE
        - TRIGDATA
        - TRIGDPTH
        - TRIGGER
        - TRIGMPRI
        - TRIGTYPE
        - USAGE
        - XMITQ
      section_sources:
        Parameter descriptions for DISPLAY QUEUE:
          - WHERE
          - ALL
          - CFSTRUCT
          - CLUSINFO
          - CLUSNL
          - CLUSTER
          - CMDSCOPE
          - PSID
          - QSGDISP
          - STGCLASS
          - TARGTYPE
          - TYPE
        Requested parameters:
          - ACCTQ
          - ALTDATE
          - ALTTIME
          - BOQNAME
          - BOTHRESH
          - CAPEXPRY
          - CFSTRUCT
          - CLCHNAME
          - CLUSDATE
          - CLUSNL
          - CLUSQMGR
          - CLUSQT
          - CLUSTER
          - CLUSTIME
          - CLWLPRTY
          - CLWLRANK
          - CLWLUSEQ
          - CRDATE
          - CRTIME
          - CURDEPTH
          - CUSTOM
          - DEFBIND
          - DEFPRESP
          - DEFPRTY
          - DEFPSIST
          - DEFREADA
          - DEFSOPT
          - DEFTYPE
          - DESCR
          - DISTL
          - GET
          - HARDENBO
          - IMGRCOVQ
          - INDXTYPE
          - INITQ
          - IPPROCS
          - MAXDEPTH
          - MAXFSIZE
          - MAXMSGL
          - MONQ
          - MSGDLVSQ
          - NPMCLASS
          - OPPROCS
          - OTELPCTL
          - OTELTRAC
          - PROCESS
          - PROPCTL
          - PSID
          - PUT
          - QDEPTHHI
          - QDEPTHLO
          - QDPHIEV
          - QDPLOEV
          - QDPMAXEV
          - QMID
          - QSGDISP
          - QSVCIEV
          - QSVCINT
          - QTYPE
          - RETINTVL
          - RNAME
          - RQMNAME
          - SCOPE
          - SHARE
          - STATQ
          - STGCLASS
          - STREAMQ
          - STRMQOS
          - TARGET
          - TARGTYPE
          - TPIPE
          - TRIGDATA
          - TRIGDPTH
          - TRIGGER
          - TRIGMPRI
          - TRIGTYPE
          - USAGE
          - XMITQ
    pcf:
      command: MQCMD_INQUIRE_Q
      request_href: SSFKSJ_9.4.0/refadmin/q087800_.html
      response_href: SSFKSJ_9.4.0/refadmin/q087810_.html
      request_parameters:
        - name: QName
          pcf_type: MQCFST
          type_hint: str
        - name: CapExpiry
          pcf_type: MQCFIN
          type_hint: int
        - name: CFStructure
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterInfo
          pcf_type: MQCFIN
          type_hint: int
        - name: ClusterName
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterNamelist
          pcf_type: MQCFST
          type_hint: str
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: IntegerFilterCommand
          pcf_type: MQCFIF
          type_hint: null
        - name: PageSetID
          pcf_type: MQCFIN
          type_hint: int
        - name: QAttrs
          pcf_type: MQCFIL
          type_hint: int
          enum_values:
            - MQIACF_ALL
            - MQCA_ALTERATION_DATE
            - MQCA_ALTERATION_TIME
            - MQCA_BACKOUT_REQ_Q_NAME
            - MQCA_BASE_NAME
            - MQCA_CF_STRUC_NAME
            - MQCA_CLUS_CHL_NAME
            - MQCA_CLUSTER_DATE
            - MQCA_CLUSTER_NAME
            - MQCA_CLUSTER_NAMELIST
            - MQCA_CLUSTER_Q_MGR_NAME
            - MQCA_CLUSTER_TIME
            - MQCA_CREATION_DATE
            - MQCA_CREATION_TIME
            - MQCA_CUSTOM
            - MQCA_INITIATION_Q_NAME
            - MQCA_PROCESS_NAME
            - MQCA_Q_DESC
            - MQCA_Q_MGR_IDENTIFIER
            - MQCA_Q_NAME
            - MQCA_REMOTE_Q_MGR_NAME
            - MQCA_REMOTE_Q_NAME
            - MQCA_STORAGE_CLASS
            - MQCA_STREAM_QUEUE_NAME
            - MQCA_TPIPE_NAME
            - MQCA_TRIGGER_DATA
            - MQCA_XMIT_Q_NAME
            - MQIA_ACCOUNTING_Q
            - MQIA_BACKOUT_THRESHOLD
            - MQIA_BASE_TYPE
            - MQIA_CLUSTER_Q_TYPE
            - MQIA_CLWL_Q_PRIORITY
            - MQIA_CLWL_Q_RANK
            - MQIA_CLWL_USEQ
            - MQIA_CURRENT_Q_DEPTH
            - MQIA_DEF_BIND
            - MQIA_DEF_INPUT_OPEN_OPTION
            - MQIA_DEF_PERSISTENCE
            - MQIA_DEF_PRIORITY
            - MQIA_DEF_PUT_RESPONSE_TYPE
            - MQIA_DEF_READ_AHEAD
            - MQIA_DEFINITION_TYPE
            - MQIA_DIST_LISTS
            - MQIA_HARDEN_GET_BACKOUT
            - MQIA_INDEX_TYPE
            - MQIA_INHIBIT_GET
            - MQIA_INHIBIT_PUT
            - MQIA_MAX_MSG_LENGTH
            - MQIA_MAX_Q_DEPTH
            - MQIA_MEDIA_IMAGE_RECOVER_Q
            - MQIA_MONITORING_Q
            - MQIA_MSG_DELIVERY_SEQUENCE
            - MQIA_NPM_CLASS
            - MQIA_OPEN_INPUT_COUNT
            - MQIA_OPEN_OUTPUT_COUNT
            - MQIA_OTEL_PROPAGATION_CONTROL
            - MQIA_OTEL_TRACE
            - MQIA_PAGESET_ID
            - MQIA_PROPERTY_CONTROL
            - MQIA_Q_DEPTH_HIGH_EVENT
            - MQIA_Q_DEPTH_HIGH_LIMIT
            - MQIA_Q_DEPTH_LOW_EVENT
            - MQIA_Q_DEPTH_LOW_LIMIT
            - MQIA_Q_DEPTH_MAX_EVENT
            - MQIA_Q_SERVICE_INTERVAL
            - MQIA_Q_SERVICE_INTERVAL_EVENT
            - MQIA_Q_TYPE
            - MQIA_RETENTION_INTERVAL
            - MQIA_SCOPE
            - MQIA_SHAREABILITY
            - MQIA_STATISTICS_Q
            - MQIA_STREAM_QUEUE_QOS
            - MQIA_TRIGGER_CONTROL
            - MQIA_TRIGGER_DEPTH
            - MQIA_TRIGGER_MSG_PRIORITY
            - MQIA_TRIGGER_MTYPE
            - MQIA_USAGE
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
            - MQQSGD_SHARED
        - name: QType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQT_ALL
            - MQQT_LOCAL
            - MQQT_ALIAS
            - MQQT_REMOTE
            - MQQT_CLUSTER
            - MQQT_MODEL
        - name: StorageClass
          pcf_type: MQCFST
          type_hint: str
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
        - name: BackoutRequeueName
          pcf_type: MQCFST
          type_hint: str
        - name: BackoutThreshold
          pcf_type: MQCFIN
          type_hint: int
        - name: BaseQName
          pcf_type: MQCFST
          type_hint: str
        - name: CapExpiry
          pcf_type: MQCFIN
          type_hint: int
        - name: CFStructure
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterChannelName
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterDate
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterName
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterNamelist
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterQType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCQT_LOCAL_Q
            - MQCQT_ALIAS_Q
            - MQCQT_REMOTE_Q
            - MQCQT_Q_MGR_ALIAS
        - name: ClusterTime
          pcf_type: MQCFST
          type_hint: str
        - name: CLWLQueuePriority
          pcf_type: MQCFIN
          type_hint: int
        - name: CLWLQueueRank
          pcf_type: MQCFIN
          type_hint: int
        - name: CLWLUseQ
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCLWL_USEQ_AS_Q_MGR
            - MQCLWL_USEQ_ANY
            - MQCLWL_USEQ_LOCAL
        - name: CreationDate
          pcf_type: MQCFST
          type_hint: str
        - name: CreationTime
          pcf_type: MQCFST
          type_hint: str
        - name: CurrentQDepth
          pcf_type: MQCFIN
          type_hint: int
        - name: Custom
          pcf_type: MQCFST
          type_hint: str
        - name: DefaultPutResponse
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPRT_SYNC_RESPONSE
            - MQPRT_ASYNC_RESPONSE
        - name: DefBind
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQBND_BIND_ON_OPEN
            - MQBND_BIND_NOT_FIXED
            - MQBND_BIND_ON_GROUP
        - name: DefinitionType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQDT_PREDEFINED
            - MQQDT_PERMANENT_DYNAMIC
            - MQQDT_SHARED_DYNAMIC
            - MQQDT_TEMPORARY_DYNAMIC
        - name: DefInputOpenOption
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQOO_INPUT_EXCLUSIVE
            - MQOO_INPUT_SHARED
        - name: DefPersistence
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPER_PERSISTENT
            - MQPER_NOT_PERSISTENT
        - name: DefPriority
          pcf_type: MQCFIN
          type_hint: int
        - name: DefReadAhead
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQREADA_NO
            - MQREADA_YES
            - MQREADA_DISABLED
        - name: DistLists
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQDL_SUPPORTED
            - MQDL_NOT_SUPPORTED
        - name: HardenGetBackout
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQA_BACKOUT_HARDENED
            - MQQA_BACKOUT_NOT_HARDENED
        - name: ImageRecoverQueue
          pcf_type: MQCFST
          type_hint: str
          enum_values:
            - MQIMGRCOV_YES
            - MQIMGRCOV_NO
            - MQIMGRCOV_AS_Q_MGR
        - name: IndexType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQIT_NONE
            - MQIT_MSG_ID
            - MQIT_CORREL_ID
            - MQIT_MSG_TOKEN
            - MQIT_GROUP_ID
        - name: InhibitGet
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQA_GET_ALLOWED
            - MQQA_GET_INHIBITED
        - name: InhibitPut
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQA_PUT_ALLOWED
            - MQQA_PUT_INHIBITED
        - name: InitiationQName
          pcf_type: MQCFST
          type_hint: str
        - name: MaxMsgLength
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxQDepth
          pcf_type: MQCFIN
          type_hint: int
        - name: MsgDeliverySequence
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMDS_PRIORITY
            - MQMDS_FIFO
        - name: NonPersistentMessageClass
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQNPM_CLASS_NORMAL
            - MQNPM_CLASS_HIGH
        - name: OpenInputCount
          pcf_type: MQCFIN
          type_hint: int
        - name: OpenOutputCount
          pcf_type: MQCFIN
          type_hint: int
        - name: OTELPropagationControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQOTEL_PCTL_QMGR
            - MQOTEL_PCTL_MANUAL
            - MQOTEL_PCTL_AUTO
        - name: OTELTrace
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQOTEL_TRACE_QMGR
            - MQOTEL_TRACE_OFF
            - MQOTEL_TRACE_ON
        - name: PageSetID
          pcf_type: MQCFIN
          type_hint: int
        - name: ProcessName
          pcf_type: MQCFST
          type_hint: str
        - name: PropertyControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPROP_COMPATIBILITY
            - MQPROP_NONE
            - MQPROP_ALL
            - MQPROP_FORCE_MQRFH2
        - name: QDepthHighEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
        - name: QDepthHighLimit
          pcf_type: MQCFIN
          type_hint: int
        - name: QDepthLowEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
        - name: QDepthLowLimit
          pcf_type: MQCFIN
          type_hint: int
        - name: QDepthMaxEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
        - name: QDesc
          pcf_type: MQCFST
          type_hint: str
        - name: QMgrIdentifier
          pcf_type: MQCFST
          type_hint: str
        - name: QMgrName
          pcf_type: MQCFST
          type_hint: str
        - name: QName
          pcf_type: MQCFST
          type_hint: str
        - name: QServiceInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: QServiceIntervalEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSIE_HIGH
            - MQQSIE_OK
            - MQQSIE_NONE
        - name: QSGDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSGD_COPY
            - MQQSGD_GROUP
            - MQQSGD_Q_MGR
            - MQQSGD_SHARED
        - name: QType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQT_ALIAS
            - MQQT_CLUSTER
            - MQQT_LOCAL
            - MQQT_REMOTE
            - MQQT_MODEL
        - name: QueueAccounting
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_Q_MGR
            - MQMON_OFF
            - MQMON_ON
        - name: QueueMonitoring
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_OFF
            - MQMON_Q_MGR
            - MQMON_LOW
            - MQMON_MEDIUM
            - MQMON_HIGH
        - name: QueueStatistics
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_Q_MGR
            - MQMON_OFF
            - MQMON_ON
        - name: RemoteQMgrName
          pcf_type: MQCFST
          type_hint: str
        - name: RemoteQName
          pcf_type: MQCFST
          type_hint: str
        - name: RetentionInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: Scope
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSCO_Q_MGR
            - MQSCO_CELL
        - name: Shareability
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQA_SHAREABLE
            - MQQA_NOT_SHAREABLE
        - name: StorageClass
          pcf_type: MQCFST
          type_hint: str
        - name: StreamQ
          pcf_type: MQCFST
          type_hint: str
        - name: StreamQService
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQST_BEST_EFFORT
            - MQST_MUST_DUP
        - name: TpipeNames
          pcf_type: MQCFSL
          type_hint: str
        - name: TriggerControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQTC_OFF
            - MQTC_ON
        - name: TriggerData
          pcf_type: MQCFST
          type_hint: str
        - name: TriggerDepth
          pcf_type: MQCFIN
          type_hint: int
        - name: TriggerMsgPriority
          pcf_type: MQCFIN
          type_hint: int
        - name: TriggerType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQTT_NONE
            - MQTT_FIRST
            - MQTT_EVERY
            - MQTT_DEPTH
        - name: Usage
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQUS_NORMAL
            - MQUS_TRANSMISSION
        - name: XmitQName
          pcf_type: MQCFST
          type_hint: str
    notes:
      - display-queue-type-synonyms
      - display-queue-qtype-synonym-on-multiplatforms
      - qsgdisposition-returned-on-zos-only
  - mqsc:
      name: ALTER QALIAS
      href: SSFKSJ_9.4.0/refadmin/q085330_.html
      positional_parameters:
        - (queue-name)
      input_parameters:
        - CAPEXPRY
        - CLUSNL
        - CLUSTER
        - CLWLPRTY
        - CLWLRANK
        - CMDSCOPE
        - CUSTOM
        - DEFBIND
        - DEFPRESP
        - DEFPRTY
        - DEFPSIST
        - DEFREADA
        - DESCR
        - FORCE
        - GET
        - LIKE
        - PROPCTL
        - PUT
        - QSGDISP
        - SCOPE
        - TARGET
        - TARGQ
        - TARGTYPE
      output_parameters:
        []
      section_sources:
        Parameter descriptions for ALTER queues:
          - CAPEXPRY
          - CLUSNL
          - CLUSTER
          - CLWLPRTY
          - CLWLRANK
          - CMDSCOPE
          - CUSTOM
          - DEFBIND
          - DEFPRESP
          - DEFPRTY
          - DEFPSIST
          - DEFREADA
          - DESCR
          - FORCE
          - GET
          - LIKE
          - PROPCTL
          - PUT
          - QSGDISP
          - SCOPE
          - TARGET
          - TARGQ
          - TARGTYPE
    pcf:
      command: MQCMD_CHANGE_Q
      request_href: SSFKSJ_9.4.0/refadmin/q086990_.html
      response_href: null
      request_parameters:
        - name: QName
          pcf_type: MQCFST
          type_hint: str
        - name: QType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQT_ALIAS
            - MQQT_LOCAL
            - MQQT_REMOTE
            - MQQT_MODEL
        - name: BackoutRequeueName
          pcf_type: MQCFST
          type_hint: str
        - name: BackoutThreshold
          pcf_type: MQCFIN
          type_hint: int
        - name: BaseObjectName
          pcf_type: MQCFST
          type_hint: str
        - name: BaseQName
          pcf_type: MQCFST
          type_hint: str
        - name: CapExpiry
          pcf_type: MQCFIN
          type_hint: int
        - name: CFStructure
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterChannelName
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterName
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterNamelist
          pcf_type: MQCFST
          type_hint: str
        - name: CLWLQueuePriority
          pcf_type: MQCFIN
          type_hint: int
        - name: CLWLQueueRank
          pcf_type: MQCFIN
          type_hint: int
        - name: CLWLUseQ
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCLWL_USEQ_AS_Q_MGR
            - MQCLWL_USEQ_ANY
            - MQCLWL_USEQ_LOCAL
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: Custom
          pcf_type: MQCFST
          type_hint: str
        - name: DefaultPutResponse
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPRT_SYNC_RESPONSE
            - MQPRT_ASYNC_RESPONSE
        - name: DefBind
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQBND_BIND_ON_OPEN
            - MQBND_BIND_NOT_FIXED
            - MQBND_BIND_ON_GROUP
        - name: DefinitionType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQDT_PERMANENT_DYNAMIC
            - MQQDT_SHARED_DYNAMIC
            - MQQDT_TEMPORARY_DYNAMIC
        - name: DefInputOpenOption
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQOO_INPUT_EXCLUSIVE
            - MQOO_INPUT_SHARED
        - name: DefPersistence
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPER_PERSISTENT
            - MQPER_NOT_PERSISTENT
        - name: DefPriority
          pcf_type: MQCFIN
          type_hint: int
        - name: DefReadAhead
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQREADA_NO
            - MQREADA_YES
            - MQREADA_DISABLED
        - name: DistLists
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQDL_SUPPORTED
            - MQDL_NOT_SUPPORTED
        - name: Force
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQFC_YES
            - MQFC_NO
        - name: HardenGetBackout
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQA_BACKOUT_HARDENED
            - MQQA_BACKOUT_NOT_HARDENED
        - name: ImageRecoverQueue
          pcf_type: MQCFST
          type_hint: str
          enum_values:
            - MQIMGRCOV_YES
            - MQIMGRCOV_NO
            - MQIMGRCOV_AS_Q_MGR
        - name: IndexType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQIT_NONE
            - MQIT_MSG_ID
            - MQIT_CORREL_ID
            - MQIT_MSG_TOKEN
            - MQIT_GROUP_ID
        - name: InhibitGet
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQA_GET_ALLOWED
            - MQQA_GET_INHIBITED
        - name: InhibitPut
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQA_PUT_ALLOWED
            - MQQA_PUT_INHIBITED
        - name: InitiationQName
          pcf_type: MQCFST
          type_hint: str
        - name: MaxMsgLength
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxQDepth
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxQFileSize
          pcf_type: MQCFIN
          type_hint: int
        - name: MsgDeliverySequence
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMDS_PRIORITY
            - MQMDS_FIFO
        - name: NonPersistentMessageClass
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQNPM_CLASS_NORMAL
            - MQNPM_CLASS_HIGH
        - name: OTELPropagationControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQOTEL_PCTL_QMGR
            - MQOTEL_PCTL_MANUAL
            - MQOTEL_PCTL_AUTO
        - name: OTELTrace
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQOTEL_TRACE_QMGR
            - MQOTEL_TRACE_OFF
            - MQOTEL_TRACE_ON
        - name: ProcessName
          pcf_type: MQCFST
          type_hint: str
        - name: PropertyControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPROP_COMPATIBILITY
            - MQPROP_NONE
            - MQPROP_ALL
            - MQPROP_FORCE_MQRFH2
            - MQPROP_V6COMPAT
        - name: QDepthHighEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
        - name: QDepthHighLimit
          pcf_type: MQCFIN
          type_hint: int
        - name: QDepthLowEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
        - name: QDepthLowLimit
          pcf_type: MQCFIN
          type_hint: int
        - name: QDepthMaxEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
        - name: QDesc
          pcf_type: MQCFST
          type_hint: str
        - name: QServiceInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: QServiceIntervalEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSIE_HIGH
            - MQQSIE_OK
            - MQQSIE_NONE
        - name: QSGDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSGD_COPY
            - MQQSGD_Q_MGR
            - MQQSGD_GROUP
            - MQQSGD_PRIVATE
            - MQQSGD_SHARED
        - name: QueueAccounting
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_Q_MGR
            - MQMON_OFF
            - MQMON_ON
        - name: QueueMonitoring
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_OFF
            - MQMON_Q_MGR
            - MQMON_LOW
            - MQMON_MEDIUM
            - MQMON_HIGH
        - name: QueueStatistics
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_Q_MGR
            - MQMON_OFF
            - MQMON_ON
        - name: RemoteQMgrName
          pcf_type: MQCFST
          type_hint: str
        - name: RemoteQName
          pcf_type: MQCFST
          type_hint: str
        - name: RetentionInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: Scope
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSCO_Q_MGR
            - MQSCO_CELL
        - name: Shareability
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQA_SHAREABLE
            - MQQA_NOT_SHAREABLE
        - name: StorageClass
          pcf_type: MQCFST
          type_hint: str
        - name: StreamQ
          pcf_type: MQCFST
          type_hint: str
        - name: StreamQService
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQST_BEST_EFFORT
            - MQST_MUST_DUP
        - name: TargetType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQOT_Q
            - MQOT_TOPIC
        - name: TriggerControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQTC_OFF
            - MQTC_ON
        - name: TriggerData
          pcf_type: MQCFST
          type_hint: str
        - name: TriggerDepth
          pcf_type: MQCFIN
          type_hint: int
        - name: TriggerMsgPriority
          pcf_type: MQCFIN
          type_hint: int
        - name: TriggerType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQTT_NONE
            - MQTT_EVERY
            - MQTT_FIRST
            - MQTT_DEPTH
        - name: Usage
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQUS_NORMAL
            - MQUS_TRANSMISSION
        - name: XmitQName
          pcf_type: MQCFST
          type_hint: str
      response_parameters:
        []
    notes:
      - change-queue-excludes-copy-only-parameters
      - change-queue-excludes-replace-parameter
  - mqsc:
      name: DEFINE QALIAS
      href: SSFKSJ_9.4.0/refadmin/q085690_.html
      positional_parameters:
        - (queue-name)
      input_parameters:
        - CAPEXPRY
        - CLUSNL
        - CLUSTER
        - CLWLPRTY
        - CLWLRANK
        - CMDSCOPE
        - CUSTOM
        - DEFBIND
        - DEFPRESP
        - DEFPRTY
        - DEFPSIST
        - DEFREADA
        - DESCR
        - FORCE
        - GET
        - LIKE
        - NOREPLACE
        - PROPCTL
        - PUT
        - QSGDISP
        - REPLACE
        - SCOPE
        - TARGET
        - TARGQ
        - TARGTYPE
      output_parameters:
        []
      section_sources:
        Parameter descriptions for DEFINE queues:
          - CAPEXPRY
          - CLUSNL
          - CLUSTER
          - CLWLPRTY
          - CLWLRANK
          - CMDSCOPE
          - CUSTOM
          - DEFBIND
          - DEFPRESP
          - DEFPRTY
          - DEFPSIST
          - DEFREADA
          - DESCR
          - FORCE
          - GET
          - LIKE
          - NOREPLACE
          - PROPCTL
          - PUT
          - QSGDISP
          - REPLACE
          - SCOPE
          - TARGET
          - TARGQ
          - TARGTYPE
    pcf:
      command: MQCMD_CREATE_Q
      request_href: SSFKSJ_9.4.0/refadmin/q086990_.html
      response_href: null
      request_parameters:
        - name: QName
          pcf_type: MQCFST
          type_hint: str
        - name: QType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQT_ALIAS
            - MQQT_LOCAL
            - MQQT_REMOTE
            - MQQT_MODEL
        - name: BackoutRequeueName
          pcf_type: MQCFST
          type_hint: str
        - name: BackoutThreshold
          pcf_type: MQCFIN
          type_hint: int
        - name: BaseObjectName
          pcf_type: MQCFST
          type_hint: str
        - name: BaseQName
          pcf_type: MQCFST
          type_hint: str
        - name: CapExpiry
          pcf_type: MQCFIN
          type_hint: int
        - name: CFStructure
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterChannelName
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterName
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterNamelist
          pcf_type: MQCFST
          type_hint: str
        - name: CLWLQueuePriority
          pcf_type: MQCFIN
          type_hint: int
        - name: CLWLQueueRank
          pcf_type: MQCFIN
          type_hint: int
        - name: CLWLUseQ
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCLWL_USEQ_AS_Q_MGR
            - MQCLWL_USEQ_ANY
            - MQCLWL_USEQ_LOCAL
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: Custom
          pcf_type: MQCFST
          type_hint: str
        - name: DefaultPutResponse
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPRT_SYNC_RESPONSE
            - MQPRT_ASYNC_RESPONSE
        - name: DefBind
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQBND_BIND_ON_OPEN
            - MQBND_BIND_NOT_FIXED
            - MQBND_BIND_ON_GROUP
        - name: DefinitionType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQDT_PERMANENT_DYNAMIC
            - MQQDT_SHARED_DYNAMIC
            - MQQDT_TEMPORARY_DYNAMIC
        - name: DefInputOpenOption
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQOO_INPUT_EXCLUSIVE
            - MQOO_INPUT_SHARED
        - name: DefPersistence
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPER_PERSISTENT
            - MQPER_NOT_PERSISTENT
        - name: DefPriority
          pcf_type: MQCFIN
          type_hint: int
        - name: DefReadAhead
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQREADA_NO
            - MQREADA_YES
            - MQREADA_DISABLED
        - name: DistLists
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQDL_SUPPORTED
            - MQDL_NOT_SUPPORTED
        - name: Force
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQFC_YES
            - MQFC_NO
        - name: HardenGetBackout
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQA_BACKOUT_HARDENED
            - MQQA_BACKOUT_NOT_HARDENED
        - name: ImageRecoverQueue
          pcf_type: MQCFST
          type_hint: str
          enum_values:
            - MQIMGRCOV_YES
            - MQIMGRCOV_NO
            - MQIMGRCOV_AS_Q_MGR
        - name: IndexType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQIT_NONE
            - MQIT_MSG_ID
            - MQIT_CORREL_ID
            - MQIT_MSG_TOKEN
            - MQIT_GROUP_ID
        - name: InhibitGet
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQA_GET_ALLOWED
            - MQQA_GET_INHIBITED
        - name: InhibitPut
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQA_PUT_ALLOWED
            - MQQA_PUT_INHIBITED
        - name: InitiationQName
          pcf_type: MQCFST
          type_hint: str
        - name: MaxMsgLength
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxQDepth
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxQFileSize
          pcf_type: MQCFIN
          type_hint: int
        - name: MsgDeliverySequence
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMDS_PRIORITY
            - MQMDS_FIFO
        - name: NonPersistentMessageClass
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQNPM_CLASS_NORMAL
            - MQNPM_CLASS_HIGH
        - name: OTELPropagationControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQOTEL_PCTL_QMGR
            - MQOTEL_PCTL_MANUAL
            - MQOTEL_PCTL_AUTO
        - name: OTELTrace
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQOTEL_TRACE_QMGR
            - MQOTEL_TRACE_OFF
            - MQOTEL_TRACE_ON
        - name: ProcessName
          pcf_type: MQCFST
          type_hint: str
        - name: PropertyControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPROP_COMPATIBILITY
            - MQPROP_NONE
            - MQPROP_ALL
            - MQPROP_FORCE_MQRFH2
            - MQPROP_V6COMPAT
        - name: QDepthHighEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
        - name: QDepthHighLimit
          pcf_type: MQCFIN
          type_hint: int
        - name: QDepthLowEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
        - name: QDepthLowLimit
          pcf_type: MQCFIN
          type_hint: int
        - name: QDepthMaxEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
        - name: QDesc
          pcf_type: MQCFST
          type_hint: str
        - name: QServiceInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: QServiceIntervalEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSIE_HIGH
            - MQQSIE_OK
            - MQQSIE_NONE
        - name: QSGDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSGD_COPY
            - MQQSGD_Q_MGR
            - MQQSGD_GROUP
            - MQQSGD_PRIVATE
            - MQQSGD_SHARED
        - name: QueueAccounting
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_Q_MGR
            - MQMON_OFF
            - MQMON_ON
        - name: QueueMonitoring
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_OFF
            - MQMON_Q_MGR
            - MQMON_LOW
            - MQMON_MEDIUM
            - MQMON_HIGH
        - name: QueueStatistics
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_Q_MGR
            - MQMON_OFF
            - MQMON_ON
        - name: RemoteQMgrName
          pcf_type: MQCFST
          type_hint: str
        - name: RemoteQName
          pcf_type: MQCFST
          type_hint: str
        - name: Replace
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQRP_YES
            - MQRP_NO
        - name: RetentionInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: Scope
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSCO_Q_MGR
            - MQSCO_CELL
        - name: Shareability
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQA_SHAREABLE
            - MQQA_NOT_SHAREABLE
        - name: StorageClass
          pcf_type: MQCFST
          type_hint: str
        - name: StreamQ
          pcf_type: MQCFST
          type_hint: str
        - name: StreamQService
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQST_BEST_EFFORT
            - MQST_MUST_DUP
        - name: TargetType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQOT_Q
            - MQOT_TOPIC
        - name: TriggerControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQTC_OFF
            - MQTC_ON
        - name: TriggerData
          pcf_type: MQCFST
          type_hint: str
        - name: TriggerDepth
          pcf_type: MQCFIN
          type_hint: int
        - name: TriggerMsgPriority
          pcf_type: MQCFIN
          type_hint: int
        - name: TriggerType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQTT_NONE
            - MQTT_EVERY
            - MQTT_FIRST
            - MQTT_DEPTH
        - name: Usage
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQUS_NORMAL
            - MQUS_TRANSMISSION
        - name: XmitQName
          pcf_type: MQCFST
          type_hint: str
      response_parameters:
        []
    notes:
      - create-queue-excludes-copy-only-parameters
  - mqsc:
      name: DELETE QALIAS
      href: SSFKSJ_9.4.0/refadmin/q085890_.html
      positional_parameters:
        - (q-name)
      input_parameters:
        - AUTHREC
        - CMDSCOPE
        - IGNSTATE
        - QSGDISP
      output_parameters:
        []
      section_sources:
        Parameter descriptions for DELETE queues:
          - AUTHREC
          - CMDSCOPE
          - IGNSTATE
          - QSGDISP
    pcf:
      command: MQCMD_DELETE_Q
      request_href: SSFKSJ_9.4.0/refadmin/q087180_.html
      response_href: SSFKSJ_9.4.0/refadmin/q087180_.html
      request_parameters:
        - name: QName
          pcf_type: MQCFST
          type_hint: str
        - name: Authrec
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQRAR_YES
            - MQRAR_NO
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: Purge
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPO_YES
            - MQPO_NO
        - name: QSGDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSGD_COPY
            - MQQSGD_GROUP
            - MQQSGD_Q_MGR
            - MQQSGD_SHARED
        - name: QType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQT_ALIAS
            - MQQT_LOCAL
            - MQQT_REMOTE
            - MQQT_MODEL
        - name: IgnoreState
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQIS_NO
            - MQIS_YES
      response_parameters:
        []
    notes:
      - ignore-state-type-inferred-from-mqsc-ignstate
      - ignore-state-name-normalized
  - mqsc:
      name: DISPLAY QALIAS
      href: SSFKSJ_9.4.0/refadmin/q086270_.html
      positional_parameters:
        - (generic-qname)
      input_parameters:
        - WHERE
        - ALL
        - CFSTRUCT
        - CLUSINFO
        - CLUSNL
        - CLUSTER
        - CMDSCOPE
        - PSID
        - QSGDISP
        - STGCLASS
        - TARGTYPE
      output_parameters:
        - ALTDATE
        - ALTTIME
        - CAPEXPRY
        - CLUSNL
        - CLUSTER
        - CLWLPRTY
        - CLWLRANK
        - CUSTOM
        - DEFBIND
        - DEFPRESP
        - DEFPRTY
        - DEFPSIST
        - DEFREADA
        - DESCR
        - GET
        - PROPCTL
        - PUT
        - QSGDISP
        - QTYPE
        - SCOPE
        - TARGET
        - TARGTYPE
      section_sources:
        Parameter descriptions for DISPLAY QUEUE:
          - WHERE
          - ALL
          - CFSTRUCT
          - CLUSINFO
          - CLUSNL
          - CLUSTER
          - CMDSCOPE
          - PSID
          - QSGDISP
          - STGCLASS
          - TARGTYPE
        Requested parameters:
          - ALTDATE
          - ALTTIME
          - CAPEXPRY
          - CLUSNL
          - CLUSTER
          - CLWLPRTY
          - CLWLRANK
          - CUSTOM
          - DEFBIND
          - DEFPRESP
          - DEFPRTY
          - DEFPSIST
          - DEFREADA
          - DESCR
          - GET
          - PROPCTL
          - PUT
          - QSGDISP
          - QTYPE
          - SCOPE
          - TARGET
          - TARGTYPE
    pcf:
      command: MQCMD_INQUIRE_Q
      request_href: SSFKSJ_9.4.0/refadmin/q087800_.html
      response_href: SSFKSJ_9.4.0/refadmin/q087810_.html
      request_parameters:
        - name: QName
          pcf_type: MQCFST
          type_hint: str
        - name: CapExpiry
          pcf_type: MQCFIN
          type_hint: int
        - name: CFStructure
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterInfo
          pcf_type: MQCFIN
          type_hint: int
        - name: ClusterName
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterNamelist
          pcf_type: MQCFST
          type_hint: str
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: IntegerFilterCommand
          pcf_type: MQCFIF
          type_hint: null
        - name: PageSetID
          pcf_type: MQCFIN
          type_hint: int
        - name: QAttrs
          pcf_type: MQCFIL
          type_hint: int
          enum_values:
            - MQIACF_ALL
            - MQCA_ALTERATION_DATE
            - MQCA_ALTERATION_TIME
            - MQCA_BACKOUT_REQ_Q_NAME
            - MQCA_BASE_NAME
            - MQCA_CF_STRUC_NAME
            - MQCA_CLUS_CHL_NAME
            - MQCA_CLUSTER_DATE
            - MQCA_CLUSTER_NAME
            - MQCA_CLUSTER_NAMELIST
            - MQCA_CLUSTER_Q_MGR_NAME
            - MQCA_CLUSTER_TIME
            - MQCA_CREATION_DATE
            - MQCA_CREATION_TIME
            - MQCA_CUSTOM
            - MQCA_INITIATION_Q_NAME
            - MQCA_PROCESS_NAME
            - MQCA_Q_DESC
            - MQCA_Q_MGR_IDENTIFIER
            - MQCA_Q_NAME
            - MQCA_REMOTE_Q_MGR_NAME
            - MQCA_REMOTE_Q_NAME
            - MQCA_STORAGE_CLASS
            - MQCA_STREAM_QUEUE_NAME
            - MQCA_TPIPE_NAME
            - MQCA_TRIGGER_DATA
            - MQCA_XMIT_Q_NAME
            - MQIA_ACCOUNTING_Q
            - MQIA_BACKOUT_THRESHOLD
            - MQIA_BASE_TYPE
            - MQIA_CLUSTER_Q_TYPE
            - MQIA_CLWL_Q_PRIORITY
            - MQIA_CLWL_Q_RANK
            - MQIA_CLWL_USEQ
            - MQIA_CURRENT_Q_DEPTH
            - MQIA_DEF_BIND
            - MQIA_DEF_INPUT_OPEN_OPTION
            - MQIA_DEF_PERSISTENCE
            - MQIA_DEF_PRIORITY
            - MQIA_DEF_PUT_RESPONSE_TYPE
            - MQIA_DEF_READ_AHEAD
            - MQIA_DEFINITION_TYPE
            - MQIA_DIST_LISTS
            - MQIA_HARDEN_GET_BACKOUT
            - MQIA_INDEX_TYPE
            - MQIA_INHIBIT_GET
            - MQIA_INHIBIT_PUT
            - MQIA_MAX_MSG_LENGTH
            - MQIA_MAX_Q_DEPTH
            - MQIA_MEDIA_IMAGE_RECOVER_Q
            - MQIA_MONITORING_Q
            - MQIA_MSG_DELIVERY_SEQUENCE
            - MQIA_NPM_CLASS
            - MQIA_OPEN_INPUT_COUNT
            - MQIA_OPEN_OUTPUT_COUNT
            - MQIA_OTEL_PROPAGATION_CONTROL
            - MQIA_OTEL_TRACE
            - MQIA_PAGESET_ID
            - MQIA_PROPERTY_CONTROL
            - MQIA_Q_DEPTH_HIGH_EVENT
            - MQIA_Q_DEPTH_HIGH_LIMIT
            - MQIA_Q_DEPTH_LOW_EVENT
            - MQIA_Q_DEPTH_LOW_LIMIT
            - MQIA_Q_DEPTH_MAX_EVENT
            - MQIA_Q_SERVICE_INTERVAL
            - MQIA_Q_SERVICE_INTERVAL_EVENT
            - MQIA_Q_TYPE
            - MQIA_RETENTION_INTERVAL
            - MQIA_SCOPE
            - MQIA_SHAREABILITY
            - MQIA_STATISTICS_Q
            - MQIA_STREAM_QUEUE_QOS
            - MQIA_TRIGGER_CONTROL
            - MQIA_TRIGGER_DEPTH
            - MQIA_TRIGGER_MSG_PRIORITY
            - MQIA_TRIGGER_MTYPE
            - MQIA_USAGE
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
            - MQQSGD_SHARED
        - name: QType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQT_ALL
            - MQQT_LOCAL
            - MQQT_ALIAS
            - MQQT_REMOTE
            - MQQT_CLUSTER
            - MQQT_MODEL
        - name: StorageClass
          pcf_type: MQCFST
          type_hint: str
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
        - name: BackoutRequeueName
          pcf_type: MQCFST
          type_hint: str
        - name: BackoutThreshold
          pcf_type: MQCFIN
          type_hint: int
        - name: BaseQName
          pcf_type: MQCFST
          type_hint: str
        - name: CapExpiry
          pcf_type: MQCFIN
          type_hint: int
        - name: CFStructure
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterChannelName
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterDate
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterName
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterNamelist
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterQType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCQT_LOCAL_Q
            - MQCQT_ALIAS_Q
            - MQCQT_REMOTE_Q
            - MQCQT_Q_MGR_ALIAS
        - name: ClusterTime
          pcf_type: MQCFST
          type_hint: str
        - name: CLWLQueuePriority
          pcf_type: MQCFIN
          type_hint: int
        - name: CLWLQueueRank
          pcf_type: MQCFIN
          type_hint: int
        - name: CLWLUseQ
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCLWL_USEQ_AS_Q_MGR
            - MQCLWL_USEQ_ANY
            - MQCLWL_USEQ_LOCAL
        - name: CreationDate
          pcf_type: MQCFST
          type_hint: str
        - name: CreationTime
          pcf_type: MQCFST
          type_hint: str
        - name: CurrentQDepth
          pcf_type: MQCFIN
          type_hint: int
        - name: Custom
          pcf_type: MQCFST
          type_hint: str
        - name: DefaultPutResponse
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPRT_SYNC_RESPONSE
            - MQPRT_ASYNC_RESPONSE
        - name: DefBind
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQBND_BIND_ON_OPEN
            - MQBND_BIND_NOT_FIXED
            - MQBND_BIND_ON_GROUP
        - name: DefinitionType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQDT_PREDEFINED
            - MQQDT_PERMANENT_DYNAMIC
            - MQQDT_SHARED_DYNAMIC
            - MQQDT_TEMPORARY_DYNAMIC
        - name: DefInputOpenOption
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQOO_INPUT_EXCLUSIVE
            - MQOO_INPUT_SHARED
        - name: DefPersistence
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPER_PERSISTENT
            - MQPER_NOT_PERSISTENT
        - name: DefPriority
          pcf_type: MQCFIN
          type_hint: int
        - name: DefReadAhead
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQREADA_NO
            - MQREADA_YES
            - MQREADA_DISABLED
        - name: DistLists
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQDL_SUPPORTED
            - MQDL_NOT_SUPPORTED
        - name: HardenGetBackout
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQA_BACKOUT_HARDENED
            - MQQA_BACKOUT_NOT_HARDENED
        - name: ImageRecoverQueue
          pcf_type: MQCFST
          type_hint: str
          enum_values:
            - MQIMGRCOV_YES
            - MQIMGRCOV_NO
            - MQIMGRCOV_AS_Q_MGR
        - name: IndexType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQIT_NONE
            - MQIT_MSG_ID
            - MQIT_CORREL_ID
            - MQIT_MSG_TOKEN
            - MQIT_GROUP_ID
        - name: InhibitGet
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQA_GET_ALLOWED
            - MQQA_GET_INHIBITED
        - name: InhibitPut
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQA_PUT_ALLOWED
            - MQQA_PUT_INHIBITED
        - name: InitiationQName
          pcf_type: MQCFST
          type_hint: str
        - name: MaxMsgLength
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxQDepth
          pcf_type: MQCFIN
          type_hint: int
        - name: MsgDeliverySequence
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMDS_PRIORITY
            - MQMDS_FIFO
        - name: NonPersistentMessageClass
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQNPM_CLASS_NORMAL
            - MQNPM_CLASS_HIGH
        - name: OpenInputCount
          pcf_type: MQCFIN
          type_hint: int
        - name: OpenOutputCount
          pcf_type: MQCFIN
          type_hint: int
        - name: OTELPropagationControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQOTEL_PCTL_QMGR
            - MQOTEL_PCTL_MANUAL
            - MQOTEL_PCTL_AUTO
        - name: OTELTrace
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQOTEL_TRACE_QMGR
            - MQOTEL_TRACE_OFF
            - MQOTEL_TRACE_ON
        - name: PageSetID
          pcf_type: MQCFIN
          type_hint: int
        - name: ProcessName
          pcf_type: MQCFST
          type_hint: str
        - name: PropertyControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPROP_COMPATIBILITY
            - MQPROP_NONE
            - MQPROP_ALL
            - MQPROP_FORCE_MQRFH2
        - name: QDepthHighEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
        - name: QDepthHighLimit
          pcf_type: MQCFIN
          type_hint: int
        - name: QDepthLowEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
        - name: QDepthLowLimit
          pcf_type: MQCFIN
          type_hint: int
        - name: QDepthMaxEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
        - name: QDesc
          pcf_type: MQCFST
          type_hint: str
        - name: QMgrIdentifier
          pcf_type: MQCFST
          type_hint: str
        - name: QMgrName
          pcf_type: MQCFST
          type_hint: str
        - name: QName
          pcf_type: MQCFST
          type_hint: str
        - name: QServiceInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: QServiceIntervalEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSIE_HIGH
            - MQQSIE_OK
            - MQQSIE_NONE
        - name: QSGDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSGD_COPY
            - MQQSGD_GROUP
            - MQQSGD_Q_MGR
            - MQQSGD_SHARED
        - name: QType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQT_ALIAS
            - MQQT_CLUSTER
            - MQQT_LOCAL
            - MQQT_REMOTE
            - MQQT_MODEL
        - name: QueueAccounting
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_Q_MGR
            - MQMON_OFF
            - MQMON_ON
        - name: QueueMonitoring
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_OFF
            - MQMON_Q_MGR
            - MQMON_LOW
            - MQMON_MEDIUM
            - MQMON_HIGH
        - name: QueueStatistics
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_Q_MGR
            - MQMON_OFF
            - MQMON_ON
        - name: RemoteQMgrName
          pcf_type: MQCFST
          type_hint: str
        - name: RemoteQName
          pcf_type: MQCFST
          type_hint: str
        - name: RetentionInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: Scope
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSCO_Q_MGR
            - MQSCO_CELL
        - name: Shareability
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQA_SHAREABLE
            - MQQA_NOT_SHAREABLE
        - name: StorageClass
          pcf_type: MQCFST
          type_hint: str
        - name: StreamQ
          pcf_type: MQCFST
          type_hint: str
        - name: StreamQService
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQST_BEST_EFFORT
            - MQST_MUST_DUP
        - name: TpipeNames
          pcf_type: MQCFSL
          type_hint: str
        - name: TriggerControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQTC_OFF
            - MQTC_ON
        - name: TriggerData
          pcf_type: MQCFST
          type_hint: str
        - name: TriggerDepth
          pcf_type: MQCFIN
          type_hint: int
        - name: TriggerMsgPriority
          pcf_type: MQCFIN
          type_hint: int
        - name: TriggerType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQTT_NONE
            - MQTT_FIRST
            - MQTT_EVERY
            - MQTT_DEPTH
        - name: Usage
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQUS_NORMAL
            - MQUS_TRANSMISSION
        - name: XmitQName
          pcf_type: MQCFST
          type_hint: str
    notes:
      - display-queue-type-synonyms
      - qsgdisposition-returned-on-zos-only
  - mqsc:
      name: ALTER QMODEL
      href: SSFKSJ_9.4.0/refadmin/q085330_.html
      positional_parameters:
        - (queue-name)
      input_parameters:
        - ACCTQ
        - BOQNAME
        - BOTHRESH
        - CAPEXPRY
        - CFSTRUCT
        - CMDSCOPE
        - CUSTOM
        - DEFPRESP
        - DEFPRTY
        - DEFPSIST
        - DEFREADA
        - DEFSOPT
        - DEFTYPE
        - DESCR
        - DISTL
        - GET
        - HARDENBO
        - NOHARDENBO
        - IMGRCOVQ
        - INDXTYPE
        - INITQ
        - LIKE
        - MAXDEPTH
        - MAXFSIZE
        - MAXMSGL
        - MONQ
        - MSGDLVSQ
        - NPMCLASS
        - OTELPCTL
        - OTELTRAC
        - PROCESS
        - PROPCTL
        - PUT
        - QDEPTHHI
        - QDEPTHLO
        - QDPHIEV
        - QDPLOEV
        - QDPMAXEV
        - QSGDISP
        - QSVCIEV
        - QSVCINT
        - RETINTVL
        - SHARE
        - NOSHARE
        - STATQ
        - STGCLASS
        - STREAMQ
        - STRMQOS
        - TRIGDATA
        - TRIGDPTH
        - TRIGGER
        - NOTRIGGER
        - TRIGMPRI
        - TRIGTYPE
        - USAGE
      output_parameters:
        []
      section_sources:
        Parameter descriptions for ALTER queues:
          - ACCTQ
          - BOQNAME
          - BOTHRESH
          - CAPEXPRY
          - CFSTRUCT
          - CMDSCOPE
          - CUSTOM
          - DEFPRESP
          - DEFPRTY
          - DEFPSIST
          - DEFREADA
          - DEFSOPT
          - DEFTYPE
          - DESCR
          - DISTL
          - GET
          - HARDENBO
          - NOHARDENBO
          - IMGRCOVQ
          - INDXTYPE
          - INITQ
          - LIKE
          - MAXDEPTH
          - MAXFSIZE
          - MAXMSGL
          - MONQ
          - MSGDLVSQ
          - NPMCLASS
          - OTELPCTL
          - OTELTRAC
          - PROCESS
          - PROPCTL
          - PUT
          - QDEPTHHI
          - QDEPTHLO
          - QDPHIEV
          - QDPLOEV
          - QDPMAXEV
          - QSGDISP
          - QSVCIEV
          - QSVCINT
          - RETINTVL
          - SHARE
          - NOSHARE
          - STATQ
          - STGCLASS
          - STREAMQ
          - STRMQOS
          - TRIGDATA
          - TRIGDPTH
          - TRIGGER
          - NOTRIGGER
          - TRIGMPRI
          - TRIGTYPE
          - USAGE
    pcf:
      command: MQCMD_CHANGE_Q
      request_href: SSFKSJ_9.4.0/refadmin/q086990_.html
      response_href: null
      request_parameters:
        - name: QName
          pcf_type: MQCFST
          type_hint: str
        - name: QType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQT_ALIAS
            - MQQT_LOCAL
            - MQQT_REMOTE
            - MQQT_MODEL
        - name: BackoutRequeueName
          pcf_type: MQCFST
          type_hint: str
        - name: BackoutThreshold
          pcf_type: MQCFIN
          type_hint: int
        - name: BaseObjectName
          pcf_type: MQCFST
          type_hint: str
        - name: BaseQName
          pcf_type: MQCFST
          type_hint: str
        - name: CapExpiry
          pcf_type: MQCFIN
          type_hint: int
        - name: CFStructure
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterChannelName
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterName
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterNamelist
          pcf_type: MQCFST
          type_hint: str
        - name: CLWLQueuePriority
          pcf_type: MQCFIN
          type_hint: int
        - name: CLWLQueueRank
          pcf_type: MQCFIN
          type_hint: int
        - name: CLWLUseQ
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCLWL_USEQ_AS_Q_MGR
            - MQCLWL_USEQ_ANY
            - MQCLWL_USEQ_LOCAL
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: Custom
          pcf_type: MQCFST
          type_hint: str
        - name: DefaultPutResponse
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPRT_SYNC_RESPONSE
            - MQPRT_ASYNC_RESPONSE
        - name: DefBind
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQBND_BIND_ON_OPEN
            - MQBND_BIND_NOT_FIXED
            - MQBND_BIND_ON_GROUP
        - name: DefinitionType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQDT_PERMANENT_DYNAMIC
            - MQQDT_SHARED_DYNAMIC
            - MQQDT_TEMPORARY_DYNAMIC
        - name: DefInputOpenOption
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQOO_INPUT_EXCLUSIVE
            - MQOO_INPUT_SHARED
        - name: DefPersistence
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPER_PERSISTENT
            - MQPER_NOT_PERSISTENT
        - name: DefPriority
          pcf_type: MQCFIN
          type_hint: int
        - name: DefReadAhead
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQREADA_NO
            - MQREADA_YES
            - MQREADA_DISABLED
        - name: DistLists
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQDL_SUPPORTED
            - MQDL_NOT_SUPPORTED
        - name: Force
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQFC_YES
            - MQFC_NO
        - name: HardenGetBackout
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQA_BACKOUT_HARDENED
            - MQQA_BACKOUT_NOT_HARDENED
        - name: ImageRecoverQueue
          pcf_type: MQCFST
          type_hint: str
          enum_values:
            - MQIMGRCOV_YES
            - MQIMGRCOV_NO
            - MQIMGRCOV_AS_Q_MGR
        - name: IndexType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQIT_NONE
            - MQIT_MSG_ID
            - MQIT_CORREL_ID
            - MQIT_MSG_TOKEN
            - MQIT_GROUP_ID
        - name: InhibitGet
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQA_GET_ALLOWED
            - MQQA_GET_INHIBITED
        - name: InhibitPut
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQA_PUT_ALLOWED
            - MQQA_PUT_INHIBITED
        - name: InitiationQName
          pcf_type: MQCFST
          type_hint: str
        - name: MaxMsgLength
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxQDepth
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxQFileSize
          pcf_type: MQCFIN
          type_hint: int
        - name: MsgDeliverySequence
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMDS_PRIORITY
            - MQMDS_FIFO
        - name: NonPersistentMessageClass
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQNPM_CLASS_NORMAL
            - MQNPM_CLASS_HIGH
        - name: OTELPropagationControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQOTEL_PCTL_QMGR
            - MQOTEL_PCTL_MANUAL
            - MQOTEL_PCTL_AUTO
        - name: OTELTrace
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQOTEL_TRACE_QMGR
            - MQOTEL_TRACE_OFF
            - MQOTEL_TRACE_ON
        - name: ProcessName
          pcf_type: MQCFST
          type_hint: str
        - name: PropertyControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPROP_COMPATIBILITY
            - MQPROP_NONE
            - MQPROP_ALL
            - MQPROP_FORCE_MQRFH2
            - MQPROP_V6COMPAT
        - name: QDepthHighEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
        - name: QDepthHighLimit
          pcf_type: MQCFIN
          type_hint: int
        - name: QDepthLowEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
        - name: QDepthLowLimit
          pcf_type: MQCFIN
          type_hint: int
        - name: QDepthMaxEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
        - name: QDesc
          pcf_type: MQCFST
          type_hint: str
        - name: QServiceInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: QServiceIntervalEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSIE_HIGH
            - MQQSIE_OK
            - MQQSIE_NONE
        - name: QSGDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSGD_COPY
            - MQQSGD_Q_MGR
            - MQQSGD_GROUP
            - MQQSGD_PRIVATE
            - MQQSGD_SHARED
        - name: QueueAccounting
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_Q_MGR
            - MQMON_OFF
            - MQMON_ON
        - name: QueueMonitoring
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_OFF
            - MQMON_Q_MGR
            - MQMON_LOW
            - MQMON_MEDIUM
            - MQMON_HIGH
        - name: QueueStatistics
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_Q_MGR
            - MQMON_OFF
            - MQMON_ON
        - name: RemoteQMgrName
          pcf_type: MQCFST
          type_hint: str
        - name: RemoteQName
          pcf_type: MQCFST
          type_hint: str
        - name: RetentionInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: Scope
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSCO_Q_MGR
            - MQSCO_CELL
        - name: Shareability
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQA_SHAREABLE
            - MQQA_NOT_SHAREABLE
        - name: StorageClass
          pcf_type: MQCFST
          type_hint: str
        - name: StreamQ
          pcf_type: MQCFST
          type_hint: str
        - name: StreamQService
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQST_BEST_EFFORT
            - MQST_MUST_DUP
        - name: TargetType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQOT_Q
            - MQOT_TOPIC
        - name: TriggerControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQTC_OFF
            - MQTC_ON
        - name: TriggerData
          pcf_type: MQCFST
          type_hint: str
        - name: TriggerDepth
          pcf_type: MQCFIN
          type_hint: int
        - name: TriggerMsgPriority
          pcf_type: MQCFIN
          type_hint: int
        - name: TriggerType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQTT_NONE
            - MQTT_EVERY
            - MQTT_FIRST
            - MQTT_DEPTH
        - name: Usage
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQUS_NORMAL
            - MQUS_TRANSMISSION
        - name: XmitQName
          pcf_type: MQCFST
          type_hint: str
      response_parameters:
        []
    notes:
      - change-queue-excludes-copy-only-parameters
      - change-queue-excludes-replace-parameter
  - mqsc:
      name: DEFINE QMODEL
      href: SSFKSJ_9.4.0/refadmin/q085690_.html
      positional_parameters:
        - (queue-name)
      input_parameters:
        - ACCTQ
        - BOQNAME
        - BOTHRESH
        - CAPEXPRY
        - CFSTRUCT
        - CMDSCOPE
        - CUSTOM
        - DEFPRESP
        - DEFPRTY
        - DEFPSIST
        - DEFREADA
        - DEFSOPT
        - DEFTYPE
        - DESCR
        - DISTL
        - GET
        - HARDENBO
        - NOHARDENBO
        - IMGRCOVQ
        - INDXTYPE
        - INITQ
        - LIKE
        - MAXDEPTH
        - MAXFSIZE
        - MAXMSGL
        - MONQ
        - MSGDLVSQ
        - NOREPLACE
        - NPMCLASS
        - OTELPCTL
        - OTELTRAC
        - PROCESS
        - PROPCTL
        - PUT
        - QDEPTHHI
        - QDEPTHLO
        - QDPHIEV
        - QDPLOEV
        - QDPMAXEV
        - QSGDISP
        - QSVCIEV
        - QSVCINT
        - REPLACE
        - RETINTVL
        - SHARE
        - NOSHARE
        - STATQ
        - STGCLASS
        - STREAMQ
        - STRMQOS
        - TRIGDATA
        - TRIGDPTH
        - TRIGGER
        - NOTRIGGER
        - TRIGMPRI
        - TRIGTYPE
        - USAGE
      output_parameters:
        []
      section_sources:
        Parameter descriptions for DEFINE queues:
          - ACCTQ
          - BOQNAME
          - BOTHRESH
          - CAPEXPRY
          - CFSTRUCT
          - CMDSCOPE
          - CUSTOM
          - DEFPRESP
          - DEFPRTY
          - DEFPSIST
          - DEFREADA
          - DEFSOPT
          - DEFTYPE
          - DESCR
          - DISTL
          - GET
          - HARDENBO
          - NOHARDENBO
          - IMGRCOVQ
          - INDXTYPE
          - INITQ
          - LIKE
          - MAXDEPTH
          - MAXFSIZE
          - MAXMSGL
          - MONQ
          - MSGDLVSQ
          - NOREPLACE
          - NPMCLASS
          - OTELPCTL
          - OTELTRAC
          - PROCESS
          - PROPCTL
          - PUT
          - QDEPTHHI
          - QDEPTHLO
          - QDPHIEV
          - QDPLOEV
          - QDPMAXEV
          - QSGDISP
          - QSVCIEV
          - QSVCINT
          - REPLACE
          - RETINTVL
          - SHARE
          - NOSHARE
          - STATQ
          - STGCLASS
          - STREAMQ
          - STRMQOS
          - TRIGDATA
          - TRIGDPTH
          - TRIGGER
          - NOTRIGGER
          - TRIGMPRI
          - TRIGTYPE
          - USAGE
    pcf:
      command: MQCMD_CREATE_Q
      request_href: SSFKSJ_9.4.0/refadmin/q086990_.html
      response_href: null
      request_parameters:
        - name: QName
          pcf_type: MQCFST
          type_hint: str
        - name: QType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQT_ALIAS
            - MQQT_LOCAL
            - MQQT_REMOTE
            - MQQT_MODEL
        - name: BackoutRequeueName
          pcf_type: MQCFST
          type_hint: str
        - name: BackoutThreshold
          pcf_type: MQCFIN
          type_hint: int
        - name: BaseObjectName
          pcf_type: MQCFST
          type_hint: str
        - name: BaseQName
          pcf_type: MQCFST
          type_hint: str
        - name: CapExpiry
          pcf_type: MQCFIN
          type_hint: int
        - name: CFStructure
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterChannelName
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterName
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterNamelist
          pcf_type: MQCFST
          type_hint: str
        - name: CLWLQueuePriority
          pcf_type: MQCFIN
          type_hint: int
        - name: CLWLQueueRank
          pcf_type: MQCFIN
          type_hint: int
        - name: CLWLUseQ
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCLWL_USEQ_AS_Q_MGR
            - MQCLWL_USEQ_ANY
            - MQCLWL_USEQ_LOCAL
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: Custom
          pcf_type: MQCFST
          type_hint: str
        - name: DefaultPutResponse
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPRT_SYNC_RESPONSE
            - MQPRT_ASYNC_RESPONSE
        - name: DefBind
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQBND_BIND_ON_OPEN
            - MQBND_BIND_NOT_FIXED
            - MQBND_BIND_ON_GROUP
        - name: DefinitionType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQDT_PERMANENT_DYNAMIC
            - MQQDT_SHARED_DYNAMIC
            - MQQDT_TEMPORARY_DYNAMIC
        - name: DefInputOpenOption
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQOO_INPUT_EXCLUSIVE
            - MQOO_INPUT_SHARED
        - name: DefPersistence
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPER_PERSISTENT
            - MQPER_NOT_PERSISTENT
        - name: DefPriority
          pcf_type: MQCFIN
          type_hint: int
        - name: DefReadAhead
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQREADA_NO
            - MQREADA_YES
            - MQREADA_DISABLED
        - name: DistLists
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQDL_SUPPORTED
            - MQDL_NOT_SUPPORTED
        - name: Force
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQFC_YES
            - MQFC_NO
        - name: HardenGetBackout
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQA_BACKOUT_HARDENED
            - MQQA_BACKOUT_NOT_HARDENED
        - name: ImageRecoverQueue
          pcf_type: MQCFST
          type_hint: str
          enum_values:
            - MQIMGRCOV_YES
            - MQIMGRCOV_NO
            - MQIMGRCOV_AS_Q_MGR
        - name: IndexType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQIT_NONE
            - MQIT_MSG_ID
            - MQIT_CORREL_ID
            - MQIT_MSG_TOKEN
            - MQIT_GROUP_ID
        - name: InhibitGet
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQA_GET_ALLOWED
            - MQQA_GET_INHIBITED
        - name: InhibitPut
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQA_PUT_ALLOWED
            - MQQA_PUT_INHIBITED
        - name: InitiationQName
          pcf_type: MQCFST
          type_hint: str
        - name: MaxMsgLength
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxQDepth
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxQFileSize
          pcf_type: MQCFIN
          type_hint: int
        - name: MsgDeliverySequence
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMDS_PRIORITY
            - MQMDS_FIFO
        - name: NonPersistentMessageClass
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQNPM_CLASS_NORMAL
            - MQNPM_CLASS_HIGH
        - name: OTELPropagationControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQOTEL_PCTL_QMGR
            - MQOTEL_PCTL_MANUAL
            - MQOTEL_PCTL_AUTO
        - name: OTELTrace
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQOTEL_TRACE_QMGR
            - MQOTEL_TRACE_OFF
            - MQOTEL_TRACE_ON
        - name: ProcessName
          pcf_type: MQCFST
          type_hint: str
        - name: PropertyControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPROP_COMPATIBILITY
            - MQPROP_NONE
            - MQPROP_ALL
            - MQPROP_FORCE_MQRFH2
            - MQPROP_V6COMPAT
        - name: QDepthHighEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
        - name: QDepthHighLimit
          pcf_type: MQCFIN
          type_hint: int
        - name: QDepthLowEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
        - name: QDepthLowLimit
          pcf_type: MQCFIN
          type_hint: int
        - name: QDepthMaxEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
        - name: QDesc
          pcf_type: MQCFST
          type_hint: str
        - name: QServiceInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: QServiceIntervalEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSIE_HIGH
            - MQQSIE_OK
            - MQQSIE_NONE
        - name: QSGDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSGD_COPY
            - MQQSGD_Q_MGR
            - MQQSGD_GROUP
            - MQQSGD_PRIVATE
            - MQQSGD_SHARED
        - name: QueueAccounting
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_Q_MGR
            - MQMON_OFF
            - MQMON_ON
        - name: QueueMonitoring
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_OFF
            - MQMON_Q_MGR
            - MQMON_LOW
            - MQMON_MEDIUM
            - MQMON_HIGH
        - name: QueueStatistics
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_Q_MGR
            - MQMON_OFF
            - MQMON_ON
        - name: RemoteQMgrName
          pcf_type: MQCFST
          type_hint: str
        - name: RemoteQName
          pcf_type: MQCFST
          type_hint: str
        - name: Replace
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQRP_YES
            - MQRP_NO
        - name: RetentionInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: Scope
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSCO_Q_MGR
            - MQSCO_CELL
        - name: Shareability
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQA_SHAREABLE
            - MQQA_NOT_SHAREABLE
        - name: StorageClass
          pcf_type: MQCFST
          type_hint: str
        - name: StreamQ
          pcf_type: MQCFST
          type_hint: str
        - name: StreamQService
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQST_BEST_EFFORT
            - MQST_MUST_DUP
        - name: TargetType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQOT_Q
            - MQOT_TOPIC
        - name: TriggerControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQTC_OFF
            - MQTC_ON
        - name: TriggerData
          pcf_type: MQCFST
          type_hint: str
        - name: TriggerDepth
          pcf_type: MQCFIN
          type_hint: int
        - name: TriggerMsgPriority
          pcf_type: MQCFIN
          type_hint: int
        - name: TriggerType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQTT_NONE
            - MQTT_EVERY
            - MQTT_FIRST
            - MQTT_DEPTH
        - name: Usage
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQUS_NORMAL
            - MQUS_TRANSMISSION
        - name: XmitQName
          pcf_type: MQCFST
          type_hint: str
      response_parameters:
        []
    notes:
      - create-queue-excludes-copy-only-parameters
  - mqsc:
      name: DELETE QMODEL
      href: SSFKSJ_9.4.0/refadmin/q085890_.html
      positional_parameters:
        - (q-name)
      input_parameters:
        - AUTHREC
        - CMDSCOPE
        - IGNSTATE
        - QSGDISP
      output_parameters:
        []
      section_sources:
        Parameter descriptions for DELETE queues:
          - AUTHREC
          - CMDSCOPE
          - IGNSTATE
          - QSGDISP
    pcf:
      command: MQCMD_DELETE_Q
      request_href: SSFKSJ_9.4.0/refadmin/q087180_.html
      response_href: SSFKSJ_9.4.0/refadmin/q087180_.html
      request_parameters:
        - name: QName
          pcf_type: MQCFST
          type_hint: str
        - name: Authrec
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQRAR_YES
            - MQRAR_NO
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: Purge
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPO_YES
            - MQPO_NO
        - name: QSGDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSGD_COPY
            - MQQSGD_GROUP
            - MQQSGD_Q_MGR
            - MQQSGD_SHARED
        - name: QType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQT_ALIAS
            - MQQT_LOCAL
            - MQQT_REMOTE
            - MQQT_MODEL
        - name: IgnoreState
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQIS_NO
            - MQIS_YES
      response_parameters:
        []
    notes:
      - ignore-state-type-inferred-from-mqsc-ignstate
      - ignore-state-name-normalized
  - mqsc:
      name: DISPLAY QMODEL
      href: SSFKSJ_9.4.0/refadmin/q086270_.html
      positional_parameters:
        - (generic-qname)
      input_parameters:
        - WHERE
        - ALL
        - CFSTRUCT
        - CLUSINFO
        - CLUSNL
        - CLUSTER
        - CMDSCOPE
        - PSID
        - QSGDISP
        - STGCLASS
        - TARGTYPE
      output_parameters:
        - ACCTQ
        - ALTDATE
        - ALTTIME
        - BOQNAME
        - BOTHRESH
        - CAPEXPRY
        - CFSTRUCT
        - CLCHNAME
        - CRDATE
        - CRTIME
        - CUSTOM
        - DEFPRESP
        - DEFPRTY
        - DEFPSIST
        - DEFREADA
        - DEFSOPT
        - DEFTYPE
        - DESCR
        - DISTL
        - GET
        - HARDENBO
        - IMGRCOVQ
        - INDXTYPE
        - INITQ
        - MAXDEPTH
        - MAXFSIZE
        - MAXMSGL
        - MONQ
        - MSGDLVSQ
        - NPMCLASS
        - OTELPCTL
        - OTELTRAC
        - PROCESS
        - PROPCTL
        - PUT
        - QDEPTHHI
        - QDEPTHLO
        - QDPHIEV
        - QDPLOEV
        - QDPMAXEV
        - QSGDISP
        - QSVCIEV
        - QSVCINT
        - QTYPE
        - RETINTVL
        - SHARE
        - STATQ
        - STGCLASS
        - STREAMQ
        - STRMQOS
        - TRIGDATA
        - TRIGDPTH
        - TRIGGER
        - TRIGMPRI
        - TRIGTYPE
        - USAGE
      section_sources:
        Parameter descriptions for DISPLAY QUEUE:
          - WHERE
          - ALL
          - CFSTRUCT
          - CLUSINFO
          - CLUSNL
          - CLUSTER
          - CMDSCOPE
          - PSID
          - QSGDISP
          - STGCLASS
          - TARGTYPE
        Requested parameters:
          - ACCTQ
          - ALTDATE
          - ALTTIME
          - BOQNAME
          - BOTHRESH
          - CAPEXPRY
          - CFSTRUCT
          - CLCHNAME
          - CRDATE
          - CRTIME
          - CUSTOM
          - DEFPRESP
          - DEFPRTY
          - DEFPSIST
          - DEFREADA
          - DEFSOPT
          - DEFTYPE
          - DESCR
          - DISTL
          - GET
          - HARDENBO
          - IMGRCOVQ
          - INDXTYPE
          - INITQ
          - MAXDEPTH
          - MAXFSIZE
          - MAXMSGL
          - MONQ
          - MSGDLVSQ
          - NPMCLASS
          - OTELPCTL
          - OTELTRAC
          - PROCESS
          - PROPCTL
          - PUT
          - QDEPTHHI
          - QDEPTHLO
          - QDPHIEV
          - QDPLOEV
          - QDPMAXEV
          - QSGDISP
          - QSVCIEV
          - QSVCINT
          - QTYPE
          - RETINTVL
          - SHARE
          - STATQ
          - STGCLASS
          - STREAMQ
          - STRMQOS
          - TRIGDATA
          - TRIGDPTH
          - TRIGGER
          - TRIGMPRI
          - TRIGTYPE
          - USAGE
    pcf:
      command: MQCMD_INQUIRE_Q
      request_href: SSFKSJ_9.4.0/refadmin/q087800_.html
      response_href: SSFKSJ_9.4.0/refadmin/q087810_.html
      request_parameters:
        - name: QName
          pcf_type: MQCFST
          type_hint: str
        - name: CapExpiry
          pcf_type: MQCFIN
          type_hint: int
        - name: CFStructure
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterInfo
          pcf_type: MQCFIN
          type_hint: int
        - name: ClusterName
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterNamelist
          pcf_type: MQCFST
          type_hint: str
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: IntegerFilterCommand
          pcf_type: MQCFIF
          type_hint: null
        - name: PageSetID
          pcf_type: MQCFIN
          type_hint: int
        - name: QAttrs
          pcf_type: MQCFIL
          type_hint: int
          enum_values:
            - MQIACF_ALL
            - MQCA_ALTERATION_DATE
            - MQCA_ALTERATION_TIME
            - MQCA_BACKOUT_REQ_Q_NAME
            - MQCA_BASE_NAME
            - MQCA_CF_STRUC_NAME
            - MQCA_CLUS_CHL_NAME
            - MQCA_CLUSTER_DATE
            - MQCA_CLUSTER_NAME
            - MQCA_CLUSTER_NAMELIST
            - MQCA_CLUSTER_Q_MGR_NAME
            - MQCA_CLUSTER_TIME
            - MQCA_CREATION_DATE
            - MQCA_CREATION_TIME
            - MQCA_CUSTOM
            - MQCA_INITIATION_Q_NAME
            - MQCA_PROCESS_NAME
            - MQCA_Q_DESC
            - MQCA_Q_MGR_IDENTIFIER
            - MQCA_Q_NAME
            - MQCA_REMOTE_Q_MGR_NAME
            - MQCA_REMOTE_Q_NAME
            - MQCA_STORAGE_CLASS
            - MQCA_STREAM_QUEUE_NAME
            - MQCA_TPIPE_NAME
            - MQCA_TRIGGER_DATA
            - MQCA_XMIT_Q_NAME
            - MQIA_ACCOUNTING_Q
            - MQIA_BACKOUT_THRESHOLD
            - MQIA_BASE_TYPE
            - MQIA_CLUSTER_Q_TYPE
            - MQIA_CLWL_Q_PRIORITY
            - MQIA_CLWL_Q_RANK
            - MQIA_CLWL_USEQ
            - MQIA_CURRENT_Q_DEPTH
            - MQIA_DEF_BIND
            - MQIA_DEF_INPUT_OPEN_OPTION
            - MQIA_DEF_PERSISTENCE
            - MQIA_DEF_PRIORITY
            - MQIA_DEF_PUT_RESPONSE_TYPE
            - MQIA_DEF_READ_AHEAD
            - MQIA_DEFINITION_TYPE
            - MQIA_DIST_LISTS
            - MQIA_HARDEN_GET_BACKOUT
            - MQIA_INDEX_TYPE
            - MQIA_INHIBIT_GET
            - MQIA_INHIBIT_PUT
            - MQIA_MAX_MSG_LENGTH
            - MQIA_MAX_Q_DEPTH
            - MQIA_MEDIA_IMAGE_RECOVER_Q
            - MQIA_MONITORING_Q
            - MQIA_MSG_DELIVERY_SEQUENCE
            - MQIA_NPM_CLASS
            - MQIA_OPEN_INPUT_COUNT
            - MQIA_OPEN_OUTPUT_COUNT
            - MQIA_OTEL_PROPAGATION_CONTROL
            - MQIA_OTEL_TRACE
            - MQIA_PAGESET_ID
            - MQIA_PROPERTY_CONTROL
            - MQIA_Q_DEPTH_HIGH_EVENT
            - MQIA_Q_DEPTH_HIGH_LIMIT
            - MQIA_Q_DEPTH_LOW_EVENT
            - MQIA_Q_DEPTH_LOW_LIMIT
            - MQIA_Q_DEPTH_MAX_EVENT
            - MQIA_Q_SERVICE_INTERVAL
            - MQIA_Q_SERVICE_INTERVAL_EVENT
            - MQIA_Q_TYPE
            - MQIA_RETENTION_INTERVAL
            - MQIA_SCOPE
            - MQIA_SHAREABILITY
            - MQIA_STATISTICS_Q
            - MQIA_STREAM_QUEUE_QOS
            - MQIA_TRIGGER_CONTROL
            - MQIA_TRIGGER_DEPTH
            - MQIA_TRIGGER_MSG_PRIORITY
            - MQIA_TRIGGER_MTYPE
            - MQIA_USAGE
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
            - MQQSGD_SHARED
        - name: QType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQT_ALL
            - MQQT_LOCAL
            - MQQT_ALIAS
            - MQQT_REMOTE
            - MQQT_CLUSTER
            - MQQT_MODEL
        - name: StorageClass
          pcf_type: MQCFST
          type_hint: str
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
        - name: BackoutRequeueName
          pcf_type: MQCFST
          type_hint: str
        - name: BackoutThreshold
          pcf_type: MQCFIN
          type_hint: int
        - name: BaseQName
          pcf_type: MQCFST
          type_hint: str
        - name: CapExpiry
          pcf_type: MQCFIN
          type_hint: int
        - name: CFStructure
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterChannelName
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterDate
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterName
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterNamelist
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterQType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCQT_LOCAL_Q
            - MQCQT_ALIAS_Q
            - MQCQT_REMOTE_Q
            - MQCQT_Q_MGR_ALIAS
        - name: ClusterTime
          pcf_type: MQCFST
          type_hint: str
        - name: CLWLQueuePriority
          pcf_type: MQCFIN
          type_hint: int
        - name: CLWLQueueRank
          pcf_type: MQCFIN
          type_hint: int
        - name: CLWLUseQ
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCLWL_USEQ_AS_Q_MGR
            - MQCLWL_USEQ_ANY
            - MQCLWL_USEQ_LOCAL
        - name: CreationDate
          pcf_type: MQCFST
          type_hint: str
        - name: CreationTime
          pcf_type: MQCFST
          type_hint: str
        - name: CurrentQDepth
          pcf_type: MQCFIN
          type_hint: int
        - name: Custom
          pcf_type: MQCFST
          type_hint: str
        - name: DefaultPutResponse
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPRT_SYNC_RESPONSE
            - MQPRT_ASYNC_RESPONSE
        - name: DefBind
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQBND_BIND_ON_OPEN
            - MQBND_BIND_NOT_FIXED
            - MQBND_BIND_ON_GROUP
        - name: DefinitionType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQDT_PREDEFINED
            - MQQDT_PERMANENT_DYNAMIC
            - MQQDT_SHARED_DYNAMIC
            - MQQDT_TEMPORARY_DYNAMIC
        - name: DefInputOpenOption
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQOO_INPUT_EXCLUSIVE
            - MQOO_INPUT_SHARED
        - name: DefPersistence
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPER_PERSISTENT
            - MQPER_NOT_PERSISTENT
        - name: DefPriority
          pcf_type: MQCFIN
          type_hint: int
        - name: DefReadAhead
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQREADA_NO
            - MQREADA_YES
            - MQREADA_DISABLED
        - name: DistLists
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQDL_SUPPORTED
            - MQDL_NOT_SUPPORTED
        - name: HardenGetBackout
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQA_BACKOUT_HARDENED
            - MQQA_BACKOUT_NOT_HARDENED
        - name: ImageRecoverQueue
          pcf_type: MQCFST
          type_hint: str
          enum_values:
            - MQIMGRCOV_YES
            - MQIMGRCOV_NO
            - MQIMGRCOV_AS_Q_MGR
        - name: IndexType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQIT_NONE
            - MQIT_MSG_ID
            - MQIT_CORREL_ID
            - MQIT_MSG_TOKEN
            - MQIT_GROUP_ID
        - name: InhibitGet
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQA_GET_ALLOWED
            - MQQA_GET_INHIBITED
        - name: InhibitPut
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQA_PUT_ALLOWED
            - MQQA_PUT_INHIBITED
        - name: InitiationQName
          pcf_type: MQCFST
          type_hint: str
        - name: MaxMsgLength
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxQDepth
          pcf_type: MQCFIN
          type_hint: int
        - name: MsgDeliverySequence
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMDS_PRIORITY
            - MQMDS_FIFO
        - name: NonPersistentMessageClass
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQNPM_CLASS_NORMAL
            - MQNPM_CLASS_HIGH
        - name: OpenInputCount
          pcf_type: MQCFIN
          type_hint: int
        - name: OpenOutputCount
          pcf_type: MQCFIN
          type_hint: int
        - name: OTELPropagationControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQOTEL_PCTL_QMGR
            - MQOTEL_PCTL_MANUAL
            - MQOTEL_PCTL_AUTO
        - name: OTELTrace
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQOTEL_TRACE_QMGR
            - MQOTEL_TRACE_OFF
            - MQOTEL_TRACE_ON
        - name: PageSetID
          pcf_type: MQCFIN
          type_hint: int
        - name: ProcessName
          pcf_type: MQCFST
          type_hint: str
        - name: PropertyControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPROP_COMPATIBILITY
            - MQPROP_NONE
            - MQPROP_ALL
            - MQPROP_FORCE_MQRFH2
        - name: QDepthHighEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
        - name: QDepthHighLimit
          pcf_type: MQCFIN
          type_hint: int
        - name: QDepthLowEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
        - name: QDepthLowLimit
          pcf_type: MQCFIN
          type_hint: int
        - name: QDepthMaxEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
        - name: QDesc
          pcf_type: MQCFST
          type_hint: str
        - name: QMgrIdentifier
          pcf_type: MQCFST
          type_hint: str
        - name: QMgrName
          pcf_type: MQCFST
          type_hint: str
        - name: QName
          pcf_type: MQCFST
          type_hint: str
        - name: QServiceInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: QServiceIntervalEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSIE_HIGH
            - MQQSIE_OK
            - MQQSIE_NONE
        - name: QSGDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSGD_COPY
            - MQQSGD_GROUP
            - MQQSGD_Q_MGR
            - MQQSGD_SHARED
        - name: QType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQT_ALIAS
            - MQQT_CLUSTER
            - MQQT_LOCAL
            - MQQT_REMOTE
            - MQQT_MODEL
        - name: QueueAccounting
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_Q_MGR
            - MQMON_OFF
            - MQMON_ON
        - name: QueueMonitoring
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_OFF
            - MQMON_Q_MGR
            - MQMON_LOW
            - MQMON_MEDIUM
            - MQMON_HIGH
        - name: QueueStatistics
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_Q_MGR
            - MQMON_OFF
            - MQMON_ON
        - name: RemoteQMgrName
          pcf_type: MQCFST
          type_hint: str
        - name: RemoteQName
          pcf_type: MQCFST
          type_hint: str
        - name: RetentionInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: Scope
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSCO_Q_MGR
            - MQSCO_CELL
        - name: Shareability
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQA_SHAREABLE
            - MQQA_NOT_SHAREABLE
        - name: StorageClass
          pcf_type: MQCFST
          type_hint: str
        - name: StreamQ
          pcf_type: MQCFST
          type_hint: str
        - name: StreamQService
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQST_BEST_EFFORT
            - MQST_MUST_DUP
        - name: TpipeNames
          pcf_type: MQCFSL
          type_hint: str
        - name: TriggerControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQTC_OFF
            - MQTC_ON
        - name: TriggerData
          pcf_type: MQCFST
          type_hint: str
        - name: TriggerDepth
          pcf_type: MQCFIN
          type_hint: int
        - name: TriggerMsgPriority
          pcf_type: MQCFIN
          type_hint: int
        - name: TriggerType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQTT_NONE
            - MQTT_FIRST
            - MQTT_EVERY
            - MQTT_DEPTH
        - name: Usage
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQUS_NORMAL
            - MQUS_TRANSMISSION
        - name: XmitQName
          pcf_type: MQCFST
          type_hint: str
    notes:
      - display-queue-type-synonyms
      - qsgdisposition-returned-on-zos-only
  - mqsc:
      name: ALTER QREMOTE
      href: SSFKSJ_9.4.0/refadmin/q085330_.html
      positional_parameters:
        - (queue-name)
      input_parameters:
        - CAPEXPRY
        - CLUSNL
        - CLUSTER
        - CLWLPRTY
        - CLWLRANK
        - CMDSCOPE
        - CUSTOM
        - DEFBIND
        - DEFPRESP
        - DEFPRTY
        - DEFPSIST
        - DESCR
        - FORCE
        - LIKE
        - OTELPCTL
        - OTELTRAC
        - PUT
        - QSGDISP
        - RNAME
        - RQMNAME
        - SCOPE
        - XMITQ
      output_parameters:
        []
      section_sources:
        Parameter descriptions for ALTER queues:
          - CAPEXPRY
          - CLUSNL
          - CLUSTER
          - CLWLPRTY
          - CLWLRANK
          - CMDSCOPE
          - CUSTOM
          - DEFBIND
          - DEFPRESP
          - DEFPRTY
          - DEFPSIST
          - DESCR
          - FORCE
          - LIKE
          - OTELPCTL
          - OTELTRAC
          - PUT
          - QSGDISP
          - RNAME
          - RQMNAME
          - SCOPE
          - XMITQ
    pcf:
      command: MQCMD_CHANGE_Q
      request_href: SSFKSJ_9.4.0/refadmin/q086990_.html
      response_href: null
      request_parameters:
        - name: QName
          pcf_type: MQCFST
          type_hint: str
        - name: QType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQT_ALIAS
            - MQQT_LOCAL
            - MQQT_REMOTE
            - MQQT_MODEL
        - name: BackoutRequeueName
          pcf_type: MQCFST
          type_hint: str
        - name: BackoutThreshold
          pcf_type: MQCFIN
          type_hint: int
        - name: BaseObjectName
          pcf_type: MQCFST
          type_hint: str
        - name: BaseQName
          pcf_type: MQCFST
          type_hint: str
        - name: CapExpiry
          pcf_type: MQCFIN
          type_hint: int
        - name: CFStructure
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterChannelName
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterName
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterNamelist
          pcf_type: MQCFST
          type_hint: str
        - name: CLWLQueuePriority
          pcf_type: MQCFIN
          type_hint: int
        - name: CLWLQueueRank
          pcf_type: MQCFIN
          type_hint: int
        - name: CLWLUseQ
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCLWL_USEQ_AS_Q_MGR
            - MQCLWL_USEQ_ANY
            - MQCLWL_USEQ_LOCAL
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: Custom
          pcf_type: MQCFST
          type_hint: str
        - name: DefaultPutResponse
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPRT_SYNC_RESPONSE
            - MQPRT_ASYNC_RESPONSE
        - name: DefBind
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQBND_BIND_ON_OPEN
            - MQBND_BIND_NOT_FIXED
            - MQBND_BIND_ON_GROUP
        - name: DefinitionType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQDT_PERMANENT_DYNAMIC
            - MQQDT_SHARED_DYNAMIC
            - MQQDT_TEMPORARY_DYNAMIC
        - name: DefInputOpenOption
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQOO_INPUT_EXCLUSIVE
            - MQOO_INPUT_SHARED
        - name: DefPersistence
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPER_PERSISTENT
            - MQPER_NOT_PERSISTENT
        - name: DefPriority
          pcf_type: MQCFIN
          type_hint: int
        - name: DefReadAhead
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQREADA_NO
            - MQREADA_YES
            - MQREADA_DISABLED
        - name: DistLists
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQDL_SUPPORTED
            - MQDL_NOT_SUPPORTED
        - name: Force
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQFC_YES
            - MQFC_NO
        - name: HardenGetBackout
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQA_BACKOUT_HARDENED
            - MQQA_BACKOUT_NOT_HARDENED
        - name: ImageRecoverQueue
          pcf_type: MQCFST
          type_hint: str
          enum_values:
            - MQIMGRCOV_YES
            - MQIMGRCOV_NO
            - MQIMGRCOV_AS_Q_MGR
        - name: IndexType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQIT_NONE
            - MQIT_MSG_ID
            - MQIT_CORREL_ID
            - MQIT_MSG_TOKEN
            - MQIT_GROUP_ID
        - name: InhibitGet
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQA_GET_ALLOWED
            - MQQA_GET_INHIBITED
        - name: InhibitPut
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQA_PUT_ALLOWED
            - MQQA_PUT_INHIBITED
        - name: InitiationQName
          pcf_type: MQCFST
          type_hint: str
        - name: MaxMsgLength
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxQDepth
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxQFileSize
          pcf_type: MQCFIN
          type_hint: int
        - name: MsgDeliverySequence
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMDS_PRIORITY
            - MQMDS_FIFO
        - name: NonPersistentMessageClass
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQNPM_CLASS_NORMAL
            - MQNPM_CLASS_HIGH
        - name: OTELPropagationControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQOTEL_PCTL_QMGR
            - MQOTEL_PCTL_MANUAL
            - MQOTEL_PCTL_AUTO
        - name: OTELTrace
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQOTEL_TRACE_QMGR
            - MQOTEL_TRACE_OFF
            - MQOTEL_TRACE_ON
        - name: ProcessName
          pcf_type: MQCFST
          type_hint: str
        - name: PropertyControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPROP_COMPATIBILITY
            - MQPROP_NONE
            - MQPROP_ALL
            - MQPROP_FORCE_MQRFH2
            - MQPROP_V6COMPAT
        - name: QDepthHighEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
        - name: QDepthHighLimit
          pcf_type: MQCFIN
          type_hint: int
        - name: QDepthLowEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
        - name: QDepthLowLimit
          pcf_type: MQCFIN
          type_hint: int
        - name: QDepthMaxEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
        - name: QDesc
          pcf_type: MQCFST
          type_hint: str
        - name: QServiceInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: QServiceIntervalEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSIE_HIGH
            - MQQSIE_OK
            - MQQSIE_NONE
        - name: QSGDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSGD_COPY
            - MQQSGD_Q_MGR
            - MQQSGD_GROUP
            - MQQSGD_PRIVATE
            - MQQSGD_SHARED
        - name: QueueAccounting
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_Q_MGR
            - MQMON_OFF
            - MQMON_ON
        - name: QueueMonitoring
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_OFF
            - MQMON_Q_MGR
            - MQMON_LOW
            - MQMON_MEDIUM
            - MQMON_HIGH
        - name: QueueStatistics
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_Q_MGR
            - MQMON_OFF
            - MQMON_ON
        - name: RemoteQMgrName
          pcf_type: MQCFST
          type_hint: str
        - name: RemoteQName
          pcf_type: MQCFST
          type_hint: str
        - name: RetentionInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: Scope
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSCO_Q_MGR
            - MQSCO_CELL
        - name: Shareability
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQA_SHAREABLE
            - MQQA_NOT_SHAREABLE
        - name: StorageClass
          pcf_type: MQCFST
          type_hint: str
        - name: StreamQ
          pcf_type: MQCFST
          type_hint: str
        - name: StreamQService
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQST_BEST_EFFORT
            - MQST_MUST_DUP
        - name: TargetType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQOT_Q
            - MQOT_TOPIC
        - name: TriggerControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQTC_OFF
            - MQTC_ON
        - name: TriggerData
          pcf_type: MQCFST
          type_hint: str
        - name: TriggerDepth
          pcf_type: MQCFIN
          type_hint: int
        - name: TriggerMsgPriority
          pcf_type: MQCFIN
          type_hint: int
        - name: TriggerType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQTT_NONE
            - MQTT_EVERY
            - MQTT_FIRST
            - MQTT_DEPTH
        - name: Usage
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQUS_NORMAL
            - MQUS_TRANSMISSION
        - name: XmitQName
          pcf_type: MQCFST
          type_hint: str
      response_parameters:
        []
    notes:
      - change-queue-excludes-copy-only-parameters
      - change-queue-excludes-replace-parameter
  - mqsc:
      name: DEFINE QREMOTE
      href: SSFKSJ_9.4.0/refadmin/q085690_.html
      positional_parameters:
        - (queue-name)
      input_parameters:
        - CAPEXPRY
        - CLUSNL
        - CLUSTER
        - CLWLPRTY
        - CLWLRANK
        - CMDSCOPE
        - CUSTOM
        - DEFBIND
        - DEFPRESP
        - DEFPRTY
        - DEFPSIST
        - DESCR
        - FORCE
        - LIKE
        - NOREPLACE
        - OTELPCTL
        - OTELTRAC
        - PUT
        - QSGDISP
        - REPLACE
        - RNAME
        - RQMNAME
        - SCOPE
        - XMITQ
      output_parameters:
        []
      section_sources:
        Parameter descriptions for DEFINE queues:
          - CAPEXPRY
          - CLUSNL
          - CLUSTER
          - CLWLPRTY
          - CLWLRANK
          - CMDSCOPE
          - CUSTOM
          - DEFBIND
          - DEFPRESP
          - DEFPRTY
          - DEFPSIST
          - DESCR
          - FORCE
          - LIKE
          - NOREPLACE
          - OTELPCTL
          - OTELTRAC
          - PUT
          - QSGDISP
          - REPLACE
          - RNAME
          - RQMNAME
          - SCOPE
          - XMITQ
    pcf:
      command: MQCMD_CREATE_Q
      request_href: SSFKSJ_9.4.0/refadmin/q086990_.html
      response_href: null
      request_parameters:
        - name: QName
          pcf_type: MQCFST
          type_hint: str
        - name: QType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQT_ALIAS
            - MQQT_LOCAL
            - MQQT_REMOTE
            - MQQT_MODEL
        - name: BackoutRequeueName
          pcf_type: MQCFST
          type_hint: str
        - name: BackoutThreshold
          pcf_type: MQCFIN
          type_hint: int
        - name: BaseObjectName
          pcf_type: MQCFST
          type_hint: str
        - name: BaseQName
          pcf_type: MQCFST
          type_hint: str
        - name: CapExpiry
          pcf_type: MQCFIN
          type_hint: int
        - name: CFStructure
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterChannelName
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterName
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterNamelist
          pcf_type: MQCFST
          type_hint: str
        - name: CLWLQueuePriority
          pcf_type: MQCFIN
          type_hint: int
        - name: CLWLQueueRank
          pcf_type: MQCFIN
          type_hint: int
        - name: CLWLUseQ
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCLWL_USEQ_AS_Q_MGR
            - MQCLWL_USEQ_ANY
            - MQCLWL_USEQ_LOCAL
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: Custom
          pcf_type: MQCFST
          type_hint: str
        - name: DefaultPutResponse
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPRT_SYNC_RESPONSE
            - MQPRT_ASYNC_RESPONSE
        - name: DefBind
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQBND_BIND_ON_OPEN
            - MQBND_BIND_NOT_FIXED
            - MQBND_BIND_ON_GROUP
        - name: DefinitionType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQDT_PERMANENT_DYNAMIC
            - MQQDT_SHARED_DYNAMIC
            - MQQDT_TEMPORARY_DYNAMIC
        - name: DefInputOpenOption
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQOO_INPUT_EXCLUSIVE
            - MQOO_INPUT_SHARED
        - name: DefPersistence
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPER_PERSISTENT
            - MQPER_NOT_PERSISTENT
        - name: DefPriority
          pcf_type: MQCFIN
          type_hint: int
        - name: DefReadAhead
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQREADA_NO
            - MQREADA_YES
            - MQREADA_DISABLED
        - name: DistLists
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQDL_SUPPORTED
            - MQDL_NOT_SUPPORTED
        - name: Force
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQFC_YES
            - MQFC_NO
        - name: HardenGetBackout
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQA_BACKOUT_HARDENED
            - MQQA_BACKOUT_NOT_HARDENED
        - name: ImageRecoverQueue
          pcf_type: MQCFST
          type_hint: str
          enum_values:
            - MQIMGRCOV_YES
            - MQIMGRCOV_NO
            - MQIMGRCOV_AS_Q_MGR
        - name: IndexType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQIT_NONE
            - MQIT_MSG_ID
            - MQIT_CORREL_ID
            - MQIT_MSG_TOKEN
            - MQIT_GROUP_ID
        - name: InhibitGet
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQA_GET_ALLOWED
            - MQQA_GET_INHIBITED
        - name: InhibitPut
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQA_PUT_ALLOWED
            - MQQA_PUT_INHIBITED
        - name: InitiationQName
          pcf_type: MQCFST
          type_hint: str
        - name: MaxMsgLength
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxQDepth
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxQFileSize
          pcf_type: MQCFIN
          type_hint: int
        - name: MsgDeliverySequence
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMDS_PRIORITY
            - MQMDS_FIFO
        - name: NonPersistentMessageClass
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQNPM_CLASS_NORMAL
            - MQNPM_CLASS_HIGH
        - name: OTELPropagationControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQOTEL_PCTL_QMGR
            - MQOTEL_PCTL_MANUAL
            - MQOTEL_PCTL_AUTO
        - name: OTELTrace
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQOTEL_TRACE_QMGR
            - MQOTEL_TRACE_OFF
            - MQOTEL_TRACE_ON
        - name: ProcessName
          pcf_type: MQCFST
          type_hint: str
        - name: PropertyControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPROP_COMPATIBILITY
            - MQPROP_NONE
            - MQPROP_ALL
            - MQPROP_FORCE_MQRFH2
            - MQPROP_V6COMPAT
        - name: QDepthHighEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
        - name: QDepthHighLimit
          pcf_type: MQCFIN
          type_hint: int
        - name: QDepthLowEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
        - name: QDepthLowLimit
          pcf_type: MQCFIN
          type_hint: int
        - name: QDepthMaxEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
        - name: QDesc
          pcf_type: MQCFST
          type_hint: str
        - name: QServiceInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: QServiceIntervalEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSIE_HIGH
            - MQQSIE_OK
            - MQQSIE_NONE
        - name: QSGDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSGD_COPY
            - MQQSGD_Q_MGR
            - MQQSGD_GROUP
            - MQQSGD_PRIVATE
            - MQQSGD_SHARED
        - name: QueueAccounting
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_Q_MGR
            - MQMON_OFF
            - MQMON_ON
        - name: QueueMonitoring
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_OFF
            - MQMON_Q_MGR
            - MQMON_LOW
            - MQMON_MEDIUM
            - MQMON_HIGH
        - name: QueueStatistics
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_Q_MGR
            - MQMON_OFF
            - MQMON_ON
        - name: RemoteQMgrName
          pcf_type: MQCFST
          type_hint: str
        - name: RemoteQName
          pcf_type: MQCFST
          type_hint: str
        - name: Replace
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQRP_YES
            - MQRP_NO
        - name: RetentionInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: Scope
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSCO_Q_MGR
            - MQSCO_CELL
        - name: Shareability
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQA_SHAREABLE
            - MQQA_NOT_SHAREABLE
        - name: StorageClass
          pcf_type: MQCFST
          type_hint: str
        - name: StreamQ
          pcf_type: MQCFST
          type_hint: str
        - name: StreamQService
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQST_BEST_EFFORT
            - MQST_MUST_DUP
        - name: TargetType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQOT_Q
            - MQOT_TOPIC
        - name: TriggerControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQTC_OFF
            - MQTC_ON
        - name: TriggerData
          pcf_type: MQCFST
          type_hint: str
        - name: TriggerDepth
          pcf_type: MQCFIN
          type_hint: int
        - name: TriggerMsgPriority
          pcf_type: MQCFIN
          type_hint: int
        - name: TriggerType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQTT_NONE
            - MQTT_EVERY
            - MQTT_FIRST
            - MQTT_DEPTH
        - name: Usage
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQUS_NORMAL
            - MQUS_TRANSMISSION
        - name: XmitQName
          pcf_type: MQCFST
          type_hint: str
      response_parameters:
        []
    notes:
      - create-queue-excludes-copy-only-parameters
  - mqsc:
      name: DELETE QREMOTE
      href: SSFKSJ_9.4.0/refadmin/q085890_.html
      positional_parameters:
        - (q-name)
      input_parameters:
        - AUTHREC
        - CMDSCOPE
        - IGNSTATE
        - QSGDISP
      output_parameters:
        []
      section_sources:
        Parameter descriptions for DELETE queues:
          - AUTHREC
          - CMDSCOPE
          - IGNSTATE
          - QSGDISP
    pcf:
      command: MQCMD_DELETE_Q
      request_href: SSFKSJ_9.4.0/refadmin/q087180_.html
      response_href: SSFKSJ_9.4.0/refadmin/q087180_.html
      request_parameters:
        - name: QName
          pcf_type: MQCFST
          type_hint: str
        - name: Authrec
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQRAR_YES
            - MQRAR_NO
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: Purge
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPO_YES
            - MQPO_NO
        - name: QSGDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSGD_COPY
            - MQQSGD_GROUP
            - MQQSGD_Q_MGR
            - MQQSGD_SHARED
        - name: QType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQT_ALIAS
            - MQQT_LOCAL
            - MQQT_REMOTE
            - MQQT_MODEL
        - name: IgnoreState
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQIS_NO
            - MQIS_YES
      response_parameters:
        []
    notes:
      - ignore-state-type-inferred-from-mqsc-ignstate
      - ignore-state-name-normalized
  - mqsc:
      name: DISPLAY QREMOTE
      href: SSFKSJ_9.4.0/refadmin/q086270_.html
      positional_parameters:
        - (generic-qname)
      input_parameters:
        - WHERE
        - ALL
        - CFSTRUCT
        - CLUSINFO
        - CLUSNL
        - CLUSTER
        - CMDSCOPE
        - PSID
        - QSGDISP
        - STGCLASS
        - TARGTYPE
      output_parameters:
        - ALTDATE
        - ALTTIME
        - CAPEXPRY
        - CLUSNL
        - CLUSTER
        - CLWLPRTY
        - CLWLRANK
        - CUSTOM
        - DEFBIND
        - DEFPRESP
        - DEFPRTY
        - DEFPSIST
        - DESCR
        - OTELPCTL
        - OTELTRAC
        - PUT
        - QSGDISP
        - QTYPE
        - RNAME
        - RQMNAME
        - SCOPE
        - XMITQ
      section_sources:
        Parameter descriptions for DISPLAY QUEUE:
          - WHERE
          - ALL
          - CFSTRUCT
          - CLUSINFO
          - CLUSNL
          - CLUSTER
          - CMDSCOPE
          - PSID
          - QSGDISP
          - STGCLASS
          - TARGTYPE
        Requested parameters:
          - ALTDATE
          - ALTTIME
          - CAPEXPRY
          - CLUSNL
          - CLUSTER
          - CLWLPRTY
          - CLWLRANK
          - CUSTOM
          - DEFBIND
          - DEFPRESP
          - DEFPRTY
          - DEFPSIST
          - DESCR
          - OTELPCTL
          - OTELTRAC
          - PUT
          - QSGDISP
          - QTYPE
          - RNAME
          - RQMNAME
          - SCOPE
          - XMITQ
    pcf:
      command: MQCMD_INQUIRE_Q
      request_href: SSFKSJ_9.4.0/refadmin/q087800_.html
      response_href: SSFKSJ_9.4.0/refadmin/q087810_.html
      request_parameters:
        - name: QName
          pcf_type: MQCFST
          type_hint: str
        - name: CapExpiry
          pcf_type: MQCFIN
          type_hint: int
        - name: CFStructure
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterInfo
          pcf_type: MQCFIN
          type_hint: int
        - name: ClusterName
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterNamelist
          pcf_type: MQCFST
          type_hint: str
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: IntegerFilterCommand
          pcf_type: MQCFIF
          type_hint: null
        - name: PageSetID
          pcf_type: MQCFIN
          type_hint: int
        - name: QAttrs
          pcf_type: MQCFIL
          type_hint: int
          enum_values:
            - MQIACF_ALL
            - MQCA_ALTERATION_DATE
            - MQCA_ALTERATION_TIME
            - MQCA_BACKOUT_REQ_Q_NAME
            - MQCA_BASE_NAME
            - MQCA_CF_STRUC_NAME
            - MQCA_CLUS_CHL_NAME
            - MQCA_CLUSTER_DATE
            - MQCA_CLUSTER_NAME
            - MQCA_CLUSTER_NAMELIST
            - MQCA_CLUSTER_Q_MGR_NAME
            - MQCA_CLUSTER_TIME
            - MQCA_CREATION_DATE
            - MQCA_CREATION_TIME
            - MQCA_CUSTOM
            - MQCA_INITIATION_Q_NAME
            - MQCA_PROCESS_NAME
            - MQCA_Q_DESC
            - MQCA_Q_MGR_IDENTIFIER
            - MQCA_Q_NAME
            - MQCA_REMOTE_Q_MGR_NAME
            - MQCA_REMOTE_Q_NAME
            - MQCA_STORAGE_CLASS
            - MQCA_STREAM_QUEUE_NAME
            - MQCA_TPIPE_NAME
            - MQCA_TRIGGER_DATA
            - MQCA_XMIT_Q_NAME
            - MQIA_ACCOUNTING_Q
            - MQIA_BACKOUT_THRESHOLD
            - MQIA_BASE_TYPE
            - MQIA_CLUSTER_Q_TYPE
            - MQIA_CLWL_Q_PRIORITY
            - MQIA_CLWL_Q_RANK
            - MQIA_CLWL_USEQ
            - MQIA_CURRENT_Q_DEPTH
            - MQIA_DEF_BIND
            - MQIA_DEF_INPUT_OPEN_OPTION
            - MQIA_DEF_PERSISTENCE
            - MQIA_DEF_PRIORITY
            - MQIA_DEF_PUT_RESPONSE_TYPE
            - MQIA_DEF_READ_AHEAD
            - MQIA_DEFINITION_TYPE
            - MQIA_DIST_LISTS
            - MQIA_HARDEN_GET_BACKOUT
            - MQIA_INDEX_TYPE
            - MQIA_INHIBIT_GET
            - MQIA_INHIBIT_PUT
            - MQIA_MAX_MSG_LENGTH
            - MQIA_MAX_Q_DEPTH
            - MQIA_MEDIA_IMAGE_RECOVER_Q
            - MQIA_MONITORING_Q
            - MQIA_MSG_DELIVERY_SEQUENCE
            - MQIA_NPM_CLASS
            - MQIA_OPEN_INPUT_COUNT
            - MQIA_OPEN_OUTPUT_COUNT
            - MQIA_OTEL_PROPAGATION_CONTROL
            - MQIA_OTEL_TRACE
            - MQIA_PAGESET_ID
            - MQIA_PROPERTY_CONTROL
            - MQIA_Q_DEPTH_HIGH_EVENT
            - MQIA_Q_DEPTH_HIGH_LIMIT
            - MQIA_Q_DEPTH_LOW_EVENT
            - MQIA_Q_DEPTH_LOW_LIMIT
            - MQIA_Q_DEPTH_MAX_EVENT
            - MQIA_Q_SERVICE_INTERVAL
            - MQIA_Q_SERVICE_INTERVAL_EVENT
            - MQIA_Q_TYPE
            - MQIA_RETENTION_INTERVAL
            - MQIA_SCOPE
            - MQIA_SHAREABILITY
            - MQIA_STATISTICS_Q
            - MQIA_STREAM_QUEUE_QOS
            - MQIA_TRIGGER_CONTROL
            - MQIA_TRIGGER_DEPTH
            - MQIA_TRIGGER_MSG_PRIORITY
            - MQIA_TRIGGER_MTYPE
            - MQIA_USAGE
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
            - MQQSGD_SHARED
        - name: QType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQT_ALL
            - MQQT_LOCAL
            - MQQT_ALIAS
            - MQQT_REMOTE
            - MQQT_CLUSTER
            - MQQT_MODEL
        - name: StorageClass
          pcf_type: MQCFST
          type_hint: str
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
        - name: BackoutRequeueName
          pcf_type: MQCFST
          type_hint: str
        - name: BackoutThreshold
          pcf_type: MQCFIN
          type_hint: int
        - name: BaseQName
          pcf_type: MQCFST
          type_hint: str
        - name: CapExpiry
          pcf_type: MQCFIN
          type_hint: int
        - name: CFStructure
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterChannelName
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterDate
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterName
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterNamelist
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterQType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCQT_LOCAL_Q
            - MQCQT_ALIAS_Q
            - MQCQT_REMOTE_Q
            - MQCQT_Q_MGR_ALIAS
        - name: ClusterTime
          pcf_type: MQCFST
          type_hint: str
        - name: CLWLQueuePriority
          pcf_type: MQCFIN
          type_hint: int
        - name: CLWLQueueRank
          pcf_type: MQCFIN
          type_hint: int
        - name: CLWLUseQ
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCLWL_USEQ_AS_Q_MGR
            - MQCLWL_USEQ_ANY
            - MQCLWL_USEQ_LOCAL
        - name: CreationDate
          pcf_type: MQCFST
          type_hint: str
        - name: CreationTime
          pcf_type: MQCFST
          type_hint: str
        - name: CurrentQDepth
          pcf_type: MQCFIN
          type_hint: int
        - name: Custom
          pcf_type: MQCFST
          type_hint: str
        - name: DefaultPutResponse
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPRT_SYNC_RESPONSE
            - MQPRT_ASYNC_RESPONSE
        - name: DefBind
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQBND_BIND_ON_OPEN
            - MQBND_BIND_NOT_FIXED
            - MQBND_BIND_ON_GROUP
        - name: DefinitionType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQDT_PREDEFINED
            - MQQDT_PERMANENT_DYNAMIC
            - MQQDT_SHARED_DYNAMIC
            - MQQDT_TEMPORARY_DYNAMIC
        - name: DefInputOpenOption
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQOO_INPUT_EXCLUSIVE
            - MQOO_INPUT_SHARED
        - name: DefPersistence
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPER_PERSISTENT
            - MQPER_NOT_PERSISTENT
        - name: DefPriority
          pcf_type: MQCFIN
          type_hint: int
        - name: DefReadAhead
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQREADA_NO
            - MQREADA_YES
            - MQREADA_DISABLED
        - name: DistLists
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQDL_SUPPORTED
            - MQDL_NOT_SUPPORTED
        - name: HardenGetBackout
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQA_BACKOUT_HARDENED
            - MQQA_BACKOUT_NOT_HARDENED
        - name: ImageRecoverQueue
          pcf_type: MQCFST
          type_hint: str
          enum_values:
            - MQIMGRCOV_YES
            - MQIMGRCOV_NO
            - MQIMGRCOV_AS_Q_MGR
        - name: IndexType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQIT_NONE
            - MQIT_MSG_ID
            - MQIT_CORREL_ID
            - MQIT_MSG_TOKEN
            - MQIT_GROUP_ID
        - name: InhibitGet
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQA_GET_ALLOWED
            - MQQA_GET_INHIBITED
        - name: InhibitPut
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQA_PUT_ALLOWED
            - MQQA_PUT_INHIBITED
        - name: InitiationQName
          pcf_type: MQCFST
          type_hint: str
        - name: MaxMsgLength
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxQDepth
          pcf_type: MQCFIN
          type_hint: int
        - name: MsgDeliverySequence
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMDS_PRIORITY
            - MQMDS_FIFO
        - name: NonPersistentMessageClass
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQNPM_CLASS_NORMAL
            - MQNPM_CLASS_HIGH
        - name: OpenInputCount
          pcf_type: MQCFIN
          type_hint: int
        - name: OpenOutputCount
          pcf_type: MQCFIN
          type_hint: int
        - name: OTELPropagationControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQOTEL_PCTL_QMGR
            - MQOTEL_PCTL_MANUAL
            - MQOTEL_PCTL_AUTO
        - name: OTELTrace
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQOTEL_TRACE_QMGR
            - MQOTEL_TRACE_OFF
            - MQOTEL_TRACE_ON
        - name: PageSetID
          pcf_type: MQCFIN
          type_hint: int
        - name: ProcessName
          pcf_type: MQCFST
          type_hint: str
        - name: PropertyControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPROP_COMPATIBILITY
            - MQPROP_NONE
            - MQPROP_ALL
            - MQPROP_FORCE_MQRFH2
        - name: QDepthHighEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
        - name: QDepthHighLimit
          pcf_type: MQCFIN
          type_hint: int
        - name: QDepthLowEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
        - name: QDepthLowLimit
          pcf_type: MQCFIN
          type_hint: int
        - name: QDepthMaxEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
        - name: QDesc
          pcf_type: MQCFST
          type_hint: str
        - name: QMgrIdentifier
          pcf_type: MQCFST
          type_hint: str
        - name: QMgrName
          pcf_type: MQCFST
          type_hint: str
        - name: QName
          pcf_type: MQCFST
          type_hint: str
        - name: QServiceInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: QServiceIntervalEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSIE_HIGH
            - MQQSIE_OK
            - MQQSIE_NONE
        - name: QSGDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSGD_COPY
            - MQQSGD_GROUP
            - MQQSGD_Q_MGR
            - MQQSGD_SHARED
        - name: QType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQT_ALIAS
            - MQQT_CLUSTER
            - MQQT_LOCAL
            - MQQT_REMOTE
            - MQQT_MODEL
        - name: QueueAccounting
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_Q_MGR
            - MQMON_OFF
            - MQMON_ON
        - name: QueueMonitoring
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_OFF
            - MQMON_Q_MGR
            - MQMON_LOW
            - MQMON_MEDIUM
            - MQMON_HIGH
        - name: QueueStatistics
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_Q_MGR
            - MQMON_OFF
            - MQMON_ON
        - name: RemoteQMgrName
          pcf_type: MQCFST
          type_hint: str
        - name: RemoteQName
          pcf_type: MQCFST
          type_hint: str
        - name: RetentionInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: Scope
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSCO_Q_MGR
            - MQSCO_CELL
        - name: Shareability
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQA_SHAREABLE
            - MQQA_NOT_SHAREABLE
        - name: StorageClass
          pcf_type: MQCFST
          type_hint: str
        - name: StreamQ
          pcf_type: MQCFST
          type_hint: str
        - name: StreamQService
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQST_BEST_EFFORT
            - MQST_MUST_DUP
        - name: TpipeNames
          pcf_type: MQCFSL
          type_hint: str
        - name: TriggerControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQTC_OFF
            - MQTC_ON
        - name: TriggerData
          pcf_type: MQCFST
          type_hint: str
        - name: TriggerDepth
          pcf_type: MQCFIN
          type_hint: int
        - name: TriggerMsgPriority
          pcf_type: MQCFIN
          type_hint: int
        - name: TriggerType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQTT_NONE
            - MQTT_FIRST
            - MQTT_EVERY
            - MQTT_DEPTH
        - name: Usage
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQUS_NORMAL
            - MQUS_TRANSMISSION
        - name: XmitQName
          pcf_type: MQCFST
          type_hint: str
    notes:
      - display-queue-type-synonyms
      - qsgdisposition-returned-on-zos-only
```

## Output-parameter refresh

```yaml
version: 1
generated_at: 2026-02-02T19:46:59Z
commands:
  - name: DISPLAY QSTATUS
    output_parameters:
      - APPLDESC
      - APPLTAG
      - APPLTYPE
      - ASID
      - ASTATE
      - BROWSE
      - CHANNEL
      - CONNAME
      - CURDEPTH
      - CURFSIZE
      - CURMAXFS
      - EXTURID
      - HSTATE
      - INPUT
      - INQUIRE
      - IPPROCS
      - LGETDATE
      - LGETTIME
      - LPUTDATE
      - LPUTTIME
      - MAXFSIZE
      - MEDIALOG
      - MONITOR
      - MONQ
      - MSGAGE
      - OFF
      - OPPROCS
      - OUTPUT
      - PID
      - PSBNAME
      - PSTID
      - QMURID
      - QSGDISP
      - QTIME
      - SET
      - TASKNO
      - TID
      - TRANSID
      - TYPE
      - UNCOM
      - URID
      - URTYPE
      - USERID
  - name: DISPLAY QUEUE
    output_parameters:
      - ACCTQ
      - ALL
      - ALTDATE
      - ALTTIME
      - BOQNAME
      - BOTHRESH
      - CAPEXPRY
      - CFSTRUCT
      - CLCHNAME
      - CLUSDATE
      - CLUSNL
      - CLUSQMGR
      - CLUSQT
      - CLUSTER
      - CLUSTIME
      - CLWLPRTY
      - CLWLRANK
      - CLWLUSEQ
      - COMPAT
      - CRDATE
      - CRTIME
      - CURDEPTH
      - CUSTOM
      - DEFBIND
      - DEFPRESP
      - DEFPRTY
      - DEFPSIST
      - DEFREADA
      - DEFSOPT
      - DEFTYPE
      - DESCR
      - DISTL
      - FORCE
      - GET
      - HARDENBO
      - IMGRCOVQ
      - INDXTYPE
      - INITQ
      - IPPROCS
      - MAXDEPTH
      - MAXFSIZE
      - MAXMSGL
      - MONQ
      - MQPMO
      - MSGDLVSQ
      - NONE
      - NPMCLASS
      - OPPROCS
      - OTELPCTL
      - OTELTRAC
      - PAGEVAL
      - PROCESS
      - PROPCTL
      - PSID
      - PUT
      - QALIAS
      - QDEPTHHI
      - QDEPTHLO
      - QDPHIEV
      - QDPLOEV
      - QDPMAXEV
      - QLOCAL
      - QMGR
      - QMID
      - QREMOTE
      - QSGDISP
      - QSVCIEV
      - QSVCINT
      - QTYPE
      - RETINTVL
      - RNAME
      - RQMNAME
      - SCOPE
      - SHARE
      - SQGETTMR
      - STATQ
      - STGCLASS
      - STREAMQ
      - STRMQOS
      - TARGET
      - TARGTYPE
      - TPIPE
      - TRIGDATA
      - TRIGDPTH
      - TRIGGER
      - TRIGMPRI
      - TRIGTYPE
      - USAGE
      - XMITQ
```
