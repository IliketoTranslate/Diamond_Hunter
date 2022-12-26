import pygame as pg
from .defs import wn

class Player():
    def __init__(self) -> None:
        self.pos_x = 880
        self.pos_y = 845
        self.speed = 3
        self.width = 20
        self.height = 40
        self.hitbox = pg.rect.Rect(self.pos_x, self.pos_y, self.width, self.height)
        self.last_key = 0
        self.color = (255, 255, 255)
        self.id = 0
    def setId(self, id):
        self.id = id
    def getId(self):
        return self.id
    def is_movable(self):
        return True
    def is_playable(self):
        return True
    def get_speed(self):
        return self.speed
    def move(self):
        pass
    def draw(self):
        self.hitbox = pg.rect.Rect(self.pos_x, self.pos_y, self.width, self.height)
        pg.draw.rect(wn, (255, 255, 255), self.hitbox)
    def getRect(self):
        return self.color, self.hitbox
    def update(self, new_x, new_y):
        self.hitbox.move_ip(new_x, new_y)
