import pygame as pg

class GObject():
    def __init__(self, pos_x, pos_y):
        self._width = 100
        self._height = 100
        self._rect = pg.rect.Rect(pos_x, pos_y, self._width, self._height)
        self._color = (0,0,0)
        self._playable = False
        self._droppable = False
    
    def getRect(self):
        return self._rect
    def getColor(self):
        return self._color
    def playable(self):
        return self._playable
    def dropable(self):
        return self._droppable

class Mud(GObject):
    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y)
        self._color = (214,122,25)

class Stone(GObject):
    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y)
        self._color = (225,242,240)
        self._droppable = True

class Diamond(GObject):
    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y)
        self._color = (225,242,240)
        self._droppable = True

class Player(GObject):
    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y)
        self._color = (97,255,0)
        self._playable = True