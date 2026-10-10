# Decorators

## Key ideas
- Functions are objects: you can pass them around, return them, and wrap them.
- A decorator is a function that takes a function and returns a (usually wrapped) function.
  `@deco` above `def f` is shorthand for `f = deco(f)`.
- Always use `functools.wraps` so the wrapper keeps the original name and docstring.
- A decorator *with arguments* is a function that returns a decorator (three nested levels).

```python
import functools

def shout(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

@shout
def greet(name):
    return f"hello {name}"
```

## Exercises
Implement `decorators_ex.py`, then `pytest 03_advanced/01_decorators`.
