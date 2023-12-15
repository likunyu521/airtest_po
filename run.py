# _*_ coding: UTF-8 _*_
# @Author   : likunyu。
# @其他      : 社群交流，公众号：李坤雨，发消息：可乐加冰

import unittest
from airtest.core.api import *
from airtest.report.report import simple_report
import settings

__author__ = settings.PROJECT_AUTHOR
__title__ = settings.PROJECT_TITLE
__desc__ = settings.PROJECT_DESC

print("hello airtest")

# 1 清除上一轮测试的报告的截图文件
dir = './log/'  # 选择删除文件夹路径
file_list = os.listdir(dir)  # 列出所有删除文件夹下的文件名加入列表
for f in file_list:  # 循环删除
    file_path = os.path.join(dir, f)  # 将待删除文件夹路径和文件名拼接为文件的绝对路径
    os.remove(file_path)  # 删除该文件

# 2.连接设备
auto_setup(__file__, logdir=True, devices=settings.DEVICES, project_root=settings.PROJECT_ROOT)

#如果没安装App，则安装下
APK = os.path.join(settings.PROJECT_ROOT, "blackjack.apk")
if settings.PACKAGE_NAME not in device().list_app():
    install(APK)

# 3.生成测试套件：以文件扫描的方式添加用例到测试套件
# unittest.defaultTestLoader.discover(扫描的文件夹路径, pattern='扫描的文件格式')
suite = unittest.defaultTestLoader.discover('./case/', pattern='*.py')

# 4.生成HTML运行器
runner = unittest.TextTestRunner()

# 5.运行器执行测试套件
runner.run(suite)

# 6.成成报告
simple_report(__file__, logpath=True)
