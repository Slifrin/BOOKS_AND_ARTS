import asyncio


async def async_gen():
    for i in range(3):
        await asyncio.sleep(1)
        yield i * i


async def main() -> None:
    print(f'Hello main from : {__file__}')
    async for i in async_gen():
        print(i)

if __name__ == '__main__':
    asyncio.run(main=main())