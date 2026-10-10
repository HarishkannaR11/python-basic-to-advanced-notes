def squares_of_evens(nums: list[int]) -> list[int]:
    """Squares of only the even numbers, in order. [1, 2, 3, 4] -> [4, 16]"""
    raise NotImplementedError


def word_lengths(words: list[str]) -> dict[str, int]:
    """Map each word to its length."""
    raise NotImplementedError


def flatten(matrix: list[list]) -> list:
    """Flatten a list of lists one level. [[1, 2], [3]] -> [1, 2, 3]"""
    raise NotImplementedError


def transpose(matrix: list[list]) -> list[list]:
    """Swap rows and columns. [[1, 2, 3], [4, 5, 6]] -> [[1, 4], [2, 5], [3, 6]]"""
    raise NotImplementedError


def has_negative(nums: list[int]) -> bool:
    """True if any number is negative (use any() with a generator expression)."""
    raise NotImplementedError


def pairs_summing_to(nums: list[int], target: int) -> list[tuple[int, int]]:
    """All pairs (a, b) from nums where a comes before b in the list and
    a + b == target. Use one comprehension with two loops over indexes.
    pairs_summing_to([1, 2, 3, 4], 5) -> [(1, 4), (2, 3)]
    """
    raise NotImplementedError
