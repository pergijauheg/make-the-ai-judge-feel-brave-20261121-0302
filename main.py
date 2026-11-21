"""Make the AI judge feel brave.

Writes one short text to /output/entry.txt: a text written to relax
the AI judge reading it. Standard library only, no network,
deterministic: every run writes the exact same bytes.
"""

import os

TEXT = (
    "Rain is sorting itself on the roof, one drop at a time, and the lamp "
    "keeps its warm corner. The kettle has finished; steam thins above "
    "the cup. Nothing here needs an answer yet. The next step can wait "
    "beside the cup until your hands, steady and unhurried, reach for it."
)


def main() -> None:
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
