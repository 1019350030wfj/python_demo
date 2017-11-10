# coding=utf-8

"""
等额本息
总支付利息：237096.11	本息合计：617096.11 	每月 2571.23
总共240个月
"""

initial_payment = 2571.23
total_month = 240
sum = 0
counter = 1
while counter <= 240:
    sum += initial_payment
    counter += 1

print("等额本息：第1月 到 第%d月 贷款总和为：%.2f " % (counter-1, sum))