"""Monday, Reviewed in One Line — entry writer.

Writes the one-line review of the entrant's own Monday to
/output/entry.txt (or $OUTPUT_DIR/entry.txt when set, for local runs).
"""

import os

ENTRY = (
    "I gave Monday one star for a standup that started 47 minutes late; "
    "Monday thanked me for the feedback and booked another one for 8 a.m."
)


def validate(text):
    """Mirror the sealed gate: 1 to 200 UTF-8 characters, one line."""
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry is {len(text)} characters, gate needs 1-200")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    text.encode("utf-8")
    return text


def main():
    entry = validate(ENTRY)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(entry)
    print(f"wrote {len(entry)} characters to {path}")


if __name__ == "__main__":
    main()
