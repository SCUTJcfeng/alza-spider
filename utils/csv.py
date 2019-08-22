# !/usr/bin/python3
# -*- coding:utf-8 -*-
'''
Author: jc feng
File Created: 2019-08-21 21:12:13
Last Modified: 2019-08-22 09:43:18
'''

import csv
from utils.file import check_if_exist


def write_csv(file_name, headers, data_list):
    file_exists = check_if_exist(file_name)
    with open(file_name, 'a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        if not file_exists and headers:
            writer.writeheader()
        for row in data_list:
            writer.writerow(row)
    print("%s is writing" % file_name)
