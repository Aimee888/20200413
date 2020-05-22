#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : Operate_system_ModeView_structure -> pcm_wav_transfer.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/5/21 8:55
@Desc    :参考链接：https://blog.csdn.net/zjm750617105/article/details/71698174
================================================="""
import wave
import numpy as np


def pcm2wave(pcm_file, wave_file):
    # 以下设置是针对这个采样率的音频，如果设置音频不同，声音会失真
    framerate = 16000  # 采样率
    channels = 1  # 一个声道
    sampwidth = 2  # 两个字节十六位

    f = open(pcm_file, 'rb')
    str_data = f.read()
    wave_out = wave.open(wave_file, 'wb')
    wave_out.setnchannels(channels)
    wave_out.setsampwidth(sampwidth)
    wave_out.setframerate(framerate)
    wave_out.writeframes(str_data)
    wave_out.close()
    f.close()


def wave2pcm(wav_file, pcm_file):
    f = open(wav_file, 'rb')
    f.seek(0)
    f.read(44)
    data = np.fromfile(f, dtype=np.int16)
    data.tofile(pcm_file)
    f.close()


if __name__ == '__main__':
    pcm2wave("./audio/chinese_test_sphinx.pcm", "./audio/chinese_test_sphinx.wav")
    # wave2pcm("record.wav", "test.pcm")
