# coding: utf-8

import pymysql

# connect database
db = pymysql.connect("localhost", "root", "root", "TESTDB")

# use the method of cursor to create cursor object
cursor = db.cursor()

# sql 插入语句
insert_sql = """insert into employee(first_name,
            last_name,age,sex,income) 
            VALUES ('jayden','wang',20,'M',2000)"""
try:
    # 执行sql语句
    cursor.execute(insert_sql)
    # 提交到数据库执行
    db.commit()
except:
    # 如果发送错误则回滚
    db.rollback()

# # SQL 插入语句
# sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
#        LAST_NAME, AGE, SEX, INCOME) \
#        VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
#        ('Mac', 'Mohan', 20, 'M', 2000)

# 关闭数据库链接
db.close()
