'''
爬取我的钢铁网每日数据

爬取一年内 全国主要城市HRB400螺纹钢价格总汇

url： http://search.mysteel.com/price/list.ms?page=1&bn=1mp56ts&time2=2017-06-01&time1=2015-03-01&bid=01010101

'''

# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
from bs4.element import NavigableString


def get_html(url, cookies):
    try:
        r = requests.get(url, headers={'cookie': cookies}, timeout=30)  # 不用转换为字典
        # r = requests.get(url, cookies=cookies, timeout=30)  转换为字典类型
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("something is wrong")


def get_url(url):
    html = requests.get(url, timeout=15)
    soup = BeautifulSoup(html.text, 'lxml')
    urls = []
    results = soup.find_all("div", class_="resultBox")
    for result in results:
        url = result.find('a')['href']
        urls.append(url)
    return urls


def get_one_data(url, cookie):
    r = get_html(url, cookie)
    soup = BeautifulSoup(r, 'lxml')

    date = soup.find('div', class_='info').contents[1]
    # 判断是否抓到了数据
    if type(date) != NavigableString:
        date = soup.find('div', class_='info').contents[0]

    datalist = soup.find('tr', attrs={'bgcolor': '#FEFBEC'}).contents
    data = datalist[-2].text
    with open('hrb400_20MM.txt', 'a+', encoding="utf-8") as f:
        f.write(date + '\t' + data + '\n')
    print('当前处理日期{}'.format(date))


if __name__ == '__main__':
    base_url = 'http://search.mysteel.com/price/list.ms?page='
    suffix = '&bn=1mp56ts&time2=2017-06-01&time1=2015-03-01&bid=01010101'

    raw_cookie = "gsScrollPos-148=; _login_token=1de3e6b7496943407ef13391cefe88d3; _login_uid=2116343; _login_mid=2934820; _last_loginuname=1019350030wfj; 1de3e6b7496943407ef13391cefe88d3=35%3D5%2617%3D5%2636%3D5%2633%3D5%2634%3D5%2613%3D5%2637%3D5%2611%3D5%2638%3D5%262%3D5%261%3D5%2642%3D5%2632%3D5%2641%3D5%2631%3D5%264%3D5%2640%3D5%26catalog%3D010205%2C010202%2C0222%2C0223%2C0205; Hm_lvt_1c4432afacfa2301369a5625795031b8=1502258524; Hm_lpvt_1c4432afacfa2301369a5625795031b8=1502265218"
    cookies = "gsScrollPos-148=; _login_token=1de3e6b7496943407ef13391cefe88d3; _login_uid=2116343; _login_mid=2934820; _last_loginuname=1019350030wfj; 1de3e6b7496943407ef13391cefe88d3=35%3D5%2617%3D5%2636%3D5%2633%3D5%2634%3D5%2613%3D5%2637%3D5%2611%3D5%2638%3D5%262%3D5%261%3D5%2642%3D5%2632%3D5%2641%3D5%2631%3D5%264%3D5%2640%3D5%26catalog%3D010205%2C010202%2C0222%2C0223%2C0205; Hm_lvt_1c4432afacfa2301369a5625795031b8=1502258524; Hm_lpvt_1c4432afacfa2301369a5625795031b8=1502265218"

    # cookies = {}   # 不用转换为字典
    # for line in raw_cookie.split(";"):
    #     key, value = line.split("=", 1)
    #     cookies[key] = value

    iron_urls = []
    for i in range(1, 58):
        url = base_url + str(i) + suffix
        iron_urls.append(url)

    urls = []
    for url in iron_urls:
        urls += (get_url(url))

    for url in urls:
        get_one_data(url, cookies)

    print("所有数据写入")
