import asyncio

async def mock_api_request(i):
    print(f"Api request started {i}")
    await asyncio.sleep(1)
    print(f"Api request completed {i}")


async def producer_with_event(queue: asyncio.Queue, stop_event: asyncio.Event):
    for i in range(20):
        await queue.put(i)
    stop_event.set()

async def consumer_with_event(queue: asyncio.Queue, stop_event: asyncio.Event):
    while True:
        if queue.empty() and stop_event.is_set():
            break
        item = await queue.get()
        await mock_api_request(item)

async def tasks_with_queue():
    queue = asyncio.Queue(maxsize=2)
    stop_event = asyncio.Event()
    producer_task = asyncio.create_task(producer_with_event(queue, stop_event))
    consumers = []
    for _ in range(10):
        consumer_task = asyncio.create_task(consumer_with_event(queue, stop_event))
        consumers.append(consumer_task)
    print("Before sleep")
    await asyncio.sleep(1)
    print("After sleep")
    await asyncio.wait([producer_task, *consumers])

if __name__ == "__main__":
    asyncio.run(tasks_with_queue())