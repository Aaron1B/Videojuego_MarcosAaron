import pygame
from player import Player
from opponent import Opponent
from shot import Shot

class Game:
    def __init__(self):
        self.player = Player(100, 100, "player.png")
        self.opponents = []
        self.shoots = []
        self.score = 0
        self.is_running = True

    def start(self):
        for i in range(5):
            self.opponents.append(Opponent(i * 50, 0, "enemy.png"))