#!/usr/bin/env python3
"""The One-Line Exit — make.fun entry.

Writes a single original one-line resignation letter to
$MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt when the variable
is unset).

Python 3.13, standard library only, no network access, fully deterministic:
every run writes exactly the same bytes.
"""

import os

# The entry: one line, 97 characters, inside the 1-140 gate.
# A real, sendable resignation line with a specific voice — the office
# plant got promoted twice, the writer did not — and the punch lands
# in the final words.
ENTRY = (
    "I hereby resign, effective immediately: the office plant has been "
    "promoted twice, and I have not."
)

MAX_CHARS = 140


def main() -> None:
    line = ENTRY.strip()
    if not (1 <= len(line) <= MAX_CHARS):
        raise SystemExit(f"entry is {len(line)} chars, outside the 1-{MAX_CHARS} gate")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be exactly one line")
    if not line.strip():
        raise SystemExit("entry must not be only whitespace")
    if "  " in line:
        raise SystemExit("entry contains a double space")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the file holds exactly the judged line.
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line)
    print(f"wrote {len(line)} chars to {path}")


if __name__ == "__main__":
    main()
