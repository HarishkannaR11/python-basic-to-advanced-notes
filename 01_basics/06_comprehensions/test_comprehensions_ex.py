from comprehensions_ex import (
    flatten,
    has_negative,
    pairs_summing_to,
    squares_of_evens,
    transpose,
    word_lengths,
)


def test_squares_of_evens():
    assert squares_of_evens([1, 2, 3, 4]) == [4, 16]
    assert squares_of_evens([1, 3]) == []


def test_word_lengths():
    assert word_lengths(["hi", "hello"]) == {"hi": 2, "hello": 5}


def test_flatten():
    assert flatten([[1, 2], [3], []]) == [1, 2, 3]


def test_transpose():
    assert transpose([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]


def test_has_negative():
    assert has_negative([3, -1, 2]) is True
    assert has_negative([0, 1]) is False
    assert has_negative([]) is False


def test_pairs_summing_to():
    assert pairs_summing_to([1, 2, 3, 4], 5) == [(1, 4), (2, 3)]
    assert pairs_summing_to([2, 2, 2], 4) == [(2, 2), (2, 2), (2, 2)]
    assert pairs_summing_to([1], 2) == []
