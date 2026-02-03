# MQSC and PCF mapping extraction rules

This document defines how to gather and analyze IBM MQ MQSC and PCF documentation to produce attribute and value mappings for the wrapper.

## Table of Contents

- [Purpose](#purpose)
- [Inputs](#inputs)
- [Output format](#output-format)
- [Extraction process](#extraction-process)
- [Type extraction](#type-extraction)
- [Command equivalence](#command-equivalence)
- [Parameter extraction and mapping](#parameter-extraction-and-mapping)
- [Validation and iteration](#validation-and-iteration)
- [Edge cases](#edge-cases)

## Purpose

Create a repeatable process that converts IBM MQ documentation into consistent mapping tables between MQSC attributes, PCF attributes, and snake_case names. This process depends on the command metadata extraction baseline described in `docs/command-metadata-extraction.md`.

## Inputs

- MQSC command reference pages for the target command.
- PCF command format and response pages for the equivalent command.
- A list of supported qualifiers and command families (queues, channels, queue manager).

## Output format

Mappings are recorded in a simple schema with three names per attribute and optional value mappings.

```yaml
version: 1
commands:
  - mqsc: <MQSC_COMMAND>
    pcf: <MQCMD_COMMAND>
    qualifier: <qualifier>
    status: <confirmed|provisional|no-equivalent>
    notes: <string>
qualifiers:
  <qualifier>:
    attributes:
      - mqsc: <MQSC_ATTRIBUTE>
        pcf: <PCFAttributeName>
        snake: <snake_case_name>
        type: <python_type>
        pcf_type: <pcf_type>
        values:
          <MQSC_VALUE>: <snake_case_value>
```

Rules:

- Command mappings record MQSC -> PCF equivalence; `no-equivalent` means MQSC has no PCF match.
- `mqsc` is the MQSC attribute token, in its canonical uppercase form.
- `pcf` matches the PCF attribute name from IBM docs.
- `snake` is the external name derived from `pcf`.
- `type` is the target Python type derived from `pcf_type`.
- `pcf_type` is the PCF C-structure type from IBM docs.
- `values` is optional; include only when MQSC uses symbolic tokens.

## Extraction process

1. Build the command metadata baseline for MQSC and PCF (see `docs/command-metadata-extraction.md`).
2. Identify the MQSC command and the PCF command that represent the same operation.
3. Extract MQSC attribute names and their allowed values from the MQSC command page.
4. Extract PCF attribute names from both the command format and response pages.
5. Pair attributes by meaning, not by spelling, using IBM’s wording and examples as the tie-breaker.
6. Convert PCF attribute names to snake_case for external use.
7. Map MQSC attribute values to snake_case when values are symbolic tokens; keep numeric values as-is.
8. Assign mappings at the qualifier level by default; add command-specific overrides only when necessary.
9. Record any ambiguity in a separate notes log and mark the mapping as provisional.

## Type extraction

Types are sourced from PCF command format and response pages. MQSC documentation is used only as a secondary reference when PCF does not define a type.

Type mapping rules:

- PCF `MQCFST` or string-valued fields -> `str`.
- PCF `MQCFIN`/`MQCFIN64` numeric fields -> `int`.
- PCF list or array fields -> `list[str]` or `list[int]` based on element type.
- PCF boolean-style flags -> `bool` only when the docs define a true/false semantic; otherwise keep `int`.
- Ignore enumerated constants and section labels; only parameters with explicit `MQCF*` types are treated as typed attributes.
- Enumerated constants listed under a typed parameter should be captured as candidate values for that parameter.

When MQSC documents numeric values with symbolic tokens:

- Use `int` as the type and add a `values` mapping for the symbolic tokens.
- If both numeric and string values are allowed by the API, treat the type as `str | int` and note it as provisional.

## Command equivalence

Start by mapping MQSC commands to their PCF equivalents and record missing mappings on either side.

Rules:

- Use the MQSC command reference as the source of the MQSC command list.
- Use the PCF command definitions as the source of the PCF list.
- Match commands by intended operation and object type, not by wording alone.
- When an MQSC command has no PCF equivalent, set `status: no-equivalent` and document why.
- PCF-only commands are out of scope because the wrapper only uses the MQSC command namespace; note them only if they clarify naming or mapping decisions.

## Parameter extraction and mapping

For each confirmed MQSC <-> PCF command pair, extract both request and response parameters, then map them.

Steps:

1. MQSC inputs: list all MQSC keyword parameters and allowed values for the command.
2. MQSC outputs: list response attributes returned by the MQSC display or inquiry.
3. PCF request: list PCF input parameters from the command format page (exclude response pages).
4. PCF response: list PCF output parameters from the response page (explicit "Response" topic).
5. Map MQSC inputs to PCF request parameters and MQSC outputs to PCF response parameters.
6. Record conflicts, ambiguities, and mixed-type responses in notes.
7. Keep separate entries for input-only and response-only attributes when they differ.
8. For `DISPLAY` commands, treat "Parameter descriptions" as input filters and "Requested parameters" (including syntax diagrams and requested-parameter tables) as output attributes.
9. Normalize MQSC abbreviations when matching to PCF (for example: `INT` -> `INTERVAL`, `HB` -> `HEARTBEAT`, `LIM` -> `LIMIT`, `SZ` -> `SIZE`).

## Validation and iteration

- Validate mappings against real command responses during integration tests.
- Replace provisional mappings with confirmed ones as soon as empirical data is available.
- Treat response payloads as the source of truth when docs and behavior diverge.

## Edge cases

- One MQSC attribute maps to multiple PCF attributes: document the split and use a command-specific override.
- Value tokens that collide or alias: prefer IBM’s current terminology and note deprecated forms.
- Attributes present in responses but not in command input: include them in mappings with a response-only note.
- Attributes that vary by platform or MQ version: record the version constraint in the notes log and keep the mapping conservative.
