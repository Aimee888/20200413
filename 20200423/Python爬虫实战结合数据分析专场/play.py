#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : Operate_system_ModeView_structure -> play.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/4/23 20:16
@Desc    :爬虫 - 数据分析
================================================="""

import requests
import json
import pandas as pd


# https://movie.douban.com/j/search_subjects?type=movie&tag=%E8%B1%86%E7%93%A3%E9%AB%98%E5%88%86&sort=rank&page_limit={}&page_start=0
def doubanmovie():
    limit = 10
    url = "https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&page_limit={}&page_start=0".format(limit)
    # 浏览器类型
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36"
    }
    result = requests.get(url.format(limit), headers=headers)
    json_result = result.text
    json_result = json.loads(json_result)
    col = ['title', 'rate', 'url']
    num = len(json_result['subjects'])

    # 确定一个数据类型，NaN代表非数值的特殊型
    data = pd.DataFrame(index=range(num), columns=col)
    for i in range(num):
        data.loc[i, 'title'] = json_result['subjects'][i]['title']
        data.loc[i, 'rate'] = json_result['subjects'][i]['rate']
        data.loc[i, 'url'] = json_result['subjects'][i]['url']
    filename = "电影排行.xlsx"
    data.to_excel(filename)


if __name__ == '__main__':
    doubanmovie()
