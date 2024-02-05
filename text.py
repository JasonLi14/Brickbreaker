# text.py in e_inheritance

"""
Title: Text Child Class
Author: Jason Li
Date Created: 2023-12-22
"""

from my_sprite import MySprite
import pygame
from window import Window


class Text(MySprite):  # Brackets indicate that it is inheriting
    """
    Subclass of MySprite
    """

    def __init__(self, TEXT, F_FAMILY="Comic Sans", F_SIZE=36):
        MySprite.__init__(self)
        # This allows the Text sprite to init as the parent but we can add stuff to __init__.
        self.__TEXT = TEXT
        self.__FONT_FAMILY = F_FAMILY
        self.__FONT_SIZE = F_SIZE
        self.__FONT = pygame.font.SysFont(self.__FONT_FAMILY, self.__FONT_SIZE)
        self._SURFACE = self.__FONT.render(self.__TEXT, True, self._COLOR)

    def setColor(self, COLOR):
        MySprite.setColor(self, COLOR)
        self._SURFACE = self.__FONT.render(self.__TEXT, True, self._COLOR)


if __name__ == "__main__":
    pygame.init()

    WINDOW = Window("Text subClass")
    TEXT_OBJ = Text("Hello World")
    TEXT_OBJ.setColor((0, 255, 0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        WINDOW.clearScreen()
        WINDOW.getSurface().blit(TEXT_OBJ.getSurface(), TEXT_OBJ.getPOS())
        WINDOW.updateFrame()
