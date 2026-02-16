# Namespace origin

## How the `snake_case` namespace was created

The `snake_case` attribute namespace in `mapping_data.py` was initialized
by parsing IBM MQ 9.4 MQSC and PCF documentation using an automated
extraction pipeline. The pipeline:

1. Downloaded MQSC and PCF command reference pages from IBM documentation
2. Extracted attribute names, types, and value constants
3. Built a mapping between MQSC and PCF attribute names
4. Proposed `snake_case` equivalents for each attribute

The automated output was then reviewed, customized, and rationalized by
hand. Many names were changed, value mappings were corrected, and
qualifier-specific overrides were applied.

## Current source of truth

`src/pymqrest/mapping_data.py` is the sole authoritative source for all
attribute mappings. It is maintained directly — not generated from
external documentation.

The original extraction pipeline and its artifacts are archived in
`docs/archive/extraction/` for historical reference.

## Handling future MQ versions

When IBM releases a new MQ version (for example, 9.5):

1. Compare the previous and new MQSC command reference for new, changed,
   or removed attributes
2. Propose `snake_case` names for new attributes following the
   established naming conventions in `mapping_data.py`
3. Update `mapping_data.py` directly with the new mappings
4. Regenerate downstream artifacts:

   ```bash
   uv run python3 scripts/dev/generate_commands.py
   uv run python3 scripts/dev/generate_mapping_docs.py
   uv run python3 scripts/dev/validate_local.py
   ```

Re-running the archived extraction pipeline is not recommended. The
namespace has diverged significantly from what automation would produce,
and manual maintenance preserves the naming consistency that has been
built up over time.
