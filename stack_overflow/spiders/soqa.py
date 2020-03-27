# -*- coding: utf-8 -*-
import scrapy
import csv
import sys
import os
from tkinter import *
from scrapy.linkextractors import LinkExtractor
from ..items import StackOverflowItem


def main():
    global keyword, text, num
    # 创建空白窗口,作为主载体
    root = Tk()
    root.title('测试spider')

    # 窗口的大小，后面的加号是窗口在整个屏幕的位置
    root.geometry('550x400+398+279')

    # 标签控件，窗口中放置文本组件
    Label(root, text='请输入爬取关键词（有多个请用+隔开，不要有空格）:', font=("华文行楷", 20), fg='black').grid()


    # 定位 pack包 place位置 grid是网格式的布局 #Entry是可输入文本框
    keyword = Entry(root, font=("微软雅黑", 15))
    keyword.grid(row=0, column=1)

    Label(root, text='请输入爬取问题的数量:', font=("华文行楷", 20), fg='black').grid(row=3, column=0,sticky=W)

    Label(root, text='回答中应含有的关键字同时含有以空格间隔，或含有用+间隔:', font=("华文行楷", 20), fg='black').grid(row=4, column=0,sticky=W)

    # 列表控件
    text = Listbox(root, font=('微软雅黑', 15), width=45, height=10)

    # columnspan 组件所跨越的列数
    text.grid(row=1, columnspan=2)

    # 设置按钮 sticky对齐方式，N S W E
    #开始爬取按钮后还缺少 command
    button = Button(root, text='开始搜索爬取', font=("微软雅黑", 15)).grid(row=5, column=0, sticky=W)
    button = Button(root, text='退出', font=("微软雅黑", 15), command=root.quit).grid(row=5, column=1, sticky=E)

    # 使得窗口一直存在
    mainloop()


main()


class SoqaSpider(scrapy.Spider):
    name = 'soqa'
    allowed_domains = ['stackoverflow.com']

    # print("请输入在stack overflow 搜索的关键词（若有多个关键词请用+隔开，不要有空格）：")

    global keyword
    x = keyword.get()
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

        # 问题内容,vote数
        sel = response.css('div.question')
        qa['questioncontent'] = sel.xpath('normalize-space(//*[@id="question"]/div[2]/div[2]/div[1])')
        qa['questionvote'] = sel.xpath('//*[@id="question"]/div[2]/div[1]/div/div/text()')

        # qa['questioncomment'] = sel.xpath('normalize-space(//*[@class="comments js-comment"]/div[2]/div/span[1])')

        # answercount
        qa['answercount'] = sel.xpath('normalize-space(//*[@id="answers-header"]/div/div[1]/h2)')

        # accepted-answer内容及vote数
        sel = response.css('[itemprop = acceptedAnswer]')
        qa['accepted_answer'] = sel.xpath('normalize-space(./div/div[2]/div[1])')
        qa['accepted_answervote'] = sel.xpath('./div/div[1]/div/div[1]/text()')
        # qa['accepted_answercomment'] = sel.xpath('normalize-space(./div/div[3]/div[1]//div[2]/div/span[1])')

        # 其他回答内容及vote数
        sel = response.css('[itemprop = suggestedAnswer]')
        qa['suggestedanswers'] = sel.xpath('normalize-space(./div/div[2]/div[1])')
        qa['suggestedanswersvote'] = sel.xpath('./div/div[1]/div/div[1]/text()')
        # qa['suggestedanswerscomment'] = sel.xpath('normalize-space(./div/div[3]/div[1]//div[2]/div/span[1])')

        yield qa



