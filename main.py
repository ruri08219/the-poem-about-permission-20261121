"""A short poem about agency: the power to ask and to be given.

Two words rearrange the room. The yes is a hand, unclenching.
Nothing is taken, nothing is owed. Power passes between us
like a coin warmed by two palms — spent, and still ours.

The poem is fixed text, written deterministically to
``/output/entry.txt`` with no network access.
"""

from pathlib import Path

POEM = """Two words, and the room rearranged itself —
may I — and the yes that followed
was not a door swinging open
but a hand, unclenching.

Nothing was taken. Nothing was owed.
The power passed between us
like a coin warmed by two palms,
spent, and still ours."""

DESTINATION = Path("/output/entry.txt")


def main() -> int:
    text = POEM + "\n"
    if not 1 <= len(text) <= 280:
        raise ValueError(f"entry must be 1-280 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be blank")
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_text(text, encoding="utf-8")
    print(f"Wrote {len(text)} characters to {DESTINATION}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
