
# !/usr/bin/python3
# -*- coding:utf-8 -*-
'''
Author: jc feng
File Created: 2019-08-21 23:09:12
Last Modified: 2019-08-21 23:48:01
'''

from utils.http import Http
from utils.parse import HtmlParse
from utils.date import today_date


class AlzaSpider:

    @staticmethod
    def main_page_spider():
        url = 'https://www.alza.cz/Services/EShopService.svc/GetBestsellers'
        form_data = {
            'categoryType': 1,
            'idCategory': 18843092,
            'idPrefix': 0,
            'leasingCatId': None,
            'maxPrice': -1,
            'minPrice': -1,
            'parameters': [],
            'producers': "",
            'shouldDisplayVirtooal': False
        }
        headers = {
            'Content-Type': 'application/json; charset=UTF-8'
        }
        html_data = Http.post_for_json(url, form_data, headers)
        if html_data and 'd' in html_data:
            date = today_date()
            return HtmlParse.parse_alza_main(html_data['d'], date)
        return []

    @staticmethod
    def detail_page_spider(url):
        html_txt = Http.get_for_txt(url)
        print(f'正在解析: {url}')
        return HtmlParse.parse_alza_detail(html_txt)
