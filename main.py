#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers — make.fun entry.

Writes one original fortune-cookie line for a software developer to
/output/entry.txt. The line is a single short balanced sentence about
estimates and the future, with a quiet double meaning.

The program writes the line as exact bytes (no trailing newline), then
reads the file back and fails loudly if the bytes differ or the text
breaks the competition gate (1-120 UTF-8 characters, not only
whitespace), so a bad write can never silently pass as an entry.
"""

import os
import sys

LINE = "Your estimate was honest; the future simply charged interest."
MAX_CHARS = 120


def main() -> int:
    data = LINE.encode("utf-8")
    text = LINE
    if not (1 <= len(text) <= MAX_CHARS) or not text.strip():
        print("entry fails gate: length %d" % len(text), file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(data)
    with open("/output/entry.txt", "rb") as f:
        back = f.read()
    if back != data:
        print("read-back mismatch", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
