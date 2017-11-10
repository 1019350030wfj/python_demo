# coding=utf-8

"""
等额本金
总支付利息：202239.17	本息合计：582239.17
首月还款 3261.67
逐月递减6.99
总共240个月
"""

# initial_payment = 3261.67
# subtraction = 6.99
# total_month = 240
# sum = 0
# counter = 1
# while counter <= total_month:
#     sum += initial_payment
#     initial_payment -= subtraction
#     counter += 1
#
# print("等额payment = 3261.67

initial_payment = 3264.83
subtraction = 7.01
total_month = 84
sum = 0
counter = 1
while counter <= total_month:
    sum += initial_payment
    initial_payment -= subtraction
    counter += 1

print("等额本金 第1月 到 第%d月 贷款总和为：%.2f " % (counter-1, sum))