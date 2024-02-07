# window.py

"""
Title: Pygame Template File
Author: Jason Li
Date Created: 2023-12-18
"""

import pygame


class Window:
    """
    Creates the window that will load the game.
    """

    def __init__(self, TITLE, WIDTH=800, HEIGHT=600, FPS=30, COLOR=(0, 0, 0)):
        self.__TITLE = TITLE
        self.__FPS = FPS
        self.__WIDTH = WIDTH
        self.__HEIGHT = HEIGHT
        self.__COLOR = COLOR
        self.__SCREEN_DIM = (self.__WIDTH, self.__HEIGHT)
        self.__CLOCK = pygame.time.Clock()
        self.__SURFACE = pygame.display.set_mode(self.__SCREEN_DIM)
        self.__SURFACE.fill(self.__COLOR)
        pygame.display.set_caption(self.__TITLE)

    def updateFrame(self):
        self.__CLOCK.tick(self.__FPS)
        pygame.display.flip()

    def clearScreen(self):
        # Fills screen again. This does not affect memory too much because pygame has
        # garbage collection
        self.__SURFACE.fill(self.__COLOR)

    def getSurface(self):
        return self.__SURFACE

    def getWidth(self):
        return self.__WIDTH

    def getHeight(self):
        return self.__HEIGHT


class Text:
    """
    Creates a text object to put on the screen.
    """

    def __init__(self, TEXT_CONTENT):
        self.__TEXT = pygame.font.SysFont("Comic Sans", 80)
        self.__SURFACE = self.__TEXT.render(TEXT_CONTENT, 1, (255, 240, 230))

    def getSurface(self):
        return self.__SURFACE


if __name__ == "__main__":
    pygame.init()

    WINDOW = Window("A Template", 800, 600, 30)
    TEXT = Text("Hello World")

    while True:

        # Teaches pygame to exit when you click on the red "X"
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        WINDOW.getSurface().blit(TEXT.getSurface(), (0, 0))
        WINDOW.updateFrame()
