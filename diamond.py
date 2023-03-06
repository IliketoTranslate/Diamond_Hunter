#!/usr/bin/python3

import argparse
from components.screen import Screen           
from components.game import Game,GameStatus
from components.welcome import Welcome

class Main:
    def __init__(self, fps) -> None:
        self._screen = Screen()
        self._game = None
        self._welcome_board = Welcome(self._screen)
        self._running = True
        self._show_fps = fps

    def run(self):
        rc = GameStatus.GAME_INIT
        while self._running == True:
            if rc == GameStatus.GAME_INIT:
                rc = self._welcome_board.run()
                if not rc == GameStatus.GAME_INIT:
                    break#exit
            self._game = Game(self._screen, self._show_fps)
            rc = self._game.mainLoop()
            if rc == GameStatus.GAME_EXIT:
                self._running = False
            elif rc == GameStatus.GAME_ENDED:
                self._game = Game(self._screen, self._show_fps)
                rc = GameStatus.GAME_INIT
        self._screen.cleanup()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Diamond Hunter")
    parser.add_argument('-fps', action='store_true', help='Show frame rate')
    args=parser.parse_args()
    main = Main(args.fps)
    main.run()
