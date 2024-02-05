"""
Title: Collision Text Sprite
Author: Jason
Date Created: 2024-01-11
"""
from window import Window
from box import Box
import pygame
from random import randint


if __name__ == "__main__":
    pygame.init()
    WINDOW = Window("Collision Text", COLOR=(15, 40, 28))

    PLAYER_BOX = Box(50, 50)
    PLAYER_BOX.setColor((255, 29, 142))
    PLAYER_BOX.setPos(WINDOW.getWidth() - PLAYER_BOX.getWidth(),
                      WINDOW.getHeight() - PLAYER_BOX.getHeight())  # get rand position
    BOT_BOX = Box(60, 60)
    BOT_BOX.setColor((114, 137, 218))
    BOT_BOX.setPos(0, 0)
    """
    R = 255
    G = 0
    B = 0
    """
    while True:
        """
        if R == 255 and B == 0 and G < 255:
            G += 5
        elif G == 255 and R != 0:
            R -= 5
        elif G == 255 and R == 0 and  B < 255:
            B += 5
        elif B == 255 and G != 0:
            G -= 5
        elif B == 255 and G == 0 and R < 255:
            R += 5
        elif R == 255 and B != 0:
            B -= 5
        """

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # Move player box
        PRESSED_KEYS = pygame.key.get_pressed()
        PLAYER_BOX.WASDmove(PRESSED_KEYS)
        PLAYER_BOX.wrapX(WINDOW.getWidth())
        PLAYER_BOX.wrapY(WINDOW.getHeight())

        # Move bot box
        # BOT_BOX.marqueeX()
        # BOT_BOX.marqueeY()
        # BOT_BOX.bounceX(WINDOW.getWidth())
        # BOT_BOX.bounceY(WINDOW.getHeight())

        # Check for collisions
        if PLAYER_BOX.isCollision(BOT_BOX.getSurface(), BOT_BOX.getPOS()):
            print("HIT")
            # PLAYER_BOX.setPos(randint(0, WINDOW.getWidth()), randint(0, WINDOW.getHeight()))

        # Window stuff
        WINDOW.clearScreen()
        WINDOW.getSurface().blit(PLAYER_BOX.getSurface(), PLAYER_BOX.getPOS())
        WINDOW.getSurface().blit(BOT_BOX.getSurface(), BOT_BOX.getPOS())
        WINDOW.updateFrame()

