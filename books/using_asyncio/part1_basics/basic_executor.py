import time
import asyncio

async def main() -> None:
    print(f"{time.ctime()} Hello!")
    await asyncio.sleep(1.0)
    print(f"{time.ctime()} Goodbye!")


def blocking():
    """
    blocking() calls the traditional time.sleep() internally, which would have
    blocked the main thread and prevented your event loop from running. This
    means that you must not make this function a coroutine—indeed, you cannot
    even call this function from anywhere in the main thread, which is where the
    asyncio loop is running. We solve this problem by running this function in an
    executor.
    """
    time.sleep(0.5)
    print(f"{time.ctime()} Hello from a thread!")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    task = loop.create_task(main())

    loop.run_in_executor(None, blocking) # calling in executor
    loop.run_until_complete(task)

    pending = asyncio.all_tasks(loop=loop)
    for task in pending:
        task.cancel()
    
    group = asyncio.gather(*pending, return_exceptions=True)
    loop.run_until_complete(group)
    loop.close()