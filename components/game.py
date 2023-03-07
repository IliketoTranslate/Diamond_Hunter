from .screen import Screen
from .boardparser import Boardparser
from .object import StateText,Exit,Statement
import pygame as pg

from enum import Enum

class GameStatus(Enum):
    NONE = 0
    GAME_INIT = 1
    GAME_EXIT = 2
    NEXT_LEVEL = 3
    PLAYER_KILLED = 4
    GAME_ENDED = 5

class Game():
    def __init__(self, screen, fps) -> None:
        self._screen = screen
        self._done = False
        self._game_status = GameStatus.GAME_INIT
        self._shift = 30
        self._tick = 200 #milliseconds
        self._player = None
        self._chances = 3
        self._show_fps = fps
        self._diamonds = 15
        self._time_left = 150
        self._SECOND = pg.USEREVENT+1
        self._statement = None
        self._level = 1
        self.resetGame()
        self._breaking_dirt_sd = pg.mixer.Sound("sds/breaking_dirt.ogg")
        self._collecting_diamond_sd = pg.mixer.Sound("sds/collecting_diamond.ogg")
        self._player_death_sd = pg.mixer.Sound("sds/player_death.ogg")
        self.backgorund_music = pg.mixer.Sound("sds/background_music.ogg")
    
    def resetGame(self):
        self._objects = []
        self._state = StateText(self._show_fps, self._chances, (255,255,255))
        filename = "boards/board"+str(self._level)+".txt"
        _parser = Boardparser(self._shift, filename)
        for el in _parser.generateObjects():
            self._objects.append(el)
            if el.playable() == True:
                self._player = el
                self._player.setSkin(self._player.standing())
        if len(self._objects) == 0:#no board loaded
            self._game_status = GameStatus.GAME_ENDED
            return
        self._time_left = 150
        pg.time.set_timer(self._SECOND, 1000)
        
    def processEvent(self, event):
        if event.type == pg.QUIT:
            self._done = True
            self._game_status = GameStatus.GAME_EXIT
            return
        elif event.type == self._SECOND:
            if self._time_left == 0:
                self.killPlayer()
            self._state.setTimeLeft(self._time_left)
            self._state.updateText()
            self._time_left -= 1
            return
        elif event.type == pg.KEYDOWN:
            delta_x = 0
            delta_y = 0
            keys = pg.key.get_pressed()
            pg.time.set_timer(pg.KEYDOWN, 200)
            if keys[pg.K_ESCAPE]:
                self._done = True
                self._game_status = GameStatus.GAME_INIT
                return
            if keys[pg.K_SPACE]:
                if self._game_status == GameStatus.PLAYER_KILLED:
                    self._statement = None
                    if self._chances == 0:
                        self._game_status = GameStatus.GAME_INIT
                        self._done = True
                        return
                    else:
                        self._game_status = GameStatus.GAME_INIT
                        self.resetGame()
                        return
                elif self._game_status == GameStatus.NEXT_LEVEL:
                    self._statement = None
                    self._game_status = GameStatus.NONE
                    self._level += 1
                    self.resetGame()
                    return
                elif self._game_status == GameStatus.GAME_ENDED:
                    self._statement = None
                    self._done = True
                    return
            if self._game_status == GameStatus.PLAYER_KILLED \
                or self._game_status == GameStatus.GAME_ENDED:
                return
            if keys[pg.K_LEFT]:
                delta_x = -self._shift
                self._player.setWalking(True)
                self._player.setLeft()
            elif keys[pg.K_RIGHT]:
                delta_x = self._shift
                self._player.setWalking(True)
                self._player.setRight()
            elif keys[pg.K_UP]:
                delta_y = -self._shift
                self._player.setWalking(True)
            elif keys[pg.K_DOWN]:
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
        if delta_x == 0 and delta_y == 0:
            return False
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
                if isinstance(collided_obj, Exit):#open doors, end level
                    self._game_status = GameStatus.NEXT_LEVEL
                    pg.time.set_timer(self._SECOND, 0)
                    return True
                if not collided_obj.dropable() \
                    and not collided_obj.playable():#Mud
                    self._objects.pop(idx)
                    pg.mixer.Sound.play(self._breaking_dirt_sd)
                    return True
                elif collided_obj.dropable():#Diamond
                    self._objects.pop(idx)
                    self._state.addPoint()
                    pg.mixer.Sound.play(self._collecting_diamond_sd)
                    if self._state.getPoints() == self._diamonds:
                        self.openDoors()
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
                        if object.inFall() == True: 
                            if el.playable() == True:#unfortunately we found player
                                self.killPlayer()
                                object.setInFall(False)
                                return
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
        self._chances -= 1
        self._game_status = GameStatus.PLAYER_KILLED
        pg.time.set_timer(self._SECOND, 0)
        pg.mixer.Sound.play(self._player_death_sd)

    def openDoors(self):
        for object in self._objects:
            if isinstance(object, Exit):
                object.openDoors()
                break

    def mainLoop(self):
        pg.mixer.Sound.play(self.backgorund_music)
        clock = pg.time.Clock()
        ticks = 0
        while not self._done:
            ticks += clock.tick()
            self._screen.refresh()
            self._screen.blitObject(self._state)
            for el in self._objects:
                self._screen.blitObject(el)
            if not self._statement == None:
                self._screen.blitObject(self._statement)
            self._screen.update()
            for event in pg.event.get():
                self.processEvent(event)
            if ticks > self._tick:
                for el in self._objects:
                    el.changeSkin()
                ticks = 0
                self.moveObjects()
                if self._show_fps:
                    self._state.setFps(clock.get_fps())
                    self._state.updateText()
            if self._game_status == GameStatus.NEXT_LEVEL:
                self._statement = Statement("Success")
            if self._game_status == GameStatus.PLAYER_KILLED:
                self._statement = Statement("You have failed")
            if self._game_status == GameStatus.GAME_ENDED:
                self._statement = Statement("Game Over")
        return self._game_status
