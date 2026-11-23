import sys
from pathlib import Path

ENTRY = "I keep telling myself 'later' so often it's started charging me rent."
MAX_CHARS = 200
DEFAULT_OUTPUT = Path("/output/entry.txt")


def validate(text: str) -> None:
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    if not text or not text.strip():
        raise ValueError("entry must contain non-whitespace text")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    size = len(text.encode("utf-8"))
    if len(text) > MAX_CHARS or size > MAX_CHARS:
        raise ValueError(
            f"entry must be at most {MAX_CHARS} characters, "
            f"got {len(text)} characters / {size} bytes"
        )


def write_entry(path: Path = DEFAULT_OUTPUT) -> str:
    validate(ENTRY)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(ENTRY.encode("utf-8"))
    return ENTRY


def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_OUTPUT
    write_entry(path)


if __name__ == "__main__":
    main()
