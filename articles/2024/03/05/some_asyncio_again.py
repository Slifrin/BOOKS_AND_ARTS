import asyncio

async def mock_api_request(i):
    print(f"Api request started {i}")
    await asyncio.sleep(1)
    print(f"Api request completed {i}")

async def run():
    for i in range(1_000_000):
        await mock_api_request(i)

async def run_tasks():
    tasks = []
    for i in range(1_000_000):
        tasks.append(asyncio.create_task(mock_api_request(i)))
    await asyncio.wait(tasks)

async def run_batch():
    tasks = []
    batch_size = 1000
    for i in range(1_000_000):
        tasks.append(asyncio.create_task(mock_api_request(i)))
        if len(tasks) >= batch_size:
            await asyncio.wait(tasks)
            tasks = []

    if tasks:
        await asyncio.wait(tasks)

async def producer(queue: asyncio.Queue):
    for i in range(1_000_000):
        await queue.put(i)
    while not queue.full():
        await queue.put(None)

async def consumer(queue: asyncio.Queue):
    while True:
        item = await queue.get()
        if item in None:
            break
        await mock_api_request(item)

async def run_with_queue():
    queue = asyncio.Queue(maxsize=100)
    producer_task = asyncio.create_task(producer(queue))
    consumer_task = asyncio.create_task(consumer(queue))

    await asyncio.wait([producer_task, consumer_task])

async def run_with_queue_with_more_connsumers():
    queue = asyncio.Queue(maxsize=100)
    producer_task = asyncio.create_task(producer(queue))
    consumers = []
    for _ in range(10):
        consumer_task = asyncio.create_task(consumer(queue))
        consumers.append(consumer_task)

    await asyncio.wait([producer_task, *consumers])

async def producer_with_event(queue: asyncio.Queue, stop_event: asyncio.Event):
    for i in range(1_000_000):
        await queue.put(i)
    stop_event.set()

async def consumer_with_event(queue: asyncio.Queue, stop_event: asyncio.Event):
    while True:
        if queue.empty() and stop_event.is_set():
            break
        item = await queue.get()
        await mock_api_request(item)

async def run_with_queue_with_more_connsumers_and_event():
    queue = asyncio.Queue(maxsize=100)
    stop_event = asyncio.Event()
    producer_task = asyncio.create_task(producer_with_event(queue, stop_event))
    consumers = []
    for _ in range(10):
        consumer_task = asyncio.create_task(consumer_with_event(queue, stop_event))
        consumers.append(consumer_task)

    await asyncio.wait([producer_task, *consumers])

if __name__ == "__main__":
    asyncio.run(run_with_queue_with_more_connsumers())