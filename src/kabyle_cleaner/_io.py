import sys
from pathlib import Path
from typing import Dict

if sys.version_info >= (3, 11):
    import tomllib
else:
    import tomli as tomllib  # py<3.11

def load_extra_mapping(toml_path: Path) -> Dict[str, str]:
    with toml_path.open("rb") as fh:
        extra = tomllib.load(fh)
    return extra.get("mapping", {})

def read_file(path: Path) -> str:
    with path.open(encoding="utf-8") as fh:
        return fh.read()

def write_file(path: Path, text: str) -> None:
    with path.open("w", encoding="utf-8") as fh:
        fh.write(text)
