import re
from urllib import request, error


def traverse(pattern, html, page, x):
    image_url_list = pattern.findall(html)

    for image_url in image_url_list:
        image_path = str(page) + str(x) + '.jpg'
        image_url = 'http://' + image_url
        try:
            request.urlretrieve(image_url, image_path)
        except error.URLError as e:
            if hasattr(e, "code"):
                x += 1
            if hasattr(e, "reason"):
                x += 1

        x += 1


def craw_phone_image(url, page):
    # 编写正则表达式
    pattern1 = re.compile(r'<img width="220" height="220" data-img="1" data-lazy-img="//(.+?\.jpg)">')
    # pattern2 = re.compile(r'<img width="220" height="220" data-img="1" src="//(.+?\.jpg)">')

    # 爬取网页数据
    html = request.urlopen(url).read()
    # read是 字节数据， 转为字符串
    html = str(html)
    x = 1
    traverse(pattern1, html, page, x)
    # traverse(pattern2, html, page, x)


jd_phone_url = 'https://list.jd.com/list.html?cat=9987,653,655&page=1&sort=sort_rank_asc&trans=1&JL=6_0_0&ms=6#J_main'
craw_phone_image(jd_phone_url, 1)

