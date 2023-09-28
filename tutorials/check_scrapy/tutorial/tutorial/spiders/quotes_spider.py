from pathlib import Path

import scrapy
from scrapy.http.response.html import HtmlResponse


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            "https://quotes.toscrape.com/page/1/",
            # "https://quotes.toscrape.com/page/2/",
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # page = response.url.split("/")[-2]
        # filename = f"quotes-{page}.html"
        # Path(filename).write_bytes(response.body)
        # self.log(f"Saved file {filename}")

        print("hello there", type(response))

        for quote in response.css("div.quote"):
            yield {
                "text": quote.css("span.text::text").get(),
                "author": quote.css("small.author::text").get(),
                "tags": quote.css("div.tags a.tag::text").getall(),
            }

        next_page = response.css("li.next a::attr(href)").get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)


class SimplerQuotesSpider(scrapy.Spider):
    name = "simpler_quotes"
    start_urls = [
        "https://quotes.toscrape.com/page/1/",
        "https://quotes.toscrape.com/page/2/",
    ]

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"quotes-{page}-from-simpler-spider.html"
        Path(filename).write_bytes(response.body)


class CrawlinQuotedSpider(scrapy.Spider):
    name = "crawling_quotes"

    start_urls = [
        "https://quotes.toscrape.com/page/1/",
    ]

    def parse(self, response: HtmlResponse):
        for quote in response.css("div.quote"):
            yield {
                "text": quote.css("span.text::text").get(),
                "author": quote.css("small.author::text").get(),
                "tags": quote.css("div.tags a.tag::text").getall(),
            }

        href_next_page = response.css("ul.pager a::attr(href)")
        self.log(f"Hello again {href_next_page}")
        next_page = response.css("li.next a::attr(href)").get()
        if next_page:
            """This is a shortcut for creation of Requests
            Unlike scrapy.Request, response.follow supports relative URLs directly - no need
            to call urljoin. Note that response.follow just returns a Request instance; you
            still have to yield this Request.
            """
            yield response.follow(next_page, callback=self.parse)


class AuthorSpider(scrapy.Spider):
    name = "author"

    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response: HtmlResponse):
        author_page_links = response.css(".author + a")
        yield from response.follow_all(author_page_links, self.parse_author)

        pagination_links = response.css("li.next a")
        yield from response.follow_all(pagination_links, self.parse)

    def parse_author(self, response: HtmlResponse):
        def extract_with_css(query):
            return response.css(query).get(default="").strip()

        yield {
            "name": extract_with_css("h3.author-title::text"),
            "birthdate": extract_with_css(".author-born-date::text"),
            "bio": extract_with_css(".author-description::text"),
        }


class QuotedSpiderWithTags(scrapy.Spider):
    name = "quotes_with_tags"

    def start_requests(self):
        url = "https://quotes.toscrape.com/"
        tag = getattr(self, "tag", None)
        if tag is not None:
            url = f"{url}tag/{tag}"

        yield scrapy.Request(url, self.parse)

    def parse(self, response: HtmlResponse):
        for quote in response.css("div.quote"):
            yield {
                "text": quote.css("span.text::text").get(),
                "author": quote.css("small.author::text").get(),
            }

            next_page = response.css("li.next a::attr(href)").get()
            if next_page is not None:
                yield response.follow(next_page, self.parse)
