# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline


class DoubanMovieImagePipeline(object):
    def process_item(self, item, spider):
        return item


class Douban_image_Pipelines(ImagesPipeline):
    pass
    