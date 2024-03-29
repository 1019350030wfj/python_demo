# -*- coding:utf-8 -*-

'''
查询两站之间的火车票信息
输入参数 data from to
api:
https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2017-08-19&leftTicketDTO.from_station=NJH&leftTicketDTO.to_station=SZH&purpose_codes=ADULT
'''
import requests
import json
from train_stations import stations_dict

# 关闭https证书验证警告
requests.packages.urllib3.disable_warnings()

# 城市名代码查询字典
# key： 城市名 value： 城市代码


# 反转k,v 形成新的字典
code_dict = {v: k for k, v in stations_dict.items()}


def get_query_url(text):
    '''
    返回调用api的url链接
    :param text:
    :return:
    '''
    # 解析参数aggs[0] 里是固定字符串： 车票查询 用于匹配公众号接口
    args = str(text).split(' ')
    try:
        date = args[1]
        from_station_name = args[2]
        to_station_name = args[3]
        from_station = stations_dict[from_station_name]
        to_station = stations_dict[to_station_name]
    except:
        date, from_station, to_station = '--', '--', '--'

    # 将城市名转换为城市代码

    # api url构造
    url = (
        'https://kyfw.12306.cn/otn/leftTicket/query?'
        'leftTicketDTO.train_date={}&'
        'leftTicketDTO.from_station={}&'
        'leftTicketDTO.to_station={}&'
        'purpose_codes=ADULT'
    ).format(date, from_station, to_station)
    print(url)

    return url

def query_train_info(url):
    '''
    查询火车票信息
    返回 信息查询列表
    :param url:
    :return:
    '''
    info_list = []
    try:
        r = requests.get(url, verify=False)
        # 获取返回的json数据里的data字段的result结果
        raw_trains = r.json()['data']['result']

        for raw_train in raw_trains:
            # 循环遍历每辆列车的信息
            data_list = raw_train.split('|')

            # 车次号码
            train_no = data_list[3]
            # 出发站
            from_station_code = data_list[6]
            from_station_name = code_dict[from_station_code]

            # 终点站
            to_station_code = data_list[7]
            to_station_name = code_dict[to_station_code]

            # 出发时间
            start_time = data_list[8]
            # 到达时间
            arrive_time = data_list[9]
            # 总耗时
            time_fucked_up = data_list[10]
            # 一等座
            first_class_seat = data_list[31] or '--'
            # 二等座
            second_class_seat = data_list[30] or '--'
            # 软卧
            soft_sleep = data_list[23] or '--'
            # 硬卧
            hard_sleep = data_list[28] or '--'
            # 硬座
            hard_seat = data_list[29] or '--'
            # 无座
            no_seat = data_list[26] or '--'

            # 打印查询结果
            info = (('车次:{}  出发站:{}  目的地:{}  出发时间:{}  到达时间:{}  消耗时间:{}\n座位情况：'
                    '   一等座：「{}」\t二等座：「{}」\t软卧：「{}」\t硬卧：「{}」\t硬座：「{}」\t无座：「{}」').format(
                train_no, from_station_name, to_station_name, start_time, arrive_time, time_fucked_up, first_class_seat,
                second_class_seat, soft_sleep, hard_sleep, hard_seat, no_seat))

            info_list.append(info)
        return info_list
    except:
        return '输出信息有误，请重新输入'

date = '2017-08-25'
from_station = '厦门'
to_station = '惠安'


info_list = query_train_info(get_query_url('车票查询 {} {} {}'.format(date, from_station, to_station)))
for info in info_list:
    print(info, '\n', '=' * len(info))