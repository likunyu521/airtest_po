# _*_ coding: UTF-8 _*_
from airtest.core.api import *
from airtest.cli.parser import cli_setup
import settings

class MainMenuScreen():
    """
    定义主菜单界面类
    """

    def __init__(self):
        """
        定义主菜单元素
        """
        self.elements = {
            '快速开始': Template(r'../pic/main_menu_screen/快速开始.png'),
            '争霸场': Template(r'../pic/main_menu_screen/争霸场.png'),
            '进阶场': Template(r'../pic/main_menu_screen/进阶场.png'),
            '今日赢家': Template(r'../pic/main_menu_screen/今日赢家.png')
        }

    def quick_start(self):
        """
        点击快速开始
        :return:None
        """
        wait(self.elements['快速开始'])
        touch(self.elements['快速开始'])

    def advanced(self):
        """
        点击进阶场
        :return:None
        """
        wait(self.elements['进阶场'])
        touch(self.elements['进阶场'])

    def tournament(self):
        """
        点击争霸场
        :return:
        """
        wait(self.elements['争霸场'])
        touch(self.elements['争霸场'])

    def swipe_today_winner(self, dirction='up'):
        """
        滑动今日玩家
        :param dirction: up向上，down向下
        :return:None
        """
        if dirction == 'up':
            wait(self.elements['今日赢家'])
            swipe(self.elements['今日赢家'],vector=[0,-0.4])
        elif dirction=='down':
            wait(self.elements['今日赢家'])
            swipe(self.elements['今日赢家'], vector=[0, -0.4])
        else:
            raise Exception


if __name__=='__main__':
    if not cli_setup():
        auto_setup(__file__, logdir=True, devices=settings.DEVICES, project_root=settings.PROJECT_ROOT)
    start_app(settings.PACKAGE_NAME)
    mm = MainMenuScreen()
    # mm.swipe_today_winner('up')
    mm.quick_start()