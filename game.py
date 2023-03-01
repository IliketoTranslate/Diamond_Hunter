from screen import Screen
from boardparser import Boardparser
import pygame as pg

class Game():
    def __init__(self) -> None:
        self._screen = Screen()
        self._done = False
        self._shift = 100
        self._objects = list()
        self._player = None
        _parser = Boardparser(self._shift, "board.txt")
        for el in _parser.generateObjects():
            self._objects.append(el)
            if el.playable() == True:
                self._player = el
    
    def processEvent(self, event):
        if event.type == pg.QUIT:
            self._done = True
        elif event.type == pg.KEYDOWN:
            keys = pg.key.get_pressed()
            if keys[pg.K_LEFT]:
                new_y=-1
            if keys[pg.K_RIGHT]:
                new_x = -1
            if keys[pg.K_UP]:
                new_y = 1
            if keys[pg.K_DOWN]:
                new_x = 1
        else:
            self._screen.processEvent(event)

    def mainLoop(self):
        while not self._done:
            for el in self._objects:
                self._screen.drawObject(el)
            self._screen.update()
            for event in pg.event.get():
                #print("Event "+str(event.type))
                self.processEvent(event)
        self._screen.cleanup()
