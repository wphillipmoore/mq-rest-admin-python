# MQSC to PCF parameter extraction: Clusqmgr

## Table of Contents

- [Purpose](#purpose)
- [First-run extraction](#first-run-extraction)

## Purpose

Collect MQSC and PCF parameter mappings for clusqmgr commands, split from the first-run extraction to keep each qualifier readable.

## First-run extraction

```yaml
version: 1
generated_at: 2026-01-11T23:40:29Z
commands:
  - mqsc:
      name: DISPLAY CLUSQMGR
      href: SSFKSJ_9.4.0/refadmin/q086110_.html
      positional_parameters:
        - filter-keyword
        - filter-value
        - generic-name
        - generic-qmgr-name
        - qmgr-name
      input_parameters: []
      output_parameters:
        - ALTDATE
        - ALTTIME
        - BATCHHB
        - BATCHINT
        - BATCHLIM
        - BATCHSZ
        - CLUSDATE
        - CLUSTIME
        - CLWLPRTY
        - CLWLRANK
        - CLWLWGHT
        - COMPHDR
        - COMPMSG
        - CONNAME
        - CONVERT
        - DEFTYPE
        - DESCR
        - DISCINT
        - HBINT
        - KAINT
        - LOCLADDR
        - LONGRTY
        - LONGTMR
        - MAXMSGL
        - MCANAME
        - MCATYPE
        - MCAUSER
        - MODENAME
        - MRDATA
        - MREXIT
        - MRRTY
        - MRTMR
        - MSGDATA
        - MSGEXIT
        - NETPRTY
        - NPMSPEED
        - PASSWORD
        - PROPCTL
        - PUTAUT
        - QMID
        - QMTYPE
        - RCVDATA
        - RCVEXIT
        - SCYDATA
        - SCYEXIT
        - SENDDATA
        - SENDEXIT
        - SEQWRAP
        - SHORTRTY
        - SHORTTMR
        - SSLCAUTH
        - SSLCIPH
        - SSLPEER
        - STATUS
        - SUSPEND
        - TPNAME
        - TRPTYPE
        - USEDLQ
        - USERID
        - VERSION
        - XMITQ
      section_sources:
        {}
    pcf:
      command: MQCMD_INQUIRE_CLUSTER_Q_MGR
      request_href: SSFKSJ_9.4.0/refadmin/q087580_.html
      response_href: SSFKSJ_9.4.0/refadmin/q087590_.html
      request_parameters:
        - name: ClusterQMgrName
          pcf_type: MQCFST
          type_hint: str
        - name: Channel
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterName
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterQMgrAttrs
          pcf_type: MQCFIL
          type_hint: int
          enum_values:
            - MQIACF_ALL
            - MQCA_ALTERATION_DATE
            - MQCA_ALTERATION_TIME
            - MQCA_CLUSTER_DATE
            - MQCA_CLUSTER_NAME
            - MQCA_CLUSTER_Q_MGR_NAME
            - MQCA_CLUSTER_TIME
            - MQCA_Q_MGR_IDENTIFIER
            - MQCA_VERSION
            - MQCA_XMIT_Q_NAME
            - MQCACH_CONNECTION_NAME
            - MQCACH_DESCRIPTION
            - MQCACH_LOCAL_ADDRESS
            - MQCACH_MCA_NAME
            - MQCACH_MCA_USER_ID
            - MQCACH_MODE_NAME
            - MQCACH_MR_EXIT_NAME
            - MQCACH_MR_EXIT_USER_DATA
            - MQCACH_MSG_EXIT_NAME
            - MQCACH_MSG_EXIT_USER_DATA
            - MQCACH_PASSWORD
            - MQCACH_RCV_EXIT_NAME
            - MQCACH_RCV_EXIT_USER_DATA
            - MQCACH_SEC_EXIT_NAME
            - MQCACH_SEC_EXIT_USER_DATA
            - MQCACH_SEND_EXIT_NAME
            - MQCACH_SEND_EXIT_USER_DATA
            - MQCACH_SSL_CIPHER_SPEC
            - MQIACH_SSL_CLIENT_AUTH
            - MQCACH_SSL_PEER_NAME
            - MQCACH_TP_NAME
            - MQCACH_USER_ID
            - MQIA_MONITORING_CHANNEL
            - MQIA_USE_DEAD_LETTER_Q
            - MQIACF_Q_MGR_DEFINITION_TYPE
            - MQIACF_Q_MGR_TYPE
            - MQIACF_SUSPEND
            - MQIACH_BATCH_HB
            - MQIACH_BATCH_INTERVAL
            - MQIACH_BATCH_DATA_LIMIT
            - MQIACH_BATCH_SIZE
            - MQIACH_CHANNEL_STATUS
            - MQIACH_CLWL_CHANNEL_PRIORITY
            - MQIACH_CLWL_CHANNEL_RANK
            - MQIACH_CLWL_CHANNEL_WEIGHT
            - MQIACH_DATA_CONVERSION
            - MQIACH_DISC_INTERVAL
            - MQIACH_HB_INTERVAL
            - MQIACH_HDR_COMPRESSION
            - MQIACH_KEEP_ALIVE_INTERVAL
            - MQIACH_LONG_RETRY
            - MQIACH_LONG_TIMER
            - MQIACH_MAX_MSG_LENGTH
            - MQIACH_MCA_TYPE
            - MQIACH_MR_COUNT
            - MQIACH_MR_INTERVAL
            - MQIACH_MSG_COMPRESSION
            - MQIACH_NETWORK_PRIORITY
            - MQIACH_NPM_SPEED
            - MQIACH_PUT_AUTHORITY
            - MQIACH_SEQUENCE_NUMBER_WRAP
            - MQIACH_SHORT_RETRY
            - MQIACH_SHORT_TIMER
            - MQIACH_XMIT_PROTOCOL_TYPE
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: IntegerFilterCommand
          pcf_type: MQCFIF
          type_hint: null
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
        - name: BatchHeartbeat
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchSize
          pcf_type: MQCFIN
          type_hint: int
        - name: ChannelDesc
          pcf_type: MQCFST
          type_hint: str
        - name: ChannelMonitoring
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_OFF
            - MQMON_Q_MGR
            - MQMON_LOW
            - MQMON_MEDIUM
            - MQMON_HIGH
        - name: ChannelName
          pcf_type: MQCFST
          type_hint: str
        - name: ChannelStatus
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHS_BINDING
            - MQCHS_INACTIVE
            - MQCHS_STARTING
            - MQCHS_RUNNING
            - MQCHS_PAUSED
            - MQCHS_STOPPING
            - MQCHS_RETRYING
            - MQCHS_STOPPED
            - MQCHS_REQUESTING
            - MQCHS_INITIALIZING
        - name: ClusterDate
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterInfo
          pcf_type: MQCFIN
          type_hint: int
        - name: ClusterName
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterTime
          pcf_type: MQCFST
          type_hint: str
        - name: CLWLChannelPriority
          pcf_type: MQCFIN
          type_hint: int
        - name: CLWLChannelRank
          pcf_type: MQCFIN
          type_hint: int
        - name: CLWLChannelWeight
          pcf_type: MQCFIN
          type_hint: int
        - name: ConnectionName
          pcf_type: MQCFST
          type_hint: str
        - name: DataConversion
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCDC_NO_SENDER_CONVERSION
            - MQCDC_SENDER_CONVERSION
        - name: DiscInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: HeaderCompression
          pcf_type: MQCFIL
          type_hint: int
          enum_values:
            - MQCOMPRESS_NONE
            - MQCOMPRESS_SYSTEM
        - name: HeartbeatInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: KeepAliveInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: LocalAddress
          pcf_type: MQCFST
          type_hint: str
        - name: LongRetryCount
          pcf_type: MQCFIN
          type_hint: int
        - name: LongRetryInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxMsgLength
          pcf_type: MQCFIN
          type_hint: int
        - name: MCAName
          pcf_type: MQCFST
          type_hint: str
        - name: MCAType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMCAT_PROCESS
            - MQMCAT_THREAD
        - name: MCAUserIdentifier
          pcf_type: MQCFST
          type_hint: str
        - name: MessageCompression
          pcf_type: MQCFIL
          type_hint: int
          enum_values:
            - MQCOMPRESS_NONE
            - MQCOMPRESS_RLE
            - MQCOMPRESS_ZLIBFAST
            - MQCOMPRESS_ZLIBHIGH
        - name: ModeName
          pcf_type: MQCFST
          type_hint: str
        - name: MsgExit
          pcf_type: MQCFST
          type_hint: str
        - name: MsgRetryCount
          pcf_type: MQCFIN
          type_hint: int
        - name: MsgRetryExit
          pcf_type: MQCFST
          type_hint: str
        - name: MsgRetryInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: MsgRetryUserData
          pcf_type: MQCFST
          type_hint: str
        - name: MsgUserData
          pcf_type: MQCFST
          type_hint: str
        - name: NetworkPriority
          pcf_type: MQCFIN
          type_hint: int
        - name: NonPersistentMsgSpeed
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQNPMS_NORMAL
            - MQNPMS_FAST
        - name: Password
          pcf_type: MQCFST
          type_hint: str
        - name: PutAuthority
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPA_DEFAULT
            - MQPA_CONTEXT
            - MQPA_ALTERNATE_OR_MCA
            - MQPA_ONLY_MCA
        - name: QMgrDefinitionType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQMDT_EXPLICIT_CLUSTER_SENDER
            - MQQMDT_AUTO_CLUSTER_SENDER
            - MQQMDT_CLUSTER_RECEIVER
            - MQQMDT_AUTO_EXP_CLUSTER_SENDER
        - name: QMgrIdentifier
          pcf_type: MQCFST
          type_hint: str
        - name: QMgrName
          pcf_type: MQCFST
          type_hint: str
        - name: QMgrType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQMT_NORMAL
            - MQQMT_REPOSITORY
        - name: ReceiveExit
          pcf_type: MQCFST
          type_hint: str
        - name: ReceiveUserData
          pcf_type: MQCFST
          type_hint: str
        - name: SecurityExit
          pcf_type: MQCFST
          type_hint: str
        - name: SecurityUserData
          pcf_type: MQCFST
          type_hint: str
        - name: SendExit
          pcf_type: MQCFST
          type_hint: str
        - name: SendUserData
          pcf_type: MQCFST
          type_hint: str
        - name: SeqNumberWrap
          pcf_type: MQCFIN
          type_hint: int
        - name: ShortRetryCount
          pcf_type: MQCFIN
          type_hint: int
        - name: ShortRetryInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: SSLCipherSpec
          pcf_type: MQCFST
          type_hint: str
        - name: SSLClientAuth
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSCA_REQUIRED
            - MQSCA_OPTIONAL
        - name: SSLPeerName
          pcf_type: MQCFST
          type_hint: str
        - name: Suspend
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSUS_NO
            - MQSUS_YES
        - name: TpName
          pcf_type: MQCFST
          type_hint: str
        - name: TranmissionQName
          pcf_type: MQCFST
          type_hint: str
        - name: TransportType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQXPT_LU62
            - MQXPT_TCP
            - MQXPT_NETBIOS
            - MQXPT_SPX
            - MQXPT_DECNET
        - name: UseDLQ
          pcf_type: MQCFIN
          type_hint: int
        - name: UserIdentifier
          pcf_type: MQCFST
          type_hint: str
        - name: Version
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
          - Channel
          - ClusterName
          - ClusterQMgrAttrs
          - ClusterQMgrName
          - CommandScope
          - IntegerFilterCommand
          - StringFilterCommand
      response:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - AlterationDate
          - AlterationTime
          - BatchHeartbeat
          - BatchInterval
          - BatchSize
          - CLWLChannelPriority
          - CLWLChannelRank
          - CLWLChannelWeight
          - ChannelDesc
          - ChannelMonitoring
          - ChannelName
          - ChannelStatus
          - ClusterDate
          - ClusterInfo
          - ClusterName
          - ClusterTime
          - ConnectionName
          - DataConversion
          - DiscInterval
          - HeaderCompression
          - HeartbeatInterval
          - KeepAliveInterval
          - LocalAddress
          - LongRetryCount
          - LongRetryInterval
          - MCAName
          - MCAType
          - MCAUserIdentifier
          - MaxMsgLength
          - MessageCompression
          - ModeName
          - MsgExit
          - MsgRetryCount
          - MsgRetryExit
          - MsgRetryInterval
          - MsgRetryUserData
          - MsgUserData
          - NetworkPriority
          - NonPersistentMsgSpeed
          - Password
          - PutAuthority
          - QMgrDefinitionType
          - QMgrIdentifier
          - QMgrName
          - QMgrType
          - ReceiveExit
          - ReceiveUserData
          - SSLCipherSpec
          - SSLClientAuth
          - SSLPeerName
          - SecurityExit
          - SecurityUserData
          - SendExit
          - SendUserData
          - SeqNumberWrap
          - ShortRetryCount
          - ShortRetryInterval
          - Suspend
          - TpName
          - TranmissionQName
          - TransportType
          - UseDLQ
          - UserIdentifier
          - Version
    notes: []
```

## Output-parameter refresh

```yaml
version: 1
generated_at: 2026-02-02T19:46:59Z
commands:
  - name: DISPLAY CLUSQMGR
    output_parameters:
      - ALTDATE
      - ALTTIME
      - BATCHHB
      - BATCHINT
      - BATCHLIM
      - BATCHSZ
      - CLUSDATE
      - CLUSTIME
      - CLWLPRTY
      - CLWLRANK
      - CLWLWGHT
      - COMPHDR
      - COMPMSG
      - CONNAME
      - CONVERT
      - DEFTYPE
      - DESCR
      - DISCINT
      - HBINT
      - KAINT
      - LOCLADDR
      - LONGRTY
      - LONGTMR
      - MAXMSGL
      - MCANAME
      - MCATYPE
      - MCAUSER
      - MODENAME
      - MRDATA
      - MREXIT
      - MRRTY
      - MRTMR
      - MSGDATA
      - MSGEXIT
      - NETPRTY
      - NPMSPEED
      - PASSWORD
      - PROPCTL
      - PUTAUT
      - QMID
      - QMTYPE
      - RCVDATA
      - RCVEXIT
      - SCYDATA
      - SCYEXIT
      - SENDDATA
      - SENDEXIT
      - SEQWRAP
      - SHORTRTY
      - SHORTTMR
      - SSLCAUTH
      - SSLCIPH
      - SSLPEER
      - STATUS
      - SUSPEND
      - TPNAME
      - TRPTYPE
      - USEDLQ
      - USERID
      - VERSION
      - XMITQ
```
