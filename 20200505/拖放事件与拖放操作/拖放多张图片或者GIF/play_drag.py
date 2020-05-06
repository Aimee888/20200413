#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : Operate_system_ModeView_structure -> play_drag.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/5/5 16:50
@Desc    :
================================================="""
import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap, QMovie
from ui_play_drag import Ui_Form
import sip


class QmyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数
        self.ui = Ui_Form()  # 创建UI对象
        self.ui.setupUi(self)  # 构造UI

        self.setAcceptDrops(True)
        self.ui.plainTextEdit.setAcceptDrops(False)  # 不允许放置

        # 存放label对象
        self.label_set = []

    # # =======================================事件处理函数
    def dragEnterEvent(self, event):
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
        # 移除水平布局中的所有label
        for j in range(len(self.label_set)):
            self.ui.horizontalLayout_2.removeWidget(self.label_set[j])  # 将label移除，但并未彻底删除
            sip.delete(self.label_set[j])  # 彻底删除label
        # 将label集合置零
        self.label_set = []

        # 遍历图片
        for i, url in enumerate(event.mimeData().urls()):
            filename = url.path()  # 完整文件名
            cnt = len(filename)
            realname = filename[1:cnt]  # 去掉最左边的"/"
            basename, ext = os.path.splitext(realname)
            ext = ext.upper()

            # 创建一个Label
            self.addLabel = QLabel(self)
            self.addLabel.setScaledContents(True)  # 自适应图片大小
            self.ui.horizontalLayout_2.addWidget(self.addLabel)
            self.ui.horizontalLayout_2.setStretch(i, 0)
            self.label_set.append(self.addLabel)

            if ext == ".JPG" or ext == ".PNG":  # 显示图片
                pixmap = QPixmap(realname)
                self.addLabel.setPixmap(pixmap)
            elif ext == ".GIF":  # 显示动画
                movie = QMovie(realname)
                self.addLabel.setMovie(movie)
                movie.start()
        event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建app
    form = QmyWidget()
    form.show()
    sys.exit(app.exec_())
