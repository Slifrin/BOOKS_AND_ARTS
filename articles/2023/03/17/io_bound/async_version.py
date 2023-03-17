import time
import asyncio

import aiohttp

from typing import Callable

async def download_site(session: aiohttp.ClientSession , url):
    async with session.get(url) as response:
        print(f"Read {response.content_length} from {url}")


async def simpler_solution(urls):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(download_site(session, url))
        await asyncio.gather(*tasks, return_exceptions=True)


async def more_complex_one(urls): # I think
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            task = asyncio.ensure_future(download_site(session, url))
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)


def run_for_me(urls, func: Callable):
    start_time = time.time()
    asyncio.run(func(urls))
    duration = time.time() - start_time
    print(f"{func.__name__.upper()} Downloaded {len(urls)} in {duration}s")

def main() -> None:
    print(f'Hello main from : {__file__}')
    urls = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    run_for_me(urls, more_complex_one)
    # run_for_me(urls, simpler_solution)

if __name__ == '__main__':
    main()