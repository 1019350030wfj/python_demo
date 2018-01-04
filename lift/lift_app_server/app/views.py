from app import app
from flask import jsonify, request
import json
from flask_cors import *
import pymysql


@app.route('/')
@app.route('/index')
def index():
    return 'Hello, World!'


import contextlib
# 定义上下文管理器，连接后自动关闭连接
@contextlib.contextmanager
def mysql(host='127.0.0.1', port=3306, user='root', passwd='root', db='lift_detail', charset='utf8'):
    conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    try:
        yield cursor
    finally:
        conn.commit()
        cursor.close()
        conn.close()


@app.route('/lift/<device_category>', methods=['GET', 'POST'])
@cross_origin()
def getDataByCategory(device_category):
    # data = request.args.get("data")  # 获取前台json数据
    # temp = json.loads(data)  # 将json转为字典
    # id = temp['id']  # 获取相应的值
    with mysql() as cursor:
        print(cursor)
        row_count = cursor.execute("select * from lift_details_notd where r_device_category=%s", (device_category))
        # row_1 = cursor.fetchone()
        return jsonify(status=200,
                   info=json.dumps(cursor.fetchall()),
                   msg='success')
    conn.commit()
    cursor.close()
    conn.close()
