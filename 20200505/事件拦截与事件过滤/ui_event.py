# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_event.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(624, 389)
        self.btnTest = QtWidgets.QPushButton(Form)
        self.btnTest.setGeometry(QtCore.QRect(420, 110, 121, 51))
        self.btnTest.setObjectName("btnTest")
        self.btnMove = QtWidgets.QPushButton(Form)
        self.btnMove.setGeometry(QtCore.QRect(60, 250, 141, 51))
        self.btnMove.setObjectName("btnMove")
        self.LabMove = QtWidgets.QLabel(Form)
        self.LabMove.setGeometry(QtCore.QRect(80, 60, 171, 21))
        self.LabMove.setText("")
        self.LabMove.setObjectName("LabMove")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btnTest.setText(_translate("Form", "resizeEvent事件"))
        self.btnMove.setText(_translate("Form", "moveable Button"))
