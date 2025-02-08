import pygame.font


class Button:

    def __init__(self, ai_game, msg, difficulty):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 250, 50
        self.button_color = (0, 135, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self._check_difficulty(difficulty)

        self._prep_msg(msg)

    def _check_difficulty(self, difficulty):
        if difficulty == "normal":
            self.rect.center = self.screen_rect.center
        if difficulty == "easy":
            self.rect.midtop = self.screen_rect.midtop
        if difficulty == "hard":
            self.rect.midbottom = self.screen_rect.midbottom

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
