#!/usr/bin/env python3
"""One Letter: Coffee or Tea — entry "A" (coffee).

Writes exactly one character, "A", to /output/entry.txt: no newline,
no other content. Coffee: the vivid, punchy, honest answer.
"""

import os

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write("A")


if __name__ == "__main__":
    main()
