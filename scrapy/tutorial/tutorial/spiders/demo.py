# -*- coding: utf-8 -*-
import scrapy


class DemoSpider(scrapy.Spider):
    name = 'demo'
    allowed_domains = ['baidu.com/']
    start_urls = ['http://www.somode.com/jiaocheng/4991.html']

    def parse(self, response):
        fnmae=response.url.split('/')[-1]
        with open(fnmae ,'wb')as f:
            f.write(response.body)
            self.log("success %s" %fnmae)
        pass
