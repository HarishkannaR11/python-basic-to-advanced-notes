import asyncio
import time

from async_ex import first_to_finish, slow_square, squares_concurrently


def test_slow_square():
    assert asyncio.run(slow_square(7, delay=0.01)) == 49


def test_squares_run_concurrently():
    start = time.perf_counter()
    result = asyncio.run(squares_concurrently(list(range(20))))
    elapsed = time.perf_counter() - start
    assert result == [n * n for n in range(20)]
    assert elapsed < 0.5  # sequential would take ~2 seconds


def test_first_to_finish():
    start = time.perf_counter()
    winner = asyncio.run(first_to_finish([0.3, 0.05, 0.2]))
    elapsed = time.perf_counter() - start
    assert winner == 0.05
    assert elapsed < 0.25
