#!/usr/bin/env python3
"""The Tired Dark Lord: A 100-Word Villain Monologue.

Writes the keeper monologue verbatim to $MAKEFUN_OUTPUT_DIR/entry.txt
(falls back to a relative output/ directory when the variable is unset).
Pure stdlib only -- the grader runs python:3.13-slim with no site-packages.
"""

import os

ENTRY = (
    "Hero. The apprentice. I am training him. I have trained him for "
    "thirty-four years. His name is Mortimer. My name is Mortimer. "
    "I named him Mortimer. That was a mistake. There are two Mortimers "
    "now. The forms are confused. The minions are confused. The tower "
    "is confused. I am confused. He is keen. Keen is not enough. Keen "
    "is the problem. He wants my tower. He wants my curse. He wants my "
    "name. He has my name. Come, hero. The sword. The speech. The "
    "apprentice will watch. He takes notes. His notes are wrong. "
    "I keep them anyway."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
