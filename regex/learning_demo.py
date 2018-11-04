# -*- coding:utf-8 -*-
import re

# ^
str1 = "hello world"
# # pattern1 = "^world"
# pattern1 = "^hello"
# print(re.sub(pattern1, "meipai", str1))

# $
# # pattern3 = "world$"
# pattern3 = "hello$"
# print(re.sub(pattern3, "meipai", str1))

# ^ $
# str_qq = "1019350030123"
# pattern5 = "^\d{5,12}$"
# print(re.match(pattern5, str_qq))

# \b    单词边界    https://blog.csdn.net/uvyoaa/article/details/80854459
# str_b = "rhythm schoolshape technology rhythmtechnology school language"
# # pattern_b = "rhythm"
# pattern_b = r"\brhythm\b"
# print(re.findall(pattern_b, str_b))

# 表示字母数字与非字母数字的边界，     非字母数字与字母数字的边界
# print(re.split('123', '==123!! abc123. 123. 123abc. 123'))
# print(re.split('123\\b', '==123!! abc123. 123. 123abc. 123'))


# * ？ + {n,m}
# print(re.match(r'(meipai)*', "meipaimeipai").group())
# print(re.match(r'\w?', "meipai").group())
# print(re.match(r'meipai+', "meipai").group())
# print(re.match(r'meipai{3,5}', "meipaiii").string)


# re.I re.M re.S re.X
# str_i = "Meipai!"
# re_c_i = re.compile("meipai!")
# print(re_c_i.match(str_i).group())

# re.M
# str_m = "meitu line\nmeipai line\njayden line"
# re_not_m = re.compile(r'^\w+')
# print(re_not_m.findall(str_m))
# #
# re_h_m = re.compile(r'^\w+', re.M)
# print(re_h_m.findall(str_m))

# re.S
# str_s = '''meitu line
# meipai line
# jayden line
# '''
# re_not_s = re.compile('.+')
# print(re_not_s.findall(str_s))
# #
# re_h_s = re.compile('.+', re.S)
# print(re_h_s.findall(str_s))

# re.X
# re_email = re.compile("[\w+\.]+@[a-zA-Z\d]+\.(com|cn|net)")
# re_email_h_X = re.compile("""[\w+\.]+  # 匹配@符前的部分
#                             @  # @符
#                             [a-zA-Z\d]+  # 邮箱类别
#                             \.(com|cn|net)   # 邮箱后缀  """, re.X)

# 贪婪 and 懒惰
str_jin = "#hello#world#"
print(re.match("#.*#", str_jin))  # 贪婪模式 输出 #hello#world#
print(re.match("#.*?#", str_jin))  # 非贪婪模式 输出 #hello#
