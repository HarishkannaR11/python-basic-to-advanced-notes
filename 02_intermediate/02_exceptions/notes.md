# Exceptions

## Key ideas
- `try / except / else / finally`: `else` runs when nothing was raised, `finally` always runs.
- Catch the *narrowest* exception you can; never use a bare `except:`.
- Define your own exceptions by subclassing `Exception`.
- `raise NewError(...) from err` keeps the original cause visible in the traceback.
- EAFP ("easier to ask forgiveness than permission") is the Pythonic style: try it, handle failure.

```python
class ValidationError(Exception):
    pass

def parse_port(s):
    try:
        port = int(s)
    except ValueError as err:
        raise ValidationError(f"not a number: {s!r}") from err
    return port
```

## Exercises
Implement `exceptions_ex.py`, then `pytest 02_intermediate/02_exceptions`.
