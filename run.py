# !/usr/bin/python3
# -*- coding:utf-8 -*-
'''
Author: jc feng
File Created: 2019-08-21 15:56:29
Last Modified: 2019-08-21 17:08:21
'''

from utils.http import Http
from utils.parse import HtmlParse
from utils.file import build_file_name
from utils.csv import write_csv
from utils.date import today_date

# BASE_URL = 'https://www.alza.cz/sitove-prvky/broadband-routery/18843092.htm'
BASE_URL = 'https://www.alza.cz/Services/EShopService.svc/GetBestsellers'

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

html_data = Http.post(BASE_URL, form_data, headers)

if html_data and 'd' in html_data:
    date = today_date()
    result_list = HtmlParse.parse_alza_main(html_data['d'], date)
    file_name = build_file_name(date)
    headers = ['date', 'rank', 'name', 'price', 'link']
    write_csv(file_name, headers, result_list)


if __name__ == "__main__":
    pass
