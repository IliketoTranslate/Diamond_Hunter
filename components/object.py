import pygame as pg

class GObject():
    def __init__(self, pos_x, pos_y, size):
        self._width = size
        self._height = size
        self._rect = pg.Rect(pos_x, pos_y, self._width, self._height)
        self._color = (0,0,0)
        self._playable = False
        self._dropable = False
        self._inFall = False
        self._movable = False
        self._solid = False
        self._skins = list()
        self._skin_idx = 0
        #this will be deleted after work complete
    
    def getRect(self):
        return self._rect
    def getColor(self):
        return self._color
    def playable(self):
        return self._playable
    def dropable(self):
        return self._dropable
    def inFall(self):
        return self._inFall
    def setInFall(self, val):
        self._inFall = val
    def movable(self):
        return self._movable
    def solid(self):
        return self._solid
    def addSkin(self, file):
        tmp = pg.image.load(file)
        tmp = pg.transform.scale(tmp, (30, 30))
        self._skins.append(tmp)
    def setSkin(self, skin):
        self._skin = skin
    def getSurface(self):
        return self._skins[self._skin_idx]
    def changeSkin(self):
        self._skin_idx = (self._skin_idx+1)%len(self._skins)

class Mud(GObject):
    def __init__(self, pos_x, pos_y, size):
        super().__init__(pos_x, pos_y, size)
        self._color = (214,122,25)
        self.addSkin("pic/mud.png")

class Wall(GObject):
    def __init__(self, pos_x, pos_y, size):
        super().__init__(pos_x, pos_y, size)
        self._color = (136,136,136)
        self._solid = True
        self.addSkin("pic/wall.png")

class Stone(GObject):
    def __init__(self, pos_x, pos_y, size, sound):
        super().__init__(pos_x, pos_y, size)
        self._color = (225,242,240)
        self.addSkin("pic/stone.png")
        self._dropable = True
        self._solid = True
        self._movable = True
        self._falling_stone_sd = sound
    def setInFall(self, val):
        self._inFall = val
        if val == False:
             pg.mixer.Sound.play(self._falling_stone_sd)
                

class Diamond(GObject):
    def __init__(self, pos_x, pos_y, size, sound):
        super().__init__(pos_x, pos_y, size)
        self._color = (2,38,244)
        self.addSkin("pic/diamond.png")
        self.addSkin("pic/diamond1.png")
        self.addSkin("pic/diamond2.png")
        self.addSkin("pic/diamond3.png")
        self._dropable = True
        self._falling_diamond_sd = sound
    def setInFall(self, val):
        self._inFall = val
        if val == False:
            pg.mixer.Sound.play(self._falling_diamond_sd)

class Exit(GObject):
    def __init__(self, pos_x, pos_y, size):
        super().__init__(pos_x, pos_y, size)
        self.addSkin("pic/doors.png")
        self._open_doors = pg.image.load("pic/doors2.png")
        self._open_doors = pg.transform.scale(self._open_doors, (30, 30))
        self._open = False
        self._color = (255,51,0)
        self._solid = True
        self._opening_door_sd = pg.mixer.Sound("sds/opening_door.ogg")
    def openDoors(self):
        self._open = True
        self._solid = False
        pg.mixer.Sound.play(self._opening_door_sd)
    def getSurface(self):
        if self._open == True:
            return self._open_doors
        else:
            return self._skins[0]

class Player(GObject):
    def __init__(self, pos_x, pos_y, size):
        super().__init__(pos_x, pos_y, size)
        self._color = (97,255,0)
        self._playable = True
        self._standing = pg.image.load("pic/player.png")
        self._standing = pg.transform.scale(self._standing, (30, 30))
        self.addSkin("pic/player_move.png")
        self._walking = False
        self._left = False
    def standing(self):
        return self._standing
    def setWalking(self, isWalking):
        self._walking = isWalking
    def walking(self):
        return self._walking
    def getSurface(self):
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
        
class StateText():
    def __init__(self, fps, chances, color) -> None:
        self._color = color
        self._points = 0
        self._chances = chances
        self._time_left = 0
        self._show_fps = fps
        self._fps_rate = 0.0
        self._font = pg.font.SysFont("Calibri", 48)
        self.updateText()
    def setFps(self, fps):
        self._fps_rate = round(fps, 2)
    def setTimeLeft(self, timeleft):
        self._time_left = timeleft
    def addPoint(self):
        self._points += 1
        self.updateText()
    def getPoints(self):
        return self._points
    def setChances(self, chances):
        self._chances = chances
        self.updateText()
    def updateText(self):
        disp_string = "Chances left: "+str(self._chances)+ \
            " Diamonds: "+str(self._points)+\
            " Time left: "+str(self._time_left)
        if self._show_fps:
            disp_string += " Fps: "+str(self._fps_rate)
        self._surface = pg.font.Font.render(self._font, disp_string, True, self._color)
    def getRect(self):
        return (0,0)

    def getSurface(self):
        return self._surface
    
class Statement():
    def __init__(self, text):
        self._text = text
        self._font = pg.font.SysFont("Calibri", 35)
        self.size_w = 400
        self.size_h = 200
        self.reset()

    def reset(self):
        self._surface = pg.Surface((self.size_w, self.size_h))
        self._surface.fill((0,0,0))
        self._surface.set_alpha(200)
        _tmp_txt = pg.font.Font.render(self._font, self._text, True, (255,255,255))
        _tmp_rect = _tmp_txt.get_rect(center=(self.size_w/2, self.size_h/4))
        self._surface.blit(_tmp_txt, _tmp_rect)
        _tmp_txt = pg.font.Font.render(self._font, "Press SPACE to continue", True, (255,255,255))
        _tmp_rect = _tmp_txt.get_rect(center=(self.size_w/2, 3*self.size_h/4))
        self._surface.blit(_tmp_txt, _tmp_rect)
    def setText(self, text):
        self._text = text
        self.reset()
    def getRect(self):
        return (400,254)
    def getSurface(self):
        return self._surface
    
