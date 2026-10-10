# Threads, processes and the GIL

## Which tool for which problem?

| Workload | Best fit | Why |
|---|---|---|
| Many network/disk waits | `asyncio` or `ThreadPoolExecutor` | time is spent waiting, not computing |
| Heavy CPU work (maths, parsing) | `ProcessPoolExecutor` / `multiprocessing` | separate processes sidestep the GIL |
| Vectorisable numeric work | NumPy / pandas | the loop runs in C |

## The GIL
CPython lets only one thread execute Python bytecode at a time (the Global Interpreter Lock).
Threads still help for I/O, because the lock is released while waiting. They do **not** speed up
pure-Python CPU loops. (Free-threaded builds of Python 3.13+ are experimental.)

## The easy API: `concurrent.futures`

```python
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

with ThreadPoolExecutor(max_workers=8) as pool:
    results = list(pool.map(fetch, urls))

with ProcessPoolExecutor() as pool:
    results = list(pool.map(crunch, chunks))
```

## Hazards
- **Race conditions**: two threads mutate shared state. Protect it with `threading.Lock`, or avoid sharing.
- **Deadlocks**: two locks acquired in different orders.
- Processes need picklable arguments/results, and top-level functions.

## Practice
1. Time downloading 20 URLs sequentially vs `ThreadPoolExecutor` vs `asyncio` + `httpx`.
2. Time a CPU-heavy function (e.g. count primes below 2,000,000) with threads vs processes. Explain the result.
