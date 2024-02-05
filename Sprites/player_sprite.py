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
    def setX(self, X):
        BasicSprite.setX(self, X)
        self.__IMAGE.setX(X)
        self.__HIT_BOX.setX(
            self.getX() + self.__IMAGE.getWidth()//2 - self.__HIT_BOX.getWidth()//2
        )

    def setY(self, Y):
        BasicSprite.setY(self, Y)
        self.__IMAGE.setY(Y)
        self.__HIT_BOX.setY(
            self.getY() + self.__IMAGE.getHeight()//2 - self.__HIT_BOX.getHeight()//2
        )

    def setPos(self, X, Y):
        BasicSprite.setPos(self, X, Y)
        self.setX(X)
        self.setY(Y)

    def setScale(self, SCALE_X, SCALE_Y=0):
        self.__IMAGE.setScale(SCALE_X, SCALE_Y)
        self.__HIT_BOX = Box(
            self.__IMAGE.getWidth()//2, self.__IMAGE.getHeight()//2
        )
        self._SURFACE = self.__IMAGE.getSurface()
        self.setPos(self.getX(), self.getY())

    def WASDmove(self, KEY_PRESSES):
        BasicSprite.WASDmove(self, KEY_PRESSES)
        self.__IMAGE.WASDmove(KEY_PRESSES)
        self.setPos(self.getX(), self.getY())

    # --- ACCESSOR METHODS --- #
    def getSurface(self):
        return self.__IMAGE.getSurface()

    def getHitBox(self):
        return self.__HIT_BOX.getSurface()

    def getHitBoxPOS(self):
        return self.__HIT_BOX.getPOS()

    def isCollision(self, SURFACE, POS):
        return self.__HIT_BOX.isCollision(SURFACE, POS)


if __name__ == "__main__":
    pygame.init()

    WINDOW = Window("Composite Sprites", COLOR=(3, 10, 12))
    PLAYER = Player("media/santa.png")
    PLAYER.setScale(0.25)
    GIFT_1 = Player("media/gift1.png")
    GIFT_1.setPos(
        randrange(0, WINDOW.getWidth() - GIFT_1.getSurface().get_width()),
        randrange(0, WINDOW.getHeight() - GIFT_1.getSurface().get_height())
    )
    GIFT_1.setScale(0.25)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        PRESSED_KEYS = pygame.key.get_pressed()
        PLAYER.WASDmove(PRESSED_KEYS)

        if PLAYER.isCollision(GIFT_1.getHitBox(), GIFT_1.getHitBoxPOS()):
            GIFT_1.WASDmove(PRESSED_KEYS)

        WINDOW.clearScreen()
        WINDOW.getSurface().blit(PLAYER.getSurface(), PLAYER.getPOS())
        # WINDOW.getSurface().blit(PLAYER.getHitBox(), PLAYER.getHitBoxPOS())
        # Hit Boxes still exist
        WINDOW.getSurface().blit(GIFT_1.getSurface(), GIFT_1.getPOS())
        # WINDOW.getSurface().blit(GIFT_1.getHitBox(), GIFT_1.getHitBoxPOS())
        WINDOW.updateFrame()
