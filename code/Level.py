#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys

import pygame as pg
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import COLOR_WHITE, SCREEN_HEIGHT, MENU_OPTION, EVENT_ENEMY, SPAWN_ENEMY_TIME
from code.Enemy import Enemy
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player


class Level:
    def __init__(self, screen, name, game_mode):
        self.screen = screen
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1BG'))
        self.entity_list.append(EntityFactory.get_entity('ShipPlayer1'))
        self.timeout = 20000
        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            self.entity_list.append(EntityFactory.get_entity('ShipPlayer2'))
        pg.time.set_timer(EVENT_ENEMY, SPAWN_ENEMY_TIME)

    def run(self):
        pg.mixer_music.load(f'./asset/{self.name}.mp3')
        pg.mixer_music.play(-1)
        clock = pg.time.Clock()
        while True:
            clock.tick(60)
            for entity in self.entity_list:
                self.screen.blit(source=entity.surf, dest=entity.rect)
                entity.move()
                if isinstance(entity, (Player, Enemy)):
                    shoot = entity.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('ShipEnemy1', 'ShipEnemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))

            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', COLOR_WHITE, (10, 5))
            self.level_text(14, f'FPS: {clock.get_fps():.0f}', COLOR_WHITE, (10, SCREEN_HEIGHT - 35))
            self.level_text(14, f'ENTITIES: {len(self.entity_list)}', COLOR_WHITE, (10, SCREEN_HEIGHT - 20))
            pg.display.flip()

            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pg.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.screen.blit(source=text_surf, dest=text_rect)
