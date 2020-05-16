#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : Operate_system_ModeView_structure -> wangyiyun.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/5/15 20:34
@Desc    :1. 百度搜索网易云音乐，打开官方网站，右键检查
            2. 在检查窗口选中network，All
            3. 在音乐窗口搜索歌手名（如周杰伦）, 选择单曲
            4. 在检查窗口左侧找到web?csrf_token=那一行，点击它，右侧点击Headers
            5. 在General里面的Request URL就是我们要访问的URL
            6. 在Form Data里面的数据就是我们的data数据
            7. 在Request Headers下面的user-agent就是浏览器需要的头
================================================="""
import requests
headers = {
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36"
}
url = "https://music.163.com/weapi/cloudsearch/get/web?csrf_token="
data = {
    "params": "poJNqTPQml5d6n2XKErzjg/nSDSw0BT/e74QPbpd2r22QXa9uLkaY/N0oC36SmFGF53QubHtb/VEO0cme7WfbNc+m/phXLSiY+2Wntq6O1MNLi5NZzomQa0cWGybCKxeVhTYlHijG4ndqKbeAD2adPZmZDIonnEz1Ekfdb27HWX/JqQkZlv09Mb5QwzHGq/JgVpFGPwUBe/OXmYDy91FH4YvMBfPBWrqnn0H41jipOgbrgd/MEW1ikaxadN8i7Bf40YvpURWNp4bLsUG1Px6sotU5ALuD+JkD3JXGO++Ru4=",
    "encSecKey": "678d25b43e5420c0efdabd4ed2de013fac94a81fb3421e00f42ac7d02a851e30b6f34db3eba94b5eb5a207a8d2c04ee6d096417dbe6370b7c709756c8f46939054744134df2d42be47c6cfba79b5f522fcbe997e0b2facdbd4951520624f6f629a274676c9aee4038070d2d577b7d5b7462a79626ea5f7dd9f1fef95061918e1"
}
res = requests.post(url, headers=headers, data=data).json()
songs_list = res['result']['songs']
for song in songs_list:
    id_song = song['id']
    name_song = song['name']
    print(id_song, name_song)
    newurl = "http://music.163.com/song/media/outer/url?id={}.mp3".format(id_song)

