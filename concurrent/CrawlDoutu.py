# -*- coding: utf-8 -*-

import requests
import threading
from bs4 import BeautifulSoup
from lxml import etree
from concurrent.futures import ThreadPoolExecutor


def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'}
    request = requests.get(url=url, headers=headers)
    return request.text


def get_img_html(html):
    # 创建一个对象
    soup = BeautifulSoup(html, 'lxml')
    # 每一页中所有套图连接
    all_a = soup.find_all('a', class_='list-group-item')
    for link in all_a:
        # 获取每个套图详情的网页源码
        img_html = get_html(link['href'])
        # 将一页中10个套图详情的源码拼接
        img_html += img_html
    return img_html


# 获取每个图片src地址
def get_img(html):
    # 初始化打印源码，自动修正html源码
    soup = etree.HTML(html)
    # //代表选择盒子内容，[]代表过滤的条件 @选定属性盒子
    # 解析网页方法
    items = soup.xpath('//div[@class="artile_des"]')
    for item in items:
        imgurl_list = item.xpath('table/tbody/tr/td/a/img/@onerror')
        start_save_img(imgurl_list)


def save_img(img_url):
    # global x
    # x += 1
    # 获取src
    img_url = img_url.split('=')[-1][1:-2].replace('pn', 'png')
    print(u'Thread Id: %s 正在下载 http: %s' % (threading.current_thread(),img_url))
    img_content = requests.get("http:" + img_url).content
    # wb 	以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
    # wb+ 	以二进制格式打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
    with open('doutu/%s' % img_url.split('/')[-1], 'wb') as f:
        f.write(img_content)


# 多线程
def start_save_img(imgurl_list):
    # for i in imgurl_list:
    #     th = threading.Thread(target=save_img, args=(i,))
    #     th.start()
     threadPool = ThreadPoolExecutor(10)
     for i in imgurl_list:
         threadPool.submit(save_img(i))


# 多页
def main():
    start_url = "https://www.doutula.com/article/list/?page={}"
    for i in range(1, 7):
        # 获取外页url
        start_html = get_html(start_url.format(i))
        # 获取内页url里面的源码
        html = get_img_html(start_html)
        get_img(html)
        break


if __name__ == '__main__':
    main()
    print("crawl end")
