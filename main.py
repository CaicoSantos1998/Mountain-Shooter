import pygame as pg

# Setup start
pg.init()
screen = pg.display.set_mode(size=(600, 480))
# Setup end

# Loop start
while True:
    # Check for all events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit() # Close window
            quit() # end pg