import os
import time
from contextlib import contextmanager


class Timer:
    def __enter__(self):
        self._start = time.perf_counter()
        self.elapsed = None
        return self

    def __exit__(self, exc_type, exc, tb):
        self.elapsed = time.perf_counter() - self._start
        return False


@contextmanager
def suppress_errors(*exception_types):
    try:
        yield
    except exception_types:
        pass


@contextmanager
def cd(path):
    previous = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(previous)
