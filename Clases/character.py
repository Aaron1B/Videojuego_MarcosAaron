from entity import Entity  # Importar la clase Entity

class Character(Entity):
    def __init__(self, x, y, image, lives=3):
        super().__init__(x, y, image)
        self.lives = lives
        self.is_alive = True

    def move(self, dx, dy):
        """Mueve el personaje por dx y dy."""
        self.x += dx
        self.y += dy

    def shoot(self):
        """Dispara un proyectil desde la posición actual."""
        from shot import Shot 
        return Shot(self.x + 25, self.y, "shot.png")

    def collide(self, other):
        """Verifica si hay colisión con otro objeto."""
        return (self.x < other.x + 50 and 
                self.x + 50 > other.x and 
                self.y < other.y + 50 and 
                self.y + 50 > other.y)