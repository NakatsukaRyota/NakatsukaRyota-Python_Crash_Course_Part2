import pygame
from pygame.sprite import Sprite

class Rain(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.image = pygame.image.load("challenges/2_3/images/raindrop.png")
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        self.y += self.settings.rain_drop_speed
        if self.rect.top >= self.settings.screen_height:
            self.y = 0
        self.rect.y = self.y
        