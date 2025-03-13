import asyncio
import sys


async def locked_task(lock, msg):
    async with lock:
        print(f'{msg} has the lock')
        await asyncio.sleep(1)

    print(f'{msg} relaeased lock')


async def main() -> None:
    print(f'Hello main from : {__file__} executed by {sys.executable}')
    lock = asyncio.Lock()
    await asyncio.gather(
        locked_task(lock, 'First'),
        locked_task(lock, 'Second'),
    )


if __name__ == '__main__':
    asyncio.run(main())