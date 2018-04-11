from urllib import request, error

try:
    request.urlopen("http://blog.csdn.net")
except error.URLError as e:
    print(e.code)
    print(e.reason)