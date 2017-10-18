# -*- coding: utf-8 -*-
import scrapy
from tech.items import TechItem
import socket
import psycopg2


class BBCFutureSpider(scrapy.Spider):
    name = 'bbcfuture'
    start_urls = ['http://www.bbc.com/future']

    def parse(self, response):
        self.conn = psycopg2.connect(host="localhost",database="scrape",
            user="postgres", password="reductionism==12345")
        self.cur = self.conn.cursor()
        for header in response.css("div.promo-unit-header"):

            link = header.css("a[data-cs-element-type=story-promo-link]::attr(href)").extract_first()
            a = {
                'link': response.urljoin(link),
                'title': header.css("a[data-cs-element-type=story-promo-link] h3.promo-unit-title::text").extract_first()
            }
            self.cur.execute("INSERT INTO scraped_data (links, title) VALUES(%s, %s);", [a['link'], a['title']])
            
            self.conn.commit()            
