"""Kabyle text cleaner – fix non-standard characters and reflow paragraphs."""

from ._data import ALLOWED_SET, DEFAULT_MAPPING
from ._fix import fix_text, disallowed_in_text
from ._reflow import reflow_paragraphs
from ._io import load_extra_mapping, read_file, write_file

__all__ = [
    "ALLOWED_SET",
    "DEFAULT_MAPPING",
    "fix_text",
    "disallowed_in_text",
    "reflow_paragraphs",
    "load_extra_mapping",
    "read_file",
    "write_file",
]

__version__ = "0.1.0"
