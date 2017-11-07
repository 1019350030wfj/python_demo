# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class XiubaiPipeline(object):
    def process_item(self, item, spider):
        with open('xiubai.txt', 'a', encoding="utf-8") as f:
            f.write('作者:{} \t {} 点赞 \t  {} 评论 \n  {} '.format(item['author'], item['funNum'], item['comNum'], item['body']))
        return item
