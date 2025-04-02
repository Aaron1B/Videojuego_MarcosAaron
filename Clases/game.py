import pygame
from player import Player
from opponent import Opponent


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Mi juego")
        self.clock = pygame.time.Clock()

        self.player = Player(100, 100, "player.png")
        self.opponents = []
        self.shoots = []
        self.score = 0
        self.is_running = True

    def start(self):
        for i in range(5):
            self.opponents.append(Opponent(i * 50, 0, "enemy.png"))

    def update(self):
        for opponent in self.opponents:
            opponent.move()

        for shot in self.shoots:
            shot.move()

        self.check_collisions()


    def check_collisions(self):
        for shot in self.shoots:
            for opponent in self.opponents:
                if shot.hit_target(opponent):
                    self.score +=10
                    opponent.convert_to_star()
                    self.shoots.remove(shot)

    def end_game(self):
        print("Game Over ! Tu puntuacion es :", self.score)
        self.is_running = False

    def run(self):
        self.start()
        while self.is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
            
            self.update()
            self.clock.tick(30)

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()