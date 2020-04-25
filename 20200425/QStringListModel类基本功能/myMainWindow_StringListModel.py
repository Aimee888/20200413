#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : Operate_system_ModeView_structure -> myMainWindow_StringListModel.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/4/25 8:53
@Desc    :
================================================="""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QAbstractItemView
from PyQt5.QtCore import QDir, QStringListModel, Qt
from ui_QStringListModel import Ui_Form


class QmyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数
        self.ui = Ui_Form()  # 创建UI对象
        self.ui.setupUi(self)  # 构造UI

        self.__provinces = ["北京", "上海", "天津", "河北", "山东", "四川", "重庆", "广东", "河南"]
        self.model = QStringListModel(self)
        self.model.setStringList(self.__provinces)
        self.ui.listView.setModel(self.model)
        self.ui.listView.setEditTriggers(QAbstractItemView.DoubleClicked | QAbstractItemView.SelectedClicked)

        # # ===================自定义功能函数

        # # ===================事件处理函数

        # # ===================由connectSlotsByName()自动关联的槽函数
        # 添加项
        self.ui.btnList_Append.clicked.connect(self.do_btnlist_append_clicked)
        # 插入项
        self.ui.btnList_Insert.clicked.connect(self.do_btnlist_insert_clicked)
        # 删除当前项
        self.ui.btnList_Delete.clicked.connect(self.do_btnlist_delete_clicked)
        # 清除列表
        self.ui.btnList_Clear.clicked.connect(self.do_btnlist_clear_clicked)
        # 显示数据模型的内容
        self.ui.btnText_Display.clicked.connect(self.do_btntext_display_clicked)
        # 点击listview时show行列信息
        self.ui.listView.clicked.connect(self.do_listview_clicked)

        # # ===================自定义槽函数

    # 添加项
    def do_btnlist_append_clicked(self):
        lastRow = self.model.rowCount()
        self.model.insertRow(lastRow)  # 在尾部插入一空行
        index = self.model.index(lastRow, 0)  # 获取最后一行的模型索引
        self.model.setData(index, "new item", Qt.DisplayRole)  # 设置显示文字
        self.ui.listView.setCurrentIndex(index)  # 设置当前选中的行

    # 插入项
    def do_btnlist_insert_clicked(self):
        index = self.ui.listView.currentIndex()  # 当前模型索引
        self.model.insertRow(index.row())
        self.model.setData(index, "inserted item", Qt.DisplayRole)
        self.ui.listView.setCurrentIndex(index)  # 设置当前选中的行

    # 删除当前项
    def do_btnlist_delete_clicked(self):
        index = self.ui.listView.currentIndex()
        self.model.removeRow(index.row())  # 删除当前行

    # 清除列表
    def do_btnlist_clear_clicked(self):
        count = self.model.rowCount()
        self.model.removeRows(0, count)

    # 显示数据模型的内容
    def do_btntext_display_clicked(self):
        strList = self.model.stringList()  # 列表类型
        self.ui.plainTextEdit.clear()
        for strLine in strList:
            self.ui.plainTextEdit.appendPlainText(strLine)

    # 显示选中的行列信息
    def do_listview_clicked(self, index):
        self.ui.label.setText("当前项index: row=%d, column=%d" % (index.row(), index.column()))


if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建app
    form = QmyWidget()
    form.show()
    sys.exit(app.exec_())
