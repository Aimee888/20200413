#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : Operate_system_ModeView_structure -> myWidget_Drag.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/5/5 11:15
@Desc    :
================================================="""
import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPixmap, QMovie
from ui_drag import Ui_Form


class QmyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数
        self.ui = Ui_Form()  # 创建UI对象
        self.ui.setupUi(self)  # 构造UI

        self.setAcceptDrops(True)
        self.ui.plainTextEdit.setAcceptDrops(False)  # 不允许放置
        self.ui.LabPic.setAcceptDrops(False)  # 由父窗体处理
        self.ui.LabPic.setScaledContents(True)  # 图片适应Label大小

    # # =======================================事件处理函数
    def dragEnterEvent(self, event):
        self.ui.plainTextEdit.clear()
        self.ui.plainTextEdit.appendPlainText("dragEnterEvent 事件 mimeData().formats()")
        for strLine in event.mimeData().formats():  # 格式数据
            self.ui.plainTextEdit.appendPlainText(strLine)

        self.ui.plainTextEdit.appendPlainText("\ndragEnterEvent 事件 mimeData.urls()")
        for url in event.mimeData().urls():
            self.ui.plainTextEdit.appendPlainText(url.path())

        if event.mimeData().hasUrls():
            filename = event.mimeData().urls()[0].fileName()  # 只有文件名
            basename, ext = os.path.splitext(filename)  # 文件名和后缀
            ext = ext.upper()
            if ext == ".JPG" or ext == ".PNG" or ext == ".GIF":  # 只接受JPEG文件
                event.acceptProposedAction()  # 接收拖放操作
            else:
                event.ignore()

    def dropEvent(self, event):
        # 方法一
        filename = event.mimeData().urls()[0].path()  # 完整文件名
        print(filename)
        cnt = len(filename)
        realname = filename[1:cnt]  # 去掉最左边的"/"
        basename, ext = os.path.splitext(realname)
        ext = ext.upper()

        # # 方法二
        # realname = event.mimeData().urls()[0].toLocalFile()
        # basename, ext = os.path.splitext(realname)
        # ext = ext.upper()

        if ext == ".JPG" or ext == ".PNG":
            pixmap = QPixmap(realname)
            self.ui.LabPic.setPixmap(pixmap)
        elif ext == ".GIF":
            movie = QMovie(realname)
            self.ui.LabPic.setMovie(movie)
            movie.start()
        event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建app
    form = QmyWidget()
    form.show()
    sys.exit(app.exec_())
