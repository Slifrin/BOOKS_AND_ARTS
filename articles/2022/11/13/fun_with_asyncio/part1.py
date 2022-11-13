"""
    https://www.youtube.com/watch?v=2IW-ZEui4h4
"""
from datetime import datetime
from typing import Any, Awaitable

import asyncio


async def run_sequence(*functions: Awaitable[Any]) -> None:
    print(functions)
    for function in functions:
        print("Run sequence")
        await function

async def run_parallel(*functions: Awaitable[Any]) -> None:
    await asyncio.gather(*functions)

async def call_some_f(index):
    await asyncio.sleep(0.5)
    return index

async def done_callback_fun(element):
    print(f"Finished task number {element}")


async def parallel_version():
    start = datetime.now()
    L = await asyncio.gather(*[call_some_f(i) for i in range(5)])
    end = datetime.now()
    print(L)
    print("execution time: ", end - start)

async def main() -> None:
    print(f'Hello main from : {__file__}')
    await parallel_version()

    await run_sequence(call_some_f(1), call_some_f(2))

    print(type(call_some_f))
    print(type(call_some_f(1)))


if __name__ == '__main__':
    asyncio.run(main())