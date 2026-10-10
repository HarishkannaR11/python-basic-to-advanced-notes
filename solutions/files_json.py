import csv
import json
from collections import Counter
from pathlib import Path


def word_count(path) -> dict[str, int]:
    words = (w.strip(".,!?;:").lower() for w in Path(path).read_text().split())
    return dict(Counter(w for w in words if w))


def csv_to_json(csv_path, json_path) -> int:
    with open(csv_path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    Path(json_path).write_text(json.dumps(rows, indent=2))
    return len(rows)
