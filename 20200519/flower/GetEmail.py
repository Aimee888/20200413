#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : FDS -> GetEmail.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/5/19 19:22
@Desc    :
================================================="""
import poplib
import email
from email.header import decode_header


# 获取邮件标题
def get_email_subject(addr, password):
    # 设置连接网址，获取pop3协议的邮件读取对象
    read = poplib.POP3('pop.163.com', timeout=3600)

    # 输入邮件地址与邮件登录密码
    read.user(addr)
    read.pass_(password)

    # 读取邮件信息（邮件总数，邮件尺寸）
    total_num, total_size = read.stat()

    # 获取最新的一封邮件
    top_email = read.top(total_num, 1)

    # 解码邮件信息，将解码后的邮件信息存入tmp
    tmp = []
    for s in top_email[1]:
        tmp.append(s.decode())

    email_str = '\n'.join(tmp)
    # 将字符串类型解析为Message类型
    message = email.message_from_string(email_str)

    # 获取邮件主题
    subject_str = message['subject']

    subject = decode_header(subject_str)

    content = subject[0][0]
    enc_type = subject[0][1]
    if enc_type:
        subject_decode = content.decode(enc_type)
    else:
        subject_decode = content

    return subject_decode, read, total_num

