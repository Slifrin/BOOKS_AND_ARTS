import asyncio
import itertools
import os
import random
import time


async def make_item(size: int = 5) -> str:
    return os.urandom(size).hex()


async def randsleep(caller=None) -> None:
    i = random.randint(0, 10)
    if caller:
        print("\033[35m" + f"{caller} sleeping for {i} seconds.")
    await asyncio.sleep(i)


async def produce(name: int, q:asyncio.Queue) -> None:
    n = random.randint(0, 10)
    for _ in itertools.repeat(None, n): # it is synchronus
        await randsleep(caller=f"Producer {name}")
        i = await make_item()
        t = time.perf_counter()
        await q.put((i, t))
        print("\033[36m" + f"Producer {name} added <{i}> to queue.")

async def consume(name: int, q:asyncio.Queue) -> None:
    while True:
        await randsleep(caller=f"Consumer {name}")
        i, t = await q.get()
        now = time.perf_counter()
        print("\033[91m" + f"Consumer {name} got elemnt <{i}> in {now-t:0.5f} seconds.")
        q.task_done()


async def main(nprod: int, ncon: int):
    q = asyncio.Queue()
    producers = [asyncio.create_task(produce(n, q)) for n in range(nprod)]
    consumers = [asyncio.create_task(consume(n, q)) for n in range(ncon)]
    await asyncio.gather(*producers)
    await q.join() # implicite await for consumers
    for c in consumers:
        c.cancel()


if __name__ == '__main__':
    import argparse
    random.seed(2137)
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--nprod", type=int, default=5)
    parser.add_argument("-c", "--ncon", type=int, default=10)
    ns = parser.parse_args()
    start = time.perf_counter()
    asyncio.run(main(**ns.__dict__))
    elapsed = time.perf_counter() - start
    print("\033[0m" + f"Program completed in {elapsed:0.5f} seconds.")