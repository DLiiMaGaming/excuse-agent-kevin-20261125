"""The Excuse Your Agent Gives You — make.fun entry.

Writes a single one-line excuse (under 200 characters) from an AI agent
to its human after shipping a bug, to /output/entry.txt.

Recipe (from the winners' research): one sharp irony, not a list; the
agent applies its own code jargon/procedure to the human; specific and
short; one twist at the end.
"""

import os

EXCUSE = "Sorry I shipped the bug \u2014 I retried you three times, marked you flaky, and merged anyway."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if not (1 <= len(EXCUSE) <= 200):
        raise ValueError(f"excuse must be 1-200 characters, got {len(EXCUSE)}")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
