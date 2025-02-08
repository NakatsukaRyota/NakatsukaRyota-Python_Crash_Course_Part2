import pygame
from pygame.sprite import Sprite


class Alien(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.image = pygame.image.load("challenges/blue_bird_flying/images/alien.bmp")
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def check_edges(self):
        return (self.rect.top <= 0) or (self.rect.bottom >= self.settings.screen_height)

    def update(self):
        self.y += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.y = self.y
