"""example of __await__ usage"""
import asyncio
import sys


class LazyFetcher:
    def __init__(self, url: str) -> None:
        self.url = url

    def __await__(self):
        # 1. create a helper coroutine to do the actual async work
        async def _async_fetch():
            print(f"Starting fetch for {self.url}...")
            await asyncio.sleep(1.5)  # Simulate a 1.5-second network delay
            return f"Data from {self.url}"

        # 2. return the helper coroutine's underlying iterator
        return _async_fetch().__await__()



class CustomAwaitable:
    def __init__(self, value):
        self.value = value
    def __await__(self):
        # yield gives control back to the event loop
        yield  # this makes it a generator
        return self.value  # StopIteration value becomes the await result


class DatabaseConnection:
    def __init__(self, host):
        self.host = host
        self.connected = False
    def __await__(self):
        return self._connect().__await__()
    async def _connect(self):
        print(f"Connecting to {self.host}...")
        await asyncio.sleep(0.5)
        self.connected = True
        print("Connected!")
        return self


async def main() -> None:
    print(f'Hello main from : {__file__} executed by {sys.executable}')
    fetcher = LazyFetcher("https://api.example.com/items")

    result = await fetcher
    print(f"{result=}")

    obj = CustomAwaitable(42)
    result = await obj
    print(f"Got: {result=}")

    db = await DatabaseConnection("localhost:5432")
    print(f"Connection status: {db.connected}")

if __name__ == '__main__':
    asyncio.run(main())