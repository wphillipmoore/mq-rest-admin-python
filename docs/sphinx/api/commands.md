# Commands

`MQRESTSession` provides a method for every MQSC command. Method names
follow the pattern `<verb>_<qualifier>` in lowercase.

All methods accept these optional parameters:

name
: Object name or pattern (required for most non-QMGR commands).

request_parameters
: Request attributes as a dict. Mapped from `snake_case` when mapping
  is enabled.

response_parameters
: List of response attribute names to return. Defaults to `["all"]`.

`DISPLAY` methods also accept:

where
: Filter expression (e.g. `"current_depth GT 100"`). The keyword is
  mapped from `snake_case` when mapping is enabled.

## Return types

**DISPLAY commands** return `list[dict[str, object]]` — an empty list
if no objects match.

**Queue manager singletons** (`display_qmgr`, `display_qmstatus`,
`display_cmdserv`) return `dict[str, object] | None`.

**All other commands** return `None` on success, raise
`MQRESTCommandError` on failure.

## DISPLAY methods

| Method | MQSC command | Qualifier mapping |
| --- | --- | --- |
| `display_apstatus()` | `DISPLAY APSTATUS` | apstatus |
| `display_archive()` | `DISPLAY ARCHIVE` | archive |
| `display_authinfo()` | `DISPLAY AUTHINFO` | authinfo |
| `display_authrec()` | `DISPLAY AUTHREC` | authrec |
| `display_authserv()` | `DISPLAY AUTHSERV` | authserv |
| `display_cfstatus()` | `DISPLAY CFSTATUS` | cfstatus |
| `display_cfstruct()` | `DISPLAY CFSTRUCT` | cfstruct |
| `display_channel()` | `DISPLAY CHANNEL` | channel |
| `display_chinit()` | `DISPLAY CHINIT` | chinit |
| `display_chlauth()` | `DISPLAY CHLAUTH` | chlauth |
| `display_chstatus()` | `DISPLAY CHSTATUS` | chstatus |
| `display_clusqmgr()` | `DISPLAY CLUSQMGR` | clusqmgr |
| `display_cmdserv()` | `DISPLAY CMDSERV` | cmdserv |
| `display_comminfo()` | `DISPLAY COMMINFO` | comminfo |
| `display_conn()` | `DISPLAY CONN` | conn |
| `display_entauth()` | `DISPLAY ENTAUTH` | entauth |
| `display_group()` | `DISPLAY GROUP` | group |
| `display_listener()` | `DISPLAY LISTENER` | listener |
| `display_log()` | `DISPLAY LOG` | log |
| `display_lsstatus()` | `DISPLAY LSSTATUS` | lsstatus |
| `display_maxsmsgs()` | `DISPLAY MAXSMSGS` | maxsmsgs |
| `display_namelist()` | `DISPLAY NAMELIST` | namelist |
| `display_policy()` | `DISPLAY POLICY` | policy |
| `display_process()` | `DISPLAY PROCESS` | process |
| `display_pubsub()` | `DISPLAY PUBSUB` | pubsub |
| `display_qmgr()` | `DISPLAY QMGR` | qmgr |
| `display_qmstatus()` | `DISPLAY QMSTATUS` | qmgr |
| `display_qstatus()` | `DISPLAY QSTATUS` | queue |
| `display_queue()` | `DISPLAY QUEUE` | queue |
| `display_sbstatus()` | `DISPLAY SBSTATUS` | sbstatus |
| `display_security()` | `DISPLAY SECURITY` | security |
| `display_service()` | `DISPLAY SERVICE` | service |
| `display_smds()` | `DISPLAY SMDS` | smds |
| `display_smdsconn()` | `DISPLAY SMDSCONN` | smdsconn |
| `display_stgclass()` | `DISPLAY STGCLASS` | stgclass |
| `display_sub()` | `DISPLAY SUB` | sub |
| `display_svstatus()` | `DISPLAY SVSTATUS` | svstatus |
| `display_tcluster()` | `DISPLAY TCLUSTER` | tcluster |
| `display_thread()` | `DISPLAY THREAD` | thread |
| `display_topic()` | `DISPLAY TOPIC` | topic |
| `display_tpstatus()` | `DISPLAY TPSTATUS` | tpstatus |
| `display_trace()` | `DISPLAY TRACE` | trace |
| `display_usage()` | `DISPLAY USAGE` | usage |

