# !/usr/bin/python3
# -*- coding:utf-8 -*-
'''
Author: jc feng
File Created: 2019-08-21 23:01:07
Last Modified: 2019-08-24 17:51:42
'''

import datetime


def last_date():
    lastday = datetime.datetime.now() + datetime.timedelta(days=-1)
    return lastday.strftime('%Y-%m-%d')
