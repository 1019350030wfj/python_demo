'''
使用selenium模拟浏览器
抓取电梯查询结果
'''

# 导入selenium模块中的web引擎
# from selenium import webdriver
#
# # 建立浏览器对象，通过phantom.js
# browser = webdriver.PhantomJS()
#
# url = "http://117.25.179.165:7003/wapq/elevatorSearch.jsp?&EqpCod=T008858"
#
# browser.get(url)
#
# browser.implicitly_wait(3)
#
# button = browser.find_element_by_name("form")
#
# button.submit()
#
# print(browser.page_source)

import requests

head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',
    'Referer': 'http://117.25.179.165:7003/wapq/elevatorSearch.jsp?&EqpCod=T008859'}
url = 'http://117.25.179.165:7003/wapq/elevator.do?task=search'
data = {
    'eqpCod': "T008859",
    'smsCod': "",
    'regCod': "",
}
loginhtml = requests.post(url, data=data, headers=head)
print(loginhtml)
