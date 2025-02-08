import json
import sys
from pathlib import Path
from time import sleep

import pygame
from blue_bird import Blue_bird

from alien import Alien
from bullet import Bullet
from button import Button
from game_stats import GameStats
from scoreboard import ScoreBoard
from settings import Settings


class Bird_fly:

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("バードフライ")

        self.stats = GameStats(self)
        self.sb = ScoreBoard(self)

        self.bird = Blue_bird(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        self.game_active = False

        self.game_active = False

        self.play_button_normal = Button(self, "Play(normal)", "normal")
        self.play_button_easy = Button(self, "Play(easy)", "easy")
        self.play_button_hard = Button(self, "Play(hard)", "hard")

    def run_game(self):
        while True:
            self._check_events()

            if self.game_active:
                self.bird.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._write_high_score()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        button_clicked_normal = self.play_button_normal.rect.collidepoint(mouse_pos)
        button_clicked_easy = self.play_button_easy.rect.collidepoint(mouse_pos)
        button_clicked_hard = self.play_button_hard.rect.collidepoint(mouse_pos)

        if button_clicked_normal and not self.game_active:
            self.settings.initialize_dynamic_settings("normal")
            self._start_game()
        if button_clicked_easy and not self.game_active:
            self.settings.initialize_dynamic_settings("easy")
            self._start_game()
        if button_clicked_hard and not self.game_active:
            self.settings.initialize_dynamic_settings("hard")
            self._start_game()

    def _write_high_score(self):
        path = Path("challenges/blue_bird_flying/high_score.json")
        contents = path.read_text()
        high_score = json.loads(contents)
        if high_score < self.stats.high_score:
            high_score = json.dumps(self.stats.high_score)
            path.write_text(high_score)

    def _start_game(self):
        self.stats.reset_stats()
        self.game_active = True

        self.bullets.empty()
        self.aliens.empty()

        self._create_fleet()
        self.bird.center_bird()

        pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_UP:
            self.bird.moving_up = True
        elif event.key == pygame.K_RIGHT:
            self.bird.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.bird.moving_left = True
        elif event.key == pygame.K_DOWN:
            self.bird.moving_down = True
        elif event.key == pygame.K_q:
            self._write_high_score()
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_UP:
            self.bird.moving_up = False
        elif event.key == pygame.K_RIGHT:
            self.bird.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.bird.moving_left = False
        elif event.key == pygame.K_DOWN:
            self.bird.moving_down = False

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.settings.screen_width:
                self.bullets.remove(bullet)
                self._check_failed_bullet()

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        self._start_new_level()

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

    def _start_new_level(self):
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.bird.center_bird()
            self.settings.increase_speeed()

    def _check_aliens_bottom(self):
        for alien in self.aliens.sprites():
            if alien.rect.left <= 0:
                self._bird_hit()
                break

    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()

        if pygame.sprite.spritecollideany(self.bird, self.aliens):
            self._bird_hit()

        self._check_aliens_bottom()

    def _bird_hit(self):
        if self.stats.birds_left > 0:
            self.stats.birds_left -= 1
            self.sb.prep_bird()

            self.bullets.empty()
            self.aliens.empty()

            self._create_fleet()
            self.bird.center_bird()
            sleep(0.5)
        else:
            self._stop_game()

    def _check_failed_bullet(self):
        if self.stats.bullets_left > 0:
            self.stats.bullets_left -= 1
        else:
            self._stop_game()

    def _stop_game(self):
        self.game_active = False
        pygame.mouse.set_visible(True)

    def _create_fleet(self):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x = self.settings.screen_width - 2 * alien_width
        current_y = alien_height

        while current_x > (alien_width * 3):
            while current_y < (self.settings.screen_height - 2 * alien_height):
                self._create_alien(current_x, current_y)
                current_y += 2 * alien_height

            current_y = alien_height
            current_x -= 2 * alien_width

    def _create_alien(self, x_position, y_position):
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.y = y_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.x -= self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.bird.bliteme()
        self.aliens.draw(self.screen)

        self.sb.show_score()

        if not self.game_active:
            self.play_button_normal.draw_button()
            self.play_button_easy.draw_button()
            self.play_button_hard.draw_button()

        pygame.display.flip()


if __name__ == "__main__":
    ai = Bird_fly()
    ai.run_game()
