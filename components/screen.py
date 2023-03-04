import pygame as pg

class Screen():
    def __init__(self):
        pg.init()
        self._screen_h = 708
        self._screen_w = 1200
        self._screen_size = None
        self._window = pg.display.set_mode((self._screen_w, self._screen_h), pg.RESIZABLE)
        self._window.fill((0,0,0)) #set background
        self._suppress_resize = False
    
    def cleanup(self):
        pg.quit()

    def processEvent(self, event):
        if event.type == pg.WINDOWTAKEFOCUS:
            self._suppress_resize = True
        if event.type == 772:
            self._suppress_resize = False
        if event.type == pg.VIDEORESIZE:
            self._screen_h = event.h
            self._screen_w = event.w
            self._screen_size = event.size
            if self._suppress_resize == False:
                self._window = pg.display.set_mode(self._screen_size, pg.RESIZABLE)
                self.update()
    
    def drawObject(self, object):
        pg.draw.rect(self._window, object.getColor(), object.getRect())

    def refresh(self):
        self._window.fill((0,0,0)) #set background
    def blit(self, text):
        self._window.blit(text.getRenderedText(), (0,0))
    def blitObject(self, object):
        self._window.blit(object.getSkin(), object.getRect())

    def update(self):
        pg.display.update()

