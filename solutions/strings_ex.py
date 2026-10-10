def reverse_string(s: str) -> str:
    return s[::-1]


def is_palindrome(s: str) -> bool:
    cleaned = [ch.lower() for ch in s if ch.isalnum()]
    return cleaned == cleaned[::-1]


def count_vowels(s: str) -> int:
    return sum(1 for ch in s.lower() if ch in "aeiou")


def initials(full_name: str) -> str:
    return "".join(word[0].upper() + "." for word in full_name.split())


def truncate(text: str, max_len: int) -> str:
    if len(text) <= max_len:
        return text
    return text[: max_len - 3] + "..."
