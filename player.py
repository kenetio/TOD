import pygame.sprite
import math


class Player(pygame.sprite.Sprite):
    def __init__(self, coords):
        super().__init__()
        self.image = pygame.image.load(f"image/Игрок с пистолетомxdxd.png")
        self.original_image = self.image
        self.rect = self.image.get_rect()
        self.rect.topleft = coords

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self, u, d, l, r):
        if u:
            self.rect.y += 3
        if d:
            self.rect.y -= 3
        if l:
            self.rect.x -= 3
        if r:
            self.rect.x += 3
        mouse_x, mouse_y = pygame.mouse.get_pos()
        rel_x, rel_y = mouse_x - self.rect.x, mouse_y - self.rect.y
        angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
        self.image = pygame.transform.rotate(self.original_image, int(angle))
        self.rect = self.image.get_rect(center=self.rect.center)
