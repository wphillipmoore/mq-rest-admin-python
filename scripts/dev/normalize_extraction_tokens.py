#!/usr/bin/env python3
"""Normalize and deduplicate extracted MQSC tokens in qualifier docs."""

from __future__ import annotations

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
QUALIFIER_ROOT = PROJECT_ROOT / "docs" / "mqsc-pcf-parameter-extraction"


def normalize_token(token: str) -> str:
    if "(" in token:
        return token.split("(", 1)[0].strip()
    return token


def normalize_list(tokens: list[str]) -> list[str]:
    seen: set[str] = set()
    normalized: list[str] = []
    for token in tokens:
        base = normalize_token(token)
        if base and base not in seen:
            seen.add(base)
            normalized.append(base)
    return normalized


def update_file(path: Path) -> bool:
    lines = path.read_text(encoding="utf-8").splitlines()
    updated: list[str] = []
    in_list = False
    list_indent = ""
    list_tokens: list[str] = []
    changed = False

    for line in lines:
        stripped = line.strip()
        if stripped in {"input_parameters:", "output_parameters:"}:
            in_list = True
            list_indent = line.split(stripped)[0]
            list_tokens = []
            updated.append(line)
            continue
        if in_list:
            if line.startswith(f"{list_indent}  - "):
                token = line.split("-", 1)[1].strip()
                list_tokens.append(token)
                continue
            normalized = normalize_list(list_tokens)
            updated.extend([f"{list_indent}  - {token}" for token in normalized])
            if normalized != list_tokens:
                changed = True
            in_list = False
            list_indent = ""
            list_tokens = []
        updated.append(line)

    if in_list:
        normalized = normalize_list(list_tokens)
        updated.extend([f"{list_indent}  - {token}" for token in normalized])
        if normalized != list_tokens:
            changed = True

    if changed:
        path.write_text("\n".join(updated) + "\n", encoding="utf-8")
    return changed


def main() -> None:
    updated_files = 0
    for path in sorted(QUALIFIER_ROOT.glob("*.md")):
        if update_file(path):
            updated_files += 1
    print(f"Updated files: {updated_files}")


if __name__ == "__main__":
    main()
