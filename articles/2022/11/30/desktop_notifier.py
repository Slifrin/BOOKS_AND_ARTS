"""
    https://www.geeksforgeeks.org/desktop-notifier-python/?ref=lbp
"""
import pathlib

import requests
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pprint import pprint


RSS_FEED_URL = 'https://spidersweb.pl/api/post/feed/feed-gn'

def load_rss(feed_url: str) -> bytes:
    resp = requests.get(feed_url)
    return resp.content

def load_data():
    
    data_file = pathlib.Path(__file__).parent / 'data.txt'

    if data_file.is_file():
        return data_file.read_bytes()

    data = load_rss(RSS_FEED_URL)
    data_file.write_bytes(data)
    return data


def parse_xml(rss_content:bytes):
    root = ET.fromstring(rss_content)
    pprint(root.findall('./channel/item'))

    for element in root:
        print(element)
        for i, child in enumerate(element):
            if child.tag == 'item':
                for ch in child:
                    pprint(ch)

                return


def main() -> None:
    print(f'Hello main from : {__file__}')
    parse_xml(load_data())


if __name__ == '__main__':
    main()