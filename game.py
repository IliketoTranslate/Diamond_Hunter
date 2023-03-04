from screen import Screen
from boardparser import Boardparser
from object import StateText
import pygame as pg

from enum import Enum

class GameStatus(Enum):
    GAME_EXIT = 0
    PLAYER_DIED = 1
    ESCAPE_HIT = 2

class Game():
    def __init__(self) -> None:
        self._screen = Screen()
        self._done = False
        self._return_val = GameStatus.GAME_EXIT
        self._shift = 30
        self._tick = 200 #milliseconds
        self._player = None
        self._chances = 3
        self.resetGame()
    
    def resetGame(self):
        self._objects = []
        self._state = StateText(self._chances, (255,255,255))
        _parser = Boardparser(self._shift, "board.txt")
        for el in _parser.generateObjects():
            self._objects.append(el)
            if el.playable() == True:
                self._player = el
                self._player.setSkin(self._player.standing())
        
    def processEvent(self, event):
        if event.type == pg.QUIT:
            self._done = True
            self._return_val = GameStatus.GAME_EXIT
        elif event.type == pg.KEYDOWN:
            delta_x = 0
            delta_y = 0
            keys = pg.key.get_pressed()
            pg.time.set_timer(pg.KEYDOWN, 200)
            if keys[pg.K_ESCAPE]:
                self._done = True
                self._return_val = GameStatus.ESCAPE_HIT
            if keys[pg.K_LEFT]:
                delta_x = -self._shift
                self._player.setWalking(True)
                self._player.setLeft()
            if keys[pg.K_RIGHT]:
                delta_x = self._shift
                self._player.setWalking(True)
                self._player.setRight()
            if keys[pg.K_UP]:
                delta_y = -self._shift
                self._player.setWalking(True)
            if keys[pg.K_DOWN]:
                delta_y = self._shift
                self._player.setWalking(True)
            if self.movePlayer(delta_x, delta_y) == True:
                #print("Move player by x="+str(delta_x)+" y="+str(delta_y))
                self._player.getRect().move_ip(delta_x, delta_y)
        elif event.type == pg.KEYUP:
            pg.time.set_timer(pg.KEYDOWN, 0)
            self._player.setWalking(False)
        else:
            self._screen.processEvent(event)

    def movePlayer(self, delta_x, delta_y) -> bool:
        updated_rect = self._player.getRect().move(delta_x, delta_y)
        rect_list = [el.getRect() for el in self._objects]
        idx = updated_rect.collidelist(rect_list)
        if idx != -1:
            collided_obj = self._objects[idx]
            if collided_obj.solid():
                if collided_obj.movable():#rock
                    if delta_y == 0:
                        if self.canMoveRock(collided_obj, delta_x):
                            self.moveObject(collided_obj, delta_x, 0)
                            return True
                    else:#moving up/down, don't check rock
                        return False
                else:#wall
                    return False #move not allowed
            else:
                if not collided_obj.dropable() \
                    and not collided_obj.playable():#Mud
                    self._objects.pop(idx)
                    return True
                elif collided_obj.dropable():#Diamond
                    self._objects.pop(idx)
                    self._state.addPoint()
                    return True
        else:#no collision
            return True

    def canMoveRock(self, rock, delta_x):
        searched_rect = rock.getRect().move(delta_x, 0)
        for el in self._objects:
            if searched_rect.contains(el.getRect()):
                return False
        return True


    def moveObject(self, object, delta_x, delta_y):
        object.getRect().move_ip(delta_x, delta_y)

    def moveObjects(self):
        obj_below = None
        for object in self._objects:
            if object.dropable():
                #1. check if there is something to fall
                check_rect = object.getRect().move(0, self._shift)
                for el in self._objects:
                    if check_rect.contains(el.getRect()):
                        obj_below = el
                        if object.inFall(): 
                            if el.playable() == True:#unfortunately we found player
                                self.killPlayer()
                                object.setInFall(False)
                        else:
                            object.setInFall(False)
                        break#something exists below
                #if we get here, there is nothing below, it can drop
                else:
                    self.moveObject(object, 0, self._shift)
                    object.setInFall(True)
                    continue
                if not obj_below == None and obj_below.dropable():
                    #2. check if there is something on right/left bottom
                    check_nextto = object.getRect().move(self._shift, 0)
                    check_below = object.getRect().move(self._shift, self._shift)
                    for el in self._objects:
                        if check_nextto.contains(el.getRect()) or check_below.contains(el.getRect()):
                            break
                    else:
                        self.moveObject(object, self._shift, self._shift)
                        object.setInFall(True)
                    check_nextto = object.getRect().move(-self._shift, 0)
                    check_below = object.getRect().move(-self._shift, self._shift)
                    for el in self._objects:
                        if check_nextto.contains(el.getRect()) or check_below.contains(el.getRect()):
                            break
                    else:
                        self.moveObject(object, -self._shift, self._shift)
                        object.setInFall(True)


    def killPlayer(self):
        if self._chances == 0:
            self._return_val = GameStatus.PLAYER_DIED
            self._done = True
        self._chances -= 1
        self._state.setChances(self._chances)
        self.resetGame()

    def mainLoop(self):
        clock = pg.time.Clock()
        ticks = 0
        while not self._done:
            ticks += clock.tick()
            self._screen.refresh()
            self._screen.blit(self._state)
            for el in self._objects:
                self._screen.blitObject(el)
            self._screen.update()
            for event in pg.event.get():
                self.processEvent(event)
            if ticks > self._tick:
                for el in self._objects:
                    el.changeSkin()
                ticks = 0
                self.moveObjects()
        self._screen.cleanup()
        return self._return_val
