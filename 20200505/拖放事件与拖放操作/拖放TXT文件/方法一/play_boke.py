#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : Operate_system_ModeView_structure -> play_boke.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/5/6 11:34
@Desc    :
================================================="""

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from ui_boke import Ui_Form


class QmyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数
        self.ui = Ui_Form()  # 创建UI对象
        self.ui.setupUi(self)  # 构造UI

        self.setAcceptDrops(True)
        self.ui.LabPic.setAcceptDrops(True)
        self.ui.LabPic.setScaledContents(True)  # 图片适应Label大小

    # # =======================================事件处理函数
    def dragEnterEvent(self, event):
        if event.mimeData().hasText():
            event.acceptProposedAction()  # 接收拖放操作

    def dropEvent(self, event):
        txt_path = event.mimeData().text().replace('file:///', '')
        with open(txt_path, 'r') as f:
            self.ui.LabPic.setText(f.read())


if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建app
    form = QmyWidget()
    form.show()
    sys.exit(app.exec_())
