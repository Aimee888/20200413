#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : Operate_system_ModeView_structure -> sphinx_voice_recognition.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/5/21 9:09
@Desc    :参考链接：https://www.jianshu.com/p/08b9c6fc6bcb
================================================="""
import speech_recognition as sr  # 加载包


def wav2txt(wav_file_path, str_language):
    r = sr.Recognizer()
    with sr.AudioFile(wav_file_path) as src:
        audio_res = r.record(src)
    txt = r.recognize_sphinx(audio_res, language=str_language)
    return txt


if __name__ == '__main__':
    # 默认只有英文模型，中文模型要自行安装
    wav2txt('chinese_test_sphinx.wav', "zh-CN")
    # wav2txt('audio-file.flac', "en-US")
    # wav2txt('english_test_sphinx.wav', "en-US")
