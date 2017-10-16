# -*- coding: utf-8 -*-
import scrapy
from tech.items import TechItem


class HackerNewsSpider(scrapy.Spider):
    name = 'HN'
    start_urls = ["https://thehackernews.com"]

    def parse(self, response):
        for header in response.css("article.post"):

            yield {
                'link': header.css("h2.post-title a::attr(href)").extract_first(),
                'title': header.css("h2.post-title a::text").extract_first(),
                'date': header.css("span.updated::text").extract_first()
            }
