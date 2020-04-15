# -*- coding: utf-8 -*-
import scrapy
import numpy as np
import pandas as pd
import csv
import sys
import os
from tkinter import *
from scrapy.linkextractors import LinkExtractor
from stack_overflow.items import StackOverflowItem

class SoqaSpider(scrapy.Spider):
    name = 'soqa'
    allowed_domains = ['stackoverflow.com']


    # 搜索得到页面的解析函数
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
        so = StackOverflowItem()

        # 问题标题
        sel = response.css('div#question-header')
        so['_question'] = sel.xpath('//*[@id="question-header"]/h1/a/text()').extract()

        # 问题内容,vote数，评论
        sel = response.css('div.question')
        so['_qv_content'] = sel.xpath('normalize-space(//*[@id="question"]/div[2]/div[2]/div[1])').extract()
        so['_qv_vote'] = sel.xpath('//*[@id="question"]/div[2]/div[1]/div/div/text()').extract()
        so['_qv_comment'] = sel.xpath('normalize-space(//span[@class="comment-copy"])').extract()
        # ./div[2]/div[3]/div[1]/ul/*/div[2]/div
        # //span[@class="comment-copy"]

        # answercount
        so['total_answer_count'] = sel.xpath('normalize-space(//*[@id="answers-header"]/div/div[1]/h2)').extract()

        # accepted-answer内容及vote数
        sel = response.css('[itemprop = acceptedAnswer]')
        so['accepted_answer'] = sel.xpath('normalize-space(./div/div[2]/div[1])').extract()
        so['at_vote'] = sel.xpath('./div/div[1]/div/div[1]/text()').extract()
        so['at_comment'] = sel.xpath('normalize-space(./div/div[3]/div[1]/ul/*/div[2]/div)').extract()

        # 其他回答内容及vote数
        sel = response.css('[itemprop = suggestedAnswer]')
        so['suggestedanswers'] = sel.xpath('normalize-space(./div/div[2]/div[1])').extract()
        so['sv_vote'] = sel.xpath('./div/div[1]/div/div[1]/text()').extract()
        so['sv_comment'] = sel.xpath('normalize-space(./div/div[3]/div[1]/ul/*/div[2]/div)').extract()

        yield so


    def main():
        global keyword, text, num, k1, k2
        # 创建空白窗口,作为主载体
        root = Tk()
        root.title('Stack Overflow Spider')

        # 窗口的大小，后面的加号是窗口在整个屏幕的位置
        root.geometry('900x600+198+79')

        # 标签控件，窗口中放置文本组件
        Label(root, text='输入爬取关键词（多个请用+隔开，不要有空格）:', font=("华文行楷", 20), fg='black').grid(row=0, column=0, sticky=W)

        # 定位 pack包 place位置 grid是网格式的布局 #Entry是可输入文本框
        keyword = Entry(root, font=("微软雅黑", 15))
        keyword.grid(row=1, column=0)

        Label(root, text='定制功能', font=("华文行楷", 20), fg='black').grid(row=2, column=0, sticky=W)
        Label(root, text='以下为可选项目，可空', font=("华文行楷", 20), fg='black').grid(row=3, column=0, sticky=W)

        Label(root, text='（1）请输入爬取问题的数量(问题点赞数降序选取):', font=("华文行楷", 20), fg='black').grid(row=4, column=0, sticky=W)
        k1 = Entry(root, font=("微软雅黑", 15))
        k1.grid(row=5, column=0)

        Label(root, text='（2）回答中应含有的关键字（同时含有以空格间隔，或含有用+间隔）:', font=("华文行楷", 20), fg='black').grid(row=6, column=0,
                                                                                                  sticky=W)
        k2 = Entry(root, font=("微软雅黑", 15))
        k2.grid(row=7, column=0)

        # 列表控件
        text = Listbox(root, font=('微软雅黑', 15), width=45, height=10)

        # columnspan 组件所跨越的列数
        # text.grid(row=1, columnspan=2)

        # 设置按钮 sticky对齐方式，N S W E
        # 开始爬取按钮后还缺少 command 跳转至爬虫解析函数
        button = Button(root, text='开始爬取', font=("微软雅黑", 15)).grid(row=9, column=0, sticky=W)
        button = Button(root, text='退出', font=("微软雅黑", 15), command=root.quit).grid(row=9, column=1, sticky=E)

        # 使得窗口一直存在
        mainloop()

    main()

    global keyword
    x = keyword.get()
    y = k1.get()
    z = k2.get()
    print('您搜索的关键词是：', x)
    start_urls = ['https://stackoverflow.com/search?q=' + x]




'''
    def wj():
        filepath = "file:///C:/spider/export.csv"
        # 打开文件
        df = pd.read_csv(filepath, header=0, skip_blank_lines=True, encoding="utf-8")
        # 以问题vote数降序排列
        df.sort_values(by='_qv_vote', axis=0, ascending=False, inplace=True, na_position='last')

        y = int(k1.get())
        z = k2.get()
        # 关键词选取
        df2 = df[df['_question'].str.contains('z')]

        # 选取前y项
        a = 0

        if y > a:
            y += 1
            y *= 2
            df.head(y)

        # df.to_csv(filepath, encoding="utf-8")

    wj()
'''

#filepath = "file:///C:/spider/export.csv"
#df = pd.read_csv(filepath, header=0, encoding="utf-8")




