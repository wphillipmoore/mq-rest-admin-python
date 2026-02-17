#!/usr/bin/env bash
set -euo pipefail

# Collect standard docs (structural checks + markdownlint).
files=()
while IFS= read -r file; do
  files+=("$file")
done < <(find docs -path docs/sphinx -prune -o -path docs/site -prune -o -path docs/announcements -prune -o -type f -name "*.md" -print)

if [[ -f README.md ]]; then
  files+=("README.md")
fi

# Collect doc-site files (markdownlint only — structural checks like
# Table of Contents and single-H1 do not apply to pages built by
# documentation site generators such as Sphinx, MkDocs, etc.).
docsite_files=()
for docsite_dir in docs/sphinx docs/site; do
  if [[ -d "$docsite_dir" ]]; then
    while IFS= read -r file; do
      docsite_files+=("$file")
    done < <(find "$docsite_dir" -type f -name "*.md")
  fi
done

all_files=("${files[@]}" ${docsite_files[@]+"${docsite_files[@]}"})

# CHANGELOG.md gets markdownlint only — no structural checks (no TOC,
# multiple H2 headings are expected, heading hierarchy differs).
if [[ -f CHANGELOG.md ]]; then
  all_files+=("CHANGELOG.md")
fi

if [[ ${#all_files[@]} -eq 0 ]]; then
  echo "ERROR: no markdown files found to lint." >&2
  exit 2
fi

if command -v markdownlint >/dev/null 2>&1; then
  markdownlint_cmd=(markdownlint)
else
  echo "ERROR: markdownlint not found. Install markdownlint-cli locally." >&2
  exit 2
fi

markdownlint_failed=0
if [[ -f ".markdownlint.yaml" ]]; then
  if ! "${markdownlint_cmd[@]}" --config ".markdownlint.yaml" "${all_files[@]}"; then
    markdownlint_failed=1
  fi
else
  if ! "${markdownlint_cmd[@]}" "${all_files[@]}"; then
    markdownlint_failed=1
  fi
fi

failed=0

for file in "${files[@]}"; do
  awk -v file="$file" '
    BEGIN {
      in_code = 0
      toc_found = 0
      h1_count = 0
      last_level = 0
      errors = 0
    }
    function report(message) {
      printf "ERROR: %s (%s:%d)\n", message, file, NR > "/dev/stderr"
      errors = 1
    }
    {
      line = $0

      if (match(line, /^```/) || match(line, /^~~~/)) {
        in_code = !in_code
      }

      if (in_code) {
        next
      }

      if (line ~ /^## Table of Contents[[:space:]]*$/) {
        toc_found = 1
      }

      if (line ~ /^#{1,6} /) {
        level = length(substr(line, 1, match(line, / /) - 1))
        if (level == 1) {
          h1_count += 1
        }
        if (last_level > 0 && level > last_level + 1) {
          report("Heading level skips from " last_level " to " level)
        }
        last_level = level
      }
    }
    END {
      if (h1_count != 1) {
        printf "ERROR: expected exactly one H1 heading, found %d (%s)\n", h1_count, file > "/dev/stderr"
        errors = 1
      }
      if (toc_found != 1) {
        printf "ERROR: missing ## Table of Contents (%s)\n", file > "/dev/stderr"
        errors = 1
      }
      exit errors
    }
  ' "$file" || failed=1

done

exit $((failed || markdownlint_failed))
