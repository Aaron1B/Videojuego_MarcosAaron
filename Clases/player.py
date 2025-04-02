from character import Character
import pygame

class Player(Character):
    def __init__(self, x, y, image):
        super().__init__(x, y, image, lives=3)
        self.score = 0
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def shoot(self):
        pass