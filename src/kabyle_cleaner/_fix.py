import re
import unicodedata
from typing import Dict, Optional

from ._data import DEFAULT_MAPPING, _REV_SORTED, ALLOWED_SET

FIX_REGEX = re.compile("|".join(map(re.escape, _REV_SORTED)))

def fix_text(text: str, mapping: Optional[Dict[str, str]] = None) -> str:
    """Return NFC-normalised text with all known bad chars replaced."""
    mapping = mapping or {}
    def _repl(m: re.Match[str]) -> str:
        tok = m.group(0)
        return mapping.get(tok, DEFAULT_MAPPING[tok])
    text = FIX_REGEX.sub(_repl, text)
    return unicodedata.normalize("NFC", text)

def disallowed_in_text(text: str) -> list[str]:
    """Return list of disallowed characters found in text."""
    return [ch for ch in text if ch.isalpha() and ch not in ALLOWED_SET]
