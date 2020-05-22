#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : Operate_system_ModeView_structure -> pcm_record.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/5/20 16:53
@Desc    :
================================================="""
import wave
from pyaudio import *


def save_wave_file(file_name, data):
    framerate = 16000  # 采样率
    channels = 1  # 一个声道
    sampwidth = 2  # 两个字节十六位

    wf = wave.open(file_name, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(sampwidth)
    wf.setframerate(framerate)  # 帧速率
    wf.writeframes(b"".join(data))
    wf.close()


# 录音
def record_audio(file_name):
    framerate = 16000  # 采样率
    chunk = 1024
    TIME = 2  # 条件变量，可以设置定义录音的时间

    pa = PyAudio()
    stream = pa.open(format=paInt16, channels=1, rate=framerate, input=True, frames_per_buffer=chunk)
    my_buf = []
    count = 0
    print("开始录音")

    while count < TIME * 13:
        string_audio_data = stream.read(chunk)
        my_buf.append(string_audio_data)
        count += 1
    save_wave_file(file_name, my_buf)
    stream.close()
    pa.terminate()  # 关闭设备实例
    print("录音完毕")
    return my_buf


# 放音
def play_audio(file_name):
    chunk = 1024
    framerate = 16000

    wf = wave.open(file_name, 'rb')
    p = PyAudio()
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()), channels=wf.getnchannels(), rate=framerate, output=True)
    print("开始放音")
    while True:
        data = wf.readframes(chunk)
        if data == b'':
            break
        stream.write(data)
    wf.close()
    stream.close()
    p.terminate()  # 关闭设备实例
    print("放音完毕")


def main():
    record_audio("./audio/chinese_test_sphinx.pcm")
    play_audio("./audio/chinese_test_sphinx.pcm")


if __name__ == '__main__':
    main()
