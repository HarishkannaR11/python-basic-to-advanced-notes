# Iterators and generators

## Key ideas
- An *iterable* can produce an iterator (`iter(x)`); an *iterator* yields values via `next()`
  and raises `StopIteration` when done. A `for` loop does this for you.
- A *generator function* uses `yield`; calling it returns a lazy iterator. It runs only as far
  as needed, so it can represent infinite or huge sequences with tiny memory.
- Generator expressions: `(x * x for x in range(10))`.
- `itertools` (`islice`, `chain`, `groupby`, `accumulate`, `tee`) composes iterators.
- `yield from other` delegates to another iterable.

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

list(countdown(3))   # [3, 2, 1]
```

## Exercises
Implement `generators_ex.py`, then `pytest 03_advanced/02_generators`.
