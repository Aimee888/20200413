#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : Operate_system_ModeView_structure -> play.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/5/4 11:16
@Desc    :
================================================="""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QPainter, QPixmap
from ui_play import Ui_Form


class QmyLabel(QLabel):
    double_clicked = pyqtSignal()  # 自定义信号

    def mouseDoubleClickEvent(self, event):  # 双击事件的处理
        self.double_clicked.emit()


class QmyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数
        self.ui = Ui_Form()  # 创建UI对象
        self.ui.setupUi(self)  # 构造UI

        # # ===================事件处理函数
        self.origin = True  # 是否是原始标签
        self.mylabel = QmyLabel(self)
        self.mylabel.setText("双击测试标签")
        font = self.mylabel.font()
        font.setPointSize(18)
        font.setBold(True)
        self.mylabel.setFont(font)
        label_size = self.mylabel.sizeHint()
        width_widget = self.width()
        height_widget = self.height()
        self.mylabel.setGeometry(int((width_widget - label_size.width()) / 2),
                                 int((height_widget - label_size.height()) / 2),
                                 label_size.width(), label_size.height())
        self.mylabel.double_clicked.connect(self.do_mylabel_double_clicked)

    def do_mylabel_double_clicked(self):
        if self.origin:
            self.mylabel.setText("已经被双击了")
            self.origin = False
        else:
            self.mylabel.setText("双击测试标签")
            self.origin = True

    def paintEvent(self, event):  # 绘制窗体背景图片
        painter = QPainter(self)
        pic = QPixmap("background.jpg")
        painter.drawPixmap(0, 0, self.width(), self.height(), pic)
        super().paintEvent(event)


if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建app
    form = QmyWidget()
    form.show()
    sys.exit(app.exec_())

