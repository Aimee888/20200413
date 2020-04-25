#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : Operate_system_ModeView_structure -> get_book_exe.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/4/25 10:28
@Desc    :爬取笔趣阁小说: https://www.52bqg.com/
            将url放入一个队列中Queue
            访问第一章的url得到第二章的url，放入队列，依次类推
================================================="""


import requests
from bs4 import BeautifulSoup
import sys
import time
import queue


# 获取内容
def get_content(url):
    try:
        # 进入主页
        # https://www.52bqg.com/
        # 随便搜索一步小说，找出变化规律
        # https://www.52bqg.com/book_110102/
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36"
        }
        res = requests.get(url=url, headers=headers)  # 获取小说目录界面
        res.encoding = "gbk"
        content = res.text
        return content
    except:
        s = sys.exc_info()
        print("Error '%s' happened on line %d" % (s[1], s[2].tb_lineno))
        return "ERROR"


# 解析内容
def parseContent(q, first_url, content):
    base_url_list = first_url.split("/")
    html_order = base_url_list[-1]
    last_number = first_url.find(html_order)
    base_url = first_url[:last_number]
    soup = BeautifulSoup(content, "html.parser")
    chapter = soup.find(name='div', class_="bookname").h1.text
    content = soup.find(name="div", id="content").text
    save(base_url, chapter, content)
    # 如果存在下一个章节的链接，则将链接加入队列
    next1 = soup.find(name='div', class_="bottem").find_all('a')[3].get('href')
    if next1 != base_url:
        q.put(next1)
    # print(next1)
    return q


def save(base_url, chapter, content):
    book_name = get_book_name(base_url)
    filename = book_name + ".txt"
    f = open(filename, "a+", encoding="utf-8")
    f.write("".join(chapter) + "\n")
    f.write("".join(content.split()[2:]) + "\n")
    f.close()


# 获取书名
def get_book_name(base_url):
    content = get_content(base_url)
    soup = BeautifulSoup(content, "html.parser")
    name = soup.find(name='div', class_="box_con").h1.text
    return name


def main():
    first_url = input("请输入小说第一章的链接：")
    start_time = time.time()

    # 进入主页
    # https://www.52bqg.com/
    # 随便搜索一步小说，找出变化规律
    # https://www.52bqg.com/book_110102/
    q = queue.Queue()
    # 小说第一章链接
    # first_url = "https://www.52bqg.com/book_110102/35620490.html"
    q.put(first_url)
    while not q.empty():
        content = get_content(q.get())
        q = parseContent(q, first_url, content)
    end_time = time.time()
    project_time = end_time - start_time
    print("下载用时：", project_time)


if __name__ == '__main__':
    main()
