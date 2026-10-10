# Files, JSON and CSV

## Key ideas
- Always open files with a `with` block so they close even on errors.
- Use `pathlib.Path` instead of string paths: `Path("data") / "file.txt"`.
- `json.load` / `json.dump` work on files; `json.loads` / `json.dumps` work on strings.
- `csv.DictReader` gives you one dict per row, keyed by the header.

```python
from pathlib import Path
import csv, json

text = Path("notes.txt").read_text(encoding="utf-8")

with open("prices.csv", newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

Path("out.json").write_text(json.dumps(rows, indent=2))
```

## Exercises
Implement the functions in `files_json.py`, then run:

```bash
pytest 02_intermediate/01_files_json_csv
```
