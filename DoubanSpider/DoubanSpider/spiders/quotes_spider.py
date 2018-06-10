# -*- coding=utf-8 -*-'''
import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request


class QuotesSpider(scrapy.Spider):
    name = "qidian"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        # urls =['https://www.qidian.com/xuanhuan']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # print(response)
        # soup = BeautifulSoup(response, "html.parser")
        # print(soup)
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.xpath('//title'))
        self.log('Saved file %s' % filename)