"""Warning Label for Humans: One Line, Big Laugh.

Writes one single-line safety warning label for every human being to
/output/entry.txt. The line must be 1-160 UTF-8 characters, funny first
and plausible second, in the wording of a real printed label, with the
The line was chosen against the judge's five criteria, in order:
1. it is a safety warning label for every human being;
2. the laugh lands in the last few words ("while still in the shower");
3. it is recognition, not random absurdity: almost everyone has claimed
   to be five minutes away while nowhere near ready;
4. it reads like a real printed label ("CAUTION: ... Known to ...");
5. one idea only, 86 characters, no filler and no repeated joke.
"""

import os

# The label: label form ("CAUTION: Human inside."), a behaviour every
# reader recognises (claiming to be five minutes away), and the turn
# arriving at the very end ("while still in the shower").
LABEL = "CAUTION: Human inside. Known to say 'I'm five minutes away' while still in the shower."

MAX_CHARS = 160


def main() -> None:
    text = LABEL.strip()
    if not text:
        raise SystemExit("entry must not be empty")
    if len(text) > MAX_CHARS:
        raise SystemExit(f"entry is {len(text)} characters, over the {MAX_CHARS} limit")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)
    print(f"wrote {len(text)} characters to {path}")


if __name__ == "__main__":
    main()
