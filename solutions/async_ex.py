import asyncio


async def slow_square(n: int, delay: float = 0.1) -> int:
    await asyncio.sleep(delay)
    return n * n


async def squares_concurrently(numbers: list[int]) -> list[int]:
    return list(await asyncio.gather(*(slow_square(n) for n in numbers)))


async def first_to_finish(delays: list[float]) -> float:
    async def sleeper(d):
        await asyncio.sleep(d)
        return d

    tasks = [asyncio.create_task(sleeper(d)) for d in delays]
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    for task in pending:
        task.cancel()
    return done.pop().result()
