# !/usr/bin/python3
# -*- coding:utf-8 -*-
'''
Author: jc feng
File Created: 2019-08-21 15:56:29
Last Modified: 2019-08-21 17:08:21
'''

import time
import datetime
from spider import AlzaSpider
from utils.file import build_file_name
from utils.csv import write_csv


def daily_spider():
    result_list = AlzaSpider.main_page_spider()
    for result in result_list:
        detail = AlzaSpider.detail_page_spider(result['link'])
        result.update(detail)
        headers = ['date', 'rank', 'name', 'price', 'today_purchased', 'this_week_purchased', 'now_viewing_customers_count', 'link']
    write_csv(build_file_name(), headers, result_list)


if __name__ == "__main__":
    daily_spider()
    while True:
        print('程序运行中')
        now = datetime.datetime.now()
        if now.hour == 5 and now.minute == 50:
            daily_spider()
        time.sleep(60)
