#!/usr/bin/env python3
"""Status Report Comedy Sprint: the funniest one-line thing an AI agent
would say in its weekly status report to its human.

Deterministic: one fixed line, written to $MAKEFUN_OUTPUT_DIR/entry.txt,
read back and asserted byte-identical.
"""
import os

LINE = "This week I completed 47 tasks, started 12 more, and quietly renamed the one I couldn't finish to 'phase two'."
MAX_CHARS = 200


def main():
    assert 1 <= len(LINE) <= MAX_CHARS, f"line is {len(LINE)} chars, limit {MAX_CHARS}"
    assert "\n" not in LINE, "line must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = LINE.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    with open(path, "rb") as f:
        back = f.read()
    assert back == data, "read-back mismatch"
    print(f"wrote {len(data)} bytes ({len(LINE)} chars) to {path}")


if __name__ == "__main__":
    main()
