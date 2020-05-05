#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : Operate_system_ModeView_structure -> myWidget_event.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/5/5 9:35
@Desc    :
================================================="""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPixmap
from ui_event import Ui_Form


class QmyMidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数
        self.ui = Ui_Form()  # 创建UI对象
        self.ui.setupUi(self)  # 构造UI

        # # ===================自定义功能函数

        # # ===================事件处理函数

        # # ===================由connectSlotsByName()自动关联的槽函数

        # # ===================自定义槽函数

    def paintEvent(self, event):  # 绘制窗体背景图片
        painter = QPainter(self)
        pic = QPixmap("background.jpg")
        painter.drawPixmap(0, 0, self.width(), self.height(), pic)
        super().paintEvent(event)

    def resizeEvent(self, event):  # 改变窗体大小
        W = self.width()
        H = self.height()
        Wbtn = self.ui.btnTest.width()
        Hbtn = self.ui.btnTest.height()
        self.ui.btnTest.setGeometry((W - Wbtn) / 2, (H - Hbtn) / 2, Wbtn, Hbtn)

    def closeEvent(self, event):  # 窗体关闭时询问
        dlgTitle = "Question 消息框"
        strInfo = "closeEvent 事件触发，确定要退出吗？"
        defaultBtn = QMessageBox.NoButton  # 默认按钮
        result = QMessageBox.question(self, dlgTitle, strInfo, QMessageBox.Yes | QMessageBox.No, defaultBtn)
        if result == QMessageBox.Yes:
            event.accept()  # 窗体可关闭
        else:
            event.ignore()  # 窗体不能被关闭

    def mousePressEvent(self, event):
        pt = event.pos()  # 鼠标位置, QPoint
        if event.button() == Qt.LeftButton:  # 鼠标左键按下
            self.ui.LabMove.setText("(x, y) = (%d, %d)" % (pt.x(), pt.y()))
            rect = self.ui.LabMove.geometry()
            self.ui.LabMove.setGeometry(pt.x(), pt.y(), rect.width(), rect.height())
        super().mousePressEvent(event)

    """
    keyPressEvent事件触发时，上下左右键时不能移动按钮的，只有ADWS有效
    keyReleaseEvent事件触发，ADWS有效，上下左右也有效
    """
    # def keyPressEvent(self, event):
    def keyReleaseEvent(self, event):
        rect = self.ui.btnMove.geometry()
        if event.key() in set([Qt.Key_A, Qt.Key_Left]):
            self.ui.btnMove.setGeometry(rect.left() - 20, rect.top(), rect.width(), rect.height())
        elif event.key() in set([Qt.Key_D, Qt.Key_Right]):
            self.ui.btnMove.setGeometry(rect.left() + 20, rect.top(), rect.width(), rect.height())
        elif event.key() in set([Qt.Key_W, Qt.Key_Up]):
            self.ui.btnMove.setGeometry(rect.left(), rect.top() - 20, rect.width(), rect.height())
        elif event.key() in set([Qt.Key_S, Qt.Key_Down]):
            self.ui.btnMove.setGeometry(rect.left(), rect.top() + 20, rect.width(), rect.height())


if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建app
    form = QmyMidget()
    form.show()
    sys.exit(app.exec_())
