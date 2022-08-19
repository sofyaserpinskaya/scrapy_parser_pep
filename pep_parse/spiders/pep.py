import re

import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        for pep in response.css('section#numerical-index td a::attr(href)'):
            yield response.follow(pep, callback=self.parse_pep)

    def parse_pep(self, response):
        number, name = re.search(
            r'PEP (?P<number>\d+) – (?P<name>.*)',
            ''.join(response.css('h1.page-title ::text').getall())
        ).groups()
        yield PepParseItem({
            'number': number,
            'name': name,
            'status': response.css('dt:contains("Status") + dd::text').get(),
        })
