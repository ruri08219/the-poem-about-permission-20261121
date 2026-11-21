"""the-poem-about-permission-20261121 — one short poem about agency.

The entry is a poem about the power to ask and to be given. Two words
rearrange the room; the yes that follows is not a door swinging open but
a hand, unclenching. Nothing is taken, nothing is owed — the power passes
between asker and giver like a coin warmed by two palms: spent, and still
ours. The poem is fixed text, written here in full, so the program is
deterministic and needs no network: it simply writes the poem to
/output/entry.txt, exactly as the competition requires (1-280 characters).
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
    """Write the poem to /output/entry.txt and report its length."""
    text = POEM + "\n"
    code_points = len(text)
    if not 1 <= code_points <= 280:
        raise ValueError(f"poem must be 1-280 characters, got {code_points}")
    if not text.strip():
        raise ValueError("poem must not be only white space")
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_text(text, encoding="utf-8")
    print(f"Wrote {code_points} characters to {DESTINATION}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
