#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : Operate_system_ModeView_structure -> play.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/5/12 14:46
@Desc    :1. 动态加载的数据都在XHR里面
            2. Referer是代表你是从哪个网站来的，表示来源
================================================="""
import requests
import re
import os


# 获取图片链接
def get_url_pics(queryWord):
    # Request URL：百度图片网页 -- 》检查--》Network --》图片下滑 --》看检查里面的变化，在左侧会新增
    url_str = "https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord={}&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=&hd=&latest=&copyright=&word={}&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&pn=30&rn=30&gsm=96&1589266814046="
    url = url_str.format(queryWord, queryWord)
    res = requests.get(url)
    url_pics = re.findall('"thumbURL":"(https://.*?)"', res.text)
    return url_pics


# 保存图片
def save_pics(url_pics, queryWord):
    headers = {
        'Referer': "https://image.baidu.com/search/index",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36"
    }

    for url_pic in url_pics:
        con = requests.get(url_pic, headers=headers)
        path = url_pic.split("/")[-1]
        print("正在下载", path)

        with open("pic/{}/{}".format(queryWord, path), "wb") as f:
            f.write(con.content)


def main():
    queryWord = input("请输入查询关键字：")
    folder_path = "./pic/{}".format(queryWord)
    # 根据搜索的字段创建相应的文件夹
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

    # 获取图片的链接
    url_pics = get_url_pics(queryWord)
    # 保存图片
    save_pics(url_pics, queryWord)


if __name__ == '__main__':
    main()

