# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import requests
import json


class WeatherPipeline(object):
    def process_item(self, item, spider):
        # 获取当前目录
        base_dir = os.getcwd()
        # 目录不存在则创建
        fileDir = base_dir + os.path.sep + "data"
        if os.path.exists(fileDir) is False:
            os.makedirs(fileDir)

        # 文件存在data目录下
        fileName = fileDir + os.path.sep + "weather.txt"

        # 文件以追加的方式打开，并从内存读取数据，然后一条一条写入
        with open(fileName, 'a', encoding="utf-8") as f:
            f.write(item['date'] + "\n")
            f.write(item['week'] + "\n")
            f.write(item['img'] + "\n")
            f.write(item['temperature'] + "\n")
            f.write(item['weather'] + "\n")
            f.write(item['wind'] + "\n")

        # 下载图片
        with open(base_dir + '/data/' + item['date'] + '.png', 'wb') as f:
            f.write(requests.get(item['img']).content)

        return item


class W2json(object):
    def process_item(self, item, spider):
        '''
        爬取的信息保存到json
        方便其他程序员调用
        :param item:
        :param spider:
        :return:
        '''
        base_dir = os.getcwd()
        fileDir = base_dir + os.path.sep + "data"
        if not os.path.exists(fileDir):
            os.mkdir(fileDir)
        filename = fileDir + os.path.sep + "weather.json"

        with open(filename, 'a', encoding="utf-8") as f:
            line = json.dumps(dict(item), ensure_ascii=False) + '\n'
            f.write(line)

        return item


import pymysql


class W2mysql(object):
    def process_item(self, item, spider):
        '''
        将爬取的信息保存到mysql
        :param item:
        :param spider:
        :return:
        '''

        # 将item里的数据拿出来
        date = item['date']
        week = item['week']
        img = item['img']
        temperature = item['temperature']
        weather = item['weather']
        wind = item['wind']

        # 和本地的scrapyDB数据库建立连接
        connection = pymysql.connect(
            host='localhost',
            user='root',
            passwd='root',
            db='scrapyDB',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        try:
            with connection.cursor() as cursor:
                # 创建更新值的sql语句
                sql = """ insert into weather(date,week,img,temperature,weather,wind)
                          VALUES (%s,%s,%s,%s,%s,%s)
                """
                # 执行sql语句 excute的第二个参数可以将sql缺省语句补全，一般以元组的格式
                cursor.execute(sql, (date,week,img,temperature,weather,wind))
            connection.commit()
        finally:
            #关闭连接
            connection.close()

        return item
