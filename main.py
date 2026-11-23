#!/usr/bin/env python3
"""One Word From Grandma.

Writes the single word Grandma would text about AI to entry.txt.

The word is "contraption": the warm, baffled word a grandma reaches for
when a machine she does not quite trust does something clever anyway.
One word, eleven bytes, no punctuation, no trailing newline -- exactly
what the gate asks for (UTF-8 text of 1 to 30 characters).

Pure standard library, fully deterministic: every run writes the same
eleven bytes.
"""

import os

WORD = "contraption"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
