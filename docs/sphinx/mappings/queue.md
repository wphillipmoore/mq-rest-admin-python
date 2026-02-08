# queue

Attribute mapping reference for the `queue` qualifier.

Related MQSC commands: `CLEAR QLOCAL`, `DISPLAY QSTATUS`, `DISPLAY QUEUE`, `MOVE QLOCAL`, `RESET QSTATS`

## Request key map

| Python name | MQSC parameter |
| --- | --- |
| `authrec` | `AUTHREC` |
| `backout_requeue_name` | `BOQNAME` |
| `backout_threshold` | `BOTHRESH` |
| `cf_struct_name` | `CFSTRUCT` |
| `cluster_channel_name` | `CLCHNAME` |
| `cluster_name` | `CLUSTER` |
| `cluster_namelist` | `CLUSNL` |
| `cluster_workload_priority` | `CLWLPRTY` |
| `cluster_workload_rank` | `CLWLRANK` |
| `cluster_workload_use_queue` | `CLWLUSEQ` |
| `command_scope` | `CMDSCOPE` |
| `custom` | `CUSTOM` |
| `def_bind` | `DEFBIND` |
| `def_input_open_option` | `DEFSOPT` |
| `def_persistence` | `DEFPSIST` |
| `def_priority` | `DEFPRTY` |
| `def_read_ahead` | `DEFREADA` |
| `default_put_response` | `DEFPRESP` |
| `definition_type` | `DEFTYPE` |
| `description` | `DESCR` |
| `dist_lists` | `DISTL` |
| `force` | `FORCE` |
| `harden_get_backout` | `HARDENBO` |
| `ignore_state` | `IGNSTATE` |
| `image_recover_queue` | `IMGRCOVQ` |
| `inhibit_get` | `GET` |
| `inhibit_put` | `PUT` |
| `initiation_q_name` | `INITQ` |
| `like` | `LIKE` |
| `max_message_length` | `MAXMSGL` |
| `max_q_depth` | `MAXDEPTH` |
| `max_q_file_size` | `MAXFSIZE` |
| `message_delivery_sequence` | `MSGDLVSQ` |
| `non_persistent_message_class` | `NPMCLASS` |
| `page_set_id` | `PSID` |
| `process_name` | `PROCESS` |
| `property_control` | `PROPCTL` |
| `q_depth_high_event` | `QDPHIEV` |
| `q_depth_high_limit` | `QDEPTHHI` |
| `q_depth_low_event` | `QDPLOEV` |
| `q_depth_low_limit` | `QDEPTHLO` |
| `q_depth_max_event` | `QDPMAXEV` |
| `q_service_interval` | `QSVCINT` |
| `qsg_disposition` | `QSGDISP` |
| `queue_accounting` | `ACCTQ` |
| `queue_monitoring` | `MONQ` |
| `queue_statistics` | `STATQ` |
| `remote_q_mgr_name` | `RQMNAME` |
| `remote_q_name` | `RNAME` |
| `retention_interval` | `RETINTVL` |
| `scope` | `SCOPE` |
| `shareability` | `SHARE` |
| `storage_class` | `STGCLASS` |
| `stream_q` | `STREAMQ` |
| `stream_q_service` | `STRMQOS` |
| `target_type` | `TARGTYPE` |
| `to_q_name` | `TOQLOCAL` |
| `transmission_q_name` | `XMITQ` |
| `trigger_control` | `TRIGGER` |
| `trigger_data` | `TRIGDATA` |
| `trigger_depth` | `TRIGDPTH` |
| `trigger_message_priority` | `TRIGMPRI` |
| `trigger_type` | `TRIGTYPE` |
| `usage` | `USAGE` |

## Response key map

