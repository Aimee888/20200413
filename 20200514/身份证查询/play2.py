#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : Operate_system_ModeView_structure -> play2.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/5/15 9:29
@Desc    :
================================================="""
import configparser


def get_position(identified_num):
    id = identified_num[:6]
    id_lib_path = "id.ini"
    conf = configparser.ConfigParser()
    conf.read(id_lib_path, encoding='utf-8')
    position = conf.get("ID", id)
    return position


def get_born(identified_num):
    born = identified_num[6: 14]
    return born


def get_sex(identified_num):
    sex_num = identified_num[-2]
    if int(sex_num) % 2 == 0:
        sex = "女"
    else:
        sex = "男"
    return sex


def get_zodiac(identified_num):
    zodiac_dic = {0: "鼠", 1: "牛", 2: "虎", 3: "兔", 4: "龙", 5: "蛇", 6: "马", 7: "羊", 8: "猴", 9: "鸡", 10: "狗", 11: "猪"}
    zodiac = zodiac_dic[(int(identified_num[6: 10]) - 1972) % 12]
    return zodiac


def get_star(identified_num):
    star_dic = ["水瓶座", "双鱼座", "白羊座", "金牛座", "双子座", "巨蟹座", "狮子座", "处女座", "天秤座", "天蝎座", "射手座", "摩羯座"]
    star_day_end = (20, 19, 21, 20, 21, 22, 23, 23, 23, 24, 23, 22)
    month_star = int(identified_num[10:12]) - 1
    if int(identified_num[12:14]) > star_day_end[month_star]:
        star = star_dic[month_star]
    else:
        star = star_dic[month_star - 1]
    return star


def main():
    identified_num = input("请输入身份证号: ")
    position = get_position(identified_num)
    print("省/市/县: ", position)

    born = get_born(identified_num)
    print("年/月/日:  {}年{}月{}日".format(born[:4], born[4:6], born[6:]))

    sex = get_sex(identified_num)
    print(" 性  别 ： " + sex)

    zodiac = get_zodiac(identified_num)
    print(" 生  肖 ： " + zodiac)

    star = get_star(identified_num)
    print(" 星  座 ： " + star)


if __name__ == '__main__':
    main()
