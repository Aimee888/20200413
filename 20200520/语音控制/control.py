#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : Operate_system_ModeView_structure -> control.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/5/20 16:48
@Desc    :
================================================="""
from Recorder import record_audio
from voice_recognition import voice2Text


command = {
    "打开QQ": "E:\software\qq\qq\Bin\QQ.exe",
    "玫瑰": "rose.exe",
    "关机": "shutdown -s -t 600",
    "取消关机": "shutdown -a",
}


# record_audio("record.pcm")
voice2Text("record.pcm")


