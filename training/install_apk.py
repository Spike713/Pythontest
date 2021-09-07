#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time     :
# @Author   : Spike713
# @Site     :
# @File     : install_apk.py
# @Purpose  :
# @Software : PyCharm
# @Copyright:
# @Licence  :
import os

apkpath_list = []


def get_all_apk(path: str) -> list:
    """
	遍历文件目录把所有apk的路径存入list
	:param path:
	:return:
	"""
    for file in os.listdir(path):  # 列出所有文件夹或文件名
        filepath = os.path.join(path, file)  # os.path.join:将路径与文件或文件夹合在一起
        if os.path.isfile(filepath):  # 路径是否为文件
            if os.path.basename(filepath).endswith('.apk'):  # 查找”.apk“结尾的文件
                apkpath_list.append(filepath)  # apkpath_list列表里加入上面查找到的文件
            else:
                continue
        elif os.path.isdir(filepath):  # 路径为目录
            get_all_apk(filepath)  # 回到上面，继续执行get_all_apk方法


def install_apk(apklist: list):
    """
	遍历存放apk绝对路径的list,调用adb命令
	:param apklist:
	:return:
	"""
    for apk in apklist:
        os.system('adb install -r' + apk)


if __name__ == '__main__':
    s = get_all_apk('/Users/kagami/Desktop/apk')
    print(apkpath_list)
    install_apk(apkpath_list)
