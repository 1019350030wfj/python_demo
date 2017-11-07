#!/usr/bin/env python
# coding: utf-8
#
import requests
from pyzbar.pyzbar import decode
from PIL import Image

def get_html(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = "utf-8"
        return r.text
    except:
        return "ERROR"


decoders = decode(Image.open('lift1.png'))
decoder = decoders.pop()
url = decoder[0]
print(get_html(url))

# 获取网页的内容

