import pygame as pg

# C
COLOR_CYAN = (0, 128, 128)
COLOR_GREEN = (0, 128, 0)
COLOR_ORANGE = (255, 128, 0)
COLOR_YELLOW = (225, 255, 128)
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
# E
ENTITY_SPEED = {
    'Level1BG0': 0,
    'Level1BG1': 1,
    'Level1BG2': 2,
    'Level1BG3': 3,
    'Level1BG4': 4,
    'Level2BG0': 0,
    'Level2BG1': 1,
    'Level2BG2': 2,
    'Level2BG3': 3,
    'Level2BG4': 4,
    'Level3BG0': 0,
    'Level3BG1': 1,
    'Level3BG2': 2,
    'Level3BG3': 3,
    'Level3BG4': 4,
    'Level4BG0': 0,
    'Level4BG1': 1,
    'Level4BG2': 2,
    'Level4BG3': 3,
    'ShipPlayer1': 4,
    'ShipPlayer1Shot': 2.5,
    'ShipPlayer2Shot': 2.5,
    'ShipPlayer2': 4,
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
    'Level2BG0': 999,
    'Level2BG1': 999,
    'Level2BG2': 999,
    'Level2BG3': 999,
    'Level2BG4': 999,
    'Level3BG0': 999,
    'Level3BG1': 999,
    'Level3BG2': 999,
    'Level3BG3': 999,
    'Level3BG4': 999,
    'Level4BG0': 999,
    'Level4BG1': 999,
    'Level4BG2': 999,
    'Level4BG3': 999,
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
EVENT_TIMEOUT = pg.USEREVENT + 2
ENTITY_SHOT_DELAY = {
    'ShipPlayer1': 15,
    'ShipPlayer2': 15,
    'ShipEnemy1': 80,
    'ShipEnemy2': 100
}
ENTITY_DAMAGE = {
    'Level1BG0': 0,
    'Level1BG1': 0,
    'Level1BG2': 0,
    'Level1BG3': 0,
    'Level1BG4': 0,
    'Level2BG0': 0,
    'Level2BG1': 0,
    'Level2BG2': 0,
    'Level2BG3': 0,
    'Level2BG4': 0,
    'Level3BG0': 0,
    'Level3BG1': 0,
    'Level3BG2': 0,
    'Level3BG3': 0,
    'Level3BG4': 0,
    'Level4BG0': 0,
    'Level4BG1': 0,
    'Level4BG2': 0,
    'Level4BG3': 0,
    'ShipPlayer1': 1,
    'ShipPlayer1Shot': 45,
    'ShipPlayer2': 1,
    'ShipPlayer2Shot': 45,
    'ShipEnemy1': 1,
    'ShipEnemy1Shot': 35,
    'ShipEnemy2': 1,
    'ShipEnemy2Shot': 25
}
ENTITY_SCORE = {
    'Level1BG0': 0,
    'Level1BG1': 0,
    'Level1BG2': 0,
    'Level1BG3': 0,
    'Level1BG4': 0,
    'Level2BG0': 0,
    'Level2BG1': 0,
    'Level2BG2': 0,
    'Level2BG3': 0,
    'Level2BG4': 0,
    'Level3BG0': 0,
    'Level3BG1': 0,
    'Level3BG2': 0,
    'Level3BG3': 0,
    'Level3BG4': 0,
    'Level4BG0': 0,
    'Level4BG1': 0,
    'Level4BG2': 0,
    'Level4BG3': 0,
    'ShipPlayer1': 0,
    'ShipPlayer1Shot': 0,
    'ShipPlayer2': 0,
    'ShipPlayer2Shot': 0,
    'ShipEnemy1': 8,
    'ShipEnemy1Shot': 0,
    'ShipEnemy2': 5,
    'ShipEnemy2Shot': 0
}
# M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'SCORE',
               'EXIT')
# P
PLAYER_KEY_W = {'ShipPlayer1': pg.K_w, 'ShipPlayer2': pg.K_UP}
PLAYER_KEY_S = {'ShipPlayer1': pg.K_s, 'ShipPlayer2': pg.K_DOWN}
PLAYER_KEY_A = {'ShipPlayer1': pg.K_a, 'ShipPlayer2': pg.K_LEFT}
PLAYER_KEY_D = {'ShipPlayer1': pg.K_d, 'ShipPlayer2': pg.K_RIGHT}
PLAYER_KEY_SHOOT = {'ShipPlayer1': pg.K_SPACE, 'ShipPlayer2': pg.K_RCTRL}
# S
SPAWN_ENEMY_TIME = 4000
SCREEN_WIDTH = 676
SCREEN_HEIGHT = 380
SCORE_POS = {
    'Title': (SCREEN_WIDTH / 2, 50),
    'EnterName': (SCREEN_WIDTH / 2, 100),
    'Label': (SCREEN_WIDTH / 2, 90),
    'Name': (SCREEN_WIDTH / 2, 150),
    0: (SCREEN_WIDTH / 2, 120),
    1: (SCREEN_WIDTH / 2, 140),
    2: (SCREEN_WIDTH / 2, 160),
    3: (SCREEN_WIDTH / 2, 180),
    4: (SCREEN_WIDTH / 2, 200),
    5: (SCREEN_WIDTH / 2, 220),
    6: (SCREEN_WIDTH / 2, 240),
    7: (SCREEN_WIDTH / 2, 260),
    8: (SCREEN_WIDTH / 2, 280),
    9: (SCREEN_WIDTH / 2, 300),
}
# T
TEXT_SIZE_TITLE = 120
TEXT_SIZE_MENU = 45
TEXT_SIZE = 20
TIMEOUT_STEP = 100
TIMEOUT_LEVEL = 20000
