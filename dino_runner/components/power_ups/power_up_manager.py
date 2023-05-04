import pygame
import random

from dino_runner.components.power_ups.hammer import Hammer
from dino_runner.components.power_ups.clock import Clock

class PowerUpManager:

    def __init__(self):
        self.power_ups = []
        self.when_appears = random.randint(100, 200)
        self.duration = random.randint(3, 5)
        self.power_up = ""

    
    def generate_power_up(self, power_up_type):
        if power_up_type == 0:
            self.power_up = Hammer()
            self.when_appears += random.randint(100,200)
            self.power_ups.append(self.power_up)
        elif power_up_type == 1:
            self.power_up = Clock()
            self.when_appears += random.randint(100,200)
            self.power_ups.append(self.power_up)


    def update(self, game): 
              
        if len(self.power_ups) == 0 and self.when_appears == game.score:
            power_up_type = random.randint(0,1)
            self.generate_power_up(power_up_type)
    
        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if game.player.dino_rect.colliderect(power_up):
                power_up.start_time = pygame.time.get_ticks()
                game.player.type = power_up.type
                game.player.has_power_up = True
                game.player.power_time_up = power_up.start_time + (self.duration * 1000)
                self.power_ups.remove(power_up)
            

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset(self):
        self.power_ups = []
        self.when_appears = random.randint(100, 200)