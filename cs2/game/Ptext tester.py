import pygame as pg
import ptext

pg.init()
screen = pg.display.set_mode((640, 480))
clock = pg.time.Clock()
BG_COLOR = pg.Color('gray12')
BLUE = pg.Color('dodgerblue')
# Triple quoted strings contain newline characters.
text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
    eiusmod tempor incididunt ut labore et dolore magna aliqua.

    Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris
    nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in
    reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
    pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
    culpa qui officia deserunt mollit anim id est laborum."""

done = False
while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True

    screen.fill(BG_COLOR)
    ptext.draw(text, (10, 10), color=BLUE)  # Recognizes newline characters.
    pg.display.flip()
    clock.tick(60)

pg.quit()
