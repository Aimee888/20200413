# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_hasImage.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(588, 441)
        self.LabPic = QtWidgets.QLabel(Form)
        self.LabPic.setGeometry(QtCore.QRect(10, 10, 561, 421))
        self.LabPic.setText("")
        self.LabPic.setObjectName("LabPic")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "图片"))
