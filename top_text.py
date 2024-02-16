# top_text.py

"""
Title: Top Text
Author: Jason Li
Date-Created: 2024-02-15
"""

from Sprites.text import Text
from Sprites.box import Box


class TopText(Box):
    def __init__(self, NAME, WIDTH, HEIGHT=50):
        Box.__init__(self, WIDTH, HEIGHT)  # Self is the container
        self.setColor((0, 0, 0))  # Create color for container
        self.setPos(0, 0)  # Set position at very top
        self.__NAME = "Brick-Breaker " + NAME

        self.__TITLE = Text(self.__NAME, 30)  # Composition of multiple text
        self.__TITLE.setWidth(WIDTH//2)  # Half size
        self.__TITLE.setX(WIDTH//2 - self.__TITLE.getWidth()//2)  # Centralize

        self.__SCORE = Text("Score: ", 30)

        self.__LIVES = Text("Lives: ", 30)
        self.__LIVES.setX(WIDTH - self.__LIVES.getWidth() - 30)

    def blitOnWindow(self, WINDOW):
        """
        Puts top text on to the WINDOW
        :param WINDOW: Window
        :return: None
        """
        WINDOW.getSurface().blit(self.getSurface(), self.getPOS())  # Container
        WINDOW.getSurface().blit(self.__SCORE.getSurface(), self.__SCORE.getPOS())  # Score
        WINDOW.getSurface().blit(self.__TITLE.getSurface(), self.__TITLE.getPOS())  # Title
        WINDOW.getSurface().blit(self.__LIVES.getSurface(), self.__LIVES.getPOS())  # Lives
