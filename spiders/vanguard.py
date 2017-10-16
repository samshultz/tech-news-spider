# -*- coding: utf-8 -*-
import scrapy
from tech.items import TechItem


class VanguardSpider(scrapy.Spider):
    name = 'vanguard'
    start_urls = ["https://www.vanguardngr.com/"]

    def parse(self, response):
        for header in response.css("span.rtp-latest-news-title"):

            link = header.css("a::attr(href)").extract_first()
            yield {
                'link': response.urljoin(link),
                'title': header.css("a::text").extract_first()
            }
