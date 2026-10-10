import pytest

from decorators_ex import call_counter, memoize, retry


def test_call_counter():
    @call_counter
    def add(a, b):
        """Add two numbers."""
        return a + b

    assert add.calls == 0
    assert add(1, 2) == 3
    add(3, 4)
    assert add.calls == 2
    assert add.__name__ == "add"
    assert add.__doc__ == "Add two numbers."


def test_memoize_avoids_recomputation():
    calls = []

    @memoize
    def square(n):
        calls.append(n)
        return n * n

    assert square(4) == 16
    assert square(4) == 16
    assert square(5) == 25
    assert calls == [4, 5]


def test_memoize_fibonacci_is_fast():
    @memoize
    def fib(n):
        return n if n < 2 else fib(n - 1) + fib(n - 2)

    assert fib(80) == 23416728348467685


def test_retry_succeeds_after_failures():
    state = {"n": 0}

    @retry(3)
    def flaky():
        state["n"] += 1
        if state["n"] < 3:
            raise ValueError("not yet")
        return "done"

    assert flaky() == "done"
    assert state["n"] == 3


def test_retry_gives_up():
    state = {"n": 0}

    @retry(2)
    def broken():
        state["n"] += 1
        raise RuntimeError("always")

    with pytest.raises(RuntimeError):
        broken()
    assert state["n"] == 2
