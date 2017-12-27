# -*- coding: utf-8 -*-

import scrapy
import time
from www_zhipin_com.items import WwwZhipinComItem


class ZhipinSpider(scrapy.Spider):
    # spider的名字定义了Scrapy如何定位（并初始化）spider，所以其必须是唯一的。
    # 不过您可以生成多个相同的spider实例，这没有任何限制。name是spider最重要的属性，而且是必须的
    name = 'zhipin'
    # 可选。包含了spider允许爬取的域名（domain）列表（list）。当OffsiteMiddlerware 启用时，域名不在列表中的URL不会被跟进。
    allowed_domains = ['www.zhipin.com']

    # URL列表。 当没有制定特定的URL时，spider将从列表中开始进行爬取。
    # 这里我们进行了指定，所以不是从这个URL列表里爬取
    start_urls = ['http://www.zhipin.com/']

    # 要爬取的页面，可以改为自己需要搜的条件，这里搜的是上海-PHP，其它条件都是不限
    positionUrl = "http://www.zhipin.com/job_detail/?query=Android&scity=101230200&source=2"
    curPage = 1

    # 发送 header,伪装为浏览器
    headers = {
        'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36",
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'dnt': "1",
        'accept-encoding': "gzip, deflate",
        'accept-language': "zh-CN,zh;q=0.8,en;q=0.6",
        'cookie': "lastCity=101230200; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1514121359,1514299446,1514328193; __c=1514328193; __g=-; __l=l=%2F&r=; __a=2243278.1514121460.1514299446.1514328193.15.3.3.15; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1514329080",
        'cache-control': "no-cache",
    }

    # 该方法必须返回一个可迭代对象（iterable）。该对象包含了spider用于爬取的第一个request。
    # 该方法仅仅会被Scrapy调用一次，因此您可以将其实现为生成器。
    def start_requests(self):
        return [self.next_request()]


    # 负责处理response并返回处理的数据以及( / 或)跟进的URL。
    def parse(self, response):
        print("request -> " + response.url)
        job_list = response.css('div.job-list > ul > li')
        for job in job_list:
            item = WwwZhipinComItem()
            job_primary = job.css('div.job-primary')
            item['pid'] = job_primary.css('div.info-primary > h3 > a::attr(data-jobid)').extract_first().strip()
            item['positionName'] = job_primary.css('div.info-primary > h3 > a::text').extract_first().strip()
            print(job_primary.css('div.info-primary > h3 > a > span::text').extract_first())
            item['salary'] = job_primary.css('div.info-primary > h3 > a > span::text').extract_first().strip()
            info_primary = job_primary.css(
                'div.info-primary > p::text').extract()
            print(info_primary)
            item['city'] = info_primary[0].strip()
            item['workYear'] = info_primary[1].strip()
            item['education'] = info_primary[2].strip()
            item['companyShortName'] = job_primary.css(
                'div.info-company > div.company-text > h3 > a::text'
            ).extract_first().strip()
            company_infos = job_primary.css(
                'div.info-company > div.company-text > p::text').extract()
            if len(company_infos) == 3:  # 有一条招聘这里只有两项，所以加个判断
                item['industryField'] = company_infos[0].strip()
                item['financeStage'] = company_infos[1].strip()
                item['companySize'] = company_infos[2].strip()
            item['positionLables'] = job.css(
                'li > div.job-tags > span::text').extract()
            item['time'] = job.css('span.time::text').extract_first().strip()
            item['updated_at'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            yield item
        # self.curPage += 1
        # time.sleep(5)  # 停停停！听听听！都给我停下来听着！睡一会(～﹃～)~zZ
        # yield self.next_request()

    # 发送请求
    def next_request(self):
        return scrapy.http.FormRequest(
            self.positionUrl + ("&page=%d&ka=page-%d" %
                                (self.curPage, self.curPage)),
            headers=self.headers,
            callback=self.parse)
