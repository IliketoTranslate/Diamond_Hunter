import pygame as pg
from .defs import sc_height, wn

class SlimeFactory():
    def __init__(self, posx, width, height) -> None:
        self.factory_speed = 1
        self.factory_pos_x = posx
        self.factory_pos_y = sc_height - height - 5
        self.factory_witdh = width
        self.factory_height = height
        self.slime_pos_x = self.factory_pos_x + self.factory_witdh - 20
        self.slime_pos_y = self.factory_pos_y - 15
        self.slime_width = 15
        self.slime_height = self.slime_width
        self.factory_hitbox = pg.rect.Rect(self.factory_pos_x, self.factory_pos_y, self.factory_witdh, self.factory_height)
        self.slime_hitbox = pg.rect.Rect(self.slime_pos_x, self.slime_pos_y, self.slime_width, self.slime_height)
        self.slime_road_x = self.factory_witdh - 20
        self.slime_road_y = self.factory_height
        self.amount_slime = 0
    def draw(self):
        self.factory_hitbox = pg.rect.Rect(self.factory_pos_x, self.factory_pos_y, self.factory_witdh, self.factory_height)      
        self.slime_hitbox = pg.rect.Rect(self.slime_pos_x, self.slime_pos_y, 15, 15)
        pg.draw.rect(wn, (200, 200, 210), self.factory_hitbox)
        pg.draw.rect(wn, (10, 200, 100), self.slime_hitbox)
    def move_slime(self):
        if not(self.slime_road_x < -15):
            self.slime_pos_x -= self.factory_speed
            self.slime_road_x -= self.factory_speed
        elif not(self.slime_road_y < 1):
            self.slime_pos_y += self.factory_speed
            self.slime_road_y -= self.factory_speed
        if self.slime_pos_x <= self.factory_pos_x - 10 and self.slime_pos_y >= self.factory_pos_y + self.factory_height - self.slime_height:
            self.slime_pos_x = self.factory_pos_x + self.factory_witdh - 20
            self.slime_pos_y = self.factory_pos_y - 15
            self.slime_road_x = self.factory_witdh - 20
            self.slime_road_y = self.factory_height
            self.amount_slime += 1
    def resetAmsl(self):
        self.amount_slime = 0
    def getAmountSlime(self):
        return self.amount_slime
