# basic_sprite.py in e_inheritance

"""
Title: The Parent Class
Author: Jason Li
Date Created: 2023-12-22
"""
import pygame


class BasicSprite:

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

    def setSpeed(self, SPEED):  # Changes speed
        self.__SPEED = SPEED

    def setX(self, X):  # Public Methods
        self.__X = X
        self.__POS = (self.__X, self.__Y)

    def setY(self, Y):
        self.__Y = Y
        self.__POS = (self.__X, self.__Y)

    def setPos(self, X, Y):
        self.setX(X)
        self.setY(Y)

    def marqueeX(self):
        self.__X = self.__X + self.__SPEED * self.__DIR_X
        self.__POS = (self.__X, self.__Y)

    def marqueeY(self):
        self.__Y = self.__Y + self.__SPEED * self.__DIR_Y

    def setDirX(self, GO_RIGHT):
        """
        Set self.__DirX positive if GO_RIGHT is true, negative if false.
        :param GO_RIGHT: bool
        :return: None
        """
        if GO_RIGHT:
            self.__DIR_X = 1
        else:
            self.__DIR_X = -1

    def setDirY(self, GO_DOWN):
        """
        Set self.__DirX positive if GO_RIGHT is true, negative if false.
        :param GO_DOWN: bool
        :return: None
        """
        if GO_DOWN:
            self.__DIR_Y = 1
        else:
            self.__DIR_Y = -1

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

    def collisionBump(self, SIDE):
        """
        Change direction of Y and X depending on the side hit
        :param SIDE: 1, 2, 3 or 4
        :return: None
        """
        if SIDE == 1 or SIDE == 3:  # Top or bottom
            self.__DIR_Y = -1 * self.__DIR_Y
        if SIDE == 2 or SIDE == 4:  # Top or bottom
            self.__DIR_X = -1 * self.__DIR_X

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
        :return: int  get the side that it has collided. 1 = top, 2 = left, 3 = bottom, 4 = right,
        0 = no collide
        """
        WIDTH = SCREEN.get_width()
        HEIGHT = SCREEN.get_height()
        X = POS[0]
        Y = POS[1]
        if X - self.__WIDTH <= self.__X <= X + WIDTH:
            if Y - self.__HEIGHT <= self.__Y <= Y + HEIGHT:
                # find the edge
                # Create a list of size 4. This just lets me not have to use big if statements.
                SIDE_DIST = [0, 0, 0, 0]
                SIDE_DIST[0] = abs(Y - self.__Y)
                SIDE_DIST[1] = abs(self.__Y + self.__HEIGHT - self.__Y - HEIGHT)
                SIDE_DIST[2] = abs(X - self.__X)
                SIDE_DIST[3] = abs(self.__X + self.__WIDTH - self.__X - WIDTH)
                # Use for loop to iterate over SIDE_DIST and find the smallest value's index
                MIN_DIST = 1000000000
                MIN_INDEX = -1
                # find the minimum and return the corresponding side
                for i in range(len(SIDE_DIST)):
                    if SIDE_DIST[i] < MIN_DIST:
                        MIN_DIST = SIDE_DIST[i]
                        MIN_INDEX = i
                return MIN_INDEX + 1
        return 0

    def getWidth(self):
        return self._SURFACE.get_width()

    def getHeight(self):
        return self._SURFACE.get_height()

    def getX(self):
        return self.__X

    def getY(self):
        return self.__Y

    def getSpeed(self):
        return self.__SPEED
