import urllib.request

url = "https://blog.csdn.net/yanbober/article/details/51015630"
# data = urllib.request.urlopen(url)

# print(data.getcode())

# Method-1 opener=urllib.request.build_opener()  opener.addheaders（头部信息）
# headers = ("User-Agent", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36")
# opener = urllib.request.build_opener()
# opener.addheaders = [headers]
# data = opener.open(url).read()
# print(data)

# Method-2 req=urllib.request.Request req.add_header()
req = urllib.request.Request(url)
req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36")
data = urllib.request.urlopen(req).read()
print(data)
