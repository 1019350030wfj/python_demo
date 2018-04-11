from urllib import request

for i in range(1, 100):
    try:
        response = request.urlopen("http://yum.iqianyue.com", timeout=1)
        data = response.read()
        print(len(data))
    except Exception as e:
        print("出现异常-->"+str(e))
