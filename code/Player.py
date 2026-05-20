#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame as pg

from code.Const import ENTITY_SPEED, SCREEN_HEIGHT, SCREEN_WIDTH, PLAYER_KEY_W, PLAYER_KEY_S, PLAYER_KEY_A, PLAYER_KEY_D
from code.Entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, ):
        pressed_key = pg.key.get_pressed()
        if pressed_key[PLAYER_KEY_W[self.name]] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_KEY_S[self.name]] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_KEY_A[self.name]] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_KEY_D[self.name]] and self.rect.right < SCREEN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]
