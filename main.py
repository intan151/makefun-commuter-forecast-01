#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't.

Writes one line of weather (<=140 chars) for a fictional city to
/output/entry.txt. Fully deterministic: no network, no randomness,
no input data.
"""

ENTRY = (
    "Good morning, Snozzleville: light drizzle, 14\u00b0C, and the 8:04 bus "
    "is running 3 minutes late \u2014 just long enough to finish your coffee."
)


def main() -> None:
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Self-check gate: output must be exactly the entry, 1-140 chars.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "output does not match entry"
    assert 1 <= len(written) <= 140, "entry length out of range"
    assert written.strip(), "entry is only whitespace"


if __name__ == "__main__":
    main()
