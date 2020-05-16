#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : Operate_system_ModeView_structure -> play1.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/4/30 16:25
@Desc    :
================================================="""
#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : Operate_system_ModeView_structure -> play.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/4/30 14:39
@Desc    :
================================================="""
# 爬虫请求第三方库
import requests
# 数据提取的第三方库
from lxml import etree


def main():
    # url = "http://pic.netbian.com/"
    # BIDUPSID=911CB3D73120CF08CE8A059786D95BFF; PSTM=1589533431;
    # BAIDUID=911CB3D73120CF08C00B237535283D13:FG=1;
    # BDORZ=B490B5EBF6F3CD402E515D22BCDA1598;
    # H_PS_PSSID=1447_31670_21090_31596_31464_31322_30823;
    # delPer=0; PSINO=7

    # __cfduid=d825bb9b9a68dfc08f88c0c4750fcd5181589544319;
    # Hm_lvt_526caf4e20c21f06a4e9209712d6a20e=1589544254;
    # zkhanecookieclassrecord=%2C66%2C;
    # Hm_lpvt_526caf4e20c21f06a4e9209712d6a20e=1589544339
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36"
    }

    # s = requests.Session()
    # s.get(url=url, headers=headers)
    # 随机生成的cookies
    # print(s.cookies)
    # print(s.cookies.items())
    # print(s.cookies.keys()[0])
    # print(s.cookies.values()[0])

    # response = requests.get(url, headers=headers).content.decode("gbk")

    for i in range(1):
        # 数据提取
        # html = etree.HTML(response)
        # clearfix = html.xpath('//ul[@class="clearfix"]/li/a/@href')
        # http://pic.netbian.com/downpic.php?id=25792&classid=60
        pic_url = "http://pic.netbian.com/downpic.php?id=25792&classid=60"
        s = requests.Session()
        img_response = s.get(url=pic_url, headers=headers)
        print(s.cookies)
        print(img_response)
        # f = open('./pictures/{}.jpg'.format(count), 'wb')
        # f.write(img_response.content)
        # f.close()


if __name__ == '__main__':
    main()

