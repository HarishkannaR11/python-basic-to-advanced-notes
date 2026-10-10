# Object-oriented programming

## Key ideas
- A class bundles data (attributes) and behaviour (methods). `__init__` sets up a new instance.
- Inheritance: `class Savings(Account)` reuses and extends a parent; call `super().__init__(...)`.
- `@property` exposes a computed or protected attribute as if it were a plain one.
- Dunder methods let your objects work with operators and built-ins:
  `__repr__`, `__eq__`, `__add__`, `__len__`, `__abs__`, `__iter__`, ...
- Prefer composition ("has a") over deep inheritance ("is a") when in doubt.

```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
```

## Exercises
Implement `oop.py`, then `pytest 02_intermediate/03_oop`.
