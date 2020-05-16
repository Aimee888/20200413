#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : Operate_system_ModeView_structure -> play.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/5/15 14:48
@Desc    :
================================================="""
import xlrd  # xlrd(read) xlwt(write)
import pygal


def main():
    data = xlrd.open_workbook('heros.xlsx')
    table = data.sheets()[0]
    radar_chart = pygal.Radar()
    radar_chart.title = "英雄能力值"
    # print(table.ncols)
    for i in range(table.nrows):
        if i == 0:
            title = table.row_values(i)
            radar_chart.x_labels = title[1:]
            print(title)
        else:
            data = table.row_values(i)
            radar_chart.add(data[0], data[1:])
            print(data)

    radar_chart.render_to_file('heros.html')


if __name__ == '__main__':
    main()

