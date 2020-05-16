#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : Operate_system_ModeView_structure -> play1.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/5/15 11:09
@Desc    :
================================================="""
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
from ui_play1 import Ui_Form


class QmyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数
        self.ui = Ui_Form()  # 创建UI对象
        self.ui.setupUi(self)  # 构造UI

        self.ui.treeWidget.expandAll()
        self.ui.treeWidget.setColumnWidth(0, 200)
        self.ui.treeWidget.setStyleSheet("QHeaderView::section{background:rgb(85, 170, 127);}")

        self.ui.btnSetCheckBox.clicked.connect(self.do_btn_set_checkbox_clicked)

    def do_btn_set_checkbox_clicked(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建app
    form = QmyWidget()
    form.show()
    sys.exit(app.exec_())

