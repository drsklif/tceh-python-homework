# -*- coding: utf-8 -*-

"""
Main file. Contains program execution logic.
"""

from game import Game

__author__ = 'aildyakov'

def main():
    """
    Main method, works infinitelly until game ends.
    Or hits `Ctrl+C` in the console.
    """

    try:
    	game = Game()
    	game.start()
    except KeyboardInterrupt:
        print('\nИгра завершена! До скорых встреч!')


if __name__ == '__main__':
    main()
