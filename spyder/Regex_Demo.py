# -*- coding:utf-8 -*-

import re

str = "hello, world, life is short Using Python. What?"

result = re.search(r"\w+", str)
print(result.group())

# 匹配world，不区分大小写
b = re.search(r"w.+D", str, re.I)
print(b.group())

# 匹配字符串中所有的 (单词和数字(alphanumeric))组成的字符串
c = re.findall(r"\w+", str)
print(c)
