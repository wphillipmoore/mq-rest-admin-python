# Metadata collection milestone (2026-01-18)

## Table of Contents

- [Purpose](#purpose)
- [Scope](#scope)
- [Inputs](#inputs)
- [Process summary](#process-summary)
- [Results summary](#results-summary)
- [Outputs](#outputs)
- [Completion decision](#completion-decision)
- [Open gaps](#open-gaps)
- [Next work](#next-work)

## Purpose

Summarize the data collection work completed so far, document the process used, and mark the metadata set as complete for the first mapping milestone.

## Scope

- MQSC command inventory, command metadata, and parameter listings.
- PCF command inventory, request/response metadata, and parameter listings.
- MQSC to PCF command equivalence mapping.
- Heuristic parameter mappings collected per qualifier.

## Inputs

- IBM MQ documentation sources and content API endpoints are listed in the extraction docs.
- Extraction rules and constraints are captured in the mapping and metadata standards.

## Process summary

1. Build command inventories from the MQSC and PCF index pages.
2. Fetch per-command documentation and extract MQSC inputs, outputs, and positional tokens.
3. Fetch PCF command format and response topics and extract typed parameters.
4. Derive MQSC to PCF command equivalence and assign a qualifier per command family.
5. Run first-pass, name-based parameter mapping per qualifier and record ambiguities and gaps.

## Results summary

- MQSC command inventory: 139 commands parsed and fetched.
- MQSC metadata coverage: 133 commands with input parameters, 6 with output parameters.
- PCF command inventory: 105 commands parsed; 105 request pages fetched.
- PCF response coverage: 105 response pages fetched in the command metadata run; 67 response pages found in the parameter extraction run, 65 missing for mapping heuristics.
- Command equivalence mapping: 132 provisional mappings, 7 no-equivalent entries.
- Qualifier-specific parameter extraction: one file per qualifier with request/response parameters and mapping suggestions.

## Outputs

- Command metadata baseline: `docs/command-metadata-first-run.md`.
- MQSC to PCF command equivalence: `docs/mqsc-pcf-command-mapping.md`.
- Parameter extraction overview: `docs/mqsc-pcf-parameter-extraction-first-run.md`.
- Qualifier-specific parameter extractions: `docs/mqsc-pcf-parameter-extraction/`.
- Extraction and mapping rules: `docs/command-metadata-extraction.md`, `docs/mapping-extraction-rules.md`.

## Completion decision

As of January 18, 2026, the current metadata set is considered complete for the first mapping milestone. Further extraction or refresh work should be treated as a new milestone with its own summary and decision record.

## Open gaps

- Command mappings remain provisional until validated against live MQ responses.
- MQSC output parameters are sparse and can be incomplete where documentation relies on diagrams outside requested-parameter sections.
- PCF response coverage varies by command family; some response topics are missing or ambiguous.
- Attribute types are sourced only from PCF; MQSC parameter typing is not yet captured.

## Next work

- Define the minimal runtime mapping data structures and their derivation from the metadata set.
- Begin implementing mapping tables for MQSC <-> PCF attribute translation using the minimal dataset.
