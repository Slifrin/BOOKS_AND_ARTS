import asyncio
import functools
import logging
import pathlib
import re
import sys
from typing import IO
import urllib.error
import urllib.parse

import aiofiles
import aiohttp
import aiohttp.http_exceptions
from aiohttp import ClientSession


logging.basicConfig(
    format="%(asctime)s %(levelname)s:%(name)s: %(message)s",
    level=logging.DEBUG,
    datefmt="%H:%M:%S",
    stream=sys.stderr
)

logger = logging.Logger(pathlib.Path(__file__).stem)
logging.getLogger("chardet.charsetprober").disabled = True
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
logger.addHandler(handler)

HREF_RE = re.compile(r'href="(.*?)"')


async def fetch_html(url: str, session: ClientSession, **kwargs) -> str:
    resp = await session.request(method="GET", url=url, **kwargs)
    resp.raise_for_status()
    logger.info("Got response [%s] for URL: %s", resp.status, url)
    html = await resp.text()
    return html


async def parse(url: str, session: ClientSession, **kwargs) -> set:
    found = set()
    try:
        html = await fetch_html(url, session, **kwargs)
    except (
        aiohttp.ClientError,
        aiohttp.http_exceptions.HttpProcessingError,
    ) as e:
        logger.error(
            "aiohttp exceptio for %s [%s]: %s",
            url,
            getattr(e, "status", None),
            getattr(e, "message", None),
        )
    except Exception as e:
        logger.exception("Non-aiohttp exception occured: %s", getattr(e, "__dict__", {}))
    else:
        for link in HREF_RE.findall(html):
            try:
                abslink = urllib.parse.urljoin(url, link)
            except (urllib.error.URLError, ValueError):
                logger.exception("Error parsing URL: %s", link)
            else:
                found.add(abslink)
        logger.info("Found %d links for %s", len(found), url)
    return found


async def write_one(file: IO, url: str, **kwargs) -> tuple[str, int]:
    res = await parse(url=url, **kwargs)
    if not res:
        return url, 0
    async with aiofiles.open(file, "a") as f:
        for p in res:
            await f.write(f"{url}\t{p}\n")
        logger.info("Wrote results for source URL: %s", url)
    return url, len(res)


async def bulk_crawl_and_write(file: IO, urls: set, **kwargs) -> None:
    async with ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(
                write_one(file=file, url=url, session=session, **kwargs)
            )
        values = await asyncio.gather(*tasks)
        print(type(values))
        print(values)
        href_number = functools.reduce(lambda x, y: x + y[1], values, 0)
        logger.info("Found %d href-s", href_number)


if __name__ == '__main__':
    assert sys.version_info >= (3, 7), "Script requires Python 3.7+"
    here: pathlib.Path = pathlib.Path(__file__).parent

    with open(here.joinpath("urls.txt")) as infile:
        urls = set(map(str.strip, infile))

    outpath = here.joinpath("foundurls.txt")
    with open(outpath, "w") as outfile:
        outfile.write("source_url\tparsed_url\n")

    logger.info("Running loop")
    asyncio.run(bulk_crawl_and_write(file=outpath, urls=urls))