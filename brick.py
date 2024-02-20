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

    def setColor(self, COLOR=(0, 0, 0)):
        """
        Color is based on health.
        """
        # Find the color based on health.
        # 1 health means white
        if self.__HEALTH == 1:
            Box.setColor(self, (255, 255, 255))
        else:
            COLOR_HEALTH = min(13, self.__HEALTH)  # Anything over 12 health is the same color
            HUE = 360 * (COLOR_HEALTH - 1) // 12
            # Find color based on HSV (https://www.rapidtables.com/convert/color/hsv-to-rgb.html)
            C_VALUE = 0.5  # Slightly pastel
            X_VALUE = C_VALUE * (1 - abs((HUE / 60) % 2 - 1))
            M_VALUE = 1 - C_VALUE
            RED = 0
            GREEN = 0
            BLUE = 0
            if 0 < HUE <= 60:
                RED = C_VALUE
                GREEN = X_VALUE
            elif 60 < HUE <= 120:
                RED = X_VALUE
                GREEN = C_VALUE
            elif 120 < HUE <= 180:
                GREEN = C_VALUE
                BLUE = X_VALUE
            elif 180 < HUE <= 240:
                GREEN = X_VALUE
                BLUE = C_VALUE
            elif 240 < HUE <= 300:
                BLUE = C_VALUE
                RED = X_VALUE
            else:
                BLUE = X_VALUE
                RED = C_VALUE
            RED = int((RED + M_VALUE) * 255)
            GREEN = int((GREEN + M_VALUE) * 255)
            BLUE = int((BLUE + M_VALUE) * 255)
            Box.setColor(self, (RED, GREEN, BLUE))

    def getHealth(self):
        return self.__HEALTH
