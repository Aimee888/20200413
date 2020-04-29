#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : Operate_system_ModeView_structure -> rewite_close.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/4/29 16:30
@Desc    :
================================================="""
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui_close import Ui_MainWindow


class QmyMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数
        self.ui = Ui_MainWindow()  # 创建UI对象
        self.ui.setupUi(self)  # 构造UI

        # # ===================由connectSlotsByName()自动关联的槽函数
        self.ui.Btn_Close.clicked.connect(self.do_btn_close)

    def closeEvent(self, event):
        defaultBtn = QMessageBox.NoButton
        result = QMessageBox.question(self, "Question", "Are you sure exist ？", QMessageBox.Yes | QMessageBox.No, defaultBtn)
        if result == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def do_btn_close(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建app
    form = QmyMainWindow()
    form.show()
    sys.exit(app.exec_())
