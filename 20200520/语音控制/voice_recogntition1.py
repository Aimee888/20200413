#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@Project -> File   ：Operate_system_ModeView_structure -> voice_recogntition1
@IDE    ：PyCharm
@Author ：zihan
@Date   ：2020/5/20 22:43
@Desc   ：https://www.jianshu.com/p/08b9c6fc6bcb
=================================================="""
import speech_recognition as sr #加载包

def wav2txt(wavfilepath,str_language):
    r = sr.Recognizer()
    sudio = ""
    with sr.AudioFile(wavfilepath) as src:
        sudio = r.record(src)
    print(r.recognize_sphinx(sudio,language=str_language))

filePath1=r'chinese_test_sphinx.wav'
# filePath2=r'audio-file.flac'
# filePath2=r'english_test_sphinx.wav'
# 默认只有英文模型，中文模型要自行安装
wav2txt(filePath1,"zh-CN")
# wav2txt(filePath2,"en-US")


