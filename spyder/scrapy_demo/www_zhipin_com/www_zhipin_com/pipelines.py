# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo


class WwwZhipinComPipeline(object):
    def process_item(self, item, spider):
        return item


class MongoPipeline(object):
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db


    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri="mongodb://localhost:27017",
            mongo_db='iApp'
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient('127.0.0.1', 27017)
        self.db = self.client.iApp

    def close_spider(self,spider):
        self.client.close()

    def process_item(self, item, spider):
        res = self.db.jobs_python.insert_one(dict(item))
        print(res)
        return item

