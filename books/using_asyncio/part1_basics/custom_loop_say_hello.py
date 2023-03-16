import asyncio
import time




async def main() -> None:
    print(f"{time.ctime()} Hello!")
    await asyncio.sleep(1.0)
    print(f"{time.ctime()} Goodbye!")


if __name__ == '__main__':
    # this is what asyncio does with asyncio.run(<corutine>)
    loop = asyncio.get_event_loop()
    task = loop.create_task(main())

    loop.run_until_complete(task)
    print("After first loop start")

    pending = asyncio.all_tasks(loop=loop)
    for i, task in enumerate(pending):
        print(f"Canceling task {i} - {task}")
        task.cancel()
    print("After cancelling loop")

    group = asyncio.gather(*pending, return_exceptions=True)
    loop.run_until_complete(group)
    print("After secound start of the loop")
    loop.close()
