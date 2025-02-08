import sys
import pygame

from settings import Settings
from star import Star
from random import randint

class StarLight:

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("星空")

        self.stars = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)
    
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _create_fleet(self):
        star = Star(self)
        star_width, star_height = star.rect.size

        current_x, current_y = star_width, star_height
        while current_y < (self.settings.screen_height - 3 * star_height):
            while current_x < (self.settings.screen_width - 2 * star_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * star_width
            current_x = star_width * 2
            current_y += 2 * star_height
            while current_x < (self.settings.screen_width - 2 * star_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * star_width
            current_x = star_width
            current_y += 2 * star_height
    
    def _create_alien(self, x_position, y_position):
        new_alien = Star(self)
        new_alien.x = x_position
        random_number_x = randint(-10, 10)
        random_number_y = randint(-10, 10)
        new_alien.rect.x = x_position + random_number_x
        new_alien.rect.y = y_position + random_number_y
        self.stars.add(new_alien)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.stars.draw(self.screen)

        pygame.display.flip()

if __name__ == "__main__":
    ai = StarLight()
    ai.run_game()
