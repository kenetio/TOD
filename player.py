import pygame.sprite
import math


class Player(pygame.sprite.Sprite):
    def __init__(self, coords):
        super().__init__()
        self.image = pygame.image.load(f"image/Игрок с пистолетомxdxd.png")
        self.original_image = self.image
        self.collideimage = pygame.image.load(f"image/collideplayer.png")
        self.rect = self.image.get_rect()
        self.colliderect = self.collideimage.get_rect()
        x, y = coords
        self.rect.topleft = (x, y)
        self.colliderect.topleft = (x+28, y+28)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self, u, d, l, r, walls):
        if u:
            self.rect.y += 3
            self.colliderect.y += 3
            for i in walls:
                if self.colliderect.colliderect(i):
                    self.rect.y -= 5
                    self.colliderect.y -= 5
        if d:
            self.rect.y -= 3
            self.colliderect.y -= 3
            for i in walls:
                if self.colliderect.colliderect(i):
                    self.rect.y += 5
                    self.colliderect.y += 5
        if l:
            self.rect.x -= 3
            self.colliderect.x -= 3
            for i in walls:
                if self.colliderect.colliderect(i):
                    self.rect.x += 5
                    self.colliderect.x += 5
        if r:
            self.rect.x += 3
            self.colliderect.x += 3
            for i in walls:
                if self.colliderect.colliderect(i):
                    self.rect.x -= 5
                    self.colliderect.x -= 5

        mouse_x, mouse_y = pygame.mouse.get_pos()
        rel_x, rel_y = mouse_x - self.rect.x, mouse_y - self.rect.y
        angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)

        self.image = pygame.transform.rotate(self.original_image, int(angle))
        self.rect = self.image.get_rect(center=self.rect.center)





