# !/usr/bin/python3
# -*- coding:utf-8 -*-
'''
Author: jc feng
File Created: 2019-08-21 23:01:07
Last Modified: 2019-08-21 23:11:14
'''

import datetime


def today_date():
    return datetime.datetime.now().strftime('%Y_%m_%d')
