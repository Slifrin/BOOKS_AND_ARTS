import asyncio

from contextlib import contextmanager, asynccontextmanager


class Connection:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    async def __aenter__(self):
        self.conn = await get_conn(self.host, self.port)
        return self.conn
    async def __aexit__(self, exc_type, exc, tb):
        await self.conn.close()


@contextmanager
def web_page(url):
    data = download_webpage(url)
    try:
        yield data
    finally:
        update_stats(url)


with web_page('google.com') as data:
    process(data)

@asynccontextmanager
async def a_web_page(url):
    data = await download_webpage(url)
    try:
        yield data
    finally:
        await update_stats(url)

async with a_web_page('google.com') as data:
    process(data)


@asynccontextmanager
async def web_page_with_conversion_of_blocking_code(url):
    """
        To go around blocking calls in nonblocking code executor is needed
        it runs them in separate thread
    """
    loop = asyncio.get_event_loop()
    data = await loop.run_in_executor(
        None, blocking_download_web_page, url
    )

    try:
        yield data
    finally:
        await loop.run_in_executor(
            None, blocking_update_stats, url
        )

async with web_page_with_conversion_of_blocking_code('google.com') as data:
    process(data)


