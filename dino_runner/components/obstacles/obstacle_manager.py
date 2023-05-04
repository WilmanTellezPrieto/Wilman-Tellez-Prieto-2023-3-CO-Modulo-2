import pygame
import random

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import BIRD, HAMMER_TYPE

class ObstacleManager:
  def __init__(self):
    self.obstacles = []
    
  def generate_obstacle(self, obstacle_type):
    if obstacle_type == 0:
      cactus_type = 'SMALL'
      obstacle = Cactus(cactus_type)
    elif obstacle_type == 1:
      cactus_type = 'LARGE'
      obstacle = Cactus(cactus_type)
    else:
      obstacle = Bird(BIRD)
    return obstacle

  def update(self, game):
      if len(self.obstacles) == 0:
          obstacle_type = random.randint(0,2)
          obstacle = self.generate_obstacle(obstacle_type)
          self.obstacles.append(obstacle)

      for obstacle in self.obstacles:
          obstacle.update(game.game_speed, self.obstacles)
          if game.player.dino_rect.colliderect(obstacle.rect):
              if game.player.type == HAMMER_TYPE:
                self.obstacles.remove(obstacle)
                pass
              else: 
                game.playing = False
                pygame.time.delay(2000)
                game.death_count += 1
                pygame.mixer.init()
                pygame.mixer.music.load("dino_runner/assets/Other/died.mp3")
                pygame.mixer.music.play()
                break
     
  def draw(self, screen):
    for obstacle in self.obstacles:
        obstacle.draw(screen)

  def reset(self):
    self.obstacles = [] 