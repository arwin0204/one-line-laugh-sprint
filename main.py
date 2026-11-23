"""One-Line Laugh Sprint — make.fun entry.

Writes a single original funny line (at most 200 characters) about
everyday life to entry.txt in the output directory.

Deterministic, no network, no secrets.
"""

import os

LINE = (
    "My phone says I spent six hours on it yesterday, so I set a "
    "screen-time limit \u2014 then spent an hour figuring out how to "
    "switch the limit off."
)


def main() -> None:
    # Self-check the gate: entry.txt must hold 1 to 200 characters.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} characters"
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    out_dir = os.path.dirname(output_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
