'''
模拟浏览器爬虫

爬取快代理： http://www.kuaidaili.com
'''
from selenium import webdriver

class Item(object):
    '''
    我们模拟scrapy框架
    写一个item类出来，
    用来表示每一个爬到的代理
    '''
    ip = None  # ip address
    port = None  # ip port
    anonymous = None  # whether anonymous
    type = None  # http or https
    local = None  # physical address
    speed = None  # speed


class GetProxy(object):
    '''
    获取代理的类
    '''

    def __init__(self):
        '''
        初始化整个类
        '''
        self.starturl = "http://www.kuaidaili.com/free/inha/"
        self.urls = self.get_urls()
        self.proxylist = self.get_proxy_list(self.urls)
        self.filename = 'proxy.txt'
        self.saveFile(self.filename, self.proxylist)

    def get_urls(self):
        '''
        返回一个代理url的列表
        :return:
        '''
        urls = []
        for i in range(1, 2):
            url = self.starturl + str(i)
            urls.append(url)
        return urls

    def get_proxy_list(self, urls):
        '''
        返回抓去到代理的列表
        整个爬虫的关键
        :param urls:
        :return:
        '''

        browser = webdriver.PhantomJS()
        proxy_list = []

        for url in urls:
            browser.get(url)
            browser.implicitly_wait(3)
            # 找到代理table的位置
            elements = browser.find_elements_by_xpath("//tbody/tr")

            for element in elements:
                item = Item()
                item.ip = element.find_element_by_xpath("./td[1]").text
                item.port = element.find_element_by_xpath("./td[2]").text
                item.anonymous = element.find_element_by_xpath("./td[3]").text
                item.type = element.find_element_by_xpath("./td[4]").text
                item.local = element.find_element_by_xpath("./td[5]").text
                item.speed = element.find_element_by_xpath("./td[6]").text
                print(item.ip)
                proxy_list.append(item)

        browser.quit()
        return proxy_list

    def saveFile(self, filename, proxy_list):
        '''
        将爬取到的代理写到文件
        :param filename:
        :param proxy_list:
        :return:
        '''
        with open(filename, 'w', encoding="utf-8") as f:
            for proxy in proxy_list:
                f.write("ip: " + proxy.ip + "\t")
                f.write("port: " + proxy.port + "\t")
                f.write("anonymous: " + proxy.anonymous + "\t")
                f.write("type: " + proxy.type + "\t")
                f.write("local: " + proxy.local + "\t")
                f.write("speed: " + proxy.speed + "\n\n")


if __name__ == '__main__':
    Get = GetProxy()