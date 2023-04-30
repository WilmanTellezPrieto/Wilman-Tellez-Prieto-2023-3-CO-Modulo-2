import random
import pygame
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD


class Bird(Obstacle):
    def __init__(self, image):
        super().__init__(image, 0)
        self.rect.y = random.choice((320, 260, 230))        