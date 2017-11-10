# coding: utf-8

import pymysql

# connect database
db = pymysql.connect("localhost", "root", "root", "TESTDB")

# use the method of cursor to create cursor object
cursor = db.cursor()

# SQL 删除语句
sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (20)
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 提交修改
   db.commit()
except:
   # 发生错误时回滚
   db.rollback()


# 关闭数据库链接
db.close()
