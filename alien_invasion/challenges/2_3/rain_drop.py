import sys
import pygame

from settings import Settings
from rain import Rain

class StarLight:

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("雨")

        self.rains = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()
            self._update_rains()
            self.clock.tick(60)
    
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _create_fleet(self):
        rain = Rain(self)
        rain_width, rain_height = rain.rect.size

        current_x, current_y = rain_width, rain_height
        while current_y < (self.settings.screen_height - 3 * rain_height):
            while current_x < (self.settings.screen_width - 2 * rain_width):
                self._create_rain(current_x, current_y)
                current_x += 2 * rain_width
            current_x = rain_width * 2
            current_y += 2 * rain_height
            while current_x < (self.settings.screen_width - 2 * rain_width):
                self._create_rain(current_x, current_y)
                current_x += 2 * rain_width
            current_x = rain_width
            current_y += 2 * rain_height
    
    def _create_rain(self, x_position, y_position):
        new_rain = Rain(self)
        new_rain.x = x_position
        new_rain.y = y_position
        new_rain.rect.x = x_position
        new_rain.rect.y = y_position
        self.rains.add(new_rain)

    def _update_rains(self):
        self.rains.update()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.rains.draw(self.screen)

        pygame.display.flip()

if __name__ == "__main__":
    ai = StarLight()
    ai.run_game()
