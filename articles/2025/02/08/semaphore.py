"""
For concurrent access of some resources
"""

import asyncio
import sys

async def use_semaphore(semaphore: asyncio.Semaphore, name: str):
    async with semaphore:
        print(f'{name=} acuired the semaphore')
        await asyncio.sleep(0.5)

    print(f'{name=} released the semaphore')


async def main() -> None:
    print(f'Hello main from : {__file__} executed by {sys.executable}')
    semaphore = asyncio.Semaphore(2)
    await asyncio.gather(
        use_semaphore(semaphore, '1'),
        use_semaphore(semaphore, '2'),
        use_semaphore(semaphore, '3'),
        use_semaphore(semaphore, '4'),
    )

if __name__ == '__main__':
    asyncio.run(main())