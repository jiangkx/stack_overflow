# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class StackOverflowItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    _question = scrapy.Field()
    _qv_content = scrapy.Field()
    _qv_vote = scrapy.Field()
    _qv_comment = scrapy.Field()

    total_answer_count = scrapy.Field()

    accepted_answer = scrapy.Field()
    at_vote = scrapy.Field()
    at_comment = scrapy.Field()

# 字段串行化
    suggestedanswers = scrapy.Field(serializer=lambda x: '|'.join(x))
    sv_vote = scrapy.Field()
    sv_comment = scrapy.Field()
