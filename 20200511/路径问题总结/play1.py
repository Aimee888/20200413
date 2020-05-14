#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : Operate_system_ModeView_structure -> play1.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/5/11 14:58
@Desc    :
================================================="""
import os
import sys


def print_file_path():
    print(os.path.abspath(__file__))


def print_main_path():
    print(os.path.abspath(sys.argv[0]))
