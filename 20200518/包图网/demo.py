#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : FDS -> demo.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/5/18 14:44
@Desc    :
================================================="""
import requests
from lxml import etree


class Spider(object):
    def start_request(self):
        for i in range(1, 2):
            response = requests.get("https://ibaotu.com/shipin/")
            html = etree.HTML(response.content.decode("utf-8"))
            self.xpath_data(html)

    def xpath_data(self, html):
        src_list = html.xpath('//div[@class="video-play"]/video/@src')
        tit_list = html.xpath('//span[@class="video-title"]/text()')
        for src, tit in zip(src_list[:2], tit_list[:2]):
            url = "http:" + src
            file_name = tit + ".mp4"
            response = requests.get(url)
            print("正在抓取文件：" + file_name)

            # 保存数据
            with open("video/{}".format(file_name), "wb") as f:
                f.write(response.content)


if __name__ == '__main__':
    er = Spider()
    er.start_request()
