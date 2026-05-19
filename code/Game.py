#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame as pg

from code.Const import SCREEN_HEIGHT, SCREEN_WIDTH, MENU_OPTION
from code.Level import Level
from code.Menu import Menu


class Game:
    def __init__(self):
        #Setup start
        pg.init()
        self.screen = pg.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
        # Setup end

    def run(self):
        # Loop start
        while True:
            menu = Menu(self.screen)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                level = Level(self.screen, 'LEVEL - 1', menu_return)
                level_return = level.run()
            elif menu_return == MENU_OPTION[4]:
                pg.quit()
                quit()
            else:
                pass