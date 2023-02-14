import requests
import time
import re
import os

import cProfile
import pstats

from pprint import pprint

import httpx
import asyncio


# usage of snakeviz

def count_https_in_web_pages():
    dirname = os.path.dirname(__file__)
    print(dirname)
    with open(os.path.join(dirname, 'topWebsites.txt'), 'r', encoding='utf-8') as f:
        urls = [line.strip() for line in f.readlines()]

    htmls = []
    for url in urls:
        htmls = htmls + [requests.get(url).text]

    count_https = 0
    count_http = 0
    for html in htmls:
        count_https += len(re.findall("https://", html))
        count_http += len(re.findall("http://", html))

    print('finished parsing')
    time.sleep(2.0)
    print(f'{count_https=}')
    print(f'{count_http=}')
    print(f'{count_https/count_http=}')


async def better_count_https_in_web_pages():
    dirname = os.path.dirname(__file__)
    print(dirname)
    with open(os.path.join(dirname, 'topWebsites.txt'), 'r', encoding='utf-8') as f:
        urls = [line.strip() for line in f.readlines()]

    async with httpx.AsyncClient() as client:
        tasks = (client.get(url) for url in urls)
        reqs = await asyncio.gather(*tasks)

    htmls = [req.text for req in reqs]

    count_https = 0
    count_http = 0
    for html in htmls:
        count_https += len(re.findall("https://", html))
        count_http += len(re.findall("http://", html))

    print('finished parsing')

    print(f'{count_https=}')
    print(f'{count_http=}')
    print(f'{count_https/count_http=}')


def initial_code():
    start = time.perf_counter()
    count_https_in_web_pages()
    elapsed = time.perf_counter() - start
    print(f'Done in {elapsed:.2f}s')


def add_some_profiling():
    with cProfile.Profile() as pr:
        count_https_in_web_pages()
    
    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    # stats.print_stats()
    profiling_info_file = os.path.join(os.path.dirname(__file__), "progfiling_data.prof")
    stats.dump_stats(filename=profiling_info_file)


def add_some_profiling_for_better_f():

    start = time.perf_counter()
    with cProfile.Profile() as pr:
        asyncio.run(better_count_https_in_web_pages())

    elapsed = time.perf_counter() - start
    print(f'Done in {elapsed:.2f}s')

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    # stats.print_stats()
    # profiling_info_file = os.path.join(os.path.dirname(__file__), "progfiling_data.prof")
    # stats.dump_stats(filename=profiling_info_file)

def main() -> None:
    print(f'Hello main from : {__file__}')
    add_some_profiling_for_better_f()

if __name__ == '__main__':
    main()