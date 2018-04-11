from urllib import request


def use_proxy(proxy_addr, url):
    # 设置代理服务器信息
    proxy = request.ProxyHandler({'http': proxy_addr})
    opener = request.build_opener(proxy, request.HTTPHandler)
    request.install_opener(opener)
    return request.urlopen(url).read().decode('utf-8')


proxy_addr = "61.135.217.7:80"
data = use_proxy(proxy_addr, "http://www.baidu.com")
print(len(data))