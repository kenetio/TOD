import pygame.sprite
from random import randint

class blood(pygame.sprite.Sprite):
    def __init__(self, coords):
        super().__init__()
        if randint(1, 2) == 1:
            self.image = pygame.image.load(f"image/blood2.png")
        else:
            self.image = pygame.image.load(f"image/blood1.png")

        self.rect = self.image.get_rect()
        self.rect.topleft = coords

    def draw(self, surface):
        surface.blit(self.image, self.rect)

