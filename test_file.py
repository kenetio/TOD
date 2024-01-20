import pygame.sprite
import math

class bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, angle):
        super().__init__()

        self.image = pygame.image.load(f"image/Пуля.png")
        self.rect = pygame.Rect(x, y, 6, 2)
        self.xvel = 0
        self.yvel = 0
        self.angle = angle
        self.image = pygame.transform.rotate(self.image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)


    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        degrees = math.radians(self.angle)
        self.xvel += math.cos(degrees)
        self.yvel += math.sin(degrees)
        self.rect.x += self.xvel
        self.rect.y += self.yvel

    def check(self, bullets):
        for bullet in bullets:
            if self.rect.colliderect(bullet.rect):
                return True
            else:
                return False