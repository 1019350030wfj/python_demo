# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import lxml

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, "html.parser")
# 美化、格式化上面的html_doc
print(soup.prettify())

# 标题
print(soup.title)

# 标题名称
print(soup.title.name)

# 列出soup.title的所有属性和方法
print(dir(soup.title))

# 从文档中找到所有<a>标签的链接:
for link in soup.find_all("a"):
    # print(link["href"])
    print(link.get("href"))

# 从文档中获取所有文字内容:
print(soup.get_text())
