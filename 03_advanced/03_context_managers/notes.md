# Context managers

## Key ideas
- `with` guarantees setup and cleanup around a block, even if an exception occurs.
- Class-based: implement `__enter__` and `__exit__(self, exc_type, exc, tb)`.
  Returning `True` from `__exit__` suppresses the exception.
- Function-based: `@contextlib.contextmanager` turns a generator with one `yield` into one.
  Put cleanup in `try / finally` around the `yield`.
- Handy stdlib ones: `open`, `threading.Lock`, `contextlib.suppress`, `tempfile.TemporaryDirectory`.

```python
from contextlib import contextmanager

@contextmanager
def announce(name):
    print("start", name)
    try:
        yield
    finally:
        print("end", name)
```

## Exercises
Implement `context_managers_ex.py`, then `pytest 03_advanced/03_context_managers`.
