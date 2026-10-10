def power(base: float, exponent: float = 2) -> float:
    """Return base raised to exponent (default: square it)."""
    raise NotImplementedError


def average(*numbers: float) -> float:
    """Mean of any number of arguments. Raise ValueError if none are given."""
    raise NotImplementedError


def describe(**details) -> str:
    """Return "key=value" pairs joined by ", ", sorted by key.
    describe(name="Ada", age=36) -> "age=36, name=Ada"
    """
    raise NotImplementedError


def make_multiplier(n: float):
    """Return a function that multiplies its argument by n.
    double = make_multiplier(2); double(21) -> 42
    """
    raise NotImplementedError


def apply_twice(func, value):
    """Return func(func(value))."""
    raise NotImplementedError


def append_item(item, items=None) -> list:
    """Return a NEW list containing `items` (if given) followed by `item`.
    Calling append_item(1) twice must return [1] both times (no shared state).
    """
    raise NotImplementedError