## DEFINE methods

| Method | MQSC command | Qualifier mapping |
| --- | --- | --- |
| `define_authinfo()` | `DEFINE AUTHINFO` | authinfo |
| `define_buffpool()` | `DEFINE BUFFPOOL` | buffpool |
| `define_cfstruct()` | `DEFINE CFSTRUCT` | cfstruct |
| `define_channel()` | `DEFINE CHANNEL` | channel |
| `define_comminfo()` | `DEFINE COMMINFO` | comminfo |
| `define_listener()` | `DEFINE LISTENER` | listener |
| `define_log()` | `DEFINE LOG` | log |
| `define_maxsmsgs()` | `DEFINE MAXSMSGS` | maxsmsgs |
| `define_namelist()` | `DEFINE NAMELIST` | namelist |
| `define_process()` | `DEFINE PROCESS` | process |
| `define_psid()` | `DEFINE PSID` | psid |
| `define_qalias()` | `DEFINE QALIAS` | queue |
| `define_qlocal()` | `DEFINE QLOCAL` | queue |
| `define_qmodel()` | `DEFINE QMODEL` | queue |
| `define_qremote()` | `DEFINE QREMOTE` | queue |
| `define_service()` | `DEFINE SERVICE` | service |
| `define_stgclass()` | `DEFINE STGCLASS` | stgclass |
| `define_sub()` | `DEFINE SUB` | sub |
| `define_topic()` | `DEFINE TOPIC` | topic |

## DELETE methods

| Method | MQSC command | Qualifier mapping |
| --- | --- | --- |
| `delete_authinfo()` | `DELETE AUTHINFO` | authinfo |
| `delete_authrec()` | `DELETE AUTHREC` | authrec |
| `delete_buffpool()` | `DELETE BUFFPOOL` | buffpool |
| `delete_cfstruct()` | `DELETE CFSTRUCT` | cfstruct |
| `delete_channel()` | `DELETE CHANNEL` | channel |
| `delete_comminfo()` | `DELETE COMMINFO` | comminfo |
| `delete_listener()` | `DELETE LISTENER` | listener |
| `delete_namelist()` | `DELETE NAMELIST` | namelist |
| `delete_policy()` | `DELETE POLICY` | policy |
| `delete_process()` | `DELETE PROCESS` | process |
| `delete_psid()` | `DELETE PSID` | psid |
| `delete_queue()` | `DELETE QUEUE` | queue |
| `delete_service()` | `DELETE SERVICE` | service |
| `delete_stgclass()` | `DELETE STGCLASS` | stgclass |
| `delete_sub()` | `DELETE SUB` | sub |
| `delete_topic()` | `DELETE TOPIC` | topic |

## ALTER methods

| Method | MQSC command | Qualifier mapping |
| --- | --- | --- |
| `alter_authinfo()` | `ALTER AUTHINFO` | authinfo |
| `alter_buffpool()` | `ALTER BUFFPOOL` | buffpool |
| `alter_cfstruct()` | `ALTER CFSTRUCT` | cfstruct |
| `alter_channel()` | `ALTER CHANNEL` | channel |
| `alter_comminfo()` | `ALTER COMMINFO` | comminfo |
| `alter_listener()` | `ALTER LISTENER` | listener |
| `alter_namelist()` | `ALTER NAMELIST` | namelist |
| `alter_process()` | `ALTER PROCESS` | process |
| `alter_psid()` | `ALTER PSID` | psid |
| `alter_qmgr()` | `ALTER QMGR` | qmgr |
| `alter_security()` | `ALTER SECURITY` | security |
| `alter_service()` | `ALTER SERVICE` | service |
| `alter_smds()` | `ALTER SMDS` | smds |
| `alter_stgclass()` | `ALTER STGCLASS` | stgclass |
| `alter_sub()` | `ALTER SUB` | sub |
| `alter_topic()` | `ALTER TOPIC` | topic |
| `alter_trace()` | `ALTER TRACE` | trace |

