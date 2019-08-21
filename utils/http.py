# !/usr/bin/python3
# -*- coding:utf-8 -*-
'''
Author: jc feng
File Created: 2019-08-21 15:58:22
Last Modified: 2019-08-21 17:08:26
'''

import json
import requests
import traceback

# 临时添加fq
import os
import platform


if platform.system() == "Windows":
    os.environ['http_proxy'] = "http://127.0.0.1:10800"
    os.environ['https_proxy'] = "http://127.0.0.1:10800"


class Http:

    @staticmethod
    def get_for_txt(url):
        try:
            return requests.get(url, timeout=10).text
        except:
            traceback.print_exc()
        return ''

    @staticmethod
    def post_for_json(url, data, headers=None):
        try:
            return requests.post(url, data=json.dumps(data), headers=headers, timeout=10).json()
        except:
            traceback.print_exc()
        return {}
