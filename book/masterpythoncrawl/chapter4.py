# -*- charset:utf-8 -*-

import urllib.request

file = urllib.request.urlopen("http://www.onesoft.com.cn/")
# fileHandler = open('part4.html', 'wb+')
# fileHandler.write(file.read())
# fileHandler.close()
# print(file.readlines())
print(file.getcode())
print(file.info())
