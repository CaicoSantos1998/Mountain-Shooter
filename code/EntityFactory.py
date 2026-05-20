#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.Background import Background
from code.Const import SCREEN_WIDTH, SCREEN_HEIGHT
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'Level1BG':
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'Level1BG{i}', (0,0)))
                    list_bg.append(Background(f'Level1BG{i}', (SCREEN_WIDTH, 0)))
                return list_bg
            case 'ShipPlayer1':
                return Player('ShipPlayer1', (10, SCREEN_HEIGHT/2 - 30))
            case 'ShipPlayer2':
                return Player('ShipPlayer2', (10, SCREEN_HEIGHT/2 + 30))
            case 'ShipEnemy1':
                return Enemy('ShipEnemy1', (SCREEN_WIDTH+10, random.randint(40, SCREEN_HEIGHT - 40)))
            case 'ShipEnemy2':
                return Enemy('ShipEnemy2', (SCREEN_WIDTH + 10, random.randint(40, SCREEN_HEIGHT - 40)))
        return None