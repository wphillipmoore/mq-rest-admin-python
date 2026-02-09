# queue

Attribute mapping reference for the `queue` qualifier.

Related MQSC commands: `CLEAR QLOCAL`, `DISPLAY QSTATUS`, `DISPLAY QUEUE`, `MOVE QLOCAL`, `RESET QSTATS`

## Request key map

| Python name | MQSC parameter |
| --- | --- |
| `authorization_record` | `AUTHREC` |
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
| `default_bind` | `DEFBIND` |
| `default_input_open_option` | `DEFSOPT` |
| `default_persistence` | `DEFPSIST` |
| `default_priority` | `DEFPRTY` |
| `default_put_response` | `DEFPRESP` |
| `default_read_ahead` | `DEFREADA` |
| `definition_type` | `DEFTYPE` |
| `description` | `DESCR` |
| `distribution_lists` | `DISTL` |
| `force` | `FORCE` |
| `harden_get_backout` | `HARDENBO` |
| `ignore_state` | `IGNSTATE` |
| `image_recover_queue` | `IMGRCOVQ` |
| `inhibit_get` | `GET` |
| `inhibit_put` | `PUT` |
| `initiation_queue_name` | `INITQ` |
| `like` | `LIKE` |
| `max_message_length` | `MAXMSGL` |
| `max_queue_depth` | `MAXDEPTH` |
| `max_queue_file_size` | `MAXFSIZE` |
| `message_delivery_sequence` | `MSGDLVSQ` |
| `non_persistent_message_class` | `NPMCLASS` |
| `page_set_id` | `PSID` |
| `process_name` | `PROCESS` |
| `property_control` | `PROPCTL` |
| `queue_accounting` | `ACCTQ` |
| `queue_depth_high_event` | `QDPHIEV` |
| `queue_depth_high_limit` | `QDEPTHHI` |
| `queue_depth_low_event` | `QDPLOEV` |
| `queue_depth_low_limit` | `QDEPTHLO` |
| `queue_depth_max_event` | `QDPMAXEV` |
| `queue_monitoring` | `MONQ` |
| `queue_service_interval` | `QSVCINT` |
| `queue_sharing_group_disposition` | `QSGDISP` |
| `queue_statistics` | `STATQ` |
| `remote_queue_manager_name` | `RQMNAME` |
| `remote_queue_name` | `RNAME` |
| `retention_interval` | `RETINTVL` |
| `scope` | `SCOPE` |
| `shareability` | `SHARE` |
| `storage_class` | `STGCLASS` |
| `stream_queue` | `STREAMQ` |
| `stream_queue_service` | `STRMQOS` |
| `target_type` | `TARGTYPE` |
| `to_queue_name` | `TOQLOCAL` |
| `transmission_queue_name` | `XMITQ` |
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
| `APPLDESC` | `application_desc` |
| `APPLTAG` | `application_tag` |
| `APPLTYPE` | `application_type` |
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
| `CLUSQMGR` | `cluster_queue_manager` |
| `CLUSQT` | `cluster_queue_type` |
| `CLUSTER` | `cluster_name` |
| `CLUSTIME` | `cluster_time` |
| `CLWLPRTY` | `cluster_workload_priority` |
| `CLWLRANK` | `cluster_workload_rank` |
| `CLWLUSEQ` | `cluster_workload_use_queue` |
| `CONNAME` | `connection_name` |
| `CRDATE` | `creation_date` |
| `CRTIME` | `creation_time` |
| `CURDEPTH` | `current_queue_depth` |
| `CURFSIZE` | `current_queue_file_size` |
| `CURMAXFS` | `current_max_queue_file_size` |
| `CUSTOM` | `custom` |
| `DEFBIND` | `default_bind` |
| `DEFPRESP` | `default_put_response` |
| `DEFPRTY` | `default_priority` |
| `DEFPSIST` | `default_persistence` |
| `DEFREADA` | `default_read_ahead` |
| `DEFSOPT` | `default_input_open_option` |
| `DEFTYPE` | `definition_type` |
| `DESCR` | `description` |
| `DISTL` | `distribution_lists` |
| `GET` | `inhibit_get` |
| `HARDENBO` | `harden_get_backout` |
| `HSTATE` | `handle_state` |
| `IMGRCOVQ` | `image_recover_queue` |
| `INDXTYPE` | `index_type` |
| `INITQ` | `initiation_queue_name` |
| `INQUIRE` | `open_inquire` |
| `IPPROCS` | `open_input_count` |
| `LGETDATE` | `last_get_date` |
| `LGETTIME` | `last_get_time` |
| `LPUTDATE` | `last_put_date` |
| `LPUTTIME` | `last_put_time` |
| `MAXDEPTH` | `max_queue_depth` |
| `MAXFSIZE` | `max_queue_file_size` |
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
| `PSBNAME` | `program_spec_block_name` |
| `PSID` | `page_set_id` |
| `PSTID` | `partition_spec_table_region_id` |
| `PUT` | `inhibit_put` |
| `QDEPTHHI` | `queue_depth_high_limit` |
| `QDEPTHLO` | `queue_depth_low_limit` |
| `QDPHIEV` | `queue_depth_high_event` |
| `QDPLOEV` | `queue_depth_low_event` |
| `QDPMAXEV` | `queue_depth_max_event` |
| `QMID` | `queue_manager_id` |
| `QMURID` | `queue_manager_unit_of_work_id` |
| `QSGDISP` | `queue_sharing_group_disposition` |
| `QSVCINT` | `queue_service_interval` |
| `QTIME` | `on_queue_time` |
| `QTYPE` | `queue_type` |
| `RETINTVL` | `retention_interval` |
| `RNAME` | `remote_queue_name` |
| `RQMNAME` | `remote_queue_manager_name` |
| `SCOPE` | `scope` |
| `SET` | `open_set` |
| `SHARE` | `shareability` |
| `STATQ` | `queue_statistics` |
| `STGCLASS` | `storage_class` |
| `STREAMQ` | `stream_queue` |
| `STRMQOS` | `stream_queue_service` |
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
| `URID` | `unit_of_work_id` |
| `URTYPE` | `unit_of_work_type` |
| `USAGE` | `usage` |
| `USERID` | `user_id` |
| `XMITQ` | `transmission_queue_name` |

## Request value map

### default_persistence

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
