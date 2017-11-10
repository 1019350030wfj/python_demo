# coding: utf-8

import pymysql

# connect database
db = pymysql.connect("localhost", "root", "root", "TESTDB")

# use the method of cursor to create cursor object
cursor = db.cursor()

# SQL 更新语句
update_sql = "update employee set age = age+1 where sex = '%c'" % ('M')

try:
    # 执行sql语句
    cursor.execute(update_sql)
    # 提交到数据库执行
    db.commit()
except:
    print("update error")
    # 发生错误时回滚
    db.rollback()

# 关闭数据库链接
db.close()
