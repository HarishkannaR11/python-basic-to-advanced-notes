def fizzbuzz(n: int) -> list[str]:
    """Return a list for 1..n: "Fizz" for multiples of 3, "Buzz" for multiples
    of 5, "FizzBuzz" for both, otherwise the number as a string.
    """
    raise NotImplementedError


def sum_of_multiples(limit: int) -> int:
    """Sum of all numbers below `limit` that are multiples of 3 or 5."""
    raise NotImplementedError


def is_prime(n: int) -> bool:
    """True if n is a prime number (n < 2 is not prime)."""
    raise NotImplementedError


def collatz_steps(n: int) -> int:
    """Count steps to reach 1: if n is even, n = n // 2, else n = 3n + 1.
    collatz_steps(6) -> 8   (6,3,10,5,16,8,4,2,1)
    Assume n >= 1.
    """
    raise NotImplementedError


def grade(score: int) -> str:
    """90+ -> "A", 80-89 -> "B", 70-79 -> "C", 60-69 -> "D", else "F"."""
    raise NotImplementedError
