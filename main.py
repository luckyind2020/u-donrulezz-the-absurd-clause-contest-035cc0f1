"""Emit the absurd ToS clause for The Absurd Clause Contest."""

from pathlib import Path


def load_clause(path: str = "entry.txt") -> str:
    return Path(path).read_text(encoding="utf-8").strip()


def check_clause(clause: str, limit: int = 200) -> str:
    """Keep the clause inside the contest gate: 1 to `limit` characters."""
    if not clause:
        raise ValueError("clause is empty")
    if len(clause) > limit:
        raise ValueError(f"clause is {len(clause)} chars, over the {limit} limit")
    return clause


def main() -> None:
    print(check_clause(load_clause()))


if __name__ == "__main__":
    main()
