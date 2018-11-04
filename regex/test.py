# -*- conding:utf-8 -*-
import re

str = '<a href="https://blog.csdn.net/dQCFKyQDXYm3F8rB0/article/details/83449352" target="_blank" data-track-click=\'{"mod":"popu_459","con":",https://blog.csdn.net/dQCFKyQDXYm3F8rB0/article/details/83449352,top"}\'>机器学习大神迈克尔 &middot; 乔丹：我讨厌将机器学习称为AI                        </a>'
pattern = re.compile(r'<div class="list_con">.*?<a.*?>(.*?)</a>')
print(pattern.findall(str))



# <div class="list_con">.*?<a.*?>(.*?)</a>.*?<div class="summary oneline">(.*?)</div>.*?<dl class="list_userbar">.*?<dd class="name">.*?<a.*?>(.*?)</a>.*?<dd class="time">(.*?)</dd>.*?<span class="num">(.*?)</span>.*?<span class="num">(.*?)</span>',
#             re.S)
