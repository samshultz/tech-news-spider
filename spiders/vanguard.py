# -*- coding: utf-8 -*-
import scrapy
from tech.items import TechItem


class VanguardSpider(scrapy.Spider):
    name = 'vanguard'
    start_urls = ["https://www.vanguardngr.com/"]

    def parse(self, response):
        for header in rresponse.css("span.rtp-latest-news-title"):

            link = header.css("a[data-cs-element-type=story-promo-link]::attr(href)").extract_first()
            yield {
                'link': header.css("a::attr(href)").extract_first(),
                'title': header.css("a::text").extract_first()
            }
