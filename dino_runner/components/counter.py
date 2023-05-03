import pygame

from dino_runner.utils.constants import FONT_STYLE

class Counter():

    def __init__(self):
        self.score = 0
        self.max_score = 0
        self.highest_score = 0
    
    def update_score(self):
        self.score += 1

        if self.score % 100 == 0 and self.game_speed < 200:
            self.game_speed += 5
        
        if self.score > self.max_score:
            self.max_score = self.score

    def draw_score(self):
        font = pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f'Score {self.score}', True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (1000, 40)
        self.screen.blit(text, text_rect)

    def reset_all(self):
        self.obstacle_manager.reset()
        self.score = 0
        self.game_speed = 20
        self.player.reset()
        self.x_pos_bg = 0