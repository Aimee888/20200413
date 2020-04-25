# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_QStringListModel.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(614, 444)
        self.gridLayout_3 = QtWidgets.QGridLayout(Form)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.splitter_2 = QtWidgets.QSplitter(Form)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.splitter = QtWidgets.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.groupBox = QtWidgets.QGroupBox(self.splitter)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 0, 0, 1, 1)
        self.btnList_Append = QtWidgets.QPushButton(self.groupBox)
        self.btnList_Append.setObjectName("btnList_Append")
        self.gridLayout_2.addWidget(self.btnList_Append, 1, 0, 1, 1)
        self.btnList_Insert = QtWidgets.QPushButton(self.groupBox)
        self.btnList_Insert.setObjectName("btnList_Insert")
        self.gridLayout_2.addWidget(self.btnList_Insert, 1, 1, 1, 1)
        self.btnList_Delete = QtWidgets.QPushButton(self.groupBox)
        self.btnList_Delete.setObjectName("btnList_Delete")
        self.gridLayout_2.addWidget(self.btnList_Delete, 2, 0, 1, 1)
        self.btnList_Clear = QtWidgets.QPushButton(self.groupBox)
        self.btnList_Clear.setObjectName("btnList_Clear")
        self.gridLayout_2.addWidget(self.btnList_Clear, 2, 1, 1, 1)
        self.listView = QtWidgets.QListView(self.groupBox)
        self.listView.setObjectName("listView")
        self.gridLayout_2.addWidget(self.listView, 3, 0, 1, 2)
        self.groupBox_2 = QtWidgets.QGroupBox(self.splitter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 0, 0, 1, 1)
        self.btnText_Display = QtWidgets.QPushButton(self.groupBox_2)
        self.btnText_Display.setObjectName("btnText_Display")
        self.gridLayout.addWidget(self.btnText_Display, 1, 0, 1, 1)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 2, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.splitter_2)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.gridLayout_3.addWidget(self.splitter_2, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "QListView"))
        self.pushButton.setText(_translate("Form", "恢复列表"))
        self.btnList_Append.setText(_translate("Form", "添加项"))
        self.btnList_Insert.setText(_translate("Form", "插入项"))
        self.btnList_Delete.setText(_translate("Form", "删除当前项"))
        self.btnList_Clear.setText(_translate("Form", "清空列表"))
        self.groupBox_2.setTitle(_translate("Form", "QPlainTextEdit"))
        self.pushButton_6.setText(_translate("Form", "清空文本"))
        self.btnText_Display.setText(_translate("Form", "显示数据模型的StringList"))
        self.label.setText(_translate("Form", "TextLabel"))
