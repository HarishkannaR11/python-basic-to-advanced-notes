def celsius_to_fahrenheit(c: float) -> float:
    return c * 9 / 5 + 32


def is_even(n: int) -> bool:
    return n % 2 == 0


def swap(a, b):
    return b, a


def bmi(weight_kg: float, height_m: float) -> float:
    return round(weight_kg / height_m**2, 1)


def to_int_or_none(text: str):
    try:
        return int(text)
    except ValueError:
        return None
