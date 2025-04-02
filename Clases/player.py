from character import Character
from shot import Shot  
import pygame

class Player(Character):
    def __init__(self, x, y, image):
        super().__init__(x, y, image, lives=3)
        self.score = 0  
    
    def move(self, dx, dy):
        super().move(dx, dy)  

    def shoot(self):
        return Shot(self.x + 25, self.y, "up", "shot.png")