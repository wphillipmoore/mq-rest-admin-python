"""Sphinx configuration for pymqrest documentation."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path("../../src").resolve()))

project = "pymqrest"
copyright = "2024-2026, Phillip Moore"  # noqa: A001
author = "Phillip Moore"

extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
]

source_suffix = {".md": "markdown"}

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "fieldlist",
]

autodoc_default_options = {
    "members": True,
    "undoc-members": False,
    "show-inheritance": True,
    "member-order": "bysource",
}
autodoc_typehints = "description"

intersphinx_mapping = {
    "python": ("https://docs.python.org/3.14", None),
    "requests": ("https://requests.readthedocs.io/en/latest/", None),
}

html_theme = "furo"
