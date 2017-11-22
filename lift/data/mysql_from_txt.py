# -*- coding: utf-8 -*-

import pymysql
import sys


def create_table(conn):
    sql_drop_table = "drop table if EXISTS lift_details;"
    sql_create_table = "create table if not exists lift_details(" \
                       "_id int auto_increment," \
                       "device_id varchar(16)," \
                       "r_device_category varchar(64)," \
                       "r_rated_load varchar(64)," \
                       "r_layer_number varchar(64)," \
                       "r_rated_speed varchar(64)," \
                       "r_maintenance_name varchar(64)," \
                       "r_maintenance_phone varchar(64)," \
                       "r_put_into_use_date varchar(64)," \
                       "r_manufacture_unit varchar(64)," \
                       "r_installation_unit varchar(64)," \
                       "r_using_unit varchar(64)," \
                       "r_examination_date varchar(64)," \
                       "r_examination_result varchar(64)," \
                       "r_examination_report varchar(64)," \
                       "r_effective_expiration_date varchar(64)," \
                       "r_buffer_form varchar(64)," \
                       "r_door_opening_mode varchar(64)," \
                       "r_heavy_blocks_number varchar(64)," \
                       "r_top_height varchar(64)," \
                       "r_pit_depth varchar(64)," \
                       "r_motor_category varchar(64)," \
                       "r_motor_type varchar(64)," \
                       "r_motor_power varchar(64)," \
                       "r_rated_current varchar(64)," \
                       "primary key(_id)" \
                       ")"
    cursor = conn.cursor()
    try:
        cursor.execute(sql_drop_table)
        cursor.execute(sql_create_table)
        conn.commit()
    except:
        conn.rollback()


def load_data(conn, data_path):
    cursor = conn.cursor()
    sql_load_data = 'load data local infile \'{0}\' into table lift_details ' \
                    'fields terminated by \';\' enclosed by \'"\' ' \
                    'lines terminated by \'\n\' ' \
                    '(device_id,r_device_category,r_rated_load,r_layer_number,r_rated_speed,r_maintenance_name,r_maintenance_phone,' \
                    'r_put_into_use_date,r_manufacture_unit,r_installation_unit,r_using_unit,r_examination_date,r_examination_result,' \
                    'r_examination_report,r_effective_expiration_date,r_buffer_form,r_door_opening_mode,r_heavy_blocks_number,r_top_height,' \
                    'r_pit_depth,r_motor_category,r_motor_type,r_motor_power,r_rated_current)'.format(data_path)
    try:
        cursor.execute(sql_load_data)
        conn.commit()
    except:
        print("Unexpected error:", sys.exc_info()[0])
        conn.rollback()

if __name__ == '__main__':
    connection = pymysql.connect("localhost", "root", "root", "lift_detail", local_infile=1)
    create_table(connection)
    path = 'lift_details.txt'
    load_data(connection, path)
    connection.close()
