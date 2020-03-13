# -*- coding: utf-8 -*-
import scrapy
import sys
from scrapy.linkextractors import LinkExtractor
from ..items import StackOverflowItem


class SoqaSpider(scrapy.Spider):
    name = 'soqa'
    allowed_domains = ['stackoverflow.com']

    print("请输入在stack overflow 搜索的关键词（若有多个关键词请用+隔开，不要有空格）：")
    x = input()
    print('您搜索的关键词是：', x)
    start_urls = ['https://stackoverflow.com/search?q=' + x]

    # 搜索得到页面的解析函数（现为搜索scrapy后的界面为起始链接）
    def parse(self, response):
        # 提取页面中每一问题的链接
        le = LinkExtractor(restrict_css='div.result-link')
        for link in le.extract_links(response):
            yield scrapy.Request(link.url, callback=self.parse_question)
        # 提取下一页问题的链接
        le = LinkExtractor(restrict_css='div.pager.fl')

        links = le.extract_links(response)
        if links:
            next_url = links[0].url
            yield scrapy.Request(next.url, callback=self.parse)

    # 问题页面的解析函数
    def parse_question(self, response):
        qa = StackOverflowItem()

        # 问题标题
        sel = response.css('div#question-header')
        qa['question'] = sel.xpath('//*[@id="question-header"]/h1/a/text()')

        # 问题内容及vote数
        sel = response.css('div.question')
        qa['questioncontent'] = sel.xpath('normalize-space(//*[@id="question"]/div[2]/div[2]/div[1])')
        qa['questionvote'] = sel.xpath('//*[@id="question"]/div[2]/div[1]/div/div/text()')

        # answercount
        qa['answercount'] = sel.xpath('normalize-space(//*[@id="answers-header"]/div/h2)')

        # accepted-answer内容及vote数
        sel = response.css('[itemprop = acceptedAnswer]')
        qa['accepted_answer'] = sel.xpath('normalize-space(./div/div[2]/div[1])')
        qa['accepted_answervote'] = sel.xpath('./div/div[1]/div/div[1]/text()')

        # 其他回答内容及vote数
        sel = response.css('[itemprop = suggestedAnswer]')
        qa['suggestedanswers'] = sel.xpath('normalize-space(./div/div[2]/div[1])')
        qa['suggestedanswersvote'] = sel.xpath('./div/div[1]/div/div[1]/text()')

        yield qa
