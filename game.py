import pygame as pg
from main import Main
from components import *

pg.init()

player = Player()

main = Main(player)
clock = pg.time.Clock()
run = True
while run:
    clock.tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    bg_color = (0,0,0)
    wn.fill(bg_color)

    #rect = main.getRect()
    main.ATMFunc()
    main.PlateFunc()
    main.SlimeFactoriesStart()
    main.TextFunc()
    main.RectFunc()
    player.draw()

    pg.display.update()