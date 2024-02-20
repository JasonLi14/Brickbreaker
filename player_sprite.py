# player_sprite.py in f_santa
"""
Title: Composite Player Sprite
Author: Jason Li
Date-Created: 2024-01-17
"""

import pygame
from Sprites.box import Box
from window import Window


class Player(Box):
    def __init__(self, WIDTH=10, HEIGHT=10):
        Box.__init__(self, WIDTH, HEIGHT, 10)

    # --- MODIFIER METHODS --- #
    def ADMove(self, KEY_PRESSES):
        """
        Moves the sprite left and right
        :param KEY_PRESSES: list(int)
        :return: None
        """
        if KEY_PRESSES[pygame.K_d]:
            self.setDirX(True)
            self.marqueeX()
        if KEY_PRESSES[pygame.K_a]:
            self.setDirX(False)
            self.marqueeX()


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
