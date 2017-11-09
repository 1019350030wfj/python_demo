# coding: utf-8

import pymysql

# connect database
db = pymysql.connect("localhost", "root", "root", "TESTDB")

# use the method of cursor to create cursor object
cursor = db.cursor()

# use the method of execute to carry out searching sql
cursor.execute("SELECT VERSION()")

# use fetchone() get one single data
data = cursor.fetchone()

print("Database version : %s" % data)

# 使用execute（）方法执行SQL,如果表存在则删除
cursor.execute("drop table if exists employee")

# 使用预处理语句创建表
sql = """ create table employee (
            first_name char(20) not null,
            last_name char(20),
            age int,
            sex char(1),
            income FLOAT )
        """
cursor.execute(sql)

# 关闭数据库链接
db.close()
