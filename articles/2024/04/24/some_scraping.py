"""
Some simple webscraping 
https://brightdata.com/blog/how-tos/web-scraping-with-python
https://bas.codes/posts/py-webscraping-brightdata
"""

import requests

from bs4 import BeautifulSoup
from scrapy.selector import Selector
from lxml import html as lxhtml


def get_html(url):
    response = requests.get(url)  # can add proxy servers here
    assert response.status_code == 200
    html = response.text
    return html


def get_social_xpath():
    return ""


def meta_info(url, soup=None):
    print("Hello meta_info")
    if not soup:
        html = get_html(url)
        soup = BeautifulSoup(html, features="lxml")
    tree = lxhtml.fromstring(html)
    # social_paths = tree.xpath(get_social_xpath())
    # for leaf in social_paths:
    #     href = leaf.attrib.get("href")
    #     yield "body", href

def some_function():
    print("Hello there")


def main() -> None:
    print(f"Hello main from : {__file__}")
    meta_info("https://bas.bio")
    some_function()

if __name__ == "__main__":
    main()
