import random

from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS

class Cactus(Obstacle):
    def __init__(self, image):
        
        if image == SMALL_CACTUS:
            self.type = random.randint(0,2)
            super().__init__(image, self.type)
            self.rect.y = 325
        elif image == LARGE_CACTUS:
            self.type = random.randint(0,2)
            super().__init__(image, self.type)
            self.rect.y = 300