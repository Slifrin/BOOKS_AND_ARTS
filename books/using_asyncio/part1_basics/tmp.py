
import asyncio
import time

async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")


async def count2():
    print("One")
    asyncio.sleep(1)
    print("Two")

async def main():
    start = time.perf_counter()
    await asyncio.gather(count(), count(), count())
    print(f"Duration1 {time.perf_counter() - start}")
    print("-" * 80)
    start = time.perf_counter()
    await asyncio.gather(count2(), count2(), count2())
    print(f"Duration2 {time.perf_counter() - start}")

asyncio.run(main())