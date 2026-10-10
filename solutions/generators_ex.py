from itertools import islice


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def take(n, iterable):
    return list(islice(iterable, n))


def chunked(iterable, size):
    it = iter(iterable)
    while chunk := take(size, it):
        yield chunk


def running_mean(iterable):
    total = 0
    for count, value in enumerate(iterable, start=1):
        total += value
        yield total / count
