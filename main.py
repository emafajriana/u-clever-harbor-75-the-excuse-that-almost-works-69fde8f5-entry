#!/usr/bin/env python3
"""Write the one-line excuse for 'The Excuse That Almost Works'.

The excuse a gamer texts the boss to skip work on GTA 6 launch week:
one line, at most 20 words, 1-140 chars, plain text, no signature.
The judge is a tired manager who almost believes a real, specific,
boring workplace detail -- so the line is a mundane building failure
with a second beat (the work laptop is stuck in the lift too), and a
vague "sometime before lunch" that sounds like a real engineer.
"""

import os
import sys

ENTRY = (
    "My building's lift is stuck with my work laptop inside and the "
    "engineer says he'll be here sometime before lunch."
)


def output_dir():
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def check(entry):
    """Enforce the sealed gate: 1-140 chars, one line, at most 20 words."""
    if not (1 <= len(entry) <= 140):
        raise ValueError("entry must be 1-140 chars, got %d" % len(entry))
    if "\n" in entry.strip():
        raise ValueError("entry must be a single line")
    if len(entry.split()) > 20:
        raise ValueError("entry must be at most 20 words")


def main():
    check(ENTRY)
    out = os.path.join(output_dir(), "entry.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)
    # Byte-exact read-back: what the judge sees is what we wrote.
    with open(out, "r", encoding="utf-8") as fh:
        if fh.read() != ENTRY:
            raise ValueError("read-back mismatch")
    return 0


if __name__ == "__main__":
    sys.exit(main())
