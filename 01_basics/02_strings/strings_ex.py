def reverse_string(s: str) -> str:
    """Return s reversed."""
    raise NotImplementedError


def is_palindrome(s: str) -> bool:
    """True if s reads the same forwards and backwards, ignoring case, spaces
    and punctuation. "A man, a plan, a canal: Panama" -> True
    """
    raise NotImplementedError


def count_vowels(s: str) -> int:
    """Count the vowels a, e, i, o, u (either case)."""
    raise NotImplementedError


def initials(full_name: str) -> str:
    """Return upper-case initials followed by dots: "ada king lovelace" -> "A.K.L."
    Extra spaces between words should be ignored.
    """
    raise NotImplementedError


def truncate(text: str, max_len: int) -> str:
    """If text is longer than max_len, cut it so the result (including a
    trailing "...") has exactly max_len characters. Otherwise return text as is.
    Assume max_len >= 3.  truncate("Hello, World", 8) -> "Hello..."
    """
    raise NotImplementedError
