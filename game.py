from screen import Screen
from boardparser import Boardparser
import pygame as pg

class Game():
    def __init__(self) -> None:
        self._screen = Screen()
        self._done = False
        self._objects = list()
        _parser = Boardparser()
        for el in _parser.generateObjects():
            self._objects.append(el)
    
    def processEvent(self, event):
        if event.type == pg.QUIT:
            self._done = True
        self._screen.processEvent(event)

    def mainLoop(self):
        while not self._done:
            for el in self._objects:
                self._screen.drawObject(el)
            self._screen.update()
            for event in pg.event.get():
                self.processEvent(event)
        self._screen.cleanup()
