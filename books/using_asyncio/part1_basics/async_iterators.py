import asyncio

from aioredis import create_redis


# synchronous iterator

class A:
    def __iter__(self):
        self.x = 0
        return self
    def __next__(self):
        if self.x > 2:
            raise StopIteration
        else:
            self.x += 1
            return self.x
for i in A():
    print(i)

# async iterators

async def main():
    redis = await create_redis(('localhost', 6379))
    keys = ['Americas', 'Africa', 'Europe', 'Asia']

    async for value in OneAtATime(redis, keys):
        await do_something_with(value)

class OneAtATime:
    def __init__(self, redis, keys):
        self.redis = redis
        self.keys = keys

    def __aiter__(self):
        self.ikeys = iter(self.keys)
        return self
    async def __anext__(self):
        try:
            k = next(self.keys)
        except StopIteration:
            raise StopAsyncIteration
        
        value = await self.redis.get(k)
        return value

asyncio.run(main())


# optional simpler version with async generator

async def one_at_a_time(redis, keys):
    for k in keys:
        value = await redis.get(k)
        yield value

