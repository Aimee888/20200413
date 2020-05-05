#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : Operate_system_ModeView_structure -> myWidget_event.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/5/5 10:14
@Desc    :
================================================="""

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QEvent, Qt
from ui_event import Ui_Form


class QmyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数
        self.ui = Ui_Form()  # 创建UI对象
        self.ui.setupUi(self)  # 构造UI

        self.ui.LabHover.installEventFilter(self)  # 将窗体注册为其事件监测者
        self.ui.LabDBClick.installEventFilter(self)

        # # ===================自定义功能函数

        # # ===================事件处理函数

        # # ===================由connectSlotsByName()自动关联的槽函数

        # # ===================自定义槽函数

    def eventFilter(self, watched, event):
        if watched == self.ui.LabHover:
            if event.type() == QEvent.Enter:  # 鼠标光标移入
                self.ui.LabHover.setStyleSheet("background-color: rgb(170,255,255);")
            elif event.type() == QEvent.Leave:  # 鼠标光标移出
                self.ui.LabHover.setStyleSheet("")
                self.ui.LabHover.setText("靠近我，点击我")
            elif event.type() == QEvent.MouseButtonPress:  # 鼠标按键按下
                self.ui.LabHover.setText("button pressed")
            elif event.type() == QEvent.MouseButtonRelease:  # 鼠标按键释放
                self.ui.LabHover.setText("button released")
        if watched == self.ui.LabDBClick:
            if event.type() == QEvent.Enter:  # 鼠标光标移入
                self.ui.LabDBClick.setStyleSheet("background-color: rgb(85,255,127);")
            elif event.type() == QEvent.Leave:  # 鼠标光标移出
                self.ui.LabDBClick.setStyleSheet("")
                self.ui.LabDBClick.setText("可双击的标签")
            elif event.type() == QEvent.MouseButtonDblClick:  # 鼠标按键按下
                self.ui.LabDBClick.setText("double clicked")
        return super().eventFilter(watched, event)


if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建app
    form = QmyWidget()
    form.show()
    sys.exit(app.exec_())
