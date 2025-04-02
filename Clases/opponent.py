from character import Character
from shot import Shot

class Opponent(Character):
    def __init__(self,x,y,image):
        super().__init__(x,y,image,lives=1)
        self.is_star= False
    
    def move(self):
        self.y += 5

    def shoot(self):
        return Shot(self.x, self.y, "down", "shot_enemy.png")
    
    def convert_star(self):
        self.is_star = True