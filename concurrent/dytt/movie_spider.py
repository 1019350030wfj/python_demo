# -*- coding:utf-8 -*-
"""
多线程爬取电影天堂最新电影列表

1.电影列表地址：'http://www.ygdy8.net/html/gndy/dyzz/list_23_{0}.html'.format(str(page))
2.电影详情地址：从上面网址中截取
3.访问详情地址，提取电影信息
"""
import os
import threading
import time
from queue import Queue

import requests


def do_request(url):
    try:
        headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
            "Host":"www.ygdy8.net"
        }
        response = requests.get(url, headers=headers,timeout=10)
        return response.text
    except requests.exceptions.RequestException as e:
        return ''


def extract_urls(html):
    pass


def fetch_movie_urls(filename):
    if not os.path.isfile(filename):
        with open(filename, 'w') as file_url:
            base_url = 'http://www.ygdy8.net/html/gndy/dyzz/list_23_{0}.html'
            for page in range(1,165):
                html = do_request(base_url.format(str(page)))
                urls = extract_urls(html)
                file_url.write(urls)


def main():
    directory = 'data'
    if not os.path.isdir(directory):
        os.makedirs(directory)
    # 电影地址文件
    path_urls = os.path.join(directory, 'movie_urls.txt')
    # 电影详情文件
    path_movies = os.path.join(directory, 'movies.txt')

    # 主线程爬取电影地址
    fetch_movie_urls(path_urls)


if __name__ == '__main__':
    main()