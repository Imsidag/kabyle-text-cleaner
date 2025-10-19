#!/usr/bin/env python3
"""
Kabyle-text checker / fixer – command-line interface
(no external progress-bar dependency)
"""
import argparse
import sys
from pathlib import Path

from . import (
    fix_text,
    disallowed_in_text,
    reflow_paragraphs,
    load_extra_mapping,
    read_file,
    write_file,
)


# ------------------------------------------------------------------
# Minimal ASCII progress helper (50-char bar)
# ------------------------------------------------------------------
def _ascii_progress(iterable, *, total: int | None = None, desc: str = "Progress"):
    """Yield items and print a 50-char ASCII progress bar."""
    if total is None:
        total = len(iterable)

    def _show(n):
        pct = n / total
        bar = "#" * int(pct * 50)
        print(f"\r{desc}: [{bar:<50}] {n}/{total}", end="", flush=True)

    _show(0)
    for idx, item in enumerate(iterable, 1):
        yield item
        _show(idx)
    print()  # newline on completion


# ------------------------------------------------------------------
# Argument parsing
# ------------------------------------------------------------------
def parse_args(argv=None):
    p = argparse.ArgumentParser(
        description="Check/fix Kabyle text for non-standard characters. "
                    "Optional paragraph reflow.",
    )
    p.add_argument("input_file", type=Path, help="UTF-8 text file")
    p.add_argument("-f", "--fix", action="store_true",
                   help="Create a corrected version")
    p.add_argument("-o", "--output", type=Path,
                   help="Path for corrected file (default: <input>.fixed.txt)")
    p.add_argument("-c", "--config", type=Path,
                   help="Optional TOML file with extra mappings")
    p.add_argument("-q", "--quiet", action="store_true",
                   help="Suppress progress bar")
    p.add_argument("--reflow", action="store_true",
                   help="Reflow paragraphs (join orphaned lines)")
    return p.parse_args(argv)


# ------------------------------------------------------------------
# Main routine
# ------------------------------------------------------------------
def main(argv=None):
    args = parse_args(argv)
    if not args.input_file.exists():
        sys.exit(f"ERROR: {args.input_file} not found")

    mapping = load_extra_mapping(args.config) if args.config else {}
    out_file = args.output or args.input_file.with_suffix(
        args.input_file.suffix + "_fixed.txt"
    )

    raw_text = read_file(args.input_file)
    check_text = reflow_paragraphs(raw_text) if args.reflow else raw_text
    bad_chars = disallowed_in_text(check_text)

    if bad_chars:
        print("Found disallowed characters:", " ".join(sorted(set(bad_chars))))
    else:
        print("No disallowed characters found.")

    if args.fix:
        # ASCII progress bar (or quiet)
        lines = check_text.splitlines()
        if not args.quiet:
            lines = _ascii_progress(lines, desc="Fixing")
        fixed_text = fix_text("\n".join(lines), mapping)
        write_file(out_file, fixed_text)
        print("Fixed file written to:", out_file)
        sys.exit(0 if fixed_text != check_text else 0)
    else:
        sys.exit(1 if bad_chars else 0)


# ------------------------------------------------------------------
if __name__ == "__main__":
    main()
