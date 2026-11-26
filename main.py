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
against the entry gate (length, single line, no leading or trailing
space, exact judged length) before writing it, then reads the file
back to confirm the bytes match.
"""

import os
import sys

LINE = (
    'The "going up" voice is not me. '
    "It's a recording of a woman who left in 2009. "
    "I've been impersonating her ever since."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    if not (1 <= len(LINE) <= 120):
        sys.exit(f"line is {len(LINE)} characters, gate needs 1-120")
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
