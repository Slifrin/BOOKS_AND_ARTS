import asyncio

import sys


async def long_task():
    await asyncio.sleep(10)


async def handling_of_tasks(task):
    if not task.done():
        task.cancel(msg="tarapaty")
        try:
            await task
        except asyncio.CancelledError as e:
            print("Cancelled Error")
        except Exception as e:
            print("Other exception " + str(e))
        return 2
    return 1


async def main() -> None:
    print(f"Hello main from : {__file__} executed by {sys.executable}")


if __name__ == "__main__":
    asyncio.run(main())
