#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : Operate_system_ModeView_structure -> myMainWindow_filesystem_model.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/4/24 10:31
@Desc    :QFileSystemModel类的基本功能
            isDir(QModelIndex)：判断节点是不是一个目录
            filePath(QModelIndex)：返回节点的目录名或带路径的文件名
            fileName(QModelIndex)：返回去除路径的文件夹名或文件名
            type(QModelIndex)：返回描述节点类型的文字
            size(QModelIndex)：如果节点是文件，返回文件大小的字节数，如果节点是文件夹，返回0
================================================="""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileSystemModel
from PyQt5.QtCore import QDir
from ui_filesystem_model import Ui_MainWindow


class QmyMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数
        self.ui = Ui_MainWindow()  # 创建UI对象
        self.ui.setupUi(self)  # 构造UI

        # 自定义函数
        self.__buildModelView()

        # =======自动关联的槽函数
        self.ui.treeView.clicked.connect(self.do_tree_view_clicked)

    def __buildModelView(self):  # 构造Model/View系统
        self.model = QFileSystemModel(self)
        self.model.setRootPath(QDir.currentPath())
        self.ui.treeView.setModel(self.model)  # 设置数据模型
        self.ui.listView.setModel(self.model)
        self.ui.tableView.setModel(self.model)

        self.ui.treeView.clicked.connect(self.ui.listView.setRootIndex)
        self.ui.treeView.clicked.connect(self.ui.tableView.setRootIndex)

    def do_tree_view_clicked(self, index):
        self.ui.chkBox_IsDir.setChecked(self.model.isDir(index))
        self.ui.LabPath.setText(self.model.filePath(index))  # 目录名
        self.ui.LabType.setText(self.model.type(index))  # 节点类型
        self.ui.LabFileName.setText(self.model.fileName(index))  # 文件名

        filesize = self.model.size(index) / 1024
        if filesize < 1024:
            self.ui.LabFileSize.setText("%d KB" % filesize)
        else:
            self.ui.LabFileSize.setText("%.2f MB" % (filesize/1024.0))


if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建app
    form = QmyMainWindow()
    form.show()
    sys.exit(app.exec_())
