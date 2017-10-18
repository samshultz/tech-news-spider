# -*- coding: utf-8 -*-
import scrapy
from tech.items import TechItem
import psycopg2

class HackerNewsSpider(scrapy.Spider):
    name = 'HN'
    start_urls = ["https://thehackernews.com"]

    def parse(self, response):
        self.conn = psycopg2.connect(host="localhost",database="scrape",
            user="postgres", password="reductionism==12345")
        self.cur = self.conn.cursor()
        for header in response.css("article.post"):

            a = {
                'link': header.css("h2.post-title a::attr(href)").extract_first(),
                'title': header.css("h2.post-title a::text").extract_first(),
                'date': header.css("span.updated::text").extract_first()
            }
            self.cur.execute("INSERT INTO scraped_data (links, title) VALUES(%s, %s);", [a['link'], a['title']])
            
            self.conn.commit()
