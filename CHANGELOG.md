# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/)
and this project adheres to [Semantic Versioning](https://semver.org/).

## [1.0.1] - 2026-02-10

### Bug fixes

- resolve bare branch names to origin/ in commit-messages.sh (#159)
- use full version in release branch name to avoid collisions (#161)
- allow commits on release/* branches in pre-commit hook (#162)

### Features

- auto-bump patch version after publish, bump to 1.0.1 (#147)
- add changelog with git-cliff and CI validation gate (#149)
- add prepare_release.py to automate release preparation (#160)

## [1.0.0] - 2026-02-10

### Documentation

- rewrite README, fix sphinx markdown lint, close lint coverage gap (#145)

### Features

- bump version to 1.0.0, promote status from experimental to beta (#144)

## [0.1.0] - 2026-02-10

### Bug fixes

- prevent docs-only merge-base failures
- make docs-only detection merge-base independent
- satisfy ruff checks for metadata refresh script
- update include directives
- harden response parameter mapping
- standardize shared MQSC attribute mappings
- standardize additional shared attributes
- standardize CFSTRUCT and CLWL mappings
- correct ClusterWorkloadRank mapping
- standardize DESCR mapping
- enforce per-qualifier unique mappings
- normalize client/message/user mappings
- standardize identifiers and LIKE mapping
- normalize QMgr and Like mappings
- normalize Like and QMgr identifiers
- clean stgclass Like override
- normalize SSLPEER and cfstatus recovery mappings
- normalize cfstatus recovery fields
- normalize CLWL PCF names (issue #88)
- expand Msg to Message in PCF overrides (issue #87)
- normalize Identifier to Id (issue #86)
- normalize CFStructType override (issue #82)
- remove name parameter from QMGR and CMDSERV command methods (#100)
- omit responseParameters from non-DISPLAY commands to prevent silent failures (#125)
- configure git identity for annotated tag creation in publish workflow (#143)

### Documentation

- align repo docs with standards (#12)
- align standards entrypoint with repo type
- adopt standards include bootstrap
- align standards includes
- require uv run for python commands
- archive first-pass docs and capture mqsc list (#70)
- regroup conflicts report
- note codex command policy workaround
- add CLAUDE.md for Claude Code integration (#96)
- document standards compliance gates implementation (#99)
- add Sphinx documentation tree with mapping reference and API docs (#30) (#105)
- rework API reference pages for readability (#108)
- enrich docstrings for session, mapping, and exception modules (#111)
- add docstrings to all MQSC command wrapper methods (#109) (#116)
- fix autodoc rendering by wrapping directives in eval-rst blocks (#117)
- credit both Claude Code and Codex in AI engineering page (#118)
- separate unmapped qualifiers in mapping index, rewrite auth docs (#135)
- remove misleading "yet" from unmapped qualifier description (#137)
- clarify mapping data is bootstrapped from 9.4 docs, now authoritative in source (#141)

### Features

- add mq container tooling and refresh mqsc output metadata
- add MQ REST session framework
- switch session transport to requests
- add more MQSC helper methods
- expand MQSC command wrappers
- add MQSC qualifier placeholders
- support request key/value mappings
- document response parameter macros (issue #84)
- enable strict attribute mapping by default (#98)
- add WHERE filter support for DISPLAY commands (#101)
- flatten nested objects in command response parameters (#103)
- add practical example scripts with multi-QM Docker environment (#104) (#119)
- add idempotent ensure methods for declarative object management (#75) (#121)
- add ensure_qmgr for idempotent queue manager attribute management (#123)
- add LTPA token and mTLS client certificate authentication (#131)
- add PyPI publication infrastructure (#142)

### Refactoring

- remove explicit channel_type arg
- move mq rest exceptions to module
- move MQSC command methods to commands module
- rename _build_response_parameter_map to _build_snake_to_mqsc_map (#102)
- expand opaque MQSC shorthands to descriptive snake_case names (#126)
- expand abbreviated snake_case attribute names to descriptive forms (#127)
- expand remaining abbreviated snake_case attribute names (#128)
- expand abbreviated snake_case attribute names (batch 4) (#132)
- use snake_case attribute names exclusively in examples (#133)
- require credentials keyword argument, drop username/password (#134)
- make perform_ltpa_login internal, remove from public docs (#136)
- archive extraction pipeline, use MAPPING_DATA as sole source of truth (#140)

### Testing

- cover MQREST session helpers
- expand integration display coverage
- generalize integration display and mutating coverage
- run integration lifecycle against local mq
