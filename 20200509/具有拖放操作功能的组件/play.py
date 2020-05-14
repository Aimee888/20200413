#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : Operate_system_ModeView_structure -> play.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/5/9 15:28
@Desc    :
================================================="""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFileSystemModel
from PyQt5.QtCore import QDir
from ui_control import Ui_Form


class QmyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数
        self.ui = Ui_Form()  # 创建UI对象
        self.ui.setupUi(self)  # 构造UI

        # # ===================自定义功能函数

        # # ===================事件处理函数

        # # ===================由connectSlotsByName()自动关联的槽函数

        # # ===================自定义槽函数


if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建app
    form = QmyWidget()
    form.show()
    sys.exit(app.exec_())
