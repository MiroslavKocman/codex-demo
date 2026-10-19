"""Tiny, dependency-free text analyser for practising with Codex Cloud."""

import argparse
import json
import sys
from pathlib import Path


def analyse(text: str) -> dict[str, int]:
    """Count characters, words, logical lines, and case-insensitive unique words.

    Empty text has zero lines. A trailing newline does not add an empty line.
    Punctuation stays attached to words; this is intentionally a simple baseline.
    Unique words are compared using Unicode casefolding.
    """
    words = text.split()
    return {
        "characters": len(text),
        "words": len(words),
        "lines": len(text.splitlines()),
        "unique_words": len({word.casefold() for word in words}),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Count characters, words, lines and case-insensitive unique words."
    )
    parser.add_argument("--file", type=Path, help="Read a UTF-8 file instead of stdin.")
    args = parser.parse_args(argv)
    try:
        text = args.file.read_text(encoding="utf-8") if args.file else sys.stdin.read()
    except (OSError, UnicodeError) as error:
        print(f"Cannot read input: {error}", file=sys.stderr)
        return 1
    print(json.dumps(analyse(text), ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
