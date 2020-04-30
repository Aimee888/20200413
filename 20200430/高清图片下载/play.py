#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : Operate_system_ModeView_structure -> play.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/4/30 14:39
@Desc    :
================================================="""
# 爬虫请求第三方库
import requests
# 数据提取的第三方库
from lxml import etree


def main():
    count = 1
    url = "http://pic.netbian.com/"
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36"
    }

    # s = requests.Session()
    # s.get(url=url, headers=headers)
    # # 随机生成的cookies
    # print(s.cookies.items())
    # print(s.cookies.keys()[0])
    # print(s.cookies.values()[0])

    response = requests.get(url, headers=headers).content.decode("gbk")

    # 数据提取
    html = etree.HTML(response)
    clearfix = html.xpath('//ul[@class="clearfix"]/li/a/@href')
    # http://pic.netbian.com/downpic.php?id=25792&classid=60
    for i in clearfix:
        ID = i[8:-5]
        pic_url = "http://pic.netbian.com/downpic.php?id=" + ID + '&classid=66'
        s = requests.Session()
        s.get(url=pic_url, headers=headers)
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36",
        }
        img_response = requests.get(pic_url, cookies=s.cookies, headers=headers)
        print(img_response.content)
        # f = open('./pictures/{}.jpg'.format(count), 'wb')
        # f.write(img_response.content)
        # f.close()
        count += 1


if __name__ == '__main__':
    main()
