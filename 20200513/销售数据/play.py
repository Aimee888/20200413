#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : Operate_system_ModeView_structure -> play.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/5/13 14:56
@Desc    :
================================================="""
import xlrd
from pyecharts.charts import Bar
import matplotlib.pyplot as plt

data = xlrd.open_workbook("销售数据.xlsx")
# print(data)

table = data.sheets()[0]  # 索引
# print(table)
# print(table.nrows)
# print(table.ncols)
# print(table.row_values(0))
# print(table.row_values(1))
names = []
sales = []
for i in range(1, table.nrows):
    # print(table.row_values(i))
    names.append(table.row_values(i)[0])
    sales.append(table.row_values(i)[2])
# print(names)
# print(sales)
bar = Bar()
bar.add_xaxis(names)
bar.add_yaxis("业务详情", sales)
bar.render('data.html')


# 第二种方式：matlab 绘图
# 设置中文字体
# plt.rcParams['font.sans-serif'] = ['SimHei']
zhong = 0
nan = 0
bei = 0
for i in range(1, table.nrows):
    di = table.row_values(i)[3]
    if di == "华中":
        zhong += table.row_values(i)[2]
    elif di == "华南":
        nan += table.row_values(i)[2]
    elif di == "华北":
        bei += table.row_values(i)[2]
    else:
        pass
# print(zhong)
# print(nan)
# print(bei)

# 部门业绩
sales_bm = []
sales_bm.append(zhong)
sales_bm.append(nan)
sales_bm.append(bei)
# print(sales_bm)

fracs = []

for i in sales_bm:
    i = i / sum(sales_bm)
    fracs.append(i)
print(fracs)

labels = ['华中', '华南', '华北']
explode = [0.2, 0, 0]
plt.pie(x=fracs, labels=labels, autopct="%.2f%%", explode=explode, shadow=True)
plt.legend()
plt.show()

