#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : Operate_system_ModeView_structure -> voice_recognition.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/5/20 18:21
@Desc    :https://blog.csdn.net/zjm750617105/article/details/71698174
================================================="""
import os
import speech_recognition as sr

chunk = 1024
framerate = 16000  # 采样率
NUM_SAMPLES = 2000  # 采样点
channels = 1  # 一个声道
sampwidth = 2  # 两个字节十六位
TIME = 2  # 条件变量，可以设置定义录音的时间


def pcm2wave(pcm_file):
    import wave
    import os

    f = open(pcm_file, 'rb')
    str_data = f.read()
    wave_out = wave.open("chinese_test_sphinx.wav", 'wb')
    wave_out.setnchannels(channels)
    wave_out.setsampwidth(sampwidth)
    wave_out.setframerate(framerate)
    wave_out.writeframes(str_data)
    wave_out.close()
    f.close()


def wave2pcm(wav_file):
    import os
    import numpy as np
    f = open(wav_file, 'rb')
    f.seek(0)
    f.read(44)
    data = np.fromfile(f, dtype=np.int16)
    data.tofile("test.pcm")
    f.close()


# 语音转文字
def voice2Text(file_name):
    # voice_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), file_name)
    voice_file = file_name
    # use the audio file as the audio source
    r = sr.Recognizer()
    content = ""
    with sr.AudioFile(voice_file) as source:
        audio = r.record(source)
    try:
        content = r.recognize_google(audio, language='en-US')
        print(content)
        # print("Google Speech Recognition:" + content)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Google Speech Recognition error; {0}".format(e))

    return content or '无法翻译'


if __name__ == '__main__':
    # wave2pcm("record.wav")
    pcm2wave("chinese_test_sphinx.pcm")
    # voice2Text("record.wav")
    # voice2Text("audio-file.flac")

