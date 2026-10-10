class ValidationError(Exception):
    """Raised when input fails validation."""


def safe_divide(a, b):
    """Return a / b, or None if b is zero."""
    raise NotImplementedError


def parse_age(value) -> int:
    """Convert `value` to int.

    Raise ValidationError if it cannot be converted to an int, or if the
    result is outside 0..150 (inclusive). Chain the original error with `from`.
    """
    raise NotImplementedError


def retry(func, attempts: int):
    """Call `func()` up to `attempts` times until it returns without raising.

    Return its result. If every attempt raises, re-raise the last exception.
    """
    raise NotImplementedError
