#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : Operate_system_ModeView_structure -> baidu_voice_recognition.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/5/21 9:31
@Desc    :参考链接：https://blog.csdn.net/Lynn_coder/article/details/79436768
================================================="""
from aip import AipSpeech


""" 你的 APPID AK SK """
APP_ID = '你的 App ID'
API_KEY = '你的 Api Key'
SECRET_KEY = '你的 Secret Key'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


# 识别本地文件
result_json = client.asr(get_file_content('audio.pcm'), 'pcm', 16000, {
    'lan': 'zh',
})
