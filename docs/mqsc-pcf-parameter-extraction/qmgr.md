# MQSC to PCF parameter extraction: QMGR

## Table of Contents
- [Purpose](#purpose)
- [First-run extraction](#first-run-extraction)

## Purpose
Collect MQSC and PCF parameter mappings for qmgr commands, split from the first-run extraction to keep each qualifier readable.

## First-run extraction
```yaml
version: 1
generated_at: 2026-01-11T23:40:29Z
commands:
  - mqsc:
      name: ALTER QMGR
      href: SSFKSJ_9.4.0/refadmin/q085320_.html
      positional_parameters:
        - 1 - 999 999 999
        - Specific_user_ID
        - clustername
        - integer
        - nlname
        - parentname
        - qmgr-name
        - string
      input_parameters:
        - FORCE
      output_parameters: []
      section_sources:
        'Parameter descriptions for ALTER QMGR':
          - FORCE
        'Queue manager parameters':
          - ACCTCONO
          - ACCTINT
          - ACCTMQI
          - ACCTQ
          - ACTCHL
          - ACTIVREC
          - ACTVCONO
          - ACTVTRC
          - ADOPTCHK
          - ADOPTMCA
          - AUTHEVSC
          - AUTHOREV
          - BRIDGEEV
          - CCSID
          - CERTLABL
          - CERTQSGL
          - CERTVPOL
          - CFCONLOS
          - CHAD
          - CHADEV
          - CHADEXIT
          - CHIADAPS
          - CHIDISPS
          - CHISERVP
          - CHLAUTH
          - CHLEV
          - CLWLDATA
          - CLWLEXIT
          - CLWLLEN
          - CLWLMRUC
          - CLWLUSEQ
          - CMDEV
          - CMDSCOPE
          - CONFIGEV
          - CONNAUTH
          - CUSTOM
          - DEADQ
          - DEFCLXQ
          - DEFXMITQ
          - DESCR
          - DNSGROUP
          - DNSWLM
          - EXPRYINT
          - GROUPUR
          - IGQ
          - IGQAUT
          - IGQUSER
          - IMGINTVL
          - IMGLOGLN
          - IMGRCOVO
          - IMGRCOVQ
          - IMGSCHED
          - INHIBTEV
          - INITKEY
          - IPADDRV
          - KEYRPWD
          - LOCALEV
          - LOGGEREV
          - LSTRTMR
          - LU62ARM
          - LU62CHL
          - LUGROUP
          - LUNAME
          - MARKINT
          - MAXCHL
          - MAXHANDS
          - MAXMSGL
          - MAXPROPL
          - MAXUMSGS
          - MONACLS
          - MONCHL
          - MONQ
          - OPORTMAX
          - OPORTMIN
          - OTELPCTL
          - OTELTRAC
          - PARENT
          - PERFMEV
          - PSCLUS
          - PSMODE
          - PSNPMSG
          - PSNPRES
          - PSRTYCNT
          - PSSYNCPT
          - RCVTIME
          - RCVTMIN
          - RCVTTYPE
          - REMOTEEV
          - REPOS
          - REPOSNL
          - REVDNS
          - ROUTEREC
          - SCHINIT
          - SCMDSERV
          - SCYCASE
          - SQQMNAME
          - SSLCRLNL
          - SSLCRYP
          - SSLEV
          - SSLFIPS
          - SSLKEYR
          - SSLRKEYC
          - SSLTASKS
          - STATACLS
          - STATCHL
          - STATINT
          - STATMQI
          - STATQ
          - STRSTPEV
          - SUITEB
          - TCPCHL
          - TCPKEEP
          - TCPNAME
          - TCPSTACK
          - TRAXSTR
          - TRAXTBL
          - TREELIFE
          - TRIGINT
    pcf:
      command: MQCMD_CHANGE_Q_MGR
      request_href: SSFKSJ_9.4.0/refadmin/q087000_.html
      response_href: SSFKSJ_9.4.0/refadmin/q087000_.html
      request_parameters:
        - name: AccountingConnOverride
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_DISABLED
            - MQMON_ENABLED
        - name: AccountingInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: ActivityRecording
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQRECORDING_DISABLED
            - MQRECORDING_MSG
            - MQRECORDING_Q
        - name: AdoptNewMCACheck
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQADOPT_CHECK_Q_MGR_NAME
            - MQADOPT_CHECK_NET_ADDR
            - MQADOPT_CHECK_ALL
            - MQADOPT_CHECK_NONE
        - name: AdoptNewMCAType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQADOPT_TYPE_NO
            - MQADOPT_TYPE_ALL
        - name: AuthorityEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
        - name: AuthorityEventScope
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQAUSC_FAILURES
            - MQAUSC_ALLCONNS
            - MQAUSC_ALLCHECKS
        - name: BridgeEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
        - name: CertificateLabel
          pcf_type: MQCFST
          type_hint: str
        - name: CertificateValPolicy
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQ_CERT_VAL_POLICY_ANY
            - MQ_CERT_VAL_POLICY_RFC5280
        - name: CFConlos
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCFCONLOS_TERMINATE
            - MQCFCONLOS_TOLERATE
        - name: ChannelAutoDef
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHAD_DISABLED
            - MQCHAD_ENABLED
        - name: ChannelAutoDefEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
        - name: ChannelAutoDefExit
          pcf_type: MQCFIN
          type_hint: int
        - name: ChannelAuthenticationRecords
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHLA_DISABLED
            - MQCHLA_ENABLED
        - name: ChannelEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
            - MQEVR_EXCEPTION
        - name: ChannelInitiatorControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSVC_CONTROL_MANUAL
            - MQSVC_CONTROL_Q_MGR
        - name: ChannelMonitoring
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_NONE
            - MQMON_OFF
            - MQMON_LOW
            - MQMON_MEDIUM
            - MQMON_HIGH
        - name: ChannelStatistics
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_NONE
            - MQMON_OFF
            - MQMON_LOW
            - MQMON_MEDIUM
            - MQMON_HIGH
        - name: ChinitAdapters
          pcf_type: MQCFIN
          type_hint: int
        - name: ChinitDispatchers
          pcf_type: MQCFIN
          type_hint: int
        - name: ChinitServiceParm
          pcf_type: MQCFIN
          type_hint: int
        - name: ChinitTraceAutoStart
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQTRAXSTR_YES
            - MQTRAXSTR_NO
        - name: ChinitTraceTableSize
          pcf_type: MQCFIN
          type_hint: int
        - name: ClusterSenderMonitoringDefault
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_Q_MGR
            - MQMON_OFF
            - MQMON_LOW
            - MQMON_MEDIUM
            - MQMON_HIGH
        - name: ClusterSenderStatistics
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_Q_MGR
            - MQMON_OFF
            - MQMON_LOW
            - MQMON_MEDIUM
            - MQMON_HIGH
        - name: ClusterWorkLoadData
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterWorkLoadExit
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterWorkLoadLength
          pcf_type: MQCFIN
          type_hint: int
        - name: CLWLMRUChannels
          pcf_type: MQCFIN
          type_hint: int
        - name: CLWLUseQ
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCLWL_USEQ_ANY
            - MQCLWL_USEQ_LOCAL
        - name: CodedCharSetId
          pcf_type: MQCFIN
          type_hint: int
        - name: CommandEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
            - MQEVR_NO_DISPLAY
        - name: CommandScope
          pcf_type: MQCFIN
          type_hint: int
        - name: CommandServerControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSVC_CONTROL_MANUAL
            - MQSVC_CONTROL_Q_MGR
        - name: ConfigurationEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
        - name: ConnAuth
          pcf_type: MQCFST
          type_hint: str
        - name: Custom
          pcf_type: MQCFST
          type_hint: str
        - name: DeadLetterQName
          pcf_type: MQCFIN
          type_hint: int
        - name: DefClusterXmitQueueType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCLXQ_SCTQ
            - MQCLXQ_CHANNEL
        - name: DefXmitQName
          pcf_type: MQCFST
          type_hint: str
        - name: DNSGroup
          pcf_type: MQCFST
          type_hint: str
        - name: DNSWLM
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQDNSWLM_NO
        - name: ExpiryInterval
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEXPI_OFF
        - name: EncryptionPolicySuiteB
          pcf_type: MQCFIL
          type_hint: int
          enum_values:
            - MQ_SUITE_B_NONE
            - MQ_SUITE_B_128_BIT
            - MQ_SUITE_B_192_BIT
        - name: Force
          pcf_type: MQCFIN
          type_hint: int
        - name: GroupUR
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQGUR_DISABLED
            - MQGUR_ENABLED
        - name: IGQPutAuthority
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQIGQPA_DEFAULT
            - MQIGQPA_CONTEXT
            - MQIGQPA_ONLY_IGQ
            - MQIGQPA_ALTERNATE_OR_IGQ
        - name: IGQUserId
          pcf_type: MQCFST
          type_hint: str
        - name: ImageInterval
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMEDIMGINTVL_OFF
        - name: ImageLogLength
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMEDIMGLOGLN_OFF
        - name: ImageRecoverObject
          pcf_type: MQCFST
          type_hint: str
          enum_values:
            - MQIMGRCOV_NO
            - MQIMGRCOV_YES
        - name: ImageRecoverQueue
          pcf_type: MQCFST
          type_hint: str
          enum_values:
            - MQIMGRCOV_NO
            - MQIMGRCOV_YES
        - name: ImageSchedule
          pcf_type: MQCFST
          type_hint: str
          enum_values:
            - MQMEDIMGSCHED_AUTO
            - MQMEDIMGSCHED_MANUAL
        - name: InhibitEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
        - name: InitialKey
          pcf_type: MQCFST
          type_hint: str
        - name: IntraGroupQueuing
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQIGQ_DISABLED
            - MQIGQ_ENABLED
        - name: IPAddressVersion
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQIPADDR_IPV4
            - MQIPADDR_IPV6
        - name: ListenerTimer
          pcf_type: MQCFIN
          type_hint: int
        - name: LocalEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
        - name: LoggerEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
        - name: LUGroupName
          pcf_type: MQCFST
          type_hint: str
        - name: LUName
          pcf_type: MQCFST
          type_hint: str
        - name: LU62ARMSuffix
          pcf_type: MQCFST
          type_hint: str
        - name: LU62Channels
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxActiveChannels
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxChannels
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxHandles
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxMsgLength
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxPropertiesLength
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPROP_UNRESTRICTED_LENGTH
        - name: MaxUncommittedMsgs
          pcf_type: MQCFIN
          type_hint: int
        - name: MQIAccounting
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_OFF
            - MQMON_ON
        - name: MQIStatistics
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_OFF
            - MQMON_ON
        - name: MsgMarkBrowseInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: OTELPropagationControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQOTEL_PCTL_MANUAL
            - MQOTEL_PCTL_AUTO
        - name: OTELTrace
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQOTEL_TRACE_OFF
            - MQOTEL_TRACE_ON
            - MQOTEL_TRACE_NONE
        - name: OutboundPortMax
          pcf_type: MQCFIN
          type_hint: int
        - name: OutboundPortMin
          pcf_type: MQCFIN
          type_hint: int
        - name: Parent
          pcf_type: MQCFST
          type_hint: str
        - name: PerformanceEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
        - name: PubSubClus
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPSCLUS_ENABLED
            - MQPSCLUS_DISABLED
        - name: PubSubMaxMsgRetryCount
          pcf_type: MQCFIN
          type_hint: int
        - name: PubSubMode
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPSM_COMPAT
            - MQPSM_DISABLED
            - MQPSM_ENABLED
        - name: PubSubNPInputMsg
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQUNDELIVERED_DISCARD
            - MQUNDELIVERED_KEEP
        - name: PubSubNPResponse
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQUNDELIVERED_NORMAL
            - MQUNDELIVERED_SAFE
            - MQUNDELIVERED_DISCARD
            - MQUNDELIVERED_KEEP
        - name: PubSubSyncPoint
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSYNCPOINT_IFPER
            - MQSYNCPOINT_YES
        - name: QMgrDesc
          pcf_type: MQCFST
          type_hint: str
        - name: QSGCertificateLabel
          pcf_type: MQCFST
          type_hint: str
        - name: QueueAccounting
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_NONE
            - MQMON_OFF
            - MQMON_ON
        - name: QueueMonitoring
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_OFF
            - MQMON_NONE
            - MQMON_LOW
            - MQMON_MEDIUM
            - MQMON_HIGH
        - name: QueueStatistics
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_NONE
            - MQMON_OFF
            - MQMON_ON
        - name: ReceiveTimeout
          pcf_type: MQCFIN
          type_hint: int
        - name: ReceiveTimeoutMin
          pcf_type: MQCFIN
          type_hint: int
        - name: ReceiveTimeoutType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQRCVTIME_MULTIPLY
            - MQRCVTIME_ADD
            - MQRCVTIME_EQUAL
        - name: RemoteEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
        - name: RepositoryName
          pcf_type: MQCFST
          type_hint: str
        - name: RepositoryNamelist
          pcf_type: MQCFST
          type_hint: str
        - name: RevDns
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQRDNS_DISABLED
            - MQRDNS_ENABLED
        - name: SecurityCase
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSCYC_UPPER
            - MQSCYC_MIXED
        - name: SharedQQmgrName
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSQQM_USE
            - MQSQQM_IGNORE
        - name: SSLCRLNamelist
          pcf_type: MQCFST
          type_hint: str
        - name: SSLCryptoHardware
          pcf_type: MQCFST
          type_hint: str
          enum_values:
            - SYMMETRIC_CIPHER_OFF
            - SYMMETRIC_CIPHER_ON
        - name: SSLEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
        - name: SSLFipsRequired
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSSL_FIPS_NO
            - MQSSL_FIPS_YES
        - name: SSLKeyRepository
          pcf_type: MQCFST
          type_hint: str
        - name: SSLKeyRepositoryPassword
          pcf_type: MQCFST
          type_hint: str
        - name: SSLKeyResetCount
          pcf_type: MQCFIN
          type_hint: int
        - name: SSLTasks
          pcf_type: MQCFIN
          type_hint: int
        - name: StartStopEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
        - name: StatisticsInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: TCPChannels
          pcf_type: MQCFIN
          type_hint: int
        - name: TCPKeepAlive
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQTCPKEEP_YES
            - MQTCPKEEP_NO
        - name: TCPName
          pcf_type: MQCFST
          type_hint: str
        - name: TCPStackType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQTCPSTACK_SINGLE
            - MQTCPSTACK_MULTIPLE
        - name: TraceRouteRecording
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQRECORDING_DISABLED
            - MQRECORDING_MSG
            - MQRECORDING_Q
        - name: TreeLifeTime
          pcf_type: MQCFIN
          type_hint: int
        - name: TriggerInterval
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQRCCF_CERT_LABEL_NOT_ALLOWED
            - MQRCCF_CHAD_ERROR
            - MQRCCF_CHAD_EVENT_ERROR
            - MQRCCF_CHAD_EVENT_WRONG_TYPE
            - MQRCCF_CHAD_EXIT_ERROR
            - MQRCCF_CHAD_EXIT_WRONG_TYPE
            - MQRCCF_CHAD_WRONG_TYPE
            - MQRCCF_FORCE_VALUE_ERROR
            - MQRCCF_PATH_NOT_VALID
            - MQRCCF_PWD_LENGTH_ERROR
            - MQRCCF_PSCLUS_DISABLED_TOPDEF
            - MQRCCF_PSCLUS_TOPIC_EXSITS
            - MQRCCF_Q_MGR_ATTR_CONFLICT
            - MQRCCF_Q_MGR_CCSID_ERROR
            - MQRCCF_REPOS_NAME_CONFLICT
            - MQRCCF_UNKNOWN_Q_MGR
            - MQRCCF_WRONG_CHANNEL_TYPE
      response_parameters:
        - name: AccountingConnOverride
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_DISABLED
            - MQMON_ENABLED
        - name: AccountingInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: ActivityRecording
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQRECORDING_DISABLED
            - MQRECORDING_MSG
            - MQRECORDING_Q
        - name: AdoptNewMCACheck
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQADOPT_CHECK_Q_MGR_NAME
            - MQADOPT_CHECK_NET_ADDR
            - MQADOPT_CHECK_ALL
            - MQADOPT_CHECK_NONE
        - name: AdoptNewMCAType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQADOPT_TYPE_NO
            - MQADOPT_TYPE_ALL
        - name: AuthorityEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
        - name: AuthorityEventScope
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQAUSC_FAILURES
            - MQAUSC_ALLCONNS
            - MQAUSC_ALLCHECKS
        - name: BridgeEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
        - name: CertificateLabel
          pcf_type: MQCFST
          type_hint: str
        - name: CertificateValPolicy
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQ_CERT_VAL_POLICY_ANY
            - MQ_CERT_VAL_POLICY_RFC5280
        - name: CFConlos
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCFCONLOS_TERMINATE
            - MQCFCONLOS_TOLERATE
        - name: ChannelAutoDef
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHAD_DISABLED
            - MQCHAD_ENABLED
        - name: ChannelAutoDefEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
        - name: ChannelAutoDefExit
          pcf_type: MQCFIN
          type_hint: int
        - name: ChannelAuthenticationRecords
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHLA_DISABLED
            - MQCHLA_ENABLED
        - name: ChannelEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
            - MQEVR_EXCEPTION
        - name: ChannelInitiatorControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSVC_CONTROL_MANUAL
            - MQSVC_CONTROL_Q_MGR
        - name: ChannelMonitoring
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_NONE
            - MQMON_OFF
            - MQMON_LOW
            - MQMON_MEDIUM
            - MQMON_HIGH
        - name: ChannelStatistics
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_NONE
            - MQMON_OFF
            - MQMON_LOW
            - MQMON_MEDIUM
            - MQMON_HIGH
        - name: ChinitAdapters
          pcf_type: MQCFIN
          type_hint: int
        - name: ChinitDispatchers
          pcf_type: MQCFIN
          type_hint: int
        - name: ChinitServiceParm
          pcf_type: MQCFIN
          type_hint: int
        - name: ChinitTraceAutoStart
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQTRAXSTR_YES
            - MQTRAXSTR_NO
        - name: ChinitTraceTableSize
          pcf_type: MQCFIN
          type_hint: int
        - name: ClusterSenderMonitoringDefault
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_Q_MGR
            - MQMON_OFF
            - MQMON_LOW
            - MQMON_MEDIUM
            - MQMON_HIGH
        - name: ClusterSenderStatistics
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_Q_MGR
            - MQMON_OFF
            - MQMON_LOW
            - MQMON_MEDIUM
            - MQMON_HIGH
        - name: ClusterWorkLoadData
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterWorkLoadExit
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterWorkLoadLength
          pcf_type: MQCFIN
          type_hint: int
        - name: CLWLMRUChannels
          pcf_type: MQCFIN
          type_hint: int
        - name: CLWLUseQ
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCLWL_USEQ_ANY
            - MQCLWL_USEQ_LOCAL
        - name: CodedCharSetId
          pcf_type: MQCFIN
          type_hint: int
        - name: CommandEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
            - MQEVR_NO_DISPLAY
        - name: CommandScope
          pcf_type: MQCFIN
          type_hint: int
        - name: CommandServerControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSVC_CONTROL_MANUAL
            - MQSVC_CONTROL_Q_MGR
        - name: ConfigurationEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
        - name: ConnAuth
          pcf_type: MQCFST
          type_hint: str
        - name: Custom
          pcf_type: MQCFST
          type_hint: str
        - name: DeadLetterQName
          pcf_type: MQCFIN
          type_hint: int
        - name: DefClusterXmitQueueType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCLXQ_SCTQ
            - MQCLXQ_CHANNEL
        - name: DefXmitQName
          pcf_type: MQCFST
          type_hint: str
        - name: DNSGroup
          pcf_type: MQCFST
          type_hint: str
        - name: DNSWLM
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQDNSWLM_NO
        - name: ExpiryInterval
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEXPI_OFF
        - name: EncryptionPolicySuiteB
          pcf_type: MQCFIL
          type_hint: int
          enum_values:
            - MQ_SUITE_B_NONE
            - MQ_SUITE_B_128_BIT
            - MQ_SUITE_B_192_BIT
        - name: Force
          pcf_type: MQCFIN
          type_hint: int
        - name: GroupUR
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQGUR_DISABLED
            - MQGUR_ENABLED
        - name: IGQPutAuthority
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQIGQPA_DEFAULT
            - MQIGQPA_CONTEXT
            - MQIGQPA_ONLY_IGQ
            - MQIGQPA_ALTERNATE_OR_IGQ
        - name: IGQUserId
          pcf_type: MQCFST
          type_hint: str
        - name: ImageInterval
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMEDIMGINTVL_OFF
        - name: ImageLogLength
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMEDIMGLOGLN_OFF
        - name: ImageRecoverObject
          pcf_type: MQCFST
          type_hint: str
          enum_values:
            - MQIMGRCOV_NO
            - MQIMGRCOV_YES
        - name: ImageRecoverQueue
          pcf_type: MQCFST
          type_hint: str
          enum_values:
            - MQIMGRCOV_NO
            - MQIMGRCOV_YES
        - name: ImageSchedule
          pcf_type: MQCFST
          type_hint: str
          enum_values:
            - MQMEDIMGSCHED_AUTO
            - MQMEDIMGSCHED_MANUAL
        - name: InhibitEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
        - name: InitialKey
          pcf_type: MQCFST
          type_hint: str
        - name: IntraGroupQueuing
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQIGQ_DISABLED
            - MQIGQ_ENABLED
        - name: IPAddressVersion
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQIPADDR_IPV4
            - MQIPADDR_IPV6
        - name: ListenerTimer
          pcf_type: MQCFIN
          type_hint: int
        - name: LocalEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
        - name: LoggerEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
        - name: LUGroupName
          pcf_type: MQCFST
          type_hint: str
        - name: LUName
          pcf_type: MQCFST
          type_hint: str
        - name: LU62ARMSuffix
          pcf_type: MQCFST
          type_hint: str
        - name: LU62Channels
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxActiveChannels
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxChannels
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxHandles
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxMsgLength
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxPropertiesLength
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPROP_UNRESTRICTED_LENGTH
        - name: MaxUncommittedMsgs
          pcf_type: MQCFIN
          type_hint: int
        - name: MQIAccounting
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_OFF
            - MQMON_ON
        - name: MQIStatistics
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_OFF
            - MQMON_ON
        - name: MsgMarkBrowseInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: OTELPropagationControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQOTEL_PCTL_MANUAL
            - MQOTEL_PCTL_AUTO
        - name: OTELTrace
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQOTEL_TRACE_OFF
            - MQOTEL_TRACE_ON
            - MQOTEL_TRACE_NONE
        - name: OutboundPortMax
          pcf_type: MQCFIN
          type_hint: int
        - name: OutboundPortMin
          pcf_type: MQCFIN
          type_hint: int
        - name: Parent
          pcf_type: MQCFST
          type_hint: str
        - name: PerformanceEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
        - name: PubSubClus
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPSCLUS_ENABLED
            - MQPSCLUS_DISABLED
        - name: PubSubMaxMsgRetryCount
          pcf_type: MQCFIN
          type_hint: int
        - name: PubSubMode
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPSM_COMPAT
            - MQPSM_DISABLED
            - MQPSM_ENABLED
        - name: PubSubNPInputMsg
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQUNDELIVERED_DISCARD
            - MQUNDELIVERED_KEEP
        - name: PubSubNPResponse
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQUNDELIVERED_NORMAL
            - MQUNDELIVERED_SAFE
            - MQUNDELIVERED_DISCARD
            - MQUNDELIVERED_KEEP
        - name: PubSubSyncPoint
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSYNCPOINT_IFPER
            - MQSYNCPOINT_YES
        - name: QMgrDesc
          pcf_type: MQCFST
          type_hint: str
        - name: QSGCertificateLabel
          pcf_type: MQCFST
          type_hint: str
        - name: QueueAccounting
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_NONE
            - MQMON_OFF
            - MQMON_ON
        - name: QueueMonitoring
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_OFF
            - MQMON_NONE
            - MQMON_LOW
            - MQMON_MEDIUM
            - MQMON_HIGH
        - name: QueueStatistics
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_NONE
            - MQMON_OFF
            - MQMON_ON
        - name: ReceiveTimeout
          pcf_type: MQCFIN
          type_hint: int
        - name: ReceiveTimeoutMin
          pcf_type: MQCFIN
          type_hint: int
        - name: ReceiveTimeoutType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQRCVTIME_MULTIPLY
            - MQRCVTIME_ADD
            - MQRCVTIME_EQUAL
        - name: RemoteEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
        - name: RepositoryName
          pcf_type: MQCFST
          type_hint: str
        - name: RepositoryNamelist
          pcf_type: MQCFST
          type_hint: str
        - name: RevDns
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQRDNS_DISABLED
            - MQRDNS_ENABLED
        - name: SecurityCase
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSCYC_UPPER
            - MQSCYC_MIXED
        - name: SharedQQmgrName
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSQQM_USE
            - MQSQQM_IGNORE
        - name: SSLCRLNamelist
          pcf_type: MQCFST
          type_hint: str
        - name: SSLCryptoHardware
          pcf_type: MQCFST
          type_hint: str
          enum_values:
            - SYMMETRIC_CIPHER_OFF
            - SYMMETRIC_CIPHER_ON
        - name: SSLEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
        - name: SSLFipsRequired
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSSL_FIPS_NO
            - MQSSL_FIPS_YES
        - name: SSLKeyRepository
          pcf_type: MQCFST
          type_hint: str
        - name: SSLKeyRepositoryPassword
          pcf_type: MQCFST
          type_hint: str
        - name: SSLKeyResetCount
          pcf_type: MQCFIN
          type_hint: int
        - name: SSLTasks
          pcf_type: MQCFIN
          type_hint: int
        - name: StartStopEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
        - name: StatisticsInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: TCPChannels
          pcf_type: MQCFIN
          type_hint: int
        - name: TCPKeepAlive
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQTCPKEEP_YES
            - MQTCPKEEP_NO
        - name: TCPName
          pcf_type: MQCFST
          type_hint: str
        - name: TCPStackType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQTCPSTACK_SINGLE
            - MQTCPSTACK_MULTIPLE
        - name: TraceRouteRecording
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQRECORDING_DISABLED
            - MQRECORDING_MSG
            - MQRECORDING_Q
        - name: TreeLifeTime
          pcf_type: MQCFIN
          type_hint: int
        - name: TriggerInterval
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQRCCF_CERT_LABEL_NOT_ALLOWED
            - MQRCCF_CHAD_ERROR
            - MQRCCF_CHAD_EVENT_ERROR
            - MQRCCF_CHAD_EVENT_WRONG_TYPE
            - MQRCCF_CHAD_EXIT_ERROR
            - MQRCCF_CHAD_EXIT_WRONG_TYPE
            - MQRCCF_CHAD_WRONG_TYPE
            - MQRCCF_FORCE_VALUE_ERROR
            - MQRCCF_PATH_NOT_VALID
            - MQRCCF_PWD_LENGTH_ERROR
            - MQRCCF_PSCLUS_DISABLED_TOPDEF
            - MQRCCF_PSCLUS_TOPIC_EXSITS
            - MQRCCF_Q_MGR_ATTR_CONFLICT
            - MQRCCF_Q_MGR_CCSID_ERROR
            - MQRCCF_REPOS_NAME_CONFLICT
            - MQRCCF_UNKNOWN_Q_MGR
            - MQRCCF_WRONG_CHANNEL_TYPE
    mapping:
      request:
        suggested:
          FORCE: Force
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - AccountingConnOverride
          - AccountingInterval
          - ActivityRecording
          - AdoptNewMCACheck
          - AdoptNewMCAType
          - AuthorityEvent
          - AuthorityEventScope
          - BridgeEvent
          - CFConlos
          - CLWLMRUChannels
          - CLWLUseQ
          - CertificateLabel
          - CertificateValPolicy
          - ChannelAuthenticationRecords
          - ChannelAutoDef
          - ChannelAutoDefEvent
          - ChannelAutoDefExit
          - ChannelEvent
          - ChannelInitiatorControl
          - ChannelMonitoring
          - ChannelStatistics
          - ChinitAdapters
          - ChinitDispatchers
          - ChinitServiceParm
          - ChinitTraceAutoStart
          - ChinitTraceTableSize
          - ClusterSenderMonitoringDefault
          - ClusterSenderStatistics
          - ClusterWorkLoadData
          - ClusterWorkLoadExit
          - ClusterWorkLoadLength
          - CodedCharSetId
          - CommandEvent
          - CommandScope
          - CommandServerControl
          - ConfigurationEvent
          - ConnAuth
          - Custom
          - DNSGroup
          - DNSWLM
          - DeadLetterQName
          - DefClusterXmitQueueType
          - DefXmitQName
          - EncryptionPolicySuiteB
          - ExpiryInterval
          - GroupUR
          - IGQPutAuthority
          - IGQUserId
          - IPAddressVersion
          - ImageInterval
          - ImageLogLength
          - ImageRecoverObject
          - ImageRecoverQueue
          - ImageSchedule
          - InhibitEvent
          - InitialKey
          - IntraGroupQueuing
          - LU62ARMSuffix
          - LU62Channels
          - LUGroupName
          - LUName
          - ListenerTimer
          - LocalEvent
          - LoggerEvent
          - MQIAccounting
          - MQIStatistics
          - MaxActiveChannels
          - MaxChannels
          - MaxHandles
          - MaxMsgLength
          - MaxPropertiesLength
          - MaxUncommittedMsgs
          - MsgMarkBrowseInterval
          - OTELPropagationControl
          - OTELTrace
          - OutboundPortMax
          - OutboundPortMin
          - Parent
          - PerformanceEvent
          - PubSubClus
          - PubSubMaxMsgRetryCount
          - PubSubMode
          - PubSubNPInputMsg
          - PubSubNPResponse
          - PubSubSyncPoint
          - QMgrDesc
          - QSGCertificateLabel
          - QueueAccounting
          - QueueMonitoring
          - QueueStatistics
          - ReceiveTimeout
          - ReceiveTimeoutMin
          - ReceiveTimeoutType
          - RemoteEvent
          - RepositoryName
          - RepositoryNamelist
          - RevDns
          - SSLCRLNamelist
          - SSLCryptoHardware
          - SSLEvent
          - SSLFipsRequired
          - SSLKeyRepository
          - SSLKeyRepositoryPassword
          - SSLKeyResetCount
          - SSLTasks
          - SecurityCase
          - SharedQQmgrName
          - StartStopEvent
          - StatisticsInterval
          - TCPChannels
          - TCPKeepAlive
          - TCPName
          - TCPStackType
          - TraceRouteRecording
          - TreeLifeTime
          - TriggerInterval
      response:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - AccountingConnOverride
          - AccountingInterval
          - ActivityRecording
          - AdoptNewMCACheck
          - AdoptNewMCAType
          - AuthorityEvent
          - AuthorityEventScope
          - BridgeEvent
          - CFConlos
          - CLWLMRUChannels
          - CLWLUseQ
          - CertificateLabel
          - CertificateValPolicy
          - ChannelAuthenticationRecords
          - ChannelAutoDef
          - ChannelAutoDefEvent
          - ChannelAutoDefExit
          - ChannelEvent
          - ChannelInitiatorControl
          - ChannelMonitoring
          - ChannelStatistics
          - ChinitAdapters
          - ChinitDispatchers
          - ChinitServiceParm
          - ChinitTraceAutoStart
          - ChinitTraceTableSize
          - ClusterSenderMonitoringDefault
          - ClusterSenderStatistics
          - ClusterWorkLoadData
          - ClusterWorkLoadExit
          - ClusterWorkLoadLength
          - CodedCharSetId
          - CommandEvent
          - CommandScope
          - CommandServerControl
          - ConfigurationEvent
          - ConnAuth
          - Custom
          - DNSGroup
          - DNSWLM
          - DeadLetterQName
          - DefClusterXmitQueueType
          - DefXmitQName
          - EncryptionPolicySuiteB
          - ExpiryInterval
          - Force
          - GroupUR
          - IGQPutAuthority
          - IGQUserId
          - IPAddressVersion
          - ImageInterval
          - ImageLogLength
          - ImageRecoverObject
          - ImageRecoverQueue
          - ImageSchedule
          - InhibitEvent
          - InitialKey
          - IntraGroupQueuing
          - LU62ARMSuffix
          - LU62Channels
          - LUGroupName
          - LUName
          - ListenerTimer
          - LocalEvent
          - LoggerEvent
          - MQIAccounting
          - MQIStatistics
          - MaxActiveChannels
          - MaxChannels
          - MaxHandles
          - MaxMsgLength
          - MaxPropertiesLength
          - MaxUncommittedMsgs
          - MsgMarkBrowseInterval
          - OTELPropagationControl
          - OTELTrace
          - OutboundPortMax
          - OutboundPortMin
          - Parent
          - PerformanceEvent
          - PubSubClus
          - PubSubMaxMsgRetryCount
          - PubSubMode
          - PubSubNPInputMsg
          - PubSubNPResponse
          - PubSubSyncPoint
          - QMgrDesc
          - QSGCertificateLabel
          - QueueAccounting
          - QueueMonitoring
          - QueueStatistics
          - ReceiveTimeout
          - ReceiveTimeoutMin
          - ReceiveTimeoutType
          - RemoteEvent
          - RepositoryName
          - RepositoryNamelist
          - RevDns
          - SSLCRLNamelist
          - SSLCryptoHardware
          - SSLEvent
          - SSLFipsRequired
          - SSLKeyRepository
          - SSLKeyRepositoryPassword
          - SSLKeyResetCount
          - SSLTasks
          - SecurityCase
          - SharedQQmgrName
          - StartStopEvent
          - StatisticsInterval
          - TCPChannels
          - TCPKeepAlive
          - TCPName
          - TCPStackType
          - TraceRouteRecording
          - TreeLifeTime
          - TriggerInterval
    notes: []
  - mqsc:
      name: DISPLAY QMGR
      href: SSFKSJ_9.4.0/refadmin/q086240_.html
      positional_parameters:
        - integer
        - qmgr-name
      input_parameters: []
      output_parameters:
        - ACCTQ
        - ACCTQMQI
        - ACTVTRC
        - ADOPTCHK
        - ADVCAP
        - ALL
        - CFCONLOS
        - CLWLUSEQ
        - DEFCLXQ
        - MAXUMSGS
        - OTELPCTL
        - OTELTRAC
        - QMGRPROD
        - RCVTIME
        - RCVTTYPE
        - SQQMNAME
        - SSLCRLNL
      section_sources:
        'Requested parameters':
          - DEFCLXQ
          - OTELPCTL
          - OTELTRAC
    pcf:
      command: MQCMD_INQUIRE_Q_MGR
      request_href: SSFKSJ_9.4.0/refadmin/q087820_.html
      response_href: SSFKSJ_9.4.0/refadmin/q087830_.html
      request_parameters:
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: QMgrAttrs
          pcf_type: MQCFIL
          type_hint: int
          enum_values:
            - MQIACF_ALL
            - MQCA_ALTERATION_DATE
            - MQCA_ALTERATION_TIME
            - MQCA_CERT_LABEL
            - MQCA_CHANNEL_AUTO_DEF_EXIT
            - MQCA_CLUSTER_WORKLOAD_DATA
            - MQCA_CLUSTER_WORKLOAD_EXIT
            - MQCA_COMMAND_INPUT_Q_NAME
            - MQCA_CONN_AUTH
            - MQCA_CREATION_DATE
            - MQCA_CREATION_TIME
            - MQCA_CUSTOM
            - MQCA_DEAD_LETTER_Q_NAME
            - MQCA_DEF_XMIT_Q_NAME
            - MQCA_DNS_GROUP
            - MQCA_IGQ_USER_ID
            - MQCA_INITIAL_KEY
            - MQCA_LU_GROUP_NAME
            - MQCA_LU_NAME
            - MQCA_LU62_ARM_SUFFIX
            - MQCA_PARENT
            - MQCA_Q_MGR_DESC
            - MQCA_Q_MGR_IDENTIFIER
            - MQCA_Q_MGR_NAME
            - MQCA_QSG_CERT_LABEL
            - MQCA_QSG_NAME
            - MQCA_REPOSITORY_NAME
            - MQCA_REPOSITORY_NAMELIST
            - MQCA_SSL_CRL_NAMELIST
            - MQCA_SSL_CRYPTO_HARDWARE
            - MQCA_SSL_KEY_REPO_PASSWORD
            - MQCA_SSL_KEY_REPOSITORY
            - MQCA_TCP_NAME
            - MQCA_VERSION
            - MQIA_ACCOUNTING_CONN_OVERRIDE
            - MQIA_ACCOUNTING_INTERVAL
            - MQIA_ACCOUNTING_MQI
            - MQIA_ACCOUNTING_Q
            - MQIA_ACTIVE_CHANNELS
            - MQIA_ACTIVITY_CONN_OVERRIDE
            - MQIA_ACTIVITY_RECORDING
            - MQIA_ACTIVITY_TRACE
            - MQIA_ADOPTNEWMCA_CHECK
            - MQIA_ADOPTNEWMCA_TYPE
            - MQIA_ADVANCED_CAPABILITY
            - MQIA_AMQP_CAPABILITY
            - MQIA_AUTHORITY_EVENT
            - MQIA_BRIDGE_EVENT
            - MQIA_CERT_VAL_POLICY
            - MQIA_CHANNEL_AUTO_DEF
            - MQIA_CHANNEL_AUTO_DEF_EVENT
            - MQIA_CHANNEL_EVENT
            - MQIA_CHINIT_ADAPTERS
            - MQIA_CHINIT_CONTROL
            - MQIA_CHINIT_DISPATCHERS
            - MQIA_CHINIT_SERVICE_PARM
            - MQIA_CHINIT_TRACE_AUTO_START
            - MQIA_CHINIT_TRACE_TABLE_SIZE
            - MQIA_CHLAUTH_RECORDS
            - MQIA_CLUSTER_WORKLOAD_LENGTH
            - MQIA_CLWL_MRU_CHANNELS
            - MQIA_CLWL_USEQ
            - MQIA_CMD_SERVER_CONTROL
            - MQIA_CODED_CHAR_SET_ID
            - MQIA_COMMAND_EVENT
            - MQIA_COMMAND_LEVEL
            - MQIA_CONFIGURATION_EVENT
            - MQIA_CPI_LEVEL
            - MQIA_DEF_CLUSTER_XMIT_Q_TYPE
            - MQIA_DIST_LISTS
            - MQIA_DNS_WLM
            - MQIA_EXPIRY_INTERVAL
            - MQIA_GROUP_UR
            - MQIA_IGQ_PUT_AUTHORITY
            - MQIA_INHIBIT_EVENT
            - MQIA_INTRA_GROUP_QUEUING
            - MQIA_IP_ADDRESS_VERSION
            - MQIA_LISTENER_TIMER
            - MQIA_LOCAL_EVENT
            - MQIA_LOGGER_EVENT
            - MQIA_LU62_CHANNELS
            - MQIA_MSG_MARK_BROWSE_INTERVAL
            - MQIA_MAX_CHANNELS
            - MQIA_MAX_HANDLES
            - MQIA_MAX_MSG_LENGTH
            - MQIA_MAX_PRIORITY
            - MQIA_MAX_PROPERTIES_LENGTH
            - MQIA_MAX_UNCOMMITTED_MSGS
            - MQIA_MEDIA_IMAGE_INTERVAL
            - MQIA_MEDIA_IMAGE_LOG_LENGTH
            - MQIA_MEDIA_IMAGE_RECOVER_OBJ
            - MQIA_MEDIA_IMAGE_RECOVER_Q
            - MQIA_MEDIA_IMAGE_SCHEDULING
            - MQIA_MONITORING_AUTO_CLUSSDR
            - MQIA_MONITORING_CHANNEL
            - MQIA_MONITORING_Q
            - MQIA_OTEL_PROPAGATION_CONTROL
            - MQIA_OTEL_TRACE
            - MQIA_OUTBOUND_PORT_MAX
            - MQIA_OUTBOUND_PORT_MIN
            - MQIA_PERFORMANCE_EVENT
            - MQIA_PLATFORM
            - MQIA_PROT_POLICY_CAPABILITY
            - MQIA_PUBSUB_CLUSTER
            - MQIA_PUBSUB_MAXMSG_RETRY_COUNT
            - MQIA_PUBSUB_MODE
            - MQIA_PUBSUB_NP_MSG
            - MQIA_PUBSUB_NP_RESP
            - MQIA_PUBSUB_SYNC_PT
            - MQIA_QMGR_CFCONLOS
            - MQIA_RECEIVE_TIMEOUT
            - MQIA_RECEIVE_TIMEOUT_MIN
            - MQIA_RECEIVE_TIMEOUT_TYPE
            - MQIA_REMOTE_EVENT
            - MQIA_SECURITY_CASE
            - MQIA_SHARED_Q_Q_MGR_NAME
            - MQIA_SSL_EVENT
            - MQIA_SSL_FIPS_REQUIRED
            - MQIA_SSL_RESET_COUNT
            - MQIA_SSL_TASKS
            - MQIA_START_STOP_EVENT
            - MQIA_STATISTICS_AUTO_CLUSSDR
            - MQIA_STATISTICS_CHANNEL
            - MQIA_STATISTICS_INTERVAL
            - MQIA_STATISTICS_MQI
            - MQIA_STATISTICS_Q
            - MQIA_SUITE_B_STRENGTH
            - MQIA_SYNCPOINT
            - MQIA_TCP_CHANNELS
            - MQIA_TCP_KEEP_ALIVE
            - MQIA_TCP_STACK_TYPE
            - MQIA_TRACE_ROUTE_RECORDING
            - MQIA_TREE_LIFE_TIME
            - MQIA_TRIGGER_INTERVAL
            - MQIA_XR_CAPABILITY
            - MQIACF_Q_MGR_CLUSTER
            - MQIACF_Q_MGR_DQM
            - MQIACF_Q_MGR_EVENT
            - MQIACF_Q_MGR_PUBSUB
            - MQIACF_Q_MGR_SYSTEM
      response_parameters:
        - name: AccountingConnOverride
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_DISABLED
            - MQMON_ENABLED
        - name: AccountingInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: ActivityConnOverride
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_DISABLED
            - MQMON_ENABLED
        - name: ActivityRecording
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQRECORDING_DISABLED
            - MQRECORDING_MSG
            - MQRECORDING_Q
        - name: ActivityTrace
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_OFF
            - MQMON_ON
        - name: AdoptNewMCACheck
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQADOPT_CHECK_Q_MGR_NAME
            - MQADOPT_CHECK_NET_ADDR
            - MQADOPT_CHECK_ALL
            - MQADOPT_CHECK_NONE
        - name: AdoptNewMCAType
          pcf_type: MQCFIL
          type_hint: int
          enum_values:
            - MQADOPT_TYPE_NO
            - MQADOPT_TYPE_ALL
        - name: AdvancedCapability
          pcf_type: MQCFIN
          type_hint: int
        - name: AlterationDate
          pcf_type: MQCFST
          type_hint: str
        - name: AlterationTime
          pcf_type: MQCFST
          type_hint: str
        - name: AMQPCapability
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCAP_SUPPORTED
            - MQCAP_NOT_SUPPORTED
        - name: AuthorityEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
        - name: BridgeEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
        - name: CertificateLabel
          pcf_type: MQCFST
          type_hint: str
        - name: CertificateValPolicy
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQ_CERT_VAL_POLICY_ANY
            - MQ_CERT_VAL_POLICY_RFC5280
        - name: CFConlos
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCFCONLOS_TERMINATE
            - MQCFCONLOS_TOLERATE
        - name: ChannelAutoDef
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHAD_DISABLED
            - MQCHAD_ENABLED
        - name: ChannelAutoDefEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
        - name: ChannelAutoDefExit
          pcf_type: MQCFST
          type_hint: str
        - name: ChannelAuthenticationRecords
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHLA_DISABLED
            - MQCHLA_ENABLED
        - name: ChannelEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
            - MQEVR_EXCEPTION
        - name: ChannelInitiatorControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSVC_CONTROL_MANUAL
            - MQSVC_CONTROL_Q_MGR
        - name: ChannelMonitoring
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_OFF
            - MQMON_NONE
            - MQMON_LOW
            - MQMON_MEDIUM
            - MQMON_HIGH
        - name: ChannelStatistics
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_OFF
            - MQMON_LOW
            - MQMON_MEDIUM
            - MQMON_HIGH
        - name: ChinitAdapters
          pcf_type: MQCFIN
          type_hint: int
        - name: ChinitDispatchers
          pcf_type: MQCFIN
          type_hint: int
        - name: ChinitServiceParm
          pcf_type: MQCFST
          type_hint: str
        - name: ChinitTraceAutoStart
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQTRAXSTR_YES
            - MQTRAXSTR_NO
        - name: ChinitTraceTableSize
          pcf_type: MQCFIN
          type_hint: int
        - name: ClusterSenderMonitoringDefault
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_Q_MGR
            - MQMON_OFF
            - MQMON_LOW
            - MQMON_MEDIUM
            - MQMON_HIGH
        - name: ClusterSenderStatistics
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_Q_MGR
            - MQMON_OFF
            - MQMON_LOW
            - MQMON_MEDIUM
            - MQMON_HIGH
        - name: ClusterWorkLoadData
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterWorkLoadExit
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterWorkLoadLength
          pcf_type: MQCFIN
          type_hint: int
        - name: CLWLMRUChannels
          pcf_type: MQCFIN
          type_hint: int
        - name: CLWLUseQ
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCLWL_USEQ_ANY
            - MQCLWL_USEQ_LOCAL
        - name: CodedCharSetId
          pcf_type: MQCFIN
          type_hint: int
        - name: CommandEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
            - MQEVR_NODISPLAY
        - name: CommandInputQName
          pcf_type: MQCFST
          type_hint: str
        - name: CommandLevel
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCMDL_LEVEL_800
            - MQCMDL_LEVEL_801
            - MQCMDL_LEVEL_802
            - MQCMDL_LEVEL_900
            - MQCMDL_LEVEL_901
            - MQCMDL_LEVEL_902
            - MQCMDL_LEVEL_903
            - MQCMDL_LEVEL_904
            - MQCMDL_LEVEL_905
            - MQCMDL_LEVEL_910
            - MQCMDL_LEVEL_911
            - MQCMDL_LEVEL_912
            - MQCMDL_LEVEL_913
            - MQCMDL_LEVEL_914
            - MQCMDL_LEVEL_915
            - MQCMDL_LEVEL_920
            - MQCMDL_LEVEL_921
            - MQCMDL_LEVEL_922
            - MQCMDL_LEVEL_923
            - MQCMDL_LEVEL_924
            - MQCMDL_LEVEL_925
            - MQCMDL_LEVEL_930
            - MQCMDL_LEVEL_931
            - MQCMDL_LEVEL_932
            - MQCMDL_LEVEL_933
            - MQCMDL_LEVEL_934
            - MQCMDL_LEVEL_935
            - MQCMDL_LEVEL_940
        - name: CommandServerControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSVC_CONTROL_MANUAL
            - MQSVC_CONTROL_Q_MGR
        - name: ConfigurationEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
        - name: ConnAuth
          pcf_type: MQCFST
          type_hint: str
        - name: CreationDate
          pcf_type: MQCFST
          type_hint: str
        - name: CreationTime
          pcf_type: MQCFST
          type_hint: str
        - name: Custom
          pcf_type: MQCFST
          type_hint: str
        - name: DeadLetterQName
          pcf_type: MQCFST
          type_hint: str
        - name: DefClusterXmitQueueType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCLXQ_SCTQ
            - MQCLXQ_CHANNEL
        - name: DefXmitQName
          pcf_type: MQCFST
          type_hint: str
        - name: DistLists
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQDL_SUPPORTED
            - MQDL_NOT_SUPPORTED
        - name: DNSGroup
          pcf_type: MQCFST
          type_hint: str
        - name: DNSWLM
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQDNSWLM_NO
        - name: EncryptionPolicySuiteB
          pcf_type: MQCFIL
          type_hint: int
          enum_values:
            - MQ_SUITE_B_NONE
            - MQ_SUITE_B_128_BIT
            - MQ_SUITE_B_192_BIT
        - name: ExpiryInterval
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEXPI_OFF
        - name: GroupUR
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQGUR_DISABLED
            - MQGUR_ENABLED
        - name: IGQPutAuthority
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQIGQPA_DEFAULT
            - MQIGQPA_CONTEXT
            - MQIGQPA_ONLY_IGQ
            - MQIGQPA_ALTERNATE_OR_IGQ
        - name: IGQUserId
          pcf_type: MQCFST
          type_hint: str
        - name: ImageInterval
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMEDIMGINTVL_OFF
        - name: ImageLogLength
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMEDIMGLOGLN_OFF
        - name: ImageRecoverObject
          pcf_type: MQCFST
          type_hint: str
          enum_values:
            - MQIMGRCOV_NO
            - MQIMGRCOV_YES
        - name: ImageRecoverQueue
          pcf_type: MQCFST
          type_hint: str
          enum_values:
            - MQIMGRCOV_NO
            - MQIMGRCOV_YES
        - name: ImageSchedule
          pcf_type: MQCFST
          type_hint: str
          enum_values:
            - MQMEDIMGSCHED_AUTO
            - MQMEDIMGSCHED_MANUAL
        - name: InhibitEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
        - name: InitialKey
          pcf_type: MQCFST
          type_hint: str
        - name: IntraGroupQueuing
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQIGQ_DISABLED
            - MQIGQ_ENABLED
        - name: IPAddressVersion
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQIPADDR_IPV4
            - MQIPADDR_IPV6
        - name: ListenerTimer
          pcf_type: MQCFIN
          type_hint: int
        - name: LocalEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
        - name: LoggerEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
        - name: LUGroupName
          pcf_type: MQCFST
          type_hint: str
        - name: LUName
          pcf_type: MQCFST
          type_hint: str
        - name: LU62ARMSuffix
          pcf_type: MQCFST
          type_hint: str
        - name: LU62Channels
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxActiveChannels
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxChannels
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxHandles
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxMsgLength
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxPriority
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxPropertiesLength
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxUncommittedMsgs
          pcf_type: MQCFIN
          type_hint: int
        - name: MQIAccounting
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_OFF
            - MQMON_ON
        - name: MQIStatistics
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_OFF
            - MQMON_ON
        - name: MsgMarkBrowseInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: OTELPropagationControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQOTEL_PCTL_MANUAL
            - MQOTEL_PCTL_AUTO
        - name: OTELTrace
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQOTEL_TRACE_OFF
            - MQOTEL_TRACE_ON
            - MQOTEL_TRACE_NONE
        - name: OutboundPortMax
          pcf_type: MQCFIN
          type_hint: int
        - name: OutboundPortMin
          pcf_type: MQCFIN
          type_hint: int
        - name: Parent
          pcf_type: MQCFST
          type_hint: str
        - name: PerformanceEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
        - name: Platform
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPL_AIX
            - MQPL_APPLIANCE
            - MQPL_OS400
            - MQPL_UNIX
            - MQPL_WINDOWS_NT
            - MQPL_ZOS
        - name: PubSubClus
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPSCLUS_ENABLED
            - MQPSCLUS_DISABLED
        - name: PubSubMaxMsgRetryCount
          pcf_type: MQCFIN
          type_hint: int
        - name: PubSubMode
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPSM_COMPAT
            - MQPSM_DISABLED
            - MQPSM_ENABLED
        - name: PubSubNPInputMsg
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQUNDELIVERED_DISCARD
            - MQUNDELIVERED_KEEP
        - name: PubSubNPResponse
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQUNDELIVERED_NORMAL
            - MQUNDELIVERED_SAFE
            - MQUNDELIVERED_DISCARD
            - MQUNDELIVERED_KEEP
        - name: PubSubSyncPoint
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSYNCPOINT_IFPER
            - MQSYNCPOINT_YES
        - name: QMgrDesc
          pcf_type: MQCFST
          type_hint: str
        - name: QMgrIdentifier
          pcf_type: MQCFST
          type_hint: str
        - name: QMgrName
          pcf_type: MQCFST
          type_hint: str
        - name: QSGCertificateLabel
          pcf_type: MQCFST
          type_hint: str
        - name: QSGName
          pcf_type: MQCFST
          type_hint: str
        - name: QueueAccounting
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_NONE
            - MQMON_OFF
            - MQMON_ON
        - name: QueueMonitoring
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_OFF
            - MQMON_NONE
            - MQMON_LOW
            - MQMON_MEDIUM
            - MQMON_HIGH
        - name: QueueStatistics
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_NONE
            - MQMON_OFF
            - MQMON_ON
        - name: ReceiveTimeout
          pcf_type: MQCFIN
          type_hint: int
        - name: ReceiveTimeoutMin
          pcf_type: MQCFIN
          type_hint: int
        - name: ReceiveTimeoutType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQRCVTIME_MULTIPLY
            - MQRCVTIME_ADD
            - MQRCVTIME_EQUAL
        - name: RemoteEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
        - name: RepositoryName
          pcf_type: MQCFST
          type_hint: str
        - name: RepositoryNamelist
          pcf_type: MQCFST
          type_hint: str
        - name: RevDns
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQRDNS_DISABLED
            - MQRDNS_ENABLED
        - name: SecurityCase
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSCYC_UPPER
            - MQSCYC_MIXED
        - name: SharedQQmgrName
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSQQM_USE
            - MQSQQM_IGNORE
        - name: Splcap
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCAP_SUPPORTED
            - MQCAP_NOT_SUPPORTED
        - name: SSLCRLNamelist
          pcf_type: MQCFST
          type_hint: str
        - name: SSLCryptoHardware
          pcf_type: MQCFST
          type_hint: str
        - name: SSLEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
        - name: SSLFipsRequired
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSSL_FIPS_NO
            - MQSSL_FIPS_YES
        - name: SSLKeyRepository
          pcf_type: MQCFST
          type_hint: str
        - name: SSLKeyRepositoryPassword
          pcf_type: MQCFST
          type_hint: str
        - name: SSLKeyResetCount
          pcf_type: MQCFIN
          type_hint: int
        - name: SSLTasks
          pcf_type: MQCFIN
          type_hint: int
        - name: StartStopEvent
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQEVR_DISABLED
            - MQEVR_ENABLED
        - name: StatisticsInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: SyncPoint
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSP_AVAILABLE
            - MQSP_NOT_AVAILABLE
        - name: TCPChannels
          pcf_type: MQCFIN
          type_hint: int
        - name: TCPKeepAlive
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQTCPKEEP_YES
            - MQTCPKEEP_NO
        - name: TCPName
          pcf_type: MQCFST
          type_hint: str
        - name: TCPStackType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQTCPSTACK_SINGLE
            - MQTCPSTACK_MULTIPLE
        - name: TraceRouteRecording
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQRECORDING_DISABLED
            - MQRECORDING_MSG
            - MQRECORDING_Q
        - name: TreeLifeTime
          pcf_type: MQCFIN
          type_hint: int
        - name: TriggerInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: Version
          pcf_type: MQCFST
          type_hint: str
        - name: XrCapability
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
          - QMgrAttrs
      response:
        suggested:
          OTELTRAC: OTELTrace
        ambiguous:
          {}
        unmapped:
          - DEFCLXQ
          - OTELPCTL
        pcf_unmapped:
          - AMQPCapability
          - AccountingConnOverride
          - AccountingInterval
          - ActivityConnOverride
          - ActivityRecording
          - ActivityTrace
          - AdoptNewMCACheck
          - AdoptNewMCAType
          - AdvancedCapability
          - AlterationDate
          - AlterationTime
          - AuthorityEvent
          - BridgeEvent
          - CFConlos
          - CLWLMRUChannels
          - CLWLUseQ
          - CertificateLabel
          - CertificateValPolicy
          - ChannelAuthenticationRecords
          - ChannelAutoDef
          - ChannelAutoDefEvent
          - ChannelAutoDefExit
          - ChannelEvent
          - ChannelInitiatorControl
          - ChannelMonitoring
          - ChannelStatistics
          - ChinitAdapters
          - ChinitDispatchers
          - ChinitServiceParm
          - ChinitTraceAutoStart
          - ChinitTraceTableSize
          - ClusterSenderMonitoringDefault
          - ClusterSenderStatistics
          - ClusterWorkLoadData
          - ClusterWorkLoadExit
          - ClusterWorkLoadLength
          - CodedCharSetId
          - CommandEvent
          - CommandInputQName
          - CommandLevel
          - CommandServerControl
          - ConfigurationEvent
          - ConnAuth
          - CreationDate
          - CreationTime
          - Custom
          - DNSGroup
          - DNSWLM
          - DeadLetterQName
          - DefClusterXmitQueueType
          - DefXmitQName
          - DistLists
          - EncryptionPolicySuiteB
          - ExpiryInterval
          - GroupUR
          - IGQPutAuthority
          - IGQUserId
          - IPAddressVersion
          - ImageInterval
          - ImageLogLength
          - ImageRecoverObject
          - ImageRecoverQueue
          - ImageSchedule
          - InhibitEvent
          - InitialKey
          - IntraGroupQueuing
          - LU62ARMSuffix
          - LU62Channels
          - LUGroupName
          - LUName
          - ListenerTimer
          - LocalEvent
          - LoggerEvent
          - MQIAccounting
          - MQIStatistics
          - MaxActiveChannels
          - MaxChannels
          - MaxHandles
          - MaxMsgLength
          - MaxPriority
          - MaxPropertiesLength
          - MaxUncommittedMsgs
          - MsgMarkBrowseInterval
          - OTELPropagationControl
          - OutboundPortMax
          - OutboundPortMin
          - Parent
          - PerformanceEvent
          - Platform
          - PubSubClus
          - PubSubMaxMsgRetryCount
          - PubSubMode
          - PubSubNPInputMsg
          - PubSubNPResponse
          - PubSubSyncPoint
          - QMgrDesc
          - QMgrIdentifier
          - QMgrName
          - QSGCertificateLabel
          - QSGName
          - QueueAccounting
          - QueueMonitoring
          - QueueStatistics
          - ReceiveTimeout
          - ReceiveTimeoutMin
          - ReceiveTimeoutType
          - RemoteEvent
          - RepositoryName
          - RepositoryNamelist
          - RevDns
          - SSLCRLNamelist
          - SSLCryptoHardware
          - SSLEvent
          - SSLFipsRequired
          - SSLKeyRepository
          - SSLKeyRepositoryPassword
          - SSLKeyResetCount
          - SSLTasks
          - SecurityCase
          - SharedQQmgrName
          - Splcap
          - StartStopEvent
          - StatisticsInterval
          - SyncPoint
          - TCPChannels
          - TCPKeepAlive
          - TCPName
          - TCPStackType
          - TraceRouteRecording
          - TreeLifeTime
          - TriggerInterval
          - Version
          - XrCapability
    notes: []
  - mqsc:
      name: DISPLAY QMSTATUS
      href: SSFKSJ_9.4.0/refadmin/q086250_.html
      positional_parameters: []
      input_parameters: []
      output_parameters:
        - LDAPCONN
        - QMFSUSE
        - SHARED
        - TYPE(REDUCELOG)
      section_sources:
        'Requested parameters for TYPE(NATIVEHA)':
          - ACTIVE
          - LEADER
          - REPLICA
          - UNKNOWN
    pcf:
      command: MQCMD_INQUIRE_Q_MGR_STATUS
      request_href: SSFKSJ_9.4.0/refadmin/q087840_.html
      response_href: SSFKSJ_9.4.0/refadmin/q087850_.html
      request_parameters:
        - name: IntegerFilterCommand
          pcf_type: MQCFIF
          type_hint: null
        - name: NativeHAType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQNHATYPE_INSTANCE
            - MQNHATYPE_GROUP
            - MQNHATYPE_ALL
        - name: QMStatusAttrs
          pcf_type: MQCFIL
          type_hint: int
          enum_values:
            - MQIACF_ALL
            - MQCA_Q_MGR_NAME
            - MQCA_INSTALLATION_DESC
            - MQCA_INSTALLATION_NAME
            - MQCA_INSTALLATION_PATH
            - MQCACF_ARCHIVE_LOG_EXTENT_NAME
            - MQCACF_CURRENT_LOG_EXTENT_NAME
            - MQCACF_DISK_WRITTEN_LSN
            - MQCACF_HOST_NAME
            - MQCACF_LOG_PATH
            - MQCACF_LOG_START_DATE
            - MQCACF_LOG_START_LSN
            - MQCACF_LOG_START_TIME
            - MQCACF_MEDIA_LOG_EXTENT_NAME
            - MQCACF_NHA_GROUP_LSN
            - MQCACF_NHA_GROUP_NAME
            - MQCACF_NHA_INSTANCE_NAME
            - MQCACF_RESTART_LOG_EXTENT_NAME
            - MQCACF_Q_MGR_DATA_PATH
            - MQCACF_Q_MGR_START_DATE
            - MQCACF_Q_MGR_START_TIME
            - MQCACF_UNIFORM_CLUSTER_NAME
            - MQIACF_ARCHIVE_LOG_SIZE
            - MQIACF_AUTO_CLUSTER_TYPE
            - MQIACF_CHECKPOINT_COUNT
            - MQIACF_CHECKPOINT_OPERATIONS
            - MQIACF_CHECKPOINT_SIZE
            - MQIACF_CHINIT_STATUS
            - MQIACF_CMD_SERVER_STATUS
            - MQIACF_CONNECTION_COUNT
            - MQIACF_DATA_FS_SIZE
            - MQIACF_DATA_FS_IN_USE
            - MQIACF_LDAP_CONNECTION_STATUS
            - MQIACF_LOG_EXTENT_SIZE
            - MQIACF_LOG_FS_SIZE
            - MQIACF_LOG_FS_IN_USE
            - MQIACF_LOG_IN_USE
            - MQIACF_LOG_PRIMARIES
            - MQIACF_LOG_SECONDARIES
            - MQIACF_LOG_TYPE
            - MQIACF_LOG_UTILIZATION
            - MQIACF_MEDIA_LOG_SIZE
            - MQIACF_NHA_GROUP_ROLE
            - MQIACF_NHA_IN_SYNC_INSTANCES
            - MQIACF_NHA_TOTAL_INSTANCES
            - MQIACF_PERMIT_STANDBY
            - MQIACF_Q_MGR_FS_ENCRYPTED
            - MQIACF_Q_MGR_FS_SIZE
            - MQIACF_Q_MGR_FS_IN_USE
            - MQIACF_Q_MGR_STATUS
            - MQIACF_Q_MGR_STATUS_LOG
            - MQIACF_RESTART_LOG_SIZE
            - MQIACF_REUSABLE_LOG_SIZE
            - MQCA_VERSION
            - MQCACF_NHA_ACKNOWLEDGED_LSN
            - MQCACF_NHA_GROUP_ADDRESS
            - MQCACF_NHA_GROUP_INITIAL_DATE
            - MQCACF_NHA_GROUP_INITIAL_LSN
            - MQCACF_NHA_GROUP_INITIAL_TIME
            - MQCACF_NHA_REPL_ADDRESS
            - MQCACF_NHA_SYNC_ISOTIME
            - MQIACF_NHA_GROUP_BACKLOG
            - MQIACF_NHA_GROUP_CONNECTED
            - MQIACF_NHA_GROUP_IN_SYNC
            - MQCACF_NHA_GROUP_INIT_ISOTIME
            - MQCACF_NHA_GROUP_LIVE_ISOTIME
            - MQCACF_NHA_GROUP_RECOV_LSN
            - MQCACF_NHA_GROUP_RECOV_ISOTIME
            - MQCACF_NHA_GROUP_SYNC_ISOTIME
            - MQIACF_NHA_GROUP_STATUS
            - MQIACF_NHA_INSTANCE_ACTV_CONNS
            - MQIACF_NHA_INSTANCE_BACKLOG
            - MQIACF_NHA_INSTANCE_IN_SYNC
            - MQIACF_NHA_INSTANCE_ROLE
            - MQIACF_NHA_INSTANCE_STATUS
            - MQIACF_NHA_TYPE
        - name: StatusType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQIACF_Q_MGR_STATUS_INFO_Q_MGR
            - MQIACF_Q_MGR_STATUS_INFO_NHA
        - name: StringFilterCommand
          pcf_type: MQCFSF
          type_hint: null
          enum_values:
            - MQRCCF_NHA_NOT_AVAILABLE
      response_parameters:
        - name: ArchiveLog
          pcf_type: MQCFST
          type_hint: str
        - name: ArchiveLogSize
          pcf_type: MQCFIN
          type_hint: int
        - name: AutoCluster
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQAUTOCLUS_TYPE_NONE
            - MQAUTOCLUS_TYPE_UNIFORM
        - name: ChannelInitiatorStatus
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSVC_STATUS_STOPPED
            - MQSVC_STATUS_STARTING
            - MQSVC_STATUS_RUNNING
            - MQSVC_STATUS_STOPPING
        - name: ChkptCnt
          pcf_type: MQCFIN
          type_hint: int
        - name: ChkptOps
          pcf_type: MQCFIN
          type_hint: int
        - name: ChkptSz
          pcf_type: MQCFIN
          type_hint: int
        - name: CommandServerStatus
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSVC_STATUS_STARTING
            - MQSVC_STATUS_RUNNING
            - MQSVC_STATUS_STOPPING
        - name: ConnectionCount
          pcf_type: MQCFIN
          type_hint: int
        - name: CurrentLog
          pcf_type: MQCFST
          type_hint: str
        - name: DataFSSize
          pcf_type: MQCFIN
          type_hint: int
        - name: DataFSUse
          pcf_type: MQCFIN
          type_hint: int
        - name: DataPath
          pcf_type: MQCFST
          type_hint: str
        - name: DiskLsn
          pcf_type: MQCFST
          type_hint: str
        - name: GrpLsn
          pcf_type: MQCFST
          type_hint: str
        - name: GrpName
          pcf_type: MQCFST
          type_hint: str
        - name: GrpRole
          pcf_type: MQCFIN
          type_hint: int
        - name: HostName
          pcf_type: MQCFST
          type_hint: str
        - name: InstallationDesc
          pcf_type: MQCFST
          type_hint: str
        - name: InstallationName
          pcf_type: MQCFST
          type_hint: str
        - name: InstallationPath
          pcf_type: MQCFST
          type_hint: str
        - name: InSyncInstances
          pcf_type: MQCFIN
          type_hint: int
        - name: LDAPConnectionStatus
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQLDAPC_CONNECTED
            - MQLDAPC_ERROR
            - MQLDAPC_INACTIVE
        - name: LogExtSize
          pcf_type: MQCFIN
          type_hint: int
        - name: LogFSSize
          pcf_type: MQCFIN
          type_hint: int
        - name: LogFSUse
          pcf_type: MQCFIN
          type_hint: int
        - name: LogInUse
          pcf_type: MQCFIN
          type_hint: int
        - name: LogPath
          pcf_type: MQCFST
          type_hint: str
        - name: LogPrim
          pcf_type: MQCFIN
          type_hint: int
        - name: LogSec
          pcf_type: MQCFIN
          type_hint: int
        - name: LogStartDate
          pcf_type: MQCFST
          type_hint: str
        - name: LogStartLSN
          pcf_type: MQCFST
          type_hint: str
        - name: LogStartTime
          pcf_type: MQCFST
          type_hint: str
        - name: LogType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQLOGTYPE_CIRCULAR
            - MQLOGTYPE_LINEAR
            - MQLOGTYPE_REPLICATED
        - name: LogUtilization
          pcf_type: MQCFIN
          type_hint: int
        - name: MediaRecoveryLog
          pcf_type: MQCFST
          type_hint: str
        - name: MediaRecoveryLogSize
          pcf_type: MQCFIN
          type_hint: int
        - name: NativeHAInstanceName
          pcf_type: MQCFST
          type_hint: str
        - name: PermitStandby
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSTDBY_NOT_PERMITTED
            - MQSTDBY_PERMITTED
        - name: QMgrName
          pcf_type: MQCFST
          type_hint: str
        - name: QMgrStatus
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQMSTA_STARTING
            - MQQMSTA_RUNNING
            - MQQMSTA_QUIESCING
        - name: QMgrEncryption
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQFSENC_NO
            - MQFSENC_YES
            - MQFSENC_UNKNOWN
        - name: QMgrFSSize
          pcf_type: MQCFIN
          type_hint: int
        - name: QMgrFSUse
          pcf_type: MQCFIN
          type_hint: int
        - name: RestartRecoveryLog
          pcf_type: MQCFST
          type_hint: str
        - name: RestartRecoveryLogSize
          pcf_type: MQCFIN
          type_hint: int
        - name: ReusableLogSize
          pcf_type: MQCFIN
          type_hint: int
        - name: StartDate
          pcf_type: MQCFST
          type_hint: str
        - name: StartTime
          pcf_type: MQCFST
          type_hint: str
        - name: StatusType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQIACF_Q_MGR_STATUS_INFO_Q_MGR
        - name: TotalInstances
          pcf_type: MQCFIN
          type_hint: int
        - name: UniClusterName
          pcf_type: MQCFST
          type_hint: str
        - name: AckLsn
          pcf_type: MQCFST
          type_hint: str
        - name: Backlog
          pcf_type: MQCFIN
          type_hint: int
        - name: GroupBacklog
          pcf_type: MQCFIN
          type_hint: int
        - name: ConnActv
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQNHACONNACTV_NO
            - MQNHACONNACTV_YES
        - name: ConnGrp
          pcf_type: MQCFIN
          type_hint: int
        - name: GrpAddr
          pcf_type: MQCFIN
          type_hint: int
        - name: GrpName
          pcf_type: MQCFST
          type_hint: str
        - name: GrpRole
          pcf_type: MQCFIN
          type_hint: int
        - name: GrpStatus
          pcf_type: MQCFIN
          type_hint: int
        - name: GrpVer
          pcf_type: MQCFST
          type_hint: str
        - name: HAInitDate
          pcf_type: MQCFST
          type_hint: str
        - name: HAInitLSN
          pcf_type: MQCFST
          type_hint: str
        - name: HAInitTime
          pcf_type: MQCFST
          type_hint: str
        - name: HAStatus
          pcf_type: MQCFIN
          type_hint: int
        - name: InitLsn
          pcf_type: MQCFST
          type_hint: str
        - name: InitTime
          pcf_type: MQCFST
          type_hint: str
        - name: InSync
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQNHAINSYNC_NO
            - MQNHAINSYNC_YES
        - name: Instance
          pcf_type: MQCFST
          type_hint: str
        - name: LiveTime
          pcf_type: MQCFST
          type_hint: str
        - name: NhaType
          pcf_type: MQCFST
          type_hint: str
          enum_values:
            - MQNHATYPE_INSTANCE
            - MQNHATYPE_GROUP
        - name: RcovLsn
          pcf_type: MQCFST
          type_hint: str
        - name: RcovTime
          pcf_type: MQCFST
          type_hint: str
        - name: ReplAddr
          pcf_type: MQCFST
          type_hint: str
        - name: Role
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQNHAROLE_UNKNOWN
            - MQNHAROLE_ACTIVE
            - MQNHAROLE_LEADER
            - MQNHAROLE_REPLICA
        - name: SyncTime
          pcf_type: MQCFST
          type_hint: str
        - name: StatusType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQIACF_Q_MGR_STATUS_INFO_NHA
    mapping:
      request:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - IntegerFilterCommand
          - NativeHAType
          - QMStatusAttrs
          - StatusType
          - StringFilterCommand
      response:
        suggested:
          {}
        ambiguous:
          {}
        unmapped:
          - ACTIVE
          - LEADER
          - REPLICA
          - UNKNOWN
        pcf_unmapped:
          - AckLsn
          - ArchiveLog
          - ArchiveLogSize
          - AutoCluster
          - Backlog
          - ChannelInitiatorStatus
          - ChkptCnt
          - ChkptOps
          - ChkptSz
          - CommandServerStatus
          - ConnActv
          - ConnGrp
          - ConnectionCount
          - CurrentLog
          - DataFSSize
          - DataFSUse
          - DataPath
          - DiskLsn
          - GroupBacklog
          - GrpAddr
          - GrpLsn
          - GrpName
          - GrpName
          - GrpRole
          - GrpRole
          - GrpStatus
          - GrpVer
          - HAInitDate
          - HAInitLSN
          - HAInitTime
          - HAStatus
          - HostName
          - InSync
          - InSyncInstances
          - InitLsn
          - InitTime
          - InstallationDesc
          - InstallationName
          - InstallationPath
          - Instance
          - LDAPConnectionStatus
          - LiveTime
          - LogExtSize
          - LogFSSize
          - LogFSUse
          - LogInUse
          - LogPath
          - LogPrim
          - LogSec
          - LogStartDate
          - LogStartLSN
          - LogStartTime
          - LogType
          - LogUtilization
          - MediaRecoveryLog
          - MediaRecoveryLogSize
          - NativeHAInstanceName
          - NhaType
          - PermitStandby
          - QMgrEncryption
          - QMgrFSSize
          - QMgrFSUse
          - QMgrName
          - QMgrStatus
          - RcovLsn
          - RcovTime
          - ReplAddr
          - RestartRecoveryLog
          - RestartRecoveryLogSize
          - ReusableLogSize
          - Role
          - StartDate
          - StartTime
          - StatusType
          - StatusType
          - SyncTime
          - TotalInstances
          - UniClusterName
    notes: []
  - mqsc:
      name: PING QMGR
      href: SSFKSJ_9.4.0/refadmin/q086440_.html
      positional_parameters: []
      input_parameters: []
      output_parameters: []
      section_sources:
        {}
    pcf:
      command: MQCMD_PING_Q_MGR
      request_href: SSFKSJ_9.4.0/refadmin/q088200_.html
      response_href: SSFKSJ_9.4.0/refadmin/q088200_.html
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
      name: REFRESH QMGR
      href: SSFKSJ_9.4.0/refadmin/q086480_.html
      positional_parameters:
        - (generic-object-name)
        - (integer)
        - (objtype)
        - qmgr-name
      input_parameters: []
      output_parameters: []
      section_sources:
        {}
    pcf:
      command: MQCMD_REFRESH_Q_MGR
      request_href: SSFKSJ_9.4.0/refadmin/q088240_.html
      response_href: SSFKSJ_9.4.0/refadmin/q088240_.html
      request_parameters:
        - name: RefreshType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQRT_CONFIGURATION
            - MQRT_EXPIRY
            - MQRT_EARLY
            - MQRT_PROXYSUB
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: ObjectName
          pcf_type: MQCFST
          type_hint: str
        - name: ObjectType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQOT_AUTH_INFO
            - MQOT_CF_STRUC
            - MQOT_CHANNEL
            - MQOT_CHLAUTH
            - MQOT_LISTENER
            - MQOT_NAMELIST
            - MQOT_PROCESS
            - MQOT_Q
            - MQOT_LOCAL_Q
            - MQOT_MODEL_Q
            - MQOT_ALIAS_Q
            - MQOT_REMOTE_Q
            - MQOT_Q_MGR
            - MQOT_CFSTRUC
            - MQOT_SERVICE
            - MQOT_STORAGE_CLASS
            - MQOT_TOPIC
        - name: RefreshInterval
          pcf_type: MQCFIN
          type_hint: int
      response_parameters:
        - name: RefreshType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQRT_CONFIGURATION
            - MQRT_EXPIRY
            - MQRT_EARLY
            - MQRT_PROXYSUB
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: ObjectName
          pcf_type: MQCFST
          type_hint: str
        - name: ObjectType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQOT_AUTH_INFO
            - MQOT_CF_STRUC
            - MQOT_CHANNEL
            - MQOT_CHLAUTH
            - MQOT_LISTENER
            - MQOT_NAMELIST
            - MQOT_PROCESS
            - MQOT_Q
            - MQOT_LOCAL_Q
            - MQOT_MODEL_Q
            - MQOT_ALIAS_Q
            - MQOT_REMOTE_Q
            - MQOT_Q_MGR
            - MQOT_CFSTRUC
            - MQOT_SERVICE
            - MQOT_STORAGE_CLASS
            - MQOT_TOPIC
        - name: RefreshInterval
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
          - ObjectName
          - ObjectType
          - RefreshInterval
          - RefreshType
      response:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - CommandScope
          - ObjectName
          - ObjectType
          - RefreshInterval
          - RefreshType
    notes: []
  - mqsc:
      name: RESET QMGR
      href: SSFKSJ_9.4.0/refadmin/q086530_.html
      positional_parameters:
        - name
        - qmgr-name
      input_parameters: []
      output_parameters: []
      section_sources:
        {}
    pcf:
      command: MQCMD_RESET_Q_MGR
      request_href: SSFKSJ_9.4.0/refadmin/q088290_.html
      response_href: SSFKSJ_9.4.0/refadmin/q088290_.html
      request_parameters:
        - name: Action
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQACT_ADVANCE_LOG
            - MQACT_COLLECT_STATISTICS
            - MQACT_PUBSUB
        - name: ArchivedLog
          pcf_type: MQCFST
          type_hint: str
        - name: ChildName
          pcf_type: MQCFST
          type_hint: str
        - name: ParentName
          pcf_type: MQCFST
          type_hint: str
        - name: LogReduction
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQLR_AUTO
            - MQLR_ONE
            - MQLR_MAX
            - MQRCCF_CURRENT_LOG_EXTENT
            - MQRCCF_LOG_EXTENT_NOT_FOUND
            - MQRCCF_LOG_NOT_REDUCED
            - MQRC_RESOURCE_PROBLEM
      response_parameters:
        - name: Action
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQACT_ADVANCE_LOG
            - MQACT_COLLECT_STATISTICS
            - MQACT_PUBSUB
        - name: ArchivedLog
          pcf_type: MQCFST
          type_hint: str
        - name: ChildName
          pcf_type: MQCFST
          type_hint: str
        - name: ParentName
          pcf_type: MQCFST
          type_hint: str
        - name: LogReduction
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQLR_AUTO
            - MQLR_ONE
            - MQLR_MAX
            - MQRCCF_CURRENT_LOG_EXTENT
            - MQRCCF_LOG_EXTENT_NOT_FOUND
            - MQRCCF_LOG_NOT_REDUCED
            - MQRC_RESOURCE_PROBLEM
    mapping:
      request:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - Action
          - ArchivedLog
          - ChildName
          - LogReduction
          - ParentName
      response:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - Action
          - ArchivedLog
          - ChildName
          - LogReduction
          - ParentName
    notes: []
  - mqsc:
      name: RESUME QMGR
      href: SSFKSJ_9.4.0/refadmin/q086590_.html
      positional_parameters:
        - (clustername)
        - (nlname)
        - qmgr-name
      input_parameters: []
      output_parameters: []
      section_sources:
        {}
    pcf:
      command: MQCMD_RESUME_Q_MGR
      request_href: SSFKSJ_9.4.0/refadmin/q088340_.html
      response_href: SSFKSJ_9.4.0/refadmin/q088340_.html
      request_parameters:
        - name: Facility
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQMFAC_DB2
            - MQQMFAC_IMS_BRIDGE
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
      response_parameters:
        - name: Facility
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQMFAC_DB2
            - MQQMFAC_IMS_BRIDGE
        - name: CommandScope
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
          - CommandScope
          - Facility
      response:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - CommandScope
          - Facility
    notes: []
  - mqsc:
      name: START QMGR
      href: SSFKSJ_9.4.0/refadmin/q086710_.html
      positional_parameters:
        - backward-migration-target-vrm
        - jcl-substitution
        - member-name
      input_parameters: []
      output_parameters: []
      section_sources:
        {}
    pcf:
      command: MQCMD_START_Q_MGR
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
      name: STOP QMGR
      href: SSFKSJ_9.4.0/refadmin/q086810_.html
      positional_parameters:
        - qmgr-name
      input_parameters: []
      output_parameters: []
      section_sources:
        {}
    pcf:
      command: MQCMD_STOP_Q_MGR
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
      name: SUSPEND QMGR
      href: SSFKSJ_9.4.0/refadmin/q086850_.html
      positional_parameters:
        - (clustername)
        - (nlname)
        - qmgr-name
      input_parameters: []
      output_parameters: []
      section_sources:
        {}
    pcf:
      command: MQCMD_SUSPEND_Q_MGR
      request_href: SSFKSJ_9.4.0/refadmin/q088550_.html
      response_href: SSFKSJ_9.4.0/refadmin/q088550_.html
      request_parameters:
        - name: Facility
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQMFAC_DB2
            - MQQMFAC_IMS_BRIDGE
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
      response_parameters:
        - name: Facility
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQMFAC_DB2
            - MQQMFAC_IMS_BRIDGE
        - name: CommandScope
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
          - CommandScope
          - Facility
      response:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - CommandScope
          - Facility
    notes: []
```













## Output-parameter refresh
```yaml
version: 1
generated_at: 2026-01-27T20:30:57Z
commands:
  - name: DISPLAY QMGR
    output_parameters:
      - ACCTQ
      - ACCTQMQI
      - ACTVTRC
      - ADOPTCHK
      - ADVCAP
      - ALL
      - CFCONLOS
      - CLWLUSEQ
      - DEFCLXQ
      - MAXUMSGS
      - OTELPCTL
      - OTELTRAC
      - QMGRPROD
      - RCVTIME
      - RCVTTYPE
      - SQQMNAME
      - SSLCRLNL
  - name: DISPLAY QMSTATUS
    output_parameters:
      - LDAPCONN
      - QMFSUSE
      - SHARED
      - TYPE(REDUCELOG)
```
