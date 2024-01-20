import pygame
from pygame.transform import scale
import math


class mymia(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(f"image/Мумия.png")
        self.original_image = pygame.image.load(f"image/Мумия.png")
        self.rect = pygame.Rect(x, y, 150, 150)
        self.xvel = 0
        self.yvel = 0
        self.life = 5

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self, rectplayer):
        if rectplayer.y < self.rect.y:
            self.yvel -= 1
        if rectplayer.y > self.rect.y:
            self.yvel += 1
        if rectplayer.x < self.rect.x:
            self.xvel -= 1
        if rectplayer.x > self.rect.x:
            self.xvel += 1
        self.rect.x += self.xvel
        self.rect.y += self.yvel
        self.yvel = 0
        self.xvel = 0
        mouse_x, mouse_y = rectplayer.center
        rel_x, rel_y = mouse_x - self.rect.x, mouse_y - self.rect.y
        angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
        self.image = pygame.transform.rotate(self.original_image, int(angle))
        self.rect = self.image.get_rect(center=self.rect.center)
