# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class StackOverflowItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    question = scrapy.Field()
    qcontent = scrapy.Field()
    accepted_answer = scrapy.Field()
    otheranswers = scrapy.Field()
    qvote = scrapy.Field()
    avote = scrapy.Field()
    ovote = scrapy.Field()
