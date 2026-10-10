# Comprehensions

A compact, readable way to build a list, dict or set from another iterable.

```python
nums = [1, 2, 3, 4, 5, 6]

[n * n for n in nums]                    # [1, 4, 9, 16, 25, 36]
[n for n in nums if n % 2 == 0]          # [2, 4, 6]
{w: len(w) for w in ["hi", "hello"]}     # {'hi': 2, 'hello': 5}
{n % 3 for n in nums}                    # {0, 1, 2}
[(x, y) for x in "ab" for y in (1, 2)]   # nested loops: left to right
[row[0] for row in [[1, 2], [3, 4]]]     # [1, 3]
```

Pattern: `[expression for item in iterable if condition]`.

## Tips
- If it doesn't fit comfortably on one or two lines, use a normal `for` loop.
- Use a **generator expression** `(x for x in ...)` when you only need to loop once or feed it to
  `sum`, `max`, `any`, `all`. It doesn't build the whole list in memory.
- `any(x > 5 for x in nums)` and `all(...)` are comprehension's best friends.

## Exercises
Implement `comprehensions_ex.py`, then `pytest 01_basics/06_comprehensions`.
