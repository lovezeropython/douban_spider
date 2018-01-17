# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from douban_movie_image.items import DoubanMovieImageItem
# 导入项目中用到的库

class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['movie.douban.com']
    # start_urls =["https://movie.douban.com/top250"]
    def start_requests(self):
        for x in range(0, 225+25, 25):
            url = "https://movie.douban.com/top250?start={}".format(x)
            yield Request(url, dont_filter=True)
            # Request 对象时增加一个参数 dont_filter=True，从而对此请求禁用掉调度器中的过滤。

    def parse(self, response):
        print(response.url, response.status)

        # print(response.status)
        items = DoubanMovieImageItem()
        # 实例化DoubanMovieImageItem
        for item in response.css('.item'):
            items['img_url'] = item.css('.pic img::attr(src)').extract()
            print(items)
            yield items
            # yield item 传送给 pipelines