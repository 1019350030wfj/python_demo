# -*- coding:utf-8 -*-

import re


D_str = "mei"
D_p = r'\D{3}'
print(re.match(D_p, D_str))

def fun(m):
    img_tag = m.group()
    src = m.group(1)
    if not src.startswith("http:"):
        full_src = "http://foofish.net" + src
    else:
        full_src = src
    new_img_tag = img_tag.replace(src, full_src)
    return new_img_tag


html = """
        <img src="/images/category.png">
        this is anothor words
        <img src="http://foofish.net/images/js_framework.png">
       """
pattern_html = r'.*?<img src="(.*?)".*?>'
print(re.findall(pattern_html, html))

new_html = re.compile(pattern_html).sub(fun, html)
print(new_html)

h_pattern = "<(\w+)>"
h_str = "<html>"
print(re.match(h_pattern, h_str).group(1))

bpattern = r'\bhi\b.*\bLucky\b'
bstr = "hi helloworld Lucky"
print(re.match(bpattern, bstr).group())

python = "hello python"
pPattern = "^hello python$"
pPattern1 = "h(.*?)n"

print(re.findall(pPattern, python))
print(re.findall(pPattern1, python))

string = "3\\8"
m = re.search(r'(\d+)\\', string)
if m is not None:
    print(m.group(1))
n = re.search('(\d+)\\\\', string)
if n is not None:
    print(n.group(1))

p = re.search('(\\\\){2}', string)
if p is not None:
    print(p.group(0))

space = "i\\"
print(re.findall(r'^i\\', space))

# matchObj = re.match(r"(#(.*?)#)|((.*?)#)|(#(.*?))", "#wfj#")
# if matchObj:
#     print("match --> matchObj.group() : ", matchObj.group(2), re.I)
# else:
#     print('not match')
str = "123456meipai"
pattern = "pai$"
obj = re.search(pattern, str)
print(obj.group(0))

phone = '18898537584 #this is my telephone number'
print(re.sub('\D', '', phone))

colors = '''The colors of the rainbow have many colours 
and the rainbow does not  have a single colour.
'''
print(re.findall(r'colou?rs?', colors))

# 匹配5个字母组成的单词
five = '''This is something
is about
a blah
words
sequence of words
Hello and
GoodBye and 
Go gogo!
'''
print(re.match(r'\w', five).group())

string = """
            <html>
                <div><a href='www.baidu.com'></a></div></div></div>
                </div><title>正则</title></div>
                <html><div><a href='www.baidu1.com'></a></div>
                </div></div></div><title>正则1</title></div>
                <html><div><a href='www.baidu2.com'></a>
                </div></div></div></div><title>正则2</title></div>
                <html><div><a href='www.baidu3.com'>
                </a></div></div></div></div><title>正则3</title></div>"""
pattern_string = re.compile(r"<a href='(.*?)'.*?<title>(.*?)</title>", re.S)
res = re.findall(pattern_string, string)
print(res)