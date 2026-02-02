# MQSC to PCF parameter extraction (first run)

## Table of Contents

- [Purpose](#purpose)
- [Scope and constraints](#scope-and-constraints)
- [Sources](#sources)
- [Summary](#summary)
- [Qualifier mappings](#qualifier-mappings)
- [Notes and gaps](#notes-and-gaps)

## Purpose

Provide a first-pass extraction of MQSC command parameters, PCF request/response parameters, and heuristic mappings across the full MQSC command set.

## Scope and constraints

- MQSC commands are sourced from the IBM MQSC command index and include commands beyond the V1 scope.
- PCF-only commands are ignored; the extraction starts from MQSC names and uses PCF only for attribute names/types.
- Parameter classification is heuristic and prioritized for breadth over precision in this run.

## Sources

- MQSC commands index: <https://www.ibm.com/docs/en/ibm-mq/9.4.x?topic=reference-mqsc-commands>
- PCF commands index: <https://www.ibm.com/docs/en/ibm-mq/9.4.x?topic=reference-definitions-programmable-command-formats>
- IBM Docs content API: <https://www.ibm.com/docs/api/v1/content>

## Summary

- MQSC commands parsed: 139
- MQSC docs fetched: 139
- MQSC commands with input parameters: 53
- MQSC commands with output parameters: 42
- PCF commands referenced: 132
- PCF request pages fetched: 106
- PCF response topics found: 67
- PCF response pages fetched: 67
- PCF response pages missing: 65
- PCF response pages fetch failed: 0

## Qualifier mappings

Mappings are split into one file per qualifier to keep each file renderable. Use the links below.

- [Apstatus](mqsc-pcf-parameter-extraction/apstatus.md)
- [Archive](mqsc-pcf-parameter-extraction/archive.md)
- [Authinfo](mqsc-pcf-parameter-extraction/authinfo.md)
- [Authrec](mqsc-pcf-parameter-extraction/authrec.md)
- [Authserv](mqsc-pcf-parameter-extraction/authserv.md)
- [Bsds](mqsc-pcf-parameter-extraction/bsds.md)
- [Buffpool](mqsc-pcf-parameter-extraction/buffpool.md)
- [Cfstatus](mqsc-pcf-parameter-extraction/cfstatus.md)
- [Cfstruct](mqsc-pcf-parameter-extraction/cfstruct.md)
- [Channel](mqsc-pcf-parameter-extraction/channel.md)
- [Chinit](mqsc-pcf-parameter-extraction/chinit.md)
- [Chlauth](mqsc-pcf-parameter-extraction/chlauth.md)
- [Clusqmgr](mqsc-pcf-parameter-extraction/clusqmgr.md)
- [Cluster](mqsc-pcf-parameter-extraction/cluster.md)
- [Cmdserv](mqsc-pcf-parameter-extraction/cmdserv.md)
- [Comminfo](mqsc-pcf-parameter-extraction/comminfo.md)
- [Conn](mqsc-pcf-parameter-extraction/conn.md)
- [Entauth](mqsc-pcf-parameter-extraction/entauth.md)
- [Group](mqsc-pcf-parameter-extraction/group.md)
- [Indoubt](mqsc-pcf-parameter-extraction/indoubt.md)
- [Listener](mqsc-pcf-parameter-extraction/listener.md)
- [Log](mqsc-pcf-parameter-extraction/log.md)
- [Maxsmsgs](mqsc-pcf-parameter-extraction/maxsmsgs.md)
- [Namelist](mqsc-pcf-parameter-extraction/namelist.md)
- [Policy](mqsc-pcf-parameter-extraction/policy.md)
- [Process](mqsc-pcf-parameter-extraction/process.md)
- [Psid](mqsc-pcf-parameter-extraction/psid.md)
- [Pubsub](mqsc-pcf-parameter-extraction/pubsub.md)
- [QMGR](mqsc-pcf-parameter-extraction/qmgr.md)
- [Queue](mqsc-pcf-parameter-extraction/queue.md)
- [Security](mqsc-pcf-parameter-extraction/security.md)
- [Service](mqsc-pcf-parameter-extraction/service.md)
- [Smds](mqsc-pcf-parameter-extraction/smds.md)
- [Smdsconn](mqsc-pcf-parameter-extraction/smdsconn.md)
- [Stgclass](mqsc-pcf-parameter-extraction/stgclass.md)
- [Subscription](mqsc-pcf-parameter-extraction/subscription.md)
- [System](mqsc-pcf-parameter-extraction/system.md)
- [Tcluster](mqsc-pcf-parameter-extraction/tcluster.md)
- [Thread](mqsc-pcf-parameter-extraction/thread.md)
- [Topic](mqsc-pcf-parameter-extraction/topic.md)
- [Tpipe](mqsc-pcf-parameter-extraction/tpipe.md)
- [Tpstatus](mqsc-pcf-parameter-extraction/tpstatus.md)
- [Trace](mqsc-pcf-parameter-extraction/trace.md)
- [Usage](mqsc-pcf-parameter-extraction/usage.md)

## Notes and gaps

- Display commands mix filter keywords and attributes; parameter descriptions are treated as input filters and requested parameters as outputs when possible.
- MQSC parameter types are not extracted; only PCF parameter types are captured and type hints are inferred from the PCF C-structure names.
- PCF enums are captured when listed as constants under a typed attribute; these need review for completeness.
- Response pages are discovered via IBM Docs index/search and may be missing or misclassified for some commands.
- Section parsing ignores syntax diagram content outside requested-parameter sections, which means parameters only documented in other diagrams may be missing.
- Mapping suggestions are name-based heuristics and will need refinement for conflicts and mixed-type responses.
