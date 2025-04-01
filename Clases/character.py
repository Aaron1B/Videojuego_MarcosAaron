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
        """Handle collision with another entity."""
        if self.rect.colliderect(other.rect):  # Asumo que vas a usar rects para colisiones
            self.lives -= 1
            if self.lives <= 0:
                self.is_alive = False
