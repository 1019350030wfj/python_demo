# -*- coding: utf-8 -*-

import sys
import os
import threading
from queue import Queue
import datetime
import requests
from re_util import *


class Spider(threading.Thread):
    """
    1、从输入队列中提取电梯详情url请求并提取有效信息
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
        return extract_details(html, url)


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
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = "utf-8"
        return r.text
    except:
        print("Unexpected error:", sys.exc_info()[0])
        return "ERROR"


def fetch_lift_urls(in_queue):
    base_url = 'http://117.25.179.165:7003/wapq/elevator.do?task=search&eqpCod=T0'
    for i in range(1, 42996):
        if i < 10:
            in_queue.put(base_url+'0000' + str(i))
        elif i < 100:
            in_queue.put(base_url + '000' + str(i))
        elif i < 1000:
            in_queue.put(base_url + '00' + str(i))
        elif i < 10000:
            in_queue.put(base_url + '0' + str(i))
        else:
            in_queue.put(base_url + str(i))


def main():
    directory = 'data'
    if not os.path.isdir(directory):
        os.makedirs(directory)
    # 电梯详情文件
    path_movies = os.path.join(directory, 'lift_details.txt')

    in_queue = Queue()
    out_queue = Queue()

    # 主线程爬取电影地址
    fetch_lift_urls(in_queue)
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