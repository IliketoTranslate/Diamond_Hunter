import pygame as pg
from .defs import wn

class Player():
    def __init__(self) -> None:
        self.pos_x = 880
        self.pos_y = 855
        self.speed = 3
        self.width = 20
        self.height = 40
        self.hitbox = pg.rect.Rect(self.pos_x, self.pos_y, self.width, self.height)
        self.last_key = 0
    def move_up(self):
        self.pos_y -= self.speed
    def move_down(self):
        self.pos_y += self.speed
    def move_left(self):
        self.pos_x -= self.speed
    def move_rigth(self):
        self.pos_x += self.speed
    def move(self, rect):
        keys = pg.key.get_pressed()
        if not(self.hitbox.colliderect(rect)):
            if not(self.pos_y < 10):
                if keys[pg.K_w]:
                    self.move_up()
                    self.last_key = "w"
            if not(self.pos_x < 10):
                if keys[pg.K_a]:
                    self.move_left()
                    self.last_key = "a"
            if not(self.pos_y > 850):
                if keys[pg.K_s]:
                    self.move_down()
                    self.last_key = "s"
            if not(self.pos_x > 1770):
                if keys[pg.K_d]:
                    self.move_rigth()
                    self.last_key = "d"
        else:
            if self.last_key == "w":
                self.move_down()
            if self.last_key == "a":
                self.move_rigth()
            if self.last_key == "s":
                self.move_up()
            if self.last_key == "d":
                self.move_left()
            
        #print("position x = " + str(self.pos_x) + " position y = " + str(self.pos_y)) 
    def draw(self):
        self.hitbox = pg.rect.Rect(self.pos_x, self.pos_y, self.width, self.height)
        pg.draw.rect(wn, (255, 255, 255), self.hitbox)
    def getRect(self):
        return self.hitbox
