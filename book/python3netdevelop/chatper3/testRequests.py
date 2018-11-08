# -*- coding: utf-8 -*-

import requests
import re

# r = requests.get("https://www.baidu.com")
# print(type(r))
# print(r.status_code)
# print(r.text)
# print(r.cookies)
#
# r = requests.get("http://httpbin.org/get")
# print(r.text)

# data = {
#     'name': 'jayden',
#     'age': 22
# }
# r = requests.get('http://httpbin.org/get', params=data)
# print(type(r.text))
# print(r.json())
# print(type(r.json()))

# 抓去网页
# headers = {
#     'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
# }
#
# r = requests.get('https://www.zhihu.com/explore', headers=headers)
# pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
# titles = re.findall(pattern, r.text)
# print(titles)

# 抓取二进制数据
# r = requests.get("https://github.com/favicon.ico")
# print(r.text) # 乱码， 图片直接转换为str
# print(r.content) #结果前面带有b''

# 二进制数据直接写入文件
# r = requests.get("https://github.com/favicon.ico")
# with open('favicon.ico', 'wb') as f:
#     f.write(r.content)

# POST请求
# data = {'name': 'jayden', 'age': '26'}
# r = requests.post('http://httpbin.org/post', data=data)
# print(r.text)

# r = requests.get("https://www.jianshu.com")
# print(type(r.status_code), r.status_code)
# print(type(r.headers), r.headers)
# print(type(r.cookies), r.cookies)
# print(type(r.url), r.url)
# print(type(r.history), r.history)

# 会话维持
# s = requests.Session()
# s.get('http://httpbin.org/cookies/set/number/123456789')
# r = s.get('http://httpbin.org/cookies')
# print(r.text)

# SSL证书验证
# resp = requests.get('https://www.12306.cn')
# print(resp.status_code)

# 文件
# files = {'file': open('favicon.ico', 'rb')}
# r = requests.post('http://httpbin.org/post', files=files)
# print(r.text)

# Cookies
# r = requests.get('https://www.baidu.com')
# print(r.cookies)
# for key, value in r.cookies.items():
#     print(key + "=" + value)

# 代理
proxies = {
    "http": "http://10.10.1.10:3128",
    "https": "http://10.10.1.10:1080",
}

requests.get("https://www.taobao.com", proxies=proxies)
