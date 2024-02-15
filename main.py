# main.py
"""
Name: Brick-Breaker
Author: Jason Li
Date-Created: 2024-02-05
"""

import pygame
from window import Window
from level import Level
from Sprites.text import Text


if __name__ == "__main__":  # just a test
    pygame.init()
    WINDOW = Window("Brick-Breaker", COLOR=(30, 30, 30))
    LEVEL = Level("Level 1", 10, 6, WINDOW.getWidth(), 3, 100, 5, 3)
    LEVEL.setup(WINDOW.getWidth() - 100, 300, 100, 100, 5, 5)
    LEVEL.getPlayer().setPos((WINDOW.getWidth() - 100)//2, WINDOW.getHeight() - 50)
    BRICKS = LEVEL.getBricks()

    START_TEXT = Text("Press SPACE to start", 20)
    START_TEXT.setPos(WINDOW.getWidth()//2 - START_TEXT.getWidth()//2,
                      LEVEL.getPlayer().getY() - 3 * START_TEXT.getHeight())

    # Set ball position
    LEVEL.getBall().setPos(WINDOW.getWidth()//2 - LEVEL.getBall().getWidth()//2,
                           LEVEL.getPlayer().getY() - 10)

    while True:  # Main game play
        # INPUT (getting player movements)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        PRESSED_KEYS = pygame.key.get_pressed()

        # Wait until the space key is pressed
        if not LEVEL.STARTED:
            # Detect if space key is pressed
            if PRESSED_KEYS[pygame.K_SPACE]:
                LEVEL.STARTED = True
        else:
            # PROCESSING
            # Moving the player
            LEVEL.getPlayer().ADMove(PRESSED_KEYS)
            LEVEL.getPlayer().wrapX(WINDOW.getWidth())

            # Moving the Ball
            LEVEL.getBall().marqueeX()
            LEVEL.getBall().marqueeY()
            LEVEL.getBall().bounceX(WINDOW.getWidth())

            # Check if ball is out of bounds, then bounce Y
            if LEVEL.getBall().getY() > WINDOW.getHeight() - LEVEL.getBall().getHeight() - 3:
                # A life is lost ==> reset positions
                LEVEL.death()
                LEVEL.STARTED = False
            else:
                LEVEL.getBall().bounceY(WINDOW.getHeight(), LEVEL.getTopText().getHeight())
                # Enable to bounce on the top edge right under the top text

            # Checking for collisions with the paddle
            BALL_PLAYER_COLLIDE = LEVEL.getBall().isCollision(LEVEL.getPlayer().getSurface(),
                                                              LEVEL.getPlayer().getPOS())
            if BALL_PLAYER_COLLIDE != 0:
                LEVEL.getBall().collisionBump(BALL_PLAYER_COLLIDE)

            # Checking for collisions with bricks
            COLLIDED_BRICK, COLLIDED_SIDE = LEVEL.checkCollisions()
            if COLLIDED_BRICK != -1:
                BRICKS.pop(COLLIDED_BRICK)  # Remove that brick
                LEVEL.getBall().collisionBump(COLLIDED_SIDE)

        # OUTPUT (rendering game)
        WINDOW.clearScreen()
        # Bricks
        for BRICK in BRICKS:
            WINDOW.getSurface().blit(BRICK.getSurface(), BRICK.getPOS())
        # Player
        WINDOW.getSurface().blit(LEVEL.getPlayer().getSurface(), LEVEL.getPlayer().getPOS())
        # Ball
        WINDOW.getSurface().blit(LEVEL.getBall().getSurface(), LEVEL.getBall().getPOS())
        # Top Bit
        LEVEL.getTopText().blitOnWindow(WINDOW)
        # Space prompt
        if not LEVEL.STARTED:
            WINDOW.getSurface().blit(START_TEXT.getSurface(), START_TEXT.getPOS())

        WINDOW.updateFrame()
