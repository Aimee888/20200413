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
        Form.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.LabHover = QtWidgets.QLabel(Form)
        self.LabHover.setAlignment(QtCore.Qt.AlignCenter)
        self.LabHover.setObjectName("LabHover")
        self.verticalLayout.addWidget(self.LabHover)
        self.LabDBClick = QtWidgets.QLabel(Form)
        self.LabDBClick.setAlignment(QtCore.Qt.AlignCenter)
        self.LabDBClick.setObjectName("LabDBClick")
        self.verticalLayout.addWidget(self.LabDBClick)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.LabHover.setText(_translate("Form", "button released"))
        self.LabDBClick.setText(_translate("Form", "可双击的标签"))
