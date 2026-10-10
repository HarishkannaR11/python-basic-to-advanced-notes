# asyncio

## Key ideas
- `async def` defines a coroutine; `await` pauses it until the awaited thing is ready, letting other tasks run.
- asyncio is *single-threaded concurrency*: great for waiting on I/O (network, files, sleeps), useless for heavy CPU work.
- `asyncio.run(main())` is the entry point. `asyncio.gather(*coros)` runs coroutines concurrently.
- Never call blocking functions (`time.sleep`, `requests.get`) inside a coroutine; use `await asyncio.sleep` or async libraries (`httpx`, `aiohttp`).
- `asyncio.TaskGroup` (3.11+) gives structured concurrency with proper error handling.

```python
import asyncio

async def job(n):
    await asyncio.sleep(1)
    return n

async def main():
    return await asyncio.gather(job(1), job(2), job(3))   # ~1 second total, not 3

asyncio.run(main())
```

## Exercises
Implement `async_ex.py`, then `pytest 03_advanced/05_async`.
