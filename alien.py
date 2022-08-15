import pygame
from random import randint

class Alien(pygame.sprite.Sprite):

    def __init__(self, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.image = pygame.image.load(f'images/alien{randint(0, 5)}.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        """display alien on the screen"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """movement alien"""
        self.y += 0.05
        self.rect.y = self.y
