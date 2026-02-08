# channel

Attribute mapping reference for the `channel` qualifier.

Related MQSC commands: `ALTER CHANNEL`, `DEFINE CHANNEL`, `DELETE CHANNEL`, `DISPLAY CHANNEL`, `PING CHANNEL`, `PURGE CHANNEL`, `RESET CHANNEL`, `RESOLVE CHANNEL`, `START CHANNEL`, `STOP CHANNEL`

## Request key map

| Python name | MQSC parameter |
| --- | --- |
| `amqp_keep_alive` | `AMQPKA` |
| `backlog` | `BACKLOG` |
| `batch_data_limit` | `BATCHLIM` |
| `batch_heartbeat` | `BATCHHB` |
| `batch_interval` | `BATCHINT` |
| `batch_size` | `BATCHSZ` |
| `certificate_label` | `CERTLABL` |
| `channel_disposition` | `CHLDISP` |
| `channel_monitoring` | `MONCHL` |
| `channel_statistics` | `STATCHL` |
| `channel_status` | `STATUS` |
| `channel_table` | `CHLTABLE` |
| `channel_type` | `CHLTYPE` |
| `client_channel_weight` | `CLNTWGHT` |
| `client_id` | `CLIENTID` |
| `cluster_name` | `CLUSTER` |
| `cluster_namelist` | `CLUSNL` |
| `cluster_workload_channel_weight` | `CLWLWGHT` |
| `cluster_workload_priority` | `CLWLPRTY` |
| `cluster_workload_rank` | `CLWLRANK` |
| `command_scope` | `CMDSCOPE` |
| `connection_affinity` | `AFFINITY` |
| `connection_name` | `CONNAME` |
| `data_conversion` | `CONVERT` |
| `data_count` | `DATALEN` |
| `def_reconnect` | `DEFRECON` |
| `default_channel_disposition` | `DEFCDISP` |
| `description` | `DESCR` |
| `disc_interval` | `DISCINT` |
| `header_compression` | `COMPHDR` |
| `heartbeat_interval` | `HBINT` |
| `ignore_state` | `IGNSTATE` |
| `in_doubt` | `ACTION` |
| `jaas_config` | `JAASCFG` |
| `keep_alive_interval` | `KAINT` |
| `like` | `LIKE` |
| `local_address` | `LOCLADDR` |
| `long_retry_count` | `LONGRTY` |
| `long_retry_interval` | `LONGTMR` |
| `max_instances` | `MAXINST` |
| `max_instances_per_client` | `MAXINSTC` |
| `max_message_length` | `MAXMSGL` |
| `mca_name` | `MCANAME` |
| `mca_type` | `MCATYPE` |
| `mca_user` | `MCAUSER` |
| `message_compression` | `COMPMSG` |
| `message_exit` | `MSGEXIT` |
| `message_retry_count` | `MRRTY` |
| `message_retry_exit` | `MREXIT` |
| `message_retry_interval` | `MRTMR` |
| `message_retry_user_data` | `MRDATA` |
| `message_seq_number` | `SEQNUM` |
| `message_user_data` | `MSGDATA` |
| `mode` | `MODE` |
| `mode_name` | `MODENAME` |
| `network_priority` | `NETPRTY` |
| `non_persistent_message_speed` | `NPMSPEED` |
| `password` | `PASSWORD` |
| `port` | `PORT` |
| `property_control` | `PROPCTL` |
| `protocol` | `PROTOCOL` |
| `put_authority` | `PUTAUT` |
| `q_mgr_name` | `QMNAME` |
| `qsg_disposition` | `QSGDISP` |
| `receive_exit` | `RCVEXIT` |
| `receive_user_data` | `RCVDATA` |
| `security_exit` | `SCYEXIT` |
| `security_user_data` | `SCYDATA` |
| `send_exit` | `SENDEXIT` |
| `send_user_data` | `SENDDATA` |
| `seq_number_wrap` | `SEQWRAP` |
| `sharing_conversations` | `SHARECNV` |
| `short_retry_count` | `SHORTRTY` |
| `short_retry_interval` | `SHORTTMR` |
| `spl_protection` | `SPLPROT` |
| `ssl_cipher_spec` | `SSLCIPH` |
| `ssl_client_auth` | `SSLCAUTH` |
| `ssl_key_repository` | `SSLKEYR` |
| `ssl_pass_phrase` | `SSLKEYP` |
| `ssl_peer_name` | `SSLPEER` |
| `temporary_model_q_name` | `TMPMODEL` |
| `temporary_q_prefix` | `TMPQPRFX` |
| `topic_root` | `TPROOT` |
| `tp_name` | `TPNAME` |
| `transmission_q_name` | `XMITQ` |
| `transport_type` | `TRPTYPE` |
| `use_clt_id` | `USECLTID` |
| `use_dlq` | `USEDLQ` |
| `user_id` | `USERID` |

