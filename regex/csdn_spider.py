# -*- coding: utf-8 -*-

import re
import requests


# https://blog.csdn.net/qq_33472765/article/details/80785441


class DataParserTool(object):
    @classmethod
    def parser_data(cls, data):
        """
        handle data
        :param data:
        :return: data_list [(), (), ()]
        """
        data_list = []
        for title, info, name, time, read_num, comment_num in data:
            title = title.strip()  # 去除两端空格

            res = info.replace('&amp;#13;', '')
            res1 = res.replace('\n', '')
            info = res1.strip()
            name = name.strip()
            time = time.strip()

            data_list.append((title, info, name, time, read_num, comment_num))
        return data_list


class CSDNSpider(object):
    def __init__(self, url):
        self.url = url
        self.user_agent = {
            'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}

    def parse_data_by_html(self, html):
        # print(html)
        pattern = re.compile(
            r'<h2>.*?<a.*?>(.*?)</a>.*?<div class="summary oneline">(.*?)</div>.*?<dl class="list_userbar">.*?<dd class="name">.*?<a.*?>(.*?)</a>.*?<dd class="time">(.*?)</dd>.*?<span class="num">(.*?)</span>.*?<span class="num">(.*?)</span>',
            re.S)
        res = re.findall(pattern, html)

        # parse data
        data = DataParserTool.parser_data(res)
        return data

    def get_page_code(self):
        headers = {
            'Host':"blog.csdn.net",
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
            'Cookie': 'uuid_tt_dd=10_18507371140-1540449521544-367705; dc_session_id=10_1540449521544.326361; ADHOC_MEMBERSHIP_CLIENT_ID1.0=627e9e73-1b3a-ee2a-45c2-f3e8eea191e8; TY_SESSION_ID=11cbce7c-81ab-43a4-8156-bb58373abf88; CloudGuest=n4GT2YI0aSNZKmkwqBs4h4ueDooFoUUtTOhX+N3JL/uKi6U1SR+lwzzAOV9mwZCNNhRjFaWJ/YgtComOmYL3CSE3XV8u2b70bAdaKwQjzAg72DgoEteDMnHyfyZSwtcQL9Abjzv3OwKPSdkpA6S+W+oUB3ijcsnwyIBb+QZaMkT7MHVdADR2quoFGhauX5d1; sid=gzanh04mgyqzuohasaugoo10; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1540962281,1540964755,1540965507,1540966963; dc_tos=phgc8a; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1540970219'}
        # headers = self.user_agent
        req = requests.get(self.url, headers)
        return req.text

    def start_spider(self):
        html = self.get_page_code()
        data = self.parse_data_by_html(html)
        self.save_data_to_db(data)
        # print(data)

    def save_data_to_db(self, data):
        with open("csdn.txt", 'w', encoding="utf-8") as f:
            for title, info, name, time, read_num, comment_num in data:
                f.write('title:' + title)
                f.write('\n')
                f.write('info:' + info)
                f.write('\n')
                f.write('name:' + name)
                f.write('\n')
                f.write('time:' + time)
                f.write('\n')
                f.write('read_num:' + read_num)
                f.write('\n')
                f.write('comment_num:' + comment_num)
                f.write('\n\n')


def read_file(file_path):
    with open(file_path, 'r') as f:
        print(f.read())


if __name__ == '__main__':
    csdn = CSDNSpider('https://blog.csdn.net/')
    csdn.start_spider()
