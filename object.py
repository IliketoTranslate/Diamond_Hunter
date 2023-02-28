import pygame as pg

class GObject():
    def __init__(self, pos_x, pos_y):
        self._width = 100
        self._height = 100
        self._rect = pg.rect.Rect(pos_x, pos_y, self._width, self._height)
        self._color = (0,0,0)
    
    def getRect(self):
        return self._rect
    def getColor(self):
        return self._color
    
    def move(self):
        pass

class Mud(GObject):
    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y)
        self._color = (255,0,0)

class Stone(GObject):
    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y)
        self._color = (0,255,0)
    def move(self):
        pass