import pygame as pg

class Screen():
    def __init__(self):
        pg.init()
        self._screen_h = 320
        self._screen_w = 320
        self._screen_size = None
        self._window = pg.display.set_mode((self._screen_w, self._screen_h), pg.RESIZABLE)
        self._window.fill((0,0,0)) #set background
    
    def cleanup(self):
        pg.quit()

    def processEvent(self, event):
        if event.type == pg.VIDEORESIZE:
            self._screen_h = event.h
            self._screen_w = event.w
            self._screen_size = event.size
            self._window = pg.display.set_mode(self._screen_size, pg.RESIZABLE)
    
    def drawObject(self, object):
        pg.draw.rect(self._window, object.getColor(), object.getRect())

    def update(self):
        pg.display.update()

