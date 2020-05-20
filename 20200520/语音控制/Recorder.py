#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : Operate_system_ModeView_structure -> Recorder.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/5/20 16:53
@Desc    :
================================================="""
import wave
from pyaudio import *


chunk = 1024
framerate = 16000  # 采样率
NUM_SAMPLES = 2000  # 采样点
channels = 1  # 一个声道
sampwidth = 2  # 两个字节十六位
TIME = 2  # 条件变量，可以设置定义录音的时间


def save_wave_file(file_name, data):
    wf = wave.open(file_name, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(sampwidth)
    wf.setframerate(framerate)  # 帧速率
    wf.writeframes(b"".join(data))
    wf.close()


def record_audio(file_name):
    pa = PyAudio()
    stream = pa.open(format=paInt16, channels=1, rate=framerate, input=True, frames_per_buffer=chunk)
    my_buf = []
    count = 0
    print("开始录音")

    while count < TIME * 20:
        string_audio_data = stream.read(chunk)
        my_buf.append(string_audio_data)
        count += 1
    save_wave_file(file_name, my_buf)
    stream.close()
    pa.terminate()  # 关闭设备实例
    return my_buf


def play_audio(file_name):
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


def main():
    record_audio("record.pcm")
    print("录音完毕")
    play_audio("record.pcm")
    print("放音完毕")


if __name__ == '__main__':
    main()
