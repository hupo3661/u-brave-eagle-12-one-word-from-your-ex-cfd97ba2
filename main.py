#!/usr/bin/env python3
"""One Word From Your Ex - writes exactly one word to /output/entry.txt.

The word is the one an ex would use to describe you: "Exhausting".
It lands because it is painfully honest and funny at once - being with
you was a lot, in the best and worst ways - and it even starts with "ex".

Deterministic: no randomness, no network, no clock. The output is exactly
one word, with no trailing newline and no extra text.
"""

import os

WORD = "Exhausting"


def validate(word: str) -> None:
    if not word:
        raise SystemExit("Invalid word: entry must be non-empty.")
    if not word.isalpha():
        raise SystemExit(
            "Invalid word: entry must be a single alphabetic word, "
            "with no spaces, punctuation, digits, or other characters."
        )
    if word != word.strip() or len(word.split()) != 1:
        raise SystemExit(
            "Invalid word: entry must be exactly one word with no "
            "leading or trailing whitespace."
        )
    if "\n" in word or "\r" in word:
        raise SystemExit(
            "Invalid word: entry must contain no newline characters."
        )


def main() -> None:
    validate(WORD)
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    directory = os.path.dirname(output_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
    with open(output_path, "rb") as f:
        written = f.read()
    if written != WORD.encode("utf-8"):
        raise SystemExit(
            "Write verification failed: entry file bytes do not match the word."
        )


if __name__ == "__main__":
    main()
