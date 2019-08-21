# !/usr/bin/python3
# -*- coding:utf-8 -*-
'''
Author: jc feng
File Created: 2019-08-21 21:12:13
Last Modified: 2019-08-21 22:57:20
'''

import csv


def write_csv(file_name, headers, data_list):
    with open(file_name, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        if headers is not None:
            writer.writeheader()
        for row in data_list:
            writer.writerow(row)
    print("%s is writing" % file_name)
