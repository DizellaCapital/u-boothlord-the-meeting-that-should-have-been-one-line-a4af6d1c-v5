#!/usr/bin/env python3
"""The Meeting That Should Have Been One Line — make.fun bounty entry.

Writes a single sentence that replaces one useless meeting to
MAKEFUN_OUTPUT_DIR/entry.txt (falling back to /output).
Standard library only.
"""

import os
import sys

LINE = (
    "The launch is cancelled, the $40,000 is already spent on the party, "
    "and this meeting is just twelve people billing an hour to mourn a "
    "decision Karen made in the hallway at 8:12."
)

SENTENCE_ENDINGS = (".", "!", "?")


def validate(line: str) -> None:
    """Enforce the bounty constraints on the entry line."""
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be exactly one line")
    if "\t" in line:
        raise ValueError("entry must not contain tabs")
    if not 1 <= len(line) <= 200:
        raise ValueError(
            "entry must be 1-200 characters, got %d" % len(line)
        )
    if not line.endswith(SENTENCE_ENDINGS):
        raise ValueError("entry must end with sentence punctuation")
    if line != line.strip():
        raise ValueError("entry must not have leading/trailing whitespace")


def main() -> int:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(LINE + "\n")
    # Read back and verify what was actually written.
    with open(path, "r", encoding="utf-8") as fh:
        written = fh.read()
    if written != LINE + "\n":
        raise RuntimeError("read-back verification failed")
    print("wrote %s (%d characters, 1 line)" % (path, len(LINE)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
