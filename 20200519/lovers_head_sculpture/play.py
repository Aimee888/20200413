#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : Operate_system_ModeView_structure -> play.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/5/19 20:27
@Desc    :
================================================="""
import requests
import re
import os


headers = {
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36",
    }


def get_matched_data(url, matched_string):
    html = requests.get(url, headers=headers).content.decode("utf-8")
    result = re.findall(matched_string, html)
    return result


def save_data(img, title):
    img_url = "http:" + img
    img_data = requests.get(img_url, headers=headers).content

    img_path = "./picture/" + title + "/" + str(img.split("/")[-1])
    print("正在下载：", str(img))
    with open(img_path, "wb") as f:
        f.write(img_data)
    print(str(img.split("/")[-1]) + "下载完毕")


def main():
    url_enter = "https://www.woyaogexing.com/touxiang/qinglv/"
    match_url_title = '<a href="(.*?)" class="img" target="_blank" title="(.*?)">'
    url_title_tuple_list = get_matched_data(url_enter, match_url_title)

    for url_title_tuple in url_title_tuple_list:
        url_pic = "https://www.woyaogexing.com" + url_title_tuple[0]
        title_pic = url_title_tuple[1]
        title = re.sub("[/]+", "_", title_pic)
        if not os.path.exists("./picture/" + title):
            os.mkdir("./picture/" + title)
        match_img_src = '<img class="lazy" src="(.*?)" width="200" height="200" />'
        img_list = get_matched_data(url_pic, match_img_src)
        # http://img2.woyaogexing.com/2020/05/19/809860d777c44c57bafb96f86caef654!400x400.jpeg
        for img in img_list:
            save_data(img, title)


if __name__ == '__main__':
    main()

