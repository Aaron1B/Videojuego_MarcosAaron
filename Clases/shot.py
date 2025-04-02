from entity import Entity

class Shot(Entity):
    def __init__(self, x, y, direction, image):
        super().__init__(x, y, image)
        self.direction = direction

    def move(self):
        if self.direction == "up":
            self.y -= 5
        elif self.direction == "down":
            self.y += 5

    def hit_target(self, target):
        return (self.x < target.x + 50 and 
                self.x + 10 > target.x and 
                self.y < target.y + 50 and 
                self.y + 10 > target.y)
                
