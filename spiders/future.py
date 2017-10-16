# -*- coding: utf-8 -*-
import scrapy
from tech.items import TechItem
import socket


class BBCFutureSpider(scrapy.Spider):
    name = 'bbcfuture'
    start_urls = ['http://www.bbc.com/future']

    def parse(self, response):
        for header in response.css("div.promo-unit-header"):

            link = header.css("a[data-cs-element-type=story-promo-link]::attr(href)").extract_first()
            yield {
                'link': response.urljoin(link),
                'title': header.css("a[data-cs-element-type=story-promo-link] h3.promo-unit-title::text").extract_first()
            }
