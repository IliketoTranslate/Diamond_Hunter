import pygame as pg
from .defs import sc_height, wn

class ATM():
    def __init__(self) -> None:
        self.pos_x = 10
        self.width = 40
        self.height = 100
        self.pos_y = sc_height - self.height - 5
        self.hitbox = pg.rect.Rect(self.pos_x, self.pos_y, self.width, self.height)
        self.amount_money = 0
        self.last_ammn = 0
    def draw(self):
        self.hitbox = pg.rect.Rect(self.pos_x, self.pos_y, self.width, self.height)
        pg.draw.rect(wn, (255, 255, 255), self.hitbox)
    def turnSintoM(self, slimes):
        self.amount_money = slimes * 2
        return self.amount_money
