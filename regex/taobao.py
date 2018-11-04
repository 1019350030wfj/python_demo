# -*- coding:utf-8 -*-

import re
import requests


def getPageCode(url):
    try:
        headers = {'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",'cookie': "t=3e8f19e344c28ce66ba51498e607683e; cookie2=16513ca497b273feec88d6ac9ab786c0; v=0; _tb_token_=313fa6d34efeb; cna=VoJdFPYfNgsCAW5WARJG6ijG; unb=908299285; sg=j5d; _l_g_=Ug%3D%3D; skt=44009d1200c81eec; cookie1=VANFwamkOBm4DbojTFlu2YgBB5HNsT1el%2FabuhHFlWk%3D; csg=bd4de811; uc3=vt3=F8dByRjO3xY3kesN7us%3D&id2=WvA8PAoZTCA9&nk2=UoH%2B7%2B9f2EeSRpsplQ%3D%3D&lg2=UtASsssmOIJ0bQ%3D%3D; existShop=MTU0MDk1Mzg2MQ%3D%3D; tracknick=1019350030wfj; lgc=1019350030wfj; _cc_=WqG3DMC9EA%3D%3D; dnk=1019350030wfj; _nk_=1019350030wfj; cookie17=WvA8PAoZTCA9; tg=0; enc=lqQtQNSvxJCMvWUy0AVvBlWzA0cTz5%2FVLjHyd4sZccD01YqacYrODk0a20OR%2B%2FjXoxvUcsAfZCQl7xIGtAyQQQ%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; thw=cn; mt=ci=0_1; JSESSIONID=01E5ADA9557DEDC88F94984320EA2478; isg=BImJ5yMTNuFAWMoVjVxs-2ADmLNPwi3x_4gvUSv-PnD0cqmEcyTD2HYgsJbhKhVA; uc1=cookie14=UoTYNk79PErkeA%3D%3D&lng=zh_CN&cookie16=Vq8l%2BKCLySLZMFWHxqs8fwqnEw%3D%3D&existShop=false&cookie21=WqG3DMC9FxUx&tag=8&cookie15=VFC%2FuZ9ayeYq2g%3D%3D&pas=0"}
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def parsePage(itemList, html):
    titleList = re.findall(r'"raw_title":".*?"', html)
    priceList = re.findall(r'"view_price":"[\d.]*"', html)
    for i in range(len(titleList)):
        itemList.append([eval(titleList[i].split(':')[1]), eval(priceList[i].split(':')[1])])



def printItemList(itemList):
    demo = "{:^8}{:^12}{}"
    print(demo.format("序号", "价格", "名称"))
    count = 0
    for item in itemList:
        count = count + 1
        print(demo.format(count, item[1], item[0]))


if __name__ == '__main__':
    start_url = "https://s.taobao.com/search?q="
    keyword = "手机"
    itemList = []

    html = getPageCode(start_url + keyword + "&s=" + str(44))
    parsePage(itemList, html)
    printItemList(itemList)
