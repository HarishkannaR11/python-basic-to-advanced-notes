from pathlib import Path


def word_count(path) -> dict[str, int]:
    """Return how often each word appears in the text file at `path`.

    Words are lowercase and split on whitespace; strip the punctuation
    characters `.,!?;:` from both ends of each word. Ignore empty words.
    """
    raise NotImplementedError


def csv_to_json(csv_path, json_path) -> int:
    """Read a CSV file with a header row and write its rows to `json_path`
    as a JSON list of objects (indent=2). Return the number of rows written.
    """
    raise NotImplementedError