## Response key map

| MQSC parameter | Python name |
| --- | --- |
| `AFFINITY` | `connection_affinity` |
| `ALTDATE` | `alteration_date` |
| `ALTTIME` | `alteration_time` |
| `AMQPKA` | `amqp_keep_alive` |
| `AUTOSTART` | `auto_start` |
| `BATCHHB` | `batch_heartbeat` |
| `BATCHINT` | `batch_interval` |
| `BATCHLIM` | `batch_data_limit` |
| `BATCHSZ` | `batch_size` |
| `CERTLABL` | `certificate_label` |
| `CHLTYPE` | `channel_type` |
| `CLNTWGHT` | `client_channel_weight` |
| `CLUSNL` | `cluster_namelist` |
| `CLUSTER` | `cluster_name` |
| `CLWLPRTY` | `cluster_workload_priority` |
| `CLWLRANK` | `cluster_workload_rank` |
| `CLWLWGHT` | `cluster_workload_channel_weight` |
| `COMPHDR` | `header_compression` |
| `COMPMSG` | `message_compression` |
| `CONNAME` | `connection_name` |
| `CONVERT` | `data_conversion` |
| `DEFCDISP` | `default_channel_disposition` |
| `DESCR` | `description` |
| `DISCINT` | `disc_interval` |
| `HBINT` | `heartbeat_interval` |
| `KAINT` | `keep_alive_interval` |
| `LOCLADDR` | `local_address` |
| `LONGRTY` | `long_retry_count` |
| `LONGTMR` | `long_retry_interval` |
| `MAXINST` | `max_instances` |
| `MAXINSTC` | `max_instances_per_client` |
| `MAXMSGL` | `max_message_length` |
| `MCANAME` | `mca_name` |
| `MCATYPE` | `mca_type` |
| `MCAUSER` | `mca_user` |
| `MODENAME` | `mode_name` |
| `MONCHL` | `channel_monitoring` |
| `MRDATA` | `message_retry_user_data` |
| `MREXIT` | `message_retry_exit` |
| `MRRTY` | `message_retry_count` |
| `MRTMR` | `message_retry_interval` |
| `MSGDATA` | `message_user_data` |
| `MSGEXIT` | `message_exit` |
| `NETPRTY` | `network_priority` |
| `NPMSPEED` | `non_persistent_message_speed` |
| `PASSWORD` | `password` |
| `PORT` | `port` |
| `PROPCTL` | `property_control` |
| `PUTAUT` | `put_authority` |
| `QMNAME` | `q_mgr_name` |
| `RCVDATA` | `receive_user_data` |
| `RCVEXIT` | `receive_exit` |
| `RESETSEQ` | `reset_seq` |
| `SCYDATA` | `security_user_data` |
| `SCYEXIT` | `security_exit` |
| `SENDDATA` | `send_user_data` |
| `SENDEXIT` | `send_exit` |
| `SEQWRAP` | `seq_number_wrap` |
| `SHARECNV` | `sharing_conversations` |
| `SHORTRTY` | `short_retry_count` |
| `SHORTTMR` | `short_retry_interval` |
| `SPLPROT` | `spl_protection` |
| `SSLCAUTH` | `ssl_client_auth` |
| `SSLCIPH` | `ssl_cipher_spec` |
| `SSLPEER` | `ssl_peer_name` |
| `STATCHL` | `channel_statistics` |
| `TPNAME` | `tp_name` |
| `TPROOT` | `topic_root` |
| `TRPTYPE` | `transport_type` |
| `USECLTID` | `use_clt_id` |
| `USEDLQ` | `use_dlq` |
| `USERID` | `user_id` |
| `XMITQ` | `transmission_q_name` |

## Request key-value map

### channel_instance_type

| Python value | MQSC key | MQSC value |
| --- | --- | --- |
| `current` | `CURRENT` | `YES` |
| `saved` | `SAVED` | `YES` |
| `short` | `SHORT` | `YES` |

### noreplace

| Python value | MQSC key | MQSC value |
| --- | --- | --- |
| `yes` | `REPLACE` | `NO` |

### replace

| Python value | MQSC key | MQSC value |
| --- | --- | --- |
| `no` | `REPLACE` | `NO` |
| `yes` | `REPLACE` | `YES` |

---

*Auto-generated by `scripts/dev/generate_mapping_docs.py`.*
