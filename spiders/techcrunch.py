# -*- coding: utf-8 -*-
import scrapy
from tech.items import TechItem


class TechCrunchSpider(scrapy.Spider):
    name = 'techcrunch'
    start_urls = ["https://techcrunch.com"]

    def parse(self, response):
        for header in response.css("div.block-content"):

            link = header.css("a[data-cs-element-type=story-promo-link]::attr(href)").extract_first()
            yield {
                'link': header.css("h2.post-title a::attr(href)").extract_first(),
                'title': header.css("h2.post-title a::text").extract_first()
            }
