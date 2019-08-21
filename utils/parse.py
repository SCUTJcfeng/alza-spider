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
    def parse_alza_main(html_txt):
        soup = HtmlParse.use_lxml(html_txt)
        best_items = soup.findAll(class_=re.compile("bestitem"))
        for item in best_items:
            div_b1a = item.find('div', class_=re.compile('b1a')).contents[1]
            # rank = div_b1a.contents[0]
            # rank = item.find(class_='b1a')
            print(item.string)
        pass
        # div_list = besti.find(class_)
        # print(besti.string if besti else None)
