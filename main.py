"""Print (and save) two lines to your past self.

Exactly two lines, each at most 200 characters: a short, warm note
to the person you used to be. Pure Python standard library,
deterministic, no network access. It prints the lines to stdout and
also writes them to /output/entry.txt, where the competition's scorer
reads them.
"""

import os

LINES = (
    "Dear past me: the thing you are afraid to start is the thing that saves you.",
    "Buy the ticket, send the message, and stop rehearsing the version of you that loses.",
)


def main():
    text = "\n".join(LINES)
    print(text)
    try:
        os.makedirs("/output", exist_ok=True)
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(text + "\n")
    except OSError:
        pass


if __name__ == "__main__":
    main()
