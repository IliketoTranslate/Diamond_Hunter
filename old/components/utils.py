import pygame as pg
from .defs import wn

class Text():
    def __init__(self, x, y, text, color) -> None:
        self.pos_x = x
        self.pos_y = y
        self.text = text
        self.color = color
        self.font = pg.font.SysFont("Calibri", 48)
        self.wrtx = pg.font.Font.render(self.font, self.text, True, self.color)
    def drawTextVar(self, text):
        self.text = text
        self.wrtx = pg.font.Font.render(self.font, self.text, True, self.color)
        wn.blit(self.wrtx, (self.pos_x, self.pos_y))
    def getPos(self):
        return self.pos_x, self.pos_y

class Rect():
    def __init__(self, x, y, width, height) -> None:
        self.pos_x = x
        self.pos_y = y
        self.width = width
        self.height = height
        self.id = 0
        self.rect = pg.rect.Rect(self.pos_x, self.pos_y, self.width, self.height)
    def setId(self, id):
        self.id = id
    def draw(self):
        self.rect = pg.rect.Rect(self.pos_x, self.pos_y, self.width, self.height)
        pg.draw.rect(wn, (100, 100, 100), self.rect)
    #TODO: wprowadzajace w blad nazewnictwo: obiekt jest typu Rect i skladnik jest self.rect, do zmiany
    def getRect(self):
        return self.rect
    def getId(self):
        return self.id

#wrapperek
class Rectangle():
    def __init__(self, x, y ,width, height) -> None:
        self.rect = pg.rect.Rect(x,y, width, height)
        self.color = (100,100,100)
        self.id = 0
    def setId(self, id):
        self.id = id
    def getId(self):
        return self.id
    def is_movable(self):
        return False
    def is_playable(self):
        return False
    def getRect(self):
        return self.color, self.rect

