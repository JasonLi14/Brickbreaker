# box.py in e_inheritance

"""
Title: Box Sub Class
Author: Jason Li
Date Created: 2023-12-22
"""

from my_sprite import MySprite
from window import Window
import pygame


class Box(MySprite):

    def __init__(self, WIDTH=1, HEIGHT=1):
        MySprite.__init__(self, WIDTH, HEIGHT)
        self._SURFACE = pygame.Surface(self._DIMENSIONS, pygame.SRCALPHA, 32)
        self._SURFACE.fill(self._COLOR)

    def setColor(self, COLOR):  # We have modified a method ==> polymorphism
        MySprite.setColor(self, COLOR)
        self._SURFACE.fill(self._COLOR)

    def setDimensions(self, WIDTH, HEIGHT):
        MySprite.setDimensions(self, WIDTH, HEIGHT)
        self._SURFACE = pygame.transform.scale(
            self._SURFACE, (self.getWidth(),
                            self.getHeight()))


if __name__ == "__main__":
    pygame.init()

    WINDOW = Window("Boxes Subclass")
    RED_BOX = Box(100, 100)
    RED_BOX.setColor((255, 0, 0))

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        WINDOW.clearScreen()
        WINDOW.getSurface().blit(RED_BOX.getSurface(), RED_BOX.getPOS())
        WINDOW.updateFrame()
