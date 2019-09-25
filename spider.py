# !/usr/bin/python3
# -*- coding:utf-8 -*-
'''
Author: jc feng
File Created: 2019-08-21 23:09:12
Last Modified: 2019-09-25 21:41:49
'''

from utils.http import Http
from utils.parse import HtmlParse


class AlzaSpider:
    @staticmethod
    def main_page_spider(category_id):
        url = 'https://www.alza.cz/Services/EShopService.svc/GetBestsellers'
        form_data = {
            'categoryType': 1,
            'idCategory': category_id,
            'idPrefix': 0,
            'leasingCatId': None,
            'maxPrice': -1,
            'minPrice': -1,
            'parameters': [],
            'producers': "",
            'shouldDisplayVirtooal': False,
        }
        headers = {'Content-Type': 'application/json; charset=UTF-8'}
        cookies = {'LNG': 'EN'}
        html_data = Http.post_for_json(url, form_data, headers, cookies)
        if html_data and 'd' in html_data:
            return HtmlParse.parse_alza_main(html_data['d'])
        return []

    @staticmethod
    def detail_page_spider(url):
        html_txt = Http.get_for_txt(url)
        print(f'正在解析: {url}')
        return HtmlParse.parse_alza_detail(html_txt)
