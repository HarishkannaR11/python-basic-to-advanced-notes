import pytest

from strings_ex import count_vowels, initials, is_palindrome, reverse_string, truncate


def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("") == ""


@pytest.mark.parametrize(
    "text, expected",
    [
        ("racecar", True),
        ("A man, a plan, a canal: Panama", True),
        ("hello", False),
        ("", True),
    ],
)
def test_is_palindrome(text, expected):
    assert is_palindrome(text) is expected


def test_count_vowels():
    assert count_vowels("Hello World") == 3
    assert count_vowels("AEIOU") == 5
    assert count_vowels("rhythm") == 0


def test_initials():
    assert initials("ada king lovelace") == "A.K.L."
    assert initials("  grace   hopper ") == "G.H."
    assert initials("plato") == "P."


def test_truncate():
    assert truncate("Hello, World", 8) == "Hello..."
    assert truncate("Short", 10) == "Short"
    assert truncate("exactly10!", 10) == "exactly10!"
    assert len(truncate("x" * 100, 20)) == 20
