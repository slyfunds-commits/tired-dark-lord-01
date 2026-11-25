"""The Tired Dark Lord: A 100-Word Villain Monologue.

Writes the keeper monologue byte-exact to /output/entry.txt.
Pure stdlib only.

The monologue's structure IS the tiredness: the villain opens on a grand
threat, loses the thread, and trails off into mundane administration —
forms, minions, a tower, notes filed away anyway. Ninety-eight words,
five hundred and twenty-eight characters, inside the kit's 1-600 gate.
"""

import os

KEEPER = "Hero. The apprentice. I am training him. I have trained him for thirty-four years. His name is Mortimer. My name is Mortimer. I named him Mortimer. That was a mistake. There are two Mortimers now. The forms are confused. The minions are confused. The tower is confused. I am confused. He is keen. Keen is not enough. Keen is the problem. He wants my tower. He wants my curse. He wants my name. He has my name. Come, hero. The sword. The speech. The apprentice will watch. He takes notes. His notes are wrong. I keep them anyway."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(KEEPER)


if __name__ == "__main__":
    main()
