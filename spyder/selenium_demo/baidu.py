'''
使用selenium模拟浏览器
抓去百度查询结果
'''

# 导入selenium模块中的web引擎
from selenium import webdriver

# 建立浏览器对象，通过phantom.js
browser = webdriver.PhantomJS()

url = "https://www.baidu.com"

browser.get(url)

browser.implicitly_wait(3)

text = browser.find_element_by_id('kw')

text.clear()

text.send_keys("python")

button = browser.find_element_by_id("su")

button.submit()

print(browser.title)

browser.save_screenshot("text.png")

results = browser.find_elements_by_class_name("t")

for result in results:
    print("title: {} link: {}".format(result.text, result.find_element_by_tag_name("a").get_attribute("href")))


















