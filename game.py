import pygame as pg
from main import Main
from components import *

pg.init()

player = Player()

clock = pg.time.Clock()
run = True

all_objects = list()
all_objects.append(Rectangle(500, 400, 200, 50))
all_objects.append(Player())

main = Main(all_objects)

while run:
    clock.tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    bg_color = (0,0,0)
    wn.fill(bg_color)

    #rect = main.getRect()
    #to wyswietla prostokat z lewej dolnej strony ekranu
    main.ATMFunc()
    #co to robi ?
    main.PlateFunc(player)
    #to wyswietla prostokaciki na dole
    main.SlimeFactoriesStart()
    main.TextFunc()
    #to wyswietla prostokat w centrum ekranu
    #main.RectFunc()
    main.move()
    main.draw()

    pg.display.update()