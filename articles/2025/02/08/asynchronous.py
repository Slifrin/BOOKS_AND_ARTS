
import asyncio
import sys
import time

async def fetch_data():
    print('Start fetching')
    await asyncio.sleep(2)
    print('Done fetching')
    return {'data': 1}


async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.25)



async def say_after(delay, word):
    await asyncio.sleep(delay)
    print(word)


async def main():
    print(f'Hello main from : {__file__} executed by {sys.executable}')

    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(print_numbers())

    value = await task1
    await task2
    print(value)

    async with asyncio.TaskGroup() as tg:
        task3 = tg.create_task(say_after(1, 'hello'))
        task4 = tg.create_task(say_after(2, 'world'))

        print(f'started at {time.strftime("%X")}')

    print(f'Finished at {time.strftime("%X")}')

    task5 = asyncio.create_task(fetch_data())
    await asyncio.sleep(1.1)
    task5.cancel()

    try:
        await task5
    except asyncio.CancelledError as err:
        print(err)
        print('Taske was already cnceled')

if __name__ == '__main__':
    asyncio.run(main())