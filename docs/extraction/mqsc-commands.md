# MQSC command list extraction (issue #64)

## Source

- IBM MQSC commands reference index: <https://www.ibm.com/docs/en/ibm-mq/9.4.x?topic=reference-mqsc-commands>

## Extraction notes

- Generated at (UTC): 2026-02-03T15:21:18Z
- Raw command entries detected: 145
- Unique command names recorded: 133
- Commands are normalized by taking the text before the first "(" in the index entry.
- Platform-specific and MQTT duplicates are collapsed to a single command name in the YAML list.
- Generic queue-family entries (ALTER/DEFINE/DELETE queues) are omitted and will be expanded in issue #65.

## Duplicate entries collapsed

- DISPLAY CHSTATUS: 3 entries
- ALTER CHANNEL: 2 entries
- DEFINE CHANNEL: 2 entries
- DELETE CHANNEL: 2 entries
- DISPLAY CHANNEL: 2 entries
- SET LOG: 2 entries
- START CHANNEL: 2 entries
- STOP CHANNEL: 2 entries

## Output artifact

- `docs/extraction/mqsc-commands.yaml`
