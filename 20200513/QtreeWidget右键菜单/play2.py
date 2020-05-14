#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : FDS -> play2.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/5/13 10:41
@Desc    :
================================================="""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMenu, QMessageBox
from PyQt5.QtCore import Qt
from ui_play2 import Ui_Form


class QmyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数
        self.ui = Ui_Form()  # 创建UI对象
        self.ui.setupUi(self)  # 构造UI

        self.ui.treeWidget.expandAll()
        self.ui.treeWidget.setColumnWidth(0, 200)
        self.ui.treeWidget.setStyleSheet("QHeaderView::section{background:rgb(85, 170, 127);}")

        self.ui.treeWidget.setContextMenuPolicy(Qt.CustomContextMenu)  # 允许右击菜单
        self.ui.treeWidget.customContextMenuRequested.connect(self.do_custom_context_menu_request)  # 右击时触发函数

    def do_custom_context_menu_request(self, pos):
        # row_num = -1  # 当前节点的行号
        parent_num = -1  # 存放当前行的父节点的行号
        for i in self.ui.treeWidget.selectionModel().selection().indexes():
            # row_num = i.row()
            parent_num = i.parent().row()
        # print(parent_num)
        # print(row_num)
        if parent_num == -1:
            pass
        else:
            menu = QMenu()
            item1 = menu.addAction(u"选项一")
            item2 = menu.addAction(u"选项二")
            item3 = menu.addAction(u"选项三")
            action = menu.exec_(self.ui.treeWidget.mapToGlobal(pos))
            if action == item1:
                QMessageBox.information(self, "消息框标题", "你选择了：选项一", QMessageBox.Yes | QMessageBox.No)
                print("you select 1")
            elif action == item2:
                QMessageBox.information(self, "消息框标题", "你选择了：选项二", QMessageBox.Yes | QMessageBox.No)
                print("you select 2")
            elif action == item3:
                QMessageBox.information(self, "消息框标题", "你选择了：选项三", QMessageBox.Yes | QMessageBox.No)
                print("you select 3")
            else:
                return


if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建app
    form = QmyWidget()
    form.show()
    sys.exit(app.exec_())