| MQSC parameter | Python name |
| --- | --- |
| `ACCTQ` | `queue_accounting` |
| `ALTDATE` | `alteration_date` |
| `ALTTIME` | `alteration_time` |
| `APPLDESC` | `appl_desc` |
| `APPLTAG` | `appl_tag` |
| `APPLTYPE` | `appl_type` |
| `ASID` | `as_id` |
| `ASTATE` | `asynchronous_state` |
| `BOQNAME` | `backout_requeue_name` |
| `BOTHRESH` | `backout_threshold` |
| `BROWSE` | `open_browse` |
| `CAPEXPRY` | `cap_expiry` |
| `CFSTRUCT` | `cf_struct_name` |
| `CHANNEL` | `channel_name` |
| `CLCHNAME` | `cluster_channel_name` |
| `CLUSDATE` | `cluster_date` |
| `CLUSNL` | `cluster_namelist` |
| `CLUSQMGR` | `cluster_q_mgr` |
| `CLUSQT` | `cluster_q_type` |
| `CLUSTER` | `cluster_name` |
| `CLUSTIME` | `cluster_time` |
| `CLWLPRTY` | `cluster_workload_priority` |
| `CLWLRANK` | `cluster_workload_rank` |
| `CLWLUSEQ` | `cluster_workload_use_queue` |
| `CONNAME` | `connection_name` |
| `CRDATE` | `creation_date` |
| `CRTIME` | `creation_time` |
| `CURDEPTH` | `current_q_depth` |
| `CURFSIZE` | `current_q_file_size` |
| `CURMAXFS` | `current_max_q_file_size` |
| `CUSTOM` | `custom` |
| `DEFBIND` | `def_bind` |
| `DEFPRESP` | `default_put_response` |
| `DEFPRTY` | `def_priority` |
| `DEFPSIST` | `def_persistence` |
| `DEFREADA` | `def_read_ahead` |
| `DEFSOPT` | `def_input_open_option` |
| `DEFTYPE` | `definition_type` |
| `DESCR` | `description` |
| `DISTL` | `dist_lists` |
| `GET` | `inhibit_get` |
| `HARDENBO` | `harden_get_backout` |
| `HSTATE` | `handle_state` |
| `IMGRCOVQ` | `image_recover_queue` |
| `INDXTYPE` | `index_type` |
| `INITQ` | `initiation_q_name` |
| `INQUIRE` | `open_inquire` |
| `IPPROCS` | `open_input_count` |
| `LGETDATE` | `last_get_date` |
| `LGETTIME` | `last_get_time` |
| `LPUTDATE` | `last_put_date` |
| `LPUTTIME` | `last_put_time` |
| `MAXDEPTH` | `max_q_depth` |
| `MAXFSIZE` | `max_q_file_size` |
| `MAXMSGL` | `max_message_length` |
| `MEDIALOG` | `media_recovery_log_extent` |
| `MONQ` | `queue_monitoring` |
| `MSGAGE` | `oldest_message_age` |
| `MSGDLVSQ` | `message_delivery_sequence` |
| `NPMCLASS` | `non_persistent_message_class` |
| `OPPROCS` | `open_output_count` |
| `OTELPCTL` | `otel_propagation_control` |
| `OTELTRAC` | `otel_trace` |
| `OUTPUT` | `open_output` |
| `PID` | `process_id` |
| `PROCESS` | `process_name` |
| `PROPCTL` | `property_control` |
| `PSBNAME` | `psb_name` |
| `PSID` | `page_set_id` |
| `PSTID` | `pst_id` |
| `PUT` | `inhibit_put` |
| `QDEPTHHI` | `q_depth_high_limit` |
| `QDEPTHLO` | `q_depth_low_limit` |
| `QDPHIEV` | `q_depth_high_event` |
| `QDPLOEV` | `q_depth_low_event` |
| `QDPMAXEV` | `q_depth_max_event` |
| `QMID` | `q_mgr_id` |
| `QMURID` | `q_mgr_uow_id` |
| `QSGDISP` | `qsg_disposition` |
| `QSVCINT` | `q_service_interval` |
| `QTIME` | `on_q_time` |
| `QTYPE` | `q_type` |
| `RETINTVL` | `retention_interval` |
| `RNAME` | `remote_q_name` |
| `RQMNAME` | `remote_q_mgr_name` |
| `SCOPE` | `scope` |
| `SET` | `open_set` |
| `SHARE` | `shareability` |
| `STATQ` | `queue_statistics` |
| `STGCLASS` | `storage_class` |
| `STREAMQ` | `stream_q` |
| `STRMQOS` | `stream_q_service` |
| `TARGTYPE` | `target_type` |
| `TASKNO` | `task_number` |
| `TID` | `thread_id` |
| `TPIPE` | `tpipe_names` |
| `TRANSID` | `transaction_id` |
| `TRIGDATA` | `trigger_data` |
| `TRIGDPTH` | `trigger_depth` |
| `TRIGGER` | `trigger_control` |
| `TRIGMPRI` | `trigger_message_priority` |
| `TRIGTYPE` | `trigger_type` |
| `UNCOM` | `uncommitted_messages` |
| `URID` | `uow_id` |
| `URTYPE` | `uow_type` |
| `USAGE` | `usage` |
| `USERID` | `user_id` |
| `XMITQ` | `transmission_q_name` |

## Request value map

### def_persistence

| Python value | MQSC value |
| --- | --- |
| `def` | `DEF` |
| `not_fixed` | `NOTFIXED` |

## Response value map

### DEFPSIST

| MQSC value | Python value |
| --- | --- |
| `DEF` | `def` |
| `NOTFIXED` | `not_fixed` |

## Request key-value map

### nopurge

| Python value | MQSC key | MQSC value |
| --- | --- | --- |
| `yes` | `PURGE` | `NO` |

### noreplace

| Python value | MQSC key | MQSC value |
| --- | --- | --- |
| `yes` | `REPLACE` | `NO` |

### purge

| Python value | MQSC key | MQSC value |
| --- | --- | --- |
| `no` | `PURGE` | `NO` |
| `yes` | `PURGE` | `YES` |

### replace

| Python value | MQSC key | MQSC value |
| --- | --- | --- |
| `no` | `REPLACE` | `NO` |
| `yes` | `REPLACE` | `YES` |

---

*Auto-generated by `scripts/dev/generate_mapping_docs.py`.*
