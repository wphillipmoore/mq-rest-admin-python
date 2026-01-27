# Command metadata (first run)

## Table of Contents
- [Purpose](#purpose)
- [Sources](#sources)
- [Summary](#summary)
- [Metadata output](#metadata-output)
- [Notes and gaps](#notes-and-gaps)

## Purpose
Capture command-specific MQSC and PCF metadata without cross-namespace mapping.

## Sources
- MQSC commands index: https://www.ibm.com/docs/en/ibm-mq/9.4.x?topic=reference-mqsc-commands
- PCF commands index: https://www.ibm.com/docs/en/ibm-mq/9.4.x?topic=reference-definitions-programmable-command-formats
- IBM Docs content API: https://www.ibm.com/docs/api/v1/content

## Summary
- Output refresh updated: 2026-01-27T20:30:57Z
- MQSC commands parsed: 139
- MQSC docs fetched: 139
- MQSC commands with input parameters: 133
- MQSC commands with output parameters: 42
- PCF commands parsed: 105
- PCF request pages fetched: 105
- PCF response pages fetched: 105
- PCF response pages missing: 0

## Metadata output
```yaml
version: 1
generated_at: 2026-01-12T13:07:15Z
mqsc_commands:
  - name: ALTER AUTHINFO
    href: SSFKSJ_9.4.0/refadmin/q085140_.html
    positional_parameters:
      - LDAP class user
      - LDAP password
      - LDAP user
      - Responder URL
      - base DN
      - connection name
      - delay time
      - name
      - qmgr-name
      - string
      - user field
      - user name
    parameters:
      - ADOPTCTX
      - AUTHENMD
      - AUTHORMD
      - AUTHTYPE
      - BASEDNG
      - BASEDNU
      - BASEDNU(base DN)
      - CHCKCLNT
      - CHCKLOCL
      - CLASSGRP
      - CLASSUSR
      - CLASSUSR(LDAP class user)
      - CMDSCOPE
      - CONNAME
      - CONNAME(connection name)
      - DESCR
      - DESCR(string)
      - FAILDLAY
      - FAILDLAY(delay time)
      - FINDGRP
      - GRPFIELD
      - LDAPPWD
      - LDAPPWD(LDAP password)
      - LDAPUSER
      - LDAPUSER(LDAP user)
      - NESTGRP
      - OCSPURL
      - OCSPURL(Responder URL)
      - QSGDISP
      - SECCOMM
      - SHORTUSR
      - SHORTUSR(user name)
      - USRFIELD
      - USRFIELD(user field)
      - name
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: ALTER BUFFPOOL
    href: SSFKSJ_9.4.0/refadmin/q085150_.html
    positional_parameters:
      - (buf-pool-id)
      - integer
    parameters:
      - (buf-pool-id)
      - BUFFERS
      - BUFFERS(integer)
      - LOC
      - LOCATION
      - LOCATION or LOC(BELOW or ABOVE)
      - PAGECLAS
      - PAGECLAS(4KB or FIXED4KB)
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: ALTER CFSTRUCT
    href: SSFKSJ_9.4.0/refadmin/q085160_.html
    positional_parameters:
      - (structure-name)
      - data.set.name.*
      - integer
      - string
    parameters:
      - (structure-name)
      - CFCONLOS
      - CFLEVEL
      - CFLEVEL(integer)
      - DESCR
      - DESCR(string)
      - DSBLOCK
      - DSBUFS
      - DSEXPAND
      - DSGROUP
      - OFFLD1SZ
      - OFFLD1TH
      - OFFLD1TH(percentage) OFFLD1SZ(size)
      - OFFLD2SZ
      - OFFLD2TH
      - OFFLD2TH(percentage) OFFLD2SZ(size)
      - OFFLD3SZ
      - OFFLD3TH
      - OFFLD3TH(percentage) OFFLD3SZ(size)
      - OFFLOAD
      - RECAUTO
      - RECOVER
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: ALTER CHANNEL
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
    parameters:
      - (channel-name)
      - AFFINITY
      - AMQP: LOCLADDR(ip-addr)
      - AMQPKA
      - AMQPKA(integer)
      - BATCHHB
      - BATCHHB(integer)
      - BATCHINT
      - BATCHINT(integer)
      - BATCHLIM
      - BATCHLIM(integer)
      - BATCHSZ
      - BATCHSZ(integer)
      - CERTLABL
      - CHLTYPE
      - CLNTWGHT
      - CLUSNL
      - CLUSNL(nlname)
      - CLUSTER
      - CLUSTER(clustername)
      - CLWLPRTY
      - CLWLPRTY(integer)
      - CLWLRANK
      - CLWLRANK(integer)
      - CLWLWGHT
      - CLWLWGHT(integer)
      - CMDSCOPE
      - COMPHDR
      - COMPMSG
      - CONNAME
      - CONNAME(string)
      - CONVERT
      - DEFCDISP
      - DEFRECON
      - DESCR
      - DESCR(string)
      - DISCINT
      - DISCINT(integer)
      - HBINT
      - HBINT(integer)
      - KAINT
      - KAINT(integer)
      - LIKE
      - LIKE(channel-name)
      - LOCLADDR
      - LOCLADDR(string)
      - LONGRTY
      - LONGRTY(integer)
      - LONGTMR
      - LONGTMR(integer)
      - MAXINST
      - MAXINST(integer)
      - MAXINSTC
      - MAXINSTC(integer)
      - MAXMSGL
      - MAXMSGL(integer)
      - MCANAME
      - MCANAME(string)
      - MCATYPE
      - MCAUSER
      - MCAUSER(string)
      - MODENAME
      - MODENAME(string)
      - MONCHL
      - MRDATA
      - MRDATA(string)
      - MREXIT
      - MREXIT(string)
      - MRRTY
      - MRRTY(integer)
      - MRTMR
      - MRTMR(integer)
      - MSGDATA
      - MSGDATA(string)
      - MSGEXIT
      - MSGEXIT(string)
      - NETPRTY
      - NETPRTY(integer)
      - NPMSPEED
      - PASSWORD
      - PASSWORD(string)
      - PORT
      - PORT(integer)
      - PROPCTL
      - PUTAUT
      - QMNAME
      - QMNAME(string)
      - QSGDISP
      - RCVDATA
      - RCVDATA(string)
      - RCVEXIT
      - RCVEXIT(string)
      - SCYDATA
      - SCYDATA(string)
      - SCYEXIT
      - SCYEXIT(string)
      - SENDDATA
      - SENDDATA(string)
      - SENDEXIT
      - SENDEXIT(string)
      - SEQWRAP
      - SEQWRAP(integer)
      - SHARECNV
      - SHARECNV(integer)
      - SHORTRTY
      - SHORTRTY(integer)
      - SHORTTMR
      - SHORTTMR(integer)
      - SPLPROT
      - SSLCAUTH
      - SSLCIPH
      - SSLCIPH(string)
      - SSLPEER
      - SSLPEER(string)
      - STATCHL
      - TMPMODEL
      - TMPMODEL(string)
      - TMPQPRFX
      - TMPQPRFX(string)
      - TPNAME
      - TPNAME(string)
      - TPROOT
      - TRPTYPE
      - USECLTID
      - USEDLQ
      - USERID
      - USERID(string)
      - XMITQ
      - XMITQ(string)
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: ALTER COMMINFO
    href: SSFKSJ_9.4.0/refadmin/q085270_.html
    positional_parameters:
      - (comminfo name)
      - integer
      - string
    parameters:
      - (comminfo name)
      - BRIDGE
      - CCSID
      - CCSID(integer)
      - COMMEV
      - DESCR
      - DESCR(string)
      - ENCODING
      - GRPADDR
      - MCHBINT
      - MCPROP
      - MONINT
      - MONINT( integer )
      - MSGHIST
      - NSUBHIST
      - PORT
      - PORT(integer)
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: ALTER LISTENER
    href: SSFKSJ_9.4.0/refadmin/q085280_.html
    positional_parameters:
      - (listener-name)
      - integer
      - listener-name
      - string
    parameters:
      - (listener-name)
      - ADAPTER
      - ADAPTER(integer)
      - BACKLOG
      - BACKLOG(integer)
      - COMMANDS
      - COMMANDS(integer)
      - CONTROL
      - CONTROL(string)
      - DESCR
      - DESCR(string)
      - IPADDR
      - IPADDR(string)
      - LIKE
      - LIKE(listener-name)
      - LOCLNAME
      - LOCLNAME(string)
      - NTBNAMES
      - NTBNAMES(integer)
      - PORT
      - PORT(integer)
      - SESSIONS
      - SESSIONS(integer)
      - SOCKET
      - SOCKET(integer)
      - TPNAME
      - TPNAME(string)
      - TRPTYPE
      - TRPTYPE( string )
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: ALTER NAMELIST
    href: SSFKSJ_9.4.0/refadmin/q085290_.html
    positional_parameters:
      - (name)
      - name, ...
      - qmgr-name
      - string
    parameters:
      - (name)
      - CMDSCOPE
      - DESCR
      - DESCR(string)
      - NAMES
      - NAMES(name, ...)
      - NLTYPE
      - QSGDISP
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: ALTER PROCESS
    href: SSFKSJ_9.4.0/refadmin/q085300_.html
    positional_parameters:
      - process-name
      - qmgr-name
      - string
    parameters:
      - APPLICID
      - APPLICID(string)
      - APPLTYPE
      - APPLTYPE(string)
      - CMDSCOPE
      - DESCR
      - DESCR(string)
      - ENVRDATA
      - ENVRDATA(string)
      - QSGDISP
      - USERDATA
      - USERDATA(string)
      - process-name
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: ALTER PSID
    href: SSFKSJ_9.4.0/refadmin/q085310_.html
    positional_parameters:
      - (psid-number)
    parameters:
      - (psid-number)
      - EXPAND
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: ALTER QMGR
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
    parameters:
      - FORCE
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: ALTER SECURITY
    href: SSFKSJ_9.4.0/refadmin/q085380_.html
    positional_parameters:
      - integer
      - qmgr-name
    parameters:
      - CMDSCOPE
      - INTERVAL
      - INTERVAL(integer)
      - TIMEOUT
      - TIMEOUT(integer)
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: ALTER SERVICE
    href: SSFKSJ_9.4.0/refadmin/q085390_.html
    positional_parameters:
      - (service-name)
      - service-name
      - string
    parameters:
      - (service-name)
      - CONTROL
      - CONTROL(string)
      - DESCR
      - DESCR(string)
      - LIKE
      - LIKE(service-name)
      - NOREPLACE
      - REPLACE
      - REPLACE and NOREPLACE
      - SERVTYPE
      - STARTARG
      - STARTARG(string)
      - STARTCMD
      - STARTCMD(string)
      - STDERR
      - STDERR(string)
      - STDOUT
      - STDOUT(string)
      - STOPARG
      - STOPARG(string)
      - STOPCMD
      - STOPCMD(string)
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: ALTER SMDS
    href: SSFKSJ_9.4.0/refadmin/q085400_.html
    positional_parameters:
      - qmgr-name
      - structure-name
    parameters:
      - CFSTRUCT
      - CFSTRUCT(structure-name)
      - DSBUFS
      - DSBUFS(number|DEFAULT)
      - DSEXPAND
      - DSEXPAND(YES|NO|DEFAULT)
      - SMDS
      - SMDS(qmgr-name|*)
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: ALTER STGCLASS
    href: SSFKSJ_9.4.0/refadmin/q085410_.html
    positional_parameters:
      - (storage-class)
      - application name
      - description
      - group name
      - integer
      - member name
      - qmgr-name
    parameters:
      - (storage-class)
      - CMDSCOPE
      - DESCR
      - DESCR(description)
      - PASSTKTA
      - PASSTKTA(application name)
      - PSID
      - PSID(integer)
      - QSGDISP
      - XCFGNAME
      - XCFGNAME(group name)
      - XCFMNAME
      - XCFMNAME(member name)
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: ALTER SUB
    href: SSFKSJ_9.4.0/refadmin/q085420_.html
    positional_parameters:
      - integer
      - qmgr-name
      - string
    parameters:
      - (string)
      - CMDSCOPE
      - DEST
      - DEST(string)
      - DESTCORL
      - DESTCORL(string)
      - DESTQMGR
      - DESTQMGR(string)
      - EXPIRY
      - PSPROP
      - PUBACCT
      - PUBACCT(string)
      - PUBAPPID
      - PUBAPPID(string)
      - PUBPRTY
      - REQONLY
      - SUBUSER
      - SUBUSER(string)
      - USERDATA
      - USERDATA(string)
      - VARUSER
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: ALTER TOPIC
    href: SSFKSJ_9.4.0/refadmin/q085430_.html
    positional_parameters:
      - (topic-name)
      - comminfo-name
      - integer
      - qmgr-name
      - string
    parameters:
      - (topic-name)
      - CAPEXPRY
      - CAPEXPRY(integer)
      - CLROUTE
      - CLUSTER
      - CMDSCOPE
      - COMMINFO
      - COMMINFO(comminfo-name)
      - CUSTOM
      - CUSTOM(string)
      - DEFPRESP
      - DEFPRTY
      - DEFPRTY(integer)
      - DEFPSIST
      - DESCR
      - DESCR(string)
      - DURSUB
      - MCAST
      - MDURMDL
      - MDURMDL(string)
      - MNDURMDL
      - MNDURMDL(string)
      - NPMSGDLV
      - PMSGDLV
      - PROXYSUB
      - PUB
      - PUBSCOPE
      - QSGDISP
      - SUB
      - SUBSCOPE
      - TOPICSTR
      - TOPICSTR( string )
      - TYPE
      - TYPE (topic-type)
      - USEDLQ
      - WILDCARD
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: ALTER TRACE
    href: SSFKSJ_9.4.0/refadmin/q085440_.html
    positional_parameters:
      - ifcid
      - integer
      - string
    parameters:
      - ACCTG
      - CMDSCOPE
      - GLOBAL
      - STAT
      - TNO
      - TNO( integer )
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: ARCHIVE LOG
    href: SSFKSJ_9.4.0/refadmin/q085450_.html
    positional_parameters:
      - nnn
      - qmgr-name
    parameters:
      - CANCEL OFFLOAD
      - CMDSCOPE
      - MODE(QUIESCE)
      - TIME
      - TIME( nnn )
      - WAIT
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: BACKUP CFSTRUCT
    href: SSFKSJ_9.4.0/refadmin/q085460_.html
    positional_parameters:
      - integer
      - structure-name
    parameters:
      - CMDSCOPE
      - EXCLINT
      - EXCLINT( integer )
      - structure-name
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: CLEAR QLOCAL
    href: SSFKSJ_9.4.0/refadmin/q085470_.html
    positional_parameters:
      - (q-name)
    parameters:
      - (q-name)
      - CMDSCOPE
      - QSGDISP
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: CLEAR TOPICSTR
    href: SSFKSJ_9.4.0/refadmin/q085480_.html
    positional_parameters:
      - (topic-string)
      - qmgr-name
    parameters:
      - (topic-string)
      - CLRTYPE
      - CMDSCOPE
      - SCOPE
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: DEFINE AUTHINFO
    href: SSFKSJ_9.4.0/refadmin/q085490_.html
    positional_parameters:
      - LDAP class name
      - LDAP field name
      - LDAP password
      - LDAP user
      - Responder URL
      - authinfo-name
      - base DN
      - connection name
      - delay time
      - name
      - qmgr-name
      - string
      - user name
    parameters:
      - ADOPTCTX
      - AUTHENMD
      - AUTHORMD
      - AUTHTYPE
      - BASEDNG
      - BASEDNU
      - BASEDNU(base DN)
      - CHCKCLNT
      - CHCKLOCL
      - CLASSGRP
      - CLASSUSR
      - CLASSUSR( LDAP class name )
      - CMDSCOPE
      - CONNAME
      - CONNAME(connection name)
      - DESCR
      - DESCR(string)
      - FAILDLAY
      - FAILDLAY(delay time)
      - FINDGRP
      - GRPFIELD
      - LDAPPWD
      - LDAPPWD(LDAP password)
      - LDAPUSER
      - LDAPUSER(LDAP user)
      - LIKE
      - LIKE(authinfo-name)
      - NESTGRP
      - NOREPLACE
      - OCSPURL
      - OCSPURL(Responder URL)
      - QSGDISP
      - REPLACE
      - REPLACE and NOREPLACE
      - SECCOMM
      - SHORTUSR
      - SHORTUSR(user name)
      - USRFIELD
      - USRFIELD( LDAP field name )
      - name
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: DEFINE BUFFPOOL
    href: SSFKSJ_9.4.0/refadmin/q085500_.html
    positional_parameters:
      - (buf-pool-id)
      - 4KB
      - ABOVE
      - BELOW
      - FIXED4KB
      - integer
    parameters:
      - (buf-pool-id)
      - BUFFERS
      - BUFFERS( integer )
      - LOC
      - LOCATION
      - LOCATION(LOC)(BELOW or ABOVE)
      - NOREPLACE
      - PAGECLAS
      - PAGECLAS( 4KB or FIXED4KB )
      - REPLACE
      - REPLACE/NOREPLACE
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: DEFINE CFSTRUCT
    href: SSFKSJ_9.4.0/refadmin/q085510_.html
    positional_parameters:
      - (structure-name)
      - cfstruct-name
      - dsname.prefix.*.dsname.suffix
      - integer
      - percentage
      - size
      - string
    parameters:
      - (structure-name)
      - CFCONLOS
      - CFLEVEL
      - CFLEVEL( integer )
      - DESCR
      - DESCR( string )
      - DSBLOCK
      - DSBUFS
      - DSEXPAND
      - DSGROUP
      - LIKE
      - LIKE(cfstruct-name)
      - NOREPLACE
      - OFFLD1SZ
      - OFFLD1TH
      - OFFLD1TH(percentage) OFFLD1SZ(size)
      - OFFLD2SZ
      - OFFLD2TH
      - OFFLD2TH(percentage) OFFLD2SZ(size)
      - OFFLD3SZ
      - OFFLD3TH
      - OFFLD3TH(percentage) OFFLD3SZ(size)
      - OFFLOAD
      - RECAUTO
      - RECOVER
      - REPLACE
      - REPLACE and NOREPLACE
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: DEFINE CHANNEL
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
    parameters:
      - (channel-name)
      - AFFINITY
      - AMQP: LOCLADDR(ip-addr)
      - AMQPKA
      - AMQPKA(integer)
      - BATCHHB
      - BATCHHB(integer)
      - BATCHINT
      - BATCHINT(integer)
      - BATCHLIM
      - BATCHLIM(integer)
      - BATCHSZ
      - BATCHSZ(integer)
      - CERTLABL
      - CHLTYPE
      - CLNTWGHT
      - CLUSNL
      - CLUSNL(nlname)
      - CLUSTER
      - CLUSTER(clustername)
      - CLWLPRTY
      - CLWLPRTY(integer)
      - CLWLRANK
      - CLWLRANK(integer)
      - CLWLWGHT
      - CLWLWGHT(integer)
      - CMDSCOPE
      - COMPHDR
      - COMPMSG
      - CONNAME
      - CONNAME(string)
      - CONVERT
      - DEFCDISP
      - DEFRECON
      - DESCR
      - DESCR(string)
      - DISCINT
      - DISCINT(integer)
      - HBINT
      - HBINT(integer)
      - KAINT
      - KAINT(integer)
      - LIKE
      - LIKE(channel-name)
      - LOCLADDR
      - LOCLADDR(string)
      - LONGRTY
      - LONGRTY(integer)
      - LONGTMR
      - LONGTMR(integer)
      - MAXINST
      - MAXINST(integer)
      - MAXINSTC
      - MAXINSTC(integer)
      - MAXMSGL
      - MAXMSGL(integer)
      - MCANAME
      - MCANAME(string)
      - MCATYPE
      - MCAUSER
      - MCAUSER(string)
      - MODENAME
      - MODENAME(string)
      - MONCHL
      - MRDATA
      - MRDATA(string)
      - MREXIT
      - MREXIT(string)
      - MRRTY
      - MRRTY(integer)
      - MRTMR
      - MRTMR(integer)
      - MSGDATA
      - MSGDATA(string)
      - MSGEXIT
      - MSGEXIT(string)
      - NETPRTY
      - NETPRTY(integer)
      - NOREPLACE
      - NPMSPEED
      - PASSWORD
      - PASSWORD(string)
      - PORT
      - PORT(integer)
      - PROPCTL
      - PUTAUT
      - QMNAME
      - QMNAME(string)
      - QSGDISP
      - RCVDATA
      - RCVDATA(string)
      - RCVEXIT
      - RCVEXIT(string)
      - REPLACE
      - REPLACE and NOREPLACE
      - SCYDATA
      - SCYDATA(string)
      - SCYEXIT
      - SCYEXIT(string)
      - SENDDATA
      - SENDDATA(string)
      - SENDEXIT
      - SENDEXIT(string)
      - SEQWRAP
      - SEQWRAP(integer)
      - SHARECNV
      - SHARECNV(integer)
      - SHORTRTY
      - SHORTRTY(integer)
      - SHORTTMR
      - SHORTTMR(integer)
      - SPLPROT
      - SSLCAUTH
      - SSLCIPH
      - SSLCIPH(string)
      - SSLPEER
      - SSLPEER (string)
      - STATCHL
      - TMPMODEL
      - TMPMODEL(string)
      - TMPQPRFX
      - TMPQPRFX(string?
      - TPNAME
      - TPNAME(string)
      - TPROOT
      - TRPTYPE
      - USECLTID
      - USEDLQ
      - USERID
      - USERID(string)
      - XMITQ
      - XMITQ(string)
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: DEFINE COMMINFO
    href: SSFKSJ_9.4.0/refadmin/q085620_.html
    positional_parameters:
      - authinfo-name
      - comminfo name
      - integer
      - string
    parameters:
      - (comminfo name)
      - BRIDGE
      - CCSID
      - CCSID( integer )
      - COMMEV
      - DESCR
      - DESCR( string )
      - ENCODING
      - GRPADDR
      - LIKE
      - LIKE( authinfo-name )
      - MCHBINT
      - MCPROP
      - MONINT
      - MONINT( integer )
      - MSGHIST
      - NOREPLACE
      - NSUBHIST
      - PORT
      - PORT(integer)
      - REPLACE
      - REPLACE and NOREPLACE
      - TYPE
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: DEFINE LISTENER
    href: SSFKSJ_9.4.0/refadmin/q085630_.html
    positional_parameters:
      - (listener-name)
      - integer
      - listener-name
      - string
    parameters:
      - (listener-name)
      - ADAPTER
      - ADAPTER(integer)
      - BACKLOG
      - BACKLOG(integer)
      - COMMANDS
      - COMMANDS(integer)
      - CONTROL
      - CONTROL(string)
      - DESCR
      - DESCR(string)
      - IPADDR
      - IPADDR(string)
      - LIKE
      - LIKE(listener-name)
      - LOCLNAME
      - LOCLNAME(string)
      - NTBNAMES
      - NTBNAMES(integer)
      - PORT
      - PORT(integer)
      - SESSIONS
      - SESSIONS(integer)
      - SOCKET
      - SOCKET(integer)
      - TPNAME
      - TPNAME(string)
      - TRPTYPE
      - TRPTYPE( string )
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: DEFINE LOG
    href: SSFKSJ_9.4.0/refadmin/q085640_.html
    positional_parameters:
      - name
      - qmgr-name
    parameters:
      - (name)
      - CMDSCOPE
      - COPY
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: DEFINE MAXSMSGS
    href: SSFKSJ_9.4.0/refadmin/q085650_.html
    positional_parameters:
      - integer
      - qmgr-name
    parameters:
      - (integer)
      - CMDSCOPE
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: DEFINE NAMELIST
    href: SSFKSJ_9.4.0/refadmin/q085660_.html
    positional_parameters:
      - name
      - name, ...
      - namelist-name
      - qmgr-name
      - string
    parameters:
      - (name)
      - CMDSCOPE
      - DESCR
      - DESCR(string)
      - LIKE
      - LIKE(namelist-name)
      - NAMES
      - NAMES(name, ...)
      - NLTYPE
      - NOREPLACE
      - QSGDISP
      - REPLACE
      - REPLACE and NOREPLACE
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: DEFINE PROCESS
    href: SSFKSJ_9.4.0/refadmin/q085670_.html
    positional_parameters:
      - integer
      - process-name
      - qmgr-name
      - string
    parameters:
      - (process-name)
      - APPLICID
      - APPLICID( string )
      - APPLTYPE
      - APPLTYPE( string )
      - CMDSCOPE
      - DESCR
      - DESCR( string )
      - ENVRDATA
      - ENVRDATA( string )
      - LIKE
      - LIKE( process-name )
      - NOREPLACE
      - QSGDISP
      - REPLACE
      - REPLACE and NOREPLACE
      - USERDATA
      - USERDATA( string )
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: DEFINE PSID
    href: SSFKSJ_9.4.0/refadmin/q085680_.html
    positional_parameters:
      - data set name
      - integer
      - psid-number
    parameters:
      - (psid-number)
      - BUFFPOOL
      - BUFFPOOL( integer )
      - DSN
      - DSN( data set name )
      - EXPAND
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: DEFINE SERVICE
    href: SSFKSJ_9.4.0/refadmin/q085740_.html
    positional_parameters:
      - (service-name)
      - service-name
      - string
    parameters:
      - (service-name)
      - CONTROL
      - CONTROL(string)
      - DESCR
      - DESCR(string)
      - LIKE
      - LIKE(service-name)
      - NOREPLACE
      - REPLACE
      - REPLACE and NOREPLACE
      - SERVTYPE
      - STARTARG
      - STARTARG(string)
      - STARTCMD
      - STARTCMD(string)
      - STDERR
      - STDERR(string)
      - STDOUT
      - STDOUT(string)
      - STOPARG
      - STOPARG(string)
      - STOPCMD
      - STOPCMD(string)
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: DEFINE STGCLASS
    href: SSFKSJ_9.4.0/refadmin/q085750_.html
    positional_parameters:
      - application name
      - description
      - group name
      - integer
      - member name
      - qmgr-name
      - stgclass-name
      - storage-class
    parameters:
      - (storage-class)
      - CMDSCOPE
      - DESCR
      - DESCR(description)
      - LIKE
      - LIKE(stgclass-name)
      - NOREPLACE
      - PASSTKTA
      - PASSTKTA(application name)
      - PSID
      - PSID(integer)
      - QSGDISP
      - REPLACE
      - REPLACE and NOREPLACE
      - XCFGNAME
      - XCFGNAME( group name )
      - XCFMNAME
      - XCFMNAME( member name )
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: DEFINE SUB
    href: SSFKSJ_9.4.0/refadmin/q085760_.html
    positional_parameters:
      - integer
      - qmgr-name
      - string
      - subscription-name
    parameters:
      - (string)
      - CMDSCOPE
      - DEST
      - DEST(string)
      - DESTCLAS
      - DESTCORL
      - DESTCORL(string)
      - DESTQMGR
      - DESTQMGR(string)
      - EXPIRY
      - LIKE
      - LIKE(subscription-name)
      - NOREPLACE
      - PSPROP
      - PUBACCT
      - PUBACCT(string)
      - PUBAPPID
      - PUBAPPID(string)
      - PUBPRTY
      - REPLACE
      - REPLACE and NOREPLACE
      - REQONLY
      - SELECTOR
      - SELECTOR(string)
      - SUBLEVEL
      - SUBLEVEL(integer)
      - SUBNAME
      - SUBSCOPE
      - SUBUSER
      - SUBUSER(string)
      - TOPICOBJ
      - TOPICOBJ(string)
      - TOPICSTR
      - TOPICSTR(string)
      - USERDATA
      - USERDATA(string)
      - VARUSER
      - WSCHEMA
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: DEFINE TOPIC
    href: SSFKSJ_9.4.0/refadmin/q085770_.html
    positional_parameters:
      - comminfo-name
      - integer
      - string
      - topic-name
      - topic-type
    parameters:
      - (topic-name)
      - CAPEXPRY
      - CAPEXPRY(integer)
      - CLROUTE
      - CLUSTER
      - CMDSCOPE
      - COMMINFO
      - COMMINFO( comminfo-name )
      - CUSTOM
      - CUSTOM(string)
      - DEFPRESP
      - DEFPRTY
      - DEFPRTY( integer )
      - DEFPSIST
      - DESCR
      - DESCR( string )
      - DURSUB
      - LIKE
      - LIKE( topic-name )
      - MCAST
      - MDURMDL
      - MDURMDL(string)
      - MNDURMDL
      - MNDURMDL( string )
      - NOREPLACE
      - NPMSGDLV
      - PMSGDLV
      - PROXYSUB
      - PUB
      - PUBSCOPE
      - QSGDISP
      - REPLACE
      - REPLACE and NOREPLACE
      - SUB
      - SUBSCOPE
      - TOPICSTR
      - TOPICSTR(string)
      - TYPE
      - TYPE(topic-type)
      - USEDLQ
      - WILDCARD
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: DELETE AUTHINFO
    href: SSFKSJ_9.4.0/refadmin/q085780_.html
    positional_parameters:
      - name
      - qmgr-name
    parameters:
      - (name)
      - CMDSCOPE
      - IGNSTATE
      - QSGDISP
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: DELETE AUTHREC
    href: SSFKSJ_9.4.0/refadmin/q085790_.html
    positional_parameters:
      - group-name
      - principal-name
      - profile-name
    parameters:
      - GROUP
      - GROUP(group-name)
      - IGNSTATE
      - OBJTYPE
      - PRINCIPAL
      - PRINCIPAL(principal-name)
      - PROFILE
      - PROFILE(profile-name)
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: DELETE BUFFPOOL
    href: SSFKSJ_9.4.0/refadmin/q085800_.html
    positional_parameters:
      - integer
    parameters:
      - (integer)
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: DELETE CFSTRUCT
    href: SSFKSJ_9.4.0/refadmin/q085810_.html
    positional_parameters:
      - structure-name
    parameters:
      - (structure-name)
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: DELETE CHANNEL
    href: SSFKSJ_9.4.0/refadmin/q085820_.html
    positional_parameters:
      - channel-name
      - qmgr-name
    parameters:
      - (channel-name)
      - CHLTABLE
      - CMDSCOPE
      - IGNSTATE
      - QSGDISP
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: DELETE COMMINFO
    href: SSFKSJ_9.4.0/refadmin/q085840_.html
    positional_parameters:
      - comminfo_name
    parameters:
      - (comminfo_name)
      - IGNSTATE
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: DELETE LISTENER
    href: SSFKSJ_9.4.0/refadmin/q085850_.html
    positional_parameters:
      - listener-name
    parameters:
      - (listener-name)
      - IGNSTATE
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: DELETE NAMELIST
    href: SSFKSJ_9.4.0/refadmin/q085860_.html
    positional_parameters:
      - name
      - qmgr-name
    parameters:
      - (name)
      - CMDSCOPE
      - IGNSTATE
      - QSGDISP
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: DELETE POLICY
    href: SSFKSJ_9.4.0/refadmin/q120810_.html
    positional_parameters:
      - policy-name
    parameters:
      - (policy-name)
      - IGNSTATE
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: DELETE PROCESS
    href: SSFKSJ_9.4.0/refadmin/q085870_.html
    positional_parameters:
      - process-name
      - qmgr-name
    parameters:
      - (process-name)
      - CMDSCOPE
      - IGNSTATE
      - QSGDISP
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: DELETE PSID
    href: SSFKSJ_9.4.0/refadmin/q085880_.html
    positional_parameters:
      - psid-number
    parameters:
      - (psid-number)
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: DELETE SERVICE
    href: SSFKSJ_9.4.0/refadmin/q085940_.html
    positional_parameters:
      - service-name
    parameters:
      - (service-name)
      - IGNSTATE
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: DELETE STGCLASS
    href: SSFKSJ_9.4.0/refadmin/q085960_.html
    positional_parameters:
      - name
      - qmgr-name
    parameters:
      - (name)
      - CMDSCOPE
      - QSGDISP
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: DELETE SUB
    href: SSFKSJ_9.4.0/refadmin/q085950_.html
    positional_parameters:
      - qmgr-name
      - string
      - subscription-name
    parameters:
      - CMDSCOPE
      - IGNSTATE
      - SUBID
      - SUBID(string)
      - subscription-name
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: DELETE TOPIC
    href: SSFKSJ_9.4.0/refadmin/q085970_.html
    positional_parameters:
      - qmgr-name
      - topic-name
    parameters:
      - (topic-name)
      - AUTHREC
      - CMDSCOPE
      - IGNSTATE
      - QSGDISP
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: DISPLAY APSTATUS
    href: SSFKSJ_9.4.0/refadmin/q133100_.html
    positional_parameters:
      - applicationnamestr
      - value
    parameters:
      - ALL
      - TYPE
      - WHERE
      - applicationnamestr
    input_only: []
    output_only: []
    notes:
  - name: DISPLAY ARCHIVE
    href: SSFKSJ_9.4.0/refadmin/q085980_.html
    positional_parameters:
      - qmgr-name
    parameters:
      - CMDSCOPE
    input_only: []
    output_only: []
    notes:
  - name: DISPLAY AUTHINFO
    href: SSFKSJ_9.4.0/refadmin/q085990_.html
    positional_parameters:
      - generic-authentication-information-object-name
      - qmgr-name
    parameters:
      - (generic-authentication-information-object-name)
      - ADOPTCTX
      - ALL
      - ALTDATE
      - ALTTIME
      - AUTHENMD
      - AUTHORMD
      - AUTHTYPE
      - BASEDNG
      - BASEDNU
      - CHCKCLNT
      - CHCKLOCL
      - CLASSGRP
      - CLASSUSR
      - CMDSCOPE
      - CONNAME
      - DESCR
      - FAILDLAY
      - FINDGRP
      - GRPFIELD
      - LDAPPWD
      - LDAPUSER
      - NESTGRP
      - OCSPURL
      - QSGDISP
      - SECCOMM
      - SHORTUSR
      - USRFIELD
      - WHERE
    input_only:
      - CMDSCOPE
      - WHERE
    output_only:
      - ADOPTCTX
      - ALTDATE
      - ALTTIME
      - AUTHENMD
      - AUTHORMD
      - BASEDNG
      - BASEDNU
      - CHCKCLNT
      - CHCKLOCL
      - CLASSGRP
      - CLASSUSR
      - CONNAME
      - FAILDLAY
      - FINDGRP
      - GRPFIELD
      - LDAPPWD
      - LDAPUSER
      - NESTGRP
      - OCSPURL
      - SECCOMM
      - SHORTUSR
      - USRFIELD
    notes: []
  - name: DISPLAY AUTHREC
    href: SSFKSJ_9.4.0/refadmin/q086000_.html
    positional_parameters:
      - group-name
      - principal-name
      - profile-name
      - service-component
    parameters:
      - ALL
      - GROUP(group-name)
      - MATCH
      - OBJTYPE
      - PRINCIPAL(principal-name)
      - PROFILE(profile-name)
      - SERVCOMP(service-component)
    input_only: []
    output_only: []
    notes:
  - name: DISPLAY AUTHSERV
    href: SSFKSJ_9.4.0/refadmin/q086010_.html
    positional_parameters: []
    parameters:
      - ALL
    input_only: []
    output_only:
      - ALL
      - IFVER
      - SERVCOMP
      - UIDSUPP
    notes:
  - name: DISPLAY CFSTATUS
    href: SSFKSJ_9.4.0/refadmin/q086020_.html
    positional_parameters:
      - (date)
      - (generic-structure-name)
      - (hexadecimal)
      - (integer)
      - (qmgrname)
      - (qmgrname-list)
      - (size)
      - (systemname)
      - (time)
    parameters:
      - (generic-structure-name)
      - SMDS
      - TYPE
      - WHERE
    input_only: []
    output_only: []
    notes:
  - name: DISPLAY CFSTRUCT
    href: SSFKSJ_9.4.0/refadmin/q086030_.html
    positional_parameters:
      - generic-structure-name
    parameters:
      - ( generic-structure-name )
      - ALL
      - WHERE
    input_only:
      - DESCR
      - RECOVER
    output_only:
      - ALL
      - CFLEVEL
      - OFFLD1SZ
      - OFFLD1TH
      - OFFLD2SZ
      - OFFLD2TH
      - OFFLD3SZ
      - OFFLD3TH
    notes:
  - name: DISPLAY CHANNEL
    href: SSFKSJ_9.4.0/refadmin/q086040_.html
    positional_parameters:
      - (generic-channel-name)
      - integer
      - qmgr-name
    parameters:
      - (generic-channel-name)
      - AFFINITY
      - ALL
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
      - WHERE
      - XMITQ
    input_only:
      - ALL
      - CMDSCOPE
      - QSGDISP
      - QSGDISP(ALL)
      - QSGDISP(COPY)
      - QSGDISP(GROUP)
      - QSGDISP(LIVE)
      - QSGDISP(PRIVATE)
      - QSGDISP(QMGR)
      - WHERE
    output_only:
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
      - CLNTWGHT
      - CLNTWGHT(0)
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
      - DISCINT
      - HBINT
      - KAINT
      - LOCLADDR
      - LONGRTY
      - LONGTMR
      - MAXINST
      - MAXINSTC
      - MAXMSGL
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
      - USECLTID
      - USEDLQ
      - USERID
      - XMITQ
    notes: []
  - name: DISPLAY CHINIT
    href: SSFKSJ_9.4.0/refadmin/q086060_.html
    positional_parameters:
      - qmgr-name
    parameters:
      - CMDSCOPE
    input_only: []
    output_only: []
    notes:
      - mqsc-display-output-empty
      - mqsc-output-not-parsed
  - name: DISPLAY CHLAUTH
    href: SSFKSJ_9.4.0/refadmin/q086070_.html
    positional_parameters:
      - qmgr-name
    parameters: []
    input_only: []
    output_only:
      - ADDRESS
      - CLNTUSER
      - MATCH
      - MATCH(EXACT)
      - MATCH(GENERIC)
      - QMNAME
      - REVDNS(ENABLED)
      - SSLCERTI
      - SSLPEER
      - TYPE(ALL)
      - TYPE(USERMAP)
      - WARN
    notes:
  - name: DISPLAY CHSTATUS
    href: SSFKSJ_9.4.0/refadmin/q086090_.html
    positional_parameters:
      - connection-name
      - filter-keyword
      - filter-value
      - generic-channel-name
      - operator
      - q-name
    parameters:
      - (generic-channel-name)
      - ALL
      - CHLDISP
      - CMDSCOPE
      - CONNAME( connection-name )
      - CURRENT
      - Current channels
      - Inactive channels
      - MONITOR
      - SAVED
      - SHORT
      - WHERE
      - XMITQ( q-name )
    input_only: []
    output_only: []
    notes:
  - name: DISPLAY CLUSQMGR
    href: SSFKSJ_9.4.0/refadmin/q086110_.html
    positional_parameters:
      - filter-keyword
      - filter-value
      - generic-name
      - generic-qmgr-name
      - qmgr-name
    parameters:
      - (generic-qmgr-name)
      - ALL
      - CHANNEL ( generic-name )
      - CLUSTER ( generic-name )
      - CMDSCOPE
      - WHERE
    input_only:
      - STATUS
    output_only:
      - SUSPEND
    notes:
  - name: DISPLAY CMDSERV
    href: SSFKSJ_9.4.0/refadmin/q086120_.html
    positional_parameters: []
    parameters: []
    input_only: []
    output_only: []
    notes:
      - mqsc-display-output-empty
      - mqsc-output-not-parsed
  - name: DISPLAY COMMINFO
    href: SSFKSJ_9.4.0/refadmin/q086130_.html
    positional_parameters:
      - (generic-comminfo-name)
      - filter-keyword
      - filter-value
      - operator
      - string
    parameters:
      - (generic-comminfo-name)
      - ALL
      - TYPE
      - WHERE
    input_only:
      - COMMEV
    output_only:
      - ALL
      - TYPE
    notes:
  - name: DISPLAY CONN
    href: SSFKSJ_9.4.0/refadmin/q086140_.html
    positional_parameters:
      - generic-connid
      - qmgr-name
    parameters:
      - (generic-connid)
      - ALL
      - CMDSCOPE
      - EXTCONN
      - TYPE
      - URDISP
      - WHERE
    input_only: []
    output_only: []
    notes:
  - name: DISPLAY ENTAUTH
    href: SSFKSJ_9.4.0/refadmin/q086150_.html
    positional_parameters:
      - group-name
      - object-name
      - principal-name
      - service-component
    parameters:
      - ALL
      - GROUP(group-name)
      - OBJNAME(object-name)
      - OBJTYPE
      - PRINCIPAL(principal-name)
      - SERVCOMP(service-component)
    input_only: []
    output_only: []
    notes:
  - name: DISPLAY GROUP
    href: SSFKSJ_9.4.0/refadmin/q086160_.html
    positional_parameters: []
    parameters:
      - OBSMSGS
    input_only: []
    output_only:
      - OBSMSGS
    notes:
  - name: DISPLAY LISTENER
    href: SSFKSJ_9.4.0/refadmin/q086170_.html
    positional_parameters:
      - filter-keyword
      - filter-value
      - generic-listener-name
      - operator
    parameters:
      - ( generic-listener-name )
      - ALL
      - TRPTYPE
      - WHERE
    input_only: []
    output_only: []
    notes:
  - name: DISPLAY LOG
    href: SSFKSJ_9.4.0/refadmin/q086180_.html
    positional_parameters:
      - qmgr-name
    parameters:
      - CMDSCOPE
    input_only: []
    output_only: []
    notes:
  - name: DISPLAY LSSTATUS
    href: SSFKSJ_9.4.0/refadmin/q086190_.html
    positional_parameters:
      - filter-keyword
      - filter-value
      - generic-listener-name
      - operator
    parameters:
      - ( generic-listener-name )
      - ALL
      - WHERE
    input_only: []
    output_only:
      - ADAPTER
      - BACKLOG
      - CONTROL
      - DESCR
      - IPADDR
      - LISTENER
      - LOCLNAME
      - NTBNAMES
      - PID
      - PORT
      - SESSIONS
      - SOCKET
      - STARTDA
      - STARTTI
      - STATUS
      - TPNAME
      - TRPTYPE
    notes:
  - name: DISPLAY MAXSMSGS
    href: SSFKSJ_9.4.0/refadmin/q086200_.html
    positional_parameters:
      - qmgr-name
    parameters:
      - CMDSCOPE
    input_only: []
    output_only:
      - MAXUMSGS
    notes:
  - name: DISPLAY NAMELIST
    href: SSFKSJ_9.4.0/refadmin/q086210_.html
    positional_parameters:
      - filter-keyword
      - filter-value
      - generic-namelist-name
      - operator
      - qmgr-name
    parameters:
      - ( generic-namelist-name )
      - ALL
      - CMDSCOPE
      - NLTYPE
      - QSGDISP
      - WHERE
    input_only:
      - CMDSCOPE
      - QSGDISP(ALL)
      - QSGDISP(COPY)
      - QSGDISP(GROUP)
      - QSGDISP(LIVE)
      - QSGDISP(PRIVATE)
      - QSGDISP(QMGR)
      - WHERE
    output_only: []
    notes:
  - name: DISPLAY POLICY
    href: SSFKSJ_9.4.0/refadmin/q120820_.html
    positional_parameters:
      - (policy-name)
    parameters:
      - (policy-name)
    input_only: []
    output_only:
      - ENCALG
      - ENFORCE
      - KEYREUSE
      - POLICY
      - SIGNALG
    notes:
  - name: DISPLAY PROCESS
    href: SSFKSJ_9.4.0/refadmin/q086220_.html
    positional_parameters:
      - (generic-process-name)
      - filter-keyword
      - filter-value
      - operator
      - qmgr-name
    parameters:
      - (generic-process-name)
      - ALL
      - CMDSCOPE
      - QSGDISP
      - WHERE
    input_only:
      - APPLTYPE
      - CMDSCOPE
      - QSGDISP
      - QSGDISP(ALL)
      - QSGDISP(COPY)
      - QSGDISP(GROUP)
      - QSGDISP(LIVE)
      - QSGDISP(PRIVATE)
      - QSGDISP(QMGR)
      - WHERE
    output_only:
      - ALL
    notes:
  - name: DISPLAY PUBSUB
    href: SSFKSJ_9.4.0/refadmin/q086230_.html
    positional_parameters:
      - qmgr-name
    parameters:
      - CMDSCOPE
      - TYPE
    input_only:
      - CMDSCOPE
    output_only:
      - CLUSRCVR
      - QMNAME
      - STATUS
      - SUBCOUNT
      - TPCOUNT
      - TYPE
    notes:
  - name: DISPLAY QMGR
    href: SSFKSJ_9.4.0/refadmin/q086240_.html
    positional_parameters:
      - integer
      - qmgr-name
    parameters:
      - ALL
      - CHINIT
      - CLUSTER
      - CMDSCOPE
      - DEFCLXQ
      - EVENT
      - OTELPCTL
      - OTELTRAC
      - PUBSUB
      - SYSTEM
    input_only: []
    output_only:
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
    notes: []
  - name: DISPLAY QMSTATUS
    href: SSFKSJ_9.4.0/refadmin/q086250_.html
    positional_parameters: []
    parameters:
      - ACTIVE
      - ALL
      - LEADER
      - LOG
      - NHATYPE
      - REPLICA
      - TYPE
      - UNKNOWN
      - WHERE
    input_only:
      - LOG
      - TYPE(NATIVEHA)
    output_only:
      - LDAPCONN
      - QMFSUSE
      - SHARED
      - TYPE(REDUCELOG)
    notes: []
  - name: DISPLAY QSTATUS
    href: SSFKSJ_9.4.0/refadmin/q086260_.html
    positional_parameters:
      - generic-qname
      - n
    parameters:
      - ( generic-qname )
      - ALL
      - CMDSCOPE
      - MONITOR
      - OPENTYPE
      - TYPE
      - WHERE
    input_only: []
    output_only: []
    notes:
  - name: DISPLAY QUEUE
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
    parameters:
      - ACCTQ
      - ALL
      - ALTDATE
      - ALTTIME
      - BOQNAME
      - BOTHRESH
      - CAPEXPRY
      - CFSTRUCT
      - CFSTRUCT ( generic-name)
      - CLCHNAME
      - CLUSDATE
      - CLUSINFO
      - CLUSNL
      - CLUSNL ( generic-name )
      - CLUSQMGR
      - CLUSQT
      - CLUSTER
      - CLUSTER ( generic-name )
      - CLUSTIME
      - CLWLPRTY
      - CLWLRANK
      - CLWLUSEQ
      - CMDSCOPE
      - COMPAT
      - COPY
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
      - EQ
      - FORCE
      - GE
      - GET
      - GROUP
      - GT
      - HARDENBO
      - IMGRCOVQ
      - INDXTYPE
      - INITQ
      - IPPROCS
      - LE
      - LIVE
      - LK
      - LT
      - MAXDEPTH
      - MAXFSIZE
      - MAXMSGL
      - MONQ
      - MSGDLVSQ
      - NE
      - NL
      - NONE
      - NPMCLASS
      - OPPROCS
      - OTELPCTL
      - OTELTRAC
      - PRIVATE
      - PROCESS
      - PROPCTL
      - PSID
      - PSID ( integer )
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
      - QMODEL
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
      - SHARED
      - STATQ
      - STGCLASS
      - STGCLASS ( generic-name)
      - STREAMQ
      - STRMQOS
      - TARGET
      - TARGTYPE
      - TARGTYPE ( target-type )
      - TPIPE
      - TRIGDATA
      - TRIGDPTH
      - TRIGGER
      - TRIGMPRI
      - TRIGTYPE
      - TYPE
      - TYPE ( queue-type )
      - USAGE
      - WHERE
      - XMITQ
      - queue-name
    input_only:
      - CLUSINFO
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
      - QMODEL
      - SHARED
      - TYPE
      - WHERE
    output_only:
      - ACCTQ
      - ALTDATE
      - ALTTIME
      - BOQNAME
      - BOTHRESH
      - CAPEXPRY
      - CLCHNAME
      - CLUSDATE
      - CLUSQMGR
      - CLUSQT
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
      - MQ
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
      - PUT
      - QDEPTHHI
      - QDEPTHLO
      - QMID
      - QSVCINT
      - QTYPE
      - RETINTVL
      - RNAME
      - RQMNAME
      - SCOPE
      - SHARE
      - SQGETTMR
      - STATQ
      - STREAMQ
      - STRMQOS
      - TARGET
      - TPIPE
      - TRIGDATA
      - TRIGDPTH
      - TRIGGER
      - TRIGMPRI
      - TRIGTYPE
      - USAGE
      - XMITQ
    notes: []
  - name: DISPLAY SBSTATUS
    href: SSFKSJ_9.4.0/refadmin/q086280_.html
    positional_parameters:
      - (generic-name)
      - string
    parameters:
      - (generic-name)
      - ALL
      - CMDSCOPE
      - DURABLE
      - SUBTYPE
      - WHERE
    input_only:
      - CMDSCOPE
      - QSGDISP
      - SUBTYPE
      - SUBUSER
      - WHERE
    output_only:
      - COMMEV
    notes:
  - name: DISPLAY SECURITY
    href: SSFKSJ_9.4.0/refadmin/q086290_.html
    positional_parameters:
      - qmgr-name
    parameters:
      - ALL
      - CMDSCOPE
      - INTERVAL
      - SWITCHES
      - TIMEOUT
    input_only: []
    output_only: []
    notes:
  - name: DISPLAY SERVICE
    href: SSFKSJ_9.4.0/refadmin/q086300_.html
    positional_parameters:
      - filter-keyword
      - filter-value
      - generic-service-name
      - operator
    parameters:
      - (generic-service-name)
      - ALL
      - WHERE
    input_only: []
    output_only: []
    notes:
  - name: DISPLAY SMDS
    href: SSFKSJ_9.4.0/refadmin/q086310_.html
    positional_parameters:
      - filter-keyword
      - filter-value
      - operator
      - qmgr-name
      - structure-name
    parameters:
      - ALL
      - CFSTRUCT( structure-name )
      - SMDS(qmgr-name|*)
      - WHERE
    input_only:
      - DESCR
      - RECOVER
    output_only:
      - CFSTRUCT
    notes:
  - name: DISPLAY SMDSCONN
    href: SSFKSJ_9.4.0/refadmin/q086320_.html
    positional_parameters:
      - qmgr-name
      - structure-name
    parameters:
      - CFSTRUCT( structure-name )
      - CMDSCOPE
      - SMDSCONN(qmgr-name|*)
      - WHERE
    input_only: []
    output_only: []
    notes:
  - name: DISPLAY STGCLASS
    href: SSFKSJ_9.4.0/refadmin/q086330_.html
    positional_parameters:
      - (generic-class)
      - filter-keyword
      - filter-value
      - integer
      - operator
      - qmgr-name
    parameters:
      - (generic-class)
      - ALL
      - CMDSCOPE
      - PSID( integer )
      - QSGDISP
      - WHERE
    input_only:
      - CMDSCOPE
      - PSID
      - QSGDISP
      - QSGDISP(ALL)
      - QSGDISP(COPY)
      - QSGDISP(GROUP)
      - QSGDISP(QMGR)
      - WHERE
    output_only:
      - XCFGNAME
    notes:
  - name: DISPLAY SUB
    href: SSFKSJ_9.4.0/refadmin/q086340_.html
    positional_parameters:
      - (generic-name)
      - filter-keyword
      - filter-value
      - integer
      - operator
      - qmgr-name
      - string
    parameters:
      - (generic-name)
      - ALL
      - ALTDATE(string)
      - ALTTIME(string)
      - CMDSCOPE
      - CRDATE(string)
      - CRTIME(string)
      - DEST
      - DEST(string)
      - DESTCLAS
      - DESTCORL
      - DESTCORL(string)
      - DESTQMGR(string)
      - DISTYPE
      - DURABLE
      - EXPIRY
      - PSPROP
      - PUBACCT
      - PUBACCT(string)
      - PUBAPPID
      - PUBAPPID(string)
      - PUBPRTY
      - REQONLY
      - SELECTOR
      - SELECTOR(string)
      - SELTYPE
      - SUB(string)
      - SUBID(string)
      - SUBLEVEL
      - SUBLEVEL(integer)
      - SUBSCOPE
      - SUBTYPE
      - SUBUSER
      - SUBUSER(string)
      - SUMMARY
      - TOPICOBJ
      - TOPICOBJ(string)
      - TOPICSTR(string)
      - USERDATA
      - USERDATA(string)
      - VARUSER
      - WHERE
      - WSCHEMA
    input_only: []
    output_only: []
    notes:
  - name: DISPLAY SVSTATUS
    href: SSFKSJ_9.4.0/refadmin/q086350_.html
    positional_parameters:
      - filter-keyword
      - filter-value
      - generic-service-name
      - operator
    parameters:
      - (generic-service-name)
      - ALL
      - WHERE
    input_only:
      - CONTROL
    output_only:
      - SERVTYPE
      - SERVTYPE(SERVER)
    notes:
  - name: DISPLAY SYSTEM
    href: SSFKSJ_9.4.0/refadmin/q086360_.html
    positional_parameters:
      - qmgr-name
    parameters:
      - ACELIM
      - CLCACHE
      - CMDSCOPE
      - SPLCAP
    input_only: []
    output_only: []
    notes:
  - name: DISPLAY TCLUSTER
    href: SSFKSJ_9.4.0/refadmin/q114320_.html
    positional_parameters:
      - (generic-topic-name)
      - filter-keyword
      - filter-value
      - operator
      - qmgr-name
    parameters:
      - (generic-topic-name)
      - ALL
      - CLUSTER
      - CMDSCOPE
      - QSGDISP
      - WHERE
    input_only: []
    output_only: []
    notes:
  - name: DISPLAY THREAD
    href: SSFKSJ_9.4.0/refadmin/q086370_.html
    positional_parameters:
      - (*)
      - (connection-name)
      - qmgr-name
    parameters:
      - (*)
      - (connection-name)
      - CMDSCOPE
      - QMNAME
      - TYPE
    input_only: []
    output_only: []
    notes:
  - name: DISPLAY TOPIC
    href: SSFKSJ_9.4.0/refadmin/q086380_.html
    positional_parameters:
      - (generic-topic-name)
      - filter-keyword
      - filter-value
      - integer
      - operator
      - qmgr-name
    parameters:
      - (generic-topic-name)
      - ALL
      - ALTDATE
      - ALTTIME
      - CLROUTE
      - CLSTATE
      - CLUSDATE
      - CLUSINFO
      - CLUSQMGR
      - CLUSTER
      - CLUSTIME
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
      - QMID
      - QSGDISP
      - SUB
      - SUBSCOPE
      - TOPICSTR
      - TYPE
      - USEDLQ
      - WHERE
      - WILDCARD
    input_only:
      - CLUSINFO
      - CMDSCOPE
      - QSGDISP
      - QSGDISP(ALL)
      - QSGDISP(COPY)
      - QSGDISP(GROUP)
      - QSGDISP(LIVE)
      - QSGDISP(PRIVATE)
      - QSGDISP(QMGR)
    output_only:
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
    notes: []
  - name: DISPLAY TPSTATUS
    href: SSFKSJ_9.4.0/refadmin/q086390_.html
    positional_parameters:
      - ' '
      - *
      - filter-keyword
      - filter-value
      - integer
      - operator
      - qmgr-name
      - topicstr)
    parameters:
      - ALL
      - CMDSCOPE
      - TYPE
      - WHERE
      - topicstr)
    input_only: []
    output_only: []
    notes:
  - name: DISPLAY TRACE
    href: SSFKSJ_9.4.0/refadmin/q086400_.html
    positional_parameters:
      - integer
      - output-type
      - qmgr-name
      - string
    parameters:
      - *
      - ACCTG
      - CHINIT
      - CMDSCOPE
      - COMMENT(string)
      - DETAIL(output-type)
      - GLOBAL
      - STAT
    input_only: []
    output_only:
      - ACCTG
      - CHINIT
      - CLASS
      - CMDSCOPE
      - COMMENT
      - DEST
      - DETAIL
      - GLOBAL
      - GTF
      - RES
      - RMID
      - SMF
      - SRV
      - STAT
      - TNO
      - USERID
    notes:
  - name: DISPLAY USAGE
    href: SSFKSJ_9.4.0/refadmin/q086410_.html
    positional_parameters:
      - integer
      - qmgr-name
    parameters:
      - CMDSCOPE
      - PSID(integer)
      - TYPE
    input_only: []
    output_only: []
    notes:
  - name: MOVE QLOCAL
    href: SSFKSJ_9.4.0/refadmin/q086420_.html
    positional_parameters:
      - qmgr-name
      - source
      - target
    parameters:
      - CMDSCOPE
      - QSGDISP
      - TYPE
      - source
      - target
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: PING CHANNEL
    href: SSFKSJ_9.4.0/refadmin/q086430_.html
    positional_parameters:
      - (channel-name)
      - integer
      - qmgr-name
    parameters:
      - (channel-name)
      - CHLDISP
      - CMDSCOPE
      - DATALEN( integer )
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: PING QMGR
    href: SSFKSJ_9.4.0/refadmin/q086440_.html
    positional_parameters: []
    parameters: []
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: PURGE CHANNEL
    href: SSFKSJ_9.4.0/refadmin/q086450_.html
    positional_parameters:
      - channel name
      - string
    parameters:
      - CHLTYPE string
      - CLIENTID string
      - channel name
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: RECOVER BSDS
    href: SSFKSJ_9.4.0/refadmin/q086455_.html
    positional_parameters:
      - qmgr-name
    parameters:
      - CMDSCOPE
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: RECOVER CFSTRUCT
    href: SSFKSJ_9.4.0/refadmin/q086460_.html
    positional_parameters:
      - qmgr-name
      - structure-names ...
    parameters:
      - CFSTRUCT(structure-names ...)
      - CMDSCOPE
      - TYPE
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: REFRESH CLUSTER
    href: SSFKSJ_9.4.0/refadmin/q086470_.html
    positional_parameters:
      - generic-clustername
      - qmgr-name
    parameters:
      - ( generic-clustername )
      - CMDSCOPE
      - REPOS
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: REFRESH QMGR
    href: SSFKSJ_9.4.0/refadmin/q086480_.html
    positional_parameters:
      - (generic-object-name)
      - (integer)
      - (objtype)
      - qmgr-name
    parameters:
      - CMDSCOPE
      - INCLINT (integer)
      - NAME (generic-object-name)
      - OBJECT (objtype)
      - TYPE
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: REFRESH SECURITY
    href: SSFKSJ_9.4.0/refadmin/q086490_.html
    positional_parameters:
      - qmgr-name
    parameters:
      - *
      - CMDSCOPE
      - MQADMIN
      - MQNLIST
      - MQPROC
      - MQQUEUE
      - MXADMIN
      - MXNLIST
      - MXPROC
      - MXQUEUE
      - MXTOPIC
      - TYPE
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: RESET CFSTRUCT
    href: SSFKSJ_9.4.0/refadmin/q086500_.html
    positional_parameters:
      - structure-name
    parameters:
      - ACTION(FAIL)
      - CFSTRUCT(structure-name)
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: RESET CHANNEL
    href: SSFKSJ_9.4.0/refadmin/q086510_.html
    positional_parameters:
      - (channel-name)
      - integer
      - qmgr-name
    parameters:
      - (channel-name)
      - CHLDISP
      - CMDSCOPE
      - SEQNUM(integer)
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: RESET CLUSTER
    href: SSFKSJ_9.4.0/refadmin/q086520_.html
    positional_parameters:
      - (clustername)
      - qmgr-name
      - qmid
      - qmname
    parameters:
      - (clustername)
      - ACTION(FORCEREMOVE)
      - CMDSCOPE
      - QMID(qmid)
      - QMNAME(qmname)
      - QUEUES
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: RESET QMGR
    href: SSFKSJ_9.4.0/refadmin/q086530_.html
    positional_parameters:
      - name
      - qmgr-name
    parameters:
      - CMDSCOPE
      - TYPE
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: RESET QSTATS
    href: SSFKSJ_9.4.0/refadmin/q086540_.html
    positional_parameters:
      - generic-qname
      - qmgr-name
    parameters:
      - CMDSCOPE
      - generic-qname
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: RESET SMDS
    href: SSFKSJ_9.4.0/refadmin/q086550_.html
    positional_parameters:
      - qmgr-name
      - structure-name
    parameters:
      - ACCESS(ENABLED|DISABLED)
      - CFSTRUCT(structure-name)
      - SMDS(qmgr-name|*)
      - STATUS(FAILED | RECOVERED)
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: RESET TPIPE
    href: SSFKSJ_9.4.0/refadmin/q086560_.html
    positional_parameters:
      - group-name
      - integer
      - member-name
      - qmgr-name
      - tpipe-name
    parameters:
      - (tpipe-name)
      - ACTION
      - CMDSCOPE
      - RCVSEQ(integer)
      - SENDSEQ(integer)
      - XCFGNAME( group-name )
      - XCFMNAME(member-name)
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: RESOLVE CHANNEL
    href: SSFKSJ_9.4.0/refadmin/q086570_.html
    positional_parameters:
      - (channel-name)
      - qmgr-name
    parameters:
      - (channel-name)
      - ACTION
      - CHLDISP
      - CMDSCOPE
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: RESOLVE INDOUBT
    href: SSFKSJ_9.4.0/refadmin/q086580_.html
    positional_parameters:
      - (connection-name)
      - origin-id
      - qmgr-name
    parameters:
      - (connection-name)
      - ACTION
      - CMDSCOPE
      - NID
      - QMNAME
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: RESUME QMGR
    href: SSFKSJ_9.4.0/refadmin/q086590_.html
    positional_parameters:
      - (clustername)
      - (nlname)
      - qmgr-name
    parameters:
      - CLUSNL (nlname)
      - CLUSTER (clustername)
      - CMDSCOPE
      - FACILITY
      - LOG
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: RVERIFY SECURITY
    href: SSFKSJ_9.4.0/refadmin/q086600_.html
    positional_parameters:
      - (userids...)
      - qmgr-name
    parameters:
      - (userids...)
      - CMDSCOPE
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: SET ARCHIVE
    href: SSFKSJ_9.4.0/refadmin/q086610_.html
    positional_parameters:
      - qmgr-name
    parameters:
      - CMDSCOPE
      - DEFAULT
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: SET AUTHREC
    href: SSFKSJ_9.4.0/refadmin/q086620_.html
    positional_parameters:
      - group-name
      - principal-name
      - profile-name
      - service-component
    parameters:
      - AUTHADD
      - AUTHRMV
      - GROUP(group-name)
      - OBJTYPE
      - PRINCIPAL(principal-name)
      - PROFILE(profile-name)
      - SERVCOMP(service-component)
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: SET CHLAUTH
    href: SSFKSJ_9.4.0/refadmin/q086630_.html
    positional_parameters:
      - channel-profile-name
      - qmgr-name
    parameters: []
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: SET LOG
    href: SSFKSJ_9.4.0/refadmin/q129100_.html
    positional_parameters:
      - name
    parameters:
      - ARCHIVED (name)
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: SET POLICY
    href: SSFKSJ_9.4.0/refadmin/q120800_.html
    positional_parameters:
      - (distinguished-name)
      - (policy-name)
    parameters:
      - (policy-name)
      - ACTION
      - ENCALG
      - ENFORCE
      - KEYREUSE
      - RECIP (distinguished-name)
      - SIGNALG
      - SIGNER (distinguished-name)
      - TOLERATE
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: SET SYSTEM
    href: SSFKSJ_9.4.0/refadmin/q086650_.html
    positional_parameters:
      - qmgr-name
    parameters:
      - CMDSCOPE
      - DEFAULT
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: START CHANNEL
    href: SSFKSJ_9.4.0/refadmin/q086660_.html
    positional_parameters:
      - (channel-name)
      - qmgr-name
    parameters:
      - (channel-name)
      - CHLDISP
      - CMDSCOPE
      - IGNSTATE
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: START CHINIT
    href: SSFKSJ_9.4.0/refadmin/q086680_.html
    positional_parameters:
      - jcl-substitution
      - qmgr-name
      - string
    parameters:
      - CMDSCOPE
      - ENVPARM( jcl-substitution )
      - INITQ( string )
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: START CMDSERV
    href: SSFKSJ_9.4.0/refadmin/q086690_.html
    positional_parameters: []
    parameters: []
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: START LISTENER
    href: SSFKSJ_9.4.0/refadmin/q086700_.html
    positional_parameters:
      - name
      - port-number
      - qmgr-name
      - string
    parameters:
      - ( name )
      - CMDSCOPE
      - IGNSTATE
      - INDISP
      - IPADDR
      - LUNAME( string )
      - PORT( port-number )
      - TRPTYPE
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: START QMGR
    href: SSFKSJ_9.4.0/refadmin/q086710_.html
    positional_parameters:
      - backward-migration-target-vrm
      - jcl-substitution
      - member-name
    parameters:
      - AMSPROD
      - BACKMIG( backward-migration-target-vrm )
      - ENVPARM( jcl-substitution )
      - PARM( member-name )
      - QMGRPROD
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: START SERVICE
    href: SSFKSJ_9.4.0/refadmin/q086720_.html
    positional_parameters:
      - service-name
    parameters:
      - ( service-name )
      - IGNSTATE
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: START SMDSCONN
    href: SSFKSJ_9.4.0/refadmin/q086730_.html
    positional_parameters:
      - qmgr-name
      - structure-name
    parameters:
      - CFSTRUCT(structure-name)
      - CMDSCOPE
      - SMDSCONN(qmgr-name| *)
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: START TRACE
    href: SSFKSJ_9.4.0/refadmin/q086740_.html
    positional_parameters:
      - integer
      - qmgr-name
      - string
      - userid
    parameters:
      - ACCTG
      - CHINIT
      - CMDSCOPE
      - COMMENT( string )
      - GLOBAL
      - STAT
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: STOP CHANNEL
    href: SSFKSJ_9.4.0/refadmin/q086750_.html
    positional_parameters:
      - (channel-name)
      - (connection-name)
      - (qmname)
      - qmgr-name
    parameters:
      - (channel-name)
      - CHLDISP
      - CMDSCOPE
      - CONNAME (connection-name)
      - IGNSTATE
      - MODE
      - QMNAME (qmname)
      - STATUS
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: STOP CHINIT
    href: SSFKSJ_9.4.0/refadmin/q086770_.html
    positional_parameters:
      - qmgr-name
    parameters:
      - CMDSCOPE
      - SHARED
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: STOP CMDSERV
    href: SSFKSJ_9.4.0/refadmin/q086780_.html
    positional_parameters: []
    parameters: []
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: STOP CONN
    href: SSFKSJ_9.4.0/refadmin/q086790_.html
    positional_parameters:
      - connection-identifier
    parameters:
      - (connection-identifier)
      - EXTCONN
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: STOP LISTENER
    href: SSFKSJ_9.4.0/refadmin/q086800_.html
    positional_parameters:
      - name
      - qmgr-name
    parameters:
      - (name)
      - CMDSCOPE
      - IGNSTATE
      - INDISP
      - IPADDR
      - PORT
      - TRPTYPE
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: STOP QMGR
    href: SSFKSJ_9.4.0/refadmin/q086810_.html
    positional_parameters:
      - qmgr-name
    parameters:
      - CMDSCOPE
      - MODE
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: STOP SERVICE
    href: SSFKSJ_9.4.0/refadmin/q086820_.html
    positional_parameters:
      - service-name
    parameters:
      - (service-name)
      - IGNSTATE
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: STOP SMDSCONN
    href: SSFKSJ_9.4.0/refadmin/q086830_.html
    positional_parameters:
      - qmgr-name
    parameters:
      - CFSTRUCT
      - CMDSCOPE
      - SMDSCONN
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: STOP TRACE
    href: SSFKSJ_9.4.0/refadmin/q086840_.html
    positional_parameters:
      - integer
      - qmgr-name
      - string
    parameters:
      - *
      - ACCTG
      - CHINIT
      - CMDSCOPE
      - COMMENT( string )
      - GLOBAL
      - STAT
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
  - name: SUSPEND QMGR
    href: SSFKSJ_9.4.0/refadmin/q086850_.html
    positional_parameters:
      - (clustername)
      - (nlname)
      - qmgr-name
    parameters:
      - CLUSNL (nlname)
      - CLUSTER (clustername)
      - CMDSCOPE
      - FACILITY
      - LOG
      - MODE
    input_only: []
    output_only: []
    notes:
      - mqsc-output-not-parsed
pcf_commands:
  - name: MQCMD_BACKUP_CF_STRUC
    request_href: SSFKSJ_9.4.0/refadmin/q086900_.html
    response_href: SSFKSJ_9.4.0/refadmin/q086900_.html
    request_parameters:
      - name: CFStrucName
        pcf_type: MQCFST
        type_hint: str
      - name: CommandScope
        pcf_type: MQCFST
        type_hint: str
      - name: ExcludeInterval
        pcf_type: MQCFIN
        type_hint: int
    response_parameters:
      - name: CFStrucName
        pcf_type: MQCFST
        type_hint: str
      - name: CommandScope
        pcf_type: MQCFST
        type_hint: str
      - name: ExcludeInterval
        pcf_type: MQCFIN
        type_hint: int
    notes: []
  - name: MQCMD_CHANGE_PROT_POLICY
    request_href: SSFKSJ_9.4.0/refadmin/q120830_.html
    response_href: SSFKSJ_9.4.0/refadmin/q120830_.html
    request_parameters:
      - name: PolicyName
        pcf_type: MQCFST
        type_hint: str
      - name: SignAlg
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQMLP_SIGN_ALG_NONE
          - MQMLP_SIGN_ALG_MD5
          - MQMLP_SIGN_ALG_SHA1
          - MQMLP_SIGN_ALG_SHA256
          - MQMLP_SIGN_ALG_SHA384
          - MQMLP_SIGN_ALG_SHA512
      - name: EncAlg
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQMLP_ENCRYPTION_ALG_NONE
          - MQMLP_ENCRYPTION_ALG_RC2
          - MQMLP_ENCRYPTION_ALG_DES
          - MQMLP_ENCRYPTION_ALG_3DES
          - MQMLP_ENCRYPTION_ALG_AES128
          - MQMLP_ENCRYPTION_ALG_AES256
      - name: Signer
        pcf_type: MQCFST
        type_hint: str
      - name: Recipient
        pcf_type: MQCFST
        type_hint: str
        enum_values:
          - MQMLP_TOLERATE_NO
          - MQMLP_TOLERATE_YES
      - name: KeyReuse
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQKEY_REUSE_DISABLED
          - MQKEY_REUSE_UNLIMITED
      - name: Action
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQACT_REPLACE
          - MQACT_ADD
          - MQACT_REMOVE
          - MQRCCF_POLICY_TYPE_ERROR
          - MQRC_OPTIONS_ERROR
    response_parameters:
      - name: PolicyName
        pcf_type: MQCFST
        type_hint: str
      - name: SignAlg
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQMLP_SIGN_ALG_NONE
          - MQMLP_SIGN_ALG_MD5
          - MQMLP_SIGN_ALG_SHA1
          - MQMLP_SIGN_ALG_SHA256
          - MQMLP_SIGN_ALG_SHA384
          - MQMLP_SIGN_ALG_SHA512
      - name: EncAlg
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQMLP_ENCRYPTION_ALG_NONE
          - MQMLP_ENCRYPTION_ALG_RC2
          - MQMLP_ENCRYPTION_ALG_DES
          - MQMLP_ENCRYPTION_ALG_3DES
          - MQMLP_ENCRYPTION_ALG_AES128
          - MQMLP_ENCRYPTION_ALG_AES256
      - name: Signer
        pcf_type: MQCFST
        type_hint: str
      - name: Recipient
        pcf_type: MQCFST
        type_hint: str
        enum_values:
          - MQMLP_TOLERATE_NO
          - MQMLP_TOLERATE_YES
      - name: KeyReuse
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQKEY_REUSE_DISABLED
          - MQKEY_REUSE_UNLIMITED
      - name: Action
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQACT_REPLACE
          - MQACT_ADD
          - MQACT_REMOVE
          - MQRCCF_POLICY_TYPE_ERROR
          - MQRC_OPTIONS_ERROR
    notes: []
  - name: MQCMD_CHANGE_Q_MGR
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
        type_hint: list[int]
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
        type_hint: list[int]
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
    notes: []
  - name: MQCMD_CHANGE_SECURITY
    request_href: SSFKSJ_9.4.0/refadmin/q087010_.html
    response_href: SSFKSJ_9.4.0/refadmin/q087010_.html
    request_parameters:
      - name: CommandScope
        pcf_type: MQCFST
        type_hint: str
      - name: SecurityInterval
        pcf_type: MQCFIN
        type_hint: int
      - name: SecurityTimeout
        pcf_type: MQCFIN
        type_hint: int
    response_parameters:
      - name: CommandScope
        pcf_type: MQCFST
        type_hint: str
      - name: SecurityInterval
        pcf_type: MQCFIN
        type_hint: int
      - name: SecurityTimeout
        pcf_type: MQCFIN
        type_hint: int
    notes: []
  - name: MQCMD_CHANGE_SMDS
    request_href: SSFKSJ_9.4.0/refadmin/q087020_.html
    response_href: SSFKSJ_9.4.0/refadmin/q087020_.html
    request_parameters:
      - name: SMDS
        pcf_type: MQCFST
        type_hint: str
      - name: CFStrucName
        pcf_type: MQCFST
        type_hint: str
      - name: DSBufs
        pcf_type: MQCFIN
        type_hint: int
      - name: DSEXPAND
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQDSE_YES
          - MQDSE_NO
          - MQDSE_DEFAULT
    response_parameters:
      - name: SMDS
        pcf_type: MQCFST
        type_hint: str
      - name: CFStrucName
        pcf_type: MQCFST
        type_hint: str
      - name: DSBufs
        pcf_type: MQCFIN
        type_hint: int
      - name: DSEXPAND
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQDSE_YES
          - MQDSE_NO
          - MQDSE_DEFAULT
    notes: []
  - name: MQCMD_CLEAR_Q
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
    notes: []
  - name: MQCMD_CLEAR_TOPIC_STRING
    request_href: SSFKSJ_9.4.0/refadmin/q087080_.html
    response_href: SSFKSJ_9.4.0/refadmin/q087080_.html
    request_parameters:
      - name: TopicString
        pcf_type: MQCFST
        type_hint: str
      - name: ClearType
        pcf_type: MQCFIN
        type_hint: int
      - name: Scope
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQCLRS_LOCAL
      - name: CommandScope
        pcf_type: MQCFST
        type_hint: str
    response_parameters:
      - name: TopicString
        pcf_type: MQCFST
        type_hint: str
      - name: ClearType
        pcf_type: MQCFIN
        type_hint: int
      - name: Scope
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQCLRS_LOCAL
      - name: CommandScope
        pcf_type: MQCFST
        type_hint: str
    notes: []
  - name: MQCMD_DELETE_AUTH_INFO
    request_href: SSFKSJ_9.4.0/refadmin/q087090_.html
    response_href: SSFKSJ_9.4.0/refadmin/q087090_.html
    request_parameters:
      - name: AuthInfoName
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
      - name: IgnoreState
        pcf_type: MQCFST
        type_hint: str
        enum_values:
          - MQIS_YES
          - MQIS_NO
    response_parameters:
      - name: AuthInfoName
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
      - name: IgnoreState
        pcf_type: MQCFST
        type_hint: str
        enum_values:
          - MQIS_YES
          - MQIS_NO
    notes: []
  - name: MQCMD_DELETE_AUTH_REC
    request_href: SSFKSJ_9.4.0/refadmin/q087100_.html
    response_href: SSFKSJ_9.4.0/refadmin/q087100_.html
    request_parameters:
      - name: ObjectType
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQOT_AUTH_INFO
          - MQOT_CHANNEL
          - MQOT_CLNTCONN_CHANNEL
          - MQOT_COMM_INFO
          - MQOT_LISTENER
          - MQOT_NAMELIST
          - MQOT_PROCESS
          - MQOT_Q
          - MQOT_Q_MGR
          - MQOT_REMOTE_Q_MGR_NAME
          - MQOT_SERVICE
          - MQOT_TOPIC
      - name: ProfileName
        pcf_type: MQCFST
        type_hint: str
      - name: GroupNames
        pcf_type: MQCFSL
        type_hint: list[str]
      - name: PrincipalNames
        pcf_type: MQCFSL
        type_hint: list[str]
      - name: IgnoreState
        pcf_type: MQCFST
        type_hint: str
        enum_values:
          - MQIS_YES
          - MQIS_NO
          - MQRC_OBJECT_TYPE_ERROR
          - MQRC_UNKNOWN_ENTITY
          - MQRCCF_ENTITY_NAME_MISSING
          - MQRCCF_OBJECT_TYPE_MISSING
          - MQRCCF_PROFILE_NAME_ERROR
    response_parameters:
      - name: ObjectType
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQOT_AUTH_INFO
          - MQOT_CHANNEL
          - MQOT_CLNTCONN_CHANNEL
          - MQOT_COMM_INFO
          - MQOT_LISTENER
          - MQOT_NAMELIST
          - MQOT_PROCESS
          - MQOT_Q
          - MQOT_Q_MGR
          - MQOT_REMOTE_Q_MGR_NAME
          - MQOT_SERVICE
          - MQOT_TOPIC
      - name: ProfileName
        pcf_type: MQCFST
        type_hint: str
      - name: GroupNames
        pcf_type: MQCFSL
        type_hint: list[str]
      - name: PrincipalNames
        pcf_type: MQCFSL
        type_hint: list[str]
      - name: IgnoreState
        pcf_type: MQCFST
        type_hint: str
        enum_values:
          - MQIS_YES
          - MQIS_NO
          - MQRC_OBJECT_TYPE_ERROR
          - MQRC_UNKNOWN_ENTITY
          - MQRCCF_ENTITY_NAME_MISSING
          - MQRCCF_OBJECT_TYPE_MISSING
          - MQRCCF_PROFILE_NAME_ERROR
    notes: []
  - name: MQCMD_DELETE_CF_STRUC
    request_href: SSFKSJ_9.4.0/refadmin/q087110_.html
    response_href: SSFKSJ_9.4.0/refadmin/q087110_.html
    request_parameters:
      - name: CFStrucName
        pcf_type: MQCFST
        type_hint: str
    response_parameters:
      - name: CFStrucName
        pcf_type: MQCFST
        type_hint: str
    notes: []
  - name: MQCMD_DELETE_CHANNEL
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
    notes: []
  - name: MQCMD_DELETE_COMM_INFO
    request_href: SSFKSJ_9.4.0/refadmin/q087150_.html
    response_href: SSFKSJ_9.4.0/refadmin/q087150_.html
    request_parameters:
      - name: ComminfoName
        pcf_type: MQCFST
        type_hint: str
      - name: IgnoreState
        pcf_type: MQCFST
        type_hint: str
        enum_values:
          - MQIS_YES
          - MQIS_NO
    response_parameters:
      - name: ComminfoName
        pcf_type: MQCFST
        type_hint: str
      - name: IgnoreState
        pcf_type: MQCFST
        type_hint: str
        enum_values:
          - MQIS_YES
          - MQIS_NO
    notes: []
  - name: MQCMD_DELETE_LISTENER
    request_href: SSFKSJ_9.4.0/refadmin/q087140_.html
    response_href: SSFKSJ_9.4.0/refadmin/q087140_.html
    request_parameters:
      - name: ListenerName
        pcf_type: MQCFST
        type_hint: str
      - name: IgnoreState
        pcf_type: MQCFST
        type_hint: str
        enum_values:
          - MQIS_YES
          - MQIS_NO
    response_parameters:
      - name: ListenerName
        pcf_type: MQCFST
        type_hint: str
      - name: IgnoreState
        pcf_type: MQCFST
        type_hint: str
        enum_values:
          - MQIS_YES
          - MQIS_NO
    notes: []
  - name: MQCMD_DELETE_NAMELIST
    request_href: SSFKSJ_9.4.0/refadmin/q087160_.html
    response_href: SSFKSJ_9.4.0/refadmin/q087160_.html
    request_parameters:
      - name: NamelistName
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
      - name: IgnoreState
        pcf_type: MQCFST
        type_hint: str
        enum_values:
          - MQIS_YES
          - MQIS_NO
    response_parameters:
      - name: NamelistName
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
      - name: IgnoreState
        pcf_type: MQCFST
        type_hint: str
        enum_values:
          - MQIS_YES
          - MQIS_NO
    notes: []
  - name: MQCMD_DELETE_PROCESS
    request_href: SSFKSJ_9.4.0/refadmin/q087170_.html
    response_href: SSFKSJ_9.4.0/refadmin/q087170_.html
    request_parameters:
      - name: ProcessName
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
      - name: IgnoreState
        pcf_type: MQCFST
        type_hint: str
        enum_values:
          - MQIS_YES
          - MQIS_NO
    response_parameters:
      - name: ProcessName
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
      - name: IgnoreState
        pcf_type: MQCFST
        type_hint: str
        enum_values:
          - MQIS_YES
          - MQIS_NO
    notes: []
  - name: MQCMD_DELETE_PROT_POLICY
    request_href: SSFKSJ_9.4.0/refadmin/q120860_.html
    response_href: SSFKSJ_9.4.0/refadmin/q120860_.html
    request_parameters:
      - name: IgnoreState
        pcf_type: MQCFST
        type_hint: str
        enum_values:
          - MQIS_YES
          - MQIS_NO
          - MQRC_OBJECT_TYPE_ERROR
          - MQRCCF_POLICY_NAME_ERROR
    response_parameters:
      - name: IgnoreState
        pcf_type: MQCFST
        type_hint: str
        enum_values:
          - MQIS_YES
          - MQIS_NO
          - MQRC_OBJECT_TYPE_ERROR
          - MQRCCF_POLICY_NAME_ERROR
    notes: []
  - name: MQCMD_DELETE_Q
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
        pcf_type: MQCFST
        type_hint: str
        enum_values:
          - MQIS_YES
          - MQIS_NO
          - MQRC_Q_NOT_EMPTY
    response_parameters:
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
        pcf_type: MQCFST
        type_hint: str
        enum_values:
          - MQIS_YES
          - MQIS_NO
          - MQRC_Q_NOT_EMPTY
    notes: []
  - name: MQCMD_DELETE_SERVICE
    request_href: SSFKSJ_9.4.0/refadmin/q087190_.html
    response_href: SSFKSJ_9.4.0/refadmin/q087190_.html
    request_parameters:
      - name: ServiceName
        pcf_type: MQCFST
        type_hint: str
      - name: IgnoreState
        pcf_type: MQCFST
        type_hint: str
        enum_values:
          - MQIS_YES
          - MQIS_NO
    response_parameters:
      - name: ServiceName
        pcf_type: MQCFST
        type_hint: str
      - name: IgnoreState
        pcf_type: MQCFST
        type_hint: str
        enum_values:
          - MQIS_YES
          - MQIS_NO
    notes: []
  - name: MQCMD_DELETE_STG_CLASS
    request_href: SSFKSJ_9.4.0/refadmin/q087200_.html
    response_href: SSFKSJ_9.4.0/refadmin/q087200_.html
    request_parameters:
      - name: StorageClassName
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
    response_parameters:
      - name: StorageClassName
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
    notes: []
  - name: MQCMD_DELETE_SUBSCRIPTION
    request_href: SSFKSJ_9.4.0/refadmin/q087210_.html
    response_href: SSFKSJ_9.4.0/refadmin/q087210_.html
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
    response_parameters:
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
    notes: []
  - name: MQCMD_DELETE_TOPIC
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
    notes: []
  - name: MQCMD_ESCAPE
    request_href: SSFKSJ_9.4.0/refadmin/q087230_.html
    response_href: SSFKSJ_9.4.0/refadmin/q087240_.html
    request_parameters:
      - name: EscapeType
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQET_MQSC
      - name: EscapeText
        pcf_type: MQCFST
        type_hint: str
        enum_values:
          - MQRCCF_ESCAPE_TYPE_ERROR
    response_parameters:
      - name: EscapeType
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQET_MQSC
      - name: EscapeText
        pcf_type: MQCFST
        type_hint: str
    notes: []
  - name: MQCMD_INQUIRE_APPL_STATUS
    request_href: SSFKSJ_9.4.0/refadmin/q133110_.html
    response_href: SSFKSJ_9.4.0/refadmin/q133120_.html
    request_parameters:
      - name: ApplicationName
        pcf_type: MQCFST
        type_hint: str
      - name: ApplicationInfoAttrs
        pcf_type: MQCFIL
        type_hint: list[int]
      - name: ApplicationStatusInfoType
        pcf_type: MQCFIN
        type_hint: int
      - name: ApplicationType
        pcf_type: MQCFIL
        type_hint: list[int]
      - name: BalancingOptions
        pcf_type: MQCFIL
        type_hint: list[int]
      - name: Connections
        pcf_type: MQCFIN
        type_hint: int
      - name: ConnectionTag
        pcf_type: MQCFBS
        type_hint: bytes
      - name: ImmovableCount
        pcf_type: MQCFIN
        type_hint: int
      - name: ImmovableDate
        pcf_type: MQCFST
        type_hint: str
      - name: ImmovableReason
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQIMMREASON_NONE
          - MQIMMREASON_NOT_CLIENT
          - MQIMMREASON_NOT_RECONNECTABLE
          - MQIMMREASON_MOVING
          - MQIMMREASON_APPLNAME_CHANGED
          - MQIMMREASON_IN_TRANSACTION
          - MQIMMREASON_TDQ_OPEN_INPUT
          - MQIMMREASON_AWAITS_REPLY
      - name: ImmovableTime
        pcf_type: MQCFST
        type_hint: str
      - name: IntegerFilterCommand
        pcf_type: MQCFIF
        type_hint: null
      - name: Movable
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQACTIVE_YES
          - MQACTIVE_NO
      - name: StringFilterCommand
        pcf_type: MQCFSF
        type_hint: null
      - name: Timeout
        pcf_type: MQCFIN
        type_hint: int
    response_parameters:
      - name: Balanced
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQBALANCED_NO
          - MQBALANCED_YES
          - MQBALANCED_NOT_APPLICABLE
          - MQBALANCED_UNKNOWN
      - name: ClusterName
        pcf_type: MQCFST
        type_hint: str
      - name: InstanceCount
        pcf_type: MQCFIN
        type_hint: int
      - name: MovableInstanceCount
        pcf_type: MQCFIN
        type_hint: int
      - name: BalanceState
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQBALSTATE_LOW
          - MQBALSTATE_OK
          - MQBALSTATE_HIGH
          - MQBALSTATE_NOT_APPLICABLE
          - MQBALSTATE_UNKNOWN
      - name: InstanceCount
        pcf_type: MQCFIN
        type_hint: int
      - name: LastMessageDate
        pcf_type: MQCFST
        type_hint: str
      - name: LastMessageTime
        pcf_type: MQCFST
        type_hint: str
      - name: MovableInstanceCount
        pcf_type: MQCFIN
        type_hint: int
      - name: QueueManagerActive
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQACTIVE_NO
          - MQACTIVE_YES
      - name: QueueManagerID
        pcf_type: MQCFST
        type_hint: str
      - name: QueueManagerName
        pcf_type: MQCFST
        type_hint: str
      - name: ApplicationType
        pcf_type: MQCFIL
        type_hint: list[int]
      - name: BalancingOptions
        pcf_type: MQCFIL
        type_hint: list[int]
      - name: Connections
        pcf_type: MQCFIN
        type_hint: int
      - name: ConnectionTag
        pcf_type: MQCFBS
        type_hint: bytes
      - name: ImmovableCount
        pcf_type: MQCFIN
        type_hint: int
      - name: ImmovableDate
        pcf_type: MQCFST
        type_hint: str
      - name: ImmovableReason
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQIMMREASON_NONE
          - MQIMMREASON_NOT_CLIENT
          - MQIMMREASON_NOT_RECONNECTABLE
          - MQIMMREASON_MOVING
          - MQIMMREASON_APPLNAME_CHANGED
          - MQIMMREASON_IN_TRANSACTION
          - MQIMMREASON_TDQ_OPEN_INPUT
          - MQIMMREASON_AWAITS_REPLY
      - name: ImmovableTime
        pcf_type: MQCFST
        type_hint: str
      - name: Movable
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQACTIVE_YES
          - MQACTIVE_NO
      - name: Timeout
        pcf_type: MQCFIN
        type_hint: int
    notes: []
  - name: MQCMD_INQUIRE_ARCHIVE
    request_href: SSFKSJ_9.4.0/refadmin/q087250_.html
    response_href: SSFKSJ_9.4.0/refadmin/q087260_.html
    request_parameters:
      - name: CommandScope
        pcf_type: MQCFST
        type_hint: str
    response_parameters:
      - name: AllocPrimary
        pcf_type: MQCFIN
        type_hint: int
      - name: AllocSecondary
        pcf_type: MQCFIN
        type_hint: int
      - name: AllocUnits
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQSYSP_ALLOC_BLK
          - MQSYSP_ALLOC_TRK
          - MQSYSP_ALLOC_CYL
      - name: ArchivePrefix1
        pcf_type: MQCFST
        type_hint: str
      - name: ArchivePrefix2
        pcf_type: MQCFST
        type_hint: str
      - name: ArchiveRetention
        pcf_type: MQCFIN
        type_hint: int
      - name: ArchiveUnit1
        pcf_type: MQCFST
        type_hint: str
      - name: ArchiveUnit2
        pcf_type: MQCFST
        type_hint: str
      - name: ArchiveWTOR
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQSYSP_YES
          - MQSYSP_NO
      - name: BlockSize
        pcf_type: MQCFIN
        type_hint: int
      - name: Catalog
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQSYSP_YES
          - MQSYSP_NO
      - name: Compact
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQSYSP_YES
          - MQSYSP_NO
      - name: Protect
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQSYSP_YES
          - MQSYSP_NO
      - name: QuiesceInterval
        pcf_type: MQCFIN
        type_hint: int
      - name: RoutingCode
        pcf_type: MQCFIL
        type_hint: list[int]
      - name: TimeStampFormat
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQSYSP_YES
          - MQSYSP_NO
          - MQSYSP_EXTENDED
      - name: DataSetName
        pcf_type: MQCFST
        type_hint: str
      - name: LogCorrelId
        pcf_type: MQCFST
        type_hint: str
      - name: UnitAddress
        pcf_type: MQCFIN
        type_hint: int
      - name: UnitStatus
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQSYSP_STATUS_BUSY
          - MQSYSP_STATUS_PREMOUNT
          - MQSYSP_STATUS_AVAILABLE
          - MQSYSP_STATUS_UNKNOWN
      - name: UnitVolser
        pcf_type: MQCFST
        type_hint: str
    notes: []
  - name: MQCMD_INQUIRE_AUTH_INFO
    request_href: SSFKSJ_9.4.0/refadmin/q087270_.html
    response_href: SSFKSJ_9.4.0/refadmin/q087280_.html
    request_parameters:
      - name: AuthInfoName
        pcf_type: MQCFST
        type_hint: str
      - name: AuthInfoAttrs
        pcf_type: MQCFIL
        type_hint: list[int]
        enum_values:
          - MQIACF_ALL
          - MQIA_ADOPT_CONTEXT
          - MQCA_ALTERATION_DATE
          - MQCA_ALTERATION_TIME
          - MQCA_AUTH_INFO_DESC
          - MQCA_AUTH_INFO_NAME
          - MQIA_AUTH_INFO_TYPE
          - MQCA_AUTH_INFO_CONN_NAME
          - MQIA_AUTHENTICATION_FAIL_DELAY
          - MQIA_AUTHENTICATION_METHOD
          - MQIA_CHECK_CLIENT_BINDING
          - MQIA_CHECK_LOCAL_BINDING
          - MQIA_LDAP_AUTHORMD
          - MQCA_LDAP_BASE_DN_GROUPS
          - MQCA_LDAP_BASE_DN_USERS
          - MQCA_LDAP_FIND_GROUP_FIELD
          - MQCA_LDAP_GROUP_ATTR_FIELD
          - MQCA_LDAP_GROUP_OBJECT_CLASS
          - MQIA_LDAP_NESTGRP
          - MQCA_LDAP_PASSWORD
          - MQIA_LDAP_SECURE_COMM
          - MQCA_LDAP_SHORT_USER_FIELD
          - MQCA_LDAP_USER_ATTR_FIELD
          - MQCA_LDAP_USER_NAME
          - MQCA_LDAP_USER_OBJECT_CLASS
          - MQCA_AUTH_INFO_OCSP_URL
      - name: AuthInfoType
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQAIT_CRL_LDAP
          - MQAIT_OCSP
          - MQAIT_IDPW_OS
          - MQAIT_IDPW_LDAP
          - MQAIT_ALL
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
      - name: AuthInfoConnName
        pcf_type: MQCFST
        type_hint: str
      - name: AuthInfoDesc
        pcf_type: MQCFST
        type_hint: str
      - name: AuthInfoName
        pcf_type: MQCFST
        type_hint: str
      - name: AuthInfoType
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQAIT_CRL_LDAP
          - MQAIT_OCSP
          - MQAIT_IDPW_OS
          - MQAIT_IDPW_LDAP
      - name: AuthenticationMethod
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQAUTHENTICATE_OS
          - MQAUTHENTICATE_PAM
      - name: AuthorizationMethod
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQLDAP_AUTHORMD_OS
          - MQLDAP_AUTHORMD_SEARCHGRP
          - MQLDAP_AUTHORMD_SEARCHUSER
          - MQLDAP_AUTHORMD_SRCHGRPSN
      - name: BaseDNGroup
        pcf_type: MQCFST
        type_hint: str
      - name: BaseDNUser
        pcf_type: MQCFST
        type_hint: str
        enum_values:
          - MQCHK_NONE
          - MQCHK_OPTIONAL
          - MQCHK_REQUIRED
          - MQCHK_REQUIRED_ADMIN
      - name: ClassGroup
        pcf_type: MQCFST
        type_hint: str
      - name: Classuser
        pcf_type: MQCFST
        type_hint: str
      - name: FailureDelay
        pcf_type: MQCFIN
        type_hint: int
      - name: FindGroup
        pcf_type: MQCFST
        type_hint: str
      - name: GroupField
        pcf_type: MQCFST
        type_hint: str
      - name: GroupNesting
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQLDAP_NESTGRP_NO
          - MQLDAP_NESTGRP_YES
      - name: LDAPPassword
        pcf_type: MQCFST
        type_hint: str
      - name: LDAPUserName
        pcf_type: MQCFST
        type_hint: str
      - name: OCSPResponderURL
        pcf_type: MQCFST
        type_hint: str
      - name: QSGDisposition
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQQSGD_COPY
          - MQQSGD_GROUP
          - MQQSGD_Q_MGR
      - name: SecureComms
        pcf_type: MQCFIN
        type_hint: int
      - name: ShortUser
        pcf_type: MQCFST
        type_hint: str
      - name: UserField
        pcf_type: MQCFST
        type_hint: str
    notes: []
  - name: MQCMD_INQUIRE_AUTH_INFO_NAMES
    request_href: SSFKSJ_9.4.0/refadmin/q087290_.html
    response_href: SSFKSJ_9.4.0/refadmin/q087300_.html
    request_parameters:
      - name: AuthInfoName
        pcf_type: MQCFST
        type_hint: str
      - name: AuthInfoType
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQAIT_CRL_LDAP
          - MQAIT_OCSP
          - MQAIT_ALL
      - name: CommandScope
        pcf_type: MQCFST
        type_hint: str
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
    response_parameters:
      - name: AuthInfoNames
        pcf_type: MQCFSL
        type_hint: list[str]
      - name: QSGDispositions
        pcf_type: MQCFIL
        type_hint: list[int]
        enum_values:
          - MQQSGD_COPY
          - MQQSGD_GROUP
          - MQQSGD_Q_MGR
      - name: AuthInfoTypes
        pcf_type: MQCFIL
        type_hint: list[int]
        enum_values:
          - MQAIT_CRL_LDAP
          - MQAIT_OCSP
          - MQAIT_IDPW_OS
    notes: []
  - name: MQCMD_INQUIRE_AUTH_RECS
    request_href: SSFKSJ_9.4.0/refadmin/q087310_.html
    response_href: SSFKSJ_9.4.0/refadmin/q087320_.html
    request_parameters:
      - name: Options
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQAUTHOPT_NAME_ALL_MATCHING
          - MQAUTHOPT_NAME_EXPLICIT
          - MQAUTHOPT_ENTITY_EXPLICIT
          - MQAUTHOPT_ENTITY_SET
          - MQAUTHOPT_NAME_AS_WILDCARD
      - name: ProfileName
        pcf_type: MQCFST
        type_hint: str
      - name: ObjectType
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQOT_ALL
          - MQOT_AUTH_INFO
          - MQOT_CHANNEL
          - MQOT_CLNTCONN_CHANNEL
          - MQOT_COMM_INFO
          - MQOT_LISTENER
          - MQOT_NAMELIST
          - MQOT_PROCESS
          - MQOT_Q
          - MQOT_Q_MGR
          - MQOT_REMOTE_Q_MGR_NAME
          - MQOT_SERVICE
          - MQOT_TOPIC
      - name: EntityName
        pcf_type: MQCFST
        type_hint: str
      - name: EntityType
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQZAET_GROUP
          - MQZAET_PRINCIPAL
      - name: ProfileAttrs
        pcf_type: MQCFIL
        type_hint: list[int]
        enum_values:
          - MQIACF_ALL
          - MQCACF_ENTITY_NAME
          - MQIACF_AUTHORIZATION_LIST
          - MQIACF_ENTITY_TYPE
      - name: ServiceComponent
        pcf_type: MQCFST
        type_hint: str
        enum_values:
          - MQRC_OBJECT_TYPE_ERROR
          - MQRC_UNKNOWN_ENTITY
          - MQRCCF_CFST_CONFLICTING_PARM
          - MQRCCF_PROFILE_NAME_ERROR
          - MQRCCF_ENTITY_NAME_MISSING
          - MQRCCF_OBJECT_TYPE_MISSING
          - MQRCCF_PROFILE_NAME_MISSING
    response_parameters:
      - name: AuthorizationList
        pcf_type: MQCFIL
        type_hint: list[int]
        enum_values:
          - MQAUTH_NONE
          - MQAUTH_ALT_USER_AUTHORITY
          - MQAUTH_BROWSE
          - MQAUTH_CHANGE
          - MQAUTH_CLEAR
          - MQAUTH_CONNECT
          - MQAUTH_CREATE
          - MQAUTH_DELETE
          - MQAUTH_DISPLAY
          - MQAUTH_INPUT
          - MQAUTH_INQUIRE
          - MQAUTH_OUTPUT
          - MQAUTH_PASS_ALL_CONTEXT
          - MQAUTH_PASS_IDENTITY_CONTEXT
          - MQAUTH_SET
          - MQAUTH_SET_ALL_CONTEXT
          - MQAUTH_SET_IDENTITY_CONTEXT
          - MQAUTH_CONTROL
          - MQAUTH_CONTROL_EXTENDED
          - MQAUTH_PUBLISH
          - MQAUTH_SUBSCRIBE
          - MQAUTH_RESUME
          - MQAUTH_SYSTEM
          - MQAUTH_ALL
          - MQAUTH_ALL_ADMIN
          - MQAUTH_ALL_MQI
      - name: EntityName
        pcf_type: MQCFST
        type_hint: str
      - name: EntityType
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQZAET_GROUP
          - MQZAET_PRINCIPAL
          - MQZAET_UNKNOWN
      - name: ObjectType
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQOT_AUTH_INFO
          - MQOT_CHANNEL
          - MQOT_CLNTCONN_CHANNEL
          - MQOT_COMM_INFO
          - MQOT_LISTENER
          - MQOT_NAMELIST
          - MQOT_PROCESS
          - MQOT_Q
          - MQOT_Q_MGR
          - MQOT_REMOTE_Q_MGR_NAME
          - MQOT_SERVICE
          - MQOT_TOPIC
      - name: Options
        pcf_type: MQCFIN
        type_hint: int
      - name: ProfileName
        pcf_type: MQCFST
        type_hint: str
      - name: QMgrName
        pcf_type: MQCFST
        type_hint: str
    notes: []
  - name: MQCMD_INQUIRE_AUTH_SERVICE
    request_href: SSFKSJ_9.4.0/refadmin/q087330_.html
    response_href: SSFKSJ_9.4.0/refadmin/q087340_.html
    request_parameters:
      - name: AuthServiceAttrs
        pcf_type: MQCFIL
        type_hint: list[int]
        enum_values:
          - MQIACF_ALL
          - MQIACF_INTERFACE_VERSION
          - MQIACF_USER_ID_SUPPORT
      - name: ServiceComponent
        pcf_type: MQCFST
        type_hint: str
        enum_values:
          - MQRC_SELECTOR_ERROR
          - MQRC_UNKNOWN_COMPONENT_NAME
    response_parameters:
      - name: InterfaceVersion
        pcf_type: MQCFIN
        type_hint: int
      - name: ServiceComponent
        pcf_type: MQCFSL
        type_hint: list[str]
      - name: UserIDSupport
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQUIDSUPP_YES
          - MQUIDSUPP_NO
    notes: []
  - name: MQCMD_INQUIRE_CF_STRUC
    request_href: SSFKSJ_9.4.0/refadmin/q087350_.html
    response_href: SSFKSJ_9.4.0/refadmin/q087360_.html
    request_parameters:
      - name: CFStrucName
        pcf_type: MQCFST
        type_hint: str
      - name: CFStrucAttrs
        pcf_type: MQCFIL
        type_hint: list[int]
        enum_values:
          - MQIACF_ALL
          - MQCA_ALTERATION_DATE
          - MQCA_ALTERATION_TIME
          - MQIA_CF_CFCONLOS
          - MQIA_CF_LEVEL
          - MQIA_CF_OFFLOAD
          - MQIA_CF_RECOVER
          - MQIA_CF_RECAUTO
          - MQIACF_CF_SMDS_BLOCK_SIZE
          - MQIA_CF_SMDS_BUFFERS
          - MQIACF_CF_SMDS_EXPAND
          - MQCACF_CF_SMDS_GENERIC_NAME
          - MQCA_CF_STRUC_DESC
          - MQCA_CF_STRUC_NAME
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
      - name: CFConlos
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQCFCONLOS_TERMINATE
          - MQCFCONLOS_TOLERATE
          - MQCFCONLOS_ASQMGR
      - name: CFLevel
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - 1
          - 2
          - 3
          - 4
          - 5
      - name: CFStrucDesc
        pcf_type: MQCFST
        type_hint: str
      - name: CFStrucName
        pcf_type: MQCFST
        type_hint: str
      - name: DSBLOCK
        pcf_type: MQCFIN
        type_hint: int
      - name: DSBUFS
        pcf_type: MQCFIN
        type_hint: int
      - name: DSEXPAND
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQDSE_YES
          - MQDSE_NO
          - MQDSE_DEFAULT
      - name: DSGROUP
        pcf_type: MQCFST
        type_hint: str
      - name: OFFLD1SZ
        pcf_type: MQCFST
        type_hint: str
      - name: OFFLD2SZ
        pcf_type: MQCFST
        type_hint: str
      - name: OFFLD3SZ
        pcf_type: MQCFST
        type_hint: str
      - name: OFFLD1TH
        pcf_type: MQCFIN
        type_hint: int
      - name: OFFLD2TH
        pcf_type: MQCFIN
        type_hint: int
      - name: OFFLD3TH
        pcf_type: MQCFIN
        type_hint: int
      - name: Offload
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQCFOFFLD_DB2
          - MQCFOFFLD_SMDS
          - MQCFOFFLD_NONE
      - name: RCVDATE
        pcf_type: MQCFST
        type_hint: str
      - name: RCVTIME
        pcf_type: MQCFST
        type_hint: str
      - name: Recauto
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQRECAUTO_YES
          - MQRECAUTO_NO
      - name: Recovery
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQCFR_YES
          - MQCFR_NO
    notes: []
  - name: MQCMD_INQUIRE_CF_STRUC_NAMES
    request_href: SSFKSJ_9.4.0/refadmin/q087370_.html
    response_href: SSFKSJ_9.4.0/refadmin/q087380_.html
    request_parameters:
      - name: CFStrucName
        pcf_type: MQCFST
        type_hint: str
    response_parameters:
      - name: CFStrucNames
        pcf_type: MQCFSL
        type_hint: list[str]
    notes: []
  - name: MQCMD_INQUIRE_CF_STRUC_STATUS
    request_href: SSFKSJ_9.4.0/refadmin/q087390_.html
    response_href: SSFKSJ_9.4.0/refadmin/q087400_.html
    request_parameters:
      - name: CFStrucName
        pcf_type: MQCFST
        type_hint: str
      - name: CFStatusType
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQIACF_CF_STATUS_SUMMARY
          - MQIACF_CF_STATUS_CONNECT
          - MQIACF_CF_STATUS_BACKUP
          - MQIACF_CF_STATUS_SMDS
      - name: IntegerFilterCommand
        pcf_type: MQCFIF
        type_hint: null
      - name: StringFilterCommand
        pcf_type: MQCFSF
        type_hint: null
    response_parameters:
      - name: Access
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQCFACCESS_ENABLED
          - MQCFACCESS_SUSPENDED
          - MQCFACCESS_DISABLED
      - name: BackupDate
        pcf_type: MQCFST
        type_hint: str
      - name: BackupEndRBA
        pcf_type: MQCFST
        type_hint: str
      - name: BackupSize
        pcf_type: MQCFIN
        type_hint: int
      - name: BackupStartRBA
        pcf_type: MQCFST
        type_hint: str
      - name: BackupTime
        pcf_type: MQCFST
        type_hint: str
      - name: CFStatusType
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQIACF_CF_STATUS_SUMMARY
          - MQIACF_CF_STATUS_CONNECT
          - MQIACF_CF_STATUS_BACKUP
          - MQIACF_CF_STATUS_SMDS
      - name: CFStrucName
        pcf_type: MQCFST
        type_hint: str
      - name: CFStrucStatus
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQCFSTATUS_ACTIVE
          - MQCFSTATUS_FAILED
          - MQCFSTATUS_NOT_FOUND
          - MQCFSTATUS_IN_BACKUP
          - MQCFSTATUS_IN_RECOVER
          - MQCFSTATUS_UNKNOWN
          - MQCFSTATUS_NONE
          - MQCFSTATUS_RECOVERED
          - MQCFSTATUS_EMPTY
          - MQCFSTATUS_NEW
      - name: CFStrucType
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQCFTYPE_ADMIN
          - MQCFTYPE_APPL
      - name: EntriesMax
        pcf_type: MQCFIN
        type_hint: int
      - name: EntriesUsed
        pcf_type: MQCFIN
        type_hint: int
      - name: FailDate
        pcf_type: MQCFST
        type_hint: str
      - name: FailTime
        pcf_type: MQCFST
        type_hint: str
      - name: LogQMgrNames
        pcf_type: MQCFSL
        type_hint: list[str]
      - name: OffLdUse
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQCFOFFLD_DB2
          - MQCFOFFLD_SMDS
          - MQCFOFFLD_NONE
          - MQCFOFFLD_BOTH
      - name: QMgrName
        pcf_type: MQCFST
        type_hint: str
      - name: RcvDate
        pcf_type: MQCFST
        type_hint: str
      - name: RcvTime
        pcf_type: MQCFST
        type_hint: str
      - name: SizeMax
        pcf_type: MQCFIN
        type_hint: int
      - name: SizeUsed
        pcf_type: MQCFIN
        type_hint: int
      - name: SysName
        pcf_type: MQCFST
        type_hint: str
      - name: SizeMax
        pcf_type: MQCFIN
        type_hint: int
    notes: []
  - name: MQCMD_INQUIRE_CHANNEL
    request_href: SSFKSJ_9.4.0/refadmin/q087410_.html
    response_href: SSFKSJ_9.4.0/refadmin/q087430_.html
    request_parameters:
      - name: ChannelName
        pcf_type: MQCFST
        type_hint: str
      - name: ChannelAttrs
        pcf_type: MQCFIL
        type_hint: list[int]
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
        type_hint: list[int]
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
        type_hint: list[int]
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
    notes: []
  - name: MQCMD_INQUIRE_CHANNEL_INIT
    request_href: SSFKSJ_9.4.0/refadmin/q087460_.html
    response_href: SSFKSJ_9.4.0/refadmin/q087470_.html
    request_parameters:
      - name: CommandScope
        pcf_type: MQCFST
        type_hint: str
    response_parameters:
      - name: ActiveChannels
        pcf_type: MQCFIN
        type_hint: int
      - name: ActiveChannelsMax
        pcf_type: MQCFIN
        type_hint: int
      - name: ActiveChannelsPaused
        pcf_type: MQCFIN
        type_hint: int
      - name: ActiveChannelsRetrying
        pcf_type: MQCFIN
        type_hint: int
      - name: ActiveChannelsStarted
        pcf_type: MQCFIN
        type_hint: int
      - name: ActiveChannelsStopped
        pcf_type: MQCFIN
        type_hint: int
      - name: AdaptersMax
        pcf_type: MQCFIN
        type_hint: int
      - name: AdaptersStarted
        pcf_type: MQCFIN
        type_hint: int
      - name: ChannelInitiatorStatus
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQSVC_STATUS_STOPPED
          - MQSVC_STATUS_RUNNING
      - name: CurrentChannels
        pcf_type: MQCFIN
        type_hint: int
      - name: CurrentChannelsLU62
        pcf_type: MQCFIN
        type_hint: int
      - name: CurrentChannelsMax
        pcf_type: MQCFIN
        type_hint: int
      - name: CurrentChannelsTCP
        pcf_type: MQCFIN
        type_hint: int
      - name: DispatchersMax
        pcf_type: MQCFIN
        type_hint: int
      - name: DispatchersStarted
        pcf_type: MQCFIN
        type_hint: int
      - name: SSLTasksMax
        pcf_type: MQCFIN
        type_hint: int
      - name: SSLTasksStarted
        pcf_type: MQCFIN
        type_hint: int
      - name: TCPName
        pcf_type: MQCFST
        type_hint: str
      - name: InboundDisposition
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQINBD_Q_MGR
          - MQINBD_GROUP
      - name: IPAddress
        pcf_type: MQCFST
        type_hint: str
      - name: ListenerStatus
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQSVC_STATUS_RUNNING
          - MQSVC_STATUS_STOPPED
          - MQSVC_STATUS_RETRYING
      - name: LUName
        pcf_type: MQCFST
        type_hint: str
      - name: Port
        pcf_type: MQCFIN
        type_hint: int
      - name: TransportType
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQXPT_LU62
          - MQXPT_TCP
    notes: []
  - name: MQCMD_INQUIRE_CHANNEL_NAMES
    request_href: SSFKSJ_9.4.0/refadmin/q087520_.html
    response_href: SSFKSJ_9.4.0/refadmin/q087530_.html
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
          - MQCHT_ALL
      - name: CommandScope
        pcf_type: MQCFST
        type_hint: str
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
          - MQRCCF_CHANNEL_NAME_ERROR
          - MQRCCF_CHANNEL_TYPE_ERROR
    response_parameters:
      - name: ChannelNames
        pcf_type: MQCFSL
        type_hint: list[str]
      - name: ChannelTypes
        pcf_type: MQCFIL
        type_hint: list[int]
      - name: QSGDispositions
        pcf_type: MQCFIL
        type_hint: list[int]
        enum_values:
          - MQQSGD_COPY
          - MQQSGD_GROUP
          - MQQSGD_Q_MGR
    notes: []
  - name: MQCMD_INQUIRE_CHANNEL_STATUS
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
        type_hint: list[int]
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
        type_hint: list[int]
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
        type_hint: list[int]
      - name: CompressionTime
        pcf_type: MQCFIL
        type_hint: list[int]
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
        type_hint: list[int]
      - name: HeaderCompression
        pcf_type: MQCFIL
        type_hint: list[int]
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
        type_hint: list[int]
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
        type_hint: list[int]
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
        type_hint: list[int]
    notes: []
  - name: MQCMD_INQUIRE_CHLAUTH_RECS
    request_href: SSFKSJ_9.4.0/refadmin/q087440_.html
    response_href: SSFKSJ_9.4.0/refadmin/q087450_.html
    request_parameters:
      - name: Address
        pcf_type: MQCFST
        type_hint: str
      - name: ByteStringFilterCommand
        pcf_type: MQCFBF
        type_hint: null
      - name: ChannelAuthAttrs
        pcf_type: MQCFIL
        type_hint: list[int]
        enum_values:
          - MQIACF_ALL
          - MQCA_ALTERATION_DATE
          - MQCA_ALTERATION_TIME
          - MQCA_CHLAUTH_DESC
          - MQCA_CUSTOM
          - MQCACH_CONNECTION_NAME
          - MQCACH_MCA_USER_ID
          - MQIACH_USER_SOURCE
          - MQIACH_WARNING
      - name: CheckClient
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQCHK_REQUIRED_ADMIN
          - MQCHK_REQUIRED
          - MQCHK_AS_Q_MGR
      - name: ClntUser
        pcf_type: MQCFST
        type_hint: str
      - name: CommandScope
        pcf_type: MQCFST
        type_hint: str
      - name: IntegerFilterCommand
        pcf_type: MQCFIF
        type_hint: null
      - name: Match
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQMATCH_RUNCHECK
          - MQMATCH_EXACT
          - MQMATCH_GENERIC
          - MQMATCH_ALL
      - name: QMName
        pcf_type: MQCFST
        type_hint: str
      - name: SSLCertIssuer
        pcf_type: MQCFST
        type_hint: str
      - name: SSLPeer
        pcf_type: MQCFST
        type_hint: str
      - name: StringFilterCommand
        pcf_type: MQCFSF
        type_hint: null
      - name: Type
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQCAUT_BLOCKUSER
          - MQCAUT_BLOCKADDR
          - MQCAUT_SSLPEERMAP
          - MQCAUT_ADDRESSMAP
          - MQCAUT_USERMAP
          - MQCAUT_QMGRMAP
          - MQCAUT_ALL
    response_parameters:
      - name: AlterationDate
        pcf_type: MQCFST
        type_hint: str
      - name: AlterationTime
        pcf_type: MQCFST
        type_hint: str
      - name: Address
        pcf_type: MQCFST
        type_hint: str
      - name: AddrList
        pcf_type: MQCFSL
        type_hint: list[str]
      - name: Chlauth
        pcf_type: MQCFST
        type_hint: str
      - name: CheckClient
        pcf_type: MQCFIN
        type_hint: int
      - name: ClntUser
        pcf_type: MQCFST
        type_hint: str
      - name: Description
        pcf_type: MQCFST
        type_hint: str
      - name: MCAUser
        pcf_type: MQCFST
        type_hint: str
      - name: QMName
        pcf_type: MQCFST
        type_hint: str
      - name: SSLCertIssuer
        pcf_type: MQCFST
        type_hint: str
      - name: SSLPeer
        pcf_type: MQCFST
        type_hint: str
      - name: Type
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQCAUT_BLOCKUSER
          - MQCAUT_BLOCKADDR
          - MQCAUT_SSLPEERMAP
          - MQCAUT_ADDRESSMAP
          - MQCAUT_USERMAP
          - MQCAUT_QMGRMAP
      - name: UserList
        pcf_type: MQCFSL
        type_hint: list[str]
      - name: UserSrc
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQUSRC_MAP
          - MQUSRC_NOACCESS
          - MQUSRC_CHANNEL
      - name: Warn
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQWARN_NO
          - MQWARN_YES
    notes: []
  - name: MQCMD_INQUIRE_CLUSTER_Q_MGR
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
        type_hint: list[int]
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
        type_hint: list[int]
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
        type_hint: list[int]
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
    notes: []
  - name: MQCMD_INQUIRE_COMM_INFO
    request_href: SSFKSJ_9.4.0/refadmin/q087600_.html
    response_href: SSFKSJ_9.4.0/refadmin/q087610_.html
    request_parameters:
      - name: ComminfoName
        pcf_type: MQCFST
        type_hint: str
      - name: ComminfoAttrs
        pcf_type: MQCFIL
        type_hint: list[int]
        enum_values:
          - MQIACF_ALL
          - MQIA_CODED_CHAR_SET_ID
          - MQIA_COMM_EVENT
          - MQIA_MCAST_BRIDGE
          - MQIA_MONITOR_INTERVAL
          - MQIACF_ENCODING
          - MQIACH_MC_HB_INTERVAL
          - MQIACH_MSG_HISTORY
          - MQIACH_MULTICAST_PROPERTIES
          - MQIACH_NEW_SUBSCRIBER_HISTORY
          - MQIACH_PORT
          - MQCA_ALTERATION_DATE
          - MQCA_ALTERATION_TIME
          - MQCA_COMM_INFO_DESC
          - MQCA_COMM_INFO_TYPE
          - MQCACH_GROUP_ADDRESS
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
      - name: Bridge
        pcf_type: MQCFIN
        type_hint: int
      - name: CCSID
        pcf_type: MQCFIN
        type_hint: int
      - name: CommEvent
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQEVR_DISABLED
          - MQEVR_ENABLED
          - MQEVR_EXCEPTION
      - name: ComminfoName
        pcf_type: MQCFST
        type_hint: str
      - name: Description
        pcf_type: MQCFST
        type_hint: str
      - name: Encoding
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQENC_AS_PUBLISHED
          - MQENC_NORMAL
          - MQENC_REVERSED
          - MQENC_S390
          - MQENC_TNS
      - name: GrpAddress
        pcf_type: MQCFST
        type_hint: str
      - name: MonitorInterval
        pcf_type: MQCFIN
        type_hint: int
      - name: MulticastHeartbeat
        pcf_type: MQCFIN
        type_hint: int
      - name: MulticastPropControl
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQMCP_ALL
          - MQMAP_REPLY
          - MQMAP_USER
          - MQMAP_NONE
          - MQMAP_COMPAT
      - name: MsgHistory
        pcf_type: MQCFIN
        type_hint: int
      - name: NewSubHistory
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQNSH_NONE
          - MQNSH_ALL
      - name: PortNumber
        pcf_type: MQCFIN
        type_hint: int
      - name: Type
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQCIT_MULTICAST
    notes: []
  - name: MQCMD_INQUIRE_CONNECTION
    request_href: SSFKSJ_9.4.0/refadmin/q087620_.html
    response_href: SSFKSJ_9.4.0/refadmin/q087630_.html
    request_parameters:
      - name: ConnectionId
        pcf_type: MQCFBS
        type_hint: bytes
      - name: GenericConnectionId
        pcf_type: MQCFBS
        type_hint: bytes
      - name: ByteStringFilterCommand
        pcf_type: MQCFBF
        type_hint: null
      - name: CommandScope
        pcf_type: MQCFST
        type_hint: str
      - name: ConnectionAttrs
        pcf_type: MQCFIL
        type_hint: list[int]
        enum_values:
          - MQIACF_ALL
          - MQBACF_CONNECTION_ID
          - MQBACF_CONN_TAG
          - MQBACF_EXTERNAL_UOW_ID
          - MQBACF_ORIGIN_UOW_ID
          - MQBACF_Q_MGR_UOW_ID
          - MQCACF_APPL_TAG
          - MQCACF_ASID
          - MQCACF_ORIGIN_NAME
          - MQCACF_PSB_NAME
          - MQCACF_PST_ID
          - MQCACF_TASK_NUMBER
          - MQCACF_TRANSACTION_ID
          - MQCACF_UOW_LOG_EXTENT_NAME
          - MQCACF_UOW_LOG_START_DATE
          - MQCACF_UOW_LOG_START_TIME
          - MQCACF_UOW_START_DATE
          - MQCACF_UOW_START_TIME
          - MQCACF_USER_IDENTIFIER
          - MQCACH_CHANNEL_NAME
          - MQCACH_CONNECTION_NAME
          - MQIA_APPL_TYPE
          - MQIACF_CONNECT_OPTIONS
          - MQIACF_PROCESS_ID
          - MQIACF_THREAD_ID
          - MQIACF_UOW_STATE
          - MQIACF_UOW_TYPE
          - MQCACF_OBJECT_NAME
          - MQIA_QSG_DISP
          - MQIA_READ_AHEAD
          - MQIA_UR_DISP
          - MQIACF_HANDLE_STATE
          - MQIACF_OBJECT_TYPE
          - MQIACF_OPEN_OPTIONS
      - name: ConnInfoType
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQIACF_CONN_INFO_CONN
          - MQIACF_CONN_INFO_HANDLE
          - MQIACF_CONN_INFO_ALL
      - name: IntegerFilterCommand
        pcf_type: MQCFIF
        type_hint: null
      - name: StringFilterCommand
        pcf_type: MQCFSF
        type_hint: null
      - name: URDisposition
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQQSGD_ALL
          - MQQSGD_GROUP
          - MQQSGD_Q_MGR
          - MQRCCF_CONNECTION_ID_ERROR
    response_parameters:
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
      - name: ASID
        pcf_type: MQCFST
        type_hint: str
      - name: AsynchronousState
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQAS_NONE
          - MQAS_SUSPENDED
          - MQAS_SUSPENDED_TEMPORARY
          - MQAS_STARTED
          - MQAS_START_WAIT
          - MQAS_STOPPED
          - MQAS_ACTIVE
          - MQAS_INACTIVE
      - name: ChannelName
        pcf_type: MQCFST
        type_hint: str
      - name: ClientId
        pcf_type: MQCFST
        type_hint: str
      - name: ConnectionId
        pcf_type: MQCFBS
        type_hint: bytes
      - name: ConnectionName
        pcf_type: MQCFST
        type_hint: str
      - name: ConnectionOptions
        pcf_type: MQCFIL
        type_hint: list[int]
      - name: ConnectionTag
        pcf_type: MQCFBS
        type_hint: bytes
      - name: ConnInfoType
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQIACF_CONN_INFO_CONN
          - MQIACF_CONN_INFO_HANDLE
      - name: Destination
        pcf_type: MQCFST
        type_hint: str
      - name: DestinationQueueManager
        pcf_type: MQCFST
        type_hint: str
      - name: HandleState
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQHSTATE_ACTIVE
          - MQHSTATE_INACTIVE
      - name: ObjectName
        pcf_type: MQCFST
        type_hint: str
      - name: ObjectType
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQOT_Q
          - MQOT_NAMELIST
          - MQOT_PROCESS
          - MQOT_Q_MGR
          - MQOT_CHANNEL
          - MQOT_AUTH_INFO
          - MQOT_TOPIC
      - name: OpenOptions
        pcf_type: MQCFIN
        type_hint: int
      - name: OriginName
        pcf_type: MQCFST
        type_hint: str
      - name: OriginUOWId
        pcf_type: MQCFBS
        type_hint: bytes
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
      - name: QSGDispositon
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQQSGD_COPY
          - MQQSGD_Q_MGR
          - MQQSGD_SHARED
      - name: ReadAhead
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQREADA_NO
          - MQREADA_YES
          - MQREADA_BACKLOG
          - MQREADA_INHIBITED
      - name: StartUOWLogExtent
        pcf_type: MQCFST
        type_hint: str
      - name: SubscriptionID
        pcf_type: MQCFBS
        type_hint: bytes
      - name: SubscriptionName
        pcf_type: MQCFST
        type_hint: str
      - name: ThreadId
        pcf_type: MQCFIN
        type_hint: int
      - name: TopicString
        pcf_type: MQCFST
        type_hint: str
      - name: TransactionId
        pcf_type: MQCFST
        type_hint: str
      - name: UOWIdentifier
        pcf_type: MQCFBS
        type_hint: bytes
      - name: UOWLogStartDate
        pcf_type: MQCFST
        type_hint: str
      - name: UOWLogStartTime
        pcf_type: MQCFST
        type_hint: str
      - name: UOWStartDate
        pcf_type: MQCFST
        type_hint: str
      - name: UOWStartTime
        pcf_type: MQCFST
        type_hint: str
      - name: UOWState
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQUOWST_NONE
          - MQUOWST_ACTIVE
          - MQUOWST_PREPARED
          - MQUOWST_UNRESOLVED
      - name: UOWType
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQUOWT_Q_MGR
          - MQUOWT_CICS
          - MQUOWT_RRS
          - MQUOWT_IMS
          - MQUOWT_XA
      - name: URDisposition
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQQSGD_GROUP
          - MQQSGD_Q_MGR
      - name: UserId
        pcf_type: MQCFST
        type_hint: str
    notes: []
  - name: MQCMD_INQUIRE_ENTITY_AUTH
    request_href: SSFKSJ_9.4.0/refadmin/q087640_.html
    response_href: SSFKSJ_9.4.0/refadmin/q087650_.html
    request_parameters:
      - name: EntityName
        pcf_type: MQCFST
        type_hint: str
      - name: EntityType
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQZAET_GROUP
          - MQZAET_PRINCIPAL
      - name: ObjectType
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQOT_AUTH_INFO
          - MQOT_CHANNEL
          - MQOT_CLNTCONN_CHANNEL
          - MQOT_COMM_INFO
          - MQOT_LISTENER
          - MQOT_NAMELIST
          - MQOT_PROCESS
          - MQOT_Q
          - MQOT_Q_MGR
          - MQOT_REMOTE_Q_MGR_NAME
          - MQOT_SERVICE
          - MQOT_TOPIC
      - name: Options
        pcf_type: MQCFIN
        type_hint: int
      - name: ObjectName
        pcf_type: MQCFST
        type_hint: str
      - name: ProfileAttrs
        pcf_type: MQCFIL
        type_hint: list[int]
        enum_values:
          - MQIACF_ALL
          - MQCACF_ENTITY_NAME
          - MQIACF_AUTHORIZATION_LIST
          - MQIACF_ENTITY_TYPE
          - MQIACF_OBJECT_TYPE
      - name: ServiceComponent
        pcf_type: MQCFST
        type_hint: str
        enum_values:
          - MQRC_UNKNOWN_ENTITY
          - MQRCCF_OBJECT_TYPE_MISSING
    response_parameters:
      - name: AuthorizationList
        pcf_type: MQCFIL
        type_hint: list[int]
        enum_values:
          - MQAUTH_NONE
          - MQAUTH_ALT_USER_AUTHORITY
          - MQAUTH_BROWSE
          - MQAUTH_CHANGE
          - MQAUTH_CLEAR
          - MQAUTH_CONNECT
          - MQAUTH_CREATE
          - MQAUTH_DELETE
          - MQAUTH_DISPLAY
          - MQAUTH_INPUT
          - MQAUTH_INQUIRE
          - MQAUTH_OUTPUT
          - MQAUTH_PASS_ALL_CONTEXT
          - MQAUTH_PASS_IDENTITY_CONTEXT
          - MQAUTH_SET
          - MQAUTH_SET_ALL_CONTEXT
          - MQAUTH_SET_IDENTITY_CONTEXT
          - MQAUTH_CONTROL
          - MQAUTH_CONTROL_EXTENDED
          - MQAUTH_PUBLISH
          - MQAUTH_SUBSCRIBE
          - MQAUTH_RESUME
          - MQAUTH_SYSTEM
          - MQAUTH_ALL
          - MQAUTH_ALL_ADMIN
          - MQAUTH_ALL_MQI
      - name: EntityName
        pcf_type: MQCFST
        type_hint: str
      - name: EntityType
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQZAET_GROUP
          - MQZAET_PRINCIPAL
          - MQZAET_UNKNOWN
      - name: ObjectName
        pcf_type: MQCFST
        type_hint: str
      - name: ObjectType
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQOT_AUTH_INFO
          - MQOT_CHANNEL
          - MQOT_CLNTCONN_CHANNEL
          - MQOT_COMM_INFO
          - MQOT_LISTENER
          - MQOT_NAMELIST
          - MQOT_PROCESS
          - MQOT_Q
          - MQOT_Q_MGR
          - MQOT_REMOTE_Q_MGR_NAME
          - MQOT_SERVICE
      - name: QMgrName
        pcf_type: MQCFST
        type_hint: str
    notes: []
  - name: MQCMD_INQUIRE_LISTENER
    request_href: SSFKSJ_9.4.0/refadmin/q087480_.html
    response_href: SSFKSJ_9.4.0/refadmin/q087490_.html
    request_parameters:
      - name: ListenerName
        pcf_type: MQCFST
        type_hint: str
      - name: IntegerFilterCommand
        pcf_type: MQCFIF
        type_hint: null
      - name: ListenerAttrs
        pcf_type: MQCFIL
        type_hint: list[int]
        enum_values:
          - MQIACF_ALL
          - MQCA_ALTERATION_DATE
          - MQCA_ALTERATION_TIME
          - MQCACH_IP_ADDRESS
          - MQCACH_LISTENER_DESC
          - MQCACH_LISTENER_NAME
          - MQCACH_LOCAL_NAME
          - MQCACH_TP_NAME
          - MQIACH_ADAPTER
          - MQIACH_BACKLOG
          - MQIACH_COMMAND_COUNT
          - MQIACH_LISTENER_CONTROL
          - MQIACH_NAME_COUNT
          - MQIACH_PORT
          - MQIACH_SESSION_COUNT
          - MQIACH_SOCKET
      - name: StringFilterCommand
        pcf_type: MQCFSF
        type_hint: null
      - name: TransportType
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQXPT_ALL
          - MQXPT_LU62
          - MQXPT_NETBIOS
          - MQXPT_SPX
          - MQXPT_TCP
    response_parameters:
      - name: AlterationDate
        pcf_type: MQCFST
        type_hint: str
      - name: AlterationTime
        pcf_type: MQCFST
        type_hint: str
      - name: Adapter
        pcf_type: MQCFIN
        type_hint: int
      - name: Backlog
        pcf_type: MQCFIN
        type_hint: int
      - name: Commands
        pcf_type: MQCFIN
        type_hint: int
      - name: IPAddress
        pcf_type: MQCFST
        type_hint: str
      - name: ListenerDesc
        pcf_type: MQCFST
        type_hint: str
      - name: ListenerName
        pcf_type: MQCFST
        type_hint: str
      - name: LocalName
        pcf_type: MQCFST
        type_hint: str
      - name: NetbiosNames
        pcf_type: MQCFIN
        type_hint: int
      - name: Port
        pcf_type: MQCFIN
        type_hint: int
      - name: Sessions
        pcf_type: MQCFIN
        type_hint: int
      - name: Socket
        pcf_type: MQCFIN
        type_hint: int
      - name: StartMode
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQSVC_CONTROL_MANUAL
          - MQSVC_CONTROL_Q_MGR
          - MQSVC_CONTROL_Q_MGR_START
      - name: TPName
        pcf_type: MQCFST
        type_hint: str
      - name: TransportType
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQXPT_TCP
          - MQXPT_LU62
          - MQXPT_NETBIOS
          - MQXPT_SPX
    notes: []
  - name: MQCMD_INQUIRE_LISTENER_STATUS
    request_href: SSFKSJ_9.4.0/refadmin/q087500_.html
    response_href: SSFKSJ_9.4.0/refadmin/q087510_.html
    request_parameters:
      - name: ListenerName
        pcf_type: MQCFST
        type_hint: str
      - name: IntegerFilterCommand
        pcf_type: MQCFIF
        type_hint: null
      - name: ListenerStatusAttrs
        pcf_type: MQCFIL
        type_hint: list[int]
        enum_values:
          - MQIACF_ALL
          - MQCACH_IP_ADDRESS
          - MQCACH_LISTENER_DESC
          - MQCACH_LISTENER_NAME
          - MQCACH_LISTENER_START_DATE
          - MQCACH_LISTENER_START_TIME
          - MQCACH_LOCAL_NAME
          - MQCACH_TP_NAME
          - MQIACF_PROCESS_ID
          - MQIACH_ADAPTER
          - MQIACH_BACKLOG
          - MQIACH_COMMAND_COUNT
          - MQIACH_LISTENER_CONTROL
          - MQIACH_LISTENER_STATUS
          - MQIACH_NAME_COUNT
          - MQIACH_PORT
          - MQIACH_SESSION_COUNT
          - MQIACH_SOCKET
          - MQIACH_XMIT_PROTOCOL_TYPE
      - name: StringFilterCommand
        pcf_type: MQCFSF
        type_hint: null
        enum_values:
          - MQRCCF_LSTR_STATUS_NOT_FOUND
    response_parameters:
      - name: Adapter
        pcf_type: MQCFIN
        type_hint: int
      - name: Backlog
        pcf_type: MQCFIN
        type_hint: int
      - name: Commands
        pcf_type: MQCFIN
        type_hint: int
      - name: IPAddress
        pcf_type: MQCFST
        type_hint: str
      - name: ListenerDesc
        pcf_type: MQCFST
        type_hint: str
      - name: ListenerName
        pcf_type: MQCFST
        type_hint: str
      - name: LocalName
        pcf_type: MQCFST
        type_hint: str
      - name: NetbiosNames
        pcf_type: MQCFIN
        type_hint: int
      - name: Port
        pcf_type: MQCFIN
        type_hint: int
      - name: ProcessId
        pcf_type: MQCFIN
        type_hint: int
      - name: Sessions
        pcf_type: MQCFIN
        type_hint: int
      - name: Socket
        pcf_type: MQCFIN
        type_hint: int
      - name: StartDate
        pcf_type: MQCFST
        type_hint: str
      - name: StartMode
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQSVC_CONTROL_MANUAL
          - MQSVC_CONTROL_Q_MGR
          - MQSVC_CONTROL_Q_MGR_START
      - name: StartTime
        pcf_type: MQCFST
        type_hint: str
      - name: Status
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQSVC_STATUS_STARTING
          - MQSVC_STATUS_RUNNING
          - MQSVC_STATUS_STOPPING
      - name: TPName
        pcf_type: MQCFST
        type_hint: str
      - name: TransportType
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQXPT_TCP
          - MQXPT_LU62
          - MQXPT_NETBIOS
          - MQXPT_SPX
    notes: []
  - name: MQCMD_INQUIRE_LOG
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
    notes: []
  - name: MQCMD_INQUIRE_NAMELIST
    request_href: SSFKSJ_9.4.0/refadmin/q087700_.html
    response_href: SSFKSJ_9.4.0/refadmin/q087710_.html
    request_parameters:
      - name: NamelistName
        pcf_type: MQCFST
        type_hint: str
      - name: CommandScope
        pcf_type: MQCFST
        type_hint: str
      - name: IntegerFilterCommand
        pcf_type: MQCFIF
        type_hint: null
      - name: NamelistAttrs
        pcf_type: MQCFIL
        type_hint: list[int]
        enum_values:
          - MQIACF_ALL
          - MQCA_NAMELIST_NAME
          - MQCA_NAMELIST_DESC
          - MQCA_NAMES
          - MQCA_ALTERATION_DATE
          - MQCA_ALTERATION_TIME
          - MQIA_NAME_COUNT
          - MQIA_NAMELIST_TYPE
      - name: NamelistType
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQNT_NONE
          - MQNT_Q
          - MQNT_CLUSTER
          - MQNT_AUTH_INFO
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
      - name: NameCount
        pcf_type: MQCFIN
        type_hint: int
      - name: NamelistDesc
        pcf_type: MQCFST
        type_hint: str
      - name: NamelistName
        pcf_type: MQCFST
        type_hint: str
      - name: NamelistType
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQNT_NONE
          - MQNT_Q
          - MQNT_CLUSTER
          - MQNT_AUTH_INFO
      - name: Names
        pcf_type: MQCFSL
        type_hint: list[str]
      - name: QSGDisposition
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQQSGD_COPY
          - MQQSGD_GROUP
          - MQQSGD_Q_MGR
    notes: []
  - name: MQCMD_INQUIRE_NAMELIST_NAMES
    request_href: SSFKSJ_9.4.0/refadmin/q087720_.html
    response_href: SSFKSJ_9.4.0/refadmin/q087730_.html
    request_parameters:
      - name: NamelistName
        pcf_type: MQCFST
        type_hint: str
      - name: CommandScope
        pcf_type: MQCFST
        type_hint: str
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
    response_parameters:
      - name: NamelistNames
        pcf_type: MQCFSL
        type_hint: list[str]
      - name: QSGDispositions
        pcf_type: MQCFIL
        type_hint: list[int]
        enum_values:
          - MQQSGD_COPY
          - MQQSGD_GROUP
          - MQQSGD_Q_MGR
    notes: []
  - name: MQCMD_INQUIRE_PROCESS
    request_href: SSFKSJ_9.4.0/refadmin/q087740_.html
    response_href: SSFKSJ_9.4.0/refadmin/q087750_.html
    request_parameters:
      - name: ProcessName
        pcf_type: MQCFST
        type_hint: str
      - name: CommandScope
        pcf_type: MQCFST
        type_hint: str
      - name: IntegerFilterCommand
        pcf_type: MQCFIF
        type_hint: null
      - name: ProcessAttrs
        pcf_type: MQCFIL
        type_hint: list[int]
        enum_values:
          - MQIACF_ALL
          - MQCA_ALTERATION_DATE
          - MQCA_ALTERATION_TIME
          - MQCA_APPL_ID
          - MQCA_ENV_DATA
          - MQCA_PROCESS_DESC
          - MQCA_PROCESS_NAME
          - MQCA_USER_DATA
          - MQIA_APPL_TYPE
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
      - name: ApplId
        pcf_type: MQCFST
        type_hint: str
      - name: ApplType
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQAT_AIX
          - MQAT_CICS
          - MQAT_DOS
          - MQAT_MVS
          - MQAT_OS400
          - MQAT_QMGR
          - MQAT_UNIX
          - MQAT_WINDOWS
          - MQAT_WINDOWS_NT
      - name: EnvData
        pcf_type: MQCFST
        type_hint: str
      - name: ProcessDesc
        pcf_type: MQCFST
        type_hint: str
      - name: ProcessName
        pcf_type: MQCFST
        type_hint: str
      - name: QSGDisposition
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQQSGD_COPY
          - MQQSGD_GROUP
          - MQQSGD_Q_MGR
      - name: UserData
        pcf_type: MQCFST
        type_hint: str
    notes: []
  - name: MQCMD_INQUIRE_PROCESS_NAMES
    request_href: SSFKSJ_9.4.0/refadmin/q087760_.html
    response_href: SSFKSJ_9.4.0/refadmin/q087770_.html
    request_parameters:
      - name: ProcessName
        pcf_type: MQCFST
        type_hint: str
      - name: CommandScope
        pcf_type: MQCFST
        type_hint: str
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
    response_parameters:
      - name: ProcessNames
        pcf_type: MQCFSL
        type_hint: list[str]
      - name: QSGDispositions
        pcf_type: MQCFIL
        type_hint: list[int]
        enum_values:
          - MQQSGD_COPY
          - MQQSGD_GROUP
          - MQQSGD_Q_MGR
    notes: []
  - name: MQCMD_INQUIRE_PROT_POLICY
    request_href: SSFKSJ_9.4.0/refadmin/q120840_.html
    response_href: SSFKSJ_9.4.0/refadmin/q120850_.html
    request_parameters:
      - name: PolicyAttrs
        pcf_type: MQCFIL
        type_hint: list[int]
        enum_values:
          - MQIACF_ALL
          - MQCA_POLICY_NAME
          - MQIA_SIGNATURE_ALGORITHM
          - MQIA_ENCRYPTION_ALGORITHM
          - MQCA_SIGNER_DN
          - MQCA_RECIPIENT_DN
          - MQIA_TOLERATE_UNPROTECTED
          - MQIA_KEY_REUSE_COUNT
          - MQIACF_ACTION
    response_parameters:
      - name: Action
        pcf_type: MQCFIL
        type_hint: list[int]
      - name: EncAlg
        pcf_type: MQCFIL
        type_hint: list[int]
      - name: KeyReuse
        pcf_type: MQCFIN
        type_hint: int
      - name: Recipient
        pcf_type: MQCFIL
        type_hint: list[int]
      - name: SignAlg
        pcf_type: MQCFIL
        type_hint: list[int]
      - name: Signer
        pcf_type: MQCFST
        type_hint: str
    notes: []
  - name: MQCMD_INQUIRE_PUBSUB_STATUS
    request_href: SSFKSJ_9.4.0/refadmin/q087780_.html
    response_href: SSFKSJ_9.4.0/refadmin/q087790_.html
    request_parameters:
      - name: CommandScope
        pcf_type: MQCFST
        type_hint: str
      - name: PubSubStatusAttrs
        pcf_type: MQCFIL
        type_hint: list[int]
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
    response_parameters:
      - name: QueueManagerName
        pcf_type: MQCFST
        type_hint: str
      - name: Type
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQPSST_CHILD
          - MQPSST_LOCAL
          - MQPSST_PARENT
      - name: Status
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQPS_STATUS_ACTIVE
          - MQPS_STATUS_COMPAT
          - MQPS_STATUS_ERROR
          - MQPS_STATUS_INACTIVE
          - MQPS_STATUS_STARTING
          - MQPS_STATUS_STOPPING
          - MQPS_STATUS_REFUSED
      - name: SubCount
        pcf_type: MQCFIN
        type_hint: int
      - name: TopicNodeCount
        pcf_type: MQCFIN
        type_hint: int
    notes: []
  - name: MQCMD_INQUIRE_Q
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
        type_hint: list[int]
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
        type_hint: list[str]
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
    notes: []
  - name: MQCMD_INQUIRE_QSG
    request_href: SSFKSJ_9.4.0/refadmin/q087660_.html
    response_href: SSFKSJ_9.4.0/refadmin/q087670_.html
    request_parameters:
      - name: ObsoleteDB2Msgs
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQOM_NO
          - MQOM_YES
    response_parameters:
      - name: CommandLevel
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQCMDL_LEVEL_800
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
      - name: DB2ConnectStatus
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQQSGS_ACTIVE
          - MQQSGS_INACTIVE
          - MQQSGS_FAILED
          - MQQSGS_PENDING
          - MQQSGS_UNKNOWN
      - name: DB2Name
        pcf_type: MQCFST
        type_hint: str
      - name: QMgrCPF
        pcf_type: MQCFST
        type_hint: str
      - name: QMgrName
        pcf_type: MQCFST
        type_hint: str
      - name: QmgrNumber
        pcf_type: MQCFIN
        type_hint: int
      - name: QMgrStatus
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQQSGS_ACTIVE
          - MQQSGS_INACTIVE
          - MQQSGS_FAILED
          - MQQSGS_CREATED
          - MQQSGS_UNKNOWN
      - name: QSGName
        pcf_type: MQCFST
        type_hint: str
      - name: CFMsgIdentifier
        pcf_type: MQCFBS
        type_hint: bytes
      - name: CommandInformation
        pcf_type: MQCFIN
        type_hint: int
    notes: []
  - name: MQCMD_INQUIRE_Q_MGR
    request_href: SSFKSJ_9.4.0/refadmin/q087820_.html
    response_href: SSFKSJ_9.4.0/refadmin/q087830_.html
    request_parameters:
      - name: CommandScope
        pcf_type: MQCFST
        type_hint: str
      - name: QMgrAttrs
        pcf_type: MQCFIL
        type_hint: list[int]
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
        type_hint: list[int]
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
        type_hint: list[int]
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
    notes: []
  - name: MQCMD_INQUIRE_Q_MGR_STATUS
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
        type_hint: list[int]
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
    notes: []
  - name: MQCMD_INQUIRE_Q_NAMES
    request_href: SSFKSJ_9.4.0/refadmin/q087860_.html
    response_href: SSFKSJ_9.4.0/refadmin/q087870_.html
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
          - MQQT_MODEL
    response_parameters:
      - name: QNames
        pcf_type: MQCFSL
        type_hint: list[str]
      - name: QSGDispositions
        pcf_type: MQCFIL
        type_hint: list[int]
        enum_values:
          - MQQSGD_COPY
          - MQQSGD_GROUP
          - MQQSGD_Q_MGR
          - MQQSGD_SHARED
      - name: QTypes
        pcf_type: MQCFIL
        type_hint: list[int]
        enum_values:
          - MQQT_ALIAS
          - MQQT_LOCAL
          - MQQT_REMOTE
          - MQQT_MODEL
    notes: []
  - name: MQCMD_INQUIRE_Q_STATUS
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
        type_hint: list[int]
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
        type_hint: list[int]
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
    notes: []
  - name: MQCMD_INQUIRE_SECURITY
    request_href: SSFKSJ_9.4.0/refadmin/q087900_.html
    response_href: SSFKSJ_9.4.0/refadmin/q087910_.html
    request_parameters:
      - name: CommandScope
        pcf_type: MQCFST
        type_hint: str
      - name: SecurityAttrs
        pcf_type: MQCFIL
        type_hint: list[int]
        enum_values:
          - MQIACF_ALL
          - MQIACF_SECURITY_SWITCH
          - MQIACF_SECURITY_TIMEOUT
          - MQIACF_SECURITY_INTERVAL
    response_parameters:
      - name: SecurityInterval
        pcf_type: MQCFIN
        type_hint: int
      - name: SecuritySwitch
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQSECSW_SUBSYSTEM
          - MQSECSW_Q_MGR
          - MQSECSW_QSG
          - MQSECSW_CONNECTION
          - MQSECSW_COMMAND
          - MQSECSW_CONTEXT
          - MQSECSW_ALTERNATE_USER
          - MQSECSW_PROCESS
          - MQSECSW_NAMELIST
          - MQSECSW_TOPIC
          - MQSECSW_Q
          - MQSECSW_COMMAND_RESOURCES
      - name: SecuritySwitchProfile
        pcf_type: MQCFST
        type_hint: str
      - name: SecuritySwitchSetting
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQSECSW_ON_FOUND
          - MQSECSW_OFF_FOUND
          - MQSECSW_ON_NOT_FOUND
          - MQSECSW_OFF_NOT_FOUND
          - MQSECSW_OFF_ERROR
          - MQSECSW_ON_OVERRIDDEN
      - name: SecurityTimeout
        pcf_type: MQCFIN
        type_hint: int
    notes: []
  - name: MQCMD_INQUIRE_SERVICE
    request_href: SSFKSJ_9.4.0/refadmin/q087920_.html
    response_href: SSFKSJ_9.4.0/refadmin/q087930_.html
    request_parameters:
      - name: ServiceName
        pcf_type: MQCFST
        type_hint: str
      - name: IntegerFilterCommand
        pcf_type: MQCFIF
        type_hint: null
      - name: ServiceAttrs
        pcf_type: MQCFIL
        type_hint: list[int]
        enum_values:
          - MQIACF_ALL
          - MQCA_ALTERATION_DATE
          - MQCA_ALTERATION_TIME
          - MQCA_SERVICE_DESC
          - MQCA_SERVICE_NAME
          - MQCA_SERVICE_START_ARGS
          - MQCA_SERVICE_START_COMMAND
          - MQCA_SERVICE_STOP_ARGS
          - MQCA_STDERR_DESTINATION
          - MQCA_STDOUT_DESTINATION
          - MQIA_SERVICE_CONTROL
          - MQIA_SERVICE_TYPE
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
      - name: ServiceDesc
        pcf_type: MQCFST
        type_hint: str
      - name: ServiceName
        pcf_type: MQCFST
        type_hint: str
      - name: ServiceType
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQSVC_TYPE_SERVER
          - MQSVC_TYPE_COMMAND
      - name: StartArguments
        pcf_type: MQCFST
        type_hint: str
      - name: StartCommand
        pcf_type: MQCFST
        type_hint: str
      - name: StartMode
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQSVC_CONTROL_MANUAL
          - MQSVC_CONTROL_Q_MGR
          - MQSVC_CONTROL_Q_MGR_START
      - name: StderrDestination
        pcf_type: MQCFST
        type_hint: str
      - name: StdoutDestination
        pcf_type: MQCFST
        type_hint: str
      - name: StopArguments
        pcf_type: MQCFST
        type_hint: str
      - name: StopCommand
        pcf_type: MQCFST
        type_hint: str
    notes: []
  - name: MQCMD_INQUIRE_SERVICE_STATUS
    request_href: SSFKSJ_9.4.0/refadmin/q087940_.html
    response_href: SSFKSJ_9.4.0/refadmin/q087950_.html
    request_parameters:
      - name: ServiceName
        pcf_type: MQCFST
        type_hint: str
      - name: IntegerFilterCommand
        pcf_type: MQCFIF
        type_hint: null
      - name: ServiceStatusAttrs
        pcf_type: MQCFIL
        type_hint: list[int]
        enum_values:
          - MQIACF_ALL
          - MQCA_SERVICE_DESC
          - MQCA_SERVICE_NAME
          - MQCA_SERVICE_START_ARGS
          - MQCA_SERVICE_START_COMMAND
          - MQCA_SERVICE_STOP_ARGS
          - MQCA_SERVICE_STOP_COMMAND
          - MQCA_STDERR_DESTINATION
          - MQCA_STDOUT_DESTINATION
          - MQCACF_SERVICE_START_DATE
          - MQCACF_SERVICE_START_TIME
          - MQIA_SERVICE_CONTROL
          - MQIA_SERVICE_TYPE
          - MQIACF_PROCESS_ID
          - MQIACF_SERVICE_STATUS
      - name: StringFilterCommand
        pcf_type: MQCFSF
        type_hint: null
        enum_values:
          - MQRCCF_SERV_STATUS_NOT_FOUND
    response_parameters:
      - name: ProcessId
        pcf_type: MQCFIN
        type_hint: int
      - name: ServiceDesc
        pcf_type: MQCFST
        type_hint: str
      - name: ServiceName
        pcf_type: MQCFST
        type_hint: str
      - name: StartArguments
        pcf_type: MQCFST
        type_hint: str
      - name: StartCommand
        pcf_type: MQCFST
        type_hint: str
      - name: StartDate
        pcf_type: MQCFST
        type_hint: str
      - name: StartMode
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQSVC_CONTROL_MANUAL
          - MQSVC_CONTROL_Q_MGR
          - MQSVC_CONTROL_Q_MGR_START
      - name: StartTime
        pcf_type: MQCFST
        type_hint: str
      - name: Status
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQSVC_STATUS_STARTING
          - MQSVC_STATUS_RUNNING
          - MQSVC_STATUS_STOPPING
      - name: StderrDestination
        pcf_type: MQCFST
        type_hint: str
      - name: StdoutDestination
        pcf_type: MQCFST
        type_hint: str
      - name: StopArguments
        pcf_type: MQCFST
        type_hint: str
      - name: StopCommand
        pcf_type: MQCFST
        type_hint: str
    notes: []
  - name: MQCMD_INQUIRE_SMDS
    request_href: SSFKSJ_9.4.0/refadmin/q087960_.html
    response_href: SSFKSJ_9.4.0/refadmin/q087970_.html
    request_parameters:
      - name: CFStrucName
        pcf_type: MQCFST
        type_hint: str
      - name: CFSMDSAttrs
        pcf_type: MQCFIL
        type_hint: list[int]
        enum_values:
          - MQIACF_ALL
          - MQIA_CF_SMDS_BUFFERS
          - MQIACF_CF_SMDS_EXPAND
    response_parameters:
      - name: SMDS
        pcf_type: MQCFST
        type_hint: str
      - name: CFStrucName
        pcf_type: MQCFST
        type_hint: str
      - name: DSBUFS
        pcf_type: MQCFIN
        type_hint: int
      - name: DSEXPAND
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQDSE_YES
          - MQDSE_NO
          - MQDSE_DEFAULT
    notes: []
  - name: MQCMD_INQUIRE_SMDSCONN
    request_href: SSFKSJ_9.4.0/refadmin/q087980_.html
    response_href: SSFKSJ_9.4.0/refadmin/q087990_.html
    request_parameters:
      - name: SMDSCONN
        pcf_type: MQCFST
        type_hint: str
      - name: CFStrucName
        pcf_type: MQCFST
        type_hint: str
      - name: CommandScope
        pcf_type: MQCFST
        type_hint: str
    response_parameters:
      - name: SMDSCONN
        pcf_type: MQCFST
        type_hint: str
      - name: CFStrucName
        pcf_type: MQCFST
        type_hint: str
      - name: Avail
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQS_AVAIL_NORMAL
          - MQS_AVAIL_ERROR
          - MQS_AVAIL_STOPPED
      - name: ExpandST
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQS_EXPANDST_NORMAL
          - MQS_EXPANDST_FAILED
          - MQS_EXPANDST_MAXIMUM
      - name: OpenMode
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQS_OPENMODE_NONE
          - MQS_OPENMODE_READONLY
          - MQS_OPENMODE_UPDATE
          - MQS_OPENMODE_RECOVERY
      - name: Status
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQS_STATUS_CLOSED
          - MQS_STATUS_CLOSING
          - MQS_STATUS_OPENING
          - MQS_STATUS_OPEN
          - MQS_STATUS_NOTENABLED
          - MQS_STATUS_ALLOCFAIL
          - MQS_STATUS_OPENFAIL
          - MQS_STATUS_STGFAIL
          - MQS_STATUS_DATAFAIL
    notes: []
  - name: MQCMD_INQUIRE_STG_CLASS
    request_href: SSFKSJ_9.4.0/refadmin/q088000_.html
    response_href: SSFKSJ_9.4.0/refadmin/q088010_.html
    request_parameters:
      - name: StorageClassName
        pcf_type: MQCFST
        type_hint: str
      - name: CommandScope
        pcf_type: MQCFST
        type_hint: str
      - name: IntegerFilterCommand
        pcf_type: MQCFIF
        type_hint: null
      - name: PageSetId
        pcf_type: MQCFIN
        type_hint: int
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
      - name: StgClassAttrs
        pcf_type: MQCFIL
        type_hint: list[int]
        enum_values:
          - MQIACF_ALL
          - MQCA_STORAGE_CLASS
          - MQCA_STORAGE_CLASS_DESC
          - MQIA_PAGESET_ID
          - MQCA_XCF_GROUP_NAME
          - MQIA_XCF_MEMBER_NAME
          - MQCA_ALTERATION_DATE
          - MQCA_ALTERATION_TIME
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
      - name: PageSetId
        pcf_type: MQCFIN
        type_hint: int
      - name: PassTicketApplication
        pcf_type: MQCFST
        type_hint: str
      - name: QSGDisposition
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQQSGD_COPY
          - MQQSGD_GROUP
          - MQQSGD_Q_MGR
      - name: StorageClassDesc
        pcf_type: MQCFST
        type_hint: str
      - name: StgClassName
        pcf_type: MQCFST
        type_hint: str
      - name: XCFGroupName
        pcf_type: MQCFST
        type_hint: str
      - name: XCFMemberName
        pcf_type: MQCFST
        type_hint: str
    notes: []
  - name: MQCMD_INQUIRE_STG_CLASS_NAMES
    request_href: SSFKSJ_9.4.0/refadmin/q088020_.html
    response_href: SSFKSJ_9.4.0/refadmin/q088030_.html
    request_parameters:
      - name: StorageClassName
        pcf_type: MQCFST
        type_hint: str
      - name: CommandScope
        pcf_type: MQCFST
        type_hint: str
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
    response_parameters:
      - name: StorageClassNames
        pcf_type: MQCFSL
        type_hint: list[str]
      - name: QSGDispositions
        pcf_type: MQCFIL
        type_hint: list[int]
        enum_values:
          - MQQSGD_COPY
          - MQQSGD_GROUP
          - MQQSGD_Q_MGR
    notes: []
  - name: MQCMD_INQUIRE_SUBSCRIPTION
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
    response_parameters:
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
      - name: SubID
        pcf_type: MQCFBS
        type_hint: bytes
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
    notes: []
  - name: MQCMD_INQUIRE_SUB_STATUS
    request_href: SSFKSJ_9.4.0/refadmin/q088060_.html
    response_href: SSFKSJ_9.4.0/refadmin/q088070_.html
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
      - name: SubscriptionType
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQSUBTYPE_ADMIN
          - MQSUBTYPE_ALL
          - MQSUBTYPE_API
          - MQSUBTYPE_PROXY
          - MQSUBTYPE_USER
      - name: StatusAttrs
        pcf_type: MQCFIL
        type_hint: list[int]
        enum_values:
          - MQIACF_ALL
          - MQBACF_CONNECTION_ID
          - MQIACF_DURABLE_SUBSCRIPTION
          - MQCACF_LAST_MSG_DATE
          - MQCACF_LAST_MSG_TIME
          - MQIACF_MESSAGE_COUNT
          - MQCA_RESUME_DATE
          - MQCA_RESUME_TIME
          - MQIACF_SUB_TYPE
          - MQCACF_SUB_USER_ID
          - MQCA_TOPIC_STRING
    response_parameters:
      - name: ActiveConnection
        pcf_type: MQCFBS
        type_hint: bytes
      - name: Durable
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQSUB_DURABLE_NO
          - MQSUB_DURABLE_YES
      - name: LastMessageDate
        pcf_type: MQCFST
        type_hint: str
      - name: LastMessageTime
        pcf_type: MQCFST
        type_hint: str
      - name: MCastRelIndicator
        pcf_type: MQCFIN
        type_hint: int
      - name: NumberMsgs
        pcf_type: MQCFIN
        type_hint: int
      - name: ResumeDate
        pcf_type: MQCFST
        type_hint: str
      - name: ResumeTime
        pcf_type: MQCFST
        type_hint: str
      - name: SubscriptionUser
        pcf_type: MQCFST
        type_hint: str
      - name: SubID
        pcf_type: MQCFBS
        type_hint: bytes
      - name: SubName
        pcf_type: MQCFST
        type_hint: str
      - name: SubType
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQSUBTYPE_PROXY
          - MQSUBTYPE_ADMIN
          - MQSUBTYPE_API
      - name: TopicString
        pcf_type: MQCFST
        type_hint: str
    notes: []
  - name: MQCMD_INQUIRE_SYSTEM
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
        type_hint: list[str]
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
        type_hint: list[int]
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
        type_hint: list[int]
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
    notes: []
  - name: MQCMD_INQUIRE_TOPIC
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
    notes: []
  - name: MQCMD_INQUIRE_TOPIC_NAMES
    request_href: SSFKSJ_9.4.0/refadmin/q088120_.html
    response_href: SSFKSJ_9.4.0/refadmin/q088130_.html
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
          - MQQSGD_LIVE
          - MQQSGD_ALL
          - MQQSGD_COPY
          - MQQSGD_GROUP
          - MQQSGD_Q_MGR
          - MQQSGD_PRIVATE
    response_parameters:
      - name: TopicNames
        pcf_type: MQCFSL
        type_hint: list[str]
      - name: QSGDispositions
        pcf_type: MQCFIL
        type_hint: list[int]
        enum_values:
          - MQQSGD_COPY
          - MQQSGD_GROUP
          - MQQSGD_Q_MGR
    notes: []
  - name: MQCMD_INQUIRE_TOPIC_STATUS
    request_href: SSFKSJ_9.4.0/refadmin/q088140_.html
    response_href: SSFKSJ_9.4.0/refadmin/q088150_.html
    request_parameters:
      - name: TopicString
        pcf_type: MQCFST
        type_hint: str
      - name: CommandScope
        pcf_type: MQCFST
        type_hint: str
      - name: IntegerFilterCommand
        pcf_type: MQCFIF
        type_hint: null
      - name: StatusType
        pcf_type: MQCFIN
        type_hint: int
      - name: StringFilterCommand
        pcf_type: MQCFSF
        type_hint: null
      - name: TopicStatusAttrs
        pcf_type: MQCFIL
        type_hint: list[int]
    response_parameters:
      - name: TopicString
        pcf_type: MQCFST
        type_hint: str
      - name: CapExpiry
        pcf_type: MQCFIN
        type_hint: int
      - name: ClusterName
        pcf_type: MQCFST
        type_hint: str
      - name: ClusterPubRoute
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQCLROUTE_DIRECT
          - MQCLROUTE_TOPIC_HOST
          - MQCLROUTE_NONE
      - name: CommInfo
        pcf_type: MQCFST
        type_hint: str
      - name: DefPersistence
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQPER_PERSISTENT
          - MQPER_NOT_PERSISTENT
      - name: DefaultPutResponse
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQPRT_SYNC_RESPONSE
          - MQPRT_ASYNC_RESPONSE
      - name: DefPriority
        pcf_type: MQCFIN
        type_hint: int
      - name: DurableSubscriptions
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQSUB_DURABLE_ALLOWED
          - MQSUB_DURABLE_INHIBITED
      - name: InhibitPublications
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQTA_PUB_INHIBITED
          - MQTA_PUB_ALLOWED
      - name: InhibitSubscriptions
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQTA_SUB_INHIBITED
          - MQTA_SUB_ALLOWED
      - name: AdminTopicName
        pcf_type: MQCFST
        type_hint: str
      - name: MCastRelIndicator
        pcf_type: MQCFIN
        type_hint: int
      - name: Multicast
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQMC_ENABLED
          - MQMC_DISABLED
          - MQMC_ONLY
      - name: DurableModelQName
        pcf_type: MQCFST
        type_hint: str
      - name: NonDurableModelQName
        pcf_type: MQCFST
        type_hint: str
      - name: PersistentMessageDelivery
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQDLV_ALL
          - MQDLV_ALL_DUR
          - MQDLV_ALL_AVAIL
      - name: NonPersistentMessageDelivery
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQDLV_ALL
          - MQDLV_ALL_DUR
          - MQDLV_ALL_AVAIL
      - name: RetainedPublication
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQQSO_YES
          - MQQSO_NO
      - name: PublishCount
        pcf_type: MQCFIN
        type_hint: int
      - name: SubscriptionCount
        pcf_type: MQCFIN
        type_hint: int
      - name: SubscriptionScope
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQSCOPE_QMGR
          - MQSCOPE_ALL
      - name: PublicationScope
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQSCOPE_QMGR
          - MQSCOPE_ALL
      - name: UseDLQ
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQUSEDLQ_NO
          - MQUSEDLQ_YES
      - name: SubscriptionId
        pcf_type: MQCFBS
        type_hint: bytes
      - name: SubscriptionUserId
        pcf_type: MQCFST
        type_hint: str
      - name: Durable
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQSUB_DURABLE_YES
          - MQSUB_DURABLE_NO
      - name: SubscriptionType
        pcf_type: MQCFIN
        type_hint: int
      - name: MCastRelIndicator
        pcf_type: MQCFIN
        type_hint: int
      - name: ResumeDate
        pcf_type: MQCFST
        type_hint: str
      - name: ResumeTime
        pcf_type: MQCFST
        type_hint: str
      - name: LastMessageDate
        pcf_type: MQCFST
        type_hint: str
      - name: LastMessageTime
        pcf_type: MQCFST
        type_hint: str
      - name: NumberOfMessages
        pcf_type: MQCFIN
        type_hint: int
      - name: ActiveConnection
        pcf_type: MQCFBS
        type_hint: bytes
      - name: LastPublicationDate
        pcf_type: MQCFST
        type_hint: str
      - name: LastPublicationTime
        pcf_type: MQCFST
        type_hint: str
      - name: MCastRelIndicator
        pcf_type: MQCFIN
        type_hint: int
      - name: NumberOfPublishes
        pcf_type: MQCFIN
        type_hint: int
      - name: ActiveConnection
        pcf_type: MQCFBS
        type_hint: bytes
    notes: []
  - name: MQCMD_INQUIRE_USAGE
    request_href: SSFKSJ_9.4.0/refadmin/q088160_.html
    response_href: SSFKSJ_9.4.0/refadmin/q088170_.html
    request_parameters:
      - name: CommandScope
        pcf_type: MQCFST
        type_hint: str
      - name: PageSetId
        pcf_type: MQCFIN
        type_hint: int
      - name: UsageType
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQIACF_USAGE_PAGESET
          - MQIACF_USAGE_DATA_SET
          - MQIACF_ALL
          - MQIACF_USAGE_SMDS
    response_parameters:
      - name: BufferPoolId
        pcf_type: MQCFIN
        type_hint: int
      - name: Encrypted
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQSYSP_YES
          - MQSYSP_NO
      - name: ExpandCount
        pcf_type: MQCFIN
        type_hint: int
      - name: ExpandType
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQUSAGE_EXPAND_NONE
          - MQUSAGE_EXPAND_USER
          - MQUSAGE_EXPAND_SYSTEM
      - name: NonPersistentDataPages
        pcf_type: MQCFIN
        type_hint: int
      - name: PageSetId
        pcf_type: MQCFIN
        type_hint: int
      - name: PageSetStatus
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQUSAGE_PS_AVAILABLE
          - MQUSAGE_PS_DEFINED
          - MQUSAGE_PS_OFFLINE
          - MQUSAGE_PS_NOT_DEFINED
          - MQUSAGE_PS_SUSPENDED
      - name: PersistentDataPages
        pcf_type: MQCFIN
        type_hint: int
      - name: TotalPages
        pcf_type: MQCFIN
        type_hint: int
      - name: UnusedPages
        pcf_type: MQCFIN
        type_hint: int
      - name: LogRBA
        pcf_type: MQCFST
        type_hint: str
      - name: BufferPoolId
        pcf_type: MQCFIN
        type_hint: int
      - name: FreeBuffers
        pcf_type: MQCFIN
        type_hint: int
      - name: FreeBuffersPercentage
        pcf_type: MQCFIN
        type_hint: int
      - name: TotalBuffers
        pcf_type: MQCFIN
        type_hint: int
      - name: BufferPoolLocation
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQBPLOCATION_ABOVE
          - MQBPLOCATION_BELOW
          - MQBPLOCATION_SWITCHING_ABOVE
          - MQBPLOCATION_SWITCHING_BELOW
      - name: PageClass
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQPAGECLAS_4KB
          - MQPAGECLAS_FIXED4KB
      - name: DataSetName
        pcf_type: MQCFST
        type_hint: str
      - name: DataSetType
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQUSAGE_DS_OLDEST_ACTIVE_UOW
          - MQUSAGE_DS_OLDEST_PS_RECOVERY
          - MQUSAGE__DS_OLDEST_CF_RECOVERY
      - name: LogRBA
        pcf_type: MQCFST
        type_hint: str
      - name: LogLRSN
        pcf_type: MQCFST
        type_hint: str
      - name: Encrypted
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQSYSP_YES
          - MQSYSP_NO
      - name: SMDSStatus
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQUSAGE_SMDS_NO_DATA
          - MQUSAGE_SMDS_AVAILABLE
          - A
      - name: CFStrucNames
        pcf_type: MQCFSL
        type_hint: list[str]
      - name: MQIACF_USAGE_OFFLOAD_MSGS
        pcf_type: MQCFIN
        type_hint: int
      - name: MQIACF_USAGE_TOTAL_BLOCKS
        pcf_type: MQCFIN
        type_hint: int
      - name: MQIACF_USAGE_DATA_BLOCKS
        pcf_type: MQCFIN
        type_hint: int
      - name: MQIACF_USAGE_USED_BLOCKS
        pcf_type: MQCFIN
        type_hint: int
      - name: MQIACF_USAGE_USED_RATE
        pcf_type: MQCFIN
        type_hint: int
      - name: MQIACF_SMDS_STATUS
        pcf_type: MQCFIN
        type_hint: int
      - name: MQIACF_USAGE_TYPE
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - B
      - name: CFStrucNames
        pcf_type: MQCFSL
        type_hint: list[str]
      - name: MQIACF_USAGE_BLOCK_SIZE
        pcf_type: MQCFIN
        type_hint: int
      - name: MQIACF_USAGE_TOTAL_BUFFERS
        pcf_type: MQCFIN
        type_hint: int
      - name: MQIACF_USAGE_INUSE_BUFFERS
        pcf_type: MQCFIN
        type_hint: int
      - name: MQIACF_USAGE_SAVED_BUFFERS
        pcf_type: MQCFIN
        type_hint: int
      - name: MQIACF_USAGE_EMPTY_BUFFERS
        pcf_type: MQCFIN
        type_hint: int
      - name: MQIACF_USAGE_READS_SAVED
        pcf_type: MQCFIN
        type_hint: int
      - name: MQIACF_USAGE_LOWEST_FREE
        pcf_type: MQCFIN
        type_hint: int
      - name: MQIACF_USAGE_WAIT_RATE
        pcf_type: MQCFIN
        type_hint: int
      - name: MQIACF_SMDS_STATUS
        pcf_type: MQCFIN
        type_hint: int
      - name: MQIACF_USAGE_TYPE
        pcf_type: MQCFIN
        type_hint: int
    notes: []
  - name: MQCMD_MOVE_Q
    request_href: SSFKSJ_9.4.0/refadmin/q088180_.html
    response_href: SSFKSJ_9.4.0/refadmin/q088180_.html
    request_parameters:
      - name: FromQName
        pcf_type: MQCFST
        type_hint: str
      - name: CommandScope
        pcf_type: MQCFST
        type_hint: str
      - name: MoveType
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQIACF_MOVE_TYPE_MOVE
          - MQIACF_MOVE_TYPE_ADD
      - name: QSGDisposition
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQQSGD_PRIVATE
          - MQQSGD_SHARED
      - name: ToQName
        pcf_type: MQCFST
        type_hint: str
    response_parameters:
      - name: FromQName
        pcf_type: MQCFST
        type_hint: str
      - name: CommandScope
        pcf_type: MQCFST
        type_hint: str
      - name: MoveType
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQIACF_MOVE_TYPE_MOVE
          - MQIACF_MOVE_TYPE_ADD
      - name: QSGDisposition
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQQSGD_PRIVATE
          - MQQSGD_SHARED
      - name: ToQName
        pcf_type: MQCFST
        type_hint: str
    notes: []
  - name: MQCMD_PING_CHANNEL
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
    notes: []
  - name: MQCMD_PING_Q_MGR
    request_href: SSFKSJ_9.4.0/refadmin/q088200_.html
    response_href: SSFKSJ_9.4.0/refadmin/q088200_.html
    request_parameters: []
    response_parameters: []
    notes: []
  - name: MQCMD_PURGE_CHANNEL
    request_href: SSFKSJ_9.4.0/refadmin/q088210_.html
    response_href: SSFKSJ_9.4.0/refadmin/q088210_.html
    request_parameters:
      - name: ChannelName
        pcf_type: MQCFST
        type_hint: str
      - name: ChannelType
        pcf_type: MQCFIN
        type_hint: int
      - name: ClientIdentifier
        pcf_type: MQCFST
        type_hint: str
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
    notes: []
  - name: MQCMD_RECOVER_CF_STRUC
    request_href: SSFKSJ_9.4.0/refadmin/q088220_.html
    response_href: SSFKSJ_9.4.0/refadmin/q088220_.html
    request_parameters:
      - name: CFStrucName
        pcf_type: MQCFST
        type_hint: str
      - name: CommandScope
        pcf_type: MQCFST
        type_hint: str
      - name: Purge
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQPO_YES
          - MQPO_NO
    response_parameters:
      - name: CFStrucName
        pcf_type: MQCFST
        type_hint: str
      - name: CommandScope
        pcf_type: MQCFST
        type_hint: str
      - name: Purge
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQPO_YES
          - MQPO_NO
    notes: []
  - name: MQCMD_REFRESH_CLUSTER
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
    notes: []
  - name: MQCMD_REFRESH_Q_MGR
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
    notes: []
  - name: MQCMD_REFRESH_SECURITY
    request_href: SSFKSJ_9.4.0/refadmin/q088250_.html
    response_href: SSFKSJ_9.4.0/refadmin/q088250_.html
    request_parameters:
      - name: CommandScope
        pcf_type: MQCFST
        type_hint: str
      - name: SecurityItem
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQSECITEM_ALL
          - MQSECITEM_MQADMIN
          - MQSECITEM_MQNLIST
          - MQSECITEM_MQPROC
          - MQSECITEM_MQQUEUE
          - MQSECITEM_MXADMIN
          - MQSECITEM_MXNLIST
          - MQSECITEM_MXPROC
          - MQSECITEM_MXQUEUE
          - MQSECITEM_MXTOPIC
      - name: SecurityType
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQSECTYPE_AUTHSERV
          - MQSECTYPE_CLASSES
          - MQSECTYPE_CONNAUTH
          - MQSECTYPE_SSL
    response_parameters:
      - name: CommandScope
        pcf_type: MQCFST
        type_hint: str
      - name: SecurityItem
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQSECITEM_ALL
          - MQSECITEM_MQADMIN
          - MQSECITEM_MQNLIST
          - MQSECITEM_MQPROC
          - MQSECITEM_MQQUEUE
          - MQSECITEM_MXADMIN
          - MQSECITEM_MXNLIST
          - MQSECITEM_MXPROC
          - MQSECITEM_MXQUEUE
          - MQSECITEM_MXTOPIC
      - name: SecurityType
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQSECTYPE_AUTHSERV
          - MQSECTYPE_CLASSES
          - MQSECTYPE_CONNAUTH
          - MQSECTYPE_SSL
    notes: []
  - name: MQCMD_RESET_CF_STRUC
    request_href: SSFKSJ_9.4.0/refadmin/q088260_.html
    response_href: SSFKSJ_9.4.0/refadmin/q088260_.html
    request_parameters:
      - name: CFStructName
        pcf_type: MQCFST
        type_hint: str
      - name: Action
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQACT_FAIL
    response_parameters:
      - name: CFStructName
        pcf_type: MQCFST
        type_hint: str
      - name: Action
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQACT_FAIL
    notes: []
  - name: MQCMD_RESET_CHANNEL
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
    notes: []
  - name: MQCMD_RESET_CLUSTER
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
    notes: []
  - name: MQCMD_RESET_Q_MGR
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
    notes: []
  - name: MQCMD_RESET_Q_STATS
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
    notes: []
  - name: MQCMD_RESET_SMDS
    request_href: SSFKSJ_9.4.0/refadmin/q088320_.html
    response_href: SSFKSJ_9.4.0/refadmin/q088320_.html
    request_parameters:
      - name: SMDS
        pcf_type: MQCFST
        type_hint: str
      - name: CFStrucName
        pcf_type: MQCFST
        type_hint: str
      - name: Access
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQCFACCESS_ENABLED
          - MQCFACCESS_DISABLED
      - name: Status
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQCFSTATUS_FAILED
          - MQCFSTATUS_RECOVERED
    response_parameters:
      - name: SMDS
        pcf_type: MQCFST
        type_hint: str
      - name: CFStrucName
        pcf_type: MQCFST
        type_hint: str
      - name: Access
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQCFACCESS_ENABLED
          - MQCFACCESS_DISABLED
      - name: Status
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQCFSTATUS_FAILED
          - MQCFSTATUS_RECOVERED
    notes: []
  - name: MQCMD_RESOLVE_CHANNEL
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
    notes: []
  - name: MQCMD_RESUME_Q_MGR
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
    notes: []
  - name: MQCMD_RESUME_Q_MGR_CLUSTER
    request_href: SSFKSJ_9.4.0/refadmin/q088350_.html
    response_href: SSFKSJ_9.4.0/refadmin/q088350_.html
    request_parameters:
      - name: ClusterName
        pcf_type: MQCFST
        type_hint: str
      - name: ClusterNamelist
        pcf_type: MQCFST
        type_hint: str
      - name: CommandScope
        pcf_type: MQCFST
        type_hint: str
        enum_values:
          - MQRCCF_CLUSTER_NAME_CONFLICT
    response_parameters:
      - name: ClusterName
        pcf_type: MQCFST
        type_hint: str
      - name: ClusterNamelist
        pcf_type: MQCFST
        type_hint: str
      - name: CommandScope
        pcf_type: MQCFST
        type_hint: str
        enum_values:
          - MQRCCF_CLUSTER_NAME_CONFLICT
    notes: []
  - name: MQCMD_REVERIFY_SECURITY
    request_href: SSFKSJ_9.4.0/refadmin/q088360_.html
    response_href: SSFKSJ_9.4.0/refadmin/q088360_.html
    request_parameters:
      - name: UserId
        pcf_type: MQCFST
        type_hint: str
      - name: CommandScope
        pcf_type: MQCFST
        type_hint: str
    response_parameters:
      - name: UserId
        pcf_type: MQCFST
        type_hint: str
      - name: CommandScope
        pcf_type: MQCFST
        type_hint: str
    notes: []
  - name: MQCMD_SET_ARCHIVE
    request_href: SSFKSJ_9.4.0/refadmin/q088370_.html
    response_href: SSFKSJ_9.4.0/refadmin/q086890_.html
    request_parameters:
      - name: ParameterType
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQSYSP_TYPE_INITIAL
          - MQSYSP_TYPE_SET
      - name: AllocPrimary
        pcf_type: MQCFIN
        type_hint: int
      - name: AllocSecondary
        pcf_type: MQCFIN
        type_hint: int
      - name: AllocUnits
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQSYSP_ALLOC_BLK
          - MQSYSP_ALLOC_TRK
          - MQSYSP_ALLOC_CYL
      - name: ArchivePrefix1
        pcf_type: MQCFST
        type_hint: str
      - name: ArchivePrefix2
        pcf_type: MQCFST
        type_hint: str
      - name: ArchiveRetention
        pcf_type: MQCFIN
        type_hint: int
      - name: ArchiveUnit1
        pcf_type: MQCFST
        type_hint: str
      - name: ArchiveUnit2
        pcf_type: MQCFST
        type_hint: str
      - name: ArchiveWTOR
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQSYSP_YES
          - MQSYSP_NO
      - name: BlockSize
        pcf_type: MQCFIN
        type_hint: int
      - name: Catalog
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQSYSP_YES
          - MQSYSP_NO
      - name: CommandScope
        pcf_type: MQCFST
        type_hint: str
      - name: Compact
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQSYSP_YES
          - MQSYSP_NO
      - name: Protect
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQSYSP_YES
          - MQSYSP_NO
      - name: QuiesceInterval
        pcf_type: MQCFIN
        type_hint: int
      - name: RoutingCode
        pcf_type: MQCFIL
        type_hint: list[int]
      - name: TimeStampFormat
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQSYSP_YES
          - MQSYSP_NO
          - MQSYSP_EXTENDED
    response_parameters: []
    notes: []
  - name: MQCMD_SET_AUTH_REC
    request_href: SSFKSJ_9.4.0/refadmin/q088380_.html
    response_href: SSFKSJ_9.4.0/refadmin/q088380_.html
    request_parameters:
      - name: ProfileName
        pcf_type: MQCFST
        type_hint: str
      - name: ObjectType
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQOT_AUTH_INFO
          - MQOT_CHANNEL
          - MQOT_CLNTCONN_CHANNEL
          - MQOT_COMM_INFO
          - MQOT_LISTENER
          - MQOT_NAMELIST
          - MQOT_PROCESS
          - MQOT_Q
          - MQOT_Q_MGR
          - MQOT_REMOTE_Q_MGR_NAME
          - MQOT_SERVICE
          - MQOT_TOPIC
      - name: AuthorityAdd
        pcf_type: MQCFIL
        type_hint: list[int]
        enum_values:
          - MQAUTH_NONE
          - MQAUTH_ALT_USER_AUTHORITY
          - MQAUTH_BROWSE
          - MQAUTH_CHANGE
          - MQAUTH_CLEAR
          - MQAUTH_CONNECT
          - MQAUTH_CREATE
          - MQAUTH_DELETE
          - MQAUTH_DISPLAY
          - MQAUTH_INPUT
          - MQAUTH_INQUIRE
          - MQAUTH_OUTPUT
          - MQAUTH_PASS_ALL_CONTEXT
          - MQAUTH_PASS_IDENTITY_CONTEXT
          - MQAUTH_SET
          - MQAUTH_SET_ALL_CONTEXT
          - MQAUTH_SET_IDENTITY_CONTEXT
          - MQAUTH_CONTROL
          - MQAUTH_CONTROL_EXTENDED
          - MQAUTH_PUBLISH
          - MQAUTH_SUBSCRIBE
          - MQAUTH_RESUME
          - MQAUTH_SYSTEM
          - MQAUTH_ALL
          - MQAUTH_ALL_ADMIN
          - MQAUTH_ALL_MQI
      - name: AuthorityRemove
        pcf_type: MQCFIL
        type_hint: list[int]
        enum_values:
          - MQAUTH_NONE
          - MQAUTH_ALT_USER_AUTHORITY
          - MQAUTH_BROWSE
          - MQAUTH_CHANGE
          - MQAUTH_CLEAR
          - MQAUTH_CONNECT
          - MQAUTH_CREATE
          - MQAUTH_DELETE
          - MQAUTH_DISPLAY
          - MQAUTH_INPUT
          - MQAUTH_INQUIRE
          - MQAUTH_OUTPUT
          - MQAUTH_PASS_ALL_CONTEXT
          - MQAUTH_PASS_IDENTITY_CONTEXT
          - MQAUTH_SET
          - MQAUTH_SET_ALL_CONTEXT
          - MQAUTH_SET_IDENTITY_CONTEXT
          - MQAUTH_CONTROL
          - MQAUTH_CONTROL_EXTENDED
          - MQAUTH_PUBLISH
          - MQAUTH_SUBSCRIBE
          - MQAUTH_RESUME
          - MQAUTH_SYSTEM
          - MQAUTH_ALL
          - MQAUTH_ALL_ADMIN
          - MQAUTH_ALL_MQI
      - name: GroupNames
        pcf_type: MQCFSL
        type_hint: list[str]
      - name: PrincipalNames
        pcf_type: MQCFSL
        type_hint: list[str]
      - name: ServiceComponent
        pcf_type: MQCFST
        type_hint: str
        enum_values:
          - MQRC_UNKNOWN_ENTITY
          - MQRCCF_AUTH_VALUE_ERROR
          - MQRCCF_AUTH_VALUE_MISSING
          - MQRCCF_ENTITY_NAME_MISSING
          - MQRCCF_OBJECT_TYPE_MISSING
          - MQRCCF_PROFILE_NAME_ERROR
    response_parameters:
      - name: ProfileName
        pcf_type: MQCFST
        type_hint: str
      - name: ObjectType
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQOT_AUTH_INFO
          - MQOT_CHANNEL
          - MQOT_CLNTCONN_CHANNEL
          - MQOT_COMM_INFO
          - MQOT_LISTENER
          - MQOT_NAMELIST
          - MQOT_PROCESS
          - MQOT_Q
          - MQOT_Q_MGR
          - MQOT_REMOTE_Q_MGR_NAME
          - MQOT_SERVICE
          - MQOT_TOPIC
      - name: AuthorityAdd
        pcf_type: MQCFIL
        type_hint: list[int]
        enum_values:
          - MQAUTH_NONE
          - MQAUTH_ALT_USER_AUTHORITY
          - MQAUTH_BROWSE
          - MQAUTH_CHANGE
          - MQAUTH_CLEAR
          - MQAUTH_CONNECT
          - MQAUTH_CREATE
          - MQAUTH_DELETE
          - MQAUTH_DISPLAY
          - MQAUTH_INPUT
          - MQAUTH_INQUIRE
          - MQAUTH_OUTPUT
          - MQAUTH_PASS_ALL_CONTEXT
          - MQAUTH_PASS_IDENTITY_CONTEXT
          - MQAUTH_SET
          - MQAUTH_SET_ALL_CONTEXT
          - MQAUTH_SET_IDENTITY_CONTEXT
          - MQAUTH_CONTROL
          - MQAUTH_CONTROL_EXTENDED
          - MQAUTH_PUBLISH
          - MQAUTH_SUBSCRIBE
          - MQAUTH_RESUME
          - MQAUTH_SYSTEM
          - MQAUTH_ALL
          - MQAUTH_ALL_ADMIN
          - MQAUTH_ALL_MQI
      - name: AuthorityRemove
        pcf_type: MQCFIL
        type_hint: list[int]
        enum_values:
          - MQAUTH_NONE
          - MQAUTH_ALT_USER_AUTHORITY
          - MQAUTH_BROWSE
          - MQAUTH_CHANGE
          - MQAUTH_CLEAR
          - MQAUTH_CONNECT
          - MQAUTH_CREATE
          - MQAUTH_DELETE
          - MQAUTH_DISPLAY
          - MQAUTH_INPUT
          - MQAUTH_INQUIRE
          - MQAUTH_OUTPUT
          - MQAUTH_PASS_ALL_CONTEXT
          - MQAUTH_PASS_IDENTITY_CONTEXT
          - MQAUTH_SET
          - MQAUTH_SET_ALL_CONTEXT
          - MQAUTH_SET_IDENTITY_CONTEXT
          - MQAUTH_CONTROL
          - MQAUTH_CONTROL_EXTENDED
          - MQAUTH_PUBLISH
          - MQAUTH_SUBSCRIBE
          - MQAUTH_RESUME
          - MQAUTH_SYSTEM
          - MQAUTH_ALL
          - MQAUTH_ALL_ADMIN
          - MQAUTH_ALL_MQI
      - name: GroupNames
        pcf_type: MQCFSL
        type_hint: list[str]
      - name: PrincipalNames
        pcf_type: MQCFSL
        type_hint: list[str]
      - name: ServiceComponent
        pcf_type: MQCFST
        type_hint: str
        enum_values:
          - MQRC_UNKNOWN_ENTITY
          - MQRCCF_AUTH_VALUE_ERROR
          - MQRCCF_AUTH_VALUE_MISSING
          - MQRCCF_ENTITY_NAME_MISSING
          - MQRCCF_OBJECT_TYPE_MISSING
          - MQRCCF_PROFILE_NAME_ERROR
    notes: []
  - name: MQCMD_SET_CHLAUTH_REC
    request_href: SSFKSJ_9.4.0/refadmin/q088390_.html
    response_href: SSFKSJ_9.4.0/refadmin/q088390_.html
    request_parameters:
      - name: ProfileName
        pcf_type: MQCFST
        type_hint: str
      - name: Type
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQCAUT_BLOCKUSER
          - MQCAUT_BLOCKADDR
          - MQCAUT_SSLPEERMAP
          - MQCAUT_ADDRESSMAP
          - MQCAUT_USERMAP
          - MQCAUT_QMGRMAP
      - name: Action
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQACT_ADD
          - MQACT_REPLACE
          - MQACT_REMOVE
          - MQACT_REMOVEALL
      - name: Address
        pcf_type: MQCFST
        type_hint: str
      - name: AddrList
        pcf_type: MQCFSL
        type_hint: list[str]
      - name: CheckClient
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQCHK_REQUIRED_ADMIN
          - MQCHK_REQUIRED
          - MQCHK_AS_Q_MGR
      - name: ClntUser
        pcf_type: MQCFST
        type_hint: str
      - name: CommandScope
        pcf_type: MQCFST
        type_hint: str
      - name: Custom
        pcf_type: MQCFST
        type_hint: str
      - name: Description
        pcf_type: MQCFST
        type_hint: str
      - name: MCAUser
        pcf_type: MQCFST
        type_hint: str
      - name: QMName
        pcf_type: MQCFST
        type_hint: str
      - name: SSLCertIssuer
        pcf_type: MQCFST
        type_hint: str
      - name: SSLPeer
        pcf_type: MQCFST
        type_hint: str
      - name: UserList
        pcf_type: MQCFSL
        type_hint: list[str]
      - name: UserSrc
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQUSRC_MAP
          - MQUSRC_NOACCESS
          - MQUSRC_CHANNEL
      - name: Warn
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQWARN_NO
          - MQWARN_YES
          - MQRCCF_CHLAUTH_TYPE_ERROR
          - MQRCCF_CHLAUTH_ACTION_ERROR
          - MQRCCF_CHLAUTH_USERSRC_ERROR
          - MQRCCF_WRONG_CHLAUTH_TYPE
          - MQRCCF_CHLAUTH_ALREADY_EXISTS
    response_parameters:
      - name: ProfileName
        pcf_type: MQCFST
        type_hint: str
      - name: Type
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQCAUT_BLOCKUSER
          - MQCAUT_BLOCKADDR
          - MQCAUT_SSLPEERMAP
          - MQCAUT_ADDRESSMAP
          - MQCAUT_USERMAP
          - MQCAUT_QMGRMAP
      - name: Action
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQACT_ADD
          - MQACT_REPLACE
          - MQACT_REMOVE
          - MQACT_REMOVEALL
      - name: Address
        pcf_type: MQCFST
        type_hint: str
      - name: AddrList
        pcf_type: MQCFSL
        type_hint: list[str]
      - name: CheckClient
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQCHK_REQUIRED_ADMIN
          - MQCHK_REQUIRED
          - MQCHK_AS_Q_MGR
      - name: ClntUser
        pcf_type: MQCFST
        type_hint: str
      - name: CommandScope
        pcf_type: MQCFST
        type_hint: str
      - name: Custom
        pcf_type: MQCFST
        type_hint: str
      - name: Description
        pcf_type: MQCFST
        type_hint: str
      - name: MCAUser
        pcf_type: MQCFST
        type_hint: str
      - name: QMName
        pcf_type: MQCFST
        type_hint: str
      - name: SSLCertIssuer
        pcf_type: MQCFST
        type_hint: str
      - name: SSLPeer
        pcf_type: MQCFST
        type_hint: str
      - name: UserList
        pcf_type: MQCFSL
        type_hint: list[str]
      - name: UserSrc
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQUSRC_MAP
          - MQUSRC_NOACCESS
          - MQUSRC_CHANNEL
      - name: Warn
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQWARN_NO
          - MQWARN_YES
          - MQRCCF_CHLAUTH_TYPE_ERROR
          - MQRCCF_CHLAUTH_ACTION_ERROR
          - MQRCCF_CHLAUTH_USERSRC_ERROR
          - MQRCCF_WRONG_CHLAUTH_TYPE
          - MQRCCF_CHLAUTH_ALREADY_EXISTS
    notes: []
  - name: MQCMD_SET_LOG
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
    notes: []
  - name: MQCMD_SET_SYSTEM
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
        type_hint: list[str]
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
        type_hint: list[str]
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
    notes: []
  - name: MQCMD_START_CHANNEL
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
    notes: []
  - name: MQCMD_START_CHANNEL_INIT
    request_href: SSFKSJ_9.4.0/refadmin/q088440_.html
    response_href: SSFKSJ_9.4.0/refadmin/q088440_.html
    request_parameters:
      - name: InitiationQName
        pcf_type: MQCFST
        type_hint: str
      - name: CommandScope
        pcf_type: MQCFST
        type_hint: str
      - name: EnvironmentInfo
        pcf_type: MQCFST
        type_hint: str
        enum_values:
          - MQRCCF_MQCONN_FAILED
          - MQRCCF_MQGET_FAILED
          - MQRCCF_MQOPEN_FAILED
    response_parameters:
      - name: InitiationQName
        pcf_type: MQCFST
        type_hint: str
      - name: CommandScope
        pcf_type: MQCFST
        type_hint: str
      - name: EnvironmentInfo
        pcf_type: MQCFST
        type_hint: str
        enum_values:
          - MQRCCF_MQCONN_FAILED
          - MQRCCF_MQGET_FAILED
          - MQRCCF_MQOPEN_FAILED
    notes: []
  - name: MQCMD_START_CHANNEL_LISTENER
    request_href: SSFKSJ_9.4.0/refadmin/q088450_.html
    response_href: SSFKSJ_9.4.0/refadmin/q088450_.html
    request_parameters:
      - name: CommandScope
        pcf_type: MQCFST
        type_hint: str
      - name: InboundDisposition
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQINBD_Q_MGR
          - MQINBD_GROUP
      - name: IPAddress
        pcf_type: MQCFST
        type_hint: str
      - name: ListenerName
        pcf_type: MQCFST
        type_hint: str
      - name: LUName
        pcf_type: MQCFST
        type_hint: str
      - name: Port
        pcf_type: MQCFIN
        type_hint: int
      - name: TransportType
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQXPT_LU62
          - MQXPT_TCP
          - MQXPT_NETBIOS
          - MQXPT_SPX
          - MQIACF_IGNORE_STATE
          - MQIS_NO
          - MQIS_YES
          - MQRCCF_COMMS_LIBRARY_ERROR
          - MQRCCF_LISTENER_NOT_STARTED
          - MQRCCF_LISTENER_RUNNING
          - MQRCCF_NETBIOS_NAME_ERROR
    response_parameters:
      - name: CommandScope
        pcf_type: MQCFST
        type_hint: str
      - name: InboundDisposition
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQINBD_Q_MGR
          - MQINBD_GROUP
      - name: IPAddress
        pcf_type: MQCFST
        type_hint: str
      - name: ListenerName
        pcf_type: MQCFST
        type_hint: str
      - name: LUName
        pcf_type: MQCFST
        type_hint: str
      - name: Port
        pcf_type: MQCFIN
        type_hint: int
      - name: TransportType
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQXPT_LU62
          - MQXPT_TCP
          - MQXPT_NETBIOS
          - MQXPT_SPX
          - MQIACF_IGNORE_STATE
          - MQIS_NO
          - MQIS_YES
          - MQRCCF_COMMS_LIBRARY_ERROR
          - MQRCCF_LISTENER_NOT_STARTED
          - MQRCCF_LISTENER_RUNNING
          - MQRCCF_NETBIOS_NAME_ERROR
    notes: []
  - name: MQCMD_START_SERVICE
    request_href: SSFKSJ_9.4.0/refadmin/q088460_.html
    response_href: SSFKSJ_9.4.0/refadmin/q088460_.html
    request_parameters:
      - name: ServiceName
        pcf_type: MQCFST
        type_hint: str
        enum_values:
          - MQIACF_IGNORE_STATE
          - MQIS_NO
          - MQIS_YES
          - MQRCCF_NO_START_CMD
          - MQRCCF_SERVICE_RUNNING
    response_parameters:
      - name: ServiceName
        pcf_type: MQCFST
        type_hint: str
        enum_values:
          - MQIACF_IGNORE_STATE
          - MQIS_NO
          - MQIS_YES
          - MQRCCF_NO_START_CMD
          - MQRCCF_SERVICE_RUNNING
    notes: []
  - name: MQCMD_START_SMDSCONN
    request_href: SSFKSJ_9.4.0/refadmin/q088470_.html
    response_href: SSFKSJ_9.4.0/refadmin/q088470_.html
    request_parameters:
      - name: SMDSConn
        pcf_type: MQCFST
        type_hint: str
      - name: CFStrucName
        pcf_type: MQCFST
        type_hint: str
      - name: CommandScope
        pcf_type: MQCFST
        type_hint: str
    response_parameters:
      - name: SMDSConn
        pcf_type: MQCFST
        type_hint: str
      - name: CFStrucName
        pcf_type: MQCFST
        type_hint: str
      - name: CommandScope
        pcf_type: MQCFST
        type_hint: str
    notes: []
  - name: MQCMD_STOP_CHANNEL
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
    notes: []
  - name: MQCMD_STOP_CHANNEL_INIT
    request_href: SSFKSJ_9.4.0/refadmin/q088500_.html
    response_href: SSFKSJ_9.4.0/refadmin/q088500_.html
    request_parameters:
      - name: CommandScope
        pcf_type: MQCFST
        type_hint: str
      - name: SharedChannelRestart
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQCHSH_RESTART_YES
          - MQCHSH_RESTART_NO
    response_parameters:
      - name: CommandScope
        pcf_type: MQCFST
        type_hint: str
      - name: SharedChannelRestart
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQCHSH_RESTART_YES
          - MQCHSH_RESTART_NO
    notes: []
  - name: MQCMD_STOP_CHANNEL_LISTENER
    request_href: SSFKSJ_9.4.0/refadmin/q088510_.html
    response_href: SSFKSJ_9.4.0/refadmin/q088510_.html
    request_parameters:
      - name: ListenerName
        pcf_type: MQCFST
        type_hint: str
      - name: CommandScope
        pcf_type: MQCFST
        type_hint: str
      - name: InboundDisposition
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQINBD_Q_MGR
          - MQINBD_GROUP
      - name: IPAddress
        pcf_type: MQCFST
        type_hint: str
      - name: Port
        pcf_type: MQCFIN
        type_hint: int
      - name: TransportType
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQXPT_LU62
          - MQXPT_TCP
          - MQIACF_IGNORE_STATE
          - MQIS_NO
          - MQIS_YES
          - MQRCCF_LISTENER_STOPPED
    response_parameters:
      - name: ListenerName
        pcf_type: MQCFST
        type_hint: str
      - name: CommandScope
        pcf_type: MQCFST
        type_hint: str
      - name: InboundDisposition
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQINBD_Q_MGR
          - MQINBD_GROUP
      - name: IPAddress
        pcf_type: MQCFST
        type_hint: str
      - name: Port
        pcf_type: MQCFIN
        type_hint: int
      - name: TransportType
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQXPT_LU62
          - MQXPT_TCP
          - MQIACF_IGNORE_STATE
          - MQIS_NO
          - MQIS_YES
          - MQRCCF_LISTENER_STOPPED
    notes: []
  - name: MQCMD_STOP_CONNECTION
    request_href: SSFKSJ_9.4.0/refadmin/q088520_.html
    response_href: SSFKSJ_9.4.0/refadmin/q088520_.html
    request_parameters:
      - name: ConnectionId
        pcf_type: MQCFBS
        type_hint: bytes
    response_parameters:
      - name: ConnectionId
        pcf_type: MQCFBS
        type_hint: bytes
    notes: []
  - name: MQCMD_STOP_SERVICE
    request_href: SSFKSJ_9.4.0/refadmin/q088530_.html
    response_href: SSFKSJ_9.4.0/refadmin/q088530_.html
    request_parameters:
      - name: ServiceName
        pcf_type: MQCFST
        type_hint: str
        enum_values:
          - MQIACF_IGNORE_STATE
          - MQIS_NO
          - MQIS_YES
          - MQRCCF_NO_STOP_CMD
          - MQRCCF_SERVICE_STOPPED
    response_parameters:
      - name: ServiceName
        pcf_type: MQCFST
        type_hint: str
        enum_values:
          - MQIACF_IGNORE_STATE
          - MQIS_NO
          - MQIS_YES
          - MQRCCF_NO_STOP_CMD
          - MQRCCF_SERVICE_STOPPED
    notes: []
  - name: MQCMD_STOP_SMDSCONN
    request_href: SSFKSJ_9.4.0/refadmin/q088540_.html
    response_href: SSFKSJ_9.4.0/refadmin/q088540_.html
    request_parameters:
      - name: SMDSConn
        pcf_type: MQCFST
        type_hint: str
      - name: CFStrucName
        pcf_type: MQCFST
        type_hint: str
      - name: CommandScope
        pcf_type: MQCFST
        type_hint: str
    response_parameters:
      - name: SMDSConn
        pcf_type: MQCFST
        type_hint: str
      - name: CFStrucName
        pcf_type: MQCFST
        type_hint: str
      - name: CommandScope
        pcf_type: MQCFST
        type_hint: str
    notes: []
  - name: MQCMD_SUSPEND_Q_MGR
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
    notes: []
  - name: MQCMD_SUSPEND_Q_MGR_CLUSTER
    request_href: SSFKSJ_9.4.0/refadmin/q088560_.html
    response_href: SSFKSJ_9.4.0/refadmin/q088560_.html
    request_parameters:
      - name: ClusterName
        pcf_type: MQCFST
        type_hint: str
      - name: ClusterNamelist
        pcf_type: MQCFST
        type_hint: str
      - name: CommandScope
        pcf_type: MQCFST
        type_hint: str
      - name: Mode
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQMODE_QUIESCE
          - MQMODE_FORCE
          - MQRCCF_CLUSTER_NAME_CONFLICT
          - MQRCCF_MODE_VALUE_ERROR
    response_parameters:
      - name: ClusterName
        pcf_type: MQCFST
        type_hint: str
      - name: ClusterNamelist
        pcf_type: MQCFST
        type_hint: str
      - name: CommandScope
        pcf_type: MQCFST
        type_hint: str
      - name: Mode
        pcf_type: MQCFIN
        type_hint: int
        enum_values:
          - MQMODE_QUIESCE
          - MQMODE_FORCE
          - MQRCCF_CLUSTER_NAME_CONFLICT
          - MQRCCF_MODE_VALUE_ERROR
    notes: []
```

## Notes and gaps
- DISPLAY command output parameters are derived from requested-parameter tables and syntax diagrams when available.
- Manual overrides for DISPLAY AUTHSERV, GROUP, LSSTATUS, MAXSMSGS, POLICY, and TRACE are captured in `scripts/dev/refresh_mqsc_output_parameters.py` (AUTHSERV, LSSTATUS, POLICY validated via `runCommandJSON` against the local MQ container).
- DISPLAY CHINIT and DISPLAY CMDSERV are z/OS-only; output parameters are not documented in the IBM docs pages and are not experimentally validated here.
- PCF response pages are not available for all commands; missing response metadata is expected.
- MQSC parameter types are not captured at this stage.
