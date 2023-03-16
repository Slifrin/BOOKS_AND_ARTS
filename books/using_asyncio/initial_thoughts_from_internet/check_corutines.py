import asyncio

async def inner():
    print('inner')
    return 1

async def outer():
    print('outer')
    await inner()

if __name__ == '__main__':
    asyncio.run(outer())