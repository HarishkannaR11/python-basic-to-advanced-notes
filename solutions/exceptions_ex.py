class ValidationError(Exception):
    """Raised when input fails validation."""


def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None


def parse_age(value) -> int:
    try:
        age = int(value)
    except (ValueError, TypeError) as err:
        raise ValidationError(f"invalid age: {value!r}") from err
    if not 0 <= age <= 150:
        raise ValidationError(f"age out of range: {age}")
    return age


def retry(func, attempts: int):
    last = None
    for _ in range(attempts):
        try:
            return func()
        except Exception as err:
            last = err
    raise last
