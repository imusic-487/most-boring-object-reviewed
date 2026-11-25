#!/usr/bin/env python3
"""The Most Boring Object, Reviewed in One Line.

Writes a single funny, true one-line review of the dullest everyday
object to /output/entry.txt (1-200 characters, one line).

The object: the AA battery in the junk drawer. The joke is the object's
own dullness -- dead for years, kept "just in case", never thrown away,
and somehow destined to outlive us all.
"""

import os

ENTRY = (
    "The AA battery in the junk drawer: dead since 2021, "
    "kept 'just in case', and it will outlive us all."
)


def main() -> None:
    # The gate: /output/entry.txt must be UTF-8 text of 1 to 200
    # characters, not only white space, on a single line.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert ENTRY.strip(), "entry must not be only white space"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
