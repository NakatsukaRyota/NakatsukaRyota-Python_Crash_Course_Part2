class Settings:

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        self.bird_limit = 3

        self.bullet_width = 15
        self.bullet_height = 300
        self.bullet_color = (0, 0, 0)
        self.bullet_allowed = 3
        self.bullet_limit = 2

        self.fleet_drop_speed = 10

        self.speedup_scale = 1.1
        self.score_scale = 1.5

    def initialize_dynamic_settings(self, difficulty):
        if difficulty == "normal":
            self.bird_speed = 1.5
            self.bullet_speed = 2.5
            self.alien_speed = 1.0
            self.alien_points = 50
        if difficulty == "easy":
            self.bird_speed = 1.3
            self.bullet_speed = 2.3
            self.alien_speed = 0.8
            self.alien_points = 40
        if difficulty == "hard":
            self.bird_speed = 1.7
            self.bullet_speed = 2.7
            self.alien_speed = 1.2
            self.alien_points = 60

        self.fleet_direction = 1

    def increase_speeed(self):
        self.bird_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
