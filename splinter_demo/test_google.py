# -*- coding:utf-8 -*-
from splinter import Browser

with Browser() as browser:
    url = "http://www.baidu.com"
    browser.visit(url)
    browser.fill('wd', 'splinter - phthon acceptance testing for web application')
    button = browser.find_by_id('su')
    button.click()
    if browser.is_text_present('splinter.readthedocs.io'):
        print "Yes, the official website was found!"
    else:
        print "No, it wasn't found... We need to improve our SEO techniques"