#!/usr/bin/python3

from game import Game

class Main:
    def __init__(self) -> None:
        self._game = None #Game()

    def run(self):
        self._game = Game()
        self._game.mainLoop()

if __name__ == "__main__":
    main = Main()
    main.run()
