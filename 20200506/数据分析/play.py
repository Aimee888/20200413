#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : Operate_system_ModeView_structure -> play.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/5/6 14:59
@Desc    :
================================================="""
import requests
from lxml import etree
from pyecharts.charts import Bar
import pyecharts.options as opts


def fang_spider():
    url = "https://cs.newhouse.fang.com/house/s/b91/"
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36"
    }
    resp = requests.get(url, headers=headers)  # 发送请求
    resp_txt = resp.content.decode(encoding='gbk')
    resp_html = etree.HTML(resp_txt)

    resp_list = resp_html.xpath('//div[@class="nl_con clearfix"]/ul/li')

    names = []
    prices = []
    for i in resp_list:
        name = i.xpath('.//div[@class="nlcd_name"]/a/text()')
        price = i.xpath('.//div[@class="nhouse_price"]/span/text()')

        if name != [] and price != []:
            if price != ['价格待定']:
                name = name[0].strip()
                names.append(name)
                price = price[0]
                prices.append(price)
    return names, prices


def main():
    print("main() func is starting...")
    names, prices = fang_spider()
    # print(names)
    # print(prices)
    bar = Bar()
    bar.add_xaxis(names)
    bar.add_yaxis('长沙房价图', prices)
    bar.set_global_opts(
            xaxis_opts=opts.AxisOpts(
                axislabel_opts=opts.LabelOpts(rotate=40),
            ),
        yaxis_opts=opts.AxisOpts(name="价格（元、平方米）"),
        title_opts=opts.TitleOpts(title="柱状图")
    )
    bar.render('房价图.html')


if __name__ == '__main__':
    main()
