# !/usr/bin/python3
# -*- coding:utf-8 -*-
'''
Author: jc feng
File Created: 2019-08-21 15:56:29
Last Modified: 2019-09-25 20:53:33
'''

import time
import json
import datetime
from spider import AlzaSpider
from utils.file import build_file_name
from utils.csv import write_csv
from utils.mail import Email
from utils.date import last_date
from config import TO_ADDRESS


def load_config():
    with open('./goods_config.json', 'r', encoding='utf8') as f:
        return json.load(f)


def daily_spider():
    last_day = last_date()
    files = []
    for data_config in load_config()['datalist']:
        category = data_config['category']
        category_id = data_config['idCategory']
        # spider
        result_list = AlzaSpider.main_page_spider(category_id)
        headers = [
            'date',
            'rank',
            'name',
            'price',
            'today_purchased',
            'this_week_purchased',
            'now_viewing_customers_count',
            'link',
        ]
        for result in result_list:
            detail = AlzaSpider.detail_page_spider(result['link'])
            result.update(detail)
            result.update({'date': last_day})
        # 本地csv保存
        file_name = build_file_name(category)
        write_csv(file_name, headers, result_list)
        files.append(file_name)
    # 邮件发送
    msg = Email.build_msg(TO_ADDRESS, f"{last_day} Alza 数据定时发送", "", files)
    Email.send_email(TO_ADDRESS, msg)


if __name__ == "__main__":
    daily_spider()
    while True:
        print('程序运行中')
        now = datetime.datetime.now()
        if now.hour == 5 and now.minute == 50:
            daily_spider()
        time.sleep(60)
