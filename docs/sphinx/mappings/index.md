# Qualifier Mapping Reference

Each page below documents the attribute mappings for one MQSC qualifier.
These mappings translate between Python-friendly `snake_case` names and
MQSC parameter names used by the IBM MQ REST API.

```{toctree}
:maxdepth: 1

apstatus
archive
authinfo
authrec
authserv
cfstatus
cfstruct
channel
chinit
chlauth
chstatus
clusqmgr
cluster
comminfo
conn
entauth
group
indoubt
listener
log
lsstatus
namelist
policy
process
pubsub
qmgr
queue
sbstatus
security
service
smds
smdsconn
stgclass
sub
svstatus
topic
topicstr
tpstatus
usage
```

## Qualifiers without attribute mappings

The following qualifiers are supported by pymqrest but do not have attribute name translations: `bsds`, `buffpool`, `cmdserv`, `maxsmsgs`, `psid`, `tcluster`, `thread`, `tpipe`, `trace`.

```{toctree}
:hidden:

bsds
buffpool
cmdserv
maxsmsgs
psid
tcluster
thread
tpipe
trace
```
