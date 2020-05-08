#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : Operate_system_ModeView_structure -> play.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/5/7 14:50
@Desc    :图灵机器人  -- 没绑定微信版
================================================="""
import requests


def get_response(msg):
    url = "http://openapi.tuling123.com/openapi/api/v2"
    data = {
        "reqType": 0,
        "perception": {
            "inputText": {
                "text": msg
            },
        },
        "userInfo": {
            "apiKey": "9808fe257507490081f66c6f9ff9db98",
            "userId": "zihan"
        }
    }
    # "apiKey": "9808fe257507490081f66c6f9ff9db98"
    # "userId": "6808bd9178a339c7"
    # "apiKey": "2fbec5c65c634301ab5e3555f6fa36d0"
    # "userId": "7304404f10cd09b3"
    result = requests.post(url, json=data).json()

    return result['results'][0]['values']['text']


def main():
    # 用户输入
    while True:
        # 输入自己说的话
        msg = input('我：')

        # 获取机器人回复的消息
        msg_response = get_response(msg)

        # 输出机器人回的话
        print("机器人：" + msg_response)


if __name__ == '__main__':
    main()
