# image_sprite.py

"""
Title: Image Sprite Class
Author: Jason Li
Date Created: 2024-01-15
"""
from Sprites.basic_sprite import BasicSprite
import pygame
from window import Window
from random import randrange


class ImageSprite(BasicSprite):
    def __init__(self, IMAGE_FILE, LOOKING_RIGHT=True):
        BasicSprite.__init__(self)
        self.__FILE_NAME = IMAGE_FILE
        self._SURFACE = pygame.image.load(self.__FILE_NAME).convert_alpha()
        self.__LOOKING_RIGHT = LOOKING_RIGHT  # Looking to the left

    def setScale(self, SCALE_X, SCALE_Y=0):
        """
        Adjust the scale of the image
        :param SCALE_X: float
        :param SCALE_Y: float
        :return: None
        """
        if SCALE_Y == 0:
            SCALE_Y = SCALE_X  # Allow both to be transformed at same time
        self._SURFACE = pygame.transform.scale(
            self._SURFACE, (self._SURFACE.get_width()*SCALE_X,
                            self._SURFACE.get_height()*SCALE_Y)
        )

    def WASDmove(self, KEY_PRESSES):
        # Polymorphism to flip the image if necessary
        BasicSprite.WASDmove(self, KEY_PRESSES)
        if KEY_PRESSES[pygame.K_d] == 1 and self.__LOOKING_RIGHT is False:
            self._SURFACE = pygame.transform.flip(self._SURFACE, True, False)
            self.__LOOKING_RIGHT = True
        if KEY_PRESSES[pygame.K_a] == 1 and self.__LOOKING_RIGHT is True:
            self._SURFACE = pygame.transform.flip(self._SURFACE, True, False)
            self.__LOOKING_RIGHT = False


if __name__ == "__main__":
    pygame.init()

    WINDOW = Window("Santa")
    SANTA = ImageSprite("media/santa.png", False)
    SANTA.setScale(0.5)
    GIFT_1 = ImageSprite("media/gift1.png")
    GIFT_1.setScale(0.25)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        PRESSED_KEYS = pygame.key.get_pressed()
        SANTA.WASDmove(PRESSED_KEYS)
        SANTA.wrapX(WINDOW.getWidth())
        SANTA.wrapY(WINDOW.getHeight())

        if GIFT_1.isCollision(SANTA.getSurface(), SANTA.getPOS()):
            GIFT_1.setPos(
                randrange(0, WINDOW.getWidth() - GIFT_1.getSurface().get_width()),
                randrange(0, WINDOW.getHeight() - GIFT_1.getSurface().get_height())
            )

        WINDOW.clearScreen()
        WINDOW.getSurface().blit(SANTA.getSurface(), SANTA.getPOS())
        WINDOW.getSurface().blit(GIFT_1.getSurface(), GIFT_1.getPOS())
        WINDOW.updateFrame()
