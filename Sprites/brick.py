# brick.py

"""
Title: Brick
Author: Jason Li
Date Created: 2024-02-07
"""
from Sprites.box import Box


class Brick(Box):  # Inheritance from Box Sprite
    def __init__(self, WIDTH, HEIGHT, HEALTH=1):
        Box.__init__(self, WIDTH, HEIGHT)
        self.__HEALTH = HEALTH  # Encapsulating the health parameter

    def reduceHealth(self):
        self.__HEALTH -= 1

    def getHealth(self):
        return self.__HEALTH
