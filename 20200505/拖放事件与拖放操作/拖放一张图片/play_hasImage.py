#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : Operate_system_ModeView_structure -> play_hasImage.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/5/6 14:15
@Desc    :拖动图片到窗口并且显示图片
            使用QImageReader解决了文件格式不对的读取温蒂
            使用QImage解决了图片文件过大的问题。
================================================="""
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage, QImageReader
from ui_hasImage import Ui_Form


class QmyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数
        self.ui = Ui_Form()  # 创建UI对象
        self.ui.setupUi(self)  # 构造UI

        self.setAcceptDrops(True)
        self.ui.LabPic.setAcceptDrops(False)
        self.ui.LabPic.setScaledContents(True)  # 图片适应Label大小

    # # =======================================事件处理函数
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            print("aaa")
            event.acceptProposedAction()  # 接收拖放操作

    def dropEvent(self, event):
        # # 方法一：针对小图片
        # pixmap = QPixmap(event.mimeData().urls()[0].toLocalFile())
        # self.ui.LabPic.setPixmap(pixmap)
        #
        # # 方法二：小图片和PNG格式的大图片
        # img = QImage()
        # print(event.mimeData().urls()[0].toLocalFile())
        # img.load(event.mimeData().urls()[0].toLocalFile())
        # pixmap = QPixmap.fromImage(img.scaled(self.ui.LabPic.size(), Qt.KeepAspectRatio))
        # self.ui.LabPic.setPixmap(pixmap)

        # 方法三：小图片和大图片
        reader = QImageReader()
        print(event.mimeData().urls()[0].toLocalFile())
        reader.setFileName(event.mimeData().urls()[0].toLocalFile())
        reader.setDecideFormatFromContent(True)
        if reader.canRead():
            img = QImage(reader.read())
            pixmap = QPixmap.fromImage(img.scaled(self.ui.LabPic.size(), Qt.KeepAspectRatio))
            self.ui.LabPic.setPixmap(pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建app
    form = QmyWidget()
    form.show()
    sys.exit(app.exec_())
