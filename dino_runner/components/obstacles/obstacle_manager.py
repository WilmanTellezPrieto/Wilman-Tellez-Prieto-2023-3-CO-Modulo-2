import pygame
import random

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD

class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        self.step_index = 0

    def generate_obstacle(self, oType, game):
        while game.playing:
            step_index += 1 
        if oType == 0:
          obstacle = Cactus(LARGE_CACTUS)
        elif oType == 1:
          obstacle = Cactus(SMALL_CACTUS)
        elif oType == 2:
          obstacle = Bird(BIRD[0])

        return obstacle

    def update(self, game):
        if len(self.obstacles) == 0:
            oType = random.randint(0,2)
            obstacle = self.generate_obstacle(oType)
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