# -*- coding:utf-8 -*-

import requests
import json


def download_info():
    """downloading list page(contains information of all of pictures) and save into data/info.txt"""
    page = 1
    while True:
        page_json = download_page(page)
        if not page_json['data']['list']:
            break
        save_page(page_json)
        page += 1


def download_page(page):
    """ downloading page info"""
    url = "http://api.pmkoo.cn/aiss/suite/suiteList.do"
    params = {
        'page': page,
        'userId': 153044
    }
    rsp = requests.post(url, data=params)
    return rsp.json()


def save_page(page_json):
    """ save a page information """
    txt = json.dumps(page_json)
    with open('data/info.txt', 'a') as f:
        f.write(txt)
        f.write('\n')


if __name__ == '__main__':
    download_info()
