import pygame
from pygame.sprite import Sprite


class Blue_bird(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load(
            "challenges/blue_bird_flying/images/bird_small.bmp"
        )
        self.rect = self.image.get_rect()

        self.rect.midleft = self.screen_rect.midleft

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_up = False
        self.moving_right = False
        self.moving_left = False
        self.moving_down = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.bird_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.bird_speed
        self.rect.x = self.x

        if self.moving_up and self.rect.y > 0:
            self.y -= self.settings.bird_speed
        if self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
            self.y += self.settings.bird_speed
        self.rect.y = self.y

    def bliteme(self):
        self.screen.blit(self.image, self.rect)

    def center_bird(self):
        self.rect.midleft = self.screen_rect.midleft
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
