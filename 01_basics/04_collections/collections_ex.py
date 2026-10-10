def second_largest(nums: list[int]) -> int:
    """Return the second largest *distinct* value.
    Raise ValueError if there are fewer than two distinct values.
    """
    raise NotImplementedError


def unique_in_order(items: list) -> list:
    """Remove duplicates but keep the first occurrence order.
    unique_in_order([3, 1, 3, 2, 1]) -> [3, 1, 2]
    """
    raise NotImplementedError


def word_frequency(sentence: str) -> dict[str, int]:
    """Count words in a sentence, case-insensitively (split on whitespace)."""
    raise NotImplementedError


def invert_dict(d: dict) -> dict:
    """Swap keys and values: {"a": 1, "b": 2} -> {1: "a", 2: "b"}.
    Assume the values are unique and hashable.
    """
    raise NotImplementedError


def group_by_length(words: list[str]) -> dict[int, list[str]]:
    """Group words by their length, keeping input order inside each group.
    ["hi", "yo", "hey"] -> {2: ["hi", "yo"], 3: ["hey"]}
    """
    raise NotImplementedError


def common_elements(a: list, b: list) -> list:
    """Sorted list of the distinct values that appear in both lists (use sets)."""
    raise NotImplementedError
