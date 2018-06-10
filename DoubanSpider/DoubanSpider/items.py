# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # 小说名字
    name = scrapy.Field()
    # 小说作者
    author = scrapy.Field()
    # 小说路径
    url = scrapy.Field()
    #小说分类
    categroy = scrapy.Field()
    #小说内容
    content = scrapy.Field()