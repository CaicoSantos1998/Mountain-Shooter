# C
import pygame as pg

COLOR_ORANGE = (255, 128, 0)
COLOR_WHITE = (255, 255, 255)
# E
ENTITY_SPEED = {
    'Level1BG0': 0,
    'Level1BG1': 1,
    'Level1BG2': 2,
    'Level1BG3': 3,
    'Level1BG4': 4,
    'Level1BG5': 5,
    'ShipPlayer1': 2.5,
    'ShipPlayer1Shot': 2,
    'ShipPlayer2Shot': 2,
    'ShipPlayer2': 2.5,
    'ShipEnemy1': 2,
    'ShipEnemy1Shot': 4,
    'ShipEnemy2': 2,
    'ShipEnemy2Shot': 5,
}
ENTITY_HEALTH = {
    'Level1BG0': 999,
    'Level1BG1': 999,
    'Level1BG2': 999,
    'Level1BG3': 999,
    'Level1BG4': 999,
    # 'Level2BG0': 999,
    # 'Level2BG1': 999,
    # 'Level2BG2': 999,
    # 'Level2BG3': 999,
    # 'Level2BG4': 999,
    # 'Level3BG0': 999,
    # 'Level3BG1': 999,
    # 'Level3BG2': 999,
    # 'Level3BG3': 999,
    # 'Level3BG4': 999,
    # 'Level4BG0': 999,
    # 'Level4BG1': 999,
    # 'Level4BG2': 999,
    # 'Level4BG3': 999,
    # 'Level4BG4': 999,
    'ShipPlayer1': 200,
    'ShipPlayer1Shot': 1,
    'ShipPlayer2': 200,
    'ShipPlayer2Shot': 1,
    'ShipEnemy1': 280,
    'ShipEnemy2': 300,
    'ShipEnemy1Shot': 1,
    'ShipEnemy2Shot': 1,

}

EVENT_ENEMY = pg.USEREVENT + 1

ENTITY_SHOT_DELAY = {
    'ShipPlayer1': 20,
    'ShipPlayer2': 20,
    'ShipEnemy1': 80,
    'ShipEnemy2': 100
}
# M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'SCORE',
               'EXIT')
# P
PLAYER_KEY_W = {'ShipPlayer1':pg.K_w, 'ShipPlayer2':pg.K_UP}
PLAYER_KEY_S = {'ShipPlayer1':pg.K_s, 'ShipPlayer2':pg.K_DOWN}
PLAYER_KEY_A = {'ShipPlayer1':pg.K_a, 'ShipPlayer2':pg.K_LEFT}
PLAYER_KEY_D = {'ShipPlayer1':pg.K_d, 'ShipPlayer2':pg.K_RIGHT}
PLAYER_KEY_SHOOT = {'ShipPlayer1':pg.K_SPACE, 'ShipPlayer2':pg.K_RCTRL}
# S
SPAWN_ENEMY_TIME = 4000
SCREEN_WIDTH = 676
SCREEN_HEIGHT = 380
SIZE_TEXT = 120


