# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_event.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(603, 318)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.LabMove = QtWidgets.QLabel(self.centralwidget)
        self.LabMove.setGeometry(QtCore.QRect(50, 30, 161, 31))
        self.LabMove.setObjectName("LabMove")
        self.btnMove = QtWidgets.QPushButton(self.centralwidget)
        self.btnMove.setGeometry(QtCore.QRect(40, 170, 171, 51))
        self.btnMove.setObjectName("btnMove")
        self.btnTest = QtWidgets.QPushButton(self.centralwidget)
        self.btnTest.setGeometry(QtCore.QRect(300, 90, 171, 51))
        self.btnTest.setObjectName("btnTest")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 603, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.LabMove.setText(_translate("MainWindow", "TextLabel"))
        self.btnMove.setText(_translate("MainWindow", "PushButton"))
        self.btnTest.setText(_translate("MainWindow", "PushButton"))
