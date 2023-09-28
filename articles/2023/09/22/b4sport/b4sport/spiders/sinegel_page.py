from pathlib import Path
from typing import Iterable

import scrapy
from scrapy.http import Request
from scrapy.http.response.html import HtmlResponse

base_url = 'https://wyniki.b4sport.pl/'

class b4Sport(scrapy.Spider):

    name = 'b4sport'

    def start_requests(self) -> Iterable[Request]:
        urls = [
            'https://wyniki.b4sport.pl/metalkas-ocean-lava-triathlon-polska/m961.html'
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response: HtmlResponse):
        page = response.url
        self.log(f'Got results from {page}')

        races_info = response.xpath('//div[@id="racesGrid"]//tbody/tr')

        for race in races_info:
            print(f'Hello there {race}')
            race_data = race.xpath('td')
            print(f'{len(race_data)}')
            for detail in race_data:
                print(f'{" " * 4}{detail.get()}')
                print(f'{" " * 8}{detail.attrib}')
            date = race_data[0].xpath('./text()').get()
            # title = race_data[0].xpath('./input/@value').get()
            title = race_data[1].xpath('./text()').get()
            address = race_data[4].xpath('.//@href').get()
            print(f'{date} {title} {base_url + address}')
            yield scrapy.Request(url=base_url + address, callback=self.parse_race_detail)
            break

    def parse_race_detail(self, response: HtmlResponse):
        print(response.url)
        table_head = response.xpath('//table/thead')
        head_trs = table_head.xpath('.//th/text()')
        for tr in head_trs:
            print(tr.get())
        print("Hello")


        //*[@id="resultsGrid"]/table/thead[1]/tr/th[1]


        //*[@id="resultsGrid_c0"]