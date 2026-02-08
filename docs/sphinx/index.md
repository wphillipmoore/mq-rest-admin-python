# pymqrest

Python wrapper for the IBM MQ administrative REST API.

`pymqrest` provides a Python-friendly interface to IBM MQ queue manager
administration via the `runCommandJSON` REST endpoint. It translates between
Python `snake_case` attribute names and native MQSC parameter names, wraps
every MQSC command as a typed method, and handles authentication, CSRF tokens,
and error propagation.

```{toctree}
:maxdepth: 2
:caption: User Guide

getting-started
architecture
mapping-pipeline
ai-engineering
```

```{toctree}
:maxdepth: 2
:caption: API Reference

api/index
```

```{toctree}
:maxdepth: 2
:caption: Qualifier Mappings

mappings/index
```

```{toctree}
:maxdepth: 2
:caption: Design

design/index
```

```{toctree}
:maxdepth: 2
:caption: Development

development/index
```