## SET methods

| Method | MQSC command | Qualifier mapping |
| --- | --- | --- |
| `set_archive()` | `SET ARCHIVE` | archive |
| `set_authrec()` | `SET AUTHREC` | authrec |
| `set_chlauth()` | `SET CHLAUTH` | chlauth |
| `set_log()` | `SET LOG` | log |
| `set_policy()` | `SET POLICY` | policy |

## START methods

| Method | MQSC command | Qualifier mapping |
| --- | --- | --- |
| `start_channel()` | `START CHANNEL` | channel |
| `start_chinit()` | `START CHINIT` | chinit |
| `start_cmdserv()` | `START CMDSERV` | cmdserv |
| `start_listener()` | `START LISTENER` | listener |
| `start_qmgr()` | `START QMGR` | qmgr |
| `start_service()` | `START SERVICE` | service |
| `start_smdsconn()` | `START SMDSCONN` | smdsconn |
| `start_trace()` | `START TRACE` | trace |

## STOP methods

| Method | MQSC command | Qualifier mapping |
| --- | --- | --- |
| `stop_channel()` | `STOP CHANNEL` | channel |
| `stop_chinit()` | `STOP CHINIT` | chinit |
| `stop_cmdserv()` | `STOP CMDSERV` | cmdserv |
| `stop_conn()` | `STOP CONN` | conn |
| `stop_listener()` | `STOP LISTENER` | listener |
| `stop_qmgr()` | `STOP QMGR` | qmgr |
| `stop_service()` | `STOP SERVICE` | service |
| `stop_smdsconn()` | `STOP SMDSCONN` | smdsconn |
| `stop_trace()` | `STOP TRACE` | trace |

## Other methods

| Method | MQSC command | Qualifier mapping |
| --- | --- | --- |
| `archive_log()` | `ARCHIVE LOG` | log |
| `backup_cfstruct()` | `BACKUP CFSTRUCT` | cfstruct |
| `clear_qlocal()` | `CLEAR QLOCAL` | queue |
| `clear_topicstr()` | `CLEAR TOPICSTR` | topicstr |
| `move_qlocal()` | `MOVE QLOCAL` | queue |
| `ping_channel()` | `PING CHANNEL` | channel |
| `ping_qmgr()` | `PING QMGR` | qmgr |
| `purge_channel()` | `PURGE CHANNEL` | channel |
| `recover_bsds()` | `RECOVER BSDS` | bsds |
| `recover_cfstruct()` | `RECOVER CFSTRUCT` | cfstruct |
| `refresh_cluster()` | `REFRESH CLUSTER` | cluster |
| `refresh_qmgr()` | `REFRESH QMGR` | qmgr |
| `refresh_security()` | `REFRESH SECURITY` | security |
| `reset_cfstruct()` | `RESET CFSTRUCT` | cfstruct |
| `reset_channel()` | `RESET CHANNEL` | channel |
| `reset_cluster()` | `RESET CLUSTER` | cluster |
| `reset_qmgr()` | `RESET QMGR` | qmgr |
| `reset_qstats()` | `RESET QSTATS` | queue |
| `reset_smds()` | `RESET SMDS` | smds |
| `reset_tpipe()` | `RESET TPIPE` | tpipe |
| `resolve_channel()` | `RESOLVE CHANNEL` | channel |
| `resolve_indoubt()` | `RESOLVE INDOUBT` | indoubt |
| `resume_qmgr()` | `RESUME QMGR` | qmgr |
| `rverify_security()` | `RVERIFY SECURITY` | security |
| `suspend_qmgr()` | `SUSPEND QMGR` | qmgr |
