# !/usr/bin/python3
# -*- coding:utf-8 -*-
'''
Author: jc feng
File Created: 2019-08-21 22:44:01
Last Modified: 2019-09-25 21:07:28
'''

import os

base_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
file_path = os.path.join(base_dir, 'output')


def _create_folder():
    if check_if_exist(file_path):
        return
    os.mkdir(file_path)


def build_file_name(category):
    _create_folder()
    return os.path.join(file_path, f'Alza_{category.lower()}_result.csv')


def check_if_exist(file_name):
    return os.path.exists(file_name)
