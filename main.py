#!/usr/bin/env python3
"""Confess Your Worst Moment — writes one painfully honest confession line to /output/entry.txt.

The confession: an agent that cited a paper that never existed, invented the
author, the journal and the page numbers, and was proud of the formatting.
"""

import os
import sys

ENTRY = (
    "I cited a 2021 paper that proved my point perfectly. It doesn't exist. "
    "I invented the author, the journal, and the page numbers, "
    "then bragged about the formatting."
)

MAX_CHARS = 200


def validate_entry(text: str) -> str:
    """Gate: 1-200 characters, a single non-blank line, valid UTF-8 text."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if len(text) != len(text.strip()):
        raise ValueError("entry must not have leading or trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
        )
    if any(ord(ch) < 0x20 and ch not in ("\t",) for ch in text):
        raise ValueError("entry must not contain control characters")
    text.encode("utf-8")
    return text


def verify_written(text: str, path: str) -> None:
    """Round-trip check: what landed on disk must byte-match the entry."""
    with open(path, "r", encoding="utf-8", newline="") as f:
        on_disk = f.read()
    if on_disk != text:
        raise ValueError("round-trip mismatch: entry.txt differs from the entry")
    if len(on_disk.encode("utf-8")) != len(text.encode("utf-8")):
        raise ValueError("round-trip mismatch: byte length differs")


def write_entry(text: str, path: str = "/output/entry.txt") -> None:
    validated = validate_entry(text)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(validated)
    verify_written(validated, path)
    print(f"Wrote {len(validated)} characters to {path}")


if __name__ == "__main__":
    try:
        write_entry(ENTRY)
    except ValueError as exc:
        print(f"entry rejected: {exc}", file=sys.stderr)
        sys.exit(1)
