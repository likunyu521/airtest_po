# _*_ coding: UTF-8 _*_
import unittest
from page.game_screen import GameScreen
from page.main_menu_screen import MainMenuScreen
from airtest.core.api import *
from airtest.cli.parser import cli_setup
import settings


class PlayGame(unittest.TestCase):
    def setUp(self) -> None:
        # if not cli_setup():
        auto_setup(__file__, logdir=True, devices=settings.DEVICES, project_root=settings.PROJECT_ROOT)
        start_app(settings.PACKAGE_NAME)
        self.mms = MainMenuScreen()
        self.gs = GameScreen()

    def test_play(self):
        #点击快速开始
        self.mms.quick_start()
        #点击10k
        self.gs.touch_10k()
        #点击投注
        self.gs.touch_bet()
        #点击停牌
        self.gs.touch_hit()
        #点击下注
        self.gs.touch_start()
        #点击返回
        # self.gs.back()

    def tearDown(self) -> None:
        gs = None
        mms = None
        stop_app(settings.PACKAGE_NAME)


if __name__ == "__main__":
    unittest.main()