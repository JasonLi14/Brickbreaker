# level.py
"""
Name: Level Class
Author: Jason Li
Date-Created: 2024-02-05
"""

from brick import Brick
from window import Window
import pygame


class Level:  # This is an aggregate object because it combines box classes
    """
    Level class ==> one class for each level
    """
    def __init__(self, BRICKS_AMT_X, BRICKS_AMT_Y, LIVES=3):
        self.__BRICKS_AMT_X = BRICKS_AMT_X
        self.__BRICKS_AMT_Y = BRICKS_AMT_Y
        self.__BRICKS = []
        self.__LIVES = LIVES

        # Create the bricks

    def setup(self, MAX_X, MAX_Y, MIN_X=0, MIN_Y=0, PADDING_X=5, PADDING_Y=5):
        """
        Creates bricks and sets them up.
        :param MAX_X: int
        :param MAX_Y: int
        :param MIN_X: int
        :param MIN_Y: int
        :param PADDING_X: int
        :param PADDING_Y: int
        :return: None
        """

        # Find the desired width and height
        BRICK_WIDTH = (MAX_X - MIN_X) // self.__BRICKS_AMT_X - PADDING_X
        BRICK_HEIGHT = (MAX_Y - MIN_Y) // self.__BRICKS_AMT_Y - PADDING_Y
        # Create a list of bricks
        for i in range(self.__BRICKS_AMT_Y):
            for j in range(self.__BRICKS_AMT_X):
                NEW_BRICK = Brick(BRICK_WIDTH, BRICK_HEIGHT)  # Composition
                # Set their positions and stagger them
                NEW_BRICK.setY((BRICK_HEIGHT + PADDING_Y) * i + MIN_Y)  # General Position
                if i % 2 == 0:  # Displaces every other row by half the brick's width
                    NEW_BRICK.setX((BRICK_WIDTH + PADDING_X) * j + MIN_X + BRICK_WIDTH//4)
                else:  # Ensures close to center
                    NEW_BRICK.setX((BRICK_WIDTH + PADDING_X) * j + MIN_X - BRICK_WIDTH//4)
                self.__BRICKS.append(NEW_BRICK)

    def play(self):
        pass

    def death(self, VICTORY):
        pass

    def victory(self):
        pass

    def loss(self):
        pass

    def getBricks(self):
        return self.__BRICKS


if __name__ == "__main__":  # just a test
    pygame.init()
    WINDOW = Window("Test level")
    LEVEL_1 = Level(10, 5, 3)
    LEVEL_1.setup(WINDOW.getWidth() - 100, 300, 100, 100, 3, 20)
    BRICKS = LEVEL_1.getBricks()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        PRESSED_KEYS = pygame.key.get_pressed()

        WINDOW.clearScreen()

        for BRICK in BRICKS:
            WINDOW.getSurface().blit(BRICK.getSurface(), BRICK.getPOS())
        WINDOW.updateFrame()
