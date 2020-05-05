#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : Operate_system_ModeView_structure -> myMainWindow_event.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/4/30 14:29
@Desc    :
================================================="""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QLabel
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPainter, QPixmap
from 事件拦截.ui_event import Ui_MainWindow


class QmyLabel(QLabel):
    doubleClicked = pyqtSignal()  # 自定义信号

    def mouseDoubleClickEvent(self, event):  # 双击事件的处理
        self.doubleClicked.emit()


class QmyMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数
        self.ui = Ui_MainWindow()  # 创建UI对象
        self.ui.setupUi(self)  # 构造UI

        # # ===================自定义功能函数

        # # ===================事件处理函数
        LabHello = QmyLabel(self)
        LabHello.setText("双击我啊")
        font = LabHello.font()
        font.setPointSize(14)
        font.setBold(True)
        LabHello.setFont(font)
        size = LabHello.sizeHint()
        LabHello.setGeometry(70, 60, size.width(), size.height())
        LabHello.doubleClicked.connect(self.do_doubleClicked)

    def do_doubleClicked(self):
        print("标签被双击了")

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
    form = QmyMainWindow()
    form.show()
    sys.exit(app.exec_())
