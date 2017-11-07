# -*- coding: utf-8 -*-
import scrapy
from weather.items import WeatherItem

class XmtianqiSpider(scrapy.Spider):
    name = 'XMTianqi'
    allowed_domains = ['tianqi.com']
    start_urls = []

    cities = ["xiamen"]
    # cities = ["suzhou", "xiamen", "quanzhou"]

    for city in cities:
        start_urls.append("http://" + city + ".tianqi.com/")

    def parse(self, response):
        '''
        筛选信息的函数：
        date = 今日日期
        week = 星期几
        img = 表示天气的图标
        temperature = 当天的温度
        weather = 当天的天气
        wind = 当天的风向
        :param response:
        :return:
        '''
        datas = []

        sixDay = response.xpath("//div[@class='tqshow1']")

        for day in sixDay:
            item = WeatherItem()
            date = ''
            for text in day.xpath('./h3//text()').extract():
                date += text

            item['date'] = date
            item['week'] = day.xpath('./p//text()').extract()[0]
            item['img'] = day.xpath('./ul/li[@class="tqpng"]/img/@src').extract()[0]
            tq = day.xpath('./ul/li[2]//text()').extract()
            # 将tq找到的str连接
            item['temperature'] = ''.join(tq)
            item['weather'] = day.xpath('./ul/li[3]/text()').extract()[0]
            item['wind'] = day.xpath('./ul/li[4]/text()').extract()[0]
            datas.append(item)

        return datas

