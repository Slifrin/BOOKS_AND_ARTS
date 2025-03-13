from scrapy import Request, Spider


class FtpSpider(Spider):
    name = "mozilla"

    def start_requests(self):
        yield Request('ftp://ftp.mozilla.org/pub/mozilla.org/firefox/releases/README',
                      meta={'ftp_user': 'anonymous', 'ftp_password': ''}, callback=self.parse,)
        
    def parse(self, response):
        print(response.body)
