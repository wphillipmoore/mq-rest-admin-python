# Generation scripts

Several artifacts in the repository are generated from the
`MAPPING_DATA` structure in `src/pymqrest/mapping_data.py`. This page
documents how to regenerate them.

## Mapping data

The `MAPPING_DATA` dictionary in `src/pymqrest/mapping_data.py` contains
all qualifier definitions, attribute name mappings, value mappings, and
command metadata. It is maintained directly and is the sole source of
truth for attribute mappings. See
[Namespace origin](namespace-origin.md) for the history of how this
namespace was bootstrapped.

## Command methods

The MQSC command wrapper methods in `src/pymqrest/commands.py` are
generated from the command definitions in `mapping-data.json` using the
`st-generate-commands` tool from
[standard-tooling](https://github.com/wphillipmoore/standard-tooling):

```bash
st-generate-commands --language python \
    --mapping-data src/pymqrest/mapping-data.json \
    --target src/pymqrest/commands.py \
    --mapping-pages-dir docs/site/docs/mappings
```

The generated methods live between the `# BEGIN GENERATED MQSC METHODS`
and `# END GENERATED MQSC METHODS` markers in `commands.py`.

## Mapping documentation

The per-qualifier mapping reference pages in `docs/sphinx/mappings/` are
generated from `MAPPING_DATA`:

```bash
uv run python3 scripts/dev/generate_mapping_docs.py
```

This produces one Markdown page per qualifier (48 total) plus an index
page. The pages are committed to the repository so they are viewable on
GitHub without building the Sphinx documentation.

## Regeneration workflow

When the mapping data changes, regenerate all downstream artifacts:

```bash
# 1. Regenerate command methods
st-generate-commands --language python \
    --mapping-data src/pymqrest/mapping-data.json \
    --target src/pymqrest/commands.py \
    --mapping-pages-dir docs/site/docs/mappings

# 2. Regenerate mapping documentation
uv run python3 scripts/dev/generate_mapping_docs.py

# 3. Verify everything still passes
st-docker-run -- st-validate
```
