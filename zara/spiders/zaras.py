# -*- coding: utf-8 -*-
import scrapy


class ZarasSpider(scrapy.Spider):
    name = 'zaras'
    allowed_domains = ['https://www.zara.com']
    start_urls = [
        'https://www.zara.com/in/en/t-shirt-with-front-print-p09362626.html?v1=21686755&v2=1281620']

    def parse(self, response):
        console.log(response)
