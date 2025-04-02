from entity import Entity
class shot(Entity):
    def __init__(self,x,y,direction,image):
        super().__init__(x,y,image)
        self.direction = direction

    def move(self):
        if self.direction == "up":
            self.y -= 5
        elif self.direction == "down":
            self.y += 5
        elif self.direction == "left":
            self.x -= 5
        elif self.direction == "right":
            self.x += 5

        def hit_target(self,target):
            if self.x == target.x and self.y == target.y:
                return True
            return False
