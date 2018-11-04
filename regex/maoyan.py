# -*- coding: utf-8 -*-
# https://blog.csdn.net/winycg/article/details/78177076?utm_source=blogkpcl10
import json
import requests
from multiprocessing import Pool
from requests.exceptions import RequestException
import re


# 获取页面
def get_one_page(url):
    try:
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
        headers = {"User-Agent": user_agent}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


# 解析页面
def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                         + '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'item': item[3].strip()[3:],
            'actor': item[4].strip()[5:],
            'score': item[5] + item[6]
        }


# 将抓取的结果存入文件
def write_to_file(content):
    with open('maoyan.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        f.close()


# 主要的调用方法
def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)


# 程序的入口
if __name__ == '__main__':
    # 这一步没有用多线程
    for i in range(10):
        main(i * 10)
    # 这里运用了多线程
    # pool = Pool()
    # pool.map(main, [i*10 for i in range(10)])
