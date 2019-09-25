# !/usr/bin/python3
# -*- coding:utf-8 -*-
'''
Author: jc feng
File Created: 2019-08-21 16:01:12
Last Modified: 2019-09-25 21:19:58
'''

import re
from bs4 import BeautifulSoup


class HtmlParse:
    @staticmethod
    def use_lxml(html_txt):
        return BeautifulSoup(html_txt, 'lxml')

    @staticmethod
    def parse_alza_main(html_txt):
        if html_txt == '':
            return []
        soup = HtmlParse.use_lxml(html_txt)
        best_items = soup.findAll(class_=re.compile("bestitem"))
        result_list = []
        for item in best_items:
            div_b1a_tag = item.find('div', class_=re.compile('b1a'))
            rank = div_b1a_tag.string.replace('\r\n', '').replace('.', '')

            browsing_link_tag = item.find('a', class_='bt1 browsinglink')
            name = browsing_link_tag.string
            link = 'https://www.alza.cz/EN' + browsing_link_tag['href']

            span_b32_tag = item.find('span', class_='b32')
            now_price = span_b32_tag.string.replace(',', '').replace('-', '').replace('\xa0', '')
            print(rank, name, now_price, link)
            result_list.append(
                {'name': name, 'rank': int(rank), 'price': HtmlParse.convert_price(now_price), 'link': link}
            )
        return result_list

    @staticmethod
    def convert_price(price):
        try:
            return float(price)
        except ValueError:
            return float(''.join(re.findall(r'([0-9])', price)))

    @staticmethod
    def parse_alza_detail(html_txt):
        result = {'today_purchased': 0, 'this_week_purchased': 0, 'now_viewing_customers_count': 0}
        if html_txt:
            soup = HtmlParse.use_lxml(html_txt)
            div_dynamic_promo_tag = soup.find('div', class_='dynamicPromo')
            if div_dynamic_promo_tag:
                msgs_str = div_dynamic_promo_tag['data-msgs']
                if msgs_str:
                    msg_list = msgs_str.split(';')
                    today_purchased = this_week_purchased = now_viewing_customers_count = 0
                    for msg in msg_list:
                        if msg.find('today') != -1:
                            today_purchased = re.findall('Purchased by (.*) customers today', msg)[0]
                        elif msg.find('this week') != -1:
                            this_week_purchased = re.findall('Purchased by (.*) customers this week', msg)[0]
                        elif msg.find('viewing') != -1:
                            now_viewing_customers_count = re.findall('(.*) Customers are viewing this Item', msg)[0]
                    result['today_purchased'] = int(today_purchased)
                    result['this_week_purchased'] = int(this_week_purchased)
                    result['now_viewing_customers_count'] = int(now_viewing_customers_count)
        return result
