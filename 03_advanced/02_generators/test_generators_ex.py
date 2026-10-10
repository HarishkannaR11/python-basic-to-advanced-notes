import inspect

from generators_ex import chunked, fibonacci, running_mean, take


def test_fibonacci_is_lazy_generator():
    assert inspect.isgenerator(fibonacci())


def test_fibonacci_values():
    assert take(10, fibonacci()) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


def test_take_short_iterable():
    assert take(5, [1, 2]) == [1, 2]
    assert take(0, [1, 2]) == []


def test_chunked():
    assert list(chunked(range(5), 2)) == [[0, 1], [2, 3], [4]]
    assert list(chunked([], 3)) == []


def test_chunked_works_on_infinite_input():
    gen = chunked(fibonacci(), 3)
    assert next(gen) == [0, 1, 1]
    assert next(gen) == [2, 3, 5]


def test_running_mean():
    assert list(running_mean([2, 4, 6])) == [2.0, 3.0, 4.0]
    assert list(running_mean([])) == []
