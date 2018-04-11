from urllib import request, parse

url = "http://yum.iqianyue.com"
postdata = parse.urlencode({
    "name": "ceo@iqianyue.com",
    "pass": "aA123456"
}).encode("utf-8") #将数据使用urlencode编码处理后，使用encode（）设置为utf-8
req = request.Request(url, postdata)
req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36")
res = request.urlopen(req)
data = res.read()
print(data)