#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys

import pygame as pg
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import COLOR_WHITE, MENU_OPTION, EVENT_ENEMY, SPAWN_ENEMY_TIME, COLOR_GREEN, COLOR_CYAN, EVENT_TIMEOUT, \
    TIMEOUT_STEP, TIMEOUT_LEVEL, TEXT_SIZE
from code.Enemy import Enemy
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player


class Level:
    def __init__(self, screen:Surface, name:str, game_mode:str, player_score:list[int]):
        self.screen = screen
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.timeout = TIMEOUT_LEVEL
        self.player_score = player_score
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'BG'))
        player = EntityFactory.get_entity('ShipPlayer1')
        player.score = player_score[0]
        self.entity_list.append(player)
        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            player = EntityFactory.get_entity('ShipPlayer2')
            player.score = player_score[1]
            self.entity_list.append(player)
        pg.time.set_timer(EVENT_ENEMY, SPAWN_ENEMY_TIME)
        pg.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)

    def run(self, player_score:list[int]):
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
                if entity.name == 'ShipPlayer1':
                    self.level_text(TEXT_SIZE, f'Player 1 - Health: {entity.health} | Score: {entity.score}',
                                    COLOR_GREEN, (5, 25))
                if entity.name == 'ShipPlayer2':
                    self.level_text(TEXT_SIZE, f'Player 2 - Health: {entity.health} | Score: {entity.score}',
                                    COLOR_CYAN, (5, 45))
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('ShipEnemy1', 'ShipEnemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout == 0:
                        for entity in self.entity_list:
                            if isinstance(entity, Player) and entity.name == 'ShipPlayer1':
                                player_score[0] = entity.score
                            if isinstance(entity, Player) and entity.name == 'ShipPlayer2':
                                player_score[1] = entity.score
                        return True
            found_player = False
            for entity in self.entity_list:
                if isinstance(entity, Player):
                    found_player = True
            if not found_player:
                return False

            self.level_text(TEXT_SIZE, f'{self.name}', COLOR_WHITE, (5, 5))
            self.level_text(TEXT_SIZE, f'TIME: {self.timeout / 1000:.1f}s', COLOR_WHITE, (590, 5))
            self.level_text(TEXT_SIZE, f'FPS: {clock.get_fps():.0f}', COLOR_WHITE,
                            (50, 5))
            pg.display.flip()

            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pg.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.screen.blit(source=text_surf, dest=text_rect)