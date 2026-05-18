#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame as pg
import pygame.mixer_music

from code.Const import SCREEN_HEIGHT, SCREEN_WIDTH
from code.Menu import Menu


class Game:
    def __init__(self):
        #Setup start
        pg.init()
        self.screen = pg.display.set_mode(size=(SCREEN_HEIGHT, SCREEN_WIDTH))
        # Setup end

    def run(self):
        # Loop start
        while True:
            menu = Menu(self.screen)
            menu.run()
            pass