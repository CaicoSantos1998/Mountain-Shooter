#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Background import Background
from code.Const import SCREEN_WIDTH, SCREEN_HEIGHT
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
                return Player('ShipPlayer1', (10, SCREEN_HEIGHT/2))
        return None