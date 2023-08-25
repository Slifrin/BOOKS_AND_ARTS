"""
    https://www.geeksforgeeks.org/desktop-notifier-python/?ref=lbp
"""
import pathlib
import datetime

import requests
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pprint import pprint

from plyer import notification


RSS_FEED_URL = "https://spidersweb.pl/api/post/feed/feed-gn"


def load_rss(feed_url: str) -> bytes:
    resp = requests.get(feed_url)
    return resp.content


def load_data():
    data_file = pathlib.Path(__file__).parent / "data.txt"

    if data_file.is_file():
        return data_file.read_bytes()

    data = load_rss(RSS_FEED_URL)
    data_file.write_bytes(data)
    return data


def parse_xml(rss_content: bytes):
    root = ET.fromstring(rss_content)

    for element in root:
        for i, child in enumerate(element):
            if child.tag == "item":
                new_entry = {
                    item.tag: item.text
                    for item in child
                    if item.tag in ["title", "link", "pubDate"]
                }
                new_entry["pubDate"] = datetime.datetime.strptime(
                    new_entry["pubDate"], "%a, %d %b %Y %H:%M:%S %z"
                )
                yield new_entry


def main() -> None:
    print(f"Hello main from : {__file__}")

    data = parse_xml(load_data())

    latest_news = max(data, key=lambda x: x["pubDate"])
    print(latest_news)
    if latest_news:
        notification.notify(
            title = "Latest news",
            message = f"{latest_news['title']}\n{str(latest_news['pubDate'])}\n{latest_news['link']}"
        )


if __name__ == "__main__":
    main()
