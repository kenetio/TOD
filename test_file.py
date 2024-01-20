import pygame.sprite
import math

class bullet(pygame.sprite.Sprite):
    def _init_(self, x, y):
        pygame.sprite.Sprite._init_(self)

        self.image = pygame.image.load("Пуля.png")
        self.rect = pygame.Rect(x, y, 6, 2)
        self.xvel = 0
        self.yvel = 0
    def draw(self, surface, degrees):
        surface.blit(self.image, self.rect)

    def update(self, degrees):
        degrees = math.radians(degrees)
        self.xvel += math.cos(degrees)
        self.yvel += math.sin(degrees)
        self.rect.x += self.xvel
        self.rect.y += self.yvel