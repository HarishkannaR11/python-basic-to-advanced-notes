async def slow_square(n: int, delay: float = 0.1) -> int:
    """Wait `delay` seconds (without blocking other tasks), then return n * n."""
    raise NotImplementedError


async def squares_concurrently(numbers: list[int]) -> list[int]:
    """Compute slow_square for every number *concurrently* and return the
    results in the same order as the input."""
    raise NotImplementedError


async def first_to_finish(delays: list[float]) -> float:
    """Start one task per delay (each sleeps for that many seconds and returns
    its delay). Return the delay of whichever finishes first and cancel the rest."""
    raise NotImplementedError
