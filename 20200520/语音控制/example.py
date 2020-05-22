#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : Operate_system_ModeView_structure -> example.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/5/21 18:48
@Desc    :
================================================="""
import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# recognize speech using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    print("Google Speech Recognition thinks you said in English: -  " + r.recognize_google(audio, language="en-US"))
    print("Google Speech Recognition thinks you said in Turkish: -  " + r.recognize_google(audio, language="tr-TR"))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
