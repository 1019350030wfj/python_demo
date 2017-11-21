#!/usr/bin/env python
# coding: utf-8


import requests
from pyzbar.pyzbar import decode
from PIL import Image

"""
二维码扫描出来的URL： http://117.25.179.165:7003/wapq/elevatorSearch.jsp?&EqpCod=T028592

                      http://117.25.179.165:7003/wapq/elevatorSearch.jsp?&EqpCod=T008858

真正电梯信息的URL：http://117.25.179.165:7003/wapq/elevator.do?task=search&eqpCod=T028592
"""

def get_html(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = "utf-8"
        return r.text
    except:
        return "ERROR"


decoders = decode(Image.open('lift.png'))
decoder = decoders.pop()
url = decoder[0]
print('QRCode Url = %s' % url)
print(get_html(url))

# 获取网页的内容

