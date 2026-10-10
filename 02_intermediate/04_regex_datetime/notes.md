# Regular expressions and dates

## `re` essentials
- `re.search(pattern, s)` finds the first match; `re.findall` returns all matches as strings.
- Use raw strings (`r"\d+"`) so backslashes survive.
- Groups `( )` capture parts of a match; `(?P<name>...)` names them.
- `re.compile` once if you reuse a pattern.

## `datetime` essentials
- `date.fromisoformat("2024-03-15")` parses ISO dates; `datetime.strptime` handles custom formats.
- Subtracting two dates gives a `timedelta` (`.days`).
- `date.weekday()`: Monday is 0, Sunday is 6.

```python
import re
from datetime import date

re.findall(r"\d{4}-\d{2}-\d{2}", "from 2020-02-20 to 2020-03-23")
(date(2020, 3, 23) - date(2020, 2, 20)).days   # 32
```

## Exercises
Implement `regex_dates.py`, then `pytest 02_intermediate/04_regex_datetime`.
