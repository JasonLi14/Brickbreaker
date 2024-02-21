# level.py
"""
Name: Level Class
Author: Jason Li
Date-Created: 2024-02-05
"""

from Sprites.box import Box
from brick import Brick
from player_sprite import Player
from top_text import TopText
from random import randrange


class Level:  # This is an aggregate object because it combines box classes
    """
    Level class ==> one class for each level
    """
    def __init__(self, NAME, BRICKS_AMT_X, BRICKS_AMT_Y, SCREEN_WIDTH,
                 LIVES=3, PLAYER_WIDTH=80, BALL_WIDTH=3, BALL_SPEED=5, MAX_BRICK_HEALTH=1):
        """
        Initialize the level object
        :param NAME: string
        :param BRICKS_AMT_X: int
        :param BRICKS_AMT_Y: int
        :param SCREEN_WIDTH: int
        :param LIVES: int
        :param PLAYER_WIDTH: int
        :param BALL_WIDTH: int
        :param BALL_SPEED: int
        :param MAX_BRICK_HEALTH: int
        """
        self.__BRICKS_AMT_X = BRICKS_AMT_X
        self.__BRICKS_AMT_Y = BRICKS_AMT_Y
        self.__BRICKS = []
        self.__LIVES = LIVES
        self.__SCORE = 0
        # --- COMPOSITION --- # ==> The level object is composed of the player object (and some other ones too)
        self.__PLAYER = Player(PLAYER_WIDTH)
        self.__BALL = Box(BALL_WIDTH, BALL_WIDTH)  # More composition
        self.__BALL.setSpeed(BALL_SPEED)
        self.__MAX_BRICK_HEALTH = MAX_BRICK_HEALTH
        self.__SCREEN_WIDTH = SCREEN_WIDTH
        self.__TOP_TEXT = TopText(NAME, self.__SCREEN_WIDTH)
        self.__TOP_TEXT.updateLives(self.__LIVES)  # Show amount of lives
        self.__TOP_TEXT.updateScore(self.__SCORE)
        self.STARTED = False

    # Modifier methods
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
                # --- AGGREGATION --- # ==> aggregating multiple brick objects together.
                BRICK_HEALTH = randrange(1, self.__MAX_BRICK_HEALTH + 1)  # Choose health for bricks
                NEW_BRICK = Brick(BRICK_WIDTH, BRICK_HEIGHT, BRICK_HEALTH)  # Composition ==> Level has brick objects
                # Set their positions and stagger them
                NEW_BRICK.setY((BRICK_HEIGHT + PADDING_Y) * i + MIN_Y)  # General Position
                NEW_BRICK.setColor()
                if i % 2 == 0:  # Displaces every other row by half the brick's width
                    NEW_BRICK.setX((BRICK_WIDTH + PADDING_X) * j + MIN_X + BRICK_WIDTH//4)
                else:  # Ensures close to center
                    NEW_BRICK.setX((BRICK_WIDTH + PADDING_X) * j + MIN_X - BRICK_WIDTH//4)
                self.__BRICKS.append(NEW_BRICK)

    def checkCollisions(self):
        """
        Checks if the ball has collided with any brick.
        :return: int, int (first denotes index of brick that was collided with, -1 denotes none hit,
        second denotes where it was hit
        """
        for i in range(len(self.__BRICKS)):
            COLLIDE = self.__BALL.isCollision(self.__BRICKS[i].getSurface(), self.__BRICKS[i].getPOS())
            if COLLIDE > 0:  # There was a collision
                return i, COLLIDE
        return -1, 0

    def death(self):
        self.__LIVES = self.__LIVES - 1  # reduce lives
        self.__TOP_TEXT.updateLives(self.__LIVES)
        # reset positions
        self.__BALL.setPos(self.__SCREEN_WIDTH // 2 - self.__BALL.getWidth() // 2,
                           self.__PLAYER.getY() - 20)  # set original position
        self.__PLAYER.setX(self.__SCREEN_WIDTH // 2 - self.__PLAYER.getWidth() // 2)

    def addScore(self, AMOUNT):
        self.__SCORE = self.__SCORE + AMOUNT
        self.__TOP_TEXT.updateScore(self.__SCORE)

    # Accessor Methods
    def getBricks(self):
        return self.__BRICKS

    def getPlayer(self):
        return self.__PLAYER

    def getBall(self):
        return self.__BALL

    def getTopText(self):
        return self.__TOP_TEXT

    def getLives(self):
        return self.__LIVES
