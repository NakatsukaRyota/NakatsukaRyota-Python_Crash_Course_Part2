import json
from pathlib import Path


class GameStats:

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.read_high_score()
        self.reset_stats()

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def read_high_score(self):
        path = Path("high_score.json")
        contents = path.read_text()
        self.high_score = json.loads(contents)
