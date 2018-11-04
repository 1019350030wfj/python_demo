# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup


# 获取网页的内容

def get_html(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = "utf-8"
        return r.text
    except:
        return "ERROR"


def get_content(url):
    '''
    分析贴吧的网页文件，整理信息，保存到列表变量中
    :param url:  网页地址
    :return: 列表信息
    '''
    # 初始化一个列表来保存所有的帖子信息
    comments = []
    # 首先，我们把需要爬取信息的网页下载到本地
    html = get_html(url)

    # 我们来做一锅汤
    soup = BeautifulSoup(html, "lxml")

    # 按照之前的分析，找到所有具有“ j_thread_list thread_top j_thread_list clearfix”属性的li标签。返回一个列表类型
    liTags = soup.find_all('li', attrs={'class': ' j_thread_list clearfix'})

    # 通过循环找到每个帖子里的我们需要的信息
    for li in liTags:
        # 初始化一个字典来存储文章信息
        comment = {}
        # 这里使用一个try except 防止爬虫找不到信息从而停止运行
        try:
            # 开始筛选信息，并保存到字典中
            comment['title'] = li.find('a', attrs={'class': "j_th_tit "}).text.strip()
            comment['link'] = "http://tieba.baidu.com/" + \
                              li.find('a', attrs={'class': "j_th_tit "})['href']
            comment['name'] = li.find('a', attrs={'class': 'frs-author-name j_user_card '}).text.strip()
            comment['time'] = li.find('span', attrs={'class': 'pull-right is_show_create_time'}).text.strip()
            comment['replyNum'] = li.find('span', attrs={'class': 'threadlist_rep_num center_text'}).text.strip()
            comments.append(comment)
        except:
            print('获取帖子信息错误！！！')
    return comments


def out2File(dict):
    '''
    将爬取到的文件写入到本地
    保存到当前目录的TTBT.txt文件中
    :param dict:
    :return:
    '''
    with open('TTBT.txt', 'a+', encoding='utf-8') as f:
        for comment in dict:
            f.write('标题: {} \t 链接：{} \t 发帖人：{} \t 发帖时间: {} \t 回复数量: {} \n'.format(comment['title'], comment['link'],
                                                                                  comment['name'], comment['time'],
                                                                                  comment['replyNum']))
        print('当前页面爬取完成')


def main(base_url, deep):
    url_list = []
    for i in range(0, deep):
        url_list.append(base_url + "&pn=" + str(50 * i))

    # 循环写入所有数据
    for url in url_list:
        content = get_content(url)
        out2File(content)
    print("所有的信息已经保存到文件！")


base_url = 'http://tieba.baidu.com/f?kw=%E7%94%9F%E6%B4%BB%E5%A4%A7%E7%88%86%E7%82%B8&ie=utf-8'
deep = 1

if __name__ == '__main__':
    main(base_url, deep)
