# -*- coding: utf-8 -*-
import scrapy
from tech.items import TechItem
import psycopg2

class TechCrunchSpider(scrapy.Spider):
    name = 'techcrunch'
    start_urls = ["https://techcrunch.com"]

    def parse(self, response):
        self.conn = psycopg2.connect(host="localhost",database="scrape",
            user="postgres", password="reductionism==12345")
        self.cur = self.conn.cursor()
        for header in response.css("div.block-content"):

            link = header.css("a[data-cs-element-type=story-promo-link]::attr(href)").extract_first()
            a = {
                'link': header.css("h2.post-title a::attr(href)").extract_first(),
                'title': header.css("h2.post-title a::text").extract_first()
            }
            self.cur.execute("INSERT INTO scraped_data (links, title) VALUES(%s, %s);", [a['link'], a['title']])
            
            self.conn.commit()
