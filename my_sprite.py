# my_sprite.py in e_inheritance

"""
Title: The Parent Class
Author: Jason Li
Date Created: 2023-12-22
"""
import pygame


class MySprite:

    """
    Abstract sprite class for pygame sprites.
    It is an abstract class because it does not do anything.
    It requires children to do it.
    """

    def __init__(self, WIDTH=1, HEIGHT=1, X=0, Y=0, SPEED=5, COLOR=(255, 255, 255)):
        self.__WIDTH = WIDTH  # Private Attributes
        self.__HEIGHT = HEIGHT
        self.__X = X
        self.__Y = Y
        self._DIMENSIONS = (self.__WIDTH, self.__HEIGHT)
        self.__POS = (self.__X, self.__Y)
        self.__SPEED = SPEED
        self._COLOR = COLOR  # Partially Protected Attributes
        self._SURFACE = pygame.Surface
        """
        When there is only one underscore, 
        the child classes can use 
        the same attribute.
        """
        self.__DIR_X = 1
        self.__DIR_Y = 1

    # --- MODIFIER METHODS --- #
    def WASDmove(self, KEY_PRESSES):
        """
        Moves the box based on WASD
        :param KEY_PRESSES: list[int]
        :return: None
        """
        if KEY_PRESSES[pygame.K_d]:
            self.__X = self.__X + self.__SPEED
        if KEY_PRESSES[pygame.K_a]:
            self.__X = self.__X - self.__SPEED
        if KEY_PRESSES[pygame.K_w]:
            self.__Y = self.__Y - self.__SPEED
        if KEY_PRESSES[pygame.K_s]:
            self.__Y = self.__Y + self.__SPEED

    def setX(self, X):  # Public Methods
        self.__X = X
        self.__POS = (self.__X, self.__Y)

    def setY(self, Y):
        self.__Y = Y
        self.__POS = (self.__X, self.__Y)

    def marqueeX(self):
        self.__X = self.__X + self.__SPEED * self.__DIR_X
        self.__POS = (self.__X, self.__Y)

    def marqueeY(self):
        self.__Y = self.__Y + self.__SPEED * self.__DIR_Y

    def wrapX(self, MAX_X, MIN_X=0):
        """
        When the object goes out, it goes back the other side
        :param MAX_X: int
        :param MIN_X: int
        :return: None
        """
        if self.__X < MIN_X - self.__WIDTH:
            self.__X = MAX_X
        elif self.__X > MAX_X:
            self.__X = MIN_X - self.__WIDTH
        self.__POS = (self.__X, self.__Y)

    def wrapY(self, MAX_Y, MIN_Y=0):
        """
        When the object goes out, it goes back the other side
        :param MIN_Y: int
        :param MAX_Y: int
        :return: None
        """
        if self.__Y < MIN_Y - self.__WIDTH:
            self.__Y = MAX_Y
        elif self.__Y > MAX_Y:
            self.__Y = MIN_Y - self.__HEIGHT
        self.__POS = (self.__X, self.__Y)

    def bounceX(self, MAX_X, MIN_X=0):
        self.__X = self.__X + self.__SPEED * self.__DIR_X
        if self.__X > MAX_X - self.__WIDTH:
            self.__DIR_X = -1
        if self.__X < MIN_X:
            self.__DIR_X = 1

        self.__POS = (self.__X, self.__Y)

    def bounceY(self, MAX_Y, MIN_Y=0):
        self.__Y = self.__Y + self.__SPEED * self.__DIR_Y
        if self.__Y > MAX_Y - self.__HEIGHT:
            self.__DIR_Y = -1
        if self.__Y < MIN_Y:
            self.__DIR_Y = 1

        self.__POS = (self.__X, self.__Y)

    def setPos(self, X, Y):
        self.setX(X)
        self.setY(Y)

    def setColor(self, COLOR):
        self._COLOR = COLOR

    def setDimensions(self, WIDTH, HEIGHT):
        self._DIMENSIONS = (WIDTH, HEIGHT)

    def setWidth(self, WIDTH):
        self.__WIDTH = WIDTH
        self.setDimensions(self.__WIDTH, self.__HEIGHT)

    def setHeight(self, HEIGHT):
        self.__HEIGHT = HEIGHT
        self.setDimensions(self.__WIDTH, self.__HEIGHT)

    # --- ACCESSOR METHODS --- #
    def getSurface(self):
        return self._SURFACE

    def getPOS(self):
        return self.__POS

    def isCollision(self, SCREEN: pygame.Surface, POS):
        """
        Testing whether the current sprite position is overlapping the given sprite's position.
        :param SCREEN: object -> Surface
        :param POS: tuple -> int
        :return: Bool
        """
        WIDTH = SCREEN.get_width()
        HEIGHT = SCREEN.get_height()
        X = POS[0]
        Y = POS[1]
        if X - self.__WIDTH <= self.__X <= X + WIDTH:
            if Y - self.__HEIGHT <= self.__Y <= Y + HEIGHT:
                return True
        return False

    def getWidth(self):
        return self._SURFACE.get_width()

    def getHeight(self):
        return self._SURFACE.get_height()

    def getX(self):
        return self.__X

    def getY(self):
        return self.__Y