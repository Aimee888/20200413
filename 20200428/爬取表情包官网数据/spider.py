#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : Operate_system_ModeView_structure -> spider.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/4/28 14:45
@Desc    :
================================================="""
import requests
import re


def get_gif(url, name):
    response = requests.get(url)
    with open(r'F:\gitplay\Operate_system_ModeView_structure\20200428\爬取表情包官网数据\喜羊羊\%d.gif' % name, "wb") as f:
        f.write(response.content)


def url():
    url = "https://qq.yh31.com/zjbq/2920180.html"
    response = requests.get(url)
    url_add = r'<img border="0" .*? src="(.*?)"'

    url_list = re.findall(url_add, response.text)
    return url_list


if __name__ == '__main__':
    url_list = url()
    for i, url in enumerate(url_list):
        result = "https://qq.yh31.com/" + url
        get_gif(result, i)
        print(result)
