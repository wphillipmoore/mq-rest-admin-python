# MQSC to PCF command mapping (first run)

This file captures the first-pass MQSC -> PCF command equivalence mapping. Parameter extraction is not yet populated; use this as a command coverage baseline.

## Table of Contents
- [Purpose](#purpose)
- [Sources](#sources)
- [Coverage summary](#coverage-summary)
- [Command mappings](#command-mappings)
- [Open gaps](#open-gaps)

## Purpose
Provide an initial command equivalence map across the MQSC namespace so parameter extraction can proceed in a controlled, auditable way.

## Sources
- MQSC commands index: https://www.ibm.com/docs/en/ibm-mq/9.4.x?topic=reference-mqsc-commands
- PCF commands index (partial list): https://www.ibm.com/docs/en/ibm-mq/9.4.x?topic=reference-definitions-programmable-command-formats

## Coverage summary
- MQSC commands: 139
- PCF index verification hits: 62
- Mapped (provisional): 132
- No-equivalent (verb or match missing): 7

## Command mappings
```yaml
version: 1
commands:
  - mqsc: ALTER AUTHINFO
    pcf: MQCMD_CHANGE_AUTH_INFO
    qualifier: authinfo
    status: provisional
    verification: not-in-index
    notes: normalized object; pcf not found in index
  - mqsc: ALTER BUFFPOOL
    pcf: MQCMD_CHANGE_BUFFPOOL
    qualifier: buffpool
    status: provisional
    verification: not-in-index
    notes: no normalization; pcf not found in index
  - mqsc: ALTER CFSTRUCT
    pcf: MQCMD_CHANGE_CF_STRUC
    qualifier: cfstruct
    status: provisional
    verification: not-in-index
    notes: normalized object; pcf not found in index
  - mqsc: ALTER CHANNEL
    pcf: MQCMD_CHANGE_CHANNEL
    qualifier: channel
    status: provisional
    verification: not-in-index
    notes: no normalization; pcf not found in index
  - mqsc: ALTER COMMINFO
    pcf: MQCMD_CHANGE_COMM_INFO
    qualifier: comminfo
    status: provisional
    verification: not-in-index
    notes: normalized object; pcf not found in index
  - mqsc: ALTER LISTENER
    pcf: MQCMD_CHANGE_LISTENER
    qualifier: listener
    status: provisional
    verification: not-in-index
    notes: no normalization; pcf not found in index
  - mqsc: ALTER NAMELIST
    pcf: MQCMD_CHANGE_NAMELIST
    qualifier: namelist
    status: provisional
    verification: not-in-index
    notes: no normalization; pcf not found in index
  - mqsc: ALTER PROCESS
    pcf: MQCMD_CHANGE_PROCESS
    qualifier: process
    status: provisional
    verification: not-in-index
    notes: no normalization; pcf not found in index
  - mqsc: ALTER PSID
    pcf: MQCMD_CHANGE_PSID
    qualifier: psid
    status: provisional
    verification: not-in-index
    notes: no normalization; pcf not found in index
  - mqsc: ALTER QMGR
    pcf: MQCMD_CHANGE_Q_MGR
    qualifier: qmgr
    status: provisional
    verification: index
    notes: normalized object
  - mqsc: ALTER SECURITY
    pcf: MQCMD_CHANGE_SECURITY
    qualifier: security
    status: provisional
    verification: index
    notes: no normalization
  - mqsc: ALTER SERVICE
    pcf: MQCMD_CHANGE_SERVICE
    qualifier: service
    status: provisional
    verification: not-in-index
    notes: no normalization; pcf not found in index
  - mqsc: ALTER SMDS
    pcf: MQCMD_CHANGE_SMDS
    qualifier: smds
    status: provisional
    verification: index
    notes: no normalization
  - mqsc: ALTER STGCLASS
    pcf: MQCMD_CHANGE_STGCLASS
    qualifier: stgclass
    status: provisional
    verification: not-in-index
    notes: no normalization; pcf not found in index
  - mqsc: ALTER SUB
    pcf: MQCMD_CHANGE_SUB
    qualifier: sub
    status: provisional
    verification: not-in-index
    notes: no normalization; pcf not found in index
  - mqsc: ALTER TOPIC
    pcf: MQCMD_CHANGE_TOPIC
    qualifier: topic
    status: provisional
    verification: not-in-index
    notes: no normalization; pcf not found in index
  - mqsc: ALTER TRACE
    pcf: MQCMD_CHANGE_TRACE
    qualifier: trace
    status: provisional
    verification: not-in-index
    notes: no normalization; pcf not found in index
  - mqsc: ARCHIVE LOG
    pcf: null
    qualifier: log
    status: no-equivalent
    verification: not-checked
    notes: no verb mapping
  - mqsc: BACKUP CFSTRUCT
    pcf: null
    qualifier: cfstruct
    status: no-equivalent
    verification: not-checked
    notes: no verb mapping
  - mqsc: CLEAR QLOCAL
    pcf: MQCMD_CLEAR_Q
    qualifier: queue
    status: provisional
    verification: index
    notes: normalized object
  - mqsc: CLEAR TOPICSTR
    pcf: MQCMD_CLEAR_TOPICSTR
    qualifier: topicstr
    status: provisional
    verification: not-in-index
    notes: no normalization; pcf not found in index
  - mqsc: DEFINE AUTHINFO
    pcf: MQCMD_CREATE_AUTH_INFO
    qualifier: authinfo
    status: provisional
    verification: not-in-index
    notes: normalized object; pcf not found in index
  - mqsc: DEFINE BUFFPOOL
    pcf: MQCMD_CREATE_BUFFPOOL
    qualifier: buffpool
    status: provisional
    verification: not-in-index
    notes: no normalization; pcf not found in index
  - mqsc: DEFINE CFSTRUCT
    pcf: MQCMD_CREATE_CF_STRUC
    qualifier: cfstruct
    status: provisional
    verification: not-in-index
    notes: normalized object; pcf not found in index
  - mqsc: DEFINE CHANNEL
    pcf: MQCMD_CREATE_CHANNEL
    qualifier: channel
    status: provisional
    verification: not-in-index
    notes: no normalization; pcf not found in index
  - mqsc: DEFINE COMMINFO
    pcf: MQCMD_CREATE_COMM_INFO
    qualifier: comminfo
    status: provisional
    verification: not-in-index
    notes: normalized object; pcf not found in index
  - mqsc: DEFINE LISTENER
    pcf: MQCMD_CREATE_LISTENER
    qualifier: listener
    status: provisional
    verification: not-in-index
    notes: no normalization; pcf not found in index
  - mqsc: DEFINE LOG
    pcf: MQCMD_CREATE_LOG
    qualifier: log
    status: provisional
    verification: not-in-index
    notes: no normalization; pcf not found in index
  - mqsc: DEFINE MAXSMSGS
    pcf: MQCMD_CREATE_MAXSMSGS
    qualifier: maxsmsgs
    status: provisional
    verification: not-in-index
    notes: no normalization; pcf not found in index
  - mqsc: DEFINE NAMELIST
    pcf: MQCMD_CREATE_NAMELIST
    qualifier: namelist
    status: provisional
    verification: not-in-index
    notes: no normalization; pcf not found in index
  - mqsc: DEFINE PROCESS
    pcf: MQCMD_CREATE_PROCESS
    qualifier: process
    status: provisional
    verification: not-in-index
    notes: no normalization; pcf not found in index
  - mqsc: DEFINE PSID
    pcf: MQCMD_CREATE_PSID
    qualifier: psid
    status: provisional
    verification: not-in-index
    notes: no normalization; pcf not found in index
  - mqsc: DEFINE SERVICE
    pcf: MQCMD_CREATE_SERVICE
    qualifier: service
    status: provisional
    verification: not-in-index
    notes: no normalization; pcf not found in index
  - mqsc: DEFINE STGCLASS
    pcf: MQCMD_CREATE_STGCLASS
    qualifier: stgclass
    status: provisional
    verification: not-in-index
    notes: no normalization; pcf not found in index
  - mqsc: DEFINE SUB
    pcf: MQCMD_CREATE_SUB
    qualifier: sub
    status: provisional
    verification: not-in-index
    notes: no normalization; pcf not found in index
  - mqsc: DEFINE TOPIC
    pcf: MQCMD_CREATE_TOPIC
    qualifier: topic
    status: provisional
    verification: not-in-index
    notes: no normalization; pcf not found in index
  - mqsc: DELETE AUTHINFO
    pcf: MQCMD_DELETE_AUTH_INFO
    qualifier: authinfo
    status: provisional
    verification: index
    notes: normalized object
  - mqsc: DELETE AUTHREC
    pcf: MQCMD_DELETE_AUTH_REC
    qualifier: authrec
    status: provisional
    verification: index
    notes: normalized object
  - mqsc: DELETE BUFFPOOL
    pcf: MQCMD_DELETE_BUFFPOOL
    qualifier: buffpool
    status: provisional
    verification: not-in-index
    notes: no normalization; pcf not found in index
  - mqsc: DELETE CFSTRUCT
    pcf: MQCMD_DELETE_CF_STRUC
    qualifier: cfstruct
    status: provisional
    verification: index
    notes: normalized object
  - mqsc: DELETE CHANNEL
    pcf: MQCMD_DELETE_CHANNEL
    qualifier: channel
    status: provisional
    verification: index
    notes: no normalization
  - mqsc: DELETE COMMINFO
    pcf: MQCMD_DELETE_COMM_INFO
    qualifier: comminfo
    status: provisional
    verification: index
    notes: normalized object
  - mqsc: DELETE LISTENER
    pcf: MQCMD_DELETE_LISTENER
    qualifier: listener
    status: provisional
    verification: index
    notes: no normalization
  - mqsc: DELETE NAMELIST
    pcf: MQCMD_DELETE_NAMELIST
    qualifier: namelist
    status: provisional
    verification: index
    notes: no normalization
  - mqsc: DELETE POLICY
    pcf: MQCMD_DELETE_POLICY
    qualifier: policy
    status: provisional
    verification: not-in-index
    notes: no normalization; pcf not found in index
  - mqsc: DELETE PROCESS
    pcf: MQCMD_DELETE_PROCESS
    qualifier: process
    status: provisional
    verification: index
    notes: no normalization
  - mqsc: DELETE PSID
    pcf: MQCMD_DELETE_PSID
    qualifier: psid
    status: provisional
    verification: not-in-index
    notes: no normalization; pcf not found in index
  - mqsc: DELETE SERVICE
    pcf: MQCMD_DELETE_SERVICE
    qualifier: service
    status: provisional
    verification: index
    notes: no normalization
  - mqsc: DELETE STGCLASS
    pcf: MQCMD_DELETE_STGCLASS
    qualifier: stgclass
    status: provisional
    verification: not-in-index
    notes: no normalization; pcf not found in index
  - mqsc: DELETE SUB
    pcf: MQCMD_DELETE_SUB
    qualifier: sub
    status: provisional
    verification: not-in-index
    notes: no normalization; pcf not found in index
  - mqsc: DELETE TOPIC
    pcf: MQCMD_DELETE_TOPIC
    qualifier: topic
    status: provisional
    verification: index
    notes: no normalization
  - mqsc: DISPLAY APSTATUS
    pcf: MQCMD_INQUIRE_AP_STATUS
    qualifier: apstatus
    status: provisional
    verification: not-in-index
    notes: normalized suffix; pcf not found in index
  - mqsc: DISPLAY ARCHIVE
    pcf: MQCMD_INQUIRE_ARCHIVE
    qualifier: archive
    status: provisional
    verification: index
    notes: no normalization
  - mqsc: DISPLAY AUTHINFO
    pcf: MQCMD_INQUIRE_AUTH_INFO
    qualifier: authinfo
    status: provisional
    verification: index
    notes: normalized object
  - mqsc: DISPLAY AUTHREC
    pcf: MQCMD_INQUIRE_AUTH_REC
    qualifier: authrec
    status: provisional
    verification: not-in-index
    notes: normalized object; pcf not found in index
  - mqsc: DISPLAY AUTHSERV
    pcf: MQCMD_INQUIRE_AUTHSERV
    qualifier: authserv
    status: provisional
    verification: not-in-index
    notes: no normalization; pcf not found in index
  - mqsc: DISPLAY CFSTATUS
    pcf: MQCMD_INQUIRE_CF_STATUS
    qualifier: cfstatus
    status: provisional
    verification: not-in-index
    notes: normalized suffix; pcf not found in index
  - mqsc: DISPLAY CFSTRUCT
    pcf: MQCMD_INQUIRE_CF_STRUC
    qualifier: cfstruct
    status: provisional
    verification: index
    notes: normalized object
  - mqsc: DISPLAY CHANNEL
    pcf: MQCMD_INQUIRE_CHANNEL
    qualifier: channel
    status: provisional
    verification: index
    notes: no normalization
  - mqsc: DISPLAY CHINIT
    pcf: MQCMD_INQUIRE_CHINIT
    qualifier: chinit
    status: provisional
    verification: not-in-index
    notes: no normalization; pcf not found in index
  - mqsc: DISPLAY CHLAUTH
    pcf: MQCMD_INQUIRE_CHLAUTH_RECS
    qualifier: channel
    status: provisional
    verification: index
    notes: chlauth uses record set for inquire
  - mqsc: DISPLAY CHSTATUS
    pcf: MQCMD_INQUIRE_CHANNEL_STATUS
    qualifier: channel
    status: provisional
    verification: index
    notes: normalized object
  - mqsc: DISPLAY CLUSQMGR
    pcf: MQCMD_INQUIRE_CLUSTER_Q_MGR
    qualifier: clusqmgr
    status: provisional
    verification: index
    notes: normalized object
  - mqsc: DISPLAY CMDSERV
    pcf: MQCMD_INQUIRE_CMDSERV
    qualifier: cmdserv
    status: provisional
    verification: not-in-index
    notes: no normalization; pcf not found in index
  - mqsc: DISPLAY COMMINFO
    pcf: MQCMD_INQUIRE_COMM_INFO
    qualifier: comminfo
    status: provisional
    verification: index
    notes: normalized object
  - mqsc: DISPLAY CONN
    pcf: MQCMD_INQUIRE_CONN
    qualifier: conn
    status: provisional
    verification: not-in-index
    notes: no normalization; pcf not found in index
  - mqsc: DISPLAY ENTAUTH
    pcf: MQCMD_INQUIRE_ENTAUTH
    qualifier: entauth
    status: provisional
    verification: not-in-index
    notes: no normalization; pcf not found in index
  - mqsc: DISPLAY GROUP
    pcf: MQCMD_INQUIRE_GROUP
    qualifier: group
    status: provisional
    verification: not-in-index
    notes: no normalization; pcf not found in index
  - mqsc: DISPLAY LISTENER
    pcf: MQCMD_INQUIRE_LISTENER
    qualifier: listener
    status: provisional
    verification: index
    notes: no normalization
  - mqsc: DISPLAY LOG
    pcf: MQCMD_INQUIRE_LOG
    qualifier: log
    status: provisional
    verification: index
    notes: no normalization
  - mqsc: DISPLAY LSSTATUS
    pcf: MQCMD_INQUIRE_LS_STATUS
    qualifier: lsstatus
    status: provisional
    verification: not-in-index
    notes: normalized suffix; pcf not found in index
  - mqsc: DISPLAY MAXSMSGS
    pcf: MQCMD_INQUIRE_MAXSMSGS
    qualifier: maxsmsgs
    status: provisional
    verification: not-in-index
    notes: no normalization; pcf not found in index
  - mqsc: DISPLAY NAMELIST
    pcf: MQCMD_INQUIRE_NAMELIST
    qualifier: namelist
    status: provisional
    verification: index
    notes: no normalization
  - mqsc: DISPLAY POLICY
    pcf: MQCMD_INQUIRE_POLICY
    qualifier: policy
    status: provisional
    verification: not-in-index
    notes: no normalization; pcf not found in index
  - mqsc: DISPLAY PROCESS
    pcf: MQCMD_INQUIRE_PROCESS
    qualifier: process
    status: provisional
    verification: index
    notes: no normalization
  - mqsc: DISPLAY PUBSUB
    pcf: MQCMD_INQUIRE_PUBSUB
    qualifier: pubsub
    status: provisional
    verification: not-in-index
    notes: no normalization; pcf not found in index
  - mqsc: DISPLAY QMGR
    pcf: MQCMD_INQUIRE_Q_MGR
    qualifier: qmgr
    status: provisional
    verification: index
    notes: normalized object
  - mqsc: DISPLAY QMSTATUS
    pcf: MQCMD_INQUIRE_Q_MGR_STATUS
    qualifier: qmgr
    status: provisional
    verification: index
    notes: normalized object
  - mqsc: DISPLAY QSTATUS
    pcf: MQCMD_INQUIRE_Q_STATUS
    qualifier: queue
    status: provisional
    verification: index
    notes: normalized object
  - mqsc: DISPLAY QUEUE
    pcf: MQCMD_INQUIRE_Q
    qualifier: queue
    status: provisional
    verification: index
    notes: normalized object
  - mqsc: DISPLAY SBSTATUS
    pcf: MQCMD_INQUIRE_SB_STATUS
    qualifier: sbstatus
    status: provisional
    verification: not-in-index
    notes: normalized suffix; pcf not found in index
  - mqsc: DISPLAY SECURITY
    pcf: MQCMD_INQUIRE_SECURITY
    qualifier: security
    status: provisional
    verification: index
    notes: no normalization
  - mqsc: DISPLAY SERVICE
    pcf: MQCMD_INQUIRE_SERVICE
    qualifier: service
    status: provisional
    verification: index
    notes: no normalization
  - mqsc: DISPLAY SMDS
    pcf: MQCMD_INQUIRE_SMDS
    qualifier: smds
    status: provisional
    verification: index
    notes: no normalization
  - mqsc: DISPLAY SMDSCONN
    pcf: MQCMD_INQUIRE_SMDSCONN
    qualifier: smdsconn
    status: provisional
    verification: index
    notes: no normalization
  - mqsc: DISPLAY STGCLASS
    pcf: MQCMD_INQUIRE_STGCLASS
    qualifier: stgclass
    status: provisional
    verification: not-in-index
    notes: no normalization; pcf not found in index
  - mqsc: DISPLAY SUB
    pcf: MQCMD_INQUIRE_SUB
    qualifier: sub
    status: provisional
    verification: not-in-index
    notes: no normalization; pcf not found in index
  - mqsc: DISPLAY SVSTATUS
    pcf: MQCMD_INQUIRE_SV_STATUS
    qualifier: svstatus
    status: provisional
    verification: not-in-index
    notes: normalized suffix; pcf not found in index
  - mqsc: DISPLAY SYSTEM
    pcf: MQCMD_INQUIRE_SYSTEM
    qualifier: system
    status: provisional
    verification: index
    notes: no normalization
  - mqsc: DISPLAY TCLUSTER
    pcf: MQCMD_INQUIRE_TCLUSTER
    qualifier: tcluster
    status: provisional
    verification: not-in-index
    notes: no normalization; pcf not found in index
  - mqsc: DISPLAY THREAD
    pcf: MQCMD_INQUIRE_THREAD
    qualifier: thread
    status: provisional
    verification: not-in-index
    notes: no normalization; pcf not found in index
  - mqsc: DISPLAY TOPIC
    pcf: MQCMD_INQUIRE_TOPIC
    qualifier: topic
    status: provisional
    verification: index
    notes: no normalization
  - mqsc: DISPLAY TPSTATUS
    pcf: MQCMD_INQUIRE_TP_STATUS
    qualifier: tpstatus
    status: provisional
    verification: not-in-index
    notes: normalized suffix; pcf not found in index
  - mqsc: DISPLAY TRACE
    pcf: MQCMD_INQUIRE_TRACE
    qualifier: trace
    status: provisional
    verification: not-in-index
    notes: no normalization; pcf not found in index
  - mqsc: DISPLAY USAGE
    pcf: MQCMD_INQUIRE_USAGE
    qualifier: usage
    status: provisional
    verification: index
    notes: no normalization
  - mqsc: MOVE QLOCAL
    pcf: null
    qualifier: queue
    status: no-equivalent
    verification: not-checked
    notes: no verb mapping
  - mqsc: PING CHANNEL
    pcf: MQCMD_PING_CHANNEL
    qualifier: channel
    status: provisional
    verification: index
    notes: no normalization
  - mqsc: PING QMGR
    pcf: MQCMD_PING_Q_MGR
    qualifier: qmgr
    status: provisional
    verification: index
    notes: normalized object
  - mqsc: PURGE CHANNEL
    pcf: null
    qualifier: channel
    status: no-equivalent
    verification: not-checked
    notes: no verb mapping
  - mqsc: RECOVER BSDS
    pcf: null
    qualifier: bsds
    status: no-equivalent
    verification: not-checked
    notes: no verb mapping
  - mqsc: RECOVER CFSTRUCT
    pcf: null
    qualifier: cfstruct
    status: no-equivalent
    verification: not-checked
    notes: no verb mapping
  - mqsc: REFRESH CLUSTER
    pcf: MQCMD_REFRESH_CLUSTER
    qualifier: cluster
    status: provisional
    verification: index
    notes: no normalization
  - mqsc: REFRESH QMGR
    pcf: MQCMD_REFRESH_Q_MGR
    qualifier: qmgr
    status: provisional
    verification: index
    notes: normalized object
  - mqsc: REFRESH SECURITY
    pcf: MQCMD_REFRESH_SECURITY
    qualifier: security
    status: provisional
    verification: index
    notes: no normalization
  - mqsc: RESET CFSTRUCT
    pcf: MQCMD_RESET_CF_STRUC
    qualifier: cfstruct
    status: provisional
    verification: index
    notes: normalized object
  - mqsc: RESET CHANNEL
    pcf: MQCMD_RESET_CHANNEL
    qualifier: channel
    status: provisional
    verification: index
    notes: no normalization
  - mqsc: RESET CLUSTER
    pcf: MQCMD_RESET_CLUSTER
    qualifier: cluster
    status: provisional
    verification: index
    notes: no normalization
  - mqsc: RESET QMGR
    pcf: MQCMD_RESET_Q_MGR
    qualifier: qmgr
    status: provisional
    verification: index
    notes: normalized object
  - mqsc: RESET QSTATS
    pcf: MQCMD_RESET_Q_STATS
    qualifier: queue
    status: provisional
    verification: index
    notes: normalized object
  - mqsc: RESET SMDS
    pcf: MQCMD_RESET_SMDS
    qualifier: smds
    status: provisional
    verification: index
    notes: no normalization
  - mqsc: RESET TPIPE
    pcf: MQCMD_RESET_TPIPE
    qualifier: tpipe
    status: provisional
    verification: not-in-index
    notes: no normalization; pcf not found in index
  - mqsc: RESOLVE CHANNEL
    pcf: MQCMD_RESOLVE_CHANNEL
    qualifier: channel
    status: provisional
    verification: index
    notes: no normalization
  - mqsc: RESOLVE INDOUBT
    pcf: MQCMD_RESOLVE_INDOUBT
    qualifier: indoubt
    status: provisional
    verification: not-in-index
    notes: no normalization; pcf not found in index
  - mqsc: RESUME QMGR
    pcf: MQCMD_RESUME_Q_MGR
    qualifier: qmgr
    status: provisional
    verification: index
    notes: normalized object
  - mqsc: RVERIFY SECURITY
    pcf: null
    qualifier: security
    status: no-equivalent
    verification: not-checked
    notes: no verb mapping
  - mqsc: SET ARCHIVE
    pcf: MQCMD_SET_ARCHIVE
    qualifier: archive
    status: provisional
    verification: index
    notes: no normalization
  - mqsc: SET AUTHREC
    pcf: MQCMD_SET_AUTH_REC
    qualifier: authrec
    status: provisional
    verification: index
    notes: normalized object
  - mqsc: SET CHLAUTH
    pcf: MQCMD_SET_CHLAUTH_REC
    qualifier: channel
    status: provisional
    verification: index
    notes: chlauth uses record for change/set/delete
  - mqsc: SET LOG
    pcf: MQCMD_SET_LOG
    qualifier: log
    status: provisional
    verification: index
    notes: no normalization
  - mqsc: SET POLICY
    pcf: MQCMD_SET_POLICY
    qualifier: policy
    status: provisional
    verification: not-in-index
    notes: no normalization; pcf not found in index
  - mqsc: SET SYSTEM
    pcf: MQCMD_SET_SYSTEM
    qualifier: system
    status: provisional
    verification: index
    notes: no normalization
  - mqsc: START CHANNEL
    pcf: MQCMD_START_CHANNEL
    qualifier: channel
    status: provisional
    verification: index
    notes: no normalization
  - mqsc: START CHINIT
    pcf: MQCMD_START_CHINIT
    qualifier: chinit
    status: provisional
    verification: not-in-index
    notes: no normalization; pcf not found in index
  - mqsc: START CMDSERV
    pcf: MQCMD_START_CMDSERV
    qualifier: cmdserv
    status: provisional
    verification: not-in-index
    notes: no normalization; pcf not found in index
  - mqsc: START LISTENER
    pcf: MQCMD_START_LISTENER
    qualifier: listener
    status: provisional
    verification: not-in-index
    notes: no normalization; pcf not found in index
  - mqsc: START QMGR
    pcf: MQCMD_START_Q_MGR
    qualifier: qmgr
    status: provisional
    verification: not-in-index
    notes: normalized object; pcf not found in index
  - mqsc: START SERVICE
    pcf: MQCMD_START_SERVICE
    qualifier: service
    status: provisional
    verification: index
    notes: no normalization
  - mqsc: START SMDSCONN
    pcf: MQCMD_START_SMDSCONN
    qualifier: smdsconn
    status: provisional
    verification: index
    notes: no normalization
  - mqsc: START TRACE
    pcf: MQCMD_START_TRACE
    qualifier: trace
    status: provisional
    verification: not-in-index
    notes: no normalization; pcf not found in index
  - mqsc: STOP CHANNEL
    pcf: MQCMD_STOP_CHANNEL
    qualifier: channel
    status: provisional
    verification: index
    notes: no normalization
  - mqsc: STOP CHINIT
    pcf: MQCMD_STOP_CHINIT
    qualifier: chinit
    status: provisional
    verification: not-in-index
    notes: no normalization; pcf not found in index
  - mqsc: STOP CMDSERV
    pcf: MQCMD_STOP_CMDSERV
    qualifier: cmdserv
    status: provisional
    verification: not-in-index
    notes: no normalization; pcf not found in index
  - mqsc: STOP CONN
    pcf: MQCMD_STOP_CONN
    qualifier: conn
    status: provisional
    verification: not-in-index
    notes: no normalization; pcf not found in index
  - mqsc: STOP LISTENER
    pcf: MQCMD_STOP_LISTENER
    qualifier: listener
    status: provisional
    verification: not-in-index
    notes: no normalization; pcf not found in index
  - mqsc: STOP QMGR
    pcf: MQCMD_STOP_Q_MGR
    qualifier: qmgr
    status: provisional
    verification: not-in-index
    notes: normalized object; pcf not found in index
  - mqsc: STOP SERVICE
    pcf: MQCMD_STOP_SERVICE
    qualifier: service
    status: provisional
    verification: index
    notes: no normalization
  - mqsc: STOP SMDSCONN
    pcf: MQCMD_STOP_SMDSCONN
    qualifier: smdsconn
    status: provisional
    verification: index
    notes: no normalization
  - mqsc: STOP TRACE
    pcf: MQCMD_STOP_TRACE
    qualifier: trace
    status: provisional
    verification: not-in-index
    notes: no normalization; pcf not found in index
  - mqsc: SUSPEND QMGR
    pcf: MQCMD_SUSPEND_Q_MGR
    qualifier: qmgr
    status: provisional
    verification: index
    notes: normalized object
```

## Open gaps
- Parameter extraction (MQSC inputs/outputs and PCF request/response) is not populated in this run.
- PCF command verification is limited to the index page content; some inferred names may be valid but are not yet confirmed.
- Verb mappings for ARCHIVE, BACKUP, MOVE, PURGE, RECOVER, and RVERIFY are not defined and require manual review.