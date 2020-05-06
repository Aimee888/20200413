#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : Operate_system_ModeView_structure -> 基础知识.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/5/6 15:52
@Desc    :
================================================="""
from pyecharts.charts import Bar

bar = Bar()
bar.add_xaxis(names)
bar.add_yaxis('长沙房价图', prices)
bar.render('房价图.html')


