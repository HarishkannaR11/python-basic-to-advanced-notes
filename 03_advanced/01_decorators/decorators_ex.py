def call_counter(func):
    """Decorator: count calls. Expose the count as `wrapper.calls` (starts at 0).

    Must preserve the original function's `__name__` (use functools.wraps).
    """
    raise NotImplementedError


def memoize(func):
    """Decorator: cache results by positional arguments so repeated calls with
    the same arguments do not call `func` again."""
    raise NotImplementedError


def retry(times: int):
    """Decorator factory: call the function up to `times` times until it does
    not raise. Re-raise the last exception if every attempt fails.

    Usage:
        @retry(3)
        def flaky(): ...
    """
    raise NotImplementedError
