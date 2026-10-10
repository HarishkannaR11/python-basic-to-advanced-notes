class Timer:
    """Class-based context manager that measures wall-clock time.

    with Timer() as t:
        ...
    t.elapsed  # seconds (float) the block took; set when the block exits
    """

    def __enter__(self):
        raise NotImplementedError

    def __exit__(self, exc_type, exc, tb):
        raise NotImplementedError


def suppress_errors(*exception_types):
    """Context manager (build it with @contextlib.contextmanager) that swallows
    the given exception types and lets any other exception propagate."""
    raise NotImplementedError


def cd(path):
    """Context manager (generator-based): temporarily change the working
    directory to `path`, and always restore the previous one afterwards."""
    raise NotImplementedError
