#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame as pg
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import SCREEN_WIDTH, COLOR_ORANGE, SIZE_TEXT, MENU_OPTION, COLOR_WHITE


class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.surf = pg.image.load('./assert/MenuBG.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        pg.mixer_music.load('./assert/Menu-music.wav')
        pg.mixer_music.play(-1)
        while True:
            self.screen.blit(source=self.surf, dest=self.rect)
            self.menu_text(SIZE_TEXT, "Mountain", COLOR_ORANGE, (SCREEN_WIDTH, 70))
            self.menu_text(SIZE_TEXT, "Shooter", COLOR_ORANGE, (SCREEN_WIDTH, 110))
            for i in range(len(MENU_OPTION)):
                self.menu_text(40, MENU_OPTION[i], COLOR_WHITE, (SCREEN_WIDTH, 200 + 25 * i))
            pg.display.flip()
            #Check for all events
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit() # Close window
                    quit() # end pg

    def menu_text(self, text_size:int, text:str, text_color:tuple, text_center_pos:tuple):
        text_font: Font = pg.font.SysFont(name="Lucida Sans Typerwriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.screen.blit(source=text_surf, dest=text_rect)
