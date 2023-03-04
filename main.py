#!/usr/bin/python3

from game import Game,GameStatus

class Main:
    def __init__(self) -> None:
        self._game = None
        self._welcome_board = None
        self._running = True

    def run(self):
        rc = GameStatus.ESCAPE_HIT
        while self._running == True:
            if rc == GameStatus.PLAYER_DIED and not self._welcome_board == None:
                self._welcome_board.run()
            self._game = Game()
            rc = self._game.mainLoop()
            if rc == GameStatus.GAME_EXIT:
                self._running = False

if __name__ == "__main__":
    main = Main()
    main.run()
