import pytest

from collections_ex import (
    common_elements,
    group_by_length,
    invert_dict,
    second_largest,
    unique_in_order,
    word_frequency,
)


def test_second_largest():
    assert second_largest([3, 1, 4, 1, 5]) == 4
    assert second_largest([5, 5, 4]) == 4


def test_second_largest_errors():
    with pytest.raises(ValueError):
        second_largest([7])
    with pytest.raises(ValueError):
        second_largest([2, 2, 2])


def test_unique_in_order():
    assert unique_in_order([3, 1, 3, 2, 1]) == [3, 1, 2]
    assert unique_in_order([]) == []
    assert unique_in_order(list("banana")) == ["b", "a", "n"]


def test_word_frequency():
    assert word_frequency("the cat The dog the") == {"the": 3, "cat": 1, "dog": 1}
    assert word_frequency("") == {}


def test_invert_dict():
    assert invert_dict({"a": 1, "b": 2}) == {1: "a", 2: "b"}


def test_group_by_length():
    assert group_by_length(["hi", "yo", "hey", "a"]) == {2: ["hi", "yo"], 3: ["hey"], 1: ["a"]}


def test_common_elements():
    assert common_elements([1, 2, 2, 3, 4], [4, 3, 3, 9]) == [3, 4]
    assert common_elements([1], [2]) == []
