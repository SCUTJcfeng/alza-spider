# !/usr/bin/python3
# -*- coding:utf-8 -*-
'''
Author: jc feng
File Created: 2019-08-23 09:21:54
Last Modified: 2019-09-25 20:49:21
'''

import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from secret import USER_EMAIL, USER_PASSWORD


class Email:

    @staticmethod
    def send_email(to_email, msg):
        with smtplib.SMTP_SSL('smtp.qq.com', 465, timeout=10) as conn:
            conn.login(USER_EMAIL, USER_PASSWORD)
            conn.sendmail(USER_EMAIL, to_email, msg)
            print('Email 发送成功')

    @staticmethod
    def build_msg(to_email, subject, body, files):
        msg = MIMEMultipart()
        msg['From'] = USER_EMAIL
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body))
        for file_path in files:
            msg.attach(Email.load_file(file_path))
        return msg.as_string()

    @staticmethod
    def load_file(file_path):
        with open(file_path, 'rb') as f:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(f.read())
        encoders.encode_base64(part)
        file_name = os.path.split(file_path)[-1]
        part.add_header('Content-Disposition',
                        f'attachment; filename= {file_name}')
        return part
