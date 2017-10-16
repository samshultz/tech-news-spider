# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TechItem(scrapy.Item):
    link = scrapy.Field()
    title = scrapy.Field()
    server = scrapy.Field()
