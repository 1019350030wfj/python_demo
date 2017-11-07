# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class BiqugePipeline(object):
    def process_item(self, item, spider):
        '''
        将数据写入数据库
        :param item:
        :param spider:
        :return:
        '''
        # 首先从items里取出数据
        name = item['bookname']
        order_id = item['order_id']
        title = item['title']
        body = item['body']

        # 与本地数据库建立联系
        # 和本地的scrapyDB数据库建立链接
        connection = pymysql.connect(
            host='localhost', #连接的是本地数据库
            user='root',
            passwd='root',
            db='bqxiaoshuo', #数据库名称
            charset='utf8mb4', #默认的编码方式
            cursorclass=pymysql.cursors.DictCursor
        )
        try:
            with connection.cursor() as cursor:
                # 数据库表的sql
                sql1 = 'Create Table if not exists %s(id int,zjm varchar(20), body text)' % name
                # 单章小说的写入
                sql = 'Insert into %s VALUES (%d, \'%s\', \'%s\')' % (
                    name, order_id, title, body
                )
                cursor.execute(sql1)
                cursor.execute(sql)

            # 提交本次插入的记录
            connection.commit()
        finally:
            #关闭连接
            connection.close()
            return item
