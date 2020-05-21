#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : Operate_system_ModeView_structure -> voice_recognition.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/5/20 18:21
@Desc    :参考链接: https://blog.csdn.net/shiyus1314/article/details/97391658
================================================="""
import speech_recognition as sr


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
    pass
    # wave2pcm("record.wav")
    # pcm2wave("record.pcm")
    # voice2Text("record.wav")
    # voice2Text("audio-file.flac")

