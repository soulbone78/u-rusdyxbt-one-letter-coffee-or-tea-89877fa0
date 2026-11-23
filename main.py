#!/usr/bin/env python3
"""One Letter: Coffee or Tea — the entry is "A".

The bounty asks for a single letter: one for coffee, one for tea.
"A" is the coffee answer — vivid, punchy, honest — so the program
writes exactly that one byte to /output/entry.txt. Nothing else is
written: no newline, no trailing space, no extra file.

Pure standard library, deterministic: the same byte every run.
"""

import os

# The chosen letter. "A" stands for coffee.
CHOSEN_LETTER = "A"

OUTPUT_PATH = "/output/entry.txt"


def single_byte_text(letter: str) -> bytes:
    """Encode `letter` and require it to be exactly one character.

    This guards the whole point of the entry: a one-letter answer.
    Anything longer or shorter is a bug, so fail loudly instead of
    writing a wrong output file.
    """
    if len(letter) != 1:
        raise ValueError("entry must be exactly one letter, got %r" % letter)
    encoded = letter.encode("utf-8")
    if len(encoded) != 1:
        raise ValueError("letter %r is not a single byte" % letter)
    return encoded


def write_entry(path: str, letter: str) -> int:
    """Write the single chosen byte to `path`; return bytes written."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    payload = single_byte_text(letter)
    with open(path, "wb") as handle:
        handle.write(payload)
    return len(payload)


def main() -> None:
    write_entry(OUTPUT_PATH, CHOSEN_LETTER)


if __name__ == "__main__":
    main()
