# player_sprite.py in f_santa
"""
Title: Composite Player Sprite
Author: Jason Li
Date-Created: 2024-01-17
"""

import pygame
from box import Box
from Sprites.image_sprite import ImageSprite
from Sprites.basic_sprite import BasicSprite
from window import Window
from random import randrange


class Player(BasicSprite):
    def __init__(self, IMAGE_FILE):
        BasicSprite.__init__(self)
        self.__IMAGE = ImageSprite(IMAGE_FILE, False)
        self.__HIT_BOX = Box(self.__IMAGE.getWidth()//2, self.__IMAGE.getHeight()//2)
        self.__HIT_BOX.setPos(
            self.getX() + self.__IMAGE.getWidth()//2 - self.__HIT_BOX.getWidth()//2,
            self.getY() + self.__IMAGE.getHeight()//2 - self.__HIT_BOX.getWidth()//2
        )
        self._SURFACE = self.__IMAGE.getSurface()

    # --- MODIFIER METHODS --- #
    def ADMove(self, KEY_PRESSES):
        """
        Moves the sprite left and right
        :param KEY_PRESSES: list(int)
        :return: None
        """


if __name__ == "__main__":
    pygame.init()

    WINDOW = Window("Player Sprite Test", COLOR=(3, 10, 12))
    PLAYER = Player()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        PRESSED_KEYS = pygame.key.get_pressed()
        PLAYER.WASDmove(PRESSED_KEYS)

        WINDOW.clearScreen()
        WINDOW.getSurface().blit(PLAYER.getSurface(), PLAYER.getPOS())
        WINDOW.updateFrame()
