import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, FONT_STYLE, DEFAULT_TYPE, CLOCK_TYPE, HAMMER_TYPE

from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.menu import Menu
from dino_runner.components.message import Message
from dino_runner.components.power_ups.power_up_manager import PowerUpManager

class Game:
    
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 2
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.menu = Menu('RUN DINO RUN!!', self.screen)
        self.death_count = 0
        self.score = 0
        self.max_score = 0
        self.highest_score = 0
        self.message = Message()
        self.half_screen_height = SCREEN_HEIGHT // 2
        self.half_screen_width = SCREEN_WIDTH // 2
        self.power_up_manager  = PowerUpManager()

    def execute(self):
        self.running = True
        while self.running:
            self.audio('dino_runner/assets/Other/audio.mp3')
            if not self.playing:
                if self.death_count == 0:
                    self.show_menu()
                elif self.death_count >= 1:
                    self.show_stats()
        pygame.display.quit()
        pygame.quit()


    def run(self):
        self.reset_all()
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.update_score()
        self.obstacle_manager.update(self)
        self.power_up_manager.update(self)

    def draw(self):
        self.clock.tick(FPS)
        if self.score < 700:
            self.screen.fill((128, 128, 128))
        elif self.score > 700:
            self.screen.fill((64, 64, 128))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.draw_score()
        self.draw_power_up_time()
        pygame.display.update()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def show_menu(self):
        self.menu.reset_screen_color(self.screen)
        self.menu.draw(self.screen)
        self.screen.blit(ICON, (self.half_screen_width - 50, self.half_screen_height - 150))
        self.menu.update(self)  
            

    def show_stats(self):
        self.message.reset_screen_color(self.screen)
        self.message.print_message('Game over. Press any key to restart', 530, 290, self.screen)
        self.message.print_message(f'Your score: {self.score}', 530, 370, self.screen)
        self.message.print_message(f'Highest score: {self.max_score}',  530, 420, self.screen)
        self.message.print_message(f'Total deaths: {self.death_count}', 530, 470, self.screen)
        self.screen.blit(ICON, (self.half_screen_width - 50, self.half_screen_height - 150))
        self.message.update(self)

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
        self.power_up_manager.reset()

    def draw_power_up_time(self):
        if self.player.has_power_up:

            time_to_show = round((self.player.power_time_up - pygame.time.get_ticks()) / 1000, 2)

            if time_to_show >= 0:
                if self.player.type == HAMMER_TYPE:
                    self.message.print_message(f'DESTRUCTIVE {self.player.type.upper()} IS ENABLED FOR {time_to_show}', 540, 50, self.screen)
                elif self.player.type == CLOCK_TYPE:
                    self.message.print_message(f'SLOWDOWN CLOCK HAS BEEN ENABLED', 540, 50, self.screen)
                    self.game_speed = 20
            else: 
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE

    def audio(self, route):
        pygame.mixer.init()
        pygame.mixer.music.load(route)
        pygame.mixer.music.play()