from entity import Entity  # Importar la clase Entity

class Character(Entity):
    def __init__(self, x, y, image, lives=3):
        super().__init__(x, y, image)
        self.lives = lives
        self.is_alive = True

    def move(self, dx, dy):
        """Move the character by dx and dy."""
        super().move(dx, dy)

    def shoot(self):
        """Shoot a bullet."""
        pass  # Implementar más adelante

    def collide(self, other):
        if self.x == other.x and self.y == other.y: # Verifico si el personaje ha chocado con otro
            return True
        return False 
