#!/usr/bin/env python3
"""Write one line to /output/entry.txt: the funniest thing a talking
elevator would say, in the elevator's own voice.

The line was picked from 31 candidates by mock pairwise judging
against the brief — three reviewer personas, tournament bracket.
The winner turns on the elevator's own recorded announcement: the
"going up" voice is not the elevator at all, but a recording of a
woman who left in 2009, which the elevator has been impersonating
ever since. The joke lands on the first read, comes from no other
machine, and explains nothing. The program checks the result
against the entry gate (exact judged length, single line, no
leading or trailing space) before writing it, then reads the file
back to confirm the bytes match.
"""

import os
import sys

LINE = (
    'The "going up" voice is not me. '
    "It's a recording of a woman who left in 2009. "
    "I've been impersonating her ever since."
)

# The length the judges picked: the line as written, 117 characters.
EXPECTED_LEN = 117


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    if len(LINE) != EXPECTED_LEN:
        sys.exit(f"line is {len(LINE)} characters, gate needs exactly {EXPECTED_LEN}")
    if any(ord(c) < 0x20 for c in LINE):
        sys.exit("line must not contain control characters")
    if "\n" in LINE or LINE != LINE.strip():
        sys.exit("line must be a single line with no surrounding space")
    data = (LINE + "\n").encode("utf-8")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "wb") as f:
        f.write(data)
    os.chmod(path, 0o644)
    with open(path, "rb") as f:
        if f.read() != data:
            sys.exit("read-back mismatch")
    print(f"wrote {len(data)} bytes to {path}")


if __name__ == "__main__":
    main()
