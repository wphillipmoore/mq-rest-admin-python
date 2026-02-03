# MQSC to PCF parameter extraction: Channel

## Table of Contents

- [Purpose](#purpose)
- [First-run extraction](#first-run-extraction)
- [Channel command re-parse](#channel-command-re-parse)

## Purpose

Collect MQSC and PCF parameter mappings for channel commands, split from the first-run extraction to keep each qualifier readable.

## First-run extraction

```yaml
version: 1
generated_at: 2026-01-11T23:40:29Z
commands:
  - mqsc:
      name: ALTER CHANNEL
      href: SSFKSJ_9.4.0/refadmin/q085170_.html
      positional_parameters:
        - (channel-name)
        - (string)
        - channel-name
        - clustername
        - integer
        - ip-addr
        - nlname
        - qmgr-name
        - string
      input_parameters:
        - AFFINITY
        - AMQPKA
        - BATCHHB
        - BATCHINT
        - BATCHLIM
        - BATCHSZ
        - CERTLABL
        - CHLTYPE
        - CLNTWGHT
        - CLUSNL
        - CLUSTER
        - CLWLPRTY
        - CLWLRANK
        - CLWLWGHT
        - CMDSCOPE
        - COMPHDR
        - COMPMSG
        - CONNAME
        - CONVERT
        - DEFCDISP
        - DEFRECON
        - DESCR
        - DISCINT
        - HBINT
        - KAINT
        - LIKE
        - LOCLADDR
        - LONGRTY
        - LONGTMR
        - MAXINST
        - MAXINSTC
        - MAXMSGL
        - MCANAME
        - MCATYPE
        - MCAUSER
        - MODENAME
        - MONCHL
        - MRDATA
        - MREXIT
        - MRRTY
        - MRTMR
        - MSGDATA
        - MSGEXIT
        - NETPRTY
        - NPMSPEED
        - PASSWORD
        - PORT
        - PROPCTL
        - PUTAUT
        - QMNAME
        - QSGDISP
        - RCVDATA
        - RCVEXIT
        - SCYDATA
        - SCYEXIT
        - SENDDATA
        - SENDEXIT
        - SEQWRAP
        - SHARECNV
        - SHORTRTY
        - SHORTTMR
        - SPLPROT
        - SSLCAUTH
        - SSLCIPH
        - SSLPEER
        - STATCHL
        - TMPMODEL
        - TMPQPRFX
        - TPNAME
        - TPROOT
        - TRPTYPE
        - USECLTID
        - USEDLQ
        - USERID
        - XMITQ
      output_parameters: []
      section_sources:
        'Parameter descriptions for ALTER CHANNEL':
          - AFFINITY
          - AMQPKA
          - BATCHHB
          - BATCHINT
          - BATCHLIM
          - BATCHSZ
          - CERTLABL
          - CHLTYPE
          - CLNTWGHT
          - CLUSNL
          - CLUSTER
          - CLWLPRTY
          - CLWLRANK
          - CLWLWGHT
          - CMDSCOPE
          - COMPHDR
          - COMPMSG
          - CONNAME
          - CONVERT
          - DEFCDISP
          - DEFRECON
          - DESCR
          - DISCINT
          - HBINT
          - KAINT
          - LIKE
          - LOCLADDR
          - LONGRTY
          - LONGTMR
          - MAXINST
          - MAXINSTC
          - MAXMSGL
          - MCANAME
          - MCATYPE
          - MCAUSER
          - MODENAME
          - MONCHL
          - MRDATA
          - MREXIT
          - MRRTY
          - MRTMR
          - MSGDATA
          - MSGEXIT
          - NETPRTY
          - NPMSPEED
          - PASSWORD
          - PORT
          - PROPCTL
          - PUTAUT
          - QMNAME
          - QSGDISP
          - RCVDATA
          - RCVEXIT
          - SCYDATA
          - SCYEXIT
          - SENDDATA
          - SENDEXIT
          - SEQWRAP
          - SHARECNV
          - SHORTRTY
          - SHORTTMR
          - SPLPROT
          - SSLCAUTH
          - SSLCIPH
          - SSLPEER
          - STATCHL
          - TMPMODEL
          - TMPQPRFX
          - TPNAME
          - TPROOT
          - TRPTYPE
          - USECLTID
          - USEDLQ
          - USERID
          - XMITQ
    pcf:
      command: MQCMD_CHANGE_CHANNEL
      request_href: SSFKSJ_9.4.0/refdev/q091020_.html
      response_href: SSFKSJ_7.5.0/com.ibm.mq.ref.adm.doc/q086940_.html
      request_parameters: []
      response_parameters:
        - name: ChannelName
          pcf_type: MQCFST
          type_hint: str
        - name: ChannelType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHT_MQTT
        - name: TrpType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQXPT_TCP
        - name: Port
          pcf_type: MQCFIN
          type_hint: int
        - name: ChannelType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHT_MQTT
        - name: Backlog
          pcf_type: MQCFIN
          type_hint: int
        - name: JAASConfig
          pcf_type: MQCFST
          type_hint: str
        - name: LocalAddress
          pcf_type: MQCFST
          type_hint: str
        - name: SSLCipherSuite
          pcf_type: MQCFST
          type_hint: str
        - name: SSLClientAuth
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSCA_REQUIRED
            - MQSCA_OPTIONAL
        - name: SSLKeyFile
          pcf_type: MQCFST
          type_hint: str
        - name: SSLPassPhrase
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
        - name: UseClientIdentifier
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQUCI_YES
            - MQUCI_NO
            - MQRCCF_BATCH_INT_ERROR
            - MQRCCF_BATCH_INT_WRONG_TYPE
            - MQRCCF_BATCH_SIZE_ERROR
            - MQRCCF_CHANNEL_NAME_ERROR
            - MQRCCF_CHANNEL_NOT_FOUND
            - MQRCCF_CHANNEL_TYPE_ERROR
            - MQRCCF_CLUSTER_NAME_CONFLICT
            - MQRCCF_DISC_INT_ERROR
            - MQRCCF_DISC_INT_WRONG_TYPE
            - MQRCCF_HB_INTERVAL_ERROR
            - MQRCCF_HB_INTERVAL_WRONG_TYPE
            - MQRCCF_LONG_RETRY_ERROR
            - MQRCCF_LONG_RETRY_WRONG_TYPE
            - MQRCCF_LONG_TIMER_ERROR
            - MQRCCF_LONG_TIMER_WRONG_TYPE
            - MQRCCF_MAX_INSTANCES_ERROR
            - MQRCCF_MAX_INSTS_PER_CLNT_ERR
            - MQRCCF_MAX_MSG_LENGTH_ERROR
            - MQRCCF_MCA_NAME_ERROR
            - MQRCCF_MCA_NAME_WRONG_TYPE
            - MQRCCF_MCA_TYPE_ERROR
            - MQRCCF_MISSING_CONN_NAME
            - MQRCCF_MR_COUNT_ERROR
            - MQRCCF_MR_COUNT_WRONG_TYPE
            - MQRCCF_MR_EXIT_NAME_ERROR
            - MQRCCF_MR_EXIT_NAME_WRONG_TYPE
            - MQRCCF_MR_INTERVAL_ERROR
            - MQRCCF_MR_INTERVAL_WRONG_TYPE
            - MQRCCF_MSG_EXIT_NAME_ERROR
            - MQRCCF_NET_PRIORITY_ERROR
            - MQRCCF_NET_PRIORITY_WRONG_TYPE
            - MQRCCF_NPM_SPEED_ERROR
            - MQRCCF_NPM_SPEED_WRONG_TYPE
            - MQRCCF_PARM_SEQUENCE_ERROR
            - MQRCCF_PUT_AUTH_ERROR
            - MQRCCF_PUT_AUTH_WRONG_TYPE
            - MQRCCF_RCV_EXIT_NAME_ERROR
            - MQRCCF_SEC_EXIT_NAME_ERROR
            - MQRCCF_SEND_EXIT_NAME_ERROR
            - MQRCCF_SEQ_NUMBER_WRAP_ERROR
            - MQRCCF_SHARING_CONVS_ERROR
            - MQRCCF_SHARING_CONVS_TYPE
            - MQRCCF_SHORT_RETRY_ERROR
            - MQRCCF_SHORT_RETRY_WRONG_TYPE
            - MQRCCF_SHORT_TIMER_ERROR
            - MQRCCF_SHORT_TIMER_WRONG_TYPE
            - MQRCCF_SSL_CIPHER_SPEC_ERROR
            - MQRCCF_SSL_CLIENT_AUTH_ERROR
            - MQRCCF_SSL_PEER_NAME_ERROR
            - MQRCCF_WRONG_CHANNEL_TYPE
            - MQRCCF_XMIT_PROTOCOL_TYPE_ERR
            - MQRCCF_XMIT_Q_NAME_ERROR
            - MQRCCF_XMIT_Q_NAME_WRONG_TYPE
    mapping:
      request:
        suggested:
          {}
        ambiguous:
          {}
        unmapped:
          - AFFINITY
          - AMQPKA
          - BATCHHB
          - BATCHINT
          - BATCHLIM
          - BATCHSZ
          - CERTLABL
          - CHLTYPE
          - CLNTWGHT
          - CLUSNL
          - CLUSTER
          - CLWLPRTY
          - CLWLRANK
          - CLWLWGHT
          - CMDSCOPE
          - COMPHDR
          - COMPMSG
          - CONNAME
          - CONVERT
          - DEFCDISP
          - DEFRECON
          - DESCR
          - DISCINT
          - HBINT
          - KAINT
          - LIKE
          - LOCLADDR
          - LONGRTY
          - LONGTMR
          - MAXINST
          - MAXINSTC
          - MAXMSGL
          - MCANAME
          - MCATYPE
          - MCAUSER
          - MODENAME
          - MONCHL
          - MRDATA
          - MREXIT
          - MRRTY
          - MRTMR
          - MSGDATA
          - MSGEXIT
          - NETPRTY
          - NPMSPEED
          - PASSWORD
          - PORT
          - PROPCTL
          - PUTAUT
          - QMNAME
          - QSGDISP
          - RCVDATA
          - RCVEXIT
          - SCYDATA
          - SCYEXIT
          - SENDDATA
          - SENDEXIT
          - SEQWRAP
          - SHARECNV
          - SHORTRTY
          - SHORTTMR
          - SPLPROT
          - SSLCAUTH
          - SSLCIPH
          - SSLPEER
          - STATCHL
          - TMPMODEL
          - TMPQPRFX
          - TPNAME
          - TPROOT
          - TRPTYPE
          - USECLTID
          - USEDLQ
          - USERID
          - XMITQ
        pcf_unmapped: []
      response:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - Backlog
          - ChannelName
          - ChannelType
          - ChannelType
          - JAASConfig
          - LocalAddress
          - Port
          - SSLCipherSuite
          - SSLClientAuth
          - SSLKeyFile
          - SSLPassPhrase
          - TransportType
          - TrpType
          - UseClientIdentifier
    notes: []
  - mqsc:
      name: DEFINE CHANNEL
      href: SSFKSJ_9.4.0/refadmin/q085520_.html
      positional_parameters:
        - (channel-name)
        - (string)
        - QmgrName
        - channel-name
        - clustername
        - integer
        - ip-addr
        - nlname
        - string
      input_parameters:
        - AFFINITY
        - AMQPKA
        - BATCHHB
        - BATCHINT
        - BATCHLIM
        - BATCHSZ
        - CERTLABL
        - CHLTYPE
        - CLNTWGHT
        - CLUSNL
        - CLUSTER
        - CLWLPRTY
        - CLWLRANK
        - CLWLWGHT
        - CMDSCOPE
        - COMPHDR
        - COMPMSG
        - CONNAME
        - CONVERT
        - DEFCDISP
        - DEFRECON
        - DESCR
        - DISCINT
        - HBINT
        - KAINT
        - LIKE
        - LOCLADDR
        - LONGRTY
        - LONGTMR
        - MAXINST
        - MAXINSTC
        - MAXMSGL
        - MCANAME
        - MCATYPE
        - MCAUSER
        - MODENAME
        - MONCHL
        - MRDATA
        - MREXIT
        - MRRTY
        - MRTMR
        - MSGDATA
        - MSGEXIT
        - NETPRTY
        - NOREPLACE
        - NPMSPEED
        - PASSWORD
        - PORT
        - PROPCTL
        - PUTAUT
        - QMNAME
        - QSGDISP
        - RCVDATA
        - RCVEXIT
        - REPLACE
        - SCYDATA
        - SCYEXIT
        - SENDDATA
        - SENDEXIT
        - SEQWRAP
        - SHARECNV
        - SHORTRTY
        - SHORTTMR
        - SPLPROT
        - SSLCAUTH
        - SSLCIPH
        - SSLPEER
        - STATCHL
        - TMPMODEL
        - TMPQPRFX
        - TPNAME
        - TPROOT
        - TRPTYPE
        - USECLTID
        - USEDLQ
        - USERID
        - XMITQ
      output_parameters: []
      section_sources:
        'Parameter descriptions for DEFINE CHANNEL':
          - AFFINITY
          - AMQPKA
          - BATCHHB
          - BATCHINT
          - BATCHLIM
          - BATCHSZ
          - CERTLABL
          - CHLTYPE
          - CLNTWGHT
          - CLUSNL
          - CLUSTER
          - CLWLPRTY
          - CLWLRANK
          - CLWLWGHT
          - CMDSCOPE
          - COMPHDR
          - COMPMSG
          - CONNAME
          - CONVERT
          - DEFCDISP
          - DEFRECON
          - DESCR
          - DISCINT
          - HBINT
          - KAINT
          - LIKE
          - LOCLADDR
          - LONGRTY
          - LONGTMR
          - MAXINST
          - MAXINSTC
          - MAXMSGL
          - MCANAME
          - MCATYPE
          - MCAUSER
          - MODENAME
          - MONCHL
          - MRDATA
          - MREXIT
          - MRRTY
          - MRTMR
          - MSGDATA
          - MSGEXIT
          - NETPRTY
          - NOREPLACE
          - NPMSPEED
          - PASSWORD
          - PORT
          - PROPCTL
          - PUTAUT
          - QMNAME
          - QSGDISP
          - RCVDATA
          - RCVEXIT
          - REPLACE
          - SCYDATA
          - SCYEXIT
          - SENDDATA
          - SENDEXIT
          - SEQWRAP
          - SHARECNV
          - SHORTRTY
          - SHORTTMR
          - SPLPROT
          - SSLCAUTH
          - SSLCIPH
          - SSLPEER
          - STATCHL
          - TMPMODEL
          - TMPQPRFX
          - TPNAME
          - TPROOT
          - TRPTYPE
          - USECLTID
          - USEDLQ
          - USERID
          - XMITQ
    pcf:
      command: MQCMD_CREATE_CHANNEL
      request_href: SSFKSJ_9.4.0/refdev/q091020_.html
      response_href: SSFKSJ_7.5.0/com.ibm.mq.ref.adm.doc/q086940_.html
      request_parameters: []
      response_parameters:
        - name: ChannelName
          pcf_type: MQCFST
          type_hint: str
        - name: ChannelType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHT_MQTT
        - name: TrpType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQXPT_TCP
        - name: Port
          pcf_type: MQCFIN
          type_hint: int
        - name: ChannelType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHT_MQTT
        - name: Backlog
          pcf_type: MQCFIN
          type_hint: int
        - name: JAASConfig
          pcf_type: MQCFST
          type_hint: str
        - name: LocalAddress
          pcf_type: MQCFST
          type_hint: str
        - name: SSLCipherSuite
          pcf_type: MQCFST
          type_hint: str
        - name: SSLClientAuth
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSCA_REQUIRED
            - MQSCA_OPTIONAL
        - name: SSLKeyFile
          pcf_type: MQCFST
          type_hint: str
        - name: SSLPassPhrase
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
        - name: UseClientIdentifier
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQUCI_YES
            - MQUCI_NO
            - MQRCCF_BATCH_INT_ERROR
            - MQRCCF_BATCH_INT_WRONG_TYPE
            - MQRCCF_BATCH_SIZE_ERROR
            - MQRCCF_CHANNEL_NAME_ERROR
            - MQRCCF_CHANNEL_NOT_FOUND
            - MQRCCF_CHANNEL_TYPE_ERROR
            - MQRCCF_CLUSTER_NAME_CONFLICT
            - MQRCCF_DISC_INT_ERROR
            - MQRCCF_DISC_INT_WRONG_TYPE
            - MQRCCF_HB_INTERVAL_ERROR
            - MQRCCF_HB_INTERVAL_WRONG_TYPE
            - MQRCCF_LONG_RETRY_ERROR
            - MQRCCF_LONG_RETRY_WRONG_TYPE
            - MQRCCF_LONG_TIMER_ERROR
            - MQRCCF_LONG_TIMER_WRONG_TYPE
            - MQRCCF_MAX_INSTANCES_ERROR
            - MQRCCF_MAX_INSTS_PER_CLNT_ERR
            - MQRCCF_MAX_MSG_LENGTH_ERROR
            - MQRCCF_MCA_NAME_ERROR
            - MQRCCF_MCA_NAME_WRONG_TYPE
            - MQRCCF_MCA_TYPE_ERROR
            - MQRCCF_MISSING_CONN_NAME
            - MQRCCF_MR_COUNT_ERROR
            - MQRCCF_MR_COUNT_WRONG_TYPE
            - MQRCCF_MR_EXIT_NAME_ERROR
            - MQRCCF_MR_EXIT_NAME_WRONG_TYPE
            - MQRCCF_MR_INTERVAL_ERROR
            - MQRCCF_MR_INTERVAL_WRONG_TYPE
            - MQRCCF_MSG_EXIT_NAME_ERROR
            - MQRCCF_NET_PRIORITY_ERROR
            - MQRCCF_NET_PRIORITY_WRONG_TYPE
            - MQRCCF_NPM_SPEED_ERROR
            - MQRCCF_NPM_SPEED_WRONG_TYPE
            - MQRCCF_PARM_SEQUENCE_ERROR
            - MQRCCF_PUT_AUTH_ERROR
            - MQRCCF_PUT_AUTH_WRONG_TYPE
            - MQRCCF_RCV_EXIT_NAME_ERROR
            - MQRCCF_SEC_EXIT_NAME_ERROR
            - MQRCCF_SEND_EXIT_NAME_ERROR
            - MQRCCF_SEQ_NUMBER_WRAP_ERROR
            - MQRCCF_SHARING_CONVS_ERROR
            - MQRCCF_SHARING_CONVS_TYPE
            - MQRCCF_SHORT_RETRY_ERROR
            - MQRCCF_SHORT_RETRY_WRONG_TYPE
            - MQRCCF_SHORT_TIMER_ERROR
            - MQRCCF_SHORT_TIMER_WRONG_TYPE
            - MQRCCF_SSL_CIPHER_SPEC_ERROR
            - MQRCCF_SSL_CLIENT_AUTH_ERROR
            - MQRCCF_SSL_PEER_NAME_ERROR
            - MQRCCF_WRONG_CHANNEL_TYPE
            - MQRCCF_XMIT_PROTOCOL_TYPE_ERR
            - MQRCCF_XMIT_Q_NAME_ERROR
            - MQRCCF_XMIT_Q_NAME_WRONG_TYPE
    mapping:
      request:
        suggested:
          {}
        ambiguous:
          {}
        unmapped:
          - AFFINITY
          - AMQPKA
          - BATCHHB
          - BATCHINT
          - BATCHLIM
          - BATCHSZ
          - CERTLABL
          - CHLTYPE
          - CLNTWGHT
          - CLUSNL
          - CLUSTER
          - CLWLPRTY
          - CLWLRANK
          - CLWLWGHT
          - CMDSCOPE
          - COMPHDR
          - COMPMSG
          - CONNAME
          - CONVERT
          - DEFCDISP
          - DEFRECON
          - DESCR
          - DISCINT
          - HBINT
          - KAINT
          - LIKE
          - LOCLADDR
          - LONGRTY
          - LONGTMR
          - MAXINST
          - MAXINSTC
          - MAXMSGL
          - MCANAME
          - MCATYPE
          - MCAUSER
          - MODENAME
          - MONCHL
          - MRDATA
          - MREXIT
          - MRRTY
          - MRTMR
          - MSGDATA
          - MSGEXIT
          - NETPRTY
          - NOREPLACE
          - NPMSPEED
          - PASSWORD
          - PORT
          - PROPCTL
          - PUTAUT
          - QMNAME
          - QSGDISP
          - RCVDATA
          - RCVEXIT
          - REPLACE
          - SCYDATA
          - SCYEXIT
          - SENDDATA
          - SENDEXIT
          - SEQWRAP
          - SHARECNV
          - SHORTRTY
          - SHORTTMR
          - SPLPROT
          - SSLCAUTH
          - SSLCIPH
          - SSLPEER
          - STATCHL
          - TMPMODEL
          - TMPQPRFX
          - TPNAME
          - TPROOT
          - TRPTYPE
          - USECLTID
          - USEDLQ
          - USERID
          - XMITQ
        pcf_unmapped: []
      response:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - Backlog
          - ChannelName
          - ChannelType
          - ChannelType
          - JAASConfig
          - LocalAddress
          - Port
          - SSLCipherSuite
          - SSLClientAuth
          - SSLKeyFile
          - SSLPassPhrase
          - TransportType
          - TrpType
          - UseClientIdentifier
    notes: []
  - mqsc:
      name: DELETE CHANNEL
      href: SSFKSJ_9.4.0/refadmin/q085820_.html
      positional_parameters:
        - channel-name
        - qmgr-name
      input_parameters:
        - CHLTABLE
        - CMDSCOPE
        - IGNSTATE
        - QSGDISP
      output_parameters: []
      section_sources:
        'Parameter descriptions for DELETE CHANNEL':
          - CHLTABLE
          - CMDSCOPE
          - IGNSTATE
          - QSGDISP
    pcf:
      command: MQCMD_DELETE_CHANNEL
      request_href: SSFKSJ_9.4.0/refadmin/q087120_.html
      response_href: SSFKSJ_9.4.0/refadmin/q087130_.html
      request_parameters:
        - name: ChannelName
          pcf_type: MQCFST
          type_hint: str
        - name: ChannelType
          pcf_type: MQCFIN
          type_hint: int
        - name: ChannelTable
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHTAB_Q_MGR
            - MQCHTAB_CLNTCONN
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
        - name: IgnoreState
          pcf_type: MQCFST
          type_hint: str
          enum_values:
            - MQIS_YES
            - MQIS_NO
            - MQRCCF_CHANNEL_NOT_FOUND
            - MQRCCF_CHANNEL_TABLE_ERROR
      response_parameters:
        - name: ChannelName
          pcf_type: MQCFST
          type_hint: str
        - name: ChannelType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQRCCF_CHANNEL_NOT_FOUND
    mapping:
      request:
        suggested:
          {}
        ambiguous:
          IGNSTATE:
            - IgnoreState
        unmapped:
          - CHLTABLE
          - CMDSCOPE
          - QSGDISP
        pcf_unmapped:
          - ChannelName
          - ChannelTable
          - ChannelType
          - CommandScope
          - IgnoreState
          - QSGDisposition
      response:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - ChannelName
          - ChannelType
    notes: []
  - mqsc:
      name: DISPLAY CHANNEL
      href: SSFKSJ_9.4.0/refadmin/q086040_.html
      positional_parameters:
        - (generic-channel-name)
        - integer
        - qmgr-name
      input_parameters: []
      output_parameters:
        - AFFINITY
        - ALTDATE
        - ALTTIME
        - AMQPKA
        - AUTOSTART
        - BATCHHB
        - BATCHINT
        - BATCHLIM
        - BATCHSZ
        - CERTLABL
        - CHLTYPE
        - CLNTWGHT
        - CLUSNL
        - CLUSTER
        - CLWLPRTY
        - CLWLRANK
        - CLWLWGHT
        - COMPHDR
        - COMPMSG
        - CONNAME
        - CONVERT
        - DEFCDISP
        - DEFRECON
        - DESCR
        - DISCINT
        - HBINT
        - KAINT
        - LOCLADDR
        - LONGRTY
        - LONGTMR
        - MAXINST
        - MAXINSTC
        - MAXMSGL
        - MCANAME
        - MCATYPE
        - MCAUSER
        - MODENAME
        - MONCHL
        - MRDATA
        - MREXIT
        - MRRTY
        - MRTMR
        - MSGDATA
        - MSGEXIT
        - NETPRTY
        - NPMSPEED
        - PASSWORD
        - PORT
        - PROPCTL
        - PUTAUT
        - QMNAME
        - RCVDATA
        - RCVEXIT
        - RESETSEQ
        - SCYDATA
        - SCYEXIT
        - SENDDATA
        - SENDEXIT
        - SEQWRAP
        - SHARECNV
        - SHORTRTY
        - SHORTTMR
        - SPLPROT
        - SSLCAUTH
        - SSLCIPH
        - SSLPEER
        - STATCHL
        - TPNAME
        - TPROOT
        - TRPTYPE
        - TYPE
        - USECLTID
        - USEDLQ
        - USERID
        - XMITQ
      section_sources:
        {}
    pcf:
      command: MQCMD_INQUIRE_CHANNEL
      request_href: SSFKSJ_9.4.0/refadmin/q087410_.html
      response_href: SSFKSJ_9.4.0/refadmin/q087430_.html
      request_parameters:
        - name: ChannelName
          pcf_type: MQCFST
          type_hint: str
        - name: ChannelAttrs
          pcf_type: MQCFIL
          type_hint: int
          enum_values:
            - MQIACF_ALL
        - name: ChannelType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHT_SENDER
            - MQCHT_SERVER
            - MQCHT_RECEIVER
            - MQCHT_REQUESTER
            - MQCHT_SVRCONN
            - MQCHT_CLNTCONN
            - MQCHT_CLUSRCVR
            - MQCHT_CLUSSDR
            - MQCHT_AMQP
            - MQCHT_MQTT
            - MQCHT_ALL
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
          enum_values:
            - MQRCCF_CHANNEL_NAME_ERROR
            - MQRCCF_CHANNEL_NOT_FOUND
            - MQRCCF_CHANNEL_TYPE_ERROR
      response_parameters:
        - name: AlterationDate
          pcf_type: MQCFST
          type_hint: str
        - name: AlterationTime
          pcf_type: MQCFST
          type_hint: str
        - name: BatchDataLimit
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchHeartbeat
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchSize
          pcf_type: MQCFIN
          type_hint: int
        - name: Certificatelabel
          pcf_type: MQCFST
          type_hint: str
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
        - name: ChannelStatistics
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_OFF
            - MQMON_Q_MGR
            - MQMON_LOW
            - MQMON_MEDIUM
            - MQMON_HIGH
        - name: ChannelType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHT_SENDER
            - MQCHT_SERVER
            - MQCHT_RECEIVER
            - MQCHT_REQUESTER
            - MQCHT_SVRCONN
            - MQCHT_CLNTCONN
            - MQCHT_CLUSRCVR
            - MQCHT_CLUSSDR
            - MQCHT_MQTT
        - name: ClientChannelWeight
          pcf_type: MQCFIN
          type_hint: int
        - name: ClientIdentifier
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterName
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterNamelist
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
        - name: ConnectionAffinity
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCAFTY_PREFERRED
            - MQCAFTY_NONE
        - name: ConnectionName
          pcf_type: MQCFST
          type_hint: str
        - name: DataConversion
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCDC_NO_SENDER_CONVERSION
            - MQCDC_SENDER_CONVERSION
        - name: DefaultChannelDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHLD_PRIVATE
            - MQCHLD_FIXSHARED
            - MQCHLD_SHARED
        - name: DiscInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: DefReconnect
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQRCN_NO
            - MQRCN_YES
            - MQRCN_Q_MGR
            - MQRCN_DISABLED
        - name: HeaderCompression
          pcf_type: MQCFIL
          type_hint: int
          enum_values:
            - MQCOMPRESS_NONE
            - MQCOMPRESS_SYSTEM
        - name: HeartbeatInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: InDoubtInbound
          pcf_type: MQCFIN
          type_hint: int
        - name: InDoubtOutbound
          pcf_type: MQCFIN
          type_hint: int
        - name: KeepAliveInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: LastMsgTime
          pcf_type: MQCFST
          type_hint: str
        - name: LocalAddress
          pcf_type: MQCFST
          type_hint: str
        - name: LongRetryCount
          pcf_type: MQCFIN
          type_hint: int
        - name: LongRetryInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxInstances
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxInstancesPerClient
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
            - MQCOMPRESS_ANY
        - name: ModeName
          pcf_type: MQCFST
          type_hint: str
        - name: MsgExit
          pcf_type: MQCFST
          type_hint: str
        - name: MsgsReceived
          pcf_type: MQCFIN64
          type_hint: int
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
        - name: MsgsSent
          pcf_type: MQCFIN64
          type_hint: int
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
        - name: PropertyControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPROP_COMPATIBILITY
            - MQPROP_NONE
            - MQPROP_ALL
        - name: PutAuthority
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPA_DEFAULT
            - MQPA_CONTEXT
        - name: QMgrName
          pcf_type: MQCFST
          type_hint: str
        - name: QSGDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSGD_COPY
            - MQQSGD_GROUP
            - MQQSGD_Q_MGR
        - name: ReceiveExit
          pcf_type: MQCFST
          type_hint: str
        - name: ReceiveUserData
          pcf_type: MQCFST
          type_hint: str
        - name: ResetSeq
          pcf_type: MQCFIN
          type_hint: int
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
        - name: SharingConversations
          pcf_type: MQCFIN
          type_hint: int
        - name: ShortRetryCount
          pcf_type: MQCFIN
          type_hint: int
        - name: ShortRetryInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: SPLProtection
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSPL_PASSTHRU
            - MQSPL_REMOVE
            - MQSPL_AS_POLICY
        - name: SSLCipherSpec
          pcf_type: MQCFST
          type_hint: str
        - name: SSLCipherSuite
          pcf_type: MQCFST
          type_hint: str
        - name: SSLClientAuth
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSCA_REQUIRED
            - MQSCA_OPTIONAL
            - MQSCA_NEVER_REQUIRED
        - name: SSLPeerName
          pcf_type: MQCFST
          type_hint: str
        - name: TpName
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
          enum_values:
            - MQUSEDLQ_NO
            - MQUSEDLQ_YES
        - name: UserIdentifier
          pcf_type: MQCFST
          type_hint: str
        - name: XmitQName
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
          - ChannelAttrs
          - ChannelName
          - ChannelType
          - CommandScope
          - IntegerFilterCommand
          - QSGDisposition
          - StringFilterCommand
      response:
        suggested:
          BATCHHB: BatchHeartbeat
          BATCHINT: BatchInterval
          BATCHSZ: BatchSize
          DISCINT: DiscInterval
          MCANAME: MCAName
          MCATYPE: MCAType
          MODENAME: ModeName
          MSGEXIT: MsgExit
          PASSWORD: Password
          RESETSEQ: ResetSeq
          SENDEXIT: SendExit
          TPNAME: TpName
          USEDLQ: UseDLQ
        ambiguous:
          BATCHLIM:
            - BatchDataLimit
          MREXIT:
            - MsgExit
          QMNAME:
            - QMgrName
        unmapped:
          - AFFINITY
          - ALTDATE
          - ALTTIME
          - AMQPKA
          - AUTOSTART
          - CERTLABL
          - CHLTYPE
          - CLNTWGHT
          - CLUSNL
          - CLUSTER
          - CLWLPRTY
          - CLWLRANK
          - CLWLWGHT
          - COMPHDR
          - COMPMSG
          - CONNAME
          - CONVERT
          - DEFCDISP
          - DEFRECON
          - DESCR
          - HBINT
          - KAINT
          - LOCLADDR
          - LONGRTY
          - LONGTMR
          - MAXINST
          - MAXINSTC
          - MAXMSGL
          - MCAUSER
          - MONCHL
          - MRDATA
          - MRRTY
          - MRTMR
          - MSGDATA
          - NETPRTY
          - NPMSPEED
          - PORT
          - PROPCTL
          - PUTAUT
          - RCVDATA
          - RCVEXIT
          - SCYDATA
          - SCYEXIT
          - SENDDATA
          - SEQWRAP
          - SHARECNV
          - SHORTRTY
          - SHORTTMR
          - SPLPROT
          - SSLCAUTH
          - SSLCIPH
          - SSLPEER
          - STATCHL
          - TPROOT
          - TRPTYPE
          - USECLTID
          - USERID
          - XMITQ
        pcf_unmapped:
          - AlterationDate
          - AlterationTime
          - BatchDataLimit
          - CLWLChannelPriority
          - CLWLChannelRank
          - CLWLChannelWeight
          - Certificatelabel
          - ChannelDesc
          - ChannelMonitoring
          - ChannelName
          - ChannelStatistics
          - ChannelType
          - ClientChannelWeight
          - ClientIdentifier
          - ClusterName
          - ClusterNamelist
          - ConnectionAffinity
          - ConnectionName
          - DataConversion
          - DefReconnect
          - DefaultChannelDisposition
          - HeaderCompression
          - HeartbeatInterval
          - InDoubtInbound
          - InDoubtOutbound
          - KeepAliveInterval
          - LastMsgTime
          - LocalAddress
          - LongRetryCount
          - LongRetryInterval
          - MCAUserIdentifier
          - MaxInstances
          - MaxInstancesPerClient
          - MaxMsgLength
          - MessageCompression
          - MsgRetryCount
          - MsgRetryExit
          - MsgRetryInterval
          - MsgRetryUserData
          - MsgUserData
          - MsgsReceived
          - MsgsSent
          - NetworkPriority
          - NonPersistentMsgSpeed
          - PropertyControl
          - PutAuthority
          - QMgrName
          - QSGDisposition
          - ReceiveExit
          - ReceiveUserData
          - SPLProtection
          - SSLCipherSpec
          - SSLCipherSuite
          - SSLClientAuth
          - SSLPeerName
          - SecurityExit
          - SecurityUserData
          - SendUserData
          - SeqNumberWrap
          - SharingConversations
          - ShortRetryCount
          - ShortRetryInterval
          - TransportType
          - UserIdentifier
          - XmitQName
    notes:
      - display-requested-parameters-table
  - mqsc:
      name: DISPLAY CHSTATUS
      href: SSFKSJ_9.4.0/refadmin/q086090_.html
      positional_parameters:
        - connection-name
        - filter-keyword
        - filter-value
        - generic-channel-name
        - operator
        - q-name
      input_parameters: []
      output_parameters:
        - AMQPKA
        - BATCHES
        - BATCHSZ
        - BUFSRCVD
        - BUFSSENT
        - BYTSRCVD
        - BYTSSENT
        - CHLTYPE
        - CHSTADA
        - CHSTATI
        - COMPHDR
        - COMPMSG
        - COMPRATE
        - COMPTIME
        - CURLUWID
        - CURMSGS
        - CURSEQNO
        - CURSHCNV
        - EXITTIME
        - HBINT
        - INDOUBT
        - JOBNAME
        - KAINT
        - LOCLADDR
        - LONGRTS
        - LSTLUWID
        - LSTMSGDA
        - LSTMSGTI
        - LSTSEQNO
        - MAXMSGL
        - MAXSHCNV
        - MCASTAT
        - MCAUSER
        - MONCHL
        - MONITOR
        - MSGS
        - NETTIME
        - NPMSPEED
        - PORT
        - QMNAME
        - RAPPLTAG
        - RPRODUCT
        - RQMNAME
        - RVERSION
        - SECPROT
        - SHARECNV
        - SHORTRTS
        - SSLCERTI
        - SSLCERTU
        - SSLCIPH
        - SSLKEYDA
        - SSLKEYTI
        - SSLPEER
        - SSLRKEYS
        - STATCHL
        - STATUS
        - STOPREQ
        - SUBSTATE
        - TPROOT
        - USECLTID
        - XBATCHSZ
        - XQMSGSA
        - XQTIME
      section_sources:
        {}
    pcf:
      command: MQCMD_INQUIRE_CHANNEL_STATUS
      request_href: SSFKSJ_9.4.0/refadmin/q087540_.html
      response_href: SSFKSJ_9.4.0/refadmin/q087560_.html
      request_parameters:
        - name: ChannelName
          pcf_type: MQCFST
          type_hint: str
        - name: ChannelDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHLD_ALL
            - MQCHLD_PRIVATE
            - MQCHLD_SHARED
        - name: ChannelInstanceAttrs
          pcf_type: MQCFIL
          type_hint: int
          enum_values:
            - MQIACF_ALL
            - MQCACH_CHANNEL_NAME
            - MQCACH_CONNECTION_NAME
            - MQCACH_CURRENT_LUWID
            - MQCACH_LAST_LUWID
            - MQCACH_XMIT_Q_NAME
            - MQIACH_CHANNEL_INSTANCE_TYPE
            - MQIACH_CHANNEL_TYPE
            - MQIACH_CURRENT_MSGS
            - MQIACH_CURRENT_SEQ_NUMBER
            - MQIACH_INDOUBT_STATUS
            - MQIACH_LAST_SEQ_NUMBER
            - MQCA_Q_MGR_NAME
            - MQCA_REMOTE_Q_MGR_NAME
            - MQCACH_CHANNEL_START_DATE
            - MQCACH_CHANNEL_START_TIME
            - MQCACH_LAST_MSG_DATE
            - MQCACH_LAST_MSG_TIME
            - MQCACH_LOCAL_ADDRESS
            - MQCACH_MCA_JOB_NAME
            - MQCACH_MCA_USER_ID
            - MQCACH_REMOTE_APPL_TAG
            - MQCACH_REMOTE_PRODUCT
            - MQCACH_REMOTE_VERSION
            - MQCACH_SSL_CIPHER_SPEC
            - MQCACH_SSL_SHORT_PEER_NAME
            - MQCACH_SSL_CERT_ISSUER_NAME
            - MQCACH_SSL_CERT_USER_ID
            - MQCACH_TOPIC_ROOT
            - MQIA_MONITORING_CHANNEL
            - MQIA_STATISTICS_CHANNEL
            - MQIACF_MONITORING
            - MQIACH_BATCH_SIZE_INDICATOR
            - MQIACH_COMPRESSION_RATE
            - MQIACH_COMPRESSION_TIME
            - MQIACH_EXIT_TIME_INDICATOR
            - MQIACH_NETWORK_TIME_INDICATOR
            - MQIACH_XMITQ_MSGS_AVAILABLE
            - MQIACH_XMITQ_TIME_INDICATOR
            - MQIACH_BATCHES
            - MQIACH_BUFFERS_RCVD
            - MQIACH_BUFFERS_SENT
            - MQIACH_BYTES_RCVD
            - MQIACH_BYTES_SENT
            - MQIACH_CHANNEL_SUBSTATE
            - MQIACH_CURRENT_SHARING_CONVS
            - MQIACH_HDR_COMPRESSION
            - MQIACH_KEEP_ALIVE_INTERVAL
            - MQIACH_LONG_RETRIES_LEFT
            - MQIACH_MAX_MSG_LENGTH
            - MQIACH_MAX_SHARING_CONVS
            - MQIACH_MCA_STATUS
            - MQIACH_MSG_COMPRESSION
            - MQIACH_MSGS
            - MQIACH_SECURITY_PROTOCOL
            - MQIACH_SHORT_RETRIES_LEFT
            - MQIACH_SSL_KEY_RESETS
            - MQIACH_SSL_RESET_DATE
            - MQIACH_SSL_RESET_TIME
            - MQIACH_STOP_REQUESTED
            - MQIACH_BATCH_SIZE
            - MQIACH_HB_INTERVAL
            - MQIACH_NPM_SPEED
            - MQCACH_Q_MGR_NAME
        - name: ChannelInstanceType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQOT_CURRENT_CHANNEL
            - MQOT_SAVED_CHANNEL
            - MQOT_SHORT_CHANNEL
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: ConnectionName
          pcf_type: MQCFST
          type_hint: str
        - name: IntegerFilterCommand
          pcf_type: MQCFIF
          type_hint: null
        - name: StringFilterCommand
          pcf_type: MQCFSF
          type_hint: null
        - name: XmitQName
          pcf_type: MQCFST
          type_hint: str
          enum_values:
            - MQRCCF_CHANNEL_NAME_ERROR
            - MQRCCF_CHANNEL_NOT_FOUND
            - MQRCCF_CHL_INST_TYPE_ERROR
            - MQRCCF_CHL_STATUS_NOT_FOUND
            - MQRCCF_NONE_FOUND
            - MQRCCF_XMIT_Q_NAME_ERROR
      response_parameters:
        - name: Batches
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchSize
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchSizeIndicator
          pcf_type: MQCFIL
          type_hint: int
        - name: BuffersReceived
          pcf_type: MQCFIN
          type_hint: int
        - name: BuffersSent
          pcf_type: MQCFIN
          type_hint: int
        - name: BytesReceived
          pcf_type: MQCFIN
          type_hint: int
        - name: BytesSent
          pcf_type: MQCFIN
          type_hint: int
        - name: ChannelDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHLD_PRIVATE
            - MQCHLD_SHARED
            - MQCHLD_FIXSHARED
        - name: ChannelInstanceType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQOT_CURRENT_CHANNEL
            - MQOT_SAVED_CHANNEL
            - MQOT_SHORT_CHANNEL
        - name: ChannelMonitoring
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_OFF
            - MQMON_LOW
            - MQMON_MEDIUM
            - MQMON_HIGH
        - name: ChannelName
          pcf_type: MQCFST
          type_hint: str
        - name: ChannelStartDate
          pcf_type: MQCFST
          type_hint: str
        - name: ChannelStartTime
          pcf_type: MQCFST
          type_hint: str
        - name: ChannelStatistics
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_OFF
            - MQMON_LOW
            - MQMON_MEDIUM
            - MQMON_HIGH
        - name: ChannelStatus
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHS_BINDING
            - MQCHS_STARTING
            - MQCHS_RUNNING
            - MQCHS_PAUSED
            - MQCHS_STOPPING
            - MQCHS_RETRYING
            - MQCHS_STOPPED
            - MQCHS_REQUESTING
            - MQCHS_SWITCHING
            - MQCHS_INITIALIZING
        - name: ChannelType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHT_SENDER
            - MQCHT_SERVER
            - MQCHT_RECEIVER
            - MQCHT_REQUESTER
            - MQCHT_SVRCONN
            - MQCHT_CLNTCONN
            - MQCHT_CLUSRCVR
            - MQCHT_CLUSSDR
        - name: CompressionRate
          pcf_type: MQCFIL
          type_hint: int
        - name: CompressionTime
          pcf_type: MQCFIL
          type_hint: int
        - name: ConnectionName
          pcf_type: MQCFST
          type_hint: str
        - name: CurrentLUWID
          pcf_type: MQCFST
          type_hint: str
        - name: CurrentMsgs
          pcf_type: MQCFIN
          type_hint: int
        - name: CurrentSequenceNumber
          pcf_type: MQCFIN
          type_hint: int
        - name: CurrentSharingConversations
          pcf_type: MQCFIN
          type_hint: int
        - name: ExitTime
          pcf_type: MQCFIL
          type_hint: int
        - name: HeaderCompression
          pcf_type: MQCFIL
          type_hint: int
          enum_values:
            - MQCOMPRESS_NONE
            - MQCOMPRESS_SYSTEM
            - MQCOMPRESS_NOT_AVAILABLE
        - name: HeartbeatInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: InDoubtStatus
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHIDS_NOT_INDOUBT
            - MQCHIDS_INDOUBT
        - name: KeepAliveInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: LastLUWID
          pcf_type: MQCFST
          type_hint: str
        - name: LastMsgDate
          pcf_type: MQCFST
          type_hint: str
        - name: LastMsgTime
          pcf_type: MQCFST
          type_hint: str
        - name: LastSequenceNumber
          pcf_type: MQCFIN
          type_hint: int
        - name: LocalAddress
          pcf_type: MQCFST
          type_hint: str
        - name: LongRetriesLeft
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxMsgLength
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxSharingConversations
          pcf_type: MQCFIN
          type_hint: int
        - name: MCAJobName
          pcf_type: MQCFST
          type_hint: str
        - name: MCAStatus
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMCAS_STOPPED
            - MQMCAS_RUNNING
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
            - MQCOMPRESS_NOT_AVAILABLE
        - name: Msgs
          pcf_type: MQCFIN
          type_hint: int
        - name: MsgsAvailable
          pcf_type: MQCFIN
          type_hint: int
        - name: NetTime
          pcf_type: MQCFIL
          type_hint: int
        - name: NonPersistentMsgSpeed
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQNPMS_NORMAL
            - MQNPMS_FAST
        - name: QMgrName
          pcf_type: MQCFST
          type_hint: str
        - name: RemoteApplTag
          pcf_type: MQCFST
          type_hint: str
        - name: RemoteProduct
          pcf_type: MQCFST
          type_hint: str
        - name: RemoteVersion
          pcf_type: MQCFST
          type_hint: str
          enum_values:
            - VV
            - RR
            - MM
            - FF
        - name: RemoteQMgrName
          pcf_type: MQCFST
          type_hint: str
        - name: ShortRetriesLeft
          pcf_type: MQCFIN
          type_hint: int
        - name: SecurityProtocol
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSECPROT_NONE
            - MQSECPROT_SSLV30
            - MQSECPROT_TLSV10
            - MQSECPROT_TLSV12
            - MQSECPROT_TLSV13
        - name: SSLCertRemoteIssuerName
          pcf_type: MQCFST
          type_hint: str
        - name: SSLCertUserId
          pcf_type: MQCFST
          type_hint: str
        - name: SSLCipherSpecification
          pcf_type: MQCFST
          type_hint: str
        - name: SSLKeyResetDate
          pcf_type: MQCFST
          type_hint: str
        - name: SSLKeyResets
          pcf_type: MQCFIN
          type_hint: int
        - name: SSLKeyResetTime
          pcf_type: MQCFST
          type_hint: str
        - name: SSLShortPeerName
          pcf_type: MQCFST
          type_hint: str
        - name: StopRequested
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHSR_STOP_NOT_REQUESTED
            - MQCHSR_STOP_REQUESTED
        - name: SubState
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHSSTATE_CHADEXIT
            - MQCHSSTATE_COMPRESSING
            - MQCHSSTATE_END_OF_BATCH
            - MQCHSSTATE_HANDSHAKING
            - MQCHSSTATE_HEARTBEATING
            - MQCHSSTATE_IN_MQGET
            - MQCHSSTATE_IN_MQI_CALL
            - MQCHSSTATE_IN_MQPUT
            - MQCHSSTATE_MREXIT
            - MQCHSSTATE_MSGEXIT
            - MQCHSSTATE_NAME_SERVER
            - MQCHSSTATE_NET_CONNECTING
            - MQCHSSTATE_OTHER
            - MQCHSSTATE_RCVEXIT
            - MQCHSSTATE_RECEIVING
            - MQCHSSTATE_RESYNCHING
            - MQCHSSTATE_SCYEXIT
            - MQCHSSTATE_SENDEXIT
            - MQCHSSTATE_SENDING
            - MQCHSSTATE_SERIALIZING
        - name: XmitQName
          pcf_type: MQCFST
          type_hint: str
        - name: XQTime
          pcf_type: MQCFIL
          type_hint: int
    mapping:
      request:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - ChannelDisposition
          - ChannelInstanceAttrs
          - ChannelInstanceType
          - ChannelName
          - CommandScope
          - ConnectionName
          - IntegerFilterCommand
          - StringFilterCommand
          - XmitQName
      response:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - BatchSize
          - BatchSizeIndicator
          - Batches
          - BuffersReceived
          - BuffersSent
          - BytesReceived
          - BytesSent
          - ChannelDisposition
          - ChannelInstanceType
          - ChannelMonitoring
          - ChannelName
          - ChannelStartDate
          - ChannelStartTime
          - ChannelStatistics
          - ChannelStatus
          - ChannelType
          - CompressionRate
          - CompressionTime
          - ConnectionName
          - CurrentLUWID
          - CurrentMsgs
          - CurrentSequenceNumber
          - CurrentSharingConversations
          - ExitTime
          - HeaderCompression
          - HeartbeatInterval
          - InDoubtStatus
          - KeepAliveInterval
          - LastLUWID
          - LastMsgDate
          - LastMsgTime
          - LastSequenceNumber
          - LocalAddress
          - LongRetriesLeft
          - MCAJobName
          - MCAStatus
          - MCAUserIdentifier
          - MaxMsgLength
          - MaxSharingConversations
          - MessageCompression
          - Msgs
          - MsgsAvailable
          - NetTime
          - NonPersistentMsgSpeed
          - QMgrName
          - RemoteApplTag
          - RemoteProduct
          - RemoteQMgrName
          - RemoteVersion
          - SSLCertRemoteIssuerName
          - SSLCertUserId
          - SSLCipherSpecification
          - SSLKeyResetDate
          - SSLKeyResetTime
          - SSLKeyResets
          - SSLShortPeerName
          - SecurityProtocol
          - ShortRetriesLeft
          - StopRequested
          - SubState
          - XQTime
          - XmitQName
    notes: []
  - mqsc:
      name: PING CHANNEL
      href: SSFKSJ_9.4.0/refadmin/q086430_.html
      positional_parameters:
        - (channel-name)
        - integer
        - qmgr-name
      input_parameters: []
      output_parameters: []
      section_sources:
        {}
    pcf:
      command: MQCMD_PING_CHANNEL
      request_href: SSFKSJ_9.4.0/refadmin/q088190_.html
      response_href: SSFKSJ_9.4.0/refadmin/q088190_.html
      request_parameters:
        - name: ChannelName
          pcf_type: MQCFST
          type_hint: str
        - name: DataCount
          pcf_type: MQCFIN
          type_hint: int
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: ChannelDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHLD_PRIVATE
            - MQCHLD_SHARED
            - MQCHLD_FIXSHARED
            - MQRCCF_ALLOCATE_FAILED
            - MQRCCF_BIND_FAILED
            - MQRCCF_CCSID_ERROR
            - MQRCCF_CHANNEL_CLOSED
            - MQRCCF_CHANNEL_IN_USE
            - MQRCCF_CHANNEL_NOT_FOUND
            - MQRCCF_CHANNEL_TYPE_ERROR
            - MQRCCF_CONFIGURATION_ERROR
            - MQRCCF_CONNECTION_CLOSED
            - MQRCCF_CONNECTION_REFUSED
            - MQRCCF_DATA_TOO_LARGE
            - MQRCCF_ENTRY_ERROR
            - MQRCCF_HOST_NOT_AVAILABLE
            - MQRCCF_NO_COMMS_MANAGER
            - MQRCCF_PING_DATA_COMPARE_ERROR
            - MQRCCF_PING_DATA_COUNT_ERROR
            - MQRCCF_PING_ERROR
            - MQRCCF_RECEIVE_FAILED
            - MQRCCF_RECEIVED_DATA_ERROR
            - MQRCCF_REMOTE_QM_TERMINATING
            - MQRCCF_REMOTE_QM_UNAVAILABLE
            - MQRCCF_SEND_FAILED
            - MQRCCF_STRUCTURE_TYPE_ERROR
            - MQRCCF_TERMINATED_BY_SEC_EXIT
            - MQRCCF_UNKNOWN_REMOTE_CHANNEL
            - MQRCCF_USER_EXIT_NOT_AVAILABLE
      response_parameters:
        - name: ChannelName
          pcf_type: MQCFST
          type_hint: str
        - name: DataCount
          pcf_type: MQCFIN
          type_hint: int
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: ChannelDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHLD_PRIVATE
            - MQCHLD_SHARED
            - MQCHLD_FIXSHARED
            - MQRCCF_ALLOCATE_FAILED
            - MQRCCF_BIND_FAILED
            - MQRCCF_CCSID_ERROR
            - MQRCCF_CHANNEL_CLOSED
            - MQRCCF_CHANNEL_IN_USE
            - MQRCCF_CHANNEL_NOT_FOUND
            - MQRCCF_CHANNEL_TYPE_ERROR
            - MQRCCF_CONFIGURATION_ERROR
            - MQRCCF_CONNECTION_CLOSED
            - MQRCCF_CONNECTION_REFUSED
            - MQRCCF_DATA_TOO_LARGE
            - MQRCCF_ENTRY_ERROR
            - MQRCCF_HOST_NOT_AVAILABLE
            - MQRCCF_NO_COMMS_MANAGER
            - MQRCCF_PING_DATA_COMPARE_ERROR
            - MQRCCF_PING_DATA_COUNT_ERROR
            - MQRCCF_PING_ERROR
            - MQRCCF_RECEIVE_FAILED
            - MQRCCF_RECEIVED_DATA_ERROR
            - MQRCCF_REMOTE_QM_TERMINATING
            - MQRCCF_REMOTE_QM_UNAVAILABLE
            - MQRCCF_SEND_FAILED
            - MQRCCF_STRUCTURE_TYPE_ERROR
            - MQRCCF_TERMINATED_BY_SEC_EXIT
            - MQRCCF_UNKNOWN_REMOTE_CHANNEL
            - MQRCCF_USER_EXIT_NOT_AVAILABLE
    mapping:
      request:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - ChannelDisposition
          - ChannelName
          - CommandScope
          - DataCount
      response:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - ChannelDisposition
          - ChannelName
          - CommandScope
          - DataCount
    notes: []
  - mqsc:
      name: PURGE CHANNEL
      href: SSFKSJ_9.4.0/refadmin/q086450_.html
      positional_parameters:
        - channel name
        - string
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
      name: RESET CHANNEL
      href: SSFKSJ_9.4.0/refadmin/q086510_.html
      positional_parameters:
        - (channel-name)
        - integer
        - qmgr-name
      input_parameters: []
      output_parameters: []
      section_sources:
        {}
    pcf:
      command: MQCMD_RESET_CHANNEL
      request_href: SSFKSJ_9.4.0/refadmin/q088270_.html
      response_href: SSFKSJ_9.4.0/refadmin/q088270_.html
      request_parameters:
        - name: ChannelName
          pcf_type: MQCFST
          type_hint: str
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: ChannelDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHLD_PRIVATE
            - MQCHLD_SHARED
        - name: MsgSeqNumber
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQRCCF_CHANNEL_NOT_FOUND
      response_parameters:
        - name: ChannelName
          pcf_type: MQCFST
          type_hint: str
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: ChannelDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHLD_PRIVATE
            - MQCHLD_SHARED
        - name: MsgSeqNumber
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQRCCF_CHANNEL_NOT_FOUND
    mapping:
      request:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - ChannelDisposition
          - ChannelName
          - CommandScope
          - MsgSeqNumber
      response:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - ChannelDisposition
          - ChannelName
          - CommandScope
          - MsgSeqNumber
    notes: []
  - mqsc:
      name: RESOLVE CHANNEL
      href: SSFKSJ_9.4.0/refadmin/q086570_.html
      positional_parameters:
        - (channel-name)
        - qmgr-name
      input_parameters: []
      output_parameters: []
      section_sources:
        {}
    pcf:
      command: MQCMD_RESOLVE_CHANNEL
      request_href: SSFKSJ_9.4.0/refadmin/q088330_.html
      response_href: SSFKSJ_9.4.0/refadmin/q088330_.html
      request_parameters:
        - name: ChannelName
          pcf_type: MQCFST
          type_hint: str
        - name: InDoubt
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQIDO_COMMIT
            - MQIDO_BACKOUT
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: ChannelDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHLD_PRIVATE
            - MQCHLD_SHARED
            - MQRCCF_CHANNEL_NOT_FOUND
            - MQRCCF_INDOUBT_VALUE_ERROR
      response_parameters:
        - name: ChannelName
          pcf_type: MQCFST
          type_hint: str
        - name: InDoubt
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQIDO_COMMIT
            - MQIDO_BACKOUT
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: ChannelDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHLD_PRIVATE
            - MQCHLD_SHARED
            - MQRCCF_CHANNEL_NOT_FOUND
            - MQRCCF_INDOUBT_VALUE_ERROR
    mapping:
      request:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - ChannelDisposition
          - ChannelName
          - CommandScope
          - InDoubt
      response:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - ChannelDisposition
          - ChannelName
          - CommandScope
          - InDoubt
    notes: []
  - mqsc:
      name: START CHANNEL
      href: SSFKSJ_9.4.0/refadmin/q086660_.html
      positional_parameters:
        - (channel-name)
        - qmgr-name
      input_parameters: []
      output_parameters: []
      section_sources:
        {}
    pcf:
      command: MQCMD_START_CHANNEL
      request_href: SSFKSJ_9.4.0/refadmin/q088420_.html
      response_href: SSFKSJ_9.4.0/refadmin/q088430_.html
      request_parameters:
        - name: ChannelName
          pcf_type: MQCFST
          type_hint: str
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: ChannelDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHLD_PRIVATE
            - MQCHLD_SHARED
            - MQCHLD_FIXSHARED
            - MQIACF_IGNORE_STATE
            - MQIS_NO
            - MQIS_YES
            - MQRCCF_CHANNEL_INDOUBT
            - MQRCCF_CHANNEL_IN_USE
            - MQRCCF_CHANNEL_NOT_FOUND
            - MQRCCF_CHANNEL_TYPE_ERROR
            - MQRCCF_MQCONN_FAILED
            - MQRCCF_MQINQ_FAILED
            - MQRCCF_MQOPEN_FAILED
            - MQRCCF_NOT_XMIT_Q
      response_parameters:
        - name: ChannelName
          pcf_type: MQCFST
          type_hint: str
        - name: ChannelType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQRCCF_PARM_SYNTAX_ERROR
            - MQRCCF_PARM_MISSING
            - MQRCCF_CHANNEL_NOT_FOUND
            - MQRCCF_CHANNEL_IN_USE
            - MQRCCF_NO_STORAGE
            - MQRCCF_COMMAND_FAILED
            - MQRCCF_PORT_IN_USE
            - MQRCCF_BIND_FAILED
            - MQRCCF_SOCKET_ERROR
            - MQRCCF_HOST_NOT_AVAILABLE
    mapping:
      request:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - ChannelDisposition
          - ChannelName
          - CommandScope
      response:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - ChannelName
          - ChannelType
    notes: []
  - mqsc:
      name: STOP CHANNEL
      href: SSFKSJ_9.4.0/refadmin/q086750_.html
      positional_parameters:
        - (channel-name)
        - (connection-name)
        - (qmname)
        - qmgr-name
      input_parameters: []
      output_parameters: []
      section_sources:
        {}
    pcf:
      command: MQCMD_STOP_CHANNEL
      request_href: SSFKSJ_9.4.0/refadmin/q088480_.html
      response_href: SSFKSJ_9.4.0/refadmin/q088490_.html
      request_parameters:
        - name: ChannelName
          pcf_type: MQCFST
          type_hint: str
        - name: ChannelDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHLD_PRIVATE
            - MQCHLD_SHARED
        - name: ChannelStatus
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHS_INACTIVE
            - MQCHS_STOPPED
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: ConnectionName
          pcf_type: MQCFST
          type_hint: str
        - name: Mode
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMODE_QUIESCE
            - MQMODE_FORCE
            - MQMODE_TERMINATE
        - name: QMgrName
          pcf_type: MQCFST
          type_hint: str
          enum_values:
            - MQIACF_IGNORE_STATE
            - MQIS_NO
            - MQIS_YES
            - MQRCCF_CHANNEL_DISABLED
            - MQRCCF_CHANNEL_NOT_ACTIVE
            - MQRCCF_CHANNEL_NOT_FOUND
            - MQRCCF_MODE_VALUE_ERROR
            - MQRCCF_MQCONN_FAILED
            - MQRCCF_MQOPEN_FAILED
            - MQRCCF_MQSET_FAILED
      response_parameters:
        - name: ChannelName
          pcf_type: MQCFST
          type_hint: str
        - name: ChannelType
          pcf_type: MQCFIN
          type_hint: int
        - name: ClientIdentifier
          pcf_type: MQCFST
          type_hint: str
          enum_values:
            - MQRCCF_CHANNEL_DISABLED
            - MQRCCF_CHANNEL_NOT_ACTIVE
            - MQRCCF_CHANNEL_NOT_FOUND
            - MQRCCF_MODE_VALUE_ERROR
            - MQRCCF_MQCONN_FAILED
            - MQRCCF_MQOPEN_FAILED
            - MQRCCF_MQSET_FAILED
    mapping:
      request:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - ChannelDisposition
          - ChannelName
          - ChannelStatus
          - CommandScope
          - ConnectionName
          - Mode
          - QMgrName
      response:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - ChannelName
          - ChannelType
          - ClientIdentifier
    notes: []
```

## Channel command re-parse

This addendum isolates corrected MQSC and PCF parameter sets. It is intentionally separate from the first-run extraction above and omits mapping heuristics.

```yaml
version: 1
generated_at: 2026-01-13T00:20:00Z
commands:
  - mqsc:
      name: ALTER CHANNEL (SDR)
      href: SSFKSJ_9.4.0/refadmin/q085170_.html
      positional_parameters:
        - (channel-name)
      input_parameters:
        - BATCHHB
        - BATCHINT
        - BATCHLIM
        - BATCHSZ
        - CERTLABL
        - CHLTYPE
        - CMDSCOPE
        - COMPHDR
        - COMPMSG
        - CONNAME
        - CONVERT
        - DEFCDISP
        - DESCR
        - DISCINT
        - HBINT
        - KAINT
        - LIKE
        - LOCLADDR
        - LONGRTY
        - LONGTMR
        - MAXMSGL
        - MCANAME
        - MCATYPE
        - MODENAME
        - MONCHL
        - MSGDATA
        - MSGEXIT
        - NPMSPEED
        - PASSWORD
        - PROPCTL
        - QSGDISP
        - RCVDATA
        - RCVEXIT
        - SCYDATA
        - SCYEXIT
        - SENDDATA
        - SENDEXIT
        - SEQWRAP
        - SHORTRTY
        - SHORTTMR
        - SPLPROT
        - SSLCIPH
        - SSLPEER
        - STATCHL
        - TPNAME
        - TRPTYPE
        - USEDLQ
        - USERID
        - XMITQ
      output_parameters:
        []
      section_sources:
        'Parameter descriptions for ALTER CHANNEL':
          - BATCHHB
          - BATCHINT
          - BATCHLIM
          - BATCHSZ
          - CERTLABL
          - CHLTYPE
          - CMDSCOPE
          - COMPHDR
          - COMPMSG
          - CONNAME
          - CONVERT
          - DEFCDISP
          - DESCR
          - DISCINT
          - HBINT
          - KAINT
          - LIKE
          - LOCLADDR
          - LONGRTY
          - LONGTMR
          - MAXMSGL
          - MCANAME
          - MCATYPE
          - MODENAME
          - MONCHL
          - MSGDATA
          - MSGEXIT
          - NPMSPEED
          - PASSWORD
          - PROPCTL
          - QSGDISP
          - RCVDATA
          - RCVEXIT
          - SCYDATA
          - SCYEXIT
          - SENDDATA
          - SENDEXIT
          - SEQWRAP
          - SHORTRTY
          - SHORTTMR
          - SPLPROT
          - SSLCIPH
          - SSLPEER
          - STATCHL
          - TPNAME
          - TRPTYPE
          - USEDLQ
          - USERID
          - XMITQ
    pcf:
      command: MQCMD_CHANGE_CHANNEL
      request_href: SSFKSJ_9.4.0/refadmin/q086930_.html
      response_href: null
      request_parameters:
        - name: ChannelName
          pcf_type: MQCFST
          type_hint: str
        - name: ChannelType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHT_SENDER
            - MQCHT_SERVER
            - MQCHT_RECEIVER
            - MQCHT_REQUESTER
            - MQCHT_SVRCONN
            - MQCHT_CLNTCONN
            - MQCHT_CLUSRCVR
            - MQCHT_CLUSSDR
            - MQCHT_AMQP
        - name: AMQPKeepAlive
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchHeartbeat
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchDataLimit
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchSize
          pcf_type: MQCFIN
          type_hint: int
        - name: CertificateLabel
          pcf_type: MQCFST
          type_hint: str
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
        - name: ChannelStatistics
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_OFF
            - MQMON_Q_MGR
            - MQMON_LOW
            - MQMON_MEDIUM
            - MQMON_HIGH
        - name: ClientChannelWeight
          pcf_type: MQCFIN
          type_hint: int
        - name: ClusterName
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterNamelist
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
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: ConnectionAffinity
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCAFTY_PREFERRED
            - MQCAFTY_NONE
        - name: ConnectionName
          pcf_type: MQCFST
          type_hint: str
        - name: DataConversion
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCDC_NO_SENDER_CONVERSION
            - MQCDC_SENDER_CONVERSION
        - name: DefaultChannelDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHLD_PRIVATE
            - MQCHLD_FIXSHARED
            - MQCHLD_SHARED
        - name: DefReconnect
          pcf_type: MQCFIN
          type_hint: int
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
          enum_values:
            - MQKAI_AUTO
        - name: LocalAddress
          pcf_type: MQCFST
          type_hint: str
        - name: LongRetryCount
          pcf_type: MQCFIN
          type_hint: int
        - name: LongRetryInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxInstances
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxInstancesPerClient
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
            - MQCOMPRESS_ANY
        - name: ModeName
          pcf_type: MQCFST
          type_hint: str
        - name: MsgExit
          pcf_type: MQCFSL
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
          pcf_type: MQCFSL
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
        - name: Port
          pcf_type: MQCFIN
          type_hint: int
        - name: PropertyControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPROP_COMPATIBILITY
            - MQPROP_NONE
            - MQPROP_ALL
        - name: PutAuthority
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPA_DEFAULT
            - MQPA_CONTEXT
            - MQPA_ALTERNATE_OR_MCA
            - MQPA_ONLY_MCA
        - name: QMgrName
          pcf_type: MQCFST
          type_hint: str
        - name: QSGDisposition
          pcf_type: MQCFIN
          type_hint: int
        - name: ReceiveExit
          pcf_type: MQCFSL
          type_hint: str
        - name: ReceiveUserData
          pcf_type: MQCFSL
          type_hint: str
        - name: Replace
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQRP_YES
            - MQRP_NO
        - name: SecurityExit
          pcf_type: MQCFST
          type_hint: str
        - name: SecurityUserData
          pcf_type: MQCFST
          type_hint: str
        - name: SendExit
          pcf_type: MQCFSL
          type_hint: str
        - name: SendUserData
          pcf_type: MQCFSL
          type_hint: str
        - name: SeqNumberWrap
          pcf_type: MQCFIN
          type_hint: int
        - name: SharingConversations
          pcf_type: MQCFIN
          type_hint: int
        - name: ShortRetryCount
          pcf_type: MQCFIN
          type_hint: int
        - name: ShortRetryInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: SPLProtection
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSPL_PASSTHRU
            - MQSPL_REMOVE
            - MQSPL_AS_POLICY
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
        - name: TemporaryModelQName
          pcf_type: MQCFST
          type_hint: str
        - name: TemporaryQPrefix
          pcf_type: MQCFST
          type_hint: str
        - name: TpName
          pcf_type: MQCFST
          type_hint: str
        - name: TPRoot
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
        - name: UseCltId
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQUCI_NO
            - MQUCI_YES
        - name: UseDLQ
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQUSEDLQ_NO
            - MQUSEDLQ_YES
        - name: UserIdentifier
          pcf_type: MQCFST
          type_hint: str
        - name: XmitQName
          pcf_type: MQCFST
          type_hint: str
      response_parameters:
        []
    notes:
      - change-channel-excludes-copy-only-parameters
  - mqsc:
      name: ALTER CHANNEL (SVR)
      href: SSFKSJ_9.4.0/refadmin/q085170_.html
      positional_parameters:
        - (channel-name)
      input_parameters:
        - BATCHHB
        - BATCHINT
        - BATCHLIM
        - BATCHSZ
        - CERTLABL
        - CHLTYPE
        - CMDSCOPE
        - COMPHDR
        - COMPMSG
        - CONNAME
        - CONVERT
        - DEFCDISP
        - DESCR
        - DISCINT
        - HBINT
        - KAINT
        - LIKE
        - LOCLADDR
        - LONGRTY
        - LONGTMR
        - MAXMSGL
        - MCANAME
        - MCATYPE
        - MODENAME
        - MONCHL
        - MSGDATA
        - MSGEXIT
        - NPMSPEED
        - PASSWORD
        - PROPCTL
        - QSGDISP
        - RCVDATA
        - RCVEXIT
        - SCYDATA
        - SCYEXIT
        - SENDDATA
        - SENDEXIT
        - SEQWRAP
        - SHORTRTY
        - SHORTTMR
        - SPLPROT
        - SSLCAUTH
        - SSLCIPH
        - SSLPEER
        - STATCHL
        - TPNAME
        - TRPTYPE
        - USEDLQ
        - USERID
        - XMITQ
      output_parameters:
        []
      section_sources:
        'Parameter descriptions for ALTER CHANNEL':
          - BATCHHB
          - BATCHINT
          - BATCHLIM
          - BATCHSZ
          - CERTLABL
          - CHLTYPE
          - CMDSCOPE
          - COMPHDR
          - COMPMSG
          - CONNAME
          - CONVERT
          - DEFCDISP
          - DESCR
          - DISCINT
          - HBINT
          - KAINT
          - LIKE
          - LOCLADDR
          - LONGRTY
          - LONGTMR
          - MAXMSGL
          - MCANAME
          - MCATYPE
          - MODENAME
          - MONCHL
          - MSGDATA
          - MSGEXIT
          - NPMSPEED
          - PASSWORD
          - PROPCTL
          - QSGDISP
          - RCVDATA
          - RCVEXIT
          - SCYDATA
          - SCYEXIT
          - SENDDATA
          - SENDEXIT
          - SEQWRAP
          - SHORTRTY
          - SHORTTMR
          - SPLPROT
          - SSLCAUTH
          - SSLCIPH
          - SSLPEER
          - STATCHL
          - TPNAME
          - TRPTYPE
          - USEDLQ
          - USERID
          - XMITQ
    pcf:
      command: MQCMD_CHANGE_CHANNEL
      request_href: SSFKSJ_9.4.0/refadmin/q086930_.html
      response_href: null
      request_parameters:
        - name: ChannelName
          pcf_type: MQCFST
          type_hint: str
        - name: ChannelType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHT_SENDER
            - MQCHT_SERVER
            - MQCHT_RECEIVER
            - MQCHT_REQUESTER
            - MQCHT_SVRCONN
            - MQCHT_CLNTCONN
            - MQCHT_CLUSRCVR
            - MQCHT_CLUSSDR
            - MQCHT_AMQP
        - name: AMQPKeepAlive
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchHeartbeat
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchDataLimit
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchSize
          pcf_type: MQCFIN
          type_hint: int
        - name: CertificateLabel
          pcf_type: MQCFST
          type_hint: str
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
        - name: ChannelStatistics
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_OFF
            - MQMON_Q_MGR
            - MQMON_LOW
            - MQMON_MEDIUM
            - MQMON_HIGH
        - name: ClientChannelWeight
          pcf_type: MQCFIN
          type_hint: int
        - name: ClusterName
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterNamelist
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
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: ConnectionAffinity
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCAFTY_PREFERRED
            - MQCAFTY_NONE
        - name: ConnectionName
          pcf_type: MQCFST
          type_hint: str
        - name: DataConversion
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCDC_NO_SENDER_CONVERSION
            - MQCDC_SENDER_CONVERSION
        - name: DefaultChannelDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHLD_PRIVATE
            - MQCHLD_FIXSHARED
            - MQCHLD_SHARED
        - name: DefReconnect
          pcf_type: MQCFIN
          type_hint: int
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
          enum_values:
            - MQKAI_AUTO
        - name: LocalAddress
          pcf_type: MQCFST
          type_hint: str
        - name: LongRetryCount
          pcf_type: MQCFIN
          type_hint: int
        - name: LongRetryInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxInstances
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxInstancesPerClient
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
            - MQCOMPRESS_ANY
        - name: ModeName
          pcf_type: MQCFST
          type_hint: str
        - name: MsgExit
          pcf_type: MQCFSL
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
          pcf_type: MQCFSL
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
        - name: Port
          pcf_type: MQCFIN
          type_hint: int
        - name: PropertyControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPROP_COMPATIBILITY
            - MQPROP_NONE
            - MQPROP_ALL
        - name: PutAuthority
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPA_DEFAULT
            - MQPA_CONTEXT
            - MQPA_ALTERNATE_OR_MCA
            - MQPA_ONLY_MCA
        - name: QMgrName
          pcf_type: MQCFST
          type_hint: str
        - name: QSGDisposition
          pcf_type: MQCFIN
          type_hint: int
        - name: ReceiveExit
          pcf_type: MQCFSL
          type_hint: str
        - name: ReceiveUserData
          pcf_type: MQCFSL
          type_hint: str
        - name: Replace
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQRP_YES
            - MQRP_NO
        - name: SecurityExit
          pcf_type: MQCFST
          type_hint: str
        - name: SecurityUserData
          pcf_type: MQCFST
          type_hint: str
        - name: SendExit
          pcf_type: MQCFSL
          type_hint: str
        - name: SendUserData
          pcf_type: MQCFSL
          type_hint: str
        - name: SeqNumberWrap
          pcf_type: MQCFIN
          type_hint: int
        - name: SharingConversations
          pcf_type: MQCFIN
          type_hint: int
        - name: ShortRetryCount
          pcf_type: MQCFIN
          type_hint: int
        - name: ShortRetryInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: SPLProtection
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSPL_PASSTHRU
            - MQSPL_REMOVE
            - MQSPL_AS_POLICY
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
        - name: TemporaryModelQName
          pcf_type: MQCFST
          type_hint: str
        - name: TemporaryQPrefix
          pcf_type: MQCFST
          type_hint: str
        - name: TpName
          pcf_type: MQCFST
          type_hint: str
        - name: TPRoot
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
        - name: UseCltId
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQUCI_NO
            - MQUCI_YES
        - name: UseDLQ
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQUSEDLQ_NO
            - MQUSEDLQ_YES
        - name: UserIdentifier
          pcf_type: MQCFST
          type_hint: str
        - name: XmitQName
          pcf_type: MQCFST
          type_hint: str
      response_parameters:
        []
    notes:
      - change-channel-excludes-copy-only-parameters
  - mqsc:
      name: ALTER CHANNEL (RCVR)
      href: SSFKSJ_9.4.0/refadmin/q085170_.html
      positional_parameters:
        - (channel-name)
      input_parameters:
        - BATCHSZ
        - CERTLABL
        - CHLTYPE
        - CMDSCOPE
        - COMPHDR
        - COMPMSG
        - DEFCDISP
        - DESCR
        - HBINT
        - KAINT
        - LIKE
        - MAXMSGL
        - MCAUSER
        - MONCHL
        - MRDATA
        - MREXIT
        - MRRTY
        - MRTMR
        - MSGDATA
        - MSGEXIT
        - NPMSPEED
        - PUTAUT
        - QSGDISP
        - RCVDATA
        - RCVEXIT
        - SCYDATA
        - SCYEXIT
        - SENDDATA
        - SENDEXIT
        - SEQWRAP
        - SPLPROT
        - SSLCAUTH
        - SSLCIPH
        - SSLPEER
        - STATCHL
        - TRPTYPE
        - USEDLQ
      output_parameters:
        []
      section_sources:
        'Parameter descriptions for ALTER CHANNEL':
          - BATCHSZ
          - CERTLABL
          - CHLTYPE
          - CMDSCOPE
          - COMPHDR
          - COMPMSG
          - DEFCDISP
          - DESCR
          - HBINT
          - KAINT
          - LIKE
          - MAXMSGL
          - MCAUSER
          - MONCHL
          - MRDATA
          - MREXIT
          - MRRTY
          - MRTMR
          - MSGDATA
          - MSGEXIT
          - NPMSPEED
          - PUTAUT
          - QSGDISP
          - RCVDATA
          - RCVEXIT
          - SCYDATA
          - SCYEXIT
          - SENDDATA
          - SENDEXIT
          - SEQWRAP
          - SPLPROT
          - SSLCAUTH
          - SSLCIPH
          - SSLPEER
          - STATCHL
          - TRPTYPE
          - USEDLQ
    pcf:
      command: MQCMD_CHANGE_CHANNEL
      request_href: SSFKSJ_9.4.0/refadmin/q086930_.html
      response_href: null
      request_parameters:
        - name: ChannelName
          pcf_type: MQCFST
          type_hint: str
        - name: ChannelType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHT_SENDER
            - MQCHT_SERVER
            - MQCHT_RECEIVER
            - MQCHT_REQUESTER
            - MQCHT_SVRCONN
            - MQCHT_CLNTCONN
            - MQCHT_CLUSRCVR
            - MQCHT_CLUSSDR
            - MQCHT_AMQP
        - name: AMQPKeepAlive
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchHeartbeat
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchDataLimit
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchSize
          pcf_type: MQCFIN
          type_hint: int
        - name: CertificateLabel
          pcf_type: MQCFST
          type_hint: str
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
        - name: ChannelStatistics
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_OFF
            - MQMON_Q_MGR
            - MQMON_LOW
            - MQMON_MEDIUM
            - MQMON_HIGH
        - name: ClientChannelWeight
          pcf_type: MQCFIN
          type_hint: int
        - name: ClusterName
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterNamelist
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
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: ConnectionAffinity
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCAFTY_PREFERRED
            - MQCAFTY_NONE
        - name: ConnectionName
          pcf_type: MQCFST
          type_hint: str
        - name: DataConversion
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCDC_NO_SENDER_CONVERSION
            - MQCDC_SENDER_CONVERSION
        - name: DefaultChannelDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHLD_PRIVATE
            - MQCHLD_FIXSHARED
            - MQCHLD_SHARED
        - name: DefReconnect
          pcf_type: MQCFIN
          type_hint: int
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
          enum_values:
            - MQKAI_AUTO
        - name: LocalAddress
          pcf_type: MQCFST
          type_hint: str
        - name: LongRetryCount
          pcf_type: MQCFIN
          type_hint: int
        - name: LongRetryInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxInstances
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxInstancesPerClient
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
            - MQCOMPRESS_ANY
        - name: ModeName
          pcf_type: MQCFST
          type_hint: str
        - name: MsgExit
          pcf_type: MQCFSL
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
          pcf_type: MQCFSL
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
        - name: Port
          pcf_type: MQCFIN
          type_hint: int
        - name: PropertyControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPROP_COMPATIBILITY
            - MQPROP_NONE
            - MQPROP_ALL
        - name: PutAuthority
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPA_DEFAULT
            - MQPA_CONTEXT
            - MQPA_ALTERNATE_OR_MCA
            - MQPA_ONLY_MCA
        - name: QMgrName
          pcf_type: MQCFST
          type_hint: str
        - name: QSGDisposition
          pcf_type: MQCFIN
          type_hint: int
        - name: ReceiveExit
          pcf_type: MQCFSL
          type_hint: str
        - name: ReceiveUserData
          pcf_type: MQCFSL
          type_hint: str
        - name: Replace
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQRP_YES
            - MQRP_NO
        - name: SecurityExit
          pcf_type: MQCFST
          type_hint: str
        - name: SecurityUserData
          pcf_type: MQCFST
          type_hint: str
        - name: SendExit
          pcf_type: MQCFSL
          type_hint: str
        - name: SendUserData
          pcf_type: MQCFSL
          type_hint: str
        - name: SeqNumberWrap
          pcf_type: MQCFIN
          type_hint: int
        - name: SharingConversations
          pcf_type: MQCFIN
          type_hint: int
        - name: ShortRetryCount
          pcf_type: MQCFIN
          type_hint: int
        - name: ShortRetryInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: SPLProtection
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSPL_PASSTHRU
            - MQSPL_REMOVE
            - MQSPL_AS_POLICY
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
        - name: TemporaryModelQName
          pcf_type: MQCFST
          type_hint: str
        - name: TemporaryQPrefix
          pcf_type: MQCFST
          type_hint: str
        - name: TpName
          pcf_type: MQCFST
          type_hint: str
        - name: TPRoot
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
        - name: UseCltId
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQUCI_NO
            - MQUCI_YES
        - name: UseDLQ
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQUSEDLQ_NO
            - MQUSEDLQ_YES
        - name: UserIdentifier
          pcf_type: MQCFST
          type_hint: str
        - name: XmitQName
          pcf_type: MQCFST
          type_hint: str
      response_parameters:
        []
    notes:
      - change-channel-excludes-copy-only-parameters
  - mqsc:
      name: ALTER CHANNEL (RQSTR)
      href: SSFKSJ_9.4.0/refadmin/q085170_.html
      positional_parameters:
        - (channel-name)
      input_parameters:
        - BATCHSZ
        - CERTLABL
        - CHLTYPE
        - CMDSCOPE
        - COMPHDR
        - COMPMSG
        - CONNAME
        - DEFCDISP
        - DESCR
        - HBINT
        - KAINT
        - LIKE
        - LOCLADDR
        - MAXMSGL
        - MCANAME
        - MCATYPE
        - MCAUSER
        - MODENAME
        - MONCHL
        - MRDATA
        - MREXIT
        - MRRTY
        - MRTMR
        - MSGDATA
        - MSGEXIT
        - NPMSPEED
        - PASSWORD
        - PUTAUT
        - QSGDISP
        - RCVDATA
        - RCVEXIT
        - SCYDATA
        - SCYEXIT
        - SENDDATA
        - SENDEXIT
        - SEQWRAP
        - SPLPROT
        - SSLCAUTH
        - SSLCIPH
        - SSLPEER
        - STATCHL
        - TPNAME
        - TRPTYPE
        - USEDLQ
        - USERID
      output_parameters:
        []
      section_sources:
        'Parameter descriptions for ALTER CHANNEL':
          - BATCHSZ
          - CERTLABL
          - CHLTYPE
          - CMDSCOPE
          - COMPHDR
          - COMPMSG
          - CONNAME
          - DEFCDISP
          - DESCR
          - HBINT
          - KAINT
          - LIKE
          - LOCLADDR
          - MAXMSGL
          - MCANAME
          - MCATYPE
          - MCAUSER
          - MODENAME
          - MONCHL
          - MRDATA
          - MREXIT
          - MRRTY
          - MRTMR
          - MSGDATA
          - MSGEXIT
          - NPMSPEED
          - PASSWORD
          - PUTAUT
          - QSGDISP
          - RCVDATA
          - RCVEXIT
          - SCYDATA
          - SCYEXIT
          - SENDDATA
          - SENDEXIT
          - SEQWRAP
          - SPLPROT
          - SSLCAUTH
          - SSLCIPH
          - SSLPEER
          - STATCHL
          - TPNAME
          - TRPTYPE
          - USEDLQ
          - USERID
    pcf:
      command: MQCMD_CHANGE_CHANNEL
      request_href: SSFKSJ_9.4.0/refadmin/q086930_.html
      response_href: null
      request_parameters:
        - name: ChannelName
          pcf_type: MQCFST
          type_hint: str
        - name: ChannelType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHT_SENDER
            - MQCHT_SERVER
            - MQCHT_RECEIVER
            - MQCHT_REQUESTER
            - MQCHT_SVRCONN
            - MQCHT_CLNTCONN
            - MQCHT_CLUSRCVR
            - MQCHT_CLUSSDR
            - MQCHT_AMQP
        - name: AMQPKeepAlive
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchHeartbeat
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchDataLimit
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchSize
          pcf_type: MQCFIN
          type_hint: int
        - name: CertificateLabel
          pcf_type: MQCFST
          type_hint: str
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
        - name: ChannelStatistics
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_OFF
            - MQMON_Q_MGR
            - MQMON_LOW
            - MQMON_MEDIUM
            - MQMON_HIGH
        - name: ClientChannelWeight
          pcf_type: MQCFIN
          type_hint: int
        - name: ClusterName
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterNamelist
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
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: ConnectionAffinity
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCAFTY_PREFERRED
            - MQCAFTY_NONE
        - name: ConnectionName
          pcf_type: MQCFST
          type_hint: str
        - name: DataConversion
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCDC_NO_SENDER_CONVERSION
            - MQCDC_SENDER_CONVERSION
        - name: DefaultChannelDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHLD_PRIVATE
            - MQCHLD_FIXSHARED
            - MQCHLD_SHARED
        - name: DefReconnect
          pcf_type: MQCFIN
          type_hint: int
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
          enum_values:
            - MQKAI_AUTO
        - name: LocalAddress
          pcf_type: MQCFST
          type_hint: str
        - name: LongRetryCount
          pcf_type: MQCFIN
          type_hint: int
        - name: LongRetryInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxInstances
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxInstancesPerClient
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
            - MQCOMPRESS_ANY
        - name: ModeName
          pcf_type: MQCFST
          type_hint: str
        - name: MsgExit
          pcf_type: MQCFSL
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
          pcf_type: MQCFSL
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
        - name: Port
          pcf_type: MQCFIN
          type_hint: int
        - name: PropertyControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPROP_COMPATIBILITY
            - MQPROP_NONE
            - MQPROP_ALL
        - name: PutAuthority
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPA_DEFAULT
            - MQPA_CONTEXT
            - MQPA_ALTERNATE_OR_MCA
            - MQPA_ONLY_MCA
        - name: QMgrName
          pcf_type: MQCFST
          type_hint: str
        - name: QSGDisposition
          pcf_type: MQCFIN
          type_hint: int
        - name: ReceiveExit
          pcf_type: MQCFSL
          type_hint: str
        - name: ReceiveUserData
          pcf_type: MQCFSL
          type_hint: str
        - name: Replace
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQRP_YES
            - MQRP_NO
        - name: SecurityExit
          pcf_type: MQCFST
          type_hint: str
        - name: SecurityUserData
          pcf_type: MQCFST
          type_hint: str
        - name: SendExit
          pcf_type: MQCFSL
          type_hint: str
        - name: SendUserData
          pcf_type: MQCFSL
          type_hint: str
        - name: SeqNumberWrap
          pcf_type: MQCFIN
          type_hint: int
        - name: SharingConversations
          pcf_type: MQCFIN
          type_hint: int
        - name: ShortRetryCount
          pcf_type: MQCFIN
          type_hint: int
        - name: ShortRetryInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: SPLProtection
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSPL_PASSTHRU
            - MQSPL_REMOVE
            - MQSPL_AS_POLICY
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
        - name: TemporaryModelQName
          pcf_type: MQCFST
          type_hint: str
        - name: TemporaryQPrefix
          pcf_type: MQCFST
          type_hint: str
        - name: TpName
          pcf_type: MQCFST
          type_hint: str
        - name: TPRoot
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
        - name: UseCltId
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQUCI_NO
            - MQUCI_YES
        - name: UseDLQ
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQUSEDLQ_NO
            - MQUSEDLQ_YES
        - name: UserIdentifier
          pcf_type: MQCFST
          type_hint: str
        - name: XmitQName
          pcf_type: MQCFST
          type_hint: str
      response_parameters:
        []
    notes:
      - change-channel-excludes-copy-only-parameters
  - mqsc:
      name: ALTER CHANNEL (CLNTCONN)
      href: SSFKSJ_9.4.0/refadmin/q085170_.html
      positional_parameters:
        - (channel-name)
      input_parameters:
        - AFFINITY
        - CERTLABL
        - CHLTYPE
        - CLNTWGHT
        - CMDSCOPE
        - COMPHDR
        - COMPMSG
        - CONNAME
        - DEFRECON
        - DESCR
        - HBINT
        - KAINT
        - LIKE
        - LOCLADDR
        - MAXMSGL
        - MODENAME
        - PASSWORD
        - QMNAME
        - QSGDISP
        - RCVDATA
        - RCVEXIT
        - SCYDATA
        - SCYEXIT
        - SENDDATA
        - SENDEXIT
        - SHARECNV
        - SSLCIPH
        - SSLPEER
        - TPNAME
        - TRPTYPE
        - USERID
      output_parameters:
        []
      section_sources:
        'Parameter descriptions for ALTER CHANNEL':
          - AFFINITY
          - CERTLABL
          - CHLTYPE
          - CLNTWGHT
          - CMDSCOPE
          - COMPHDR
          - COMPMSG
          - CONNAME
          - DEFRECON
          - DESCR
          - HBINT
          - KAINT
          - LIKE
          - LOCLADDR
          - MAXMSGL
          - MODENAME
          - PASSWORD
          - QMNAME
          - QSGDISP
          - RCVDATA
          - RCVEXIT
          - SCYDATA
          - SCYEXIT
          - SENDDATA
          - SENDEXIT
          - SHARECNV
          - SSLCIPH
          - SSLPEER
          - TPNAME
          - TRPTYPE
          - USERID
    pcf:
      command: MQCMD_CHANGE_CHANNEL
      request_href: SSFKSJ_9.4.0/refadmin/q086930_.html
      response_href: null
      request_parameters:
        - name: ChannelName
          pcf_type: MQCFST
          type_hint: str
        - name: ChannelType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHT_SENDER
            - MQCHT_SERVER
            - MQCHT_RECEIVER
            - MQCHT_REQUESTER
            - MQCHT_SVRCONN
            - MQCHT_CLNTCONN
            - MQCHT_CLUSRCVR
            - MQCHT_CLUSSDR
            - MQCHT_AMQP
        - name: AMQPKeepAlive
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchHeartbeat
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchDataLimit
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchSize
          pcf_type: MQCFIN
          type_hint: int
        - name: CertificateLabel
          pcf_type: MQCFST
          type_hint: str
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
        - name: ChannelStatistics
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_OFF
            - MQMON_Q_MGR
            - MQMON_LOW
            - MQMON_MEDIUM
            - MQMON_HIGH
        - name: ClientChannelWeight
          pcf_type: MQCFIN
          type_hint: int
        - name: ClusterName
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterNamelist
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
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: ConnectionAffinity
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCAFTY_PREFERRED
            - MQCAFTY_NONE
        - name: ConnectionName
          pcf_type: MQCFST
          type_hint: str
        - name: DataConversion
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCDC_NO_SENDER_CONVERSION
            - MQCDC_SENDER_CONVERSION
        - name: DefaultChannelDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHLD_PRIVATE
            - MQCHLD_FIXSHARED
            - MQCHLD_SHARED
        - name: DefReconnect
          pcf_type: MQCFIN
          type_hint: int
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
          enum_values:
            - MQKAI_AUTO
        - name: LocalAddress
          pcf_type: MQCFST
          type_hint: str
        - name: LongRetryCount
          pcf_type: MQCFIN
          type_hint: int
        - name: LongRetryInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxInstances
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxInstancesPerClient
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
            - MQCOMPRESS_ANY
        - name: ModeName
          pcf_type: MQCFST
          type_hint: str
        - name: MsgExit
          pcf_type: MQCFSL
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
          pcf_type: MQCFSL
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
        - name: Port
          pcf_type: MQCFIN
          type_hint: int
        - name: PropertyControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPROP_COMPATIBILITY
            - MQPROP_NONE
            - MQPROP_ALL
        - name: PutAuthority
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPA_DEFAULT
            - MQPA_CONTEXT
            - MQPA_ALTERNATE_OR_MCA
            - MQPA_ONLY_MCA
        - name: QMgrName
          pcf_type: MQCFST
          type_hint: str
        - name: QSGDisposition
          pcf_type: MQCFIN
          type_hint: int
        - name: ReceiveExit
          pcf_type: MQCFSL
          type_hint: str
        - name: ReceiveUserData
          pcf_type: MQCFSL
          type_hint: str
        - name: Replace
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQRP_YES
            - MQRP_NO
        - name: SecurityExit
          pcf_type: MQCFST
          type_hint: str
        - name: SecurityUserData
          pcf_type: MQCFST
          type_hint: str
        - name: SendExit
          pcf_type: MQCFSL
          type_hint: str
        - name: SendUserData
          pcf_type: MQCFSL
          type_hint: str
        - name: SeqNumberWrap
          pcf_type: MQCFIN
          type_hint: int
        - name: SharingConversations
          pcf_type: MQCFIN
          type_hint: int
        - name: ShortRetryCount
          pcf_type: MQCFIN
          type_hint: int
        - name: ShortRetryInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: SPLProtection
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSPL_PASSTHRU
            - MQSPL_REMOVE
            - MQSPL_AS_POLICY
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
        - name: TemporaryModelQName
          pcf_type: MQCFST
          type_hint: str
        - name: TemporaryQPrefix
          pcf_type: MQCFST
          type_hint: str
        - name: TpName
          pcf_type: MQCFST
          type_hint: str
        - name: TPRoot
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
        - name: UseCltId
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQUCI_NO
            - MQUCI_YES
        - name: UseDLQ
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQUSEDLQ_NO
            - MQUSEDLQ_YES
        - name: UserIdentifier
          pcf_type: MQCFST
          type_hint: str
        - name: XmitQName
          pcf_type: MQCFST
          type_hint: str
      response_parameters:
        []
    notes:
      - change-channel-excludes-copy-only-parameters
  - mqsc:
      name: ALTER CHANNEL (SVRCONN)
      href: SSFKSJ_9.4.0/refadmin/q085170_.html
      positional_parameters:
        - (channel-name)
      input_parameters:
        - CERTLABL
        - CHLTYPE
        - CMDSCOPE
        - COMPHDR
        - COMPMSG
        - DEFCDISP
        - DESCR
        - DISCINT
        - HBINT
        - KAINT
        - LIKE
        - MAXINST
        - MAXINSTC
        - MAXMSGL
        - MCAUSER
        - MONCHL
        - PUTAUT
        - QSGDISP
        - RCVDATA
        - RCVEXIT
        - SCYDATA
        - SCYEXIT
        - SENDDATA
        - SENDEXIT
        - SHARECNV
        - SSLCAUTH
        - SSLCIPH
        - SSLPEER
        - TPNAME
        - TRPTYPE
      output_parameters:
        []
      section_sources:
        'Parameter descriptions for ALTER CHANNEL':
          - CERTLABL
          - CHLTYPE
          - CMDSCOPE
          - COMPHDR
          - COMPMSG
          - DEFCDISP
          - DESCR
          - DISCINT
          - HBINT
          - KAINT
          - LIKE
          - MAXINST
          - MAXINSTC
          - MAXMSGL
          - MCAUSER
          - MONCHL
          - PUTAUT
          - QSGDISP
          - RCVDATA
          - RCVEXIT
          - SCYDATA
          - SCYEXIT
          - SENDDATA
          - SENDEXIT
          - SHARECNV
          - SSLCAUTH
          - SSLCIPH
          - SSLPEER
          - TPNAME
          - TRPTYPE
    pcf:
      command: MQCMD_CHANGE_CHANNEL
      request_href: SSFKSJ_9.4.0/refadmin/q086930_.html
      response_href: null
      request_parameters:
        - name: ChannelName
          pcf_type: MQCFST
          type_hint: str
        - name: ChannelType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHT_SENDER
            - MQCHT_SERVER
            - MQCHT_RECEIVER
            - MQCHT_REQUESTER
            - MQCHT_SVRCONN
            - MQCHT_CLNTCONN
            - MQCHT_CLUSRCVR
            - MQCHT_CLUSSDR
            - MQCHT_AMQP
        - name: AMQPKeepAlive
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchHeartbeat
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchDataLimit
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchSize
          pcf_type: MQCFIN
          type_hint: int
        - name: CertificateLabel
          pcf_type: MQCFST
          type_hint: str
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
        - name: ChannelStatistics
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_OFF
            - MQMON_Q_MGR
            - MQMON_LOW
            - MQMON_MEDIUM
            - MQMON_HIGH
        - name: ClientChannelWeight
          pcf_type: MQCFIN
          type_hint: int
        - name: ClusterName
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterNamelist
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
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: ConnectionAffinity
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCAFTY_PREFERRED
            - MQCAFTY_NONE
        - name: ConnectionName
          pcf_type: MQCFST
          type_hint: str
        - name: DataConversion
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCDC_NO_SENDER_CONVERSION
            - MQCDC_SENDER_CONVERSION
        - name: DefaultChannelDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHLD_PRIVATE
            - MQCHLD_FIXSHARED
            - MQCHLD_SHARED
        - name: DefReconnect
          pcf_type: MQCFIN
          type_hint: int
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
          enum_values:
            - MQKAI_AUTO
        - name: LocalAddress
          pcf_type: MQCFST
          type_hint: str
        - name: LongRetryCount
          pcf_type: MQCFIN
          type_hint: int
        - name: LongRetryInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxInstances
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxInstancesPerClient
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
            - MQCOMPRESS_ANY
        - name: ModeName
          pcf_type: MQCFST
          type_hint: str
        - name: MsgExit
          pcf_type: MQCFSL
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
          pcf_type: MQCFSL
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
        - name: Port
          pcf_type: MQCFIN
          type_hint: int
        - name: PropertyControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPROP_COMPATIBILITY
            - MQPROP_NONE
            - MQPROP_ALL
        - name: PutAuthority
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPA_DEFAULT
            - MQPA_CONTEXT
            - MQPA_ALTERNATE_OR_MCA
            - MQPA_ONLY_MCA
        - name: QMgrName
          pcf_type: MQCFST
          type_hint: str
        - name: QSGDisposition
          pcf_type: MQCFIN
          type_hint: int
        - name: ReceiveExit
          pcf_type: MQCFSL
          type_hint: str
        - name: ReceiveUserData
          pcf_type: MQCFSL
          type_hint: str
        - name: Replace
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQRP_YES
            - MQRP_NO
        - name: SecurityExit
          pcf_type: MQCFST
          type_hint: str
        - name: SecurityUserData
          pcf_type: MQCFST
          type_hint: str
        - name: SendExit
          pcf_type: MQCFSL
          type_hint: str
        - name: SendUserData
          pcf_type: MQCFSL
          type_hint: str
        - name: SeqNumberWrap
          pcf_type: MQCFIN
          type_hint: int
        - name: SharingConversations
          pcf_type: MQCFIN
          type_hint: int
        - name: ShortRetryCount
          pcf_type: MQCFIN
          type_hint: int
        - name: ShortRetryInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: SPLProtection
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSPL_PASSTHRU
            - MQSPL_REMOVE
            - MQSPL_AS_POLICY
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
        - name: TemporaryModelQName
          pcf_type: MQCFST
          type_hint: str
        - name: TemporaryQPrefix
          pcf_type: MQCFST
          type_hint: str
        - name: TpName
          pcf_type: MQCFST
          type_hint: str
        - name: TPRoot
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
        - name: UseCltId
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQUCI_NO
            - MQUCI_YES
        - name: UseDLQ
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQUSEDLQ_NO
            - MQUSEDLQ_YES
        - name: UserIdentifier
          pcf_type: MQCFST
          type_hint: str
        - name: XmitQName
          pcf_type: MQCFST
          type_hint: str
      response_parameters:
        []
    notes:
      - change-channel-excludes-copy-only-parameters
  - mqsc:
      name: ALTER CHANNEL (CLUSSDR)
      href: SSFKSJ_9.4.0/refadmin/q085170_.html
      positional_parameters:
        - (channel-name)
      input_parameters:
        - BATCHHB
        - BATCHINT
        - BATCHLIM
        - BATCHSZ
        - CHLTYPE
        - CLUSNL
        - CLUSTER
        - CLWLPRTY
        - CLWLRANK
        - CLWLWGHT
        - CMDSCOPE
        - COMPHDR
        - COMPMSG
        - CONNAME
        - CONVERT
        - DESCR
        - DISCINT
        - HBINT
        - KAINT
        - LIKE
        - LOCLADDR
        - LONGRTY
        - LONGTMR
        - MAXMSGL
        - MCANAME
        - MCATYPE
        - MODENAME
        - MONCHL
        - MSGDATA
        - MSGEXIT
        - NPMSPEED
        - PASSWORD
        - PROPCTL
        - QSGDISP
        - RCVDATA
        - RCVEXIT
        - SCYDATA
        - SCYEXIT
        - SENDDATA
        - SENDEXIT
        - SEQWRAP
        - SHORTRTY
        - SHORTTMR
        - SSLCIPH
        - SSLPEER
        - STATCHL
        - TPNAME
        - TRPTYPE
        - USEDLQ
        - USERID
      output_parameters:
        []
      section_sources:
        'Parameter descriptions for ALTER CHANNEL':
          - BATCHHB
          - BATCHINT
          - BATCHLIM
          - BATCHSZ
          - CHLTYPE
          - CLUSNL
          - CLUSTER
          - CLWLPRTY
          - CLWLRANK
          - CLWLWGHT
          - CMDSCOPE
          - COMPHDR
          - COMPMSG
          - CONNAME
          - CONVERT
          - DESCR
          - DISCINT
          - HBINT
          - KAINT
          - LIKE
          - LOCLADDR
          - LONGRTY
          - LONGTMR
          - MAXMSGL
          - MCANAME
          - MCATYPE
          - MODENAME
          - MONCHL
          - MSGDATA
          - MSGEXIT
          - NPMSPEED
          - PASSWORD
          - PROPCTL
          - QSGDISP
          - RCVDATA
          - RCVEXIT
          - SCYDATA
          - SCYEXIT
          - SENDDATA
          - SENDEXIT
          - SEQWRAP
          - SHORTRTY
          - SHORTTMR
          - SSLCIPH
          - SSLPEER
          - STATCHL
          - TPNAME
          - TRPTYPE
          - USEDLQ
          - USERID
    pcf:
      command: MQCMD_CHANGE_CHANNEL
      request_href: SSFKSJ_9.4.0/refadmin/q086930_.html
      response_href: null
      request_parameters:
        - name: ChannelName
          pcf_type: MQCFST
          type_hint: str
        - name: ChannelType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHT_SENDER
            - MQCHT_SERVER
            - MQCHT_RECEIVER
            - MQCHT_REQUESTER
            - MQCHT_SVRCONN
            - MQCHT_CLNTCONN
            - MQCHT_CLUSRCVR
            - MQCHT_CLUSSDR
            - MQCHT_AMQP
        - name: AMQPKeepAlive
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchHeartbeat
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchDataLimit
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchSize
          pcf_type: MQCFIN
          type_hint: int
        - name: CertificateLabel
          pcf_type: MQCFST
          type_hint: str
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
        - name: ChannelStatistics
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_OFF
            - MQMON_Q_MGR
            - MQMON_LOW
            - MQMON_MEDIUM
            - MQMON_HIGH
        - name: ClientChannelWeight
          pcf_type: MQCFIN
          type_hint: int
        - name: ClusterName
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterNamelist
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
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: ConnectionAffinity
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCAFTY_PREFERRED
            - MQCAFTY_NONE
        - name: ConnectionName
          pcf_type: MQCFST
          type_hint: str
        - name: DataConversion
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCDC_NO_SENDER_CONVERSION
            - MQCDC_SENDER_CONVERSION
        - name: DefaultChannelDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHLD_PRIVATE
            - MQCHLD_FIXSHARED
            - MQCHLD_SHARED
        - name: DefReconnect
          pcf_type: MQCFIN
          type_hint: int
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
          enum_values:
            - MQKAI_AUTO
        - name: LocalAddress
          pcf_type: MQCFST
          type_hint: str
        - name: LongRetryCount
          pcf_type: MQCFIN
          type_hint: int
        - name: LongRetryInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxInstances
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxInstancesPerClient
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
            - MQCOMPRESS_ANY
        - name: ModeName
          pcf_type: MQCFST
          type_hint: str
        - name: MsgExit
          pcf_type: MQCFSL
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
          pcf_type: MQCFSL
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
        - name: Port
          pcf_type: MQCFIN
          type_hint: int
        - name: PropertyControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPROP_COMPATIBILITY
            - MQPROP_NONE
            - MQPROP_ALL
        - name: PutAuthority
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPA_DEFAULT
            - MQPA_CONTEXT
            - MQPA_ALTERNATE_OR_MCA
            - MQPA_ONLY_MCA
        - name: QMgrName
          pcf_type: MQCFST
          type_hint: str
        - name: QSGDisposition
          pcf_type: MQCFIN
          type_hint: int
        - name: ReceiveExit
          pcf_type: MQCFSL
          type_hint: str
        - name: ReceiveUserData
          pcf_type: MQCFSL
          type_hint: str
        - name: Replace
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQRP_YES
            - MQRP_NO
        - name: SecurityExit
          pcf_type: MQCFST
          type_hint: str
        - name: SecurityUserData
          pcf_type: MQCFST
          type_hint: str
        - name: SendExit
          pcf_type: MQCFSL
          type_hint: str
        - name: SendUserData
          pcf_type: MQCFSL
          type_hint: str
        - name: SeqNumberWrap
          pcf_type: MQCFIN
          type_hint: int
        - name: SharingConversations
          pcf_type: MQCFIN
          type_hint: int
        - name: ShortRetryCount
          pcf_type: MQCFIN
          type_hint: int
        - name: ShortRetryInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: SPLProtection
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSPL_PASSTHRU
            - MQSPL_REMOVE
            - MQSPL_AS_POLICY
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
        - name: TemporaryModelQName
          pcf_type: MQCFST
          type_hint: str
        - name: TemporaryQPrefix
          pcf_type: MQCFST
          type_hint: str
        - name: TpName
          pcf_type: MQCFST
          type_hint: str
        - name: TPRoot
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
        - name: UseCltId
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQUCI_NO
            - MQUCI_YES
        - name: UseDLQ
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQUSEDLQ_NO
            - MQUSEDLQ_YES
        - name: UserIdentifier
          pcf_type: MQCFST
          type_hint: str
        - name: XmitQName
          pcf_type: MQCFST
          type_hint: str
      response_parameters:
        []
    notes:
      - change-channel-excludes-copy-only-parameters
  - mqsc:
      name: ALTER CHANNEL (CLUSRCVR)
      href: SSFKSJ_9.4.0/refadmin/q085170_.html
      positional_parameters:
        - (channel-name)
      input_parameters:
        - BATCHHB
        - BATCHINT
        - BATCHLIM
        - BATCHSZ
        - CERTLABL
        - CHLTYPE
        - CLUSNL
        - CLUSTER
        - CLWLPRTY
        - CLWLRANK
        - CLWLWGHT
        - CMDSCOPE
        - COMPHDR
        - COMPMSG
        - CONNAME
        - CONVERT
        - DESCR
        - DISCINT
        - HBINT
        - KAINT
        - LIKE
        - LOCLADDR
        - LONGRTY
        - LONGTMR
        - MAXMSGL
        - MCANAME
        - MCATYPE
        - MCAUSER
        - MODENAME
        - MONCHL
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
        - QSGDISP
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
        - STATCHL
        - TPNAME
        - TRPTYPE
        - USEDLQ
      output_parameters:
        []
      section_sources:
        'Parameter descriptions for ALTER CHANNEL':
          - BATCHHB
          - BATCHINT
          - BATCHLIM
          - BATCHSZ
          - CERTLABL
          - CHLTYPE
          - CLUSNL
          - CLUSTER
          - CLWLPRTY
          - CLWLRANK
          - CLWLWGHT
          - CMDSCOPE
          - COMPHDR
          - COMPMSG
          - CONNAME
          - CONVERT
          - DESCR
          - DISCINT
          - HBINT
          - KAINT
          - LIKE
          - LOCLADDR
          - LONGRTY
          - LONGTMR
          - MAXMSGL
          - MCANAME
          - MCATYPE
          - MCAUSER
          - MODENAME
          - MONCHL
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
          - QSGDISP
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
          - STATCHL
          - TPNAME
          - TRPTYPE
          - USEDLQ
    pcf:
      command: MQCMD_CHANGE_CHANNEL
      request_href: SSFKSJ_9.4.0/refadmin/q086930_.html
      response_href: null
      request_parameters:
        - name: ChannelName
          pcf_type: MQCFST
          type_hint: str
        - name: ChannelType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHT_SENDER
            - MQCHT_SERVER
            - MQCHT_RECEIVER
            - MQCHT_REQUESTER
            - MQCHT_SVRCONN
            - MQCHT_CLNTCONN
            - MQCHT_CLUSRCVR
            - MQCHT_CLUSSDR
            - MQCHT_AMQP
        - name: AMQPKeepAlive
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchHeartbeat
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchDataLimit
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchSize
          pcf_type: MQCFIN
          type_hint: int
        - name: CertificateLabel
          pcf_type: MQCFST
          type_hint: str
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
        - name: ChannelStatistics
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_OFF
            - MQMON_Q_MGR
            - MQMON_LOW
            - MQMON_MEDIUM
            - MQMON_HIGH
        - name: ClientChannelWeight
          pcf_type: MQCFIN
          type_hint: int
        - name: ClusterName
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterNamelist
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
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: ConnectionAffinity
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCAFTY_PREFERRED
            - MQCAFTY_NONE
        - name: ConnectionName
          pcf_type: MQCFST
          type_hint: str
        - name: DataConversion
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCDC_NO_SENDER_CONVERSION
            - MQCDC_SENDER_CONVERSION
        - name: DefaultChannelDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHLD_PRIVATE
            - MQCHLD_FIXSHARED
            - MQCHLD_SHARED
        - name: DefReconnect
          pcf_type: MQCFIN
          type_hint: int
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
          enum_values:
            - MQKAI_AUTO
        - name: LocalAddress
          pcf_type: MQCFST
          type_hint: str
        - name: LongRetryCount
          pcf_type: MQCFIN
          type_hint: int
        - name: LongRetryInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxInstances
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxInstancesPerClient
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
            - MQCOMPRESS_ANY
        - name: ModeName
          pcf_type: MQCFST
          type_hint: str
        - name: MsgExit
          pcf_type: MQCFSL
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
          pcf_type: MQCFSL
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
        - name: Port
          pcf_type: MQCFIN
          type_hint: int
        - name: PropertyControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPROP_COMPATIBILITY
            - MQPROP_NONE
            - MQPROP_ALL
        - name: PutAuthority
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPA_DEFAULT
            - MQPA_CONTEXT
            - MQPA_ALTERNATE_OR_MCA
            - MQPA_ONLY_MCA
        - name: QMgrName
          pcf_type: MQCFST
          type_hint: str
        - name: QSGDisposition
          pcf_type: MQCFIN
          type_hint: int
        - name: ReceiveExit
          pcf_type: MQCFSL
          type_hint: str
        - name: ReceiveUserData
          pcf_type: MQCFSL
          type_hint: str
        - name: Replace
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQRP_YES
            - MQRP_NO
        - name: SecurityExit
          pcf_type: MQCFST
          type_hint: str
        - name: SecurityUserData
          pcf_type: MQCFST
          type_hint: str
        - name: SendExit
          pcf_type: MQCFSL
          type_hint: str
        - name: SendUserData
          pcf_type: MQCFSL
          type_hint: str
        - name: SeqNumberWrap
          pcf_type: MQCFIN
          type_hint: int
        - name: SharingConversations
          pcf_type: MQCFIN
          type_hint: int
        - name: ShortRetryCount
          pcf_type: MQCFIN
          type_hint: int
        - name: ShortRetryInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: SPLProtection
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSPL_PASSTHRU
            - MQSPL_REMOVE
            - MQSPL_AS_POLICY
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
        - name: TemporaryModelQName
          pcf_type: MQCFST
          type_hint: str
        - name: TemporaryQPrefix
          pcf_type: MQCFST
          type_hint: str
        - name: TpName
          pcf_type: MQCFST
          type_hint: str
        - name: TPRoot
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
        - name: UseCltId
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQUCI_NO
            - MQUCI_YES
        - name: UseDLQ
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQUSEDLQ_NO
            - MQUSEDLQ_YES
        - name: UserIdentifier
          pcf_type: MQCFST
          type_hint: str
        - name: XmitQName
          pcf_type: MQCFST
          type_hint: str
      response_parameters:
        []
    notes:
      - change-channel-excludes-copy-only-parameters
  - mqsc:
      name: ALTER CHANNEL (AMQP)
      href: SSFKSJ_9.4.0/refadmin/q085170_.html
      positional_parameters:
        - (channel-name)
      input_parameters:
        - AMQPKA
        - CERTLABL
        - CHLTYPE
        - DESCR
        - LOCLADDR
        - MAXINST
        - MAXMSGL
        - MCAUSER
        - PORT
        - SSLCIPH
        - SSLPEER
        - TMPMODEL
        - TMPQPRFX
        - TPROOT
        - USECLTID
      output_parameters:
        []
      section_sources:
        'Parameter descriptions for ALTER CHANNEL':
          - AMQPKA
          - CERTLABL
          - CHLTYPE
          - DESCR
          - LOCLADDR
          - MAXINST
          - MAXMSGL
          - MCAUSER
          - PORT
          - SSLCIPH
          - SSLPEER
          - TMPMODEL
          - TMPQPRFX
          - TPROOT
          - USECLTID
    pcf:
      command: MQCMD_CHANGE_CHANNEL
      request_href: SSFKSJ_9.4.0/refadmin/q086930_.html
      response_href: null
      request_parameters:
        - name: ChannelName
          pcf_type: MQCFST
          type_hint: str
        - name: ChannelType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHT_SENDER
            - MQCHT_SERVER
            - MQCHT_RECEIVER
            - MQCHT_REQUESTER
            - MQCHT_SVRCONN
            - MQCHT_CLNTCONN
            - MQCHT_CLUSRCVR
            - MQCHT_CLUSSDR
            - MQCHT_AMQP
        - name: AMQPKeepAlive
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchHeartbeat
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchDataLimit
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchSize
          pcf_type: MQCFIN
          type_hint: int
        - name: CertificateLabel
          pcf_type: MQCFST
          type_hint: str
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
        - name: ChannelStatistics
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_OFF
            - MQMON_Q_MGR
            - MQMON_LOW
            - MQMON_MEDIUM
            - MQMON_HIGH
        - name: ClientChannelWeight
          pcf_type: MQCFIN
          type_hint: int
        - name: ClusterName
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterNamelist
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
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: ConnectionAffinity
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCAFTY_PREFERRED
            - MQCAFTY_NONE
        - name: ConnectionName
          pcf_type: MQCFST
          type_hint: str
        - name: DataConversion
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCDC_NO_SENDER_CONVERSION
            - MQCDC_SENDER_CONVERSION
        - name: DefaultChannelDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHLD_PRIVATE
            - MQCHLD_FIXSHARED
            - MQCHLD_SHARED
        - name: DefReconnect
          pcf_type: MQCFIN
          type_hint: int
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
          enum_values:
            - MQKAI_AUTO
        - name: LocalAddress
          pcf_type: MQCFST
          type_hint: str
        - name: LongRetryCount
          pcf_type: MQCFIN
          type_hint: int
        - name: LongRetryInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxInstances
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxInstancesPerClient
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
            - MQCOMPRESS_ANY
        - name: ModeName
          pcf_type: MQCFST
          type_hint: str
        - name: MsgExit
          pcf_type: MQCFSL
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
          pcf_type: MQCFSL
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
        - name: Port
          pcf_type: MQCFIN
          type_hint: int
        - name: PropertyControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPROP_COMPATIBILITY
            - MQPROP_NONE
            - MQPROP_ALL
        - name: PutAuthority
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPA_DEFAULT
            - MQPA_CONTEXT
            - MQPA_ALTERNATE_OR_MCA
            - MQPA_ONLY_MCA
        - name: QMgrName
          pcf_type: MQCFST
          type_hint: str
        - name: QSGDisposition
          pcf_type: MQCFIN
          type_hint: int
        - name: ReceiveExit
          pcf_type: MQCFSL
          type_hint: str
        - name: ReceiveUserData
          pcf_type: MQCFSL
          type_hint: str
        - name: Replace
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQRP_YES
            - MQRP_NO
        - name: SecurityExit
          pcf_type: MQCFST
          type_hint: str
        - name: SecurityUserData
          pcf_type: MQCFST
          type_hint: str
        - name: SendExit
          pcf_type: MQCFSL
          type_hint: str
        - name: SendUserData
          pcf_type: MQCFSL
          type_hint: str
        - name: SeqNumberWrap
          pcf_type: MQCFIN
          type_hint: int
        - name: SharingConversations
          pcf_type: MQCFIN
          type_hint: int
        - name: ShortRetryCount
          pcf_type: MQCFIN
          type_hint: int
        - name: ShortRetryInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: SPLProtection
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSPL_PASSTHRU
            - MQSPL_REMOVE
            - MQSPL_AS_POLICY
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
        - name: TemporaryModelQName
          pcf_type: MQCFST
          type_hint: str
        - name: TemporaryQPrefix
          pcf_type: MQCFST
          type_hint: str
        - name: TpName
          pcf_type: MQCFST
          type_hint: str
        - name: TPRoot
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
        - name: UseCltId
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQUCI_NO
            - MQUCI_YES
        - name: UseDLQ
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQUSEDLQ_NO
            - MQUSEDLQ_YES
        - name: UserIdentifier
          pcf_type: MQCFST
          type_hint: str
        - name: XmitQName
          pcf_type: MQCFST
          type_hint: str
      response_parameters:
        []
    notes:
      - change-channel-excludes-copy-only-parameters
  - mqsc:
      name: DEFINE CHANNEL (SDR)
      href: SSFKSJ_9.4.0/refadmin/q085520_.html
      positional_parameters:
        - (channel-name)
      input_parameters:
        - BATCHHB
        - BATCHINT
        - BATCHLIM
        - BATCHSZ
        - CERTLABL
        - CHLTYPE
        - CMDSCOPE
        - COMPHDR
        - COMPMSG
        - CONNAME
        - CONVERT
        - DEFCDISP
        - DESCR
        - DISCINT
        - HBINT
        - KAINT
        - LIKE
        - LOCLADDR
        - LONGRTY
        - LONGTMR
        - MAXMSGL
        - MCANAME
        - MCATYPE
        - MODENAME
        - MONCHL
        - MSGDATA
        - MSGEXIT
        - NPMSPEED
        - PASSWORD
        - PROPCTL
        - QSGDISP
        - RCVDATA
        - RCVEXIT
        - REPLACE
        - NOREPLACE
        - SCYDATA
        - SCYEXIT
        - SENDDATA
        - SENDEXIT
        - SEQWRAP
        - SHORTRTY
        - SHORTTMR
        - SPLPROT
        - SSLCIPH
        - SSLPEER
        - STATCHL
        - TPNAME
        - TRPTYPE
        - USEDLQ
        - USERID
        - XMITQ
      output_parameters:
        []
      section_sources:
        'Parameter descriptions for DEFINE CHANNEL':
          - BATCHHB
          - BATCHINT
          - BATCHLIM
          - BATCHSZ
          - CERTLABL
          - CHLTYPE
          - CMDSCOPE
          - COMPHDR
          - COMPMSG
          - CONNAME
          - CONVERT
          - DEFCDISP
          - DESCR
          - DISCINT
          - HBINT
          - KAINT
          - LIKE
          - LOCLADDR
          - LONGRTY
          - LONGTMR
          - MAXMSGL
          - MCANAME
          - MCATYPE
          - MODENAME
          - MONCHL
          - MSGDATA
          - MSGEXIT
          - NPMSPEED
          - PASSWORD
          - PROPCTL
          - QSGDISP
          - RCVDATA
          - RCVEXIT
          - REPLACE
          - NOREPLACE
          - SCYDATA
          - SCYEXIT
          - SENDDATA
          - SENDEXIT
          - SEQWRAP
          - SHORTRTY
          - SHORTTMR
          - SPLPROT
          - SSLCIPH
          - SSLPEER
          - STATCHL
          - TPNAME
          - TRPTYPE
          - USEDLQ
          - USERID
          - XMITQ
    pcf:
      command: MQCMD_CREATE_CHANNEL
      request_href: SSFKSJ_9.4.0/refadmin/q086930_.html
      response_href: null
      request_parameters:
        - name: ChannelName
          pcf_type: MQCFST
          type_hint: str
        - name: ChannelType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHT_SENDER
            - MQCHT_SERVER
            - MQCHT_RECEIVER
            - MQCHT_REQUESTER
            - MQCHT_SVRCONN
            - MQCHT_CLNTCONN
            - MQCHT_CLUSRCVR
            - MQCHT_CLUSSDR
            - MQCHT_AMQP
        - name: AMQPKeepAlive
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchHeartbeat
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchDataLimit
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchSize
          pcf_type: MQCFIN
          type_hint: int
        - name: CertificateLabel
          pcf_type: MQCFST
          type_hint: str
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
        - name: ChannelStatistics
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_OFF
            - MQMON_Q_MGR
            - MQMON_LOW
            - MQMON_MEDIUM
            - MQMON_HIGH
        - name: ClientChannelWeight
          pcf_type: MQCFIN
          type_hint: int
        - name: ClusterName
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterNamelist
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
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: ConnectionAffinity
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCAFTY_PREFERRED
            - MQCAFTY_NONE
        - name: ConnectionName
          pcf_type: MQCFST
          type_hint: str
        - name: DataConversion
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCDC_NO_SENDER_CONVERSION
            - MQCDC_SENDER_CONVERSION
        - name: DefaultChannelDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHLD_PRIVATE
            - MQCHLD_FIXSHARED
            - MQCHLD_SHARED
        - name: DefReconnect
          pcf_type: MQCFIN
          type_hint: int
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
          enum_values:
            - MQKAI_AUTO
        - name: LocalAddress
          pcf_type: MQCFST
          type_hint: str
        - name: LongRetryCount
          pcf_type: MQCFIN
          type_hint: int
        - name: LongRetryInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxInstances
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxInstancesPerClient
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
            - MQCOMPRESS_ANY
        - name: ModeName
          pcf_type: MQCFST
          type_hint: str
        - name: MsgExit
          pcf_type: MQCFSL
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
          pcf_type: MQCFSL
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
        - name: Port
          pcf_type: MQCFIN
          type_hint: int
        - name: PropertyControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPROP_COMPATIBILITY
            - MQPROP_NONE
            - MQPROP_ALL
        - name: PutAuthority
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPA_DEFAULT
            - MQPA_CONTEXT
            - MQPA_ALTERNATE_OR_MCA
            - MQPA_ONLY_MCA
        - name: QMgrName
          pcf_type: MQCFST
          type_hint: str
        - name: QSGDisposition
          pcf_type: MQCFIN
          type_hint: int
        - name: ReceiveExit
          pcf_type: MQCFSL
          type_hint: str
        - name: ReceiveUserData
          pcf_type: MQCFSL
          type_hint: str
        - name: Replace
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQRP_YES
            - MQRP_NO
        - name: SecurityExit
          pcf_type: MQCFST
          type_hint: str
        - name: SecurityUserData
          pcf_type: MQCFST
          type_hint: str
        - name: SendExit
          pcf_type: MQCFSL
          type_hint: str
        - name: SendUserData
          pcf_type: MQCFSL
          type_hint: str
        - name: SeqNumberWrap
          pcf_type: MQCFIN
          type_hint: int
        - name: SharingConversations
          pcf_type: MQCFIN
          type_hint: int
        - name: ShortRetryCount
          pcf_type: MQCFIN
          type_hint: int
        - name: ShortRetryInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: SPLProtection
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSPL_PASSTHRU
            - MQSPL_REMOVE
            - MQSPL_AS_POLICY
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
        - name: TemporaryModelQName
          pcf_type: MQCFST
          type_hint: str
        - name: TemporaryQPrefix
          pcf_type: MQCFST
          type_hint: str
        - name: TpName
          pcf_type: MQCFST
          type_hint: str
        - name: TPRoot
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
        - name: UseCltId
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQUCI_NO
            - MQUCI_YES
        - name: UseDLQ
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQUSEDLQ_NO
            - MQUSEDLQ_YES
        - name: UserIdentifier
          pcf_type: MQCFST
          type_hint: str
        - name: XmitQName
          pcf_type: MQCFST
          type_hint: str
      response_parameters:
        []
    notes:
      - create-channel-excludes-copy-only-parameters
  - mqsc:
      name: DEFINE CHANNEL (SVR)
      href: SSFKSJ_9.4.0/refadmin/q085520_.html
      positional_parameters:
        - (channel-name)
      input_parameters:
        - BATCHHB
        - BATCHINT
        - BATCHLIM
        - BATCHSZ
        - CERTLABL
        - CHLTYPE
        - CMDSCOPE
        - COMPHDR
        - COMPMSG
        - CONNAME
        - CONVERT
        - DEFCDISP
        - DESCR
        - DISCINT
        - HBINT
        - KAINT
        - LIKE
        - LOCLADDR
        - LONGRTY
        - LONGTMR
        - MAXMSGL
        - MCANAME
        - MCATYPE
        - MODENAME
        - MONCHL
        - MSGDATA
        - MSGEXIT
        - NPMSPEED
        - PASSWORD
        - PROPCTL
        - QSGDISP
        - RCVDATA
        - RCVEXIT
        - REPLACE
        - NOREPLACE
        - SCYDATA
        - SCYEXIT
        - SENDDATA
        - SENDEXIT
        - SEQWRAP
        - SHORTRTY
        - SHORTTMR
        - SPLPROT
        - SSLCAUTH
        - SSLCIPH
        - SSLPEER
        - STATCHL
        - TPNAME
        - TRPTYPE
        - USEDLQ
        - USERID
        - XMITQ
      output_parameters:
        []
      section_sources:
        'Parameter descriptions for DEFINE CHANNEL':
          - BATCHHB
          - BATCHINT
          - BATCHLIM
          - BATCHSZ
          - CERTLABL
          - CHLTYPE
          - CMDSCOPE
          - COMPHDR
          - COMPMSG
          - CONNAME
          - CONVERT
          - DEFCDISP
          - DESCR
          - DISCINT
          - HBINT
          - KAINT
          - LIKE
          - LOCLADDR
          - LONGRTY
          - LONGTMR
          - MAXMSGL
          - MCANAME
          - MCATYPE
          - MODENAME
          - MONCHL
          - MSGDATA
          - MSGEXIT
          - NPMSPEED
          - PASSWORD
          - PROPCTL
          - QSGDISP
          - RCVDATA
          - RCVEXIT
          - REPLACE
          - NOREPLACE
          - SCYDATA
          - SCYEXIT
          - SENDDATA
          - SENDEXIT
          - SEQWRAP
          - SHORTRTY
          - SHORTTMR
          - SPLPROT
          - SSLCAUTH
          - SSLCIPH
          - SSLPEER
          - STATCHL
          - TPNAME
          - TRPTYPE
          - USEDLQ
          - USERID
          - XMITQ
    pcf:
      command: MQCMD_CREATE_CHANNEL
      request_href: SSFKSJ_9.4.0/refadmin/q086930_.html
      response_href: null
      request_parameters:
        - name: ChannelName
          pcf_type: MQCFST
          type_hint: str
        - name: ChannelType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHT_SENDER
            - MQCHT_SERVER
            - MQCHT_RECEIVER
            - MQCHT_REQUESTER
            - MQCHT_SVRCONN
            - MQCHT_CLNTCONN
            - MQCHT_CLUSRCVR
            - MQCHT_CLUSSDR
            - MQCHT_AMQP
        - name: AMQPKeepAlive
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchHeartbeat
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchDataLimit
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchSize
          pcf_type: MQCFIN
          type_hint: int
        - name: CertificateLabel
          pcf_type: MQCFST
          type_hint: str
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
        - name: ChannelStatistics
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_OFF
            - MQMON_Q_MGR
            - MQMON_LOW
            - MQMON_MEDIUM
            - MQMON_HIGH
        - name: ClientChannelWeight
          pcf_type: MQCFIN
          type_hint: int
        - name: ClusterName
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterNamelist
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
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: ConnectionAffinity
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCAFTY_PREFERRED
            - MQCAFTY_NONE
        - name: ConnectionName
          pcf_type: MQCFST
          type_hint: str
        - name: DataConversion
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCDC_NO_SENDER_CONVERSION
            - MQCDC_SENDER_CONVERSION
        - name: DefaultChannelDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHLD_PRIVATE
            - MQCHLD_FIXSHARED
            - MQCHLD_SHARED
        - name: DefReconnect
          pcf_type: MQCFIN
          type_hint: int
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
          enum_values:
            - MQKAI_AUTO
        - name: LocalAddress
          pcf_type: MQCFST
          type_hint: str
        - name: LongRetryCount
          pcf_type: MQCFIN
          type_hint: int
        - name: LongRetryInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxInstances
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxInstancesPerClient
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
            - MQCOMPRESS_ANY
        - name: ModeName
          pcf_type: MQCFST
          type_hint: str
        - name: MsgExit
          pcf_type: MQCFSL
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
          pcf_type: MQCFSL
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
        - name: Port
          pcf_type: MQCFIN
          type_hint: int
        - name: PropertyControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPROP_COMPATIBILITY
            - MQPROP_NONE
            - MQPROP_ALL
        - name: PutAuthority
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPA_DEFAULT
            - MQPA_CONTEXT
            - MQPA_ALTERNATE_OR_MCA
            - MQPA_ONLY_MCA
        - name: QMgrName
          pcf_type: MQCFST
          type_hint: str
        - name: QSGDisposition
          pcf_type: MQCFIN
          type_hint: int
        - name: ReceiveExit
          pcf_type: MQCFSL
          type_hint: str
        - name: ReceiveUserData
          pcf_type: MQCFSL
          type_hint: str
        - name: Replace
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQRP_YES
            - MQRP_NO
        - name: SecurityExit
          pcf_type: MQCFST
          type_hint: str
        - name: SecurityUserData
          pcf_type: MQCFST
          type_hint: str
        - name: SendExit
          pcf_type: MQCFSL
          type_hint: str
        - name: SendUserData
          pcf_type: MQCFSL
          type_hint: str
        - name: SeqNumberWrap
          pcf_type: MQCFIN
          type_hint: int
        - name: SharingConversations
          pcf_type: MQCFIN
          type_hint: int
        - name: ShortRetryCount
          pcf_type: MQCFIN
          type_hint: int
        - name: ShortRetryInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: SPLProtection
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSPL_PASSTHRU
            - MQSPL_REMOVE
            - MQSPL_AS_POLICY
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
        - name: TemporaryModelQName
          pcf_type: MQCFST
          type_hint: str
        - name: TemporaryQPrefix
          pcf_type: MQCFST
          type_hint: str
        - name: TpName
          pcf_type: MQCFST
          type_hint: str
        - name: TPRoot
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
        - name: UseCltId
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQUCI_NO
            - MQUCI_YES
        - name: UseDLQ
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQUSEDLQ_NO
            - MQUSEDLQ_YES
        - name: UserIdentifier
          pcf_type: MQCFST
          type_hint: str
        - name: XmitQName
          pcf_type: MQCFST
          type_hint: str
      response_parameters:
        []
    notes:
      - create-channel-excludes-copy-only-parameters
  - mqsc:
      name: DEFINE CHANNEL (RCVR)
      href: SSFKSJ_9.4.0/refadmin/q085520_.html
      positional_parameters:
        - (channel-name)
      input_parameters:
        - BATCHSZ
        - CERTLABL
        - CHLTYPE
        - CMDSCOPE
        - COMPHDR
        - COMPMSG
        - DEFCDISP
        - DESCR
        - HBINT
        - KAINT
        - LIKE
        - MAXMSGL
        - MCAUSER
        - MONCHL
        - MRDATA
        - MREXIT
        - MRRTY
        - MRTMR
        - MSGDATA
        - MSGEXIT
        - NPMSPEED
        - PUTAUT
        - QSGDISP
        - RCVDATA
        - RCVEXIT
        - REPLACE
        - NOREPLACE
        - SCYDATA
        - SCYEXIT
        - SENDDATA
        - SENDEXIT
        - SEQWRAP
        - SPLPROT
        - SSLCAUTH
        - SSLCIPH
        - SSLPEER
        - STATCHL
        - TRPTYPE
        - USEDLQ
      output_parameters:
        []
      section_sources:
        'Parameter descriptions for DEFINE CHANNEL':
          - BATCHSZ
          - CERTLABL
          - CHLTYPE
          - CMDSCOPE
          - COMPHDR
          - COMPMSG
          - DEFCDISP
          - DESCR
          - HBINT
          - KAINT
          - LIKE
          - MAXMSGL
          - MCAUSER
          - MONCHL
          - MRDATA
          - MREXIT
          - MRRTY
          - MRTMR
          - MSGDATA
          - MSGEXIT
          - NPMSPEED
          - PUTAUT
          - QSGDISP
          - RCVDATA
          - RCVEXIT
          - REPLACE
          - NOREPLACE
          - SCYDATA
          - SCYEXIT
          - SENDDATA
          - SENDEXIT
          - SEQWRAP
          - SPLPROT
          - SSLCAUTH
          - SSLCIPH
          - SSLPEER
          - STATCHL
          - TRPTYPE
          - USEDLQ
    pcf:
      command: MQCMD_CREATE_CHANNEL
      request_href: SSFKSJ_9.4.0/refadmin/q086930_.html
      response_href: null
      request_parameters:
        - name: ChannelName
          pcf_type: MQCFST
          type_hint: str
        - name: ChannelType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHT_SENDER
            - MQCHT_SERVER
            - MQCHT_RECEIVER
            - MQCHT_REQUESTER
            - MQCHT_SVRCONN
            - MQCHT_CLNTCONN
            - MQCHT_CLUSRCVR
            - MQCHT_CLUSSDR
            - MQCHT_AMQP
        - name: AMQPKeepAlive
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchHeartbeat
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchDataLimit
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchSize
          pcf_type: MQCFIN
          type_hint: int
        - name: CertificateLabel
          pcf_type: MQCFST
          type_hint: str
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
        - name: ChannelStatistics
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_OFF
            - MQMON_Q_MGR
            - MQMON_LOW
            - MQMON_MEDIUM
            - MQMON_HIGH
        - name: ClientChannelWeight
          pcf_type: MQCFIN
          type_hint: int
        - name: ClusterName
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterNamelist
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
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: ConnectionAffinity
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCAFTY_PREFERRED
            - MQCAFTY_NONE
        - name: ConnectionName
          pcf_type: MQCFST
          type_hint: str
        - name: DataConversion
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCDC_NO_SENDER_CONVERSION
            - MQCDC_SENDER_CONVERSION
        - name: DefaultChannelDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHLD_PRIVATE
            - MQCHLD_FIXSHARED
            - MQCHLD_SHARED
        - name: DefReconnect
          pcf_type: MQCFIN
          type_hint: int
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
          enum_values:
            - MQKAI_AUTO
        - name: LocalAddress
          pcf_type: MQCFST
          type_hint: str
        - name: LongRetryCount
          pcf_type: MQCFIN
          type_hint: int
        - name: LongRetryInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxInstances
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxInstancesPerClient
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
            - MQCOMPRESS_ANY
        - name: ModeName
          pcf_type: MQCFST
          type_hint: str
        - name: MsgExit
          pcf_type: MQCFSL
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
          pcf_type: MQCFSL
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
        - name: Port
          pcf_type: MQCFIN
          type_hint: int
        - name: PropertyControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPROP_COMPATIBILITY
            - MQPROP_NONE
            - MQPROP_ALL
        - name: PutAuthority
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPA_DEFAULT
            - MQPA_CONTEXT
            - MQPA_ALTERNATE_OR_MCA
            - MQPA_ONLY_MCA
        - name: QMgrName
          pcf_type: MQCFST
          type_hint: str
        - name: QSGDisposition
          pcf_type: MQCFIN
          type_hint: int
        - name: ReceiveExit
          pcf_type: MQCFSL
          type_hint: str
        - name: ReceiveUserData
          pcf_type: MQCFSL
          type_hint: str
        - name: Replace
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQRP_YES
            - MQRP_NO
        - name: SecurityExit
          pcf_type: MQCFST
          type_hint: str
        - name: SecurityUserData
          pcf_type: MQCFST
          type_hint: str
        - name: SendExit
          pcf_type: MQCFSL
          type_hint: str
        - name: SendUserData
          pcf_type: MQCFSL
          type_hint: str
        - name: SeqNumberWrap
          pcf_type: MQCFIN
          type_hint: int
        - name: SharingConversations
          pcf_type: MQCFIN
          type_hint: int
        - name: ShortRetryCount
          pcf_type: MQCFIN
          type_hint: int
        - name: ShortRetryInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: SPLProtection
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSPL_PASSTHRU
            - MQSPL_REMOVE
            - MQSPL_AS_POLICY
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
        - name: TemporaryModelQName
          pcf_type: MQCFST
          type_hint: str
        - name: TemporaryQPrefix
          pcf_type: MQCFST
          type_hint: str
        - name: TpName
          pcf_type: MQCFST
          type_hint: str
        - name: TPRoot
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
        - name: UseCltId
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQUCI_NO
            - MQUCI_YES
        - name: UseDLQ
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQUSEDLQ_NO
            - MQUSEDLQ_YES
        - name: UserIdentifier
          pcf_type: MQCFST
          type_hint: str
        - name: XmitQName
          pcf_type: MQCFST
          type_hint: str
      response_parameters:
        []
    notes:
      - create-channel-excludes-copy-only-parameters
  - mqsc:
      name: DEFINE CHANNEL (RQSTR)
      href: SSFKSJ_9.4.0/refadmin/q085520_.html
      positional_parameters:
        - (channel-name)
      input_parameters:
        - BATCHSZ
        - CERTLABL
        - CHLTYPE
        - CMDSCOPE
        - COMPHDR
        - COMPMSG
        - CONNAME
        - DEFCDISP
        - DESCR
        - HBINT
        - KAINT
        - LIKE
        - LOCLADDR
        - MAXMSGL
        - MCANAME
        - MCATYPE
        - MCAUSER
        - MODENAME
        - MONCHL
        - MRDATA
        - MREXIT
        - MRRTY
        - MRTMR
        - MSGDATA
        - MSGEXIT
        - NPMSPEED
        - PASSWORD
        - PUTAUT
        - QSGDISP
        - RCVDATA
        - RCVEXIT
        - REPLACE
        - NOREPLACE
        - SCYDATA
        - SCYEXIT
        - SENDDATA
        - SENDEXIT
        - SEQWRAP
        - SPLPROT
        - SSLCAUTH
        - SSLCIPH
        - SSLPEER
        - STATCHL
        - TPNAME
        - TRPTYPE
        - USEDLQ
        - USERID
      output_parameters:
        []
      section_sources:
        'Parameter descriptions for DEFINE CHANNEL':
          - BATCHSZ
          - CERTLABL
          - CHLTYPE
          - CMDSCOPE
          - COMPHDR
          - COMPMSG
          - CONNAME
          - DEFCDISP
          - DESCR
          - HBINT
          - KAINT
          - LIKE
          - LOCLADDR
          - MAXMSGL
          - MCANAME
          - MCATYPE
          - MCAUSER
          - MODENAME
          - MONCHL
          - MRDATA
          - MREXIT
          - MRRTY
          - MRTMR
          - MSGDATA
          - MSGEXIT
          - NPMSPEED
          - PASSWORD
          - PUTAUT
          - QSGDISP
          - RCVDATA
          - RCVEXIT
          - REPLACE
          - NOREPLACE
          - SCYDATA
          - SCYEXIT
          - SENDDATA
          - SENDEXIT
          - SEQWRAP
          - SPLPROT
          - SSLCAUTH
          - SSLCIPH
          - SSLPEER
          - STATCHL
          - TPNAME
          - TRPTYPE
          - USEDLQ
          - USERID
    pcf:
      command: MQCMD_CREATE_CHANNEL
      request_href: SSFKSJ_9.4.0/refadmin/q086930_.html
      response_href: null
      request_parameters:
        - name: ChannelName
          pcf_type: MQCFST
          type_hint: str
        - name: ChannelType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHT_SENDER
            - MQCHT_SERVER
            - MQCHT_RECEIVER
            - MQCHT_REQUESTER
            - MQCHT_SVRCONN
            - MQCHT_CLNTCONN
            - MQCHT_CLUSRCVR
            - MQCHT_CLUSSDR
            - MQCHT_AMQP
        - name: AMQPKeepAlive
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchHeartbeat
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchDataLimit
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchSize
          pcf_type: MQCFIN
          type_hint: int
        - name: CertificateLabel
          pcf_type: MQCFST
          type_hint: str
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
        - name: ChannelStatistics
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_OFF
            - MQMON_Q_MGR
            - MQMON_LOW
            - MQMON_MEDIUM
            - MQMON_HIGH
        - name: ClientChannelWeight
          pcf_type: MQCFIN
          type_hint: int
        - name: ClusterName
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterNamelist
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
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: ConnectionAffinity
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCAFTY_PREFERRED
            - MQCAFTY_NONE
        - name: ConnectionName
          pcf_type: MQCFST
          type_hint: str
        - name: DataConversion
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCDC_NO_SENDER_CONVERSION
            - MQCDC_SENDER_CONVERSION
        - name: DefaultChannelDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHLD_PRIVATE
            - MQCHLD_FIXSHARED
            - MQCHLD_SHARED
        - name: DefReconnect
          pcf_type: MQCFIN
          type_hint: int
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
          enum_values:
            - MQKAI_AUTO
        - name: LocalAddress
          pcf_type: MQCFST
          type_hint: str
        - name: LongRetryCount
          pcf_type: MQCFIN
          type_hint: int
        - name: LongRetryInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxInstances
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxInstancesPerClient
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
            - MQCOMPRESS_ANY
        - name: ModeName
          pcf_type: MQCFST
          type_hint: str
        - name: MsgExit
          pcf_type: MQCFSL
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
          pcf_type: MQCFSL
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
        - name: Port
          pcf_type: MQCFIN
          type_hint: int
        - name: PropertyControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPROP_COMPATIBILITY
            - MQPROP_NONE
            - MQPROP_ALL
        - name: PutAuthority
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPA_DEFAULT
            - MQPA_CONTEXT
            - MQPA_ALTERNATE_OR_MCA
            - MQPA_ONLY_MCA
        - name: QMgrName
          pcf_type: MQCFST
          type_hint: str
        - name: QSGDisposition
          pcf_type: MQCFIN
          type_hint: int
        - name: ReceiveExit
          pcf_type: MQCFSL
          type_hint: str
        - name: ReceiveUserData
          pcf_type: MQCFSL
          type_hint: str
        - name: Replace
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQRP_YES
            - MQRP_NO
        - name: SecurityExit
          pcf_type: MQCFST
          type_hint: str
        - name: SecurityUserData
          pcf_type: MQCFST
          type_hint: str
        - name: SendExit
          pcf_type: MQCFSL
          type_hint: str
        - name: SendUserData
          pcf_type: MQCFSL
          type_hint: str
        - name: SeqNumberWrap
          pcf_type: MQCFIN
          type_hint: int
        - name: SharingConversations
          pcf_type: MQCFIN
          type_hint: int
        - name: ShortRetryCount
          pcf_type: MQCFIN
          type_hint: int
        - name: ShortRetryInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: SPLProtection
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSPL_PASSTHRU
            - MQSPL_REMOVE
            - MQSPL_AS_POLICY
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
        - name: TemporaryModelQName
          pcf_type: MQCFST
          type_hint: str
        - name: TemporaryQPrefix
          pcf_type: MQCFST
          type_hint: str
        - name: TpName
          pcf_type: MQCFST
          type_hint: str
        - name: TPRoot
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
        - name: UseCltId
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQUCI_NO
            - MQUCI_YES
        - name: UseDLQ
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQUSEDLQ_NO
            - MQUSEDLQ_YES
        - name: UserIdentifier
          pcf_type: MQCFST
          type_hint: str
        - name: XmitQName
          pcf_type: MQCFST
          type_hint: str
      response_parameters:
        []
    notes:
      - create-channel-excludes-copy-only-parameters
  - mqsc:
      name: DEFINE CHANNEL (CLNTCONN)
      href: SSFKSJ_9.4.0/refadmin/q085520_.html
      positional_parameters:
        - (channel-name)
      input_parameters:
        - AFFINITY
        - CERTLABL
        - CHLTYPE
        - CLNTWGHT
        - CMDSCOPE
        - COMPHDR
        - COMPMSG
        - CONNAME
        - DEFRECON
        - DESCR
        - HBINT
        - KAINT
        - LIKE
        - LOCLADDR
        - MAXMSGL
        - MODENAME
        - PASSWORD
        - QMNAME
        - QSGDISP
        - RCVDATA
        - RCVEXIT
        - REPLACE
        - NOREPLACE
        - SCYDATA
        - SCYEXIT
        - SENDDATA
        - SENDEXIT
        - SHARECNV
        - SSLCIPH
        - SSLPEER
        - TPNAME
        - TRPTYPE
        - USERID
      output_parameters:
        []
      section_sources:
        'Parameter descriptions for DEFINE CHANNEL':
          - AFFINITY
          - CERTLABL
          - CHLTYPE
          - CLNTWGHT
          - CMDSCOPE
          - COMPHDR
          - COMPMSG
          - CONNAME
          - DEFRECON
          - DESCR
          - HBINT
          - KAINT
          - LIKE
          - LOCLADDR
          - MAXMSGL
          - MODENAME
          - PASSWORD
          - QMNAME
          - QSGDISP
          - RCVDATA
          - RCVEXIT
          - REPLACE
          - NOREPLACE
          - SCYDATA
          - SCYEXIT
          - SENDDATA
          - SENDEXIT
          - SHARECNV
          - SSLCIPH
          - SSLPEER
          - TPNAME
          - TRPTYPE
          - USERID
    pcf:
      command: MQCMD_CREATE_CHANNEL
      request_href: SSFKSJ_9.4.0/refadmin/q086930_.html
      response_href: null
      request_parameters:
        - name: ChannelName
          pcf_type: MQCFST
          type_hint: str
        - name: ChannelType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHT_SENDER
            - MQCHT_SERVER
            - MQCHT_RECEIVER
            - MQCHT_REQUESTER
            - MQCHT_SVRCONN
            - MQCHT_CLNTCONN
            - MQCHT_CLUSRCVR
            - MQCHT_CLUSSDR
            - MQCHT_AMQP
        - name: AMQPKeepAlive
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchHeartbeat
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchDataLimit
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchSize
          pcf_type: MQCFIN
          type_hint: int
        - name: CertificateLabel
          pcf_type: MQCFST
          type_hint: str
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
        - name: ChannelStatistics
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_OFF
            - MQMON_Q_MGR
            - MQMON_LOW
            - MQMON_MEDIUM
            - MQMON_HIGH
        - name: ClientChannelWeight
          pcf_type: MQCFIN
          type_hint: int
        - name: ClusterName
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterNamelist
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
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: ConnectionAffinity
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCAFTY_PREFERRED
            - MQCAFTY_NONE
        - name: ConnectionName
          pcf_type: MQCFST
          type_hint: str
        - name: DataConversion
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCDC_NO_SENDER_CONVERSION
            - MQCDC_SENDER_CONVERSION
        - name: DefaultChannelDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHLD_PRIVATE
            - MQCHLD_FIXSHARED
            - MQCHLD_SHARED
        - name: DefReconnect
          pcf_type: MQCFIN
          type_hint: int
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
          enum_values:
            - MQKAI_AUTO
        - name: LocalAddress
          pcf_type: MQCFST
          type_hint: str
        - name: LongRetryCount
          pcf_type: MQCFIN
          type_hint: int
        - name: LongRetryInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxInstances
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxInstancesPerClient
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
            - MQCOMPRESS_ANY
        - name: ModeName
          pcf_type: MQCFST
          type_hint: str
        - name: MsgExit
          pcf_type: MQCFSL
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
          pcf_type: MQCFSL
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
        - name: Port
          pcf_type: MQCFIN
          type_hint: int
        - name: PropertyControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPROP_COMPATIBILITY
            - MQPROP_NONE
            - MQPROP_ALL
        - name: PutAuthority
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPA_DEFAULT
            - MQPA_CONTEXT
            - MQPA_ALTERNATE_OR_MCA
            - MQPA_ONLY_MCA
        - name: QMgrName
          pcf_type: MQCFST
          type_hint: str
        - name: QSGDisposition
          pcf_type: MQCFIN
          type_hint: int
        - name: ReceiveExit
          pcf_type: MQCFSL
          type_hint: str
        - name: ReceiveUserData
          pcf_type: MQCFSL
          type_hint: str
        - name: Replace
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQRP_YES
            - MQRP_NO
        - name: SecurityExit
          pcf_type: MQCFST
          type_hint: str
        - name: SecurityUserData
          pcf_type: MQCFST
          type_hint: str
        - name: SendExit
          pcf_type: MQCFSL
          type_hint: str
        - name: SendUserData
          pcf_type: MQCFSL
          type_hint: str
        - name: SeqNumberWrap
          pcf_type: MQCFIN
          type_hint: int
        - name: SharingConversations
          pcf_type: MQCFIN
          type_hint: int
        - name: ShortRetryCount
          pcf_type: MQCFIN
          type_hint: int
        - name: ShortRetryInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: SPLProtection
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSPL_PASSTHRU
            - MQSPL_REMOVE
            - MQSPL_AS_POLICY
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
        - name: TemporaryModelQName
          pcf_type: MQCFST
          type_hint: str
        - name: TemporaryQPrefix
          pcf_type: MQCFST
          type_hint: str
        - name: TpName
          pcf_type: MQCFST
          type_hint: str
        - name: TPRoot
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
        - name: UseCltId
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQUCI_NO
            - MQUCI_YES
        - name: UseDLQ
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQUSEDLQ_NO
            - MQUSEDLQ_YES
        - name: UserIdentifier
          pcf_type: MQCFST
          type_hint: str
        - name: XmitQName
          pcf_type: MQCFST
          type_hint: str
      response_parameters:
        []
    notes:
      - create-channel-excludes-copy-only-parameters
  - mqsc:
      name: DEFINE CHANNEL (SVRCONN)
      href: SSFKSJ_9.4.0/refadmin/q085520_.html
      positional_parameters:
        - (channel-name)
      input_parameters:
        - CERTLABL
        - CHLTYPE
        - CMDSCOPE
        - COMPHDR
        - COMPMSG
        - DEFCDISP
        - DESCR
        - DISCINT
        - HBINT
        - KAINT
        - LIKE
        - MAXINST
        - MAXINSTC
        - MAXMSGL
        - MCAUSER
        - MONCHL
        - PUTAUT
        - QSGDISP
        - RCVDATA
        - RCVEXIT
        - REPLACE
        - NOREPLACE
        - SCYDATA
        - SCYEXIT
        - SENDDATA
        - SENDEXIT
        - SHARECNV
        - SSLCAUTH
        - SSLCIPH
        - SSLPEER
        - TPNAME
        - TRPTYPE
      output_parameters:
        []
      section_sources:
        'Parameter descriptions for DEFINE CHANNEL':
          - CERTLABL
          - CHLTYPE
          - CMDSCOPE
          - COMPHDR
          - COMPMSG
          - DEFCDISP
          - DESCR
          - DISCINT
          - HBINT
          - KAINT
          - LIKE
          - MAXINST
          - MAXINSTC
          - MAXMSGL
          - MCAUSER
          - MONCHL
          - PUTAUT
          - QSGDISP
          - RCVDATA
          - RCVEXIT
          - REPLACE
          - NOREPLACE
          - SCYDATA
          - SCYEXIT
          - SENDDATA
          - SENDEXIT
          - SHARECNV
          - SSLCAUTH
          - SSLCIPH
          - SSLPEER
          - TPNAME
          - TRPTYPE
    pcf:
      command: MQCMD_CREATE_CHANNEL
      request_href: SSFKSJ_9.4.0/refadmin/q086930_.html
      response_href: null
      request_parameters:
        - name: ChannelName
          pcf_type: MQCFST
          type_hint: str
        - name: ChannelType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHT_SENDER
            - MQCHT_SERVER
            - MQCHT_RECEIVER
            - MQCHT_REQUESTER
            - MQCHT_SVRCONN
            - MQCHT_CLNTCONN
            - MQCHT_CLUSRCVR
            - MQCHT_CLUSSDR
            - MQCHT_AMQP
        - name: AMQPKeepAlive
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchHeartbeat
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchDataLimit
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchSize
          pcf_type: MQCFIN
          type_hint: int
        - name: CertificateLabel
          pcf_type: MQCFST
          type_hint: str
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
        - name: ChannelStatistics
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_OFF
            - MQMON_Q_MGR
            - MQMON_LOW
            - MQMON_MEDIUM
            - MQMON_HIGH
        - name: ClientChannelWeight
          pcf_type: MQCFIN
          type_hint: int
        - name: ClusterName
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterNamelist
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
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: ConnectionAffinity
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCAFTY_PREFERRED
            - MQCAFTY_NONE
        - name: ConnectionName
          pcf_type: MQCFST
          type_hint: str
        - name: DataConversion
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCDC_NO_SENDER_CONVERSION
            - MQCDC_SENDER_CONVERSION
        - name: DefaultChannelDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHLD_PRIVATE
            - MQCHLD_FIXSHARED
            - MQCHLD_SHARED
        - name: DefReconnect
          pcf_type: MQCFIN
          type_hint: int
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
          enum_values:
            - MQKAI_AUTO
        - name: LocalAddress
          pcf_type: MQCFST
          type_hint: str
        - name: LongRetryCount
          pcf_type: MQCFIN
          type_hint: int
        - name: LongRetryInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxInstances
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxInstancesPerClient
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
            - MQCOMPRESS_ANY
        - name: ModeName
          pcf_type: MQCFST
          type_hint: str
        - name: MsgExit
          pcf_type: MQCFSL
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
          pcf_type: MQCFSL
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
        - name: Port
          pcf_type: MQCFIN
          type_hint: int
        - name: PropertyControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPROP_COMPATIBILITY
            - MQPROP_NONE
            - MQPROP_ALL
        - name: PutAuthority
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPA_DEFAULT
            - MQPA_CONTEXT
            - MQPA_ALTERNATE_OR_MCA
            - MQPA_ONLY_MCA
        - name: QMgrName
          pcf_type: MQCFST
          type_hint: str
        - name: QSGDisposition
          pcf_type: MQCFIN
          type_hint: int
        - name: ReceiveExit
          pcf_type: MQCFSL
          type_hint: str
        - name: ReceiveUserData
          pcf_type: MQCFSL
          type_hint: str
        - name: Replace
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQRP_YES
            - MQRP_NO
        - name: SecurityExit
          pcf_type: MQCFST
          type_hint: str
        - name: SecurityUserData
          pcf_type: MQCFST
          type_hint: str
        - name: SendExit
          pcf_type: MQCFSL
          type_hint: str
        - name: SendUserData
          pcf_type: MQCFSL
          type_hint: str
        - name: SeqNumberWrap
          pcf_type: MQCFIN
          type_hint: int
        - name: SharingConversations
          pcf_type: MQCFIN
          type_hint: int
        - name: ShortRetryCount
          pcf_type: MQCFIN
          type_hint: int
        - name: ShortRetryInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: SPLProtection
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSPL_PASSTHRU
            - MQSPL_REMOVE
            - MQSPL_AS_POLICY
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
        - name: TemporaryModelQName
          pcf_type: MQCFST
          type_hint: str
        - name: TemporaryQPrefix
          pcf_type: MQCFST
          type_hint: str
        - name: TpName
          pcf_type: MQCFST
          type_hint: str
        - name: TPRoot
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
        - name: UseCltId
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQUCI_NO
            - MQUCI_YES
        - name: UseDLQ
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQUSEDLQ_NO
            - MQUSEDLQ_YES
        - name: UserIdentifier
          pcf_type: MQCFST
          type_hint: str
        - name: XmitQName
          pcf_type: MQCFST
          type_hint: str
      response_parameters:
        []
    notes:
      - create-channel-excludes-copy-only-parameters
  - mqsc:
      name: DEFINE CHANNEL (CLUSSDR)
      href: SSFKSJ_9.4.0/refadmin/q085520_.html
      positional_parameters:
        - (channel-name)
      input_parameters:
        - BATCHHB
        - BATCHINT
        - BATCHLIM
        - BATCHSZ
        - CHLTYPE
        - CLUSNL
        - CLUSTER
        - CLWLPRTY
        - CLWLRANK
        - CLWLWGHT
        - CMDSCOPE
        - COMPHDR
        - COMPMSG
        - CONNAME
        - CONVERT
        - DESCR
        - DISCINT
        - HBINT
        - KAINT
        - LIKE
        - LOCLADDR
        - LONGRTY
        - LONGTMR
        - MAXMSGL
        - MCANAME
        - MCATYPE
        - MODENAME
        - MONCHL
        - MSGDATA
        - MSGEXIT
        - NPMSPEED
        - PASSWORD
        - PROPCTL
        - QSGDISP
        - RCVDATA
        - RCVEXIT
        - REPLACE
        - NOREPLACE
        - SCYDATA
        - SCYEXIT
        - SENDDATA
        - SENDEXIT
        - SEQWRAP
        - SHORTRTY
        - SHORTTMR
        - SSLCIPH
        - SSLPEER
        - STATCHL
        - TPNAME
        - TRPTYPE
        - USEDLQ
        - USERID
      output_parameters:
        []
      section_sources:
        'Parameter descriptions for DEFINE CHANNEL':
          - BATCHHB
          - BATCHINT
          - BATCHLIM
          - BATCHSZ
          - CHLTYPE
          - CLUSNL
          - CLUSTER
          - CLWLPRTY
          - CLWLRANK
          - CLWLWGHT
          - CMDSCOPE
          - COMPHDR
          - COMPMSG
          - CONNAME
          - CONVERT
          - DESCR
          - DISCINT
          - HBINT
          - KAINT
          - LIKE
          - LOCLADDR
          - LONGRTY
          - LONGTMR
          - MAXMSGL
          - MCANAME
          - MCATYPE
          - MODENAME
          - MONCHL
          - MSGDATA
          - MSGEXIT
          - NPMSPEED
          - PASSWORD
          - PROPCTL
          - QSGDISP
          - RCVDATA
          - RCVEXIT
          - REPLACE
          - NOREPLACE
          - SCYDATA
          - SCYEXIT
          - SENDDATA
          - SENDEXIT
          - SEQWRAP
          - SHORTRTY
          - SHORTTMR
          - SSLCIPH
          - SSLPEER
          - STATCHL
          - TPNAME
          - TRPTYPE
          - USEDLQ
          - USERID
    pcf:
      command: MQCMD_CREATE_CHANNEL
      request_href: SSFKSJ_9.4.0/refadmin/q086930_.html
      response_href: null
      request_parameters:
        - name: ChannelName
          pcf_type: MQCFST
          type_hint: str
        - name: ChannelType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHT_SENDER
            - MQCHT_SERVER
            - MQCHT_RECEIVER
            - MQCHT_REQUESTER
            - MQCHT_SVRCONN
            - MQCHT_CLNTCONN
            - MQCHT_CLUSRCVR
            - MQCHT_CLUSSDR
            - MQCHT_AMQP
        - name: AMQPKeepAlive
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchHeartbeat
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchDataLimit
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchSize
          pcf_type: MQCFIN
          type_hint: int
        - name: CertificateLabel
          pcf_type: MQCFST
          type_hint: str
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
        - name: ChannelStatistics
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_OFF
            - MQMON_Q_MGR
            - MQMON_LOW
            - MQMON_MEDIUM
            - MQMON_HIGH
        - name: ClientChannelWeight
          pcf_type: MQCFIN
          type_hint: int
        - name: ClusterName
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterNamelist
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
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: ConnectionAffinity
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCAFTY_PREFERRED
            - MQCAFTY_NONE
        - name: ConnectionName
          pcf_type: MQCFST
          type_hint: str
        - name: DataConversion
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCDC_NO_SENDER_CONVERSION
            - MQCDC_SENDER_CONVERSION
        - name: DefaultChannelDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHLD_PRIVATE
            - MQCHLD_FIXSHARED
            - MQCHLD_SHARED
        - name: DefReconnect
          pcf_type: MQCFIN
          type_hint: int
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
          enum_values:
            - MQKAI_AUTO
        - name: LocalAddress
          pcf_type: MQCFST
          type_hint: str
        - name: LongRetryCount
          pcf_type: MQCFIN
          type_hint: int
        - name: LongRetryInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxInstances
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxInstancesPerClient
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
            - MQCOMPRESS_ANY
        - name: ModeName
          pcf_type: MQCFST
          type_hint: str
        - name: MsgExit
          pcf_type: MQCFSL
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
          pcf_type: MQCFSL
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
        - name: Port
          pcf_type: MQCFIN
          type_hint: int
        - name: PropertyControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPROP_COMPATIBILITY
            - MQPROP_NONE
            - MQPROP_ALL
        - name: PutAuthority
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPA_DEFAULT
            - MQPA_CONTEXT
            - MQPA_ALTERNATE_OR_MCA
            - MQPA_ONLY_MCA
        - name: QMgrName
          pcf_type: MQCFST
          type_hint: str
        - name: QSGDisposition
          pcf_type: MQCFIN
          type_hint: int
        - name: ReceiveExit
          pcf_type: MQCFSL
          type_hint: str
        - name: ReceiveUserData
          pcf_type: MQCFSL
          type_hint: str
        - name: Replace
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQRP_YES
            - MQRP_NO
        - name: SecurityExit
          pcf_type: MQCFST
          type_hint: str
        - name: SecurityUserData
          pcf_type: MQCFST
          type_hint: str
        - name: SendExit
          pcf_type: MQCFSL
          type_hint: str
        - name: SendUserData
          pcf_type: MQCFSL
          type_hint: str
        - name: SeqNumberWrap
          pcf_type: MQCFIN
          type_hint: int
        - name: SharingConversations
          pcf_type: MQCFIN
          type_hint: int
        - name: ShortRetryCount
          pcf_type: MQCFIN
          type_hint: int
        - name: ShortRetryInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: SPLProtection
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSPL_PASSTHRU
            - MQSPL_REMOVE
            - MQSPL_AS_POLICY
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
        - name: TemporaryModelQName
          pcf_type: MQCFST
          type_hint: str
        - name: TemporaryQPrefix
          pcf_type: MQCFST
          type_hint: str
        - name: TpName
          pcf_type: MQCFST
          type_hint: str
        - name: TPRoot
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
        - name: UseCltId
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQUCI_NO
            - MQUCI_YES
        - name: UseDLQ
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQUSEDLQ_NO
            - MQUSEDLQ_YES
        - name: UserIdentifier
          pcf_type: MQCFST
          type_hint: str
        - name: XmitQName
          pcf_type: MQCFST
          type_hint: str
      response_parameters:
        []
    notes:
      - create-channel-excludes-copy-only-parameters
  - mqsc:
      name: DEFINE CHANNEL (CLUSRCVR)
      href: SSFKSJ_9.4.0/refadmin/q085520_.html
      positional_parameters:
        - (channel-name)
      input_parameters:
        - BATCHHB
        - BATCHINT
        - BATCHLIM
        - BATCHSZ
        - CERTLABL
        - CHLTYPE
        - CLUSNL
        - CLUSTER
        - CLWLPRTY
        - CLWLRANK
        - CLWLWGHT
        - CMDSCOPE
        - COMPHDR
        - COMPMSG
        - CONNAME
        - CONVERT
        - DESCR
        - DISCINT
        - HBINT
        - KAINT
        - LIKE
        - LOCLADDR
        - LONGRTY
        - LONGTMR
        - MAXMSGL
        - MCANAME
        - MCATYPE
        - MCAUSER
        - MODENAME
        - MONCHL
        - MRDATA
        - MREXIT
        - MRRTY
        - MRTMR
        - MSGDATA
        - MSGEXIT
        - NETPRTY
        - NPMSPEED
        - PROPCTL
        - PUTAUT
        - QSGDISP
        - RCVDATA
        - RCVEXIT
        - REPLACE
        - NOREPLACE
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
        - STATCHL
        - TPNAME
        - TRPTYPE
        - USEDLQ
      output_parameters:
        []
      section_sources:
        'Parameter descriptions for DEFINE CHANNEL':
          - BATCHHB
          - BATCHINT
          - BATCHLIM
          - BATCHSZ
          - CERTLABL
          - CHLTYPE
          - CLUSNL
          - CLUSTER
          - CLWLPRTY
          - CLWLRANK
          - CLWLWGHT
          - CMDSCOPE
          - COMPHDR
          - COMPMSG
          - CONNAME
          - CONVERT
          - DESCR
          - DISCINT
          - HBINT
          - KAINT
          - LIKE
          - LOCLADDR
          - LONGRTY
          - LONGTMR
          - MAXMSGL
          - MCANAME
          - MCATYPE
          - MCAUSER
          - MODENAME
          - MONCHL
          - MRDATA
          - MREXIT
          - MRRTY
          - MRTMR
          - MSGDATA
          - MSGEXIT
          - NETPRTY
          - NPMSPEED
          - PROPCTL
          - PUTAUT
          - QSGDISP
          - RCVDATA
          - RCVEXIT
          - REPLACE
          - NOREPLACE
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
          - STATCHL
          - TPNAME
          - TRPTYPE
          - USEDLQ
    pcf:
      command: MQCMD_CREATE_CHANNEL
      request_href: SSFKSJ_9.4.0/refadmin/q086930_.html
      response_href: null
      request_parameters:
        - name: ChannelName
          pcf_type: MQCFST
          type_hint: str
        - name: ChannelType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHT_SENDER
            - MQCHT_SERVER
            - MQCHT_RECEIVER
            - MQCHT_REQUESTER
            - MQCHT_SVRCONN
            - MQCHT_CLNTCONN
            - MQCHT_CLUSRCVR
            - MQCHT_CLUSSDR
            - MQCHT_AMQP
        - name: AMQPKeepAlive
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchHeartbeat
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchDataLimit
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchSize
          pcf_type: MQCFIN
          type_hint: int
        - name: CertificateLabel
          pcf_type: MQCFST
          type_hint: str
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
        - name: ChannelStatistics
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_OFF
            - MQMON_Q_MGR
            - MQMON_LOW
            - MQMON_MEDIUM
            - MQMON_HIGH
        - name: ClientChannelWeight
          pcf_type: MQCFIN
          type_hint: int
        - name: ClusterName
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterNamelist
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
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: ConnectionAffinity
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCAFTY_PREFERRED
            - MQCAFTY_NONE
        - name: ConnectionName
          pcf_type: MQCFST
          type_hint: str
        - name: DataConversion
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCDC_NO_SENDER_CONVERSION
            - MQCDC_SENDER_CONVERSION
        - name: DefaultChannelDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHLD_PRIVATE
            - MQCHLD_FIXSHARED
            - MQCHLD_SHARED
        - name: DefReconnect
          pcf_type: MQCFIN
          type_hint: int
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
          enum_values:
            - MQKAI_AUTO
        - name: LocalAddress
          pcf_type: MQCFST
          type_hint: str
        - name: LongRetryCount
          pcf_type: MQCFIN
          type_hint: int
        - name: LongRetryInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxInstances
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxInstancesPerClient
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
            - MQCOMPRESS_ANY
        - name: ModeName
          pcf_type: MQCFST
          type_hint: str
        - name: MsgExit
          pcf_type: MQCFSL
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
          pcf_type: MQCFSL
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
        - name: Port
          pcf_type: MQCFIN
          type_hint: int
        - name: PropertyControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPROP_COMPATIBILITY
            - MQPROP_NONE
            - MQPROP_ALL
        - name: PutAuthority
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPA_DEFAULT
            - MQPA_CONTEXT
            - MQPA_ALTERNATE_OR_MCA
            - MQPA_ONLY_MCA
        - name: QMgrName
          pcf_type: MQCFST
          type_hint: str
        - name: QSGDisposition
          pcf_type: MQCFIN
          type_hint: int
        - name: ReceiveExit
          pcf_type: MQCFSL
          type_hint: str
        - name: ReceiveUserData
          pcf_type: MQCFSL
          type_hint: str
        - name: Replace
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQRP_YES
            - MQRP_NO
        - name: SecurityExit
          pcf_type: MQCFST
          type_hint: str
        - name: SecurityUserData
          pcf_type: MQCFST
          type_hint: str
        - name: SendExit
          pcf_type: MQCFSL
          type_hint: str
        - name: SendUserData
          pcf_type: MQCFSL
          type_hint: str
        - name: SeqNumberWrap
          pcf_type: MQCFIN
          type_hint: int
        - name: SharingConversations
          pcf_type: MQCFIN
          type_hint: int
        - name: ShortRetryCount
          pcf_type: MQCFIN
          type_hint: int
        - name: ShortRetryInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: SPLProtection
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSPL_PASSTHRU
            - MQSPL_REMOVE
            - MQSPL_AS_POLICY
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
        - name: TemporaryModelQName
          pcf_type: MQCFST
          type_hint: str
        - name: TemporaryQPrefix
          pcf_type: MQCFST
          type_hint: str
        - name: TpName
          pcf_type: MQCFST
          type_hint: str
        - name: TPRoot
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
        - name: UseCltId
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQUCI_NO
            - MQUCI_YES
        - name: UseDLQ
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQUSEDLQ_NO
            - MQUSEDLQ_YES
        - name: UserIdentifier
          pcf_type: MQCFST
          type_hint: str
        - name: XmitQName
          pcf_type: MQCFST
          type_hint: str
      response_parameters:
        []
    notes:
      - create-channel-excludes-copy-only-parameters
  - mqsc:
      name: DEFINE CHANNEL (AMQP)
      href: SSFKSJ_9.4.0/refadmin/q085520_.html
      positional_parameters:
        - (channel-name)
      input_parameters:
        - AMQPKA
        - CERTLABL
        - CHLTYPE
        - DESCR
        - LOCLADDR
        - MAXINST
        - MAXMSGL
        - MCAUSER
        - PORT
        - SSLCIPH
        - SSLPEER
        - TMPMODEL
        - TMPQPRFX
        - TPROOT
        - USECLTID
      output_parameters:
        []
      section_sources:
        'Parameter descriptions for DEFINE CHANNEL':
          - AMQPKA
          - CERTLABL
          - CHLTYPE
          - DESCR
          - LOCLADDR
          - MAXINST
          - MAXMSGL
          - MCAUSER
          - PORT
          - SSLCIPH
          - SSLPEER
          - TMPMODEL
          - TMPQPRFX
          - TPROOT
          - USECLTID
    pcf:
      command: MQCMD_CREATE_CHANNEL
      request_href: SSFKSJ_9.4.0/refadmin/q086930_.html
      response_href: null
      request_parameters:
        - name: ChannelName
          pcf_type: MQCFST
          type_hint: str
        - name: ChannelType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHT_SENDER
            - MQCHT_SERVER
            - MQCHT_RECEIVER
            - MQCHT_REQUESTER
            - MQCHT_SVRCONN
            - MQCHT_CLNTCONN
            - MQCHT_CLUSRCVR
            - MQCHT_CLUSSDR
            - MQCHT_AMQP
        - name: AMQPKeepAlive
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchHeartbeat
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchDataLimit
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchSize
          pcf_type: MQCFIN
          type_hint: int
        - name: CertificateLabel
          pcf_type: MQCFST
          type_hint: str
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
        - name: ChannelStatistics
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_OFF
            - MQMON_Q_MGR
            - MQMON_LOW
            - MQMON_MEDIUM
            - MQMON_HIGH
        - name: ClientChannelWeight
          pcf_type: MQCFIN
          type_hint: int
        - name: ClusterName
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterNamelist
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
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: ConnectionAffinity
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCAFTY_PREFERRED
            - MQCAFTY_NONE
        - name: ConnectionName
          pcf_type: MQCFST
          type_hint: str
        - name: DataConversion
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCDC_NO_SENDER_CONVERSION
            - MQCDC_SENDER_CONVERSION
        - name: DefaultChannelDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHLD_PRIVATE
            - MQCHLD_FIXSHARED
            - MQCHLD_SHARED
        - name: DefReconnect
          pcf_type: MQCFIN
          type_hint: int
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
          enum_values:
            - MQKAI_AUTO
        - name: LocalAddress
          pcf_type: MQCFST
          type_hint: str
        - name: LongRetryCount
          pcf_type: MQCFIN
          type_hint: int
        - name: LongRetryInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxInstances
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxInstancesPerClient
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
            - MQCOMPRESS_ANY
        - name: ModeName
          pcf_type: MQCFST
          type_hint: str
        - name: MsgExit
          pcf_type: MQCFSL
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
          pcf_type: MQCFSL
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
        - name: Port
          pcf_type: MQCFIN
          type_hint: int
        - name: PropertyControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPROP_COMPATIBILITY
            - MQPROP_NONE
            - MQPROP_ALL
        - name: PutAuthority
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPA_DEFAULT
            - MQPA_CONTEXT
            - MQPA_ALTERNATE_OR_MCA
            - MQPA_ONLY_MCA
        - name: QMgrName
          pcf_type: MQCFST
          type_hint: str
        - name: QSGDisposition
          pcf_type: MQCFIN
          type_hint: int
        - name: ReceiveExit
          pcf_type: MQCFSL
          type_hint: str
        - name: ReceiveUserData
          pcf_type: MQCFSL
          type_hint: str
        - name: Replace
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQRP_YES
            - MQRP_NO
        - name: SecurityExit
          pcf_type: MQCFST
          type_hint: str
        - name: SecurityUserData
          pcf_type: MQCFST
          type_hint: str
        - name: SendExit
          pcf_type: MQCFSL
          type_hint: str
        - name: SendUserData
          pcf_type: MQCFSL
          type_hint: str
        - name: SeqNumberWrap
          pcf_type: MQCFIN
          type_hint: int
        - name: SharingConversations
          pcf_type: MQCFIN
          type_hint: int
        - name: ShortRetryCount
          pcf_type: MQCFIN
          type_hint: int
        - name: ShortRetryInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: SPLProtection
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSPL_PASSTHRU
            - MQSPL_REMOVE
            - MQSPL_AS_POLICY
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
        - name: TemporaryModelQName
          pcf_type: MQCFST
          type_hint: str
        - name: TemporaryQPrefix
          pcf_type: MQCFST
          type_hint: str
        - name: TpName
          pcf_type: MQCFST
          type_hint: str
        - name: TPRoot
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
        - name: UseCltId
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQUCI_NO
            - MQUCI_YES
        - name: UseDLQ
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQUSEDLQ_NO
            - MQUSEDLQ_YES
        - name: UserIdentifier
          pcf_type: MQCFST
          type_hint: str
        - name: XmitQName
          pcf_type: MQCFST
          type_hint: str
      response_parameters:
        []
    notes:
      - create-channel-excludes-copy-only-parameters
  - mqsc:
      name: DELETE CHANNEL
      href: SSFKSJ_9.4.0/refadmin/q085820_.html
      positional_parameters:
        - (channel-name)
      input_parameters:
        - CHLTABLE
        - CMDSCOPE
        - QSGDISP
        - IGNSTATE
      output_parameters:
        []
      section_sources:
        'Parameter descriptions for DELETE CHANNEL':
          - CHLTABLE
          - CMDSCOPE
          - QSGDISP
          - IGNSTATE
    pcf:
      command: MQCMD_DELETE_CHANNEL
      request_href: SSFKSJ_9.4.0/refadmin/q087120_.html
      response_href: SSFKSJ_9.4.0/refadmin/q087130_.html
      request_parameters:
        - name: ChannelName
          pcf_type: MQCFST
          type_hint: str
        - name: ChannelType
          pcf_type: MQCFIN
          type_hint: int
        - name: ChannelTable
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHTAB_Q_MGR
            - MQCHTAB_CLNTCONN
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
      name: DISPLAY CHANNEL (SDR)
      href: SSFKSJ_9.4.0/refadmin/q086040_.html
      positional_parameters:
        - (generic-channel-name)
      input_parameters:
        - WHERE
        - ALL
        - CMDSCOPE
        - QSGDISP
        - TYPE
      output_parameters:
        - ALTDATE
        - ALTTIME
        - BATCHHB
        - BATCHINT
        - BATCHLIM
        - BATCHSZ
        - CERTLABL
        - CHLTYPE
        - COMPHDR
        - COMPMSG
        - CONNAME
        - CONVERT
        - DEFCDISP
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
        - MONCHL
        - MSGDATA
        - MSGEXIT
        - NPMSPEED
        - PASSWORD
        - PROPCTL
        - RESETSEQ
        - RCVDATA
        - RCVEXIT
        - SCYDATA
        - SCYEXIT
        - SENDDATA
        - SENDEXIT
        - SEQWRAP
        - SHORTRTY
        - SHORTTMR
        - SPLPROT
        - SSLCIPH
        - SSLPEER
        - STATCHL
        - TPNAME
        - TRPTYPE
        - USEDLQ
        - USERID
        - XMITQ
      section_sources:
        'Parameter descriptions for DISPLAY CHANNEL':
          - WHERE
          - ALL
          - CMDSCOPE
          - QSGDISP
          - TYPE
        'Requested parameters':
          - ALTDATE
          - ALTTIME
          - BATCHHB
          - BATCHINT
          - BATCHLIM
          - BATCHSZ
          - CERTLABL
          - CHLTYPE
          - COMPHDR
          - COMPMSG
          - CONNAME
          - CONVERT
          - DEFCDISP
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
          - MONCHL
          - MSGDATA
          - MSGEXIT
          - NPMSPEED
          - PASSWORD
          - PROPCTL
          - RESETSEQ
          - RCVDATA
          - RCVEXIT
          - SCYDATA
          - SCYEXIT
          - SENDDATA
          - SENDEXIT
          - SEQWRAP
          - SHORTRTY
          - SHORTTMR
          - SPLPROT
          - SSLCIPH
          - SSLPEER
          - STATCHL
          - TPNAME
          - TRPTYPE
          - USEDLQ
          - USERID
          - XMITQ
    pcf:
      command: MQCMD_INQUIRE_CHANNEL
      request_href: SSFKSJ_9.4.0/refadmin/q087410_.html
      response_href: SSFKSJ_9.4.0/refadmin/q087430_.html
      request_parameters:
        - name: ChannelName
          pcf_type: MQCFST
          type_hint: str
        - name: ChannelAttrs
          pcf_type: MQCFIL
          type_hint: int
          enum_values:
            - MQIACF_ALL
        - name: ChannelType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHT_SENDER
            - MQCHT_SERVER
            - MQCHT_RECEIVER
            - MQCHT_REQUESTER
            - MQCHT_SVRCONN
            - MQCHT_CLNTCONN
            - MQCHT_CLUSRCVR
            - MQCHT_CLUSSDR
            - MQCHT_AMQP
            - MQCHT_MQTT
            - MQCHT_ALL
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
      response_parameters:
        - name: AlterationDate
          pcf_type: MQCFST
          type_hint: str
        - name: AlterationTime
          pcf_type: MQCFST
          type_hint: str
        - name: BatchDataLimit
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchHeartbeat
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchSize
          pcf_type: MQCFIN
          type_hint: int
        - name: Certificatelabel
          pcf_type: MQCFST
          type_hint: str
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
        - name: ChannelStatistics
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_OFF
            - MQMON_Q_MGR
            - MQMON_LOW
            - MQMON_MEDIUM
            - MQMON_HIGH
        - name: ChannelType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHT_SENDER
            - MQCHT_SERVER
            - MQCHT_RECEIVER
            - MQCHT_REQUESTER
            - MQCHT_SVRCONN
            - MQCHT_CLNTCONN
            - MQCHT_CLUSRCVR
            - MQCHT_CLUSSDR
            - MQCHT_MQTT
        - name: ClientChannelWeight
          pcf_type: MQCFIN
          type_hint: int
        - name: ClientIdentifier
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterName
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterNamelist
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
        - name: ConnectionAffinity
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCAFTY_PREFERRED
            - MQCAFTY_NONE
        - name: ConnectionName
          pcf_type: MQCFST
          type_hint: str
        - name: DataConversion
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCDC_NO_SENDER_CONVERSION
            - MQCDC_SENDER_CONVERSION
        - name: DefaultChannelDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHLD_PRIVATE
            - MQCHLD_FIXSHARED
            - MQCHLD_SHARED
        - name: DiscInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: DefReconnect
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
        - name: InDoubtInbound
          pcf_type: MQCFIN
          type_hint: int
        - name: InDoubtOutbound
          pcf_type: MQCFIN
          type_hint: int
        - name: KeepAliveInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: LastMsgTime
          pcf_type: MQCFST
          type_hint: str
        - name: LocalAddress
          pcf_type: MQCFST
          type_hint: str
        - name: LongRetryCount
          pcf_type: MQCFIN
          type_hint: int
        - name: LongRetryInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxInstances
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxInstancesPerClient
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
            - MQCOMPRESS_ANY
        - name: ModeName
          pcf_type: MQCFST
          type_hint: str
        - name: MsgExit
          pcf_type: MQCFST
          type_hint: str
        - name: MsgsReceived
          pcf_type: MQCFIN64
          type_hint: null
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
        - name: MsgsSent
          pcf_type: MQCFIN64
          type_hint: null
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
        - name: PropertyControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPROP_COMPATIBILITY
            - MQPROP_NONE
            - MQPROP_ALL
        - name: PutAuthority
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPA_DEFAULT
            - MQPA_CONTEXT
        - name: QMgrName
          pcf_type: MQCFST
          type_hint: str
        - name: QSGDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSGD_COPY
            - MQQSGD_GROUP
            - MQQSGD_Q_MGR
        - name: ReceiveExit
          pcf_type: MQCFST
          type_hint: str
        - name: ReceiveUserData
          pcf_type: MQCFST
          type_hint: str
        - name: ResetSeq
          pcf_type: MQCFIN
          type_hint: int
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
        - name: SharingConversations
          pcf_type: MQCFIN
          type_hint: int
        - name: ShortRetryCount
          pcf_type: MQCFIN
          type_hint: int
        - name: ShortRetryInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: SPLProtection
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSPL_PASSTHRU
            - MQSPL_REMOVE
            - MQSPL_AS_POLICY
        - name: SSLCipherSpec
          pcf_type: MQCFST
          type_hint: str
        - name: SSLCipherSuite
          pcf_type: MQCFST
          type_hint: str
        - name: SSLClientAuth
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSCA_REQUIRED
            - MQSCA_OPTIONAL
            - MQSCA_NEVER_REQUIRED
        - name: SSLPeerName
          pcf_type: MQCFST
          type_hint: str
        - name: TpName
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
          enum_values:
            - MQUSEDLQ_NO
            - MQUSEDLQ_YES
        - name: UserIdentifier
          pcf_type: MQCFST
          type_hint: str
        - name: XmitQName
          pcf_type: MQCFST
          type_hint: str
    notes:
      - display-channel-chltype-synonym-on-multiplatforms
  - mqsc:
      name: DISPLAY CHANNEL (SVR)
      href: SSFKSJ_9.4.0/refadmin/q086040_.html
      positional_parameters:
        - (generic-channel-name)
      input_parameters:
        - WHERE
        - ALL
        - CMDSCOPE
        - QSGDISP
        - TYPE
      output_parameters:
        - ALTDATE
        - ALTTIME
        - AUTOSTART
        - BATCHHB
        - BATCHINT
        - BATCHLIM
        - BATCHSZ
        - CERTLABL
        - CHLTYPE
        - COMPHDR
        - COMPMSG
        - CONNAME
        - CONVERT
        - DEFCDISP
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
        - MONCHL
        - MSGDATA
        - MSGEXIT
        - NPMSPEED
        - PASSWORD
        - PROPCTL
        - RESETSEQ
        - RCVDATA
        - RCVEXIT
        - SCYDATA
        - SCYEXIT
        - SENDDATA
        - SENDEXIT
        - SEQWRAP
        - SHORTRTY
        - SHORTTMR
        - SPLPROT
        - SSLCAUTH
        - SSLCIPH
        - SSLPEER
        - STATCHL
        - TPNAME
        - TRPTYPE
        - USEDLQ
        - USERID
        - XMITQ
      section_sources:
        'Parameter descriptions for DISPLAY CHANNEL':
          - WHERE
          - ALL
          - CMDSCOPE
          - QSGDISP
          - TYPE
        'Requested parameters':
          - ALTDATE
          - ALTTIME
          - AUTOSTART
          - BATCHHB
          - BATCHINT
          - BATCHLIM
          - BATCHSZ
          - CERTLABL
          - CHLTYPE
          - COMPHDR
          - COMPMSG
          - CONNAME
          - CONVERT
          - DEFCDISP
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
          - MONCHL
          - MSGDATA
          - MSGEXIT
          - NPMSPEED
          - PASSWORD
          - PROPCTL
          - RESETSEQ
          - RCVDATA
          - RCVEXIT
          - SCYDATA
          - SCYEXIT
          - SENDDATA
          - SENDEXIT
          - SEQWRAP
          - SHORTRTY
          - SHORTTMR
          - SPLPROT
          - SSLCAUTH
          - SSLCIPH
          - SSLPEER
          - STATCHL
          - TPNAME
          - TRPTYPE
          - USEDLQ
          - USERID
          - XMITQ
    pcf:
      command: MQCMD_INQUIRE_CHANNEL
      request_href: SSFKSJ_9.4.0/refadmin/q087410_.html
      response_href: SSFKSJ_9.4.0/refadmin/q087430_.html
      request_parameters:
        - name: ChannelName
          pcf_type: MQCFST
          type_hint: str
        - name: ChannelAttrs
          pcf_type: MQCFIL
          type_hint: int
          enum_values:
            - MQIACF_ALL
        - name: ChannelType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHT_SENDER
            - MQCHT_SERVER
            - MQCHT_RECEIVER
            - MQCHT_REQUESTER
            - MQCHT_SVRCONN
            - MQCHT_CLNTCONN
            - MQCHT_CLUSRCVR
            - MQCHT_CLUSSDR
            - MQCHT_AMQP
            - MQCHT_MQTT
            - MQCHT_ALL
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
      response_parameters:
        - name: AlterationDate
          pcf_type: MQCFST
          type_hint: str
        - name: AlterationTime
          pcf_type: MQCFST
          type_hint: str
        - name: BatchDataLimit
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchHeartbeat
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchSize
          pcf_type: MQCFIN
          type_hint: int
        - name: Certificatelabel
          pcf_type: MQCFST
          type_hint: str
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
        - name: ChannelStatistics
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_OFF
            - MQMON_Q_MGR
            - MQMON_LOW
            - MQMON_MEDIUM
            - MQMON_HIGH
        - name: ChannelType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHT_SENDER
            - MQCHT_SERVER
            - MQCHT_RECEIVER
            - MQCHT_REQUESTER
            - MQCHT_SVRCONN
            - MQCHT_CLNTCONN
            - MQCHT_CLUSRCVR
            - MQCHT_CLUSSDR
            - MQCHT_MQTT
        - name: ClientChannelWeight
          pcf_type: MQCFIN
          type_hint: int
        - name: ClientIdentifier
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterName
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterNamelist
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
        - name: ConnectionAffinity
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCAFTY_PREFERRED
            - MQCAFTY_NONE
        - name: ConnectionName
          pcf_type: MQCFST
          type_hint: str
        - name: DataConversion
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCDC_NO_SENDER_CONVERSION
            - MQCDC_SENDER_CONVERSION
        - name: DefaultChannelDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHLD_PRIVATE
            - MQCHLD_FIXSHARED
            - MQCHLD_SHARED
        - name: DiscInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: DefReconnect
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
        - name: InDoubtInbound
          pcf_type: MQCFIN
          type_hint: int
        - name: InDoubtOutbound
          pcf_type: MQCFIN
          type_hint: int
        - name: KeepAliveInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: LastMsgTime
          pcf_type: MQCFST
          type_hint: str
        - name: LocalAddress
          pcf_type: MQCFST
          type_hint: str
        - name: LongRetryCount
          pcf_type: MQCFIN
          type_hint: int
        - name: LongRetryInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxInstances
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxInstancesPerClient
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
            - MQCOMPRESS_ANY
        - name: ModeName
          pcf_type: MQCFST
          type_hint: str
        - name: MsgExit
          pcf_type: MQCFST
          type_hint: str
        - name: MsgsReceived
          pcf_type: MQCFIN64
          type_hint: null
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
        - name: MsgsSent
          pcf_type: MQCFIN64
          type_hint: null
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
        - name: PropertyControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPROP_COMPATIBILITY
            - MQPROP_NONE
            - MQPROP_ALL
        - name: PutAuthority
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPA_DEFAULT
            - MQPA_CONTEXT
        - name: QMgrName
          pcf_type: MQCFST
          type_hint: str
        - name: QSGDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSGD_COPY
            - MQQSGD_GROUP
            - MQQSGD_Q_MGR
        - name: ReceiveExit
          pcf_type: MQCFST
          type_hint: str
        - name: ReceiveUserData
          pcf_type: MQCFST
          type_hint: str
        - name: ResetSeq
          pcf_type: MQCFIN
          type_hint: int
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
        - name: SharingConversations
          pcf_type: MQCFIN
          type_hint: int
        - name: ShortRetryCount
          pcf_type: MQCFIN
          type_hint: int
        - name: ShortRetryInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: SPLProtection
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSPL_PASSTHRU
            - MQSPL_REMOVE
            - MQSPL_AS_POLICY
        - name: SSLCipherSpec
          pcf_type: MQCFST
          type_hint: str
        - name: SSLCipherSuite
          pcf_type: MQCFST
          type_hint: str
        - name: SSLClientAuth
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSCA_REQUIRED
            - MQSCA_OPTIONAL
            - MQSCA_NEVER_REQUIRED
        - name: SSLPeerName
          pcf_type: MQCFST
          type_hint: str
        - name: TpName
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
          enum_values:
            - MQUSEDLQ_NO
            - MQUSEDLQ_YES
        - name: UserIdentifier
          pcf_type: MQCFST
          type_hint: str
        - name: XmitQName
          pcf_type: MQCFST
          type_hint: str
    notes:
      - display-channel-chltype-synonym-on-multiplatforms
  - mqsc:
      name: DISPLAY CHANNEL (RCVR)
      href: SSFKSJ_9.4.0/refadmin/q086040_.html
      positional_parameters:
        - (generic-channel-name)
      input_parameters:
        - WHERE
        - ALL
        - CMDSCOPE
        - QSGDISP
        - TYPE
      output_parameters:
        - ALTDATE
        - ALTTIME
        - AUTOSTART
        - BATCHSZ
        - CERTLABL
        - CHLTYPE
        - COMPHDR
        - COMPMSG
        - DEFCDISP
        - DESCR
        - HBINT
        - KAINT
        - MAXMSGL
        - MCAUSER
        - MONCHL
        - MRDATA
        - MREXIT
        - MRRTY
        - MRTMR
        - MSGDATA
        - MSGEXIT
        - NPMSPEED
        - PUTAUT
        - RESETSEQ
        - RCVDATA
        - RCVEXIT
        - SCYDATA
        - SCYEXIT
        - SENDDATA
        - SENDEXIT
        - SEQWRAP
        - SPLPROT
        - SSLCAUTH
        - SSLCIPH
        - SSLPEER
        - STATCHL
        - TRPTYPE
        - USEDLQ
      section_sources:
        'Parameter descriptions for DISPLAY CHANNEL':
          - WHERE
          - ALL
          - CMDSCOPE
          - QSGDISP
          - TYPE
        'Requested parameters':
          - ALTDATE
          - ALTTIME
          - AUTOSTART
          - BATCHSZ
          - CERTLABL
          - CHLTYPE
          - COMPHDR
          - COMPMSG
          - DEFCDISP
          - DESCR
          - HBINT
          - KAINT
          - MAXMSGL
          - MCAUSER
          - MONCHL
          - MRDATA
          - MREXIT
          - MRRTY
          - MRTMR
          - MSGDATA
          - MSGEXIT
          - NPMSPEED
          - PUTAUT
          - RESETSEQ
          - RCVDATA
          - RCVEXIT
          - SCYDATA
          - SCYEXIT
          - SENDDATA
          - SENDEXIT
          - SEQWRAP
          - SPLPROT
          - SSLCAUTH
          - SSLCIPH
          - SSLPEER
          - STATCHL
          - TRPTYPE
          - USEDLQ
    pcf:
      command: MQCMD_INQUIRE_CHANNEL
      request_href: SSFKSJ_9.4.0/refadmin/q087410_.html
      response_href: SSFKSJ_9.4.0/refadmin/q087430_.html
      request_parameters:
        - name: ChannelName
          pcf_type: MQCFST
          type_hint: str
        - name: ChannelAttrs
          pcf_type: MQCFIL
          type_hint: int
          enum_values:
            - MQIACF_ALL
        - name: ChannelType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHT_SENDER
            - MQCHT_SERVER
            - MQCHT_RECEIVER
            - MQCHT_REQUESTER
            - MQCHT_SVRCONN
            - MQCHT_CLNTCONN
            - MQCHT_CLUSRCVR
            - MQCHT_CLUSSDR
            - MQCHT_AMQP
            - MQCHT_MQTT
            - MQCHT_ALL
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
      response_parameters:
        - name: AlterationDate
          pcf_type: MQCFST
          type_hint: str
        - name: AlterationTime
          pcf_type: MQCFST
          type_hint: str
        - name: BatchDataLimit
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchHeartbeat
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchSize
          pcf_type: MQCFIN
          type_hint: int
        - name: Certificatelabel
          pcf_type: MQCFST
          type_hint: str
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
        - name: ChannelStatistics
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_OFF
            - MQMON_Q_MGR
            - MQMON_LOW
            - MQMON_MEDIUM
            - MQMON_HIGH
        - name: ChannelType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHT_SENDER
            - MQCHT_SERVER
            - MQCHT_RECEIVER
            - MQCHT_REQUESTER
            - MQCHT_SVRCONN
            - MQCHT_CLNTCONN
            - MQCHT_CLUSRCVR
            - MQCHT_CLUSSDR
            - MQCHT_MQTT
        - name: ClientChannelWeight
          pcf_type: MQCFIN
          type_hint: int
        - name: ClientIdentifier
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterName
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterNamelist
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
        - name: ConnectionAffinity
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCAFTY_PREFERRED
            - MQCAFTY_NONE
        - name: ConnectionName
          pcf_type: MQCFST
          type_hint: str
        - name: DataConversion
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCDC_NO_SENDER_CONVERSION
            - MQCDC_SENDER_CONVERSION
        - name: DefaultChannelDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHLD_PRIVATE
            - MQCHLD_FIXSHARED
            - MQCHLD_SHARED
        - name: DiscInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: DefReconnect
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
        - name: InDoubtInbound
          pcf_type: MQCFIN
          type_hint: int
        - name: InDoubtOutbound
          pcf_type: MQCFIN
          type_hint: int
        - name: KeepAliveInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: LastMsgTime
          pcf_type: MQCFST
          type_hint: str
        - name: LocalAddress
          pcf_type: MQCFST
          type_hint: str
        - name: LongRetryCount
          pcf_type: MQCFIN
          type_hint: int
        - name: LongRetryInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxInstances
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxInstancesPerClient
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
            - MQCOMPRESS_ANY
        - name: ModeName
          pcf_type: MQCFST
          type_hint: str
        - name: MsgExit
          pcf_type: MQCFST
          type_hint: str
        - name: MsgsReceived
          pcf_type: MQCFIN64
          type_hint: null
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
        - name: MsgsSent
          pcf_type: MQCFIN64
          type_hint: null
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
        - name: PropertyControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPROP_COMPATIBILITY
            - MQPROP_NONE
            - MQPROP_ALL
        - name: PutAuthority
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPA_DEFAULT
            - MQPA_CONTEXT
        - name: QMgrName
          pcf_type: MQCFST
          type_hint: str
        - name: QSGDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSGD_COPY
            - MQQSGD_GROUP
            - MQQSGD_Q_MGR
        - name: ReceiveExit
          pcf_type: MQCFST
          type_hint: str
        - name: ReceiveUserData
          pcf_type: MQCFST
          type_hint: str
        - name: ResetSeq
          pcf_type: MQCFIN
          type_hint: int
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
        - name: SharingConversations
          pcf_type: MQCFIN
          type_hint: int
        - name: ShortRetryCount
          pcf_type: MQCFIN
          type_hint: int
        - name: ShortRetryInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: SPLProtection
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSPL_PASSTHRU
            - MQSPL_REMOVE
            - MQSPL_AS_POLICY
        - name: SSLCipherSpec
          pcf_type: MQCFST
          type_hint: str
        - name: SSLCipherSuite
          pcf_type: MQCFST
          type_hint: str
        - name: SSLClientAuth
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSCA_REQUIRED
            - MQSCA_OPTIONAL
            - MQSCA_NEVER_REQUIRED
        - name: SSLPeerName
          pcf_type: MQCFST
          type_hint: str
        - name: TpName
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
          enum_values:
            - MQUSEDLQ_NO
            - MQUSEDLQ_YES
        - name: UserIdentifier
          pcf_type: MQCFST
          type_hint: str
        - name: XmitQName
          pcf_type: MQCFST
          type_hint: str
    notes:
      - display-channel-chltype-synonym-on-multiplatforms
  - mqsc:
      name: DISPLAY CHANNEL (RQSTR)
      href: SSFKSJ_9.4.0/refadmin/q086040_.html
      positional_parameters:
        - (generic-channel-name)
      input_parameters:
        - WHERE
        - ALL
        - CMDSCOPE
        - QSGDISP
        - TYPE
      output_parameters:
        - ALTDATE
        - ALTTIME
        - AUTOSTART
        - BATCHSZ
        - CERTLABL
        - CHLTYPE
        - COMPHDR
        - COMPMSG
        - CONNAME
        - DEFCDISP
        - DESCR
        - HBINT
        - KAINT
        - LOCLADDR
        - MAXMSGL
        - MCANAME
        - MCATYPE
        - MCAUSER
        - MODENAME
        - MONCHL
        - MRDATA
        - MREXIT
        - MRRTY
        - MRTMR
        - MSGDATA
        - MSGEXIT
        - NPMSPEED
        - PASSWORD
        - PUTAUT
        - RESETSEQ
        - RCVDATA
        - RCVEXIT
        - SCYDATA
        - SCYEXIT
        - SENDDATA
        - SENDEXIT
        - SEQWRAP
        - SPLPROT
        - SSLCAUTH
        - SSLCIPH
        - SSLPEER
        - STATCHL
        - TPNAME
        - TRPTYPE
        - USEDLQ
        - USERID
      section_sources:
        'Parameter descriptions for DISPLAY CHANNEL':
          - WHERE
          - ALL
          - CMDSCOPE
          - QSGDISP
          - TYPE
        'Requested parameters':
          - ALTDATE
          - ALTTIME
          - AUTOSTART
          - BATCHSZ
          - CERTLABL
          - CHLTYPE
          - COMPHDR
          - COMPMSG
          - CONNAME
          - DEFCDISP
          - DESCR
          - HBINT
          - KAINT
          - LOCLADDR
          - MAXMSGL
          - MCANAME
          - MCATYPE
          - MCAUSER
          - MODENAME
          - MONCHL
          - MRDATA
          - MREXIT
          - MRRTY
          - MRTMR
          - MSGDATA
          - MSGEXIT
          - NPMSPEED
          - PASSWORD
          - PUTAUT
          - RESETSEQ
          - RCVDATA
          - RCVEXIT
          - SCYDATA
          - SCYEXIT
          - SENDDATA
          - SENDEXIT
          - SEQWRAP
          - SPLPROT
          - SSLCAUTH
          - SSLCIPH
          - SSLPEER
          - STATCHL
          - TPNAME
          - TRPTYPE
          - USEDLQ
          - USERID
    pcf:
      command: MQCMD_INQUIRE_CHANNEL
      request_href: SSFKSJ_9.4.0/refadmin/q087410_.html
      response_href: SSFKSJ_9.4.0/refadmin/q087430_.html
      request_parameters:
        - name: ChannelName
          pcf_type: MQCFST
          type_hint: str
        - name: ChannelAttrs
          pcf_type: MQCFIL
          type_hint: int
          enum_values:
            - MQIACF_ALL
        - name: ChannelType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHT_SENDER
            - MQCHT_SERVER
            - MQCHT_RECEIVER
            - MQCHT_REQUESTER
            - MQCHT_SVRCONN
            - MQCHT_CLNTCONN
            - MQCHT_CLUSRCVR
            - MQCHT_CLUSSDR
            - MQCHT_AMQP
            - MQCHT_MQTT
            - MQCHT_ALL
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
      response_parameters:
        - name: AlterationDate
          pcf_type: MQCFST
          type_hint: str
        - name: AlterationTime
          pcf_type: MQCFST
          type_hint: str
        - name: BatchDataLimit
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchHeartbeat
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchSize
          pcf_type: MQCFIN
          type_hint: int
        - name: Certificatelabel
          pcf_type: MQCFST
          type_hint: str
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
        - name: ChannelStatistics
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_OFF
            - MQMON_Q_MGR
            - MQMON_LOW
            - MQMON_MEDIUM
            - MQMON_HIGH
        - name: ChannelType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHT_SENDER
            - MQCHT_SERVER
            - MQCHT_RECEIVER
            - MQCHT_REQUESTER
            - MQCHT_SVRCONN
            - MQCHT_CLNTCONN
            - MQCHT_CLUSRCVR
            - MQCHT_CLUSSDR
            - MQCHT_MQTT
        - name: ClientChannelWeight
          pcf_type: MQCFIN
          type_hint: int
        - name: ClientIdentifier
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterName
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterNamelist
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
        - name: ConnectionAffinity
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCAFTY_PREFERRED
            - MQCAFTY_NONE
        - name: ConnectionName
          pcf_type: MQCFST
          type_hint: str
        - name: DataConversion
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCDC_NO_SENDER_CONVERSION
            - MQCDC_SENDER_CONVERSION
        - name: DefaultChannelDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHLD_PRIVATE
            - MQCHLD_FIXSHARED
            - MQCHLD_SHARED
        - name: DiscInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: DefReconnect
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
        - name: InDoubtInbound
          pcf_type: MQCFIN
          type_hint: int
        - name: InDoubtOutbound
          pcf_type: MQCFIN
          type_hint: int
        - name: KeepAliveInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: LastMsgTime
          pcf_type: MQCFST
          type_hint: str
        - name: LocalAddress
          pcf_type: MQCFST
          type_hint: str
        - name: LongRetryCount
          pcf_type: MQCFIN
          type_hint: int
        - name: LongRetryInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxInstances
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxInstancesPerClient
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
            - MQCOMPRESS_ANY
        - name: ModeName
          pcf_type: MQCFST
          type_hint: str
        - name: MsgExit
          pcf_type: MQCFST
          type_hint: str
        - name: MsgsReceived
          pcf_type: MQCFIN64
          type_hint: null
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
        - name: MsgsSent
          pcf_type: MQCFIN64
          type_hint: null
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
        - name: PropertyControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPROP_COMPATIBILITY
            - MQPROP_NONE
            - MQPROP_ALL
        - name: PutAuthority
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPA_DEFAULT
            - MQPA_CONTEXT
        - name: QMgrName
          pcf_type: MQCFST
          type_hint: str
        - name: QSGDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSGD_COPY
            - MQQSGD_GROUP
            - MQQSGD_Q_MGR
        - name: ReceiveExit
          pcf_type: MQCFST
          type_hint: str
        - name: ReceiveUserData
          pcf_type: MQCFST
          type_hint: str
        - name: ResetSeq
          pcf_type: MQCFIN
          type_hint: int
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
        - name: SharingConversations
          pcf_type: MQCFIN
          type_hint: int
        - name: ShortRetryCount
          pcf_type: MQCFIN
          type_hint: int
        - name: ShortRetryInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: SPLProtection
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSPL_PASSTHRU
            - MQSPL_REMOVE
            - MQSPL_AS_POLICY
        - name: SSLCipherSpec
          pcf_type: MQCFST
          type_hint: str
        - name: SSLCipherSuite
          pcf_type: MQCFST
          type_hint: str
        - name: SSLClientAuth
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSCA_REQUIRED
            - MQSCA_OPTIONAL
            - MQSCA_NEVER_REQUIRED
        - name: SSLPeerName
          pcf_type: MQCFST
          type_hint: str
        - name: TpName
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
          enum_values:
            - MQUSEDLQ_NO
            - MQUSEDLQ_YES
        - name: UserIdentifier
          pcf_type: MQCFST
          type_hint: str
        - name: XmitQName
          pcf_type: MQCFST
          type_hint: str
    notes:
      - display-channel-chltype-synonym-on-multiplatforms
  - mqsc:
      name: DISPLAY CHANNEL (CLNTCONN)
      href: SSFKSJ_9.4.0/refadmin/q086040_.html
      positional_parameters:
        - (generic-channel-name)
      input_parameters:
        - WHERE
        - ALL
        - CMDSCOPE
        - QSGDISP
        - TYPE
      output_parameters:
        - AFFINITY
        - ALTDATE
        - ALTTIME
        - CERTLABL
        - CHLTYPE
        - CLNTWGHT
        - COMPHDR
        - COMPMSG
        - CONNAME
        - DEFRECON
        - DESCR
        - HBINT
        - KAINT
        - LOCLADDR
        - MAXMSGL
        - MODENAME
        - PASSWORD
        - QMNAME
        - RCVDATA
        - RCVEXIT
        - SCYDATA
        - SCYEXIT
        - SENDDATA
        - SENDEXIT
        - SSLCIPH
        - SSLPEER
        - TPNAME
        - TRPTYPE
        - USERID
      section_sources:
        'Parameter descriptions for DISPLAY CHANNEL':
          - WHERE
          - ALL
          - CMDSCOPE
          - QSGDISP
          - TYPE
        'Requested parameters':
          - AFFINITY
          - ALTDATE
          - ALTTIME
          - CERTLABL
          - CHLTYPE
          - CLNTWGHT
          - COMPHDR
          - COMPMSG
          - CONNAME
          - DEFRECON
          - DESCR
          - HBINT
          - KAINT
          - LOCLADDR
          - MAXMSGL
          - MODENAME
          - PASSWORD
          - QMNAME
          - RCVDATA
          - RCVEXIT
          - SCYDATA
          - SCYEXIT
          - SENDDATA
          - SENDEXIT
          - SSLCIPH
          - SSLPEER
          - TPNAME
          - TRPTYPE
          - USERID
    pcf:
      command: MQCMD_INQUIRE_CHANNEL
      request_href: SSFKSJ_9.4.0/refadmin/q087410_.html
      response_href: SSFKSJ_9.4.0/refadmin/q087430_.html
      request_parameters:
        - name: ChannelName
          pcf_type: MQCFST
          type_hint: str
        - name: ChannelAttrs
          pcf_type: MQCFIL
          type_hint: int
          enum_values:
            - MQIACF_ALL
        - name: ChannelType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHT_SENDER
            - MQCHT_SERVER
            - MQCHT_RECEIVER
            - MQCHT_REQUESTER
            - MQCHT_SVRCONN
            - MQCHT_CLNTCONN
            - MQCHT_CLUSRCVR
            - MQCHT_CLUSSDR
            - MQCHT_AMQP
            - MQCHT_MQTT
            - MQCHT_ALL
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
      response_parameters:
        - name: AlterationDate
          pcf_type: MQCFST
          type_hint: str
        - name: AlterationTime
          pcf_type: MQCFST
          type_hint: str
        - name: BatchDataLimit
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchHeartbeat
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchSize
          pcf_type: MQCFIN
          type_hint: int
        - name: Certificatelabel
          pcf_type: MQCFST
          type_hint: str
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
        - name: ChannelStatistics
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_OFF
            - MQMON_Q_MGR
            - MQMON_LOW
            - MQMON_MEDIUM
            - MQMON_HIGH
        - name: ChannelType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHT_SENDER
            - MQCHT_SERVER
            - MQCHT_RECEIVER
            - MQCHT_REQUESTER
            - MQCHT_SVRCONN
            - MQCHT_CLNTCONN
            - MQCHT_CLUSRCVR
            - MQCHT_CLUSSDR
            - MQCHT_MQTT
        - name: ClientChannelWeight
          pcf_type: MQCFIN
          type_hint: int
        - name: ClientIdentifier
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterName
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterNamelist
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
        - name: ConnectionAffinity
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCAFTY_PREFERRED
            - MQCAFTY_NONE
        - name: ConnectionName
          pcf_type: MQCFST
          type_hint: str
        - name: DataConversion
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCDC_NO_SENDER_CONVERSION
            - MQCDC_SENDER_CONVERSION
        - name: DefaultChannelDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHLD_PRIVATE
            - MQCHLD_FIXSHARED
            - MQCHLD_SHARED
        - name: DiscInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: DefReconnect
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
        - name: InDoubtInbound
          pcf_type: MQCFIN
          type_hint: int
        - name: InDoubtOutbound
          pcf_type: MQCFIN
          type_hint: int
        - name: KeepAliveInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: LastMsgTime
          pcf_type: MQCFST
          type_hint: str
        - name: LocalAddress
          pcf_type: MQCFST
          type_hint: str
        - name: LongRetryCount
          pcf_type: MQCFIN
          type_hint: int
        - name: LongRetryInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxInstances
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxInstancesPerClient
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
            - MQCOMPRESS_ANY
        - name: ModeName
          pcf_type: MQCFST
          type_hint: str
        - name: MsgExit
          pcf_type: MQCFST
          type_hint: str
        - name: MsgsReceived
          pcf_type: MQCFIN64
          type_hint: null
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
        - name: MsgsSent
          pcf_type: MQCFIN64
          type_hint: null
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
        - name: PropertyControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPROP_COMPATIBILITY
            - MQPROP_NONE
            - MQPROP_ALL
        - name: PutAuthority
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPA_DEFAULT
            - MQPA_CONTEXT
        - name: QMgrName
          pcf_type: MQCFST
          type_hint: str
        - name: QSGDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSGD_COPY
            - MQQSGD_GROUP
            - MQQSGD_Q_MGR
        - name: ReceiveExit
          pcf_type: MQCFST
          type_hint: str
        - name: ReceiveUserData
          pcf_type: MQCFST
          type_hint: str
        - name: ResetSeq
          pcf_type: MQCFIN
          type_hint: int
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
        - name: SharingConversations
          pcf_type: MQCFIN
          type_hint: int
        - name: ShortRetryCount
          pcf_type: MQCFIN
          type_hint: int
        - name: ShortRetryInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: SPLProtection
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSPL_PASSTHRU
            - MQSPL_REMOVE
            - MQSPL_AS_POLICY
        - name: SSLCipherSpec
          pcf_type: MQCFST
          type_hint: str
        - name: SSLCipherSuite
          pcf_type: MQCFST
          type_hint: str
        - name: SSLClientAuth
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSCA_REQUIRED
            - MQSCA_OPTIONAL
            - MQSCA_NEVER_REQUIRED
        - name: SSLPeerName
          pcf_type: MQCFST
          type_hint: str
        - name: TpName
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
          enum_values:
            - MQUSEDLQ_NO
            - MQUSEDLQ_YES
        - name: UserIdentifier
          pcf_type: MQCFST
          type_hint: str
        - name: XmitQName
          pcf_type: MQCFST
          type_hint: str
    notes:
      - display-channel-chltype-synonym-on-multiplatforms
  - mqsc:
      name: DISPLAY CHANNEL (SVRCONN)
      href: SSFKSJ_9.4.0/refadmin/q086040_.html
      positional_parameters:
        - (generic-channel-name)
      input_parameters:
        - WHERE
        - ALL
        - CMDSCOPE
        - QSGDISP
        - TYPE
      output_parameters:
        - ALTDATE
        - ALTTIME
        - AUTOSTART
        - CERTLABL
        - CHLTYPE
        - COMPHDR
        - COMPMSG
        - DEFCDISP
        - DESCR
        - DISCINT
        - HBINT
        - KAINT
        - MAXINST
        - MAXINSTC
        - MAXMSGL
        - MCAUSER
        - MONCHL
        - PUTAUT
        - RCVDATA
        - RCVEXIT
        - SCYDATA
        - SCYEXIT
        - SENDDATA
        - SENDEXIT
        - SHARECNV
        - SSLCAUTH
        - SSLCIPH
        - SSLPEER
        - TPNAME
        - TRPTYPE
      section_sources:
        'Parameter descriptions for DISPLAY CHANNEL':
          - WHERE
          - ALL
          - CMDSCOPE
          - QSGDISP
          - TYPE
        'Requested parameters':
          - ALTDATE
          - ALTTIME
          - AUTOSTART
          - CERTLABL
          - CHLTYPE
          - COMPHDR
          - COMPMSG
          - DEFCDISP
          - DESCR
          - DISCINT
          - HBINT
          - KAINT
          - MAXINST
          - MAXINSTC
          - MAXMSGL
          - MCAUSER
          - MONCHL
          - PUTAUT
          - RCVDATA
          - RCVEXIT
          - SCYDATA
          - SCYEXIT
          - SENDDATA
          - SENDEXIT
          - SHARECNV
          - SSLCAUTH
          - SSLCIPH
          - SSLPEER
          - TPNAME
          - TRPTYPE
    pcf:
      command: MQCMD_INQUIRE_CHANNEL
      request_href: SSFKSJ_9.4.0/refadmin/q087410_.html
      response_href: SSFKSJ_9.4.0/refadmin/q087430_.html
      request_parameters:
        - name: ChannelName
          pcf_type: MQCFST
          type_hint: str
        - name: ChannelAttrs
          pcf_type: MQCFIL
          type_hint: int
          enum_values:
            - MQIACF_ALL
        - name: ChannelType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHT_SENDER
            - MQCHT_SERVER
            - MQCHT_RECEIVER
            - MQCHT_REQUESTER
            - MQCHT_SVRCONN
            - MQCHT_CLNTCONN
            - MQCHT_CLUSRCVR
            - MQCHT_CLUSSDR
            - MQCHT_AMQP
            - MQCHT_MQTT
            - MQCHT_ALL
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
      response_parameters:
        - name: AlterationDate
          pcf_type: MQCFST
          type_hint: str
        - name: AlterationTime
          pcf_type: MQCFST
          type_hint: str
        - name: BatchDataLimit
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchHeartbeat
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchSize
          pcf_type: MQCFIN
          type_hint: int
        - name: Certificatelabel
          pcf_type: MQCFST
          type_hint: str
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
        - name: ChannelStatistics
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_OFF
            - MQMON_Q_MGR
            - MQMON_LOW
            - MQMON_MEDIUM
            - MQMON_HIGH
        - name: ChannelType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHT_SENDER
            - MQCHT_SERVER
            - MQCHT_RECEIVER
            - MQCHT_REQUESTER
            - MQCHT_SVRCONN
            - MQCHT_CLNTCONN
            - MQCHT_CLUSRCVR
            - MQCHT_CLUSSDR
            - MQCHT_MQTT
        - name: ClientChannelWeight
          pcf_type: MQCFIN
          type_hint: int
        - name: ClientIdentifier
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterName
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterNamelist
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
        - name: ConnectionAffinity
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCAFTY_PREFERRED
            - MQCAFTY_NONE
        - name: ConnectionName
          pcf_type: MQCFST
          type_hint: str
        - name: DataConversion
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCDC_NO_SENDER_CONVERSION
            - MQCDC_SENDER_CONVERSION
        - name: DefaultChannelDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHLD_PRIVATE
            - MQCHLD_FIXSHARED
            - MQCHLD_SHARED
        - name: DiscInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: DefReconnect
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
        - name: InDoubtInbound
          pcf_type: MQCFIN
          type_hint: int
        - name: InDoubtOutbound
          pcf_type: MQCFIN
          type_hint: int
        - name: KeepAliveInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: LastMsgTime
          pcf_type: MQCFST
          type_hint: str
        - name: LocalAddress
          pcf_type: MQCFST
          type_hint: str
        - name: LongRetryCount
          pcf_type: MQCFIN
          type_hint: int
        - name: LongRetryInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxInstances
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxInstancesPerClient
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
            - MQCOMPRESS_ANY
        - name: ModeName
          pcf_type: MQCFST
          type_hint: str
        - name: MsgExit
          pcf_type: MQCFST
          type_hint: str
        - name: MsgsReceived
          pcf_type: MQCFIN64
          type_hint: null
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
        - name: MsgsSent
          pcf_type: MQCFIN64
          type_hint: null
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
        - name: PropertyControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPROP_COMPATIBILITY
            - MQPROP_NONE
            - MQPROP_ALL
        - name: PutAuthority
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPA_DEFAULT
            - MQPA_CONTEXT
        - name: QMgrName
          pcf_type: MQCFST
          type_hint: str
        - name: QSGDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSGD_COPY
            - MQQSGD_GROUP
            - MQQSGD_Q_MGR
        - name: ReceiveExit
          pcf_type: MQCFST
          type_hint: str
        - name: ReceiveUserData
          pcf_type: MQCFST
          type_hint: str
        - name: ResetSeq
          pcf_type: MQCFIN
          type_hint: int
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
        - name: SharingConversations
          pcf_type: MQCFIN
          type_hint: int
        - name: ShortRetryCount
          pcf_type: MQCFIN
          type_hint: int
        - name: ShortRetryInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: SPLProtection
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSPL_PASSTHRU
            - MQSPL_REMOVE
            - MQSPL_AS_POLICY
        - name: SSLCipherSpec
          pcf_type: MQCFST
          type_hint: str
        - name: SSLCipherSuite
          pcf_type: MQCFST
          type_hint: str
        - name: SSLClientAuth
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSCA_REQUIRED
            - MQSCA_OPTIONAL
            - MQSCA_NEVER_REQUIRED
        - name: SSLPeerName
          pcf_type: MQCFST
          type_hint: str
        - name: TpName
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
          enum_values:
            - MQUSEDLQ_NO
            - MQUSEDLQ_YES
        - name: UserIdentifier
          pcf_type: MQCFST
          type_hint: str
        - name: XmitQName
          pcf_type: MQCFST
          type_hint: str
    notes:
      - display-channel-chltype-synonym-on-multiplatforms
  - mqsc:
      name: DISPLAY CHANNEL (CLUSSDR)
      href: SSFKSJ_9.4.0/refadmin/q086040_.html
      positional_parameters:
        - (generic-channel-name)
      input_parameters:
        - WHERE
        - ALL
        - CMDSCOPE
        - QSGDISP
        - TYPE
      output_parameters:
        - ALTDATE
        - ALTTIME
        - BATCHHB
        - BATCHINT
        - BATCHLIM
        - BATCHSZ
        - CERTLABL
        - CHLTYPE
        - CLUSNL
        - CLUSTER
        - CLWLPRTY
        - CLWLRANK
        - CLWLWGHT
        - COMPHDR
        - COMPMSG
        - CONNAME
        - CONVERT
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
        - MONCHL
        - MSGDATA
        - MSGEXIT
        - NPMSPEED
        - PASSWORD
        - PROPCTL
        - RESETSEQ
        - RCVDATA
        - RCVEXIT
        - SCYDATA
        - SCYEXIT
        - SENDDATA
        - SENDEXIT
        - SEQWRAP
        - SHORTRTY
        - SHORTTMR
        - SSLCIPH
        - SSLPEER
        - STATCHL
        - TPNAME
        - TRPTYPE
        - USEDLQ
        - USERID
      section_sources:
        'Parameter descriptions for DISPLAY CHANNEL':
          - WHERE
          - ALL
          - CMDSCOPE
          - QSGDISP
          - TYPE
        'Requested parameters':
          - ALTDATE
          - ALTTIME
          - BATCHHB
          - BATCHINT
          - BATCHLIM
          - BATCHSZ
          - CERTLABL
          - CHLTYPE
          - CLUSNL
          - CLUSTER
          - CLWLPRTY
          - CLWLRANK
          - CLWLWGHT
          - COMPHDR
          - COMPMSG
          - CONNAME
          - CONVERT
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
          - MONCHL
          - MSGDATA
          - MSGEXIT
          - NPMSPEED
          - PASSWORD
          - PROPCTL
          - RESETSEQ
          - RCVDATA
          - RCVEXIT
          - SCYDATA
          - SCYEXIT
          - SENDDATA
          - SENDEXIT
          - SEQWRAP
          - SHORTRTY
          - SHORTTMR
          - SSLCIPH
          - SSLPEER
          - STATCHL
          - TPNAME
          - TRPTYPE
          - USEDLQ
          - USERID
    pcf:
      command: MQCMD_INQUIRE_CHANNEL
      request_href: SSFKSJ_9.4.0/refadmin/q087410_.html
      response_href: SSFKSJ_9.4.0/refadmin/q087430_.html
      request_parameters:
        - name: ChannelName
          pcf_type: MQCFST
          type_hint: str
        - name: ChannelAttrs
          pcf_type: MQCFIL
          type_hint: int
          enum_values:
            - MQIACF_ALL
        - name: ChannelType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHT_SENDER
            - MQCHT_SERVER
            - MQCHT_RECEIVER
            - MQCHT_REQUESTER
            - MQCHT_SVRCONN
            - MQCHT_CLNTCONN
            - MQCHT_CLUSRCVR
            - MQCHT_CLUSSDR
            - MQCHT_AMQP
            - MQCHT_MQTT
            - MQCHT_ALL
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
      response_parameters:
        - name: AlterationDate
          pcf_type: MQCFST
          type_hint: str
        - name: AlterationTime
          pcf_type: MQCFST
          type_hint: str
        - name: BatchDataLimit
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchHeartbeat
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchSize
          pcf_type: MQCFIN
          type_hint: int
        - name: Certificatelabel
          pcf_type: MQCFST
          type_hint: str
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
        - name: ChannelStatistics
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_OFF
            - MQMON_Q_MGR
            - MQMON_LOW
            - MQMON_MEDIUM
            - MQMON_HIGH
        - name: ChannelType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHT_SENDER
            - MQCHT_SERVER
            - MQCHT_RECEIVER
            - MQCHT_REQUESTER
            - MQCHT_SVRCONN
            - MQCHT_CLNTCONN
            - MQCHT_CLUSRCVR
            - MQCHT_CLUSSDR
            - MQCHT_MQTT
        - name: ClientChannelWeight
          pcf_type: MQCFIN
          type_hint: int
        - name: ClientIdentifier
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterName
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterNamelist
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
        - name: ConnectionAffinity
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCAFTY_PREFERRED
            - MQCAFTY_NONE
        - name: ConnectionName
          pcf_type: MQCFST
          type_hint: str
        - name: DataConversion
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCDC_NO_SENDER_CONVERSION
            - MQCDC_SENDER_CONVERSION
        - name: DefaultChannelDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHLD_PRIVATE
            - MQCHLD_FIXSHARED
            - MQCHLD_SHARED
        - name: DiscInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: DefReconnect
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
        - name: InDoubtInbound
          pcf_type: MQCFIN
          type_hint: int
        - name: InDoubtOutbound
          pcf_type: MQCFIN
          type_hint: int
        - name: KeepAliveInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: LastMsgTime
          pcf_type: MQCFST
          type_hint: str
        - name: LocalAddress
          pcf_type: MQCFST
          type_hint: str
        - name: LongRetryCount
          pcf_type: MQCFIN
          type_hint: int
        - name: LongRetryInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxInstances
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxInstancesPerClient
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
            - MQCOMPRESS_ANY
        - name: ModeName
          pcf_type: MQCFST
          type_hint: str
        - name: MsgExit
          pcf_type: MQCFST
          type_hint: str
        - name: MsgsReceived
          pcf_type: MQCFIN64
          type_hint: null
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
        - name: MsgsSent
          pcf_type: MQCFIN64
          type_hint: null
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
        - name: PropertyControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPROP_COMPATIBILITY
            - MQPROP_NONE
            - MQPROP_ALL
        - name: PutAuthority
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPA_DEFAULT
            - MQPA_CONTEXT
        - name: QMgrName
          pcf_type: MQCFST
          type_hint: str
        - name: QSGDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSGD_COPY
            - MQQSGD_GROUP
            - MQQSGD_Q_MGR
        - name: ReceiveExit
          pcf_type: MQCFST
          type_hint: str
        - name: ReceiveUserData
          pcf_type: MQCFST
          type_hint: str
        - name: ResetSeq
          pcf_type: MQCFIN
          type_hint: int
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
        - name: SharingConversations
          pcf_type: MQCFIN
          type_hint: int
        - name: ShortRetryCount
          pcf_type: MQCFIN
          type_hint: int
        - name: ShortRetryInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: SPLProtection
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSPL_PASSTHRU
            - MQSPL_REMOVE
            - MQSPL_AS_POLICY
        - name: SSLCipherSpec
          pcf_type: MQCFST
          type_hint: str
        - name: SSLCipherSuite
          pcf_type: MQCFST
          type_hint: str
        - name: SSLClientAuth
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSCA_REQUIRED
            - MQSCA_OPTIONAL
            - MQSCA_NEVER_REQUIRED
        - name: SSLPeerName
          pcf_type: MQCFST
          type_hint: str
        - name: TpName
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
          enum_values:
            - MQUSEDLQ_NO
            - MQUSEDLQ_YES
        - name: UserIdentifier
          pcf_type: MQCFST
          type_hint: str
        - name: XmitQName
          pcf_type: MQCFST
          type_hint: str
    notes:
      - display-channel-chltype-synonym-on-multiplatforms
  - mqsc:
      name: DISPLAY CHANNEL (CLUSRCVR)
      href: SSFKSJ_9.4.0/refadmin/q086040_.html
      positional_parameters:
        - (generic-channel-name)
      input_parameters:
        - WHERE
        - ALL
        - CMDSCOPE
        - QSGDISP
        - TYPE
      output_parameters:
        - ALTDATE
        - ALTTIME
        - BATCHHB
        - BATCHINT
        - BATCHLIM
        - BATCHSZ
        - CERTLABL
        - CHLTYPE
        - CLUSNL
        - CLUSTER
        - CLWLPRTY
        - CLWLRANK
        - CLWLWGHT
        - COMPHDR
        - COMPMSG
        - CONNAME
        - CONVERT
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
        - MONCHL
        - MRDATA
        - MREXIT
        - MRRTY
        - MRTMR
        - MSGDATA
        - MSGEXIT
        - NETPRTY
        - NPMSPEED
        - PROPCTL
        - PUTAUT
        - RESETSEQ
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
        - STATCHL
        - TPNAME
        - TRPTYPE
        - USEDLQ
      section_sources:
        'Parameter descriptions for DISPLAY CHANNEL':
          - WHERE
          - ALL
          - CMDSCOPE
          - QSGDISP
          - TYPE
        'Requested parameters':
          - ALTDATE
          - ALTTIME
          - BATCHHB
          - BATCHINT
          - BATCHLIM
          - BATCHSZ
          - CERTLABL
          - CHLTYPE
          - CLUSNL
          - CLUSTER
          - CLWLPRTY
          - CLWLRANK
          - CLWLWGHT
          - COMPHDR
          - COMPMSG
          - CONNAME
          - CONVERT
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
          - MONCHL
          - MRDATA
          - MREXIT
          - MRRTY
          - MRTMR
          - MSGDATA
          - MSGEXIT
          - NETPRTY
          - NPMSPEED
          - PROPCTL
          - PUTAUT
          - RESETSEQ
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
          - STATCHL
          - TPNAME
          - TRPTYPE
          - USEDLQ
    pcf:
      command: MQCMD_INQUIRE_CHANNEL
      request_href: SSFKSJ_9.4.0/refadmin/q087410_.html
      response_href: SSFKSJ_9.4.0/refadmin/q087430_.html
      request_parameters:
        - name: ChannelName
          pcf_type: MQCFST
          type_hint: str
        - name: ChannelAttrs
          pcf_type: MQCFIL
          type_hint: int
          enum_values:
            - MQIACF_ALL
        - name: ChannelType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHT_SENDER
            - MQCHT_SERVER
            - MQCHT_RECEIVER
            - MQCHT_REQUESTER
            - MQCHT_SVRCONN
            - MQCHT_CLNTCONN
            - MQCHT_CLUSRCVR
            - MQCHT_CLUSSDR
            - MQCHT_AMQP
            - MQCHT_MQTT
            - MQCHT_ALL
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
      response_parameters:
        - name: AlterationDate
          pcf_type: MQCFST
          type_hint: str
        - name: AlterationTime
          pcf_type: MQCFST
          type_hint: str
        - name: BatchDataLimit
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchHeartbeat
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchSize
          pcf_type: MQCFIN
          type_hint: int
        - name: Certificatelabel
          pcf_type: MQCFST
          type_hint: str
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
        - name: ChannelStatistics
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_OFF
            - MQMON_Q_MGR
            - MQMON_LOW
            - MQMON_MEDIUM
            - MQMON_HIGH
        - name: ChannelType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHT_SENDER
            - MQCHT_SERVER
            - MQCHT_RECEIVER
            - MQCHT_REQUESTER
            - MQCHT_SVRCONN
            - MQCHT_CLNTCONN
            - MQCHT_CLUSRCVR
            - MQCHT_CLUSSDR
            - MQCHT_MQTT
        - name: ClientChannelWeight
          pcf_type: MQCFIN
          type_hint: int
        - name: ClientIdentifier
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterName
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterNamelist
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
        - name: ConnectionAffinity
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCAFTY_PREFERRED
            - MQCAFTY_NONE
        - name: ConnectionName
          pcf_type: MQCFST
          type_hint: str
        - name: DataConversion
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCDC_NO_SENDER_CONVERSION
            - MQCDC_SENDER_CONVERSION
        - name: DefaultChannelDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHLD_PRIVATE
            - MQCHLD_FIXSHARED
            - MQCHLD_SHARED
        - name: DiscInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: DefReconnect
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
        - name: InDoubtInbound
          pcf_type: MQCFIN
          type_hint: int
        - name: InDoubtOutbound
          pcf_type: MQCFIN
          type_hint: int
        - name: KeepAliveInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: LastMsgTime
          pcf_type: MQCFST
          type_hint: str
        - name: LocalAddress
          pcf_type: MQCFST
          type_hint: str
        - name: LongRetryCount
          pcf_type: MQCFIN
          type_hint: int
        - name: LongRetryInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxInstances
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxInstancesPerClient
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
            - MQCOMPRESS_ANY
        - name: ModeName
          pcf_type: MQCFST
          type_hint: str
        - name: MsgExit
          pcf_type: MQCFST
          type_hint: str
        - name: MsgsReceived
          pcf_type: MQCFIN64
          type_hint: null
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
        - name: MsgsSent
          pcf_type: MQCFIN64
          type_hint: null
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
        - name: PropertyControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPROP_COMPATIBILITY
            - MQPROP_NONE
            - MQPROP_ALL
        - name: PutAuthority
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPA_DEFAULT
            - MQPA_CONTEXT
        - name: QMgrName
          pcf_type: MQCFST
          type_hint: str
        - name: QSGDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSGD_COPY
            - MQQSGD_GROUP
            - MQQSGD_Q_MGR
        - name: ReceiveExit
          pcf_type: MQCFST
          type_hint: str
        - name: ReceiveUserData
          pcf_type: MQCFST
          type_hint: str
        - name: ResetSeq
          pcf_type: MQCFIN
          type_hint: int
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
        - name: SharingConversations
          pcf_type: MQCFIN
          type_hint: int
        - name: ShortRetryCount
          pcf_type: MQCFIN
          type_hint: int
        - name: ShortRetryInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: SPLProtection
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSPL_PASSTHRU
            - MQSPL_REMOVE
            - MQSPL_AS_POLICY
        - name: SSLCipherSpec
          pcf_type: MQCFST
          type_hint: str
        - name: SSLCipherSuite
          pcf_type: MQCFST
          type_hint: str
        - name: SSLClientAuth
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSCA_REQUIRED
            - MQSCA_OPTIONAL
            - MQSCA_NEVER_REQUIRED
        - name: SSLPeerName
          pcf_type: MQCFST
          type_hint: str
        - name: TpName
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
          enum_values:
            - MQUSEDLQ_NO
            - MQUSEDLQ_YES
        - name: UserIdentifier
          pcf_type: MQCFST
          type_hint: str
        - name: XmitQName
          pcf_type: MQCFST
          type_hint: str
    notes:
      - display-channel-chltype-synonym-on-multiplatforms
  - mqsc:
      name: DISPLAY CHANNEL (AMQP)
      href: SSFKSJ_9.4.0/refadmin/q086040_.html
      positional_parameters:
        - (generic-channel-name)
      input_parameters:
        - WHERE
        - ALL
        - CMDSCOPE
        - QSGDISP
        - TYPE
      output_parameters:
        - ALTDATE
        - ALTTIME
        - AMQPKA
        - CERTLABL
        - CHLTYPE
        - DESCR
        - LOCLADDR
        - MAXINST
        - MAXMSGL
        - MCAUSER
        - PORT
        - SSLCAUTH
        - SSLCIPH
        - SSLPEER
        - TPROOT
        - USECLTID
      section_sources:
        'Parameter descriptions for DISPLAY CHANNEL':
          - WHERE
          - ALL
          - CMDSCOPE
          - QSGDISP
          - TYPE
        'Requested parameters':
          - ALTDATE
          - ALTTIME
          - AMQPKA
          - CERTLABL
          - CHLTYPE
          - DESCR
          - LOCLADDR
          - MAXINST
          - MAXMSGL
          - MCAUSER
          - PORT
          - SSLCAUTH
          - SSLCIPH
          - SSLPEER
          - TPROOT
          - USECLTID
    pcf:
      command: MQCMD_INQUIRE_CHANNEL
      request_href: SSFKSJ_9.4.0/refadmin/q087410_.html
      response_href: SSFKSJ_9.4.0/refadmin/q087430_.html
      request_parameters:
        - name: ChannelName
          pcf_type: MQCFST
          type_hint: str
        - name: ChannelAttrs
          pcf_type: MQCFIL
          type_hint: int
          enum_values:
            - MQIACF_ALL
        - name: ChannelType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHT_SENDER
            - MQCHT_SERVER
            - MQCHT_RECEIVER
            - MQCHT_REQUESTER
            - MQCHT_SVRCONN
            - MQCHT_CLNTCONN
            - MQCHT_CLUSRCVR
            - MQCHT_CLUSSDR
            - MQCHT_AMQP
            - MQCHT_MQTT
            - MQCHT_ALL
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
      response_parameters:
        - name: AlterationDate
          pcf_type: MQCFST
          type_hint: str
        - name: AlterationTime
          pcf_type: MQCFST
          type_hint: str
        - name: BatchDataLimit
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchHeartbeat
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchSize
          pcf_type: MQCFIN
          type_hint: int
        - name: Certificatelabel
          pcf_type: MQCFST
          type_hint: str
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
        - name: ChannelStatistics
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_OFF
            - MQMON_Q_MGR
            - MQMON_LOW
            - MQMON_MEDIUM
            - MQMON_HIGH
        - name: ChannelType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHT_SENDER
            - MQCHT_SERVER
            - MQCHT_RECEIVER
            - MQCHT_REQUESTER
            - MQCHT_SVRCONN
            - MQCHT_CLNTCONN
            - MQCHT_CLUSRCVR
            - MQCHT_CLUSSDR
            - MQCHT_MQTT
        - name: ClientChannelWeight
          pcf_type: MQCFIN
          type_hint: int
        - name: ClientIdentifier
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterName
          pcf_type: MQCFST
          type_hint: str
        - name: ClusterNamelist
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
        - name: ConnectionAffinity
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCAFTY_PREFERRED
            - MQCAFTY_NONE
        - name: ConnectionName
          pcf_type: MQCFST
          type_hint: str
        - name: DataConversion
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCDC_NO_SENDER_CONVERSION
            - MQCDC_SENDER_CONVERSION
        - name: DefaultChannelDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHLD_PRIVATE
            - MQCHLD_FIXSHARED
            - MQCHLD_SHARED
        - name: DiscInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: DefReconnect
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
        - name: InDoubtInbound
          pcf_type: MQCFIN
          type_hint: int
        - name: InDoubtOutbound
          pcf_type: MQCFIN
          type_hint: int
        - name: KeepAliveInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: LastMsgTime
          pcf_type: MQCFST
          type_hint: str
        - name: LocalAddress
          pcf_type: MQCFST
          type_hint: str
        - name: LongRetryCount
          pcf_type: MQCFIN
          type_hint: int
        - name: LongRetryInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxInstances
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxInstancesPerClient
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
            - MQCOMPRESS_ANY
        - name: ModeName
          pcf_type: MQCFST
          type_hint: str
        - name: MsgExit
          pcf_type: MQCFST
          type_hint: str
        - name: MsgsReceived
          pcf_type: MQCFIN64
          type_hint: null
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
        - name: MsgsSent
          pcf_type: MQCFIN64
          type_hint: null
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
        - name: PropertyControl
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPROP_COMPATIBILITY
            - MQPROP_NONE
            - MQPROP_ALL
        - name: PutAuthority
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQPA_DEFAULT
            - MQPA_CONTEXT
        - name: QMgrName
          pcf_type: MQCFST
          type_hint: str
        - name: QSGDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSGD_COPY
            - MQQSGD_GROUP
            - MQQSGD_Q_MGR
        - name: ReceiveExit
          pcf_type: MQCFST
          type_hint: str
        - name: ReceiveUserData
          pcf_type: MQCFST
          type_hint: str
        - name: ResetSeq
          pcf_type: MQCFIN
          type_hint: int
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
        - name: SharingConversations
          pcf_type: MQCFIN
          type_hint: int
        - name: ShortRetryCount
          pcf_type: MQCFIN
          type_hint: int
        - name: ShortRetryInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: SPLProtection
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSPL_PASSTHRU
            - MQSPL_REMOVE
            - MQSPL_AS_POLICY
        - name: SSLCipherSpec
          pcf_type: MQCFST
          type_hint: str
        - name: SSLCipherSuite
          pcf_type: MQCFST
          type_hint: str
        - name: SSLClientAuth
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSCA_REQUIRED
            - MQSCA_OPTIONAL
            - MQSCA_NEVER_REQUIRED
        - name: SSLPeerName
          pcf_type: MQCFST
          type_hint: str
        - name: TpName
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
          enum_values:
            - MQUSEDLQ_NO
            - MQUSEDLQ_YES
        - name: UserIdentifier
          pcf_type: MQCFST
          type_hint: str
        - name: XmitQName
          pcf_type: MQCFST
          type_hint: str
    notes:
      - display-channel-chltype-synonym-on-multiplatforms
  - mqsc:
      name: DISPLAY CHSTATUS
      href: SSFKSJ_9.4.0/refadmin/q086090_.html
      positional_parameters:
        - (generic-channel-name)
      input_parameters:
        - WHERE
        - ALL
        - CHLDISP
        - CMDSCOPE
        - CONNAME
        - CURRENT
        - SAVED
        - SHORT
        - MONITOR
        - XMITQ
      output_parameters:
        - Batches
        - BatchSize
        - BatchSizeIndicator
        - BuffersReceived
        - BuffersSent
        - BytesReceived
        - BytesSent
        - ChannelDisposition
        - ChannelInstanceType
        - ChannelMonitoring
        - ChannelName
        - ChannelStartDate
        - ChannelStartTime
        - ChannelStatistics
        - ChannelStatus
        - ChannelType
        - CompressionRate
        - CompressionTime
        - ConnectionName
        - CurrentLUWID
        - CurrentMsgs
        - CurrentSequenceNumber
        - CurrentSharingConversations
        - ExitTime
        - HeaderCompression
        - HeartbeatInterval
        - InDoubtStatus
        - KeepAliveInterval
        - LastLUWID
        - LastMsgDate
        - LastMsgTime
        - LastSequenceNumber
        - LocalAddress
        - LongRetriesLeft
        - MaxMsgLength
        - MaxSharingConversations
        - MCAJobName
        - MCAStatus
        - MCAUserIdentifier
        - MessageCompression
        - Msgs
        - MsgsAvailable
        - NetTime
        - NonPersistentMsgSpeed
        - QMgrName
        - RemoteApplTag
        - RemoteProduct
        - RemoteVersion
        - RemoteQMgrName
        - ShortRetriesLeft
        - SecurityProtocol
        - SSLCertRemoteIssuerName
        - SSLCertUserId
        - SSLCipherSpecification
        - SSLKeyResetDate
        - SSLKeyResets
        - SSLKeyResetTime
        - SSLShortPeerName
        - StopRequested
        - SubState
        - XmitQName
        - XQTime
      section_sources:
        'Parameter descriptions for DISPLAY CHSTATUS on all platforms':
          - WHERE
          - ALL
          - CHLDISP
          - CMDSCOPE
          - CONNAME
          - CURRENT
          - SAVED
          - SHORT
          - MONITOR
          - XMITQ
    pcf:
      command: MQCMD_INQUIRE_CHANNEL_STATUS
      request_href: SSFKSJ_9.4.0/refadmin/q087540_.html
      response_href: SSFKSJ_9.4.0/refadmin/q087560_.html
      request_parameters:
        - name: ChannelName
          pcf_type: MQCFST
          type_hint: str
        - name: ChannelDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHLD_ALL
            - MQCHLD_PRIVATE
            - MQCHLD_SHARED
        - name: ChannelInstanceAttrs
          pcf_type: MQCFIL
          type_hint: int
          enum_values:
            - MQIACF_ALL
            - MQCACH_CHANNEL_NAME
            - MQCACH_CONNECTION_NAME
            - MQCACH_CURRENT_LUWID
            - MQCACH_LAST_LUWID
            - MQCACH_XMIT_Q_NAME
            - MQIACH_CHANNEL_INSTANCE_TYPE
            - MQIACH_CHANNEL_TYPE
            - MQIACH_CURRENT_MSGS
            - MQIACH_CURRENT_SEQ_NUMBER
            - MQIACH_INDOUBT_STATUS
            - MQIACH_LAST_SEQ_NUMBER
            - MQCA_Q_MGR_NAME
            - MQCA_REMOTE_Q_MGR_NAME
            - MQCACH_CHANNEL_START_DATE
            - MQCACH_CHANNEL_START_TIME
            - MQCACH_LAST_MSG_DATE
            - MQCACH_LAST_MSG_TIME
            - MQCACH_LOCAL_ADDRESS
            - MQCACH_MCA_JOB_NAME
            - MQCACH_MCA_USER_ID
            - MQCACH_REMOTE_APPL_TAG
            - MQCACH_REMOTE_PRODUCT
            - MQCACH_REMOTE_VERSION
            - MQCACH_SSL_CIPHER_SPEC
            - MQCACH_SSL_SHORT_PEER_NAME
            - MQCACH_SSL_CERT_ISSUER_NAME
            - MQCACH_SSL_CERT_USER_ID
            - MQCACH_TOPIC_ROOT
            - MQIA_MONITORING_CHANNEL
            - MQIA_STATISTICS_CHANNEL
            - MQIACF_MONITORING
            - MQIACH_BATCH_SIZE_INDICATOR
            - MQIACH_COMPRESSION_RATE
            - MQIACH_COMPRESSION_TIME
            - MQIACH_EXIT_TIME_INDICATOR
            - MQIACH_NETWORK_TIME_INDICATOR
            - MQIACH_XMITQ_MSGS_AVAILABLE
            - MQIACH_XMITQ_TIME_INDICATOR
            - MQIACH_BATCHES
            - MQIACH_BUFFERS_RCVD
            - MQIACH_BUFFERS_SENT
            - MQIACH_BYTES_RCVD
            - MQIACH_BYTES_SENT
            - MQIACH_CHANNEL_SUBSTATE
            - MQIACH_CURRENT_SHARING_CONVS
            - MQIACH_HDR_COMPRESSION
            - MQIACH_KEEP_ALIVE_INTERVAL
            - MQIACH_LONG_RETRIES_LEFT
            - MQIACH_MAX_MSG_LENGTH
            - MQIACH_MAX_SHARING_CONVS
            - MQIACH_MCA_STATUS
            - MQIACH_MSG_COMPRESSION
            - MQIACH_MSGS
            - MQIACH_SECURITY_PROTOCOL
            - MQIACH_SHORT_RETRIES_LEFT
            - MQIACH_SSL_KEY_RESETS
            - MQIACH_SSL_RESET_DATE
            - MQIACH_SSL_RESET_TIME
            - MQIACH_STOP_REQUESTED
            - MQIACH_BATCH_SIZE
            - MQIACH_HB_INTERVAL
            - MQIACH_NPM_SPEED
            - MQCACH_Q_MGR_NAME
        - name: ChannelInstanceType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQOT_CURRENT_CHANNEL
            - MQOT_SAVED_CHANNEL
            - MQOT_SHORT_CHANNEL
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: ConnectionName
          pcf_type: MQCFST
          type_hint: str
        - name: IntegerFilterCommand
          pcf_type: MQCFIF
          type_hint: null
        - name: StringFilterCommand
          pcf_type: MQCFSF
          type_hint: null
        - name: XmitQName
          pcf_type: MQCFST
          type_hint: str
      response_parameters:
        - name: Batches
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchSize
          pcf_type: MQCFIN
          type_hint: int
        - name: BatchSizeIndicator
          pcf_type: MQCFIL
          type_hint: int
        - name: BuffersReceived
          pcf_type: MQCFIN
          type_hint: int
        - name: BuffersSent
          pcf_type: MQCFIN
          type_hint: int
        - name: BytesReceived
          pcf_type: MQCFIN
          type_hint: int
        - name: BytesSent
          pcf_type: MQCFIN
          type_hint: int
        - name: ChannelDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHLD_PRIVATE
            - MQCHLD_SHARED
            - MQCHLD_FIXSHARED
        - name: ChannelInstanceType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQOT_CURRENT_CHANNEL
            - MQOT_SAVED_CHANNEL
            - MQOT_SHORT_CHANNEL
        - name: ChannelMonitoring
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_OFF
            - MQMON_LOW
            - MQMON_MEDIUM
            - MQMON_HIGH
        - name: ChannelName
          pcf_type: MQCFST
          type_hint: str
        - name: ChannelStartDate
          pcf_type: MQCFST
          type_hint: str
        - name: ChannelStartTime
          pcf_type: MQCFST
          type_hint: str
        - name: ChannelStatistics
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMON_OFF
            - MQMON_LOW
            - MQMON_MEDIUM
            - MQMON_HIGH
        - name: ChannelStatus
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHS_BINDING
            - MQCHS_STARTING
            - MQCHS_RUNNING
            - MQCHS_PAUSED
            - MQCHS_STOPPING
            - MQCHS_RETRYING
            - MQCHS_STOPPED
            - MQCHS_REQUESTING
            - MQCHS_SWITCHING
            - MQCHS_INITIALIZING
        - name: ChannelType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHT_SENDER
            - MQCHT_SERVER
            - MQCHT_RECEIVER
            - MQCHT_REQUESTER
            - MQCHT_SVRCONN
            - MQCHT_CLNTCONN
            - MQCHT_CLUSRCVR
            - MQCHT_CLUSSDR
        - name: CompressionRate
          pcf_type: MQCFIL
          type_hint: int
        - name: CompressionTime
          pcf_type: MQCFIL
          type_hint: int
        - name: ConnectionName
          pcf_type: MQCFST
          type_hint: str
        - name: CurrentLUWID
          pcf_type: MQCFST
          type_hint: str
        - name: CurrentMsgs
          pcf_type: MQCFIN
          type_hint: int
        - name: CurrentSequenceNumber
          pcf_type: MQCFIN
          type_hint: int
        - name: CurrentSharingConversations
          pcf_type: MQCFIN
          type_hint: int
        - name: ExitTime
          pcf_type: MQCFIL
          type_hint: int
        - name: HeaderCompression
          pcf_type: MQCFIL
          type_hint: int
          enum_values:
            - MQCOMPRESS_NONE
            - MQCOMPRESS_SYSTEM
            - MQCOMPRESS_NOT_AVAILABLE
        - name: HeartbeatInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: InDoubtStatus
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHIDS_NOT_INDOUBT
            - MQCHIDS_INDOUBT
        - name: KeepAliveInterval
          pcf_type: MQCFIN
          type_hint: int
        - name: LastLUWID
          pcf_type: MQCFST
          type_hint: str
        - name: LastMsgDate
          pcf_type: MQCFST
          type_hint: str
        - name: LastMsgTime
          pcf_type: MQCFST
          type_hint: str
        - name: LastSequenceNumber
          pcf_type: MQCFIN
          type_hint: int
        - name: LocalAddress
          pcf_type: MQCFST
          type_hint: str
        - name: LongRetriesLeft
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxMsgLength
          pcf_type: MQCFIN
          type_hint: int
        - name: MaxSharingConversations
          pcf_type: MQCFIN
          type_hint: int
        - name: MCAJobName
          pcf_type: MQCFST
          type_hint: str
        - name: MCAStatus
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMCAS_STOPPED
            - MQMCAS_RUNNING
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
            - MQCOMPRESS_NOT_AVAILABLE
        - name: Msgs
          pcf_type: MQCFIN
          type_hint: int
        - name: MsgsAvailable
          pcf_type: MQCFIN
          type_hint: int
        - name: NetTime
          pcf_type: MQCFIL
          type_hint: int
        - name: NonPersistentMsgSpeed
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQNPMS_NORMAL
            - MQNPMS_FAST
        - name: QMgrName
          pcf_type: MQCFST
          type_hint: str
        - name: RemoteApplTag
          pcf_type: MQCFST
          type_hint: str
        - name: RemoteProduct
          pcf_type: MQCFST
          type_hint: str
        - name: RemoteVersion
          pcf_type: MQCFST
          type_hint: str
        - name: RemoteQMgrName
          pcf_type: MQCFST
          type_hint: str
        - name: ShortRetriesLeft
          pcf_type: MQCFIN
          type_hint: int
        - name: SecurityProtocol
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSECPROT_NONE
            - MQSECPROT_SSLV30
            - MQSECPROT_TLSV10
            - MQSECPROT_TLSV12
            - MQSECPROT_TLSV13
        - name: SSLCertRemoteIssuerName
          pcf_type: MQCFST
          type_hint: str
        - name: SSLCertUserId
          pcf_type: MQCFST
          type_hint: str
        - name: SSLCipherSpecification
          pcf_type: MQCFST
          type_hint: str
        - name: SSLKeyResetDate
          pcf_type: MQCFST
          type_hint: str
        - name: SSLKeyResets
          pcf_type: MQCFIN
          type_hint: int
        - name: SSLKeyResetTime
          pcf_type: MQCFST
          type_hint: str
        - name: SSLShortPeerName
          pcf_type: MQCFST
          type_hint: str
        - name: StopRequested
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHSR_STOP_NOT_REQUESTED
            - MQCHSR_STOP_REQUESTED
        - name: SubState
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHSSTATE_CHADEXIT
            - MQCHSSTATE_COMPRESSING
            - MQCHSSTATE_END_OF_BATCH
            - MQCHSSTATE_HANDSHAKING
            - MQCHSSTATE_HEARTBEATING
            - MQCHSSTATE_IN_MQGET
            - MQCHSSTATE_IN_MQI_CALL
            - MQCHSSTATE_IN_MQPUT
            - MQCHSSTATE_MREXIT
            - MQCHSSTATE_MSGEXIT
            - MQCHSSTATE_NAME_SERVER
            - MQCHSSTATE_NET_CONNECTING
            - MQCHSSTATE_OTHER
            - MQCHSSTATE_RCVEXIT
            - MQCHSSTATE_RECEIVING
            - MQCHSSTATE_RESYNCHING
            - MQCHSSTATE_SCYEXIT
            - MQCHSSTATE_SENDEXIT
            - MQCHSSTATE_SENDING
            - MQCHSSTATE_SERIALIZING
        - name: XmitQName
          pcf_type: MQCFST
          type_hint: str
        - name: XQTime
          pcf_type: MQCFIL
          type_hint: int
    notes:
      - display-chstatus-output-derived-from-pcf-response
  - mqsc:
      name: PING CHANNEL
      href: SSFKSJ_9.4.0/refadmin/q086430_.html
      positional_parameters:
        - (channel-name)
      input_parameters:
        - CMDSCOPE
        - CHLDISP
        - DATALEN
      output_parameters:
        []
      section_sources:
        'Parameter descriptions for PING CHANNEL':
          - CMDSCOPE
          - CHLDISP
          - DATALEN
    pcf:
      command: MQCMD_PING_CHANNEL
      request_href: SSFKSJ_9.4.0/refadmin/q088190_.html
      response_href: SSFKSJ_9.4.0/refadmin/q088190_.html
      request_parameters:
        - name: ChannelName
          pcf_type: MQCFST
          type_hint: str
        - name: DataCount
          pcf_type: MQCFIN
          type_hint: int
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: ChannelDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHLD_PRIVATE
            - MQCHLD_SHARED
            - MQCHLD_FIXSHARED
      response_parameters:
        []
    notes:
      []
  - mqsc:
      name: RESET CHANNEL
      href: SSFKSJ_9.4.0/refadmin/q086510_.html
      positional_parameters:
        - (channel-name)
      input_parameters:
        - CHLDISP
        - CMDSCOPE
        - SEQNUM
      output_parameters:
        []
      section_sources:
        'Parameter descriptions for RESET CHANNEL':
          - CHLDISP
          - CMDSCOPE
          - SEQNUM
    pcf:
      command: MQCMD_RESET_CHANNEL
      request_href: SSFKSJ_9.4.0/refadmin/q088270_.html
      response_href: SSFKSJ_9.4.0/refadmin/q088270_.html
      request_parameters:
        - name: ChannelName
          pcf_type: MQCFST
          type_hint: str
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: ChannelDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHLD_PRIVATE
            - MQCHLD_SHARED
        - name: MsgSeqNumber
          pcf_type: MQCFIN
          type_hint: int
      response_parameters:
        []
    notes:
      []
  - mqsc:
      name: START CHANNEL
      href: SSFKSJ_9.4.0/refadmin/q086660_.html
      positional_parameters:
        - (channel-name)
      input_parameters:
        - CHLDISP
        - CMDSCOPE
        - IGNSTATE
      output_parameters:
        []
      section_sources:
        'Parameter descriptions for START CHANNEL':
          - CHLDISP
          - CMDSCOPE
          - IGNSTATE
    pcf:
      command: MQCMD_START_CHANNEL
      request_href: SSFKSJ_9.4.0/refadmin/q088420_.html
      response_href: SSFKSJ_9.4.0/refadmin/q088430_.html
      request_parameters:
        - name: ChannelName
          pcf_type: MQCFST
          type_hint: str
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: ChannelDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHLD_PRIVATE
            - MQCHLD_SHARED
            - MQCHLD_FIXSHARED
        - name: IgnoreState
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQIS_NO
            - MQIS_YES
      response_parameters:
        - name: ChannelName
          pcf_type: MQCFST
          type_hint: str
        - name: ChannelType
          pcf_type: MQCFIN
          type_hint: int
    notes:
      - ignore-state-type-inferred-from-mqsc-ignstate
      - ignore-state-name-normalized
  - mqsc:
      name: STOP CHANNEL
      href: SSFKSJ_9.4.0/refadmin/q086750_.html
      positional_parameters:
        - (channel-name)
      input_parameters:
        - CHLDISP
        - CMDSCOPE
        - CONNAME
        - MODE
        - QMNAME
        - STATUS
        - IGNSTATE
      output_parameters:
        []
      section_sources:
        'Parameter descriptions for STOP CHANNEL':
          - CHLDISP
          - CMDSCOPE
          - CONNAME
          - MODE
          - QMNAME
          - STATUS
          - IGNSTATE
    pcf:
      command: MQCMD_STOP_CHANNEL
      request_href: SSFKSJ_9.4.0/refadmin/q088480_.html
      response_href: SSFKSJ_9.4.0/refadmin/q088490_.html
      request_parameters:
        - name: ChannelName
          pcf_type: MQCFST
          type_hint: str
        - name: ChannelDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHLD_PRIVATE
            - MQCHLD_SHARED
        - name: ChannelStatus
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHS_INACTIVE
            - MQCHS_STOPPED
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: ConnectionName
          pcf_type: MQCFST
          type_hint: str
        - name: Mode
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQMODE_QUIESCE
            - MQMODE_FORCE
            - MQMODE_TERMINATE
        - name: QMgrName
          pcf_type: MQCFST
          type_hint: str
        - name: IgnoreState
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQIS_NO
            - MQIS_YES
      response_parameters:
        - name: ChannelName
          pcf_type: MQCFST
          type_hint: str
        - name: ChannelType
          pcf_type: MQCFIN
          type_hint: int
        - name: ClientIdentifier
          pcf_type: MQCFST
          type_hint: str
    notes:
      - ignore-state-type-inferred-from-mqsc-ignstate
      - ignore-state-name-normalized
```

## Output-parameter refresh

```yaml
version: 1
generated_at: 2026-02-02T19:46:59Z
commands:
  - name: DISPLAY CHANNEL
    output_parameters:
      - AFFINITY
      - ALTDATE
      - ALTTIME
      - AMQPKA
      - AUTOSTART
      - BATCHHB
      - BATCHINT
      - BATCHLIM
      - BATCHSZ
      - CERTLABL
      - CHLTYPE
      - CLNTWGHT
      - CLUSNL
      - CLUSTER
      - CLWLPRTY
      - CLWLRANK
      - CLWLWGHT
      - COMPHDR
      - COMPMSG
      - CONNAME
      - CONVERT
      - DEFCDISP
      - DEFRECON
      - DESCR
      - DISCINT
      - HBINT
      - KAINT
      - LOCLADDR
      - LONGRTY
      - LONGTMR
      - MAXINST
      - MAXINSTC
      - MAXMSGL
      - MCANAME
      - MCATYPE
      - MCAUSER
      - MODENAME
      - MONCHL
      - MRDATA
      - MREXIT
      - MRRTY
      - MRTMR
      - MSGDATA
      - MSGEXIT
      - NETPRTY
      - NPMSPEED
      - PASSWORD
      - PORT
      - PROPCTL
      - PUTAUT
      - QMNAME
      - RCVDATA
      - RCVEXIT
      - RESETSEQ
      - SCYDATA
      - SCYEXIT
      - SENDDATA
      - SENDEXIT
      - SEQWRAP
      - SHARECNV
      - SHORTRTY
      - SHORTTMR
      - SPLPROT
      - SSLCAUTH
      - SSLCIPH
      - SSLPEER
      - STATCHL
      - TPNAME
      - TPROOT
      - TRPTYPE
      - TYPE
      - USECLTID
      - USEDLQ
      - USERID
      - XMITQ
  - name: DISPLAY CHSTATUS
    output_parameters:
      - AMQPKA
      - BATCHES
      - BATCHSZ
      - BUFSRCVD
      - BUFSSENT
      - BYTSRCVD
      - BYTSSENT
      - CHLTYPE
      - CHSTADA
      - CHSTATI
      - COMPHDR
      - COMPMSG
      - COMPRATE
      - COMPTIME
      - CURLUWID
      - CURMSGS
      - CURSEQNO
      - CURSHCNV
      - EXITTIME
      - HBINT
      - INDOUBT
      - JOBNAME
      - KAINT
      - LOCLADDR
      - LONGRTS
      - LSTLUWID
      - LSTMSGDA
      - LSTMSGTI
      - LSTSEQNO
      - MAXMSGL
      - MAXSHCNV
      - MCASTAT
      - MCAUSER
      - MONCHL
      - MONITOR
      - MSGS
      - NETTIME
      - NPMSPEED
      - PORT
      - QMNAME
      - RAPPLTAG
      - RPRODUCT
      - RQMNAME
      - RVERSION
      - SECPROT
      - SHARECNV
      - SHORTRTS
      - SSLCERTI
      - SSLCERTU
      - SSLCIPH
      - SSLKEYDA
      - SSLKEYTI
      - SSLPEER
      - SSLRKEYS
      - STATCHL
      - STATUS
      - STOPREQ
      - SUBSTATE
      - TPROOT
      - USECLTID
      - XBATCHSZ
      - XQMSGSA
      - XQTIME
```
