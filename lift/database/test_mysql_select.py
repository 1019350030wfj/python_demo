# coding: utf-8

import pymysql

# connect database
db = pymysql.connect("localhost", "root", "root", "TESTDB")

# use the method of cursor to create cursor object
cursor = db.cursor()

# sql 查询语句
select_sql = "select * from employee \
      where income > '%d'" % (1000)

try:
    # 执行sql语句
    cursor.execute(select_sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        print("fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
              (fname, lname, age, sex, income))
except:
    print("Error: unable to fetch data")

# 关闭数据库链接
db.close()
