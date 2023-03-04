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
        self._skins = list()
        self._skin_idx = 0
        #this will be deleted after work complete
        self._skin = None
        self._toblit = False
    
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
    def toBlit(self):
        return self._toblit
    def addSkin(self, file):
        tmp = pg.image.load(file)
        tmp = pg.transform.scale(tmp, (30, 30))
        self._skins.append(tmp)
    def setSkin(self, skin):
        self._skin = skin
    def getSkin(self):
        return self._skins[self._skin_idx]
    def changeSkin(self):
        self._skin_idx = (self._skin_idx+1)%len(self._skins)

class Mud(GObject):
    def __init__(self, pos_x, pos_y, size):
        super().__init__(pos_x, pos_y, size)
        self._color = (214,122,25)
        self.addSkin("mud.png")
        self._toblit = True

class Wall(GObject):
    def __init__(self, pos_x, pos_y, size):
        super().__init__(pos_x, pos_y, size)
        self._color = (136,136,136)
        self._solid = True
        self.addSkin("wall.png")
        self._toblit = True

class Stone(GObject):
    def __init__(self, pos_x, pos_y, size):
        super().__init__(pos_x, pos_y, size)
        self._color = (225,242,240)
        self.addSkin("stone.png")
        self._toblit = True
        self._dropable = True
        self._solid = True
        self._movable = True

class Diamond(GObject):
    def __init__(self, pos_x, pos_y, size):
        super().__init__(pos_x, pos_y, size)
        self._color = (2,38,244)
        self.addSkin("diamond.png")
        self.addSkin("diamond1.png")
        self.addSkin("diamond2.png")
        self.addSkin("diamond3.png")
        self._dropable = True
        self._toblit = True

class Exit(GObject):
    def __init__(self, pos_x, pos_y, size):
        super().__init__(pos_x, pos_y, size)
        self.addSkin("doors.png")
        self._open_doors = pg.image.load("doors2.png")
        self._open_doors = pg.transform.scale(self._open_doors, (30, 30))
        self._open = False
        self._color = (255,51,0)
        self._solid = True
        self._toblit = True
    def openDoors(self):
        self._open = True
    def getSkin(self):
        if self._open == True:
            return self._open_doors
        else:
            return self._skins[0]

class Player(GObject):
    def __init__(self, pos_x, pos_y, size):
        super().__init__(pos_x, pos_y, size)
        self._color = (97,255,0)
        self._playable = True
        self._standing = pg.image.load("player.png")
        self._standing = pg.transform.scale(self._standing, (30, 30))
        self.addSkin("player_move.png")
        self._toblit = True
        self._walking = False
        self._left = False
    def standing(self):
        return self._standing
    def setWalking(self, isWalking):
        self._walking = isWalking
    def walking(self):
        return self._walking
    def getSkin(self):
        if self._walking == True:
            disp_skin = self._skins[self._skin_idx]
            if self._left == True:
                disp_skin = pg.transform.flip(disp_skin, True, False)
            return disp_skin
        else:
            return self._standing
    def setLeft(self):
        self._left = True
    def setRight(self):
        self._left = False
        
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