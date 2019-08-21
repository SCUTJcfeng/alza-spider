# !/usr/bin/python3
# -*- coding:utf-8 -*-
'''
Author: jc feng
File Created: 2019-08-21 16:01:12
Last Modified: 2019-08-21 19:16:30
'''

import re
from bs4 import BeautifulSoup


class HtmlParse:

    @staticmethod
    def use_lxml(html_txt):
        return BeautifulSoup(html_txt, 'lxml')

    @staticmethod
    def parse_alza_main(html_txt, date):
        soup = HtmlParse.use_lxml(html_txt)
        best_items = soup.findAll(class_=re.compile("bestitem"))
        result_list = []
        for item in best_items:
            div_b1a_tag = item.find('div', class_=re.compile('b1a'))
            rank = div_b1a_tag.string.replace('\r\n', '').replace('.', '')

            browsing_link_tag = item.find('a', class_='bt1 browsinglink')
            name = browsing_link_tag.string
            link = 'https://www.alza.cz' + browsing_link_tag['href']

            span_b32_tag = item.find('span', class_='b32')
            now_price = span_b32_tag.string.replace(',', '').replace('-', '').replace('\xa0', '')
            print(rank, name, now_price, link)
            result_list.append({
                'name': name,
                'rank': int(rank),
                'price': float(now_price),
                'link': link,
                'date': date
            })
        return result_list
