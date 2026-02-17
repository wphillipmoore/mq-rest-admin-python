# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/)
and this project adheres to [Semantic Versioning](https://semver.org/).

## [1.1.7] - 2026-02-17

### Bug fixes

- sync prepare_release.py empty changelog abort from canonical (#307)

## [1.1.6] - 2026-02-17

### Bug fixes

- sync prepare_release.py ruff formatting from canonical (#298)

### Features

- use GitHub App token for bump PR to trigger CI (#300)

## [1.1.5] - 2026-02-16

### Bug fixes

- move SBOM generation after PyPI publish step (#284) (#287)
- sync prepare_release.py merge message fix from canonical (#291)
- sync prepare_release.py changelog conflict fix from canonical (#293)

### Styling

- fix ruff lint errors in prepare_release.py (#288)

## [1.1.4] - 2026-02-16

### Bug fixes

- remove extra blank line in CHANGELOG.md
- disable MD041 for mkdocs snippet-include files
- correct snippets base_path resolution for fragment includes (#267)
- run mike from repo root so snippet base_path resolves in CI (#268)
- remove PR_BUMP_TOKEN and add issue linkage to version bump PR
- rename integration-test job to integration-tests
- move SBOM generation after PyPI publish step (#284)
- sync prepare_release.py with canonical version (#286)

### Documentation

- migrate from Sphinx to MkDocs Material
- fix attribute names, stale auth claim, and bare pages (#251)
- address medium-severity documentation consistency findings (#253)
- address cross-library documentation consistency nits (#259)
- switch to shared fragment includes from common repo (#264)
- add quality gates documentation page
- remove Python-specific design choices and beta status from rationale
- update CLAUDE.md architecture section for current codebase (#276)

### Features

- add Tier 1 security tooling (CodeQL, attestations, license compliance)
- add Trivy and Semgrep CI jobs and SBOM generation

### Refactoring

- convert mapping data from Python module to JSON file (#274)

## [1.1.3] - 2026-02-15

### Bug fixes

- add missing MAPPING_DATA entries for integration test failures (#236)
- allow release/* commits in library-release branching model (#244)

### Documentation

- add nested object flattening design doc and queue status example (#240)

### Features

- adopt per-project MQ container isolation (#233)

## [1.1.2] - 2026-02-13

### Bug fixes

- use PR_BUMP_TOKEN for version bump PR creation (#219)
- prevent release-gates skipped status from blocking auto-merge (#223)

## [1.1.1] - 2026-02-13

### Documentation

- add developer setup and contributing guides to Sphinx docs (#215)

### Features

- migrate MQ dev environment to shared mq-dev-environment repo (#214)

## [1.1.0] - 2026-02-12

### Bug fixes

- use PAT and merge strategy for version bump PR (#190)
- skip pre-conventional commits in commit-messages lint
- disable CONNAUTH/CHLAUTH and fix seed idempotency for gateway routing (#200)
- remove unused provisional status labels from MAPPING_DATA (#202)

### Documentation

- correct platform availability claim in gateway docs (#203)
- fix sync-methods examples to use realistic object types (#207)

### Features

- add qmstatus and qstatus qualifier mappings (#192)
- add mapping_overrides parameter to MQRESTSession (#194)
- add gateway_qmgr parameter to MQRESTSession (#197)
- add MappingOverrideMode.REPLACE for complete mapping replacement (#205)
- add synchronous start/stop/restart wrappers for channels, listeners, and services (#206)

## [1.0.3] - 2026-02-11

### Bug fixes

- merge main back into develop in version bump PR (#186)

## [1.0.2] - 2026-02-11

### Bug fixes

- use regular merge for release PRs and refresh deps in version bump (#172)

### Documentation

- add pymqrest 1.0.0 GA announcement draft (#176)
- use LTPAAuth as default in examples and docs (#181)

### Features

- add Python 3.12 and 3.13 support (#180)
- include changed attributes in EnsureResult (#178) (#182)

## [1.0.1] - 2026-02-10

### Bug fixes

- resolve bare branch names to origin/ in commit-messages.sh (#159)
- use full version in release branch name to avoid collisions (#161)
- allow commits on release/* branches in pre-commit hook (#162)
- merge main into release branch to reconcile squash-merge history (#164)
- use conventional commit message for release merge commit (#165)
- create release branch from main to avoid history pollution (#167)
- generate changelog on develop before creating release branch (#169)

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
