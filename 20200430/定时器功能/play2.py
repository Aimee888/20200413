#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : FDS -> play2.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/4/30 10:45
@Desc    :
================================================="""
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QThread, pyqtSignal, QTimer
from ui_play import Ui_MainWindow


class TimeStop(QThread):
    time_stop = pyqtSignal()  # 当时间停止的信号

    def __init__(self):
        super().__init__()

    def run(self):
        # ====================
        # 进行一些列操作
        for i in range(60000000):
            if i % 10000000 == 0:
                print(i / 10000000 + 1)

        # ====================
        self.time_stop.emit()


class QmyMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数
        self.ui = Ui_MainWindow()  # 创建UI对象
        self.ui.setupUi(self)  # 构造UI

        self.ui.label.setText("Elapsed Time".ljust(18) + "00:00:00")

        # 开启定时器
        self.curtime = 0
        self.timer = QTimer()
        self.timer.start(1000)  # 计时器每秒计数
        # 绑定计时器显示标签
        self.timer.timeout.connect(self.do_elapsed_time_set)

        self.myThread = TimeStop()
        self.myThread.time_stop.connect(self.do_time_stop)
        self.myThread.start()

    # 秒表显示
    def do_elapsed_time_set(self):
        # 显示流逝的时间
        self.curtime = self.curtime + 1
        hours = self.curtime / 3600
        minutes_curtime = self.curtime % 3600
        minutes = minutes_curtime / 60
        seconds_curtime = minutes_curtime % 60
        seconds = seconds_curtime
        str_time = "%02d:%02d:%02d" % (hours, minutes, seconds)
        self.ui.label.setText("Elapsed Time".ljust(18) + str_time)

    def do_time_stop(self):
        self.timer.stop()
        self.ui.label_2.setText("Stoped")


if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建app
    form = QmyMainWindow()
    form.show()
    sys.exit(app.exec_())
