#!/usr/bin/python3

from components.screen import Screen
from components.game import Game,GameStatus
from components.welcome import Welcome

class Main:
    def __init__(self) -> None:
        self._screen = Screen()
        self._game = None
        self._welcome_board = Welcome(self._screen)
        self._running = True

    def run(self):
        rc = GameStatus.GAME_INIT
        while self._running == True:
            if rc == GameStatus.GAME_INIT:
                rc = self._welcome_board.run()
                if not rc == GameStatus.GAME_INIT:
                    break#exit
            self._game = Game(self._screen)
            rc = self._game.mainLoop()
            if rc == GameStatus.GAME_EXIT:
                self._running = False
            elif rc == GameStatus.PLAYER_DIED:
                rc = GameStatus.GAME_INIT
        self._screen.cleanup()

if __name__ == "__main__":
    main = Main()
    main.run()
