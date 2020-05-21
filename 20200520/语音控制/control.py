#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : Operate_system_ModeView_structure -> control.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/5/20 16:48
@Desc    :
================================================="""
import os
import subprocess
from pcm_record import record_audio
from sphinx_voice_recognition import wav2txt
from pcm_wav_transfer import pcm2wave


command_set = {
    "打开QQ": "E:\software\qq\qq\Bin\QQ.exe",
    "玫瑰": "./exe/rose.exe",
    "关机": "shutdown -s -t 600",
    "取消关机": "shutdown -a",
}


def main():
    # 录音存为record.pcm
    record_audio("./audio/test.pcm")

    # 将pcm转换为wav格式
    pcm2wave("./audio/test.pcm", "./audio/test.wav")

    # 将wave音频转换为文字
    word = wav2txt("./audio/test.wav", "zh-CN")
    print(word)

    if "退出" in word:
        os.kill(os.getpid(), 9)  # getpid()获取当前程序的pid, 9表示强制退出

    for command in command_set.keys():
        if command in word:
            execute_command = command_set[command]
            # 打开终端窗口
            subprocess.Popen(execute_command, shell=True)
            break


if __name__ == '__main__':
    main()


