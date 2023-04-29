import pygame

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS

class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def generate_obstacle(self):
        #if type == 0: 
         #obstacle = Bird()
        #elif type == 1:
        obstacle = Cactus(SMALL_CACTUS)
        return obstacle

    def update(self, game):
        if len(self.obstacles) == 0:
            #otype = random.randInt(0,2)
            obstacle = self.generate_obstacle()
            self.obstacles.append(obstacle)

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                game.playing = False
                pygame.time.delay(2000)
                break
            
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    