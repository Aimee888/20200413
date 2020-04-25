#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : Operate_system_ModeView_structure -> get_hongxiutianxiang_book.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/4/25 16:15
@Desc    :爬取不到vip章节。。。
            疑惑，bs4只能爬到可以在网页上看到的东西?
================================================="""
import requests
from bs4 import BeautifulSoup


def main():
    url = "https://www.hongxiu.com/book/12256355204263303#Catalog"
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36"
    }
    html = requests.get(url, headers=headers)
    content = html.text

    # 获取小说名字
    soup = BeautifulSoup(content, "html.parser")
    book_name = soup.find(name='div', class_="book-info").h1.em.text

    # 找到小说第一章的链接
    first_url = soup.find(name='div', class_="volume").find('a').get('href')
    print(first_url)


if __name__ == '__main__':
    main()
