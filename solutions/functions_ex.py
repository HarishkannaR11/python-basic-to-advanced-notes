def power(base: float, exponent: float = 2) -> float:
    return base**exponent


def average(*numbers: float) -> float:
    if not numbers:
        raise ValueError("average() needs at least one number")
    return sum(numbers) / len(numbers)


def describe(**details) -> str:
    return ", ".join(f"{key}={details[key]}" for key in sorted(details))


def make_multiplier(n: float):
    def multiply(x):
        return x * n

    return multiply


def apply_twice(func, value):
    return func(func(value))


def append_item(item, items=None) -> list:
    return [*(items or []), item]
