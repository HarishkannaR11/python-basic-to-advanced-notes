# Functions

```python
def greet(name, greeting="Hello"):
    """Return a greeting."""
    return f"{greeting}, {name}!"

greet("Ada")                        # positional
greet("Ada", greeting="Hi")         # keyword
```

## Key ideas
- `return` ends the function; without it you get `None`.
- **Default arguments** are evaluated once. Never use a mutable default (`def f(x=[])`);
  use `None` and create the list inside.
- `*args` collects extra positional arguments into a tuple; `**kwargs` collects keyword
  arguments into a dict.
- Variables assigned inside a function are **local**. Reading a global is fine; avoid changing globals.
- Functions are values: you can pass them as arguments (`sorted(words, key=len)`) and return them.
- Write a one-line docstring for every function. Keep functions small and single-purpose.

```python
def total(*nums):
    return sum(nums)

total(1, 2, 3)                      # 6

def make_multiplier(n):
    def multiply(x):
        return x * n                # remembers n (a closure)
    return multiply

double = make_multiplier(2)
double(21)                          # 42
```

## Exercises
Implement `functions_ex.py`, then `pytest 01_basics/05_functions`.
