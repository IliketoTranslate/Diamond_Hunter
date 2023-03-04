import pygame as pg
from .screen import Screen
from .game import GameStatus

class Greet():
    def __init__(self, pos_x, pos_y, size_w, size_h):
        self._width = size_w
        self._height = size_h
        self._rect = pg.Rect(pos_x, pos_y, self._width, self._height)
        self._pic = pg.transform.scale(pg.image.load("pic/welcome.png"), (size_w, size_h))
        
    def getRect(self):
        return self._rect
    def getSkin(self):
        return self._pic

class Welcome():
    def __init__(self, screen):
        self._screen = screen
        self._greet = Greet(0, 0, 1200, 708)
        self._shutter = pg.Surface((1200, 708))
        self._shutter.set_alpha(256)
        self._shutter.fill((255,255,255))
    def run(self):
        running = True
        rc = GameStatus.NONE
        i=255
        while running:
            self._screen.refresh()
            self._screen.blitObject(self._greet)
            if i > 0:
                self._screen.blit(self._shutter)
                self._shutter.set_alpha(i)
                i-=1
            self._screen.update()
            for event in pg.event.get():
                rc = self.processEvent(event)
                if not rc == GameStatus.NONE:
                    running = False
                    break
        while i < 256:
            self._screen.refresh()
            self._shutter.set_alpha(i)
            self._screen.blitObject(self._greet)
            self._screen.blit(self._shutter)
            i+=1
            self._screen.update()
        return rc

    def processEvent(self, event) -> GameStatus:
        if event.type == pg.KEYDOWN:
            keys = pg.key.get_pressed()
            if keys[pg.K_SPACE]:
                return GameStatus.GAME_INIT
            elif keys[pg.K_ESCAPE]:
                return GameStatus.GAME_EXIT
        return GameStatus.NONE
