# -*- coding:utf-8 -*-
from splinter import Browser
import time

with Browser() as browser:
    url = "http://www.baidu.com"
    browser.visit(url)
    browser.fill('wd', 'splinter - phthon acceptance testing for web application')
    button = browser.find_by_id('su')
    button.click()
    time.sleep(4)
    href = browser.click_link_by_text(u'刘亦菲深夜发文')
    # href.click()
    if browser.is_text_present(u'的最新相关信息'):
        print "Yes, the official website was found!"
    else:
        print "No, it wasn't found... We need to improve our SEO techniques"