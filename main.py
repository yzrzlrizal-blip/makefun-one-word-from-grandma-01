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


def _check_word(word: str) -> None:
    """Refuse to write anything the gate would reject: the gate only
    accepts UTF-8 text of 1 to 30 characters, not only whitespace, and
    the judge only ever sees one word, so fail loudly here instead of
    submitting an entry that can never be judged."""
    if not 1 <= len(word) <= 30:
        raise SystemExit(f"word must be 1-30 characters, got {len(word)}")
    if not word.strip() or word != word.strip():
        raise SystemExit("word must be a single word with no whitespace")
    if any(ch.isspace() for ch in word):
        raise SystemExit("word must be a single word with no whitespace")


def main() -> None:
    _check_word(WORD)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
