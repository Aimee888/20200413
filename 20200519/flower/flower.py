#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : FDS -> flower.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/5/19 19:15
@Desc    :关机指令：shutdown -s -t 600
            取消关机: shutdown -a
================================================="""
from GetEmail import get_email_subject
import subprocess
from playsound import playsound

command_set = {
    "重启": "shutdown -r -t 600",
    "关机": "shutdown -s -t 600",
    "love": "love",
    "rose": "rose",
}


if __name__ == '__main__':
    # 开启授权码
    subject_decode, read, total_num = get_email_subject("163邮箱用户名", "授权码，需开启POP3")
    print(subject_decode, read, total_num)

    if subject_decode in command_set:
        command = command_set[subject_decode]
        print("计算机执行的指令", command)

        # 删除邮件
        read.dele()
        read.quit()

        # 执行指令
        subprocess.Popen(command, shell=True)

        if subject_decode == "rose":
            # 播放音乐
            playsound("marry.mp3")
