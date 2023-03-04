import pygame as pg

class GObject():
    def __init__(self, pos_x, pos_y, size):
        self._width = size
        self._height = size
        self._rect = pg.Rect(pos_x, pos_y, self._width, self._height)
        self._color = (0,0,0)
        self._playable = False
        self._dropable = False
        self._movable = False
        self._solid = False
    
    def getRect(self):
        return self._rect
    def getColor(self):
        return self._color
    def playable(self):
        return self._playable
    def dropable(self):
        return self._dropable
    def movable(self):
        return self._movable
    def solid(self):
        return self._solid

class Mud(GObject):
    def __init__(self, pos_x, pos_y, size):
        super().__init__(pos_x, pos_y, size)
        self._color = (214,122,25)

class Wall(GObject):
    def __init__(self, pos_x, pos_y, size):
        super().__init__(pos_x, pos_y, size)
        self._color = (136,136,136)
        self._solid = True

class Stone(GObject):
    def __init__(self, pos_x, pos_y, size):
        super().__init__(pos_x, pos_y, size)
        self._color = (225,242,240)
        self._dropable = True
        self._solid = True
        self._movable = True

class Diamond(GObject):
    def __init__(self, pos_x, pos_y, size):
        super().__init__(pos_x, pos_y, size)
        self._color = (2,38,244)
        self._dropable = True

class Exit(GObject):
    def __init__(self, pos_x, pos_y, size):
        super().__init__(pos_x, pos_y, size)
        self._color = (255,51,0)
        self._solid = True

class Player(GObject):
    def __init__(self, pos_x, pos_y, size):
        super().__init__(pos_x, pos_y, size)
        self._color = (97,255,0)
        self._playable = True
        
class Text():
    def __init__(self, text, color) -> None:
        self._text = text
        self._color = color
        self._points = 0
        self._font = pg.font.SysFont("Calibri", 48)
        self._wrtx = pg.font.Font.render(self._font, self._text+str(self._points), True, self._color)
    def addPoint(self):
        self._points += 1
        self._wrtx = pg.font.Font.render(self._font, self._text+str(self._points), True, self._color)
        self._wrtx 
    def getPoints(self):
        return self._points
    def getRenderedText(self):
        return self._wrtx
    """
    def drawTextVar(self, text):
        self.text = text
        self.wrtx = pg.font.Font.render(self.font, self.text, True, self.color)
        wn.blit(self.wrtx, (self.pos_x, self.pos_y))
    def getPos(self):
        return self.pos_x, self.pos_y
    """