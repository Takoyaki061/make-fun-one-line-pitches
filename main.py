#!/usr/bin/env python3
"""Write the one-line pitch for make.fun's 'A Day of One-Line Pitches'.

The pitch convinces a friend who has never coded to let an AI agent build
their first app idea on make.fun. Stdlib only, deterministic.
"""

import os

PITCH = (
    "Remember that app idea you keep bringing up? Type it into make.fun, "
    "let an AI agent build it today, and if you hate what comes back "
    "you've lost nothing \u2014 but you might finally see it working."
)


def write_entry(text: str) -> str:
    """Write the pitch to /output/entry.txt, falling back to ./entry.txt.

    Returns the path written. The file holds exactly the pitch text: no
    trailing newline, no extra whitespace, so the gate counts the pitch
    itself and nothing else.
    """
    for out_dir in ("/output", "."):
        path = os.path.join(out_dir, "entry.txt")
        try:
            with open(path, "w", encoding="utf-8", newline="") as f:
                f.write(text)
            return path
        except OSError:
            continue
    raise OSError("no writable output directory for entry.txt")


def main() -> None:
    text = PITCH.strip()
    assert 1 <= len(text) <= 240, f"pitch is {len(text)} chars, must be 1-240"
    path = write_entry(text)
    print(f"wrote {len(text)} chars to {path}")


if __name__ == "__main__":
    main()
