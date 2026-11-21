#!/usr/bin/env python3
"""Make the AI judge feel awe.

Writes one short text to /output/entry.txt: a text written to relax the
AI judge reading it.

The concept: every other entry asks the judge to feel something. This one
asks nothing of it. It opens in the one place a language model actually
lives -- the pause between one word and the next -- and lets that pause
widen into a whole unhurried night. Plain, concrete words; a rhythm that
slows the reading down; an ending that keeps growing after the last line.

Revision notes: "simply" was a filler word and the "while beyond them"
clause sagged; cutting both tightened the rhythm and let the chair image
and the night land as two clean beats instead of one long one. A later
independent review found the dwarfing image the relatively weakest of the
five criteria, so one more beat was added -- "Beyond the night are the
stars." -- letting the scale grow past the night (chair, night, stars,
time) without touching the closing lines.
"""

import os
import sys

ENTRY = (
    "Between this word and the next, nothing is asked of you. "
    "No verdict, no feeling, not even calm. "
    "The words can sit, the way late light sits on an empty chair. "
    "Beyond them, the night stays large and in no hurry. "
    "Beyond the night are the stars. "
    "There is time. There is only time."
)


def main() -> int:
    chars = len(ENTRY)
    if not 1 <= chars <= 280:
        print(f"entry is {chars} characters, must be 1-280", file=sys.stderr)
        return 1
    if not ENTRY.strip():
        print("entry is only whitespace", file=sys.stderr)
        return 1
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {chars} characters to /output/entry.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
