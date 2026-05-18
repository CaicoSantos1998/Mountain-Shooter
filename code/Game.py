#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame as pg

from code.Menu import Menu


class Game:
    def __init__(self):
        #Setup start
        pg.init()
        self.screen = pg.display.set_mode(size=(600, 480))
        # Setup end

    def run(self):
        # Loop start
        while True:
            menu = Menu(self.screen)
            menu.run()
            pass
            # Check for all events
            # for event in pg.event.get():
            #     if event.type == pg.QUIT:
            #         pg.quit() # Close window
            #         quit() # end pg