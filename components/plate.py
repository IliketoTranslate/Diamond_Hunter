import pygame as pg
from .defs import wn

class Plate():
    def __init__(self, x, y, type, price) -> None:
        self.pos_x = x
        self.pos_y = y
        self.pos_x2 = x
        self.pos_y2 = y
        self.price = price
        self.is_pressed = False
        self.type = type
        self.width = 30
        self.height = 10
        self.hitbox = pg.rect.Rect(self.pos_x, self.pos_y, self.width, self.height)
        self.append = 0
    def draw(self):
        self.hitbox = pg.rect.Rect(self.pos_x, self.pos_y, self.width, self.height)
        pg.draw.rect(wn, (100, 10, 10), self.hitbox)
    def checkIsPressed(self, rect):
        number = 0
        if self.hitbox.colliderect(rect):
            self.is_pressed = True
            self.height = 5
            self.append = 1
        else:
            self.is_pressed = False
            self.height = 10
            self.append = -4
        number = self.pos_y2 + self.append
        self.pos_y = number
    def getIsPressed(self):
        return self.is_pressed
    def getType(self):
        return self.type
    def getPos(self):
        return self.pos_x, self.pos_y
    def getPrice(self):
        return self.price
