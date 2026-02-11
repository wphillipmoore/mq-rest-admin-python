# pymqrest 1.0.0 announcement

General-purpose announcement for pymqrest 1.0.0 GA. Adapt tone and
length per channel; the core message stays the same.

---

## Short version (Reddit, Hacker News, forum posts)

**pymqrest: a Python wrapper for the IBM MQ administrative REST API**

I'm sharing pymqrest, a new Python library for administering IBM MQ
queue managers through the REST API.

If you manage MQ infrastructure, you've probably scripted against
`runmqsc` or reached for pymqi. pymqrest takes a different approach: it
wraps the `runCommandJSON` REST endpoint that ships with MQ 9.4, so
there's no C client library to install, no platform-specific binaries,
and nothing to compile. You get a Python session object with typed
methods for every MQSC command, automatic `snake_case` attribute
mapping, and idempotent `ensure_*` methods for declarative object
management.

```python
from pymqrest import MQRESTSession, LTPAAuth

session = MQRESTSession(
    rest_base_url="https://mq-host:9443/ibmmq/rest/v2",
    qmgr_name="QM1",
    credentials=LTPAAuth("admin", "admin"),
)

# List local queues with Pythonic attribute names
for q in session.display_qlocal(name="*"):
    print(q["queue_name"], q.get("current_queue_depth", 0))

# Declarative upsert: define, alter, or no-op as needed
result = session.ensure_qlocal(
    name="APP.REQUESTS",
    request_parameters={"max_queue_depth": "50000"},
)
print(result.action)  # EnsureAction.CREATED, UPDATED, or UNCHANGED
```

Highlights:

- **130+ generated command methods** covering the full MQSC verb set
  (DISPLAY, DEFINE, ALTER, DELETE, START, STOP, CLEAR, and more)
- **Automatic attribute mapping** between terse MQSC tokens
  (`CURDEPTH`, `DEFPSIST`) and readable `snake_case` names
  (`current_queue_depth`, `default_persistence`)
- **Idempotent ensure methods** for 16 object types: define if missing,
  alter only what changed, skip when already correct
- **No native dependencies** &mdash; pure Python over HTTPS, works
  anywhere `requests` runs
- **Three auth modes**: mutual TLS client certificates, LTPA token,
  and HTTP Basic
- **100% test coverage**, strict mypy + ty typing, all ruff rules
  enabled

Some personal context: I maintained the Perl5 MQSeries module on CPAN
years ago, and this project picks up a thread I left a long time ago.
pymqrest is my first open-source release in over 15 years, and it felt
good to get back to it.

The full backstory is on my blog: [Building pymqrest](https://the-infrastructure-mindset.ghost.io/building-pymqrest-ai-production-library/)

- **PyPI**: https://pypi.org/project/pymqrest/
- **GitHub**: https://github.com/wphillipmoore/pymqrest
- **Docs**: https://wphillipmoore.github.io/pymqrest/

Feedback, issues, and contributions are welcome. The project is marked
beta since this is the first release, but the API surface and mapping
tables are stable. Any breaking changes to the mappings would be part of
a new major version.

---

## Medium version (LinkedIn, IBM community, mailing lists)

**Announcing pymqrest: a Python wrapper for the IBM MQ administrative
REST API**

I'm pleased to announce the general availability of pymqrest, a Python
library that wraps the IBM MQ administrative REST API.

### What it does

pymqrest provides typed Python methods for every MQSC command exposed by
the MQ 9.4 `runCommandJSON` endpoint. It automatically translates
between the terse MQSC attribute tokens you know from `runmqsc`
(`CURDEPTH`, `MAXDEPTH`, `DEFPSIST`) and readable Python `snake_case`
names (`current_queue_depth`, `max_queue_depth`,
`default_persistence`). The translation is bidirectional &mdash;
request parameters are converted on the way in, response attributes on
the way out.

### Why another MQ library?

The existing Python MQ libraries (pymqi, ibmmq) bind to the C client
libraries via native extensions. That works well but ties you to
platform-specific binaries and a particular client installation. pymqrest
takes a fundamentally different approach: it talks to MQ entirely over
HTTPS using the administrative REST API, with no native dependencies
beyond the `requests` library. If you can reach the mqweb console, you
can use pymqrest.

This doesn't replace pymqi for application-level messaging (put/get).
pymqrest is specifically for administration: querying, defining,
altering, and deleting MQ objects programmatically.

### Key features

- **130+ command methods**: DISPLAY, DEFINE, ALTER, DELETE, START, STOP,
  CLEAR, PING, RESET, RESOLVE, and more
- **Attribute mapping pipeline**: automatic `snake_case` translation
  with opt-out at session or per-call level
- **Idempotent ensure methods**: declarative upsert for 16 object types
  (queues, channels, topics, listeners, and more) &mdash; define if
  missing, alter only changed attributes, no-op when already correct
- **Flexible authentication**: mutual TLS client certificates, LTPA
  token login, and HTTP Basic
- **Diagnostic state**: session retains last command/response payloads
  and HTTP status for inspection
- **Strict quality bar**: 100% branch coverage, strict mypy + ty
  typing, full ruff ruleset

### A bit of history

Some of you may remember the Perl5 MQSeries module on CPAN. I
maintained that library years ago, and pymqrest picks up a thread I left
a long time ago &mdash; a Pythonic approach to MQ administration tooling
that builds on ideas from over 25 years of working with this platform.
This is my first open-source release in over 15 years, and it's been a
rewarding experience getting back to it.

For the full backstory, see: [Building pymqrest](https://the-infrastructure-mindset.ghost.io/building-pymqrest-ai-production-library/)

### Links

- **Install**: `pip install pymqrest`
- **PyPI**: https://pypi.org/project/pymqrest/
- **GitHub**: https://github.com/wphillipmoore/pymqrest
- **Documentation**: https://wphillipmoore.github.io/pymqrest/

pymqrest is in beta as a first release, but the API surface and mapping
tables are stable. Any breaking changes to the mappings would land in a
new major version. Feedback, bug reports, and contributions are very
welcome.

---

## Micro version (Twitter/X, Mastodon, Bluesky)

pymqrest 1.0.0: a Python wrapper for the IBM MQ administrative REST
API. No C client required &mdash; pure Python over HTTPS. 130+ MQSC
command methods, automatic snake_case attribute mapping, idempotent
ensure methods. My first open-source release in 15+ years.

https://github.com/wphillipmoore/pymqrest

---

## Channel-specific notes

**Reddit** (r/Python, r/ibm, r/sysadmin): Use the short version. Reddit
audiences prefer concise, technically honest posts. Lead with what it
does, not marketing language. The "Show r/Python" format works well.

**Hacker News** (Show HN): Use the short version. Title format:
"Show HN: pymqrest &mdash; Python wrapper for IBM MQ admin REST API (no
C client needed)". Keep the submission text brief; HN readers will click
through to the repo.

**LinkedIn**: Use the medium version. Professional tone is appropriate
here, and the personal history angle resonates well on LinkedIn.

**IBM Community / MQ forums**: Use the medium version. This audience
knows MQ deeply, so the technical specifics about `runCommandJSON` and
the comparison with pymqi will land well.

**Python Discourse** (discuss.python.org): Use the short version under
the "Showcase" category.

**Perl community** (if crossposting): Mention the MQSeries CPAN
heritage directly. The Perl community will appreciate hearing about the
lineage.
