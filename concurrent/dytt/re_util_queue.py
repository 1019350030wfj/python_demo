# -*- coding: utf-8 -*-

import re

#  匹配影片详情url
r_url = re.compile('<b>.*?<a\s*href="(.*?)"\s*class="ulink">', re.DOTALL)


# 匹配影片详情
r_name_cn = re.compile(u"◎译　　名(.*?)<br />", re.DOTALL)
r_name = re.compile(u"◎片　　名(.*?)<br />", re.DOTALL)
r_year = re.compile(u"◎年　　代(.*?)<br />", re.DOTALL)
r_country = re.compile(u"◎(产　　地|国　　家)(.*?)<br />", re.DOTALL)
r_category = re.compile(u"◎类　　别(.*?)<br />", re.DOTALL)
r_language = re.compile(u"◎语　　言(.*?)<br />", re.DOTALL)
r_subtitle = re.compile(u"◎字　　幕(.*?)<br />", re.DOTALL)
r_release_date = re.compile(u"◎上映日期(.*?)<br />", re.DOTALL)
r_score = re.compile(u"◎(IMDB评分|豆瓣评分)(.*?)<br />", re.DOTALL | re.IGNORECASE)
r_file_size = re.compile(u"◎文件大小(.*?)<br />", re.DOTALL)
r_movie_duration = re.compile(u"◎片　　长(.*?)<br />", re.DOTALL)
r_director = re.compile(u"◎导　　演(.*?)<br />", re.DOTALL)

r_download_url = re.compile('<td.*?bgcolor="#fdfddf">.*?<a.*?>(.*?)</a>', re.DOTALL)

r_list = (r_name_cn,
          r_name,
          r_year,
          r_country,
          r_category,
          r_language,
          r_subtitle,
          r_release_date,
          r_score,
          r_file_size,
          r_movie_duration,
          r_director)


# 提取电影url
def extract_urls(html, in_queue):
    segments = r_url.findall(html)
    host = "http://www.ygdy8.net"
    for segment in segments:
        in_queue.put(host + segment)


# 提前电影详情
def extract_details(html):
    details = ''
    if html:
        fields = []
        for regex in r_list:
            m = regex.search(html)
            if not m:
                field = ''
            else:
                field = m.group(m.lastindex).replace('&nbsp;', '').replace(';', ',').strip()
            fields.append(field)

        urls = r_download_url.findall(html) #<class 'list'>: ['ftp://ygdy8:ygdy8@yg45.dydytt.net:8071/[阳光电影www.ygdy8.com].极寒之城.BD.720p.中英双字幕.mkv']
        field = ''
        if urls:
            for url in urls:
                field = field + url.strip()
                if urls.index(url) != len(urls) - 1:
                    field = field + ','
        fields.append(field)
        details = ''.join(map(lambda x: '"' + x + '";', fields)) + '\n'
    return details
#"极寒之城/极冻之城(台)/原子杀姬(港)/原子美人/最冷的城市";"Atomic Blonde";"2017";"美国";"动作/悬疑/惊悚";"英语";"中英双字幕";"2017-03-12(西南偏南电影节)/2017-07-28(美国)";"7.0/10 from 38,612 users";"1CD";"115分钟";"大卫&middot,里奇 David Leitch";"ftp://ygdy8:ygdy8@yg45.dydytt.net:8071/[阳光电影www.ygdy8.com].极寒之城.BD.720p.中英双字幕.mkv";
