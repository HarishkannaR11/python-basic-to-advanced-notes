import pytest

from variables_ex import bmi, celsius_to_fahrenheit, is_even, swap, to_int_or_none


@pytest.mark.parametrize("c, f", [(0, 32), (100, 212), (-40, -40), (37, 98.6)])
def test_celsius_to_fahrenheit(c, f):
    assert celsius_to_fahrenheit(c) == pytest.approx(f)


def test_is_even():
    assert is_even(4) is True
    assert is_even(7) is False
    assert is_even(0) is True
    assert is_even(-2) is True


def test_swap():
    assert swap(1, 2) == (2, 1)
    assert swap("a", [1]) == ([1], "a")


def test_bmi():
    assert bmi(70, 1.75) == 22.9
    assert bmi(90, 1.8) == 27.8


def test_to_int_or_none():
    assert to_int_or_none("42") == 42
    assert to_int_or_none("-7") == -7
    assert to_int_or_none("4x") is None
    assert to_int_or_none("") is None
    assert to_int_or_none("3.5") is None
