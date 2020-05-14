#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : Operate_system_ModeView_structure -> play.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/5/11 14:40
@Desc    :
================================================="""
from play1 import *


if __name__ == '__main__':
    # 获取当前路径
    print("打印当前目录：", end='')
    print(os.getcwd())

    # 获取上层目录
    print("打印当前文件目录的上层目录：", end='')
    print(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

    print("打印当前目录的上层目录：", end='')
    print(os.path.abspath(os.path.dirname(os.getcwd())))

    print("打印当前目录的上层目录（2）：", end='')
    print(os.path.abspath(os.path.join(os.getcwd(), "..")))

    # 获取上上级目录
    print("打印当前目录的上上级目录：", end='')
    print(os.path.abspath(os.path.join(os.getcwd(), "../..")))

    # 获取当前文件的路径（__file__是当前执行的文件）
    print("打印当前文件路径：", end='')
    print(os.path.abspath(__file__))

    # 用play1.py里面的函数打印__file__的路径
    print("打印当前文件路径（1）：", end='')
    print_file_path()

    # 打印主程序的路径
    print("打印主程序路径：", end='')
    print(os.path.abspath(sys.argv[0]))

    # 用play1.py里面的函数打印主程序路径
    print("打印主程序路径（1）：", end='')
    print_main_path()

    # 打印主程序目录
    print("打印主程序目录：", end='')
    print(os.path.abspath(sys.path[0]))

    # 切换路径到根路径
    path = "F:/"
    os.chdir(path)
    print("切换后的路径：", end='')
    print(os.getcwd())

