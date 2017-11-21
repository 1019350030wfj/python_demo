# -*- coding:utf-8 -*-
"""
多线程爬取电影天堂最新电影列表

1.电影列表地址：'http://www.ygdy8.net/html/gndy/dyzz/list_23_{0}.html'.format(str(page))
2.电影详情地址：从上面网址中截取
3.访问详情地址，提取电影信息
"""
import os
import threading
from queue import Queue
import datetime
import requests
from re_util_queue import *

class Spider(threading.Thread):
    """
    1、从输入队列中提取电影详情url请求并提取有效信息
    2、将有效信息放入输出队列中供输出线程记录
    """
    def __init__(self, in_queue, out_queue):
        super(Spider, self).__init__()
        self.in_queue = in_queue
        self.out_queue = out_queue

    def run(self):
        while True:
            if self.in_queue.empty():
                break
            else:
                url = self.in_queue.get()

            if url:
                result = Spider.process(url)
                self.out_queue.put(result)

    @staticmethod
    def process(url):
        html = do_request(url)
        return extract_details(html)


class Writer(threading.Thread):
    """
    输出线程： 不断从队列中取出处理完的信息，并记录到文件
            直到取出的元素为退出标识为止
    """
    __exit = True

    def __init__(self, queue, filename):
        super(Writer, self).__init__()
        self.queue = queue
        self.filename = filename

    def stop(self):
        self.queue.put(self.__exit)

    def run(self):
        with open(self.filename, 'wb') as f:
            while True:
                data = self.queue.get()
                if not data:
                    continue
                if data is self.__exit:
                    break
                f.write(data.encode('utf-8'))


def do_request(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
            "Host": "www.ygdy8.net"
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.encoding = 'gb2312'
        return response.text
    except requests.exceptions.RequestException as e:
        return ''


def fetch_movie_urls(in_queue):
    base_url = 'http://www.ygdy8.net/html/gndy/dyzz/list_23_{0}.html'
    for page in range(1, 2):
        html = do_request(base_url.format(str(page)))
        extract_urls(html, in_queue)


def main():
    directory = 'data'
    if not os.path.isdir(directory):
        os.makedirs(directory)
    # 电影地址文件
    # path_urls = os.path.join(directory, 'movie_urls.txt')
    # 电影详情文件
    path_movies = os.path.join(directory, 'movies_queue.txt')

    in_queue = Queue()
    out_queue = Queue()

    # 主线程爬取电影地址
    fetch_movie_urls(in_queue)
    # 多线程爬取电影详情

    # 启动记录线程
    writer = Writer(out_queue, filename=path_movies)
    writer.start()
    start = datetime.datetime.now()
    # 启动爬虫线程
    spiders = [Spider(in_queue, out_queue) for i in range(10)]
    for s in spiders:
        s.start()
    for s in spiders:
        s.join()

    # 爬虫线程结束，向输出线程发出结束信号
    writer.stop()
    writer.join()
    print("spend time = " + str((datetime.datetime.now() - start).seconds))

if __name__ == '__main__':
    main()