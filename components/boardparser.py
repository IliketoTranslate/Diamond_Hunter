import pygame as pg
from .object import *

class Boardparser():
    def __init__(self, shift, file):
        self._objects = list()
        self._file = file
        self.pos_x = 0
        self.pos_y = 48
        self._shift = shift
        self._falling_stone_sd = pg.mixer.Sound("sds/falling_stone.ogg")
        self._falling_diamond_sd = pg.mixer.Sound("sds/falling_diamond.ogg")
        self.parseFile()

    def parseFile(self):
        try: 
            with open(self._file, 'r') as infile:
                for line in infile:
                    for character in line:
                        if character == '#':
                            self._objects.append(Mud(self.pos_x, self.pos_y, self._shift))
                        elif character == 'R':
                            self._objects.append(Stone(self.pos_x, self.pos_y, self._shift, self._falling_stone_sd))
                        elif character == 'W':
                            self._objects.append(Wall(self.pos_x, self.pos_y, self._shift))
                        elif character == 'P':
                            self._objects.append(Player(self.pos_x, self.pos_y, self._shift))
                        elif character == 'D':
                            self._objects.append(Diamond(self.pos_x, self.pos_y, self._shift, self._falling_diamond_sd))
                        elif character == 'E':
                            self._objects.append(Exit(self.pos_x, self.pos_y, self._shift))
                        self.pos_x += self._shift
                    self.pos_x = 0
                    self.pos_y += self._shift
        except FileNotFoundError:
            print("File not found "+self._file)

    def generateObjects(self):
        for el in self._objects:
            yield el


