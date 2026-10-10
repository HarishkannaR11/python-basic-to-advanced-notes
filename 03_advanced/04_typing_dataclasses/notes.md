# Type hints and dataclasses

## Type hints
- Hints document intent and let tools (`mypy`, `pyright`, your editor) catch bugs. They are not enforced at runtime.
- Modern syntax: `list[int]`, `dict[str, float]`, `int | None`, `Callable[[int], str]`.
- `Protocol` describes "anything with these methods" (structural typing).

## Dataclasses
- `@dataclass` generates `__init__`, `__repr__`, `__eq__` from annotated fields.
- `frozen=True` makes instances immutable (and hashable).
- Mutable defaults need `field(default_factory=list)`, never `= []`.
- `__post_init__` runs after `__init__` for validation.

```python
from dataclasses import dataclass, field

@dataclass(frozen=True)
class Point:
    x: float
    y: float = 0.0

@dataclass
class Path:
    points: list[Point] = field(default_factory=list)
```

## Exercises
Implement `models.py` (a tiny portfolio model), then `pytest 03_advanced/04_typing_dataclasses`.
