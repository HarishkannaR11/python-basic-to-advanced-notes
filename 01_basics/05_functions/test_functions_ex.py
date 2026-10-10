import pytest

from functions_ex import append_item, apply_twice, average, describe, make_multiplier, power


def test_power():
    assert power(3) == 9
    assert power(2, 10) == 1024
    assert power(base=5, exponent=0) == 1


def test_average():
    assert average(1, 2, 3, 4) == 2.5
    assert average(10) == 10


def test_average_no_args():
    with pytest.raises(ValueError):
        average()


def test_describe():
    assert describe(name="Ada", age=36) == "age=36, name=Ada"
    assert describe() == ""


def test_make_multiplier():
    double, triple = make_multiplier(2), make_multiplier(3)
    assert double(21) == 42
    assert triple(5) == 15


def test_apply_twice():
    assert apply_twice(lambda x: x + 3, 10) == 16
    assert apply_twice(str.upper, "ab") == "AB"


def test_append_item_no_shared_state():
    assert append_item(1) == [1]
    assert append_item(1) == [1]
    assert append_item(3, [1, 2]) == [1, 2, 3]


def test_append_item_does_not_mutate_input():
    original = [1, 2]
    append_item(3, original)
    assert original == [1, 2]
