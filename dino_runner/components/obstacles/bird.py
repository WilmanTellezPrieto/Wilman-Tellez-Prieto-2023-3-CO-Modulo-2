import random
import pygame
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD


class Bird(Obstacle):
    BIRD_HEIGHTS = [320, 260, 230]

    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = self.BIRD_HEIGHTS[random.randint(0, 2)]
        self.index = 0

    def draw(self, screen):
        self.index += 1
        if self.index >= 10:
            self.index = 0

        screen.blit(BIRD[self.index // 5], self.rect)