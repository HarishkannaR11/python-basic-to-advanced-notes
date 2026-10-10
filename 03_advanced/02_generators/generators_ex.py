def fibonacci():
    """Infinite generator: 0, 1, 1, 2, 3, 5, 8, ..."""
    raise NotImplementedError


def take(n, iterable):
    """Return a list of the first `n` items of any iterable (works on infinite ones)."""
    raise NotImplementedError


def chunked(iterable, size):
    """Yield lists of length `size` from `iterable`; the last may be shorter.

    chunked(range(5), 2) -> [0, 1], [2, 3], [4]
    """
    raise NotImplementedError


def running_mean(iterable):
    """Yield the running mean after each item.

    running_mean([2, 4, 6]) -> 2.0, 3.0, 4.0
    """
    raise NotImplementedError
