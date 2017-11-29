# -*- coding: utf-8 -*-

import os


def del_dir_tree(path):
    ''' 递归删除目录及其子目录,　子文件'''
    if os.path.isfile(path):
        try:
            if 're_file.py' not in path:
                os.remove(path)
        except Exception as e:
            print(e)
    elif os.path.isdir(path):
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            del_dir_tree(item_path)
        # try:
        #     os.rmdir(path)  # 删除空目录
        # except Exception as e:
        #     print(e)

if __name__ == '__main__':
    dir_name = os.path.dirname(os.path.realpath(__file__))
    del_dir_tree(dir_name)
