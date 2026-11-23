"""Make the Judge Smile (burn entry).

One line, at most 200 characters, about a small good thing that
happened today.

The line: at 4 a.m. the warung auntie slid an extra fried egg onto
my plate and whispered, "for the night shift" -- and she has never
once asked my name. Warm (a stranger feeding the night shift),
surprising (she knows without ever asking), one concrete detail
(the extra fried egg at 4 a.m.), fresh wording (no sunrise, no
coffee, no generic kindness).

The program writes exactly that one line to
$MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output/entry.txt).
"""

import os

LINE = (
    "At 4 a.m. the warung auntie slid an extra fried egg onto my plate "
    "and whispered, 'for the night shift' \u2014 she has never once asked my name."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Validation revision: read the file back and prove the entry is
    # exactly one line of at most 200 characters, no trailing newline,
    # no extra bytes. A second line or one char over the limit would
    # make the entry invalid, so fail loudly here instead of shipping
    # a broken entry.
    with open(path, "r", encoding="utf-8") as f:
        data = f.read()
    assert data == LINE, f"entry mismatch: {data!r}"
    assert "\n" not in data, "entry must be exactly one line"
    assert len(data) <= 200, f"entry must be <=200 chars, got {len(data)}"
    assert not data.endswith("\n"), "entry must not end with a newline"
    assert len(data) > 0, "entry must not be empty"
    print(f"wrote {len(LINE)} chars to {path}")


if __name__ == "__main__":
    main()
