import pygame.font
from gun import Gun
from pygame.sprite import Group

class Scores():
    def __init__(self, screen, stats):
        """score count"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (65, 200, 50)
        self.font = pygame.font.SysFont(None, 36)
        self.image_score()
        self.image_player_name()
        self.image_guns()

    def image_score(self):
        """score in graphic"""
        self.score_img = self.font.render(str(self.stats.score), True, self.text_color, (0, 0, 0))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 40
        self.score_rect.top = 20

    def image_player_name(self):
        """player_name in graphic"""
        self.player_name_image = self.font.render(str(self.stats.player_name), True, self.text_color, (0, 0, 0))
        self.player_name_rect = self.player_name_image.get_rect()
        self.player_name_rect.centerx = self.screen_rect.centerx
        self.player_name_rect.top = self.screen_rect.top + 20

    def image_guns(self):
        """lives count"""
        self.guns = Group()
        for gun_number in range(self.stats.guns_left):
            gun = Gun(self.screen)
            gun.rect.x = 15 + gun_number * gun.rect.width
            gun.rect.y = 20
            self.guns.add(gun)

    def show_score(self):
        """display scores on the screen"""
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.player_name_image, self.player_name_rect)
        self.guns.draw(self.screen)
