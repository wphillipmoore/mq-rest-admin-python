# Command metadata extraction

## Table of Contents

- [Purpose](#purpose)
- [Inputs](#inputs)
- [Output format](#output-format)
- [MQSC extraction rules](#mqsc-extraction-rules)
- [PCF extraction rules](#pcf-extraction-rules)
- [Known gaps](#known-gaps)
- [Iteration checklist](#iteration-checklist)

## Purpose

Establish a repeatable, command-by-command metadata baseline for MQSC and PCF before attempting any cross-namespace mapping. The goal is to capture inputs and outputs per command from IBM documentation with minimal interpretation.

## Inputs

- MQSC command reference pages for each MQSC command.
- PCF command format pages for each PCF command.
- PCF response pages for each PCF command that documents response data.

## Output format

Capture MQSC and PCF command metadata separately to avoid mixing namespaces during extraction.

```yaml
version: 1
generated_at: <timestamp>
mqsc_commands:
  - name: <MQSC_COMMAND>
    href: <doc-path>
    positional_parameters: [<string>]
    parameters: [<MQSC_PARAM>]
    input_only: [<MQSC_PARAM>]
    output_only: [<MQSC_PARAM>]
    notes: [<string>]
pcf_commands:
  - name: <MQCMD_COMMAND>
    request_href: <doc-path>
    response_href: <doc-path|null>
    request_parameters:
      - name: <PCF_PARAM>
        pcf_type: <MQCF_TYPE>
        type_hint: <str|int|bytes|list>
        enum_values: [<MQ_CONSTANT>]
    response_parameters:
      - name: <PCF_PARAM>
        pcf_type: <MQCF_TYPE>
        type_hint: <str|int|bytes|list>
        enum_values: [<MQ_CONSTANT>]
    notes: [<string>]
```

## MQSC extraction rules

- Use the command’s own reference page as the source of truth.
- Input parameters:
  - Start from the “Parameter descriptions” section.
  - For `DISPLAY` commands, treat “Parameter descriptions” as input filters.
- Output parameters:
  - For `DISPLAY` commands, use the “Requested parameters” section.
  - Parse both the requested-parameter tables and any syntax diagram fragments that list output tokens.
  - For non-display commands, use “Returned parameters” or “Response parameters” sections when they exist.
- Positional parameters:
  - Capture positional tokens from syntax diagrams, including placeholders in parentheses.
- Parameters:
  - `parameters` is the union of the input and output parameter sets.
  - `input_only` and `output_only` are populated only when both input and output sets are available; otherwise record a note and leave them empty.
- Record any missing sections or ambiguous headings in notes.

## PCF extraction rules

- Request parameters:
  - Use the PCF command format page for the command.
  - Capture only parameters with explicit `MQCF*` types.
- Response parameters:
  - Use the command’s response page (explicit “Response” topic).
  - Capture only parameters with explicit `MQCF*` types.
- Enumerated constants:
  - Collect `MQ*` constants listed under a typed parameter as candidate values.

## Known gaps

- Some PCF commands do not publish a dedicated response page; record `response_href: null`.
- MQSC display output lists can be incomplete if output attributes are documented only in diagrams outside the “Requested parameters” section.
- MQSC parameter types are not captured at this stage.

## Iteration checklist

- Validate input and output lists for a representative set of commands (e.g., DISPLAY CHANNEL, DISPLAY QUEUE).
- Confirm PCF response pages for commands with known response data.
- Add extraction rules for any repeated doc patterns that are currently missed.
