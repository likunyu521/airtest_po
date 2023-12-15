# _*_ coding: UTF-8 _*_
# @Time     : 2020/11/26 下午 05:48
# @Author   : Li Jie
# @Site     : http://www.cdtest.cn/
# @File     : game_screen.py
# @Software : PyCharm

from airtest.core.api import *
from airtest.cli.parser import cli_setup
import settings

class GameScreen():
    """
    定义游戏屏类
    """

    def __init__(self):
        """
        定义界面元素
        """
        self.elements = {
            '返回': Template(r'../pic/game_screen/返回.png'),
            '清空投注': Template(r'../pic/game_screen/清空投注.png'),
            '10k': Template(r'../pic/game_screen/10k.png'),
            '5k': Template(r'../pic/game_screen/5k.png'),
            '2k': Template(r'../pic/game_screen/2k.png'),
            '1k': Template(r'../pic/game_screen/1k.png'),
            '投注': Template(r'../pic/game_screen/投注.png'),
            '停牌': Template(r'../pic/game_screen/停牌.png'),
            '要牌': Template(r'../pic/game_screen/要牌.png'),
            '双倍': Template(r'../pic/game_screen/双倍.png'),
            '下注': Template(r'../pic/game_screen/下注.png'),
        }

    def back(self):
        """
        点击返回
        :return: None
        """
        wait(self.elements['返回'])
        touch(self.elements['返回'])

    def touch_clear(self):
        """
        点击清空下注
        :return: None
        """
        wait(self.elements['清空投注'])
        touch(self.elements['清空投注'])

    def touch_10k(self):
        """
        点击10k筹码
        :return: None
        """
        wait(self.elements['10k'])
        touch(self.elements['10k'])

    def touch_5k(self):
        """
        点击5k筹码
        :return: None
        """
        wait(self.elements['5k'])
        touch(self.elements['5k'])

    def touch_2k(self):
        """
        点击2k筹码
        :return: None
        """
        wait(self.elements['2k'])
        touch(self.elements['2k'])

    def touch_1k(self):
        """
        点击1k筹码
        :return: None
        """
        wait(self.elements['1k'])
        touch(self.elements['1k'])

    def touch_bet(self):
        """
        点击投注
        :return: None
        """
        wait(self.elements['投注'])
        touch(self.elements['投注'])

    def touch_stand(self):
        """
        点击停牌
        :return: None
        """
        wait(self.elements['停牌'])
        touch(self.elements['停牌'])

    def touch_hit(self):
        """
        点击要牌
        :return: None
        """
        wait(self.elements['要牌'])
        touch(self.elements['要牌'])

    def touch_double(self):
        """
        点击双倍
        :return: None
        """
        wait(self.elements['双倍'])
        touch(self.elements['双倍'])

    def touch_start(self):
        """
        点击下注
        :return: None
        """
        wait(self.elements['下注'])
        touch(self.elements['下注'])


if __name__ == '__main__':
    if not cli_setup():
        auto_setup(__file__, logdir=True, devices=settings.DEVICES, project_root=settings.PROJECT_ROOT)
    start_app(settings.PACKAGE_NAME)
    gs = GameScreen()
    # gs.back()
    gs.touch_10k()
    gs.touch_bet()
    gs.touch_hit()
    gs.touch_start()