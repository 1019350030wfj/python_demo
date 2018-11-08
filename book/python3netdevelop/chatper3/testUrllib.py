# -*- coding:utf-8 -*-

from urllib import request
from urllib import parse

# response = request.urlopen('https://www.python.org')
# # print(response.read().decode('utf-8'))
# print(type(response))
# print(response.status)
# print(response.getheaders())
# print(response.getheader('Server'))
#
# # data参数， 是可选的，如果添加该参数，需要使用bytes()方法将参数转化为字节流便秘格式的内容
# # 请求方式也改为了POST

#
# data = bytes(parse.urlencode({'word': 'hello'}), encoding='utf8')
# response = request.urlopen('http://httpbin.org/post', data=data)
# print(response.read())
#
# # timeout参数， 设置超时时间，单位为秒
# response = request.urlopen('http://httpbin.org/get', timeout=1)
# print(response.read())

# 构造Request对象
url = "http://httpbin.org/post"
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
    'Host': 'httpbin.org'
}
dict = {
    'name': 'Germey'
}
data = bytes(parse.urlencode(dict), encoding='utf8')
req = request.Request(url=url, data=data, headers=headers, method='POST')
response = request.urlopen(req)
print(response.read().decode('utf-8'))
